"""Draw the mission console from telemetry.json: a radar of every public repo, live readouts, a launch ticker.

    python3 assets/collect_telemetry.py && python3 assets/make_console.py

Same palette and type as vinimabreu.dev (ground #05070A, amber #FFB000). Each repo
is a blip on the radar: the closer to the centre, the more recently it launched.
Flagships are amber and named; the sweep lights each blip as it passes. Plain SVG
with SMIL and CSS animation, no script and no external font, so GitHub serves it
as-is inside the README.
"""

from __future__ import annotations

import json
import math
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent

W, H = 1200, 500
MONO = "ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,monospace"
C = {
    "ground": "#05070A", "panel": "#0A0E14", "hair": "#1C2530", "hair2": "#26313D",
    "amber": "#FFB000", "amberdim": "#7A5600", "green": "#37D67A", "text": "#D8E1E8", "muted": "#6B7683",
}
CX, CY, R = 238, 258, 160      # radar
SWEEP = 6.0                     # seconds per revolution
MONTHS = "JAN FEB MAR APR MAY JUN JUL AUG SEP OCT NOV DEC".split()


def esc(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def stamp(iso: str) -> str:
    d = date.fromisoformat(iso)
    return f"{d.day:02d} {MONTHS[d.month - 1]} {d.year}"


def short(iso: str) -> str:
    d = date.fromisoformat(iso)
    return f"{d.day:02d} {MONTHS[d.month - 1]}"


def clip(text: str, n: int) -> str:
    return text if len(text) <= n else text[: n - 1].rstrip() + "…"


def radar(data: dict) -> str:
    today = date.fromisoformat(data["collected"])
    projects = data["projects"]
    oldest = max((today - date.fromisoformat(p["created"])).days for p in projects) or 1
    parts = [
        f'<circle cx="{CX}" cy="{CY}" r="{R}" fill="{C["panel"]}" stroke="{C["hair2"]}"/>',
    ]
    # rings at one, three and six months
    for days, label in ((30, "1 MO"), (91, "3 MO"), (182, "6 MO")):
        r = R * min(1, days / oldest)
        parts.append(f'<circle cx="{CX}" cy="{CY}" r="{r:.1f}" fill="none" stroke="{C["hair"]}" stroke-dasharray="2 4"/>')
        parts.append(f'<text x="{CX + r - 4:.1f}" y="{CY + 13}" text-anchor="end" font-family="{MONO}" font-size="9" fill="{C["muted"]}" letter-spacing="1">{label}</text>')
    parts.append(f'<line x1="{CX - R}" y1="{CY}" x2="{CX + R}" y2="{CY}" stroke="{C["hair"]}"/>')
    parts.append(f'<line x1="{CX}" y1="{CY - R}" x2="{CX}" y2="{CY + R}" stroke="{C["hair"]}"/>')
    # sweep: a soft wedge and an arm, rotating forever
    wedge = []
    for i in range(10):
        a0, a1 = math.radians(-90 - (i + 1) * 4), math.radians(-90 - i * 4)
        x0, y0 = CX + R * math.cos(a0), CY + R * math.sin(a0)
        x1, y1 = CX + R * math.cos(a1), CY + R * math.sin(a1)
        wedge.append(f'<path d="M{CX},{CY} L{x0:.1f},{y0:.1f} A{R},{R} 0 0 1 {x1:.1f},{y1:.1f} Z" '
                     f'fill="{C["amber"]}" opacity="{0.16 * (1 - i / 10):.3f}"/>')
    parts.append(
        f'<g>{"".join(wedge)}<line x1="{CX}" y1="{CY}" x2="{CX}" y2="{CY - R}" stroke="{C["amber"]}" stroke-width="1.5"/>'
        f'<animateTransform attributeName="transform" type="rotate" from="0 {CX} {CY}" to="360 {CX} {CY}" '
        f'dur="{SWEEP:g}s" repeatCount="indefinite"/></g>'
    )
    # blips: radius by age; flagships get fixed bearings so their names never collide,
    # the rest spread by the golden angle in launch order
    golden = 137.508
    bearings = {name: 15 + 60 * k for k, name in enumerate(data["flagships"])}
    labels = []
    for i, p in enumerate(projects):
        age = (today - date.fromisoformat(p["created"])).days
        r = 18 + (R - 26) * (age / oldest)
        deg = bearings.get(p["name"], (i * golden) % 360)   # 0 = up, clockwise, like the sweep
        a = math.radians(deg - 90)
        x, y = CX + r * math.cos(a), CY + r * math.sin(a)
        flagship = p["name"] in data["flagships"]
        colour = C["amber"] if flagship else C["text"]
        size = 3.6 if flagship else 2.2
        begin = SWEEP * deg / 360
        glow = (f'<animate attributeName="opacity" values="1;0.35;0.35" keyTimes="0;0.55;1" dur="{SWEEP:g}s" '
                f'begin="{begin:.2f}s" repeatCount="indefinite"/>')
        parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{size}" fill="{colour}" opacity="0.35">{glow}</circle>')
        if flagship:
            parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{size + 4}" fill="none" stroke="{C["amber"]}" '
                         f'stroke-width="0.8" opacity="0.5"/>')
            anchor = "start" if x >= CX else "end"
            dx = 9 if x >= CX else -9
            labels.append(f'<text x="{x + dx:.1f}" y="{y + 3.5:.1f}" text-anchor="{anchor}" font-family="{MONO}" '
                          f'font-size="10.5" fill="{C["amber"]}">{esc(p["name"])}</text>')
    parts.extend(labels)
    parts.append(f'<circle cx="{CX}" cy="{CY}" r="3" fill="{C["amber"]}"/>')
    parts.append(f'<text x="{CX}" y="{CY + R + 26}" text-anchor="middle" font-family="{MONO}" font-size="10" '
                 f'fill="{C["muted"]}" letter-spacing="2">CENTRE = TODAY · {len(projects)} PUBLIC REPOS</text>')
    return "\n  ".join(parts)


