"""The README panels that are pictures: the handbook card, the project rows, the review quotes and the button.

    python3 assets/make_theme.py

Everything a reader needs to act on (the house rule, the flagship lines, the call to
action) is plain text in the README. What stays a picture repeats its text word for
word in the alt attribute. Amber is kept for project names and the button. The repo
rows come from rows.json: one entry per repo, with the one-line description it
carries on GitHub. A new repo is a new entry there.
"""

from __future__ import annotations

import base64
import html
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
MONO = "ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,monospace"
SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif"
C = {"ground": "#05070A", "panel": "#0A0E14", "hair": "#1C2530", "hair2": "#26313D", "amber": "#FFB000",
     "green": "#37D67A", "text": "#D8E1E8", "soft": "#A9B4BF", "muted": "#6B7683", "white": "#F2F5F8"}
W = 1200


def esc(text: str) -> str:
    return html.escape(text, quote=True)


def wrap(text: str, width_px: float, size: float, mono: bool = False, per_em: float | None = None) -> list[str]:
    """Greedy word wrap with an average glyph width: 0.6em for mono, 0.52em for sans (or per_em)."""
    per = size * (per_em or (0.6 if mono else 0.52))
    limit = max(10, int(width_px / per))
    lines, line = [], ""
    for word in text.split():
        candidate = f"{line} {word}".strip()
        if len(candidate) > limit and line:
            lines.append(line)
            line = word
        else:
            line = candidate
    if line:
        lines.append(line)
    return lines


def text_block(x: float, y: float, lines: list[str], size: float, colour: str, lead: float, family: str = SANS,
               weight: str = "400", italic: bool = False, justify: float | None = None) -> tuple[str, float]:
    """With justify (a width in px), every line but the last is stretched to exactly that width,
    so a paragraph reaches the right edge whatever font the reader's system picks."""
    style = ' font-style="italic"' if italic else ""
    out = ""
    for i, t in enumerate(lines):
        # only lines already close to the width get stretched; a short line would show gaps between letters
        full = justify and i < len(lines) - 1 and len(t.split()) > 1 and len(t) * size * 0.47 >= 0.85 * justify
        fit = f' textLength="{justify:.0f}" lengthAdjust="spacing"' if full else ""
        out += (f'<text x="{x}" y="{y + i * lead:.1f}" font-family="{family}" font-size="{size}" '
                f'font-weight="{weight}" fill="{colour}"{style}{fit}>{esc(t)}</text>')
    return out, y + (len(lines) - 1) * lead


def frame(h: float, body: str, label: str = "") -> str:
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {h:.0f}" role="img" aria-label="{esc(label)}">\n'
            f'  <rect x="1" y="1" width="{W - 2}" height="{h - 2:.0f}" rx="14" fill="{C["ground"]}" stroke="{C["hair2"]}"/>\n'
            f'  {body}\n</svg>\n')


def eyebrow(x: float, y: float, text: str) -> str:
    return (f'<text x="{x}" y="{y}" font-family="{MONO}" font-size="13" fill="{C["muted"]}" letter-spacing="3" '
            f'font-weight="700">{esc(text)}</text>')


# ---------------------------------------------------------------- the button

def button(label: str, w: int = 560) -> str:
    h = 58
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{esc(label)}">\n'
            f'  <rect x="1" y="1" width="{w - 2}" height="{h - 2}" rx="10" fill="{C["amber"]}" stroke="{C["amber"]}"/>\n'
            f'  <text x="{w / 2}" y="36" text-anchor="middle" font-family="{MONO}" font-size="15" font-weight="700" '
            f'letter-spacing="2.5" fill="{C["ground"]}">{esc(label)}</text>\n</svg>\n')


# ---------------------------------------------------------------- the handbook card

HB_TITLE = "Artificial Intelligence in Practice"
HB_BODY = ('A free 84-page handbook that walks from "what is a token" to working agents with tools. Local models, '
           "RAG, agents, MCP, fine-tuning, real API costs, security, prompting as a method, and how to test AI systems "
           "so they do not embarrass you in front of a customer. Written for people starting out in AI, with every "
           "example tested by hand.")
HB_LICENSE = "CC BY-NC-SA: share it, translate it, teach with it."


