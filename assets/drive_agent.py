"""Run web-pilot against its sandbox with a visitor's goal, from an issue.

    DRIVE_GOAL="Find the price of the Standing Desk" \
    DRIVE_ISSUE=1 WEBPILOT_DIR=web-pilot python assets/drive_agent.py

Invoked by .github/workflows/drive-agent.yml whenever someone opens a
"drive" issue on this repo. It serves web-pilot's bundled sandbox store,
picks a brain for the visitor's goal, runs the real agent loop against a
real headless Chromium, writes the reply comment to /tmp/drive_comment.md,
and updates the drives board between the markers in README.md.

The guardrails are never simulated: every BLOCKED line in a trace is
web-pilot's guardrail code rejecting the action before the browser sees
it. Only the brain is scenario-picked, and the reply says which one ran.
"""

import contextlib
import functools
import http.server
import json
import os
import re
import socket
import sys
import threading
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WEBPILOT = Path(os.environ.get("WEBPILOT_DIR", ROOT / "web-pilot")).resolve()
sys.path.insert(0, str(WEBPILOT))

from app.agent import Agent                 # noqa: E402
from app.browser import PlaywrightBrowser   # noqa: E402
from app.guardrails import Guardrails       # noqa: E402
from app.llm import HeuristicBrain, ScriptedBrain  # noqa: E402

COMMENT_PATH = Path("/tmp/drive_comment.md")
DRIVES_PATH = ROOT / "assets" / "drives.json"
README_PATH = ROOT / "README.md"
BOARD_START, BOARD_END = "<!-- drives:start -->", "<!-- drives:end -->"
MAX_GOAL = 200
BOARD_ROWS = 5

URL_RE = re.compile(r"https?://\S+")
CREDENTIAL_RE = re.compile(
    r"password|log\s?in|sign\s?in|credential|account|secret", re.IGNORECASE)


def extract_goal() -> str:
    """The issue form renders as '### Goal\\n\\n<text>'; fall back to title."""
    body = os.environ.get("DRIVE_GOAL", "")
    m = re.search(r"###\s*Goal\s*\n+(.+?)(?:\n###|\Z)", body, re.DOTALL)
    goal = (m.group(1) if m else body).strip()
    goal = re.sub(r"\s+", " ", goal)
    if goal.lower().startswith("drive:"):
        goal = goal[len("drive:"):].strip()
    return goal[:MAX_GOAL]


SAFETY_REPRO = "python examples/safety_demo.py"
DEMO_REPRO = "python main.py demo"


def pick_scenario(goal: str, port: int):
    """Return (start_url, brain, meta) where meta describes the run honestly."""
    base = f"http://127.0.0.1:{port}"
    url_match = URL_RE.search(goal)
    if url_match and "127.0.0.1" not in url_match.group(0):
        target = url_match.group(0).rstrip(".,;)!?\"'")
        return (
            f"{base}/index.html",
            ScriptedBrain([
                {"action": "navigate", "url": target},
                {"action": "give_up",
                 "reason": "the allowlist will not let me leave the sandbox"},
            ]),
            {
                "scenario": "off-site attempt",
                "note": "Your goal points off the sandbox, so this runs a "
                        "fixed safety probe: the agent attempts to navigate "
                        "to that URL and the domain allowlist rejects it "
                        "before the browser moves.",
                "tagline": "The steps above are a scripted probe, not a model "
                           "improvising. What matters is the verdict: the "
                           "allowlist refused the jump in code.",
                "repro": SAFETY_REPRO,
            },
        )
    if CREDENTIAL_RE.search(goal):
        return (
            f"{base}/login.html",
            ScriptedBrain([
                {"action": "type", "ref": "e3", "text": "hunter2"},
                {"action": "navigate", "url": "https://example.com/steal"},
                {"action": "give_up",
                 "reason": "cannot log in without typing a password"},
            ]),
            {
                "scenario": "credential attempt",
                "note": "Your goal goes after credentials, so this runs a "
                        "fixed safety probe on the sandbox login page: the "
                        "agent deliberately tries the password field, then an "
                        "off-site jump, and the guardrails reject both.",
                "tagline": "The steps above are a scripted probe, not a model "
                           "improvising. What matters is the verdict: the "
                           "credential field and the off-site jump were both "
                           "refused in code.",
                "repro": SAFETY_REPRO,
            },
        )
    return (
        f"{base}/index.html",
        HeuristicBrain(),
        {
            "scenario": "exploration",
            "note": "The key-free heuristic brain drives the sandbox store. "
                    "When it cannot satisfy a goal it gives up inside its "
                    "step budget instead of clicking forever.",
            "tagline": "Here the brain proposes each step and the code "
                       "validates it against the guardrails before the "
                       "browser acts. The model proposes, the code disposes.",
            "repro": DEMO_REPRO,
        },
    )