def readouts(data: dict) -> str:
    x0, x1 = 480, 640
    flags = [p for p in data["projects"] if p["name"] in data["flagships"]]
    green = sum(1 for p in flags if p.get("ci") == "success")
    # NOMINAL only when every flagship's latest CI run passed; anything else says so
    status = ([("● ", "green"), ("NOMINAL", "text")] if green == len(flags) and flags
              else [("● ", "amber"), (f"CHECK: {len(flags) - green} flagship CI not green", "text")])
    rows = [
        ("STATUS", status),
        ("WRITE-UPS", [(str(data.get("articles_published", "")), "amber"), ("  published on dev.to", "muted")]),
        ("PUBLIC REPOS", [(str(data["project_count"]), "amber")]),
        ("TESTS STATED", [(f'{data["tests_total"]:,}', "amber"), (f'  across {data["repos_with_tests"]} READMEs', "muted")]),
        ("LAST LAUNCH", [(data["last_launch"], "amber"), (f'  {stamp(data["last_launch_date"])}', "muted")]),
    ]
    art = data.get("latest_article")
    if art:
        rows.append(("LAST WRITE-UP", [(clip(art["title"], 52), "text")]))
    rows.append(("FLAGSHIP CI", [(f"{green}/{len(flags)} ", "green" if green == len(flags) else "amber"), ("passing on the last run", "muted")]))
    out = []
    y = 120
    for i, (label, segs) in enumerate(rows):
        reveal = (f'<animate attributeName="opacity" from="0" to="1" begin="{0.35 + i * 0.28:.2f}s" dur="0.25s" fill="freeze"/>')
        spans = "".join(f'<tspan fill="{C[c]}">{esc(t)}</tspan>' for t, c in segs)
        out.append(f'<g opacity="0">{reveal}'
                   f'<text x="{x0}" y="{y}" font-family="{MONO}" font-size="11" fill="{C["muted"]}" letter-spacing="2">{label}</text>'
                   f'<text x="{x1}" y="{y}" font-family="{MONO}" font-size="15">{spans}</text>'
                   f'<line x1="{x0}" y1="{y + 14}" x2="{W - 40}" y2="{y + 14}" stroke="{C["hair"]}"/></g>')
        y += 38
    # the status dot breathes
    out.append(f'<circle cx="{x1 + 5}" cy="115" r="9" fill="{C["green"]}" opacity="0">'
               f'<animate attributeName="opacity" values="0;0.25;0" dur="2.2s" begin="0.6s" repeatCount="indefinite"/></circle>')
    return "\n  ".join(out)