def handbook(cover: bytes) -> str:
    b64 = base64.b64encode(cover).decode()
    cx, cy, cw, chh = 44, 36, 220, 285
    x = cx + cw + 44
    parts = [f'<rect x="{cx - 1}" y="{cy - 1}" width="{cw + 2}" height="{chh + 2}" rx="4" fill="none" stroke="{C["hair2"]}"/>',
             f'<image x="{cx}" y="{cy}" width="{cw}" height="{chh}" preserveAspectRatio="xMidYMid slice" '
             f'href="data:image/jpeg;base64,{b64}"/>',
             eyebrow(x, 64, "FREE HANDBOOK · 84 PAGES"),
             f'<text x="{x}" y="112" font-family="{SANS}" font-size="34" font-weight="700" fill="{C["amber"]}">{esc(HB_TITLE)}</text>']
    body, y = text_block(x, 154, wrap(HB_BODY, W - x - 48, 17.5, per_em=0.47), 17.5, C["soft"], 28, justify=W - x - 48)
    lic, _ = text_block(x, y + 40, [HB_LICENSE], 14, C["muted"], 20, MONO)
    return frame(cy * 2 + chh, "\n  ".join(parts + [body, lic]), f"{HB_TITLE}: {HB_BODY} {HB_LICENSE}")


# ---------------------------------------------------------------- repo rows

def row(name: str, desc: str, extra: str = "") -> str:
    x_name, x_desc = 32, 330
    lines = wrap(desc, W - x_desc - 40, 18)
    h = 60 + (len(lines) - 1) * 26
    mid = h / 2
    first_y = mid + 6 - (len(lines) - 1) * 13
    parts = [f'<text x="{x_name}" y="{mid + 6:.1f}" font-family="{MONO}" font-size="17" font-weight="700" fill="{C["amber"]}">{esc(name)}</text>']
    if extra:
        parts.append(f'<text x="{x_name}" y="{mid + 26:.1f}" font-family="{MONO}" font-size="11" fill="{C["muted"]}" letter-spacing="1">{esc(extra)}</text>')
    t, _ = text_block(x_desc, first_y, lines, 18, C["soft"], 26)
    parts.append(t)
    return frame(h, "\n  ".join(parts), f"{name}: {desc}")


# ---------------------------------------------------------------- client reviews, attributed by the kind of project

REVIEWS = [
    ("He built a reusable, profile-driven Python data cleansing framework with strong architecture, clear "
     "documentation, automated tests, and disciplined output controls. [...] The final delivery was professional, "
     "well-structured, tested, and ready for the next productisation phase. I would confidently work with Vinicius "
     "again.", "Python data-cleansing framework"),
    ("completed the work ahead of schedule and with accuracy. I would hire him again.",
     "Data extraction from a public registry"),
]


def quote_card(text: str, who: str) -> str:
    x = 56
    lines = wrap(f"“{text}”", W - 2 * x, 19, per_em=0.47)
    parts = [f'<text x="{x - 8}" y="96" font-family="Georgia,serif" font-size="96" fill="{C["hair2"]}">“</text>',
             eyebrow(x + 50, 58, "CLIENT REVIEW")]
    t, y = text_block(x, 112, lines, 19, C["text"], 31, SANS, italic=True, justify=W - 2 * x)
    parts.append(t)
    w, _ = text_block(x, y + 46, [f"· {who}"], 13.5, C["muted"], 20, MONO)
    parts.append(w)
    return frame(y + 80, "\n  ".join(parts), f"Client review, {who.lower()}: {text}")


def main() -> None:
    out = {
        "button-casestudies.svg": button("FULL PORTFOLIO · VINIMABREU.DEV ↗"),
        "handbook.svg": handbook((HERE / "handbook-cover.jpg").read_bytes()),
        "quote-1.svg": quote_card(*REVIEWS[0]),
        "quote-2.svg": quote_card(*REVIEWS[1]),
    }
    rows = json.loads((HERE / "rows.json").read_text(encoding="utf-8"))
    for r in rows:
        out[f"row-{r['slug']}.svg"] = row(r["name"], r["desc"], r.get("extra", ""))
    for name, svg in out.items():
        (HERE / name).write_text(svg, encoding="utf-8")
    print(f"wrote {len(out)} panels")


if __name__ == "__main__":
    main()
