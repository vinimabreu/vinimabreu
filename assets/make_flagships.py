"""Generate the flagship repo cards as self-hosted SVGs (dark + light).

    python3 assets/make_flagships.py

These replace the third-party github-readme-stats pins, whose shared instance
returns 503 often. These are committed to this repo, so the flagship row never
depends on an external service and never breaks.
"""

from pathlib import Path

HERE = Path(__file__).resolve().parent

FONT_MONO = "ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"
FONT_SANS = "-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif"
W, H = 480, 150

THEMES = {
    "dark": {"panel": "#0D1117", "border": "#30363D", "text": "#E6EDF3", "dim": "#8B949E", "brand": "#A78BFA"},
    "light": {"panel": "#FFFFFF", "border": "#D0D7DE", "text": "#1F2328", "dim": "#57606A", "brand": "#6E56CF"},
}

# repo, two description lines, meta line (feature tags, no unverified numbers)
CARDS = [
    ("bedrock",
     ["A NL-to-SQL data agent that proves it", "answers the same right thing every run."],
     "Python · stability harness · CI gate"),
    ("rag-chat",
     ["Chat with your docs: grounded answers", "with clickable citations."],
     "Python · grounded · clickable citations"),
    ("web-pilot",
     ["A browser-use agent with its guardrails", "enforced in code, plus a full audit trace."],
     "Python · guardrails in code · audit trace"),
    ("voice-receptionist",
     ["An AI phone receptionist that books", "against a live calendar."],
     "Python · Twilio · abstains on policy"),
    ("scrape-sentinel",
     ["The change-aware layer for any scraper:", "new, changed, removed since the last run."],
     "Python · change detection · zero deps"),
    ("lead-qualifier",
     ["Qualify leads with rules or an LLM, then", "measure the qualifier with an eval harness."],
     "Python · LLM + rules · eval harness"),
]


def esc(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def build(repo: str, lines: list[str], meta: str, theme: str) -> str:
    c = THEMES[theme]
    desc = "".join(
        f'<text x="24" y="{78 + i * 24}" font-family="{FONT_SANS}" '
        f'font-size="14" fill="{c["text"]}">{esc(line)}</text>'
        for i, line in enumerate(lines)
    )
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img"
     aria-label="{esc(repo)}: {esc(lines[0])} {esc(lines[1])}">
  <rect x="1.5" y="1.5" width="{W - 3}" height="{H - 3}" rx="12" fill="{c['panel']}" stroke="{c['border']}"/>
  <circle cx="30" cy="36" r="5" fill="{c['brand']}"/>
  <text x="44" y="43" font-family="{FONT_MONO}" font-size="20" font-weight="700" fill="{c['brand']}">{esc(repo)}</text>
  {desc}
  <text x="24" y="130" font-family="{FONT_SANS}" font-size="12.5" fill="{c['dim']}">{esc(meta)}</text>
</svg>
"""


def main() -> None:
    for repo, lines, meta in CARDS:
        for theme in THEMES:
            out = HERE / f"flagship-{repo}-{theme}.svg"
            out.write_text(build(repo, lines, meta, theme), encoding="utf-8")
    print(f"wrote {len(CARDS) * len(THEMES)} flagship card SVGs")


if __name__ == "__main__":
    main()
