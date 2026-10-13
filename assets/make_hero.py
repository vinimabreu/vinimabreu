"""The top of the profile as one continuous panel: header, house rule, mission console and receipts.

    python3 assets/make_console.py && python3 assets/make_hero.py

Built from the pieces the other scripts write (header.svg, brief.svg,
console.svg, the proof tiles), each nested at its offset inside one SVG with
its ids prefixed, so the console's daily refresh carries into the hero.
"""

from __future__ import annotations

import re
from pathlib import Path

import make_proof

HERE = Path(__file__).resolve().parent
W = 1200
PAD = 36
GROUND, HAIR, AMBER, MUTED = "#05070A", "#1C2530", "#FFB000", "#6B7683"
MONO = "ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,monospace"


def strip_frame(svg: str) -> str:
    """Drop a piece's own outer border, so the pieces share the hero's single frame."""
    return re.sub(r'<rect x="1" y="1" width="\d+" height="\d+" rx="14" fill="#05070A" stroke="#26313D"/>', "", svg, count=1)


def strip_glow(svg: str) -> str:
    """Drop a piece's own corner glow; the hero draws one glow across all pieces instead."""
    return re.sub(r'<rect[^>]*fill="url\(#glow\)"/>', "", svg)


def nest(svg: str, prefix: str, x: float, y: float, w: float) -> tuple[str, float]:
    """Place a whole SVG document at (x, y), scaled to width w; returns the markup and its height."""
    vb = re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', svg)
    vw, vh = float(vb.group(1)), float(vb.group(2))
    h = w * vh / vw
    body = svg[svg.index(">", svg.index("<svg")) + 1:svg.rindex("</svg>")]
    body = re.sub(r'id="([^"]+)"', lambda m: f'id="{prefix}-{m.group(1)}"', body)
    body = re.sub(r'url\(#([^)]+)\)', lambda m: f'url(#{prefix}-{m.group(1)})', body)
    return (f'<svg x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" viewBox="0 0 {vw:g} {vh:g}">{body}</svg>', h)


def main() -> None:
    # the header's own ground and rounded corners would show as a box inside the hero
    header = strip_glow((HERE / "header.svg").read_text(encoding="utf-8"))
    header = re.sub(r'<rect width="\d+" height="\d+" rx="14" fill="#05070A"/>', "", header).replace('rx="14"', 'rx="0"')
    brief = strip_frame((HERE / "brief.svg").read_text(encoding="utf-8"))
    console = strip_glow(strip_frame((HERE / "console.svg").read_text(encoding="utf-8")))
    parts, y = [], 0.0

    piece, h = nest(header, "hd", 0, y, W); parts.append(piece); y += h
    piece, h = nest(brief, "br", 0, y, W); parts.append(piece); y += h
    parts.append(f'<line x1="{PAD}" y1="{y:.1f}" x2="{W - PAD}" y2="{y:.1f}" stroke="{HAIR}"/>')
    piece, h = nest(console, "co", 0, y, W); parts.append(piece); y += h

    # receipts: the same tiles as the proof strip, without the per-tile VERIFY link
    parts.append(f'<line x1="{PAD}" y1="{y:.1f}" x2="{W - PAD}" y2="{y:.1f}" stroke="{HAIR}"/>')
    y += 44
    parts.append(f'<text x="{PAD}" y="{y:.1f}" font-family="{MONO}" font-size="13" letter-spacing="3" font-weight="700" fill="{AMBER}">RECEIPTS</text>')
    parts.append(f'<text x="{W - PAD}" y="{y:.1f}" text-anchor="end" font-family="{MONO}" font-size="12" letter-spacing="2" fill="{MUTED}">VERIFY AT VINIMABREU.DEV/PROOF</text>')
    y += 22
    tile_w = (W - 2 * PAD - 18) / 2
    for i, (stem, label, name, detail) in enumerate(make_proof.TILES):
        tile = make_proof.tile(label, name, detail)
        tile = re.sub(r'<text[^>]*>VERIFY ↗</text>', "", tile)
        piece, h = nest(tile, f"pf{i}", PAD + (i % 2) * (tile_w + 18), y + (i // 2) * (tile_w * 112 / 480 + 14), tile_w)
        parts.append(piece)
    y += 2 * (tile_w * 112 / 480) + 14 + PAD

    alt = re.search(r'aria-label="([^"]*)"', console).group(1)
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {y:.0f}" role="img" '
           f'aria-label="Vinicius Pereira, AI systems that are grounded, tested, and honest. {alt}">\n'
           f'  <defs><radialGradient id="heroglow" cx="0.92" cy="0.18" r="0.55"><stop offset="0" stop-color="{AMBER}" stop-opacity="0.13"/>'
           f'<stop offset="1" stop-color="{AMBER}" stop-opacity="0"/></radialGradient>'
           f'<radialGradient id="heroglow2" cx="0.9" cy="0.82" r="0.5"><stop offset="0" stop-color="{AMBER}" stop-opacity="0.08"/>'
           f'<stop offset="1" stop-color="{AMBER}" stop-opacity="0"/></radialGradient></defs>\n'
           f'  <rect x="1" y="1" width="{W - 2}" height="{y - 2:.0f}" rx="16" fill="{GROUND}" stroke="#26313D"/>\n'
           f'  <rect x="1" y="1" width="{W - 2}" height="{y - 2:.0f}" rx="16" fill="url(#heroglow)"/>\n'
           f'  <rect x="1" y="1" width="{W - 2}" height="{y - 2:.0f}" rx="16" fill="url(#heroglow2)"/>\n  '
           + "\n  ".join(parts) + "\n</svg>\n")
    (HERE / "hero.svg").write_text(svg, encoding="utf-8")
    print(f"wrote hero.svg ({len(svg)} bytes, {y:.0f}px tall)")


if __name__ == "__main__":
    main()
