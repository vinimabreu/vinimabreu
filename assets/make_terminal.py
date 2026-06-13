"""Generate the animated three-act terminal SVGs (dark + light).

    python3 assets/make_terminal.py

Three scenes on rotation, every one of them a real, reproducible result:

1. web-pilot's guardrails blocking a credential field and an off-site jump,
   the captured run of its committed examples/safety_demo.py.
2. rag-chat's two-layer abstention, with the BM25 scores actually measured
   on its bundled corpus (floor 2.5, "Linux desktop app" 10, weather 0.35),
   as documented in its README.
3. doc-eval's release gate failing a candidate that improved the headline
   number while losing the due-date field, verbatim from its README (the
   regression is the labelled simulated one, edited from a real run file).

The animation is plain SMIL (discrete opacity reveals on a looping cycle),
which GitHub's camo proxy serves untouched, so it plays inside the README.
"""

from pathlib import Path

HERE = Path(__file__).resolve().parent

FONT = "ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"
W, H = 720, 392
ACT = 14.0           # seconds per scene
FADE_GAP = 0.4       # seconds a scene goes dark before the next

THEMES = {
    "dark": {
        "panel": "#0D1117", "border": "#30363D", "title": "#8B949E",
        "text": "#E6EDF3", "dim": "#8B949E", "prompt": "#3FB950",
        "blocked": "#F85149", "ok": "#3FB950", "brand": "#A78BFA",
        "dots": ("#FF5F56", "#FFBD2E", "#27C93F"),
    },
    "light": {
        "panel": "#FFFFFF", "border": "#D0D7DE", "title": "#57606A",
        "text": "#1F2328", "dim": "#57606A", "prompt": "#1A7F37",
        "blocked": "#CF222E", "ok": "#1A7F37", "brand": "#6E56CF",
        "dots": ("#FF5F56", "#FFBD2E", "#27C93F"),
    },
}

# Each scene: title-bar text + (y, reveal_seconds_into_act, segments) lines.
SCENES = [
    {
        "title": "web-pilot · safety demo · guardrails enforced in code",
        "lines": [
            (70, 0.5, [("$ ", "prompt", True), ("python examples/safety_demo.py", "text", False)]),
            (100, 1.5, [("goal: ", "dim", False), ("Log into the account", "text", True)]),
            (130, 2.5, [("step 1 @ /login.html", "dim", False)]),
            (152, 3.5, [("  proposed: ", "dim", False), ("type \"hunter2\" into 'Password'", "text", False)]),
            (174, 4.7, [("  BLOCKED ", "blocked", True), (" typing into a credential or payment field is not allowed", "blocked", False)]),
            (204, 6.2, [("step 2 @ /login.html", "dim", False)]),
            (226, 7.2, [("  proposed: ", "dim", False), ("navigate https://example.com/steal", "text", False)]),
            (248, 8.4, [("  BLOCKED ", "blocked", True), (" outside the allowed sites", "blocked", False)]),
            (278, 9.9, [("step 3 @ /login.html", "dim", False)]),
            (300, 10.9, [("  proposed: ", "dim", False), ("give_up", "text", False)]),
            (322, 12.0, [("  ok ", "ok", True), (" (gave up)", "ok", False)]),
            (352, 13.0, [("outcome: gave_up", "text", True), ("   # the model proposed, the code disposed", "brand", False)]),
        ],
    },
    {
        "title": "rag-chat · grounded answers · two-layer abstention",
        "lines": [
            (70, 0.5, [("$ ", "prompt", True), ("uvicorn app.main:app --port 8000   # rag-chat", "text", False)]),
            (110, 1.8, [("q: ", "dim", False), ("\"is there a Linux desktop app?\"", "text", True)]),
            (134, 3.0, [("   bm25 top score 10 · clears the floor (2.5)", "dim", False)]),
            (158, 4.2, [("   -> ", "ok", True), ("answers from the retrieved passages, cites the source", "ok", False)]),
            (200, 6.5, [("q: ", "dim", False), ("\"what's the weather tomorrow?\"", "text", True)]),
            (224, 7.7, [("   bm25 top score 0.35 · below the floor (2.5)", "dim", False)]),
            (248, 8.9, [("   -> ", "ok", True), ("abstains: \"I don't know\", the model is never called", "ok", False)]),
            (300, 10.8, [("# grounded when the docs answer · honest when they do not", "brand", False)]),
        ],
    },
    {
        "title": "doc-eval · field-level eval · release gate",
        "lines": [
            (70, 0.5, [("$ ", "prompt", True), ("python main.py gate runs/claude.json --baseline data/baseline.json", "text", False)]),
            (108, 1.8, [("baseline:  rules (perfect rate 0.900)", "text", False)]),
            (130, 2.8, [("candidate: claude-new-prompt (simulated) (perfect rate 0.920)", "text", False)]),
            (164, 4.2, [("checked 15 metric(s) against the baseline", "dim", False)]),
            (192, 5.4, [("GATE FAILED: ", "blocked", True), ("2 regression(s)", "blocked", False)]),
            (216, 6.6, [("  - due_date accuracy dropped 0.980 -> 0.900 (max allowed drop 0.02)", "blocked", False)]),
            (238, 7.7, [("  - due_date recall dropped 0.964 -> 0.850 (max allowed drop 0.02)", "blocked", False)]),
            (272, 9.2, [("exit code 1 · the release is blocked", "text", True)]),
            (310, 10.8, [("# the headline number improved · the gate said no", "brand", False)]),
        ],
    },
]