def cadence(data: dict) -> str:
    """Launches per month, from each repo's creation date: one bar per month."""
    counts: dict[str, int] = {}
    for p in data["projects"]:
        counts[p["created"][:7]] = counts.get(p["created"][:7], 0) + 1
    months = sorted(counts)
    x0, y_base, bar_w, gap, max_h = 640, 432, 34, 18, 52
    top = max(counts.values())
    parts = [f'<text x="480" y="{y_base - 18}" font-family="{MONO}" font-size="11" fill="{C["muted"]}" letter-spacing="2">LAUNCHES / MONTH</text>']
    for i, m in enumerate(months):
        h = max(3, max_h * counts[m] / top)
        x = x0 + i * (bar_w + gap)
        last = i == len(months) - 1
        grow = (f'<animate attributeName="height" from="0" to="{h:.1f}" begin="{2.4 + i * 0.12:.2f}s" dur="0.5s" fill="freeze"/>'
                f'<animate attributeName="y" from="{y_base}" to="{y_base - h:.1f}" begin="{2.4 + i * 0.12:.2f}s" dur="0.5s" fill="freeze"/>')
        parts.append(f'<rect x="{x}" y="{y_base}" width="{bar_w}" height="0" fill="{C["amber"] if last else C["amberdim"]}">{grow}</rect>')
        parts.append(f'<text x="{x + bar_w / 2}" y="{y_base - h - 6:.1f}" text-anchor="middle" font-family="{MONO}" font-size="10" '
                     f'fill="{C["amber"] if last else C["muted"]}" opacity="0">{counts[m]}'
                     f'<animate attributeName="opacity" from="0" to="1" begin="{2.9 + i * 0.12:.2f}s" dur="0.3s" fill="freeze"/></text>')
        parts.append(f'<text x="{x + bar_w / 2}" y="{y_base + 14}" text-anchor="middle" font-family="{MONO}" font-size="9.5" '
                     f'fill="{C["muted"]}" letter-spacing="1">{MONTHS[int(m[5:]) - 1]}</text>')
    return "\n  ".join(parts)


def ticker(data: dict) -> str:
    items = "   ·   ".join(f'{p["name"]} {short(p["created"])}' for p in data["projects"][:12])
    text = f"LAUNCH LOG   {items}   ·   "
    width = len(text) * 7.2  # 12px mono advance, approximately
    y = H - 22
    run = (f'<text y="{y}" font-family="{MONO}" font-size="12" fill="{C["muted"]}" letter-spacing="0.5">'
           f'<tspan x="0">{esc(text)}</tspan><tspan x="{width:.0f}">{esc(text)}</tspan></text>')
    return (f'<clipPath id="tk"><rect x="20" y="{y - 16}" width="{W - 40}" height="24"/></clipPath>'
            f'<line x1="20" y1="{y - 22}" x2="{W - 20}" y2="{y - 22}" stroke="{C["hair"]}"/>'
            f'<g clip-path="url(#tk)"><g>{run}<animateTransform attributeName="transform" type="translate" '
            f'from="20 0" to="{20 - width:.0f} 0" dur="{width / 40:.0f}s" repeatCount="indefinite"/></g></g>')


def build(data: dict) -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img"
     aria-label="Mission console: {data['project_count']} public repos on a radar, {data['tests_total']:,} tests stated across {data['repos_with_tests']} READMEs, last launch {esc(data['last_launch'] or '')}, updated {data['collected']}">
  <defs>
    <pattern id="scan" width="4" height="3" patternUnits="userSpaceOnUse"><rect width="4" height="1" fill="#FFFFFF" opacity="0.018"/></pattern>
    <radialGradient id="glow" cx="0.85" cy="1" r="0.7"><stop offset="0" stop-color="{C['amber']}" stop-opacity="0.10"/><stop offset="1" stop-color="{C['amber']}" stop-opacity="0"/></radialGradient>
  </defs>
  <rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="14" fill="{C['ground']}" stroke="{C['hair2']}"/>
  <rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="14" fill="url(#glow)"/>
  <text x="32" y="44" font-family="{MONO}" font-size="12" fill="{C['amber']}" letter-spacing="3" font-weight="700">MISSION CONSOLE</text>
  <text x="{W - 32}" y="44" text-anchor="end" font-family="{MONO}" font-size="11" fill="{C['muted']}" letter-spacing="2">LIVE TELEMETRY · UPDATED {stamp(data['collected'])}</text>
  <line x1="20" y1="62" x2="{W - 20}" y2="62" stroke="{C['hair']}"/>
  {radar(data)}
  {readouts(data)}
  {cadence(data)}
  {ticker(data)}
  <rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="14" fill="url(#scan)"/>
</svg>
"""


def main() -> None:
    data = json.loads((HERE / "telemetry.json").read_text(encoding="utf-8"))
    out = HERE / "console.svg"
    out.write_text(build(data), encoding="utf-8")
    print(f"wrote {out.name} ({out.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
