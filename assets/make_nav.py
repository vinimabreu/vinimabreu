"""Section navigation chips in the mission palette, one SVG per section; the README links each to its heading.

    python3 assets/make_nav.py
"""

from __future__ import annotations

from pathlib import Path

HERE = Path(__file__).resolve().parent
MONO = "ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,monospace"
H = 30
ADVANCE = 8.6          # 11px mono plus 2px letter spacing, per character

# anchor, short label, alt text (the full section name)
SECTIONS = [
    ("the-house-rule-running", "RULE", "The house rule, running"),
    ("the-free-handbook", "HANDBOOK", "The free handbook"),
    ("invited-review", "REVIEW", "Invited review"),
    ("merged-upstream", "UPSTREAM", "Merged upstream"),
    ("ci-security", "SECURITY", "CI security"),
    ("flagships", "FLAGSHIPS", "Flagships"),
    ("retrieval-and-rag", "RAG", "Retrieval and RAG"),
    ("agents-and-tools", "AGENTS", "Agents and tools"),
    ("voice-and-automation", "AUTOMATION", "Voice and automation"),
    ("evaluation-and-quality", "EVALS", "Evaluation and quality"),
    ("data-engineering-and-extraction", "DATA", "Data engineering and extraction"),
    ("stack", "STACK", "Stack"),
    ("how-i-work", "HOW I WORK", "How I work"),
]


def chip(index: int, label: str) -> tuple[int, str]:
    number = f"{index:02d}"
    w = int(14 + len(number) * ADVANCE + 8 + len(label) * ADVANCE + 12)
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {H}" width="{w}" height="{H}" role="img" aria-label="{label.title()}">
  <rect x="0.5" y="0.5" width="{w - 1}" height="{H - 1}" rx="6" fill="#0A0E14" stroke="#26313D"/>
  <text x="14" y="19.5" font-family="{MONO}" font-size="11" letter-spacing="2" fill="#FFB000" font-weight="700">{number}</text>
  <text x="{14 + len(number) * ADVANCE + 8:.1f}" y="19.5" font-family="{MONO}" font-size="11" letter-spacing="2" fill="#D8E1E8">{label}</text>
</svg>
"""
    return w, svg


def main() -> None:
    for i, (anchor, label, _) in enumerate(SECTIONS, start=1):
        _, svg = chip(i, label)
        (HERE / f"nav-{anchor}.svg").write_text(svg, encoding="utf-8")
    print(f"wrote {len(SECTIONS)} nav chips")


if __name__ == "__main__":
    main()
