"""Flagship cards in the mission palette, with each repo's live CI state and last push from telemetry.json.

    python3 assets/collect_telemetry.py && python3 assets/make_payload_cards.py

Also draws the header and the amber divider that replace the third-party banner and
separator bars, so the profile no longer depends on an outside image service.
"""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
MONO = "ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,monospace"
SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif"
C = {"ground": "#05070A", "panel": "#0A0E14", "hair": "#1C2530", "hair2": "#26313D", "amber": "#FFB000",
     "amberdim": "#7A5600", "green": "#37D67A", "red": "#FF5C5C", "text": "#D8E1E8", "muted": "#6B7683"}
MONTHS = "JAN FEB MAR APR MAY JUN JUL AUG SEP OCT NOV DEC".split()
W, H = 480, 164

# repo -> two description lines and the stack tag; tests come from telemetry, not from here
COPY = {
    "revenue-loop": (["A won CRM deal reaches Google and Meta", "exactly once, or waits in quarantine."], "Data Manager + CAPI"),
    "sequence-gate": (["Decides whether the next follow-up may", "fire: stop before the send, never twice."], "n8n / Make / Zapier"),
    "tenant-fence": (["Multi-tenant RAG: entitlements filter", "before top-k, so no ranking can leak."], "RAG"),
    "langgraph-production": (["A LangGraph support agent with a human", "gate and a resume that runs exactly once."], "LangGraph"),
    "taint-trail": (["Follows an untrusted Actions value after", "it moves, until it dies or hits a shell."], "CI security"),
    "betorskip": (["A local Gemma reads the bet slip; code", "checks every number and its arithmetic."], "Ollama + Gemma 4"),
}


def esc(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def short(iso: str) -> str:
    d = date.fromisoformat(iso)
    return f"{d.day:02d} {MONTHS[d.month - 1]}"


def card(index: int, project: dict) -> str:
    lines, tag = COPY[project["name"]]
    ci = project.get("ci")
    ci_text, ci_colour = {"success": ("CI PASSING", "green"), "failure": ("CI FAILING", "red")}.get(ci, ("CI UNKNOWN", "muted"))
    meta = " · ".join(x for x in ("Python", tag, f'{project["tests"]:,} tests' if project.get("tests") else "", f'pushed {short(project["pushed"])}') if x)
    desc = "".join(f'<text x="26" y="{88 + i * 23}" font-family="{SANS}" font-size="14" fill="{C["text"]}">{esc(t)}</text>'
                   for i, t in enumerate(lines))
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img"
     aria-label="{esc(project['name'])}: {esc(' '.join(lines))} {ci_text.lower()}, {esc(meta)}">
  <rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="12" fill="{C['ground']}" stroke="{C['hair2']}"/>
  <rect x="1" y="22" width="3" height="{H - 44}" fill="{C['amber']}"/>
  <text x="26" y="30" font-family="{MONO}" font-size="10" fill="{C['muted']}" letter-spacing="2.5">PAYLOAD {index:02d}</text>
  <circle cx="{W - 120}" cy="26.5" r="3.5" fill="{C[ci_colour]}"><animate attributeName="opacity" values="1;0.35;1" dur="2.4s" repeatCount="indefinite"/></circle>
  <text x="{W - 26}" y="30" text-anchor="end" font-family="{MONO}" font-size="10" fill="{C[ci_colour]}" letter-spacing="2">{ci_text}</text>
  <text x="26" y="60" font-family="{MONO}" font-size="20" font-weight="700" fill="{C['amber']}">{esc(project['name'])}</text>
  {desc}
  <line x1="26" y1="{H - 38}" x2="{W - 26}" y2="{H - 38}" stroke="{C['hair']}"/>
  <text x="26" y="{H - 18}" font-family="{MONO}" font-size="11" fill="{C['muted']}">{esc(meta)}</text>
</svg>
"""


def divider() -> str:
    w, h = 1200, 18
    ticks = "".join(f'<line x1="{x}" y1="7" x2="{x}" y2="11" stroke="#26313D"/>' for x in range(20, w, 40))
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-label="">
  <defs><linearGradient id="g" x1="0" x2="1"><stop offset="0" stop-color="{C['amber']}" stop-opacity="0"/><stop offset="0.5" stop-color="{C['amber']}" stop-opacity="0.9"/><stop offset="1" stop-color="{C['amber']}" stop-opacity="0"/></linearGradient></defs>
  <line x1="0" y1="9" x2="{w}" y2="9" stroke="#26313D"/>
  {ticks}
  <rect x="300" y="8" width="600" height="2" fill="url(#g)"/>
  <circle cy="9" r="2.5" fill="{C['amber']}"><animate attributeName="cx" values="0;{w}" dur="9s" repeatCount="indefinite"/><animate attributeName="opacity" values="0;1;1;0" keyTimes="0;0.08;0.92;1" dur="9s" repeatCount="indefinite"/></circle>
</svg>
"""


def header() -> str:
    w, h = 1200, 230
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-label="Vinicius Pereira. AI systems that are grounded, tested, and honest.">
  <defs>
    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="#FFFFFF" stroke-opacity="0.03"/></pattern>
    <radialGradient id="glow" cx="0.9" cy="1.1" r="0.8"><stop offset="0" stop-color="{C['amber']}" stop-opacity="0.22"/><stop offset="1" stop-color="{C['amber']}" stop-opacity="0"/></radialGradient>
  </defs>
  <rect width="{w}" height="{h}" rx="14" fill="{C['ground']}"/>
  <rect width="{w}" height="{h}" rx="14" fill="url(#grid)"/>
  <rect width="{w}" height="{h}" rx="14" fill="url(#glow)"/>
  <text x="{w / 2}" y="62" text-anchor="middle" font-family="{MONO}" font-size="13" fill="{C['amber']}" letter-spacing="4" font-weight="700">VINIMABREU · MISSION CONTROL</text>
  <text x="{w / 2}" y="136" text-anchor="middle" font-family="{SANS}" font-size="64" font-weight="700" fill="#F2F5F8" letter-spacing="-1.5">Vinicius Pereira</text>
  <text x="{w / 2}" y="178" text-anchor="middle" font-family="{MONO}" font-size="17" fill="{C['text']}">AI systems that are grounded, tested, and honest<tspan fill="{C['amber']}">_</tspan></text>
  <rect x="{w - 64}" y="44" width="8" height="8" fill="{C['amber']}"><animate attributeName="opacity" values="1;0.2;1" dur="1.6s" repeatCount="indefinite"/></rect>
  <line x1="56" y1="200" x2="{w - 56}" y2="200" stroke="{C['hair2']}"/>
  <rect x="{w / 2}" y="199" width="0" height="2" fill="{C['amber']}"><animate attributeName="x" from="{w / 2}" to="56" dur="1.4s" fill="freeze"/><animate attributeName="width" from="0" to="{w - 112}" dur="1.4s" fill="freeze"/></rect>
</svg>
"""


def main() -> None:
    data = json.loads((HERE / "telemetry.json").read_text(encoding="utf-8"))
    by_name = {p["name"]: p for p in data["projects"]}
    for i, name in enumerate(data["flagships"], start=1):
        (HERE / f"payload-{name}.svg").write_text(card(i, by_name[name]), encoding="utf-8")
    (HERE / "divider.svg").write_text(divider(), encoding="utf-8")
    (HERE / "header.svg").write_text(header(), encoding="utf-8")
    print(f"wrote {len(data['flagships'])} payload cards and divider.svg")


if __name__ == "__main__":
    main()