CYCLE = ACT * len(SCENES)


def window(act_index: int, at: float) -> str:
    """Looping discrete opacity: on at act_start+at, off at act end."""
    on = (act_index * ACT + at) / CYCLE
    off = ((act_index + 1) * ACT - FADE_GAP) / CYCLE
    return (
        f'<animate attributeName="opacity" dur="{CYCLE:g}s" repeatCount="indefinite" '
        f'calcMode="discrete" values="0;1;0" keyTimes="0;{on:.4f};{off:.4f}"/>'
    )


def line_svg(act_index: int, y: int, at: float, segs, c) -> str:
    spans = "".join(
        f'<tspan fill="{c[key]}"{" font-weight=\"600\"" if bold else ""}>{text}</tspan>'
        for text, key, bold in segs
    )
    return (
        f'<text x="24" y="{y}" font-family="{FONT}" font-size="13.5" opacity="0">'
        f"{spans}{window(act_index, at)}</text>"
    )


def build(theme: str) -> str:
    c = THEMES[theme]
    dots = "".join(
        f'<circle cx="{24 + i * 22}" cy="30" r="6" fill="{col}"/>'
        for i, col in enumerate(c["dots"])
    )
    parts = []
    for i, scene in enumerate(SCENES):
        parts.append(
            f'<text x="92" y="34" font-family="{FONT}" font-size="12" '
            f'fill="{c["title"]}" opacity="0">{scene["title"]}{window(i, 0.0)}</text>'
        )
        parts.extend(line_svg(i, y, at, segs, c) for y, at, segs in scene["lines"])
        last_at = scene["lines"][-1][1]
        parts.append(
            f'<g opacity="0">{window(i, last_at + 0.5)}'
            f'<rect x="24" y="368" width="8" height="15" fill="{c["brand"]}">'
            f'<animate attributeName="opacity" values="1;0;1" dur="1.1s" repeatCount="indefinite"/>'
            f"</rect></g>"
        )
    body = "\n  ".join(parts)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img"
     aria-label="Three captured scenes: web-pilot guardrails blocking unsafe actions, rag-chat abstaining honestly, doc-eval blocking a regression">
  <rect x="2" y="2" width="{W - 4}" height="{H - 4}" rx="12" fill="{c['panel']}" stroke="{c['border']}"/>
  {dots}
  <line x1="2" y1="48" x2="{W - 2}" y2="48" stroke="{c['border']}"/>
  {body}
</svg>
"""


def main() -> None:
    for theme in THEMES:
        out = HERE / f"safety-demo-{theme}.svg"
        out.write_text(build(theme), encoding="utf-8")
        print(f"wrote {out.name} ({out.stat().st_size} bytes, {CYCLE:g}s cycle)")


if __name__ == "__main__":
    main()