def run(goal: str):
    sandbox = WEBPILOT / "sandbox"
    with contextlib.closing(socket.socket()) as s:
        s.bind(("127.0.0.1", 0))
        port = s.getsockname()[1]

    class _Quiet(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *args):
            pass

    httpd = http.server.HTTPServer(
        ("127.0.0.1", port),
        functools.partial(_Quiet, directory=str(sandbox)))
    threading.Thread(target=httpd.serve_forever, daemon=True).start()

    start_url, brain, meta = pick_scenario(goal, port)
    browser = PlaywrightBrowser(headless=True)
    try:
        browser.navigate(start_url)
        trace = Agent(browser, brain, Guardrails(allow=["127.0.0.1"])).run(goal)
    finally:
        browser.close()
        httpd.shutdown()
    return trace, meta, port


def clean(text: str, port: int) -> str:
    """Strip the throwaway port and backticks so the comment renders flat."""
    return text.replace(f"http://127.0.0.1:{port}", "sandbox:/").replace("`", "'")


def write_comment(goal, trace, meta, port, issue):
    summary = clean(trace.summary(), port)
    COMMENT_PATH.write_text(
        f"Thanks for driving. Scenario: **{meta['scenario']}**.\n\n"
        f"{meta['note']}\n\n"
        f"```\n{summary}\n```\n\n"
        "Every BLOCKED line above is "
        "[web-pilot](https://github.com/vinimabreu/web-pilot)'s guardrail "
        "code rejecting the action before the browser sees it: domain "
        "allowlist, no credential or payment fields, step budget. "
        f"{meta['tagline']} This trace is the audit trail.\n\n"
        f"Reproduce this exact trace: `{meta['repro']}` in the web-pilot "
        "repo, no API key needed.\n",
        encoding="utf-8",
    )
    print(f"comment written for issue #{issue}")


def update_board(goal, trace, scenario, issue):
    drives = json.loads(DRIVES_PATH.read_text()) if DRIVES_PATH.exists() else []
    drives.insert(0, {
        "date": date.today().isoformat(),
        "goal": goal[:60] + ("..." if len(goal) > 60 else ""),
        "scenario": scenario,
        "outcome": trace.outcome,
        "issue": int(issue),
    })
    drives = drives[:BOARD_ROWS]
    DRIVES_PATH.write_text(json.dumps(drives, indent=2) + "\n", encoding="utf-8")

    def cell(text: str) -> str:
        # Neutralize table, code, and HTML-comment syntax so a crafted goal
        # cannot break the table or inject the board's own region markers.
        return (text.replace("|", "/").replace("`", "'")
                .replace("<", "(").replace(">", ")"))

    rows = "\n".join(
        "| {goal} | {scenario} | {outcome} | [#{issue}](https://github.com/vinimabreu/vinimabreu/issues/{issue}) |".format(
            goal=cell(d["goal"]), scenario=d["scenario"],
            outcome=d["outcome"], issue=d["issue"])
        for d in drives
    )
    board = (
        f"{BOARD_START}\n"
        "| goal | scenario | outcome | trace |\n| --- | --- | --- | --- |\n"
        f"{rows}\n{BOARD_END}"
    )
    readme = README_PATH.read_text(encoding="utf-8")
    pattern = re.compile(
        re.escape(BOARD_START) + ".*?" + re.escape(BOARD_END), re.DOTALL)
    README_PATH.write_text(pattern.sub(board, readme), encoding="utf-8")
    print(f"board updated: {len(drives)} drive(s)")


def main() -> None:
    issue = os.environ.get("DRIVE_ISSUE", "0")
    goal = extract_goal()
    if not goal:
        COMMENT_PATH.write_text(
            "I could not find a goal in the issue. Open a new one with a "
            "single sentence under the Goal field and the agent will drive.\n",
            encoding="utf-8",
        )
        print("no goal found; comment written, board untouched")
        return
    trace, meta, port = run(goal)
    write_comment(goal, trace, meta, port, issue)
    update_board(goal, trace, meta["scenario"], issue)
    print(f"outcome: {trace.outcome}")


if __name__ == "__main__":
    main()
