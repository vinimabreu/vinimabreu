"""Section navigation chips, one SVG per section; the README links each to its heading.

    python3 assets/make_nav.py
"""

from __future__ import annotations

from pathlib import Path

HERE = Path(__file__).resolve().parent
MONO = "ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,monospace"
H = 30
ADVANCE = 8.6          # 11px mono plus 2px letter spacing, per character

# anchor and label; each label is the heading it jumps to
SECTIONS = [
    ("proof", "PROOF"),
    ("flagships", "FLAGSHIPS"),
    ("projects", "PROJECTS"),
    ("stack", "STACK"),
    ("contact", "CONTACT"),
]


def chip(label: str) -> tuple[int, str]:
    w = int(18 + len(label) * ADVANCE + 16)
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {H}" width="{w}" height="{H}" role="img" aria-label="{label.title()}">
  <rect x="0.5" y="0.5" width="{w - 1}" height="{H - 1}" rx="6" fill="#0A0E14" stroke="#26313D"/>
  <text x="18" y="19.5" font-family="{MONO}" font-size="11" letter-spacing="2" fill="#FFB000">{label}</text>
</svg>
"""
    return w, svg


def main() -> None:
    for anchor, label in SECTIONS:
        _, svg = chip(label)
        (HERE / f"nav-{anchor}.svg").write_text(svg, encoding="utf-8")
    print(f"wrote {len(SECTIONS)} nav chips")


if __name__ == "__main__":
    main()
