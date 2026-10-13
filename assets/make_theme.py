"""Every remaining README panel in the mission palette of vinimabreu.dev.

    python3 assets/make_theme.py

Text panels here repeat, word for word, text that the README also keeps as
plain text (in alt attributes or in folded notes), so nothing is only in a
picture. The repo rows come from rows.json: one entry per repo, with the
one-line description it carries on GitHub. A new repo is a new entry there.
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
     "amberdim": "#7A5600", "green": "#37D67A", "text": "#D8E1E8", "soft": "#A9B4BF", "muted": "#6B7683",
     "white": "#F2F5F8"}
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


def eyebrow(x: float, y: float, text: str, colour: str = "amber") -> str:
    return (f'<text x="{x}" y="{y}" font-family="{MONO}" font-size="13" fill="{C[colour]}" letter-spacing="3" '
            f'font-weight="700">{esc(text)}</text>')


# ---------------------------------------------------------------- the briefing under the header

BRIEF_RULE = "The model proposes, the code disposes."
BRIEF_SUB = "The model holds the conversation. Tested code makes every decision that matters."
BRIEF_BODY = ("I build retrieval, agents, MCP servers, voice, and automation with that one rule at the center. The "
              "flagships ship deterministic test suites that need no API key and show captured output from actual "
              "runs; every README is honest about the trade-offs. The console below counts the public repos and the "
              "tests their READMEs state, fresh every weekday; one rule runs through all of them.")
BRIEF_NDA = ("My client work is under NDA and stays private. These public projects are built to the same standard, "
             "and show how I work: grounded, tested, and honest.")


def brief() -> str:
    x = 56
    parts = [eyebrow(x, 58, "THE HOUSE RULE")]
    parts.append(f'<text x="{x}" y="112" font-family="{SANS}" font-size="40" font-weight="700" fill="{C["white"]}" '
                 f'letter-spacing="-0.5">{esc(BRIEF_RULE)}</text>')
    sub, y = text_block(x, 152, [BRIEF_SUB], 20, C["amber"], 28)
    body, y = text_block(x, y + 46, wrap(BRIEF_BODY, W - 2 * x, 18, per_em=0.47), 18, C["soft"], 29, justify=W - 2 * x)
    nda_y = y + 50
    nda, y2 = text_block(x + 22, nda_y, wrap(BRIEF_NDA, W - 2 * x - 22, 13.5, mono=True), 13.5, C["muted"], 22, MONO)
    bar = f'<rect x="{x}" y="{nda_y - 15}" width="3" height="{y2 - nda_y + 22:.0f}" fill="{C["amberdim"]}"/>'
    h = y2 + 44
    return frame(h, "\n  ".join(parts + [sub, body, bar, nda]),
                 f"{BRIEF_RULE} {BRIEF_SUB} {BRIEF_BODY} {BRIEF_NDA}")


# ---------------------------------------------------------------- buttons and chips

def button(label: str, w: int = 560, filled: bool = True) -> str:
    h = 58
    fill, ink = (C["amber"], C["ground"]) if filled else (C["panel"], C["amber"])
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{esc(label)}">\n'
            f'  <rect x="1" y="1" width="{w - 2}" height="{h - 2}" rx="10" fill="{fill}" stroke="{C["amber"]}"/>\n'
            f'  <text x="{w / 2}" y="36" text-anchor="middle" font-family="{MONO}" font-size="15" font-weight="700" '
            f'letter-spacing="2.5" fill="{ink}">{esc(label)}</text>\n</svg>\n')


def chip(label: str) -> str:
    w = int(28 + len(label) * 8.6 + 20)
    h = 34
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{esc(label.title())}">\n'
            f'  <rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="7" fill="{C["panel"]}" stroke="{C["hair2"]}"/>\n'
            f'  <text x="16" y="22" font-family="{MONO}" font-size="11" letter-spacing="2" fill="{C["amber"]}" font-weight="700">{esc(label)}</text>\n</svg>\n')


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
             eyebrow(x, 64, "FIELD MANUAL · FREE · 84 PAGES"),
             f'<text x="{x}" y="112" font-family="{SANS}" font-size="34" font-weight="700" fill="{C["white"]}">{esc(HB_TITLE)}</text>']
    body, y = text_block(x, 154, wrap(HB_BODY, W - x - 48, 17.5, per_em=0.47), 17.5, C["soft"], 28, justify=W - x - 48)
    lic, _ = text_block(x, y + 40, [HB_LICENSE], 14, C["amber"], 20, MONO)
    return frame(cy * 2 + chh, "\n  ".join(parts + [body, lic]), f"{HB_TITLE}: {HB_BODY} {HB_LICENSE}")


# ---------------------------------------------------------------- dossier cards (review, upstream, security)

def dossier(label: str, title: str, body: str, footer: str, tagline: str = "") -> str:
    x = 56
    parts = [eyebrow(x, 58, label)]
    y = 58
    if tagline:
        tl, y = text_block(x, 96, [tagline], 19, C["amber"], 26, SANS, italic=True)
        parts.append(tl)
    tlines = wrap(title, W - 2 * x, 30)
    t, y = text_block(x, y + 46, tlines, 30, C["white"], 38, SANS, "700")
    b, y = text_block(x, y + 40, wrap(body, W - 2 * x, 17.5, per_em=0.47), 17.5, C["soft"], 28, justify=W - 2 * x)
    parts += [t, b, f'<line x1="{x}" y1="{y + 28:.0f}" x2="{W - x}" y2="{y + 28:.0f}" stroke="{C["hair"]}"/>']
    f, y = text_block(x, y + 56, [footer], 13.5, C["muted"], 20, MONO)
    parts.append(f)
    return frame(y + 36, "\n  ".join(parts), f"{label}. {title}. {body} {footer}")


REVIEW = dossier(
    "INVITED REVIEW · CREDITED BY NAME",
    "A Decision-Centered Reference Architecture for Trustworthy Agentic Commerce",
    "Invited technical reviewer on this decision-centered reference architecture by Dimitrios S. Sfyris, founder of "
    "AspectSoft, now published on arXiv. Credited by name for refining the separation between commercial eligibility "
    "and actor authority, payment artifacts treated as evidence rather than automatic permission, and the controls "
    "that keep AI-generated claims grounded, scoped, and verifiable.",
    "arXiv 2607.18347 · READ THE PAPER ↗")

UPSTREAM = dossier(
    "MERGED UPSTREAM · REVIEWED BY THE MAINTAINER",
    "containers/crun #2166",
    "crun is the OCI runtime that Podman and CRI-O run containers with. Its passwd parser tested for a digit with a "
    "signed comparison and no lower bound, so a passwd line whose uid field is empty walks the parser past the end of "
    "the buffer. Traced back to the 2020 commit that dropped a U suffix to silence a warning, and fixed with an "
    "explicit range test that stays warning free without a cast. Reviewed and merged by the project maintainer.",
    "github.com/containers/crun/pull/2166 · THE BUG IN FULL BELOW ↓")

SECURITY = dossier(
    "CI SECURITY",
    "taint-trail",
    "The usual fix for a template inside a run: block is to move the value into env:, which removes the finding from "
    "every scanner that looks for templates in scripts and nothing from the job. This follows the value after the move, through env:, with:, step outputs "
    "and into the called action, until it dies as an argument, reaches a shell, can spoof $GITHUB_OUTPUT, or becomes "
    "opaque. Every verdict is a chain with a file and line at each hop. Modelled on a real finding in coordinated "
    "disclosure.",
    "707 tests · one dependency · no network · no key",
    tagline="The scanner finds the template. This follows the value after someone moves it.")


# ---------------------------------------------------------------- sector strips and repo rows

SECTORS = {
    "rag": ("07", "RETRIEVAL AND RAG", 'Citations you can click, an honest "I don\'t know", retrieval quality that is '
            "measured rather than assumed, and a fence between customers that a ranking cannot climb over."),
    "agents": ("08", "AGENTS AND TOOLS", "Agents that can only do what their tool layer allows."),
    "automation": ("09", "VOICE AND AUTOMATION", "Conversation up front, a tested service underneath, and a human "
                   "whenever confidence drops."),
    "evals": ("10", "EVALUATION AND QUALITY", "A regression gets blocked before it ships, not discovered after."),
    "data": ("11", "DATA ENGINEERING AND EXTRACTION", "The layer underneath everything above: scrape, parse, "
             "validate, schedule."),
}


def sector(number: str, name: str, tagline: str) -> str:
    x = 40
    lines = wrap(tagline, W - x - 260, 18, False)
    h = 70 + (len(lines) - 1) * 26
    parts = [f'<text x="{x}" y="44" font-family="{MONO}" font-size="13" letter-spacing="3" font-weight="700" fill="{C["amber"]}">SECTOR {number}</text>',
             f'<line x1="{x + 140}" y1="40" x2="{x + 200}" y2="40" stroke="{C["amberdim"]}"/>']
    t, _ = text_block(x + 220, 46, lines, 18, C["soft"], 26, SANS, italic=True)
    parts.append(t)
    return frame(h, "\n  ".join(parts), f"Sector {number}, {name.lower()}: {tagline}")


def row(index: str, name: str, desc: str, extra: str = "") -> str:
    x_idx, x_name, x_desc = 32, 140, 470
    lines = wrap(desc, W - x_desc - 90, 18)
    h = 60 + (len(lines) - 1) * 26
    mid = h / 2
    cross = (f'<g stroke="{C["amberdim"]}" fill="none" transform="translate({W - 50},{mid:.1f})">'
             f'<circle r="9"/><line x1="0" y1="-14" x2="0" y2="-6"/><line x1="0" y1="6" x2="0" y2="14"/>'
             f'<line x1="-14" y1="0" x2="-6" y2="0"/><line x1="6" y1="0" x2="14" y2="0"/>'
             f'<circle r="1.6" fill="{C["amber"]}" stroke="none"/></g>')
    first_y = mid + 6 - (len(lines) - 1) * 13
    parts = [f'<text x="{x_idx}" y="{mid + 5:.1f}" font-family="{MONO}" font-size="14" fill="{C["amber"]}">[{index}]</text>',
             f'<text x="{x_name}" y="{mid + 6:.1f}" font-family="{MONO}" font-size="17" font-weight="700" fill="{C["white"]}">{esc(name)}</text>']
    if extra:
        parts.append(f'<text x="{x_name}" y="{mid + 26:.1f}" font-family="{MONO}" font-size="11" fill="{C["muted"]}" letter-spacing="1">{esc(extra)}</text>')
    t, _ = text_block(x_desc, first_y, lines, 18, C["soft"], 26)
    parts += [t, cross]
    return frame(h, "\n  ".join(parts), f"{name}: {desc}")


# ---------------------------------------------------------------- how I work, reviews, call to action

HOW = [("GROUNDED", "Answers cite their sources and refuse when the evidence is not there."),
       ("TESTED", "Deterministic suites that run with no API key and no network; CI gates catch regressions."),
       ("HONEST", "Trade-offs go in the README: rag-quality ships the eval showing hybrid retrieval was not a free "
                  "win on its corpus.")]


def how_i_work() -> str:
    col = (W - 2 * 40 - 2 * 24) / 3
    parts, bottom = [], 0
    for i, (head, body) in enumerate(HOW):
        x = 40 + i * (col + 24)
        lines = wrap(body, col - 48, 17, per_em=0.47)
        t, y = text_block(x + 24, 104, lines, 17, C["soft"], 27, justify=col - 48)
        parts += [f'<rect x="{x:.0f}" y="28" width="{col:.0f}" height="__H__" rx="10" fill="{C["panel"]}" stroke="{C["hair2"]}"/>',
                  f'<rect x="{x:.0f}" y="28" width="{col:.0f}" height="3" fill="{C["amber"]}"/>',
                  eyebrow(x + 24, 70, head), t]
        bottom = max(bottom, y)
    h = bottom + 60
    body = "\n  ".join(parts).replace("__H__", f"{h - 56:.0f}")
    return frame(h, body, " ".join(f"{a}: {b}" for a, b in HOW))


REVIEWS = [
    ("He built a reusable, profile-driven Python data cleansing framework with strong architecture, clear "
     "documentation, automated tests, and disciplined output controls. [...] The final delivery was professional, "
     "well-structured, tested, and ready for the next productisation phase. I would confidently work with Vinicius "
     "again.", "recent client review"),
    ("completed the work ahead of schedule and with accuracy. I would hire him again.", "another client review"),
]


def quote_card(text: str, who: str) -> str:
    x = 56
    lines = wrap(f"“{text}”", W - 2 * x, 19, per_em=0.47)
    parts = [f'<text x="{x - 8}" y="96" font-family="Georgia,serif" font-size="96" fill="{C["amberdim"]}">“</text>',
             eyebrow(x + 50, 58, "CLIENT REVIEW")]
    t, y = text_block(x, 112, lines, 19, C["text"], 31, SANS, italic=True, justify=W - 2 * x)
    parts.append(t)
    w, _ = text_block(x, y + 46, [f"· {who}"], 13.5, C["muted"], 20, MONO)
    parts.append(w)
    return frame(y + 80, "\n  ".join(parts), f"Client review: {text} ({who})")


CTA_HEAD = "Open to AI engineering, RAG, agents, and data work."
CTA_LINES = ["RAG and LLM systems, agents and automations, scraping and data pipelines, all built with tests and CI.",
             "Based in Brazil, working with clients worldwide."]


def cta() -> str:
    parts = [f'<text x="{W / 2}" y="70" text-anchor="middle" font-family="{MONO}" font-size="13" letter-spacing="3" font-weight="700" fill="{C["amber"]}">STATUS · ACCEPTING MISSIONS</text>',
             f'<text x="{W / 2}" y="122" text-anchor="middle" font-family="{SANS}" font-size="32" font-weight="700" fill="{C["white"]}">{esc(CTA_HEAD)}</text>']
    for i, line in enumerate(CTA_LINES):
        parts.append(f'<text x="{W / 2}" y="{166 + i * 30}" text-anchor="middle" font-family="{SANS}" font-size="18" fill="{C["soft"]}">{esc(line)}</text>')
    parts.append(f'<circle cx="{W / 2 - 182}" cy="65" r="4" fill="{C["green"]}"><animate attributeName="opacity" values="1;0.3;1" dur="2s" repeatCount="indefinite"/></circle>')
    return frame(236, "\n  ".join(parts), f"{CTA_HEAD} {' '.join(CTA_LINES)}")


def main() -> None:
    out = {
        "brief.svg": brief(),
        "button-portfolio.svg": button("OPEN THE FULL PORTFOLIO · VINIMABREU.DEV ↗"),
        "button-casestudies.svg": button("CASE STUDIES · VINIMABREU.DEV ↗"),
        "handbook.svg": handbook((HERE / "handbook-cover.jpg").read_bytes()),
        "chip-read-the-pdf.svg": chip("READ THE PDF ↗"),
        "chip-star-the-repo.svg": chip("STAR THE REPO ★"),
        "chip-chapters-on-devto.svg": chip("CHAPTERS ON DEV.TO ↗"),
        "review.svg": REVIEW,
        "upstream.svg": UPSTREAM,
        "security.svg": SECURITY,
        "how-i-work.svg": how_i_work(),
        "quote-1.svg": quote_card(*REVIEWS[0]),
        "quote-2.svg": quote_card(*REVIEWS[1]),
        "cta.svg": cta(),
    }
    for key, (number, name, tagline) in SECTORS.items():
        out[f"sector-{key}.svg"] = sector(number, name, tagline)
    rows = json.loads((HERE / "rows.json").read_text(encoding="utf-8"))
    for r in rows:
        out[f"row-{r['slug']}.svg"] = row(r["index"], r["name"], r["desc"], r.get("extra", ""))
    for name, svg in out.items():
        (HERE / name).write_text(svg, encoding="utf-8")
    print(f"wrote {len(out)} panels")


if __name__ == "__main__":
    main()
