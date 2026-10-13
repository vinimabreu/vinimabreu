"""The Stack section as one instrumentation panel: a card per category, a pill per tool, each with its icon.

    python3 assets/make_stack.py

Icons are Simple Icons path data (CC0), stored in stack_icons.json so the panel
draws offline; a tool with no Simple Icons entry gets a plain amber marker.
"""

from __future__ import annotations

import html
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
MONO = "ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,monospace"
SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif"
C = {"ground": "#05070A", "panel": "#0A0E14", "hair": "#1C2530", "hair2": "#26313D", "amber": "#FFB000",
     "amberdim": "#7A5600", "text": "#D8E1E8", "muted": "#6B7683", "white": "#F2F5F8"}

# category -> tools as (name, Simple Icons slug or "")
STACK = [
    ("CORE", [("Python", "python"), ("FastAPI", "fastapi"), ("Django + DRF", "django"), ("Celery", "celery"), ("Flask", "flask"),
              ("Pydantic", "pydantic"), ("pytest", "pytest"), ("pandas", "pandas"), ("NumPy", "numpy")]),
    ("MODELS", [("Claude API", "anthropic"), ("OpenAI", "openai"), ("Gemini", "googlegemini"), ("Ollama", "ollama"), ("Gemma", "google"),
                ("Llama", "meta"), ("Qwen", ""), ("Mistral", "mistralai"), ("LM Studio", ""), ("Hugging Face", "huggingface")]),
    ("AUTOMATION", [("n8n", "n8n"), ("Make", "make"), ("Clay", ""), ("Airtable", "airtable"), ("Xero", "xero"), ("Dropbox", "dropbox"),
                    ("PDFMonkey", ""), ("Microsoft 365", ""), ("Twilio", "twilio"), ("Retell", ""), ("ElevenLabs", "elevenlabs"), ("Streamlit", "streamlit")]),
    ("RETRIEVAL", [("Chroma", ""), ("Qdrant", ""), ("pgvector", "postgresql"), ("BM25 + dense embeddings", ""), ("SQLite", "sqlite")]),
    ("AGENTS", [("LangGraph", "langgraph"), ("LangChain", "langchain"), ("CrewAI", "crewai"), ("MCP", "modelcontextprotocol"), ("Google ADK + A2A", "google")]),
    ("EXTRACTION", [("Playwright", ""), ("Selenium", "selenium"), ("Scrapy", "scrapy"), ("Tesseract OCR", ""), ("AWS Textract", "")]),
    ("FULL-STACK WEB", [("TypeScript", "typescript"), ("JavaScript", "javascript"), ("React", "react"), ("Next.js", "nextdotjs"), ("Vue", "vuedotjs"),
                        ("Node.js", "nodedotjs"), ("Vite", "vite"), ("Deno", "deno"), ("Capacitor", "capacitor"), ("Vercel", "vercel"), ("Supabase", "supabase")]),
    ("IDENTITY & TRUST", [("AWS Rekognition face match", ""), ("document + liveness KYC flows", ""), ("privacy-by-design under LGPD", "")]),
    ("OPS", [("Docker", "docker"), ("GitHub Actions", "githubactions"), ("PostgreSQL", "postgresql"), ("Google Cloud Run", "googlecloud")]),
]

W = 1200
PAD, GAP, COLS = 36, 18, 3
CARD_W = (W - 2 * PAD - (COLS - 1) * GAP) / COLS
INNER = CARD_W - 2 * 18
PILL_H, PILL_GAP, ICON = 30, 8, 14
FONT = 13


def esc(text: str) -> str:
    return html.escape(text, quote=True)


def pill_w(name: str) -> float:
    return 12 + ICON + 8 + len(name) * FONT * 0.6 + 14


def layout(tools: list[tuple[str, str]]) -> list[list[tuple[str, str, float]]]:
    rows, row, used = [], [], 0.0
    for name, slug in tools:
        w = pill_w(name)
        if row and used + PILL_GAP + w > INNER:
            rows.append(row); row, used = [], 0.0
        row.append((name, slug, w)); used += (PILL_GAP if len(row) > 1 else 0) + w
    if row:
        rows.append(row)
    return rows


def card(x: float, y: float, h: float, label: str, rows, icons: dict) -> str:
    parts = [f'<rect x="{x:.1f}" y="{y:.1f}" width="{CARD_W:.1f}" height="{h:.1f}" rx="10" fill="{C["panel"]}" stroke="{C["hair2"]}"/>',
             f'<rect x="{x:.1f}" y="{y:.1f}" width="{CARD_W:.1f}" height="3" fill="{C["amber"]}" opacity="0.85"/>',
             f'<text x="{x + 18:.1f}" y="{y + 34:.1f}" font-family="{MONO}" font-size="12" letter-spacing="2.5" font-weight="700" fill="{C["amber"]}">{esc(label)}</text>',
             f'<text x="{x + CARD_W - 18:.1f}" y="{y + 34:.1f}" text-anchor="end" font-family="{MONO}" font-size="11" fill="{C["muted"]}">{sum(len(r) for r in rows):02d}</text>']
    py = y + 52
    for row in rows:
        px = x + 18
        for name, slug, w in row:
            parts.append(f'<rect x="{px:.1f}" y="{py:.1f}" width="{w:.1f}" height="{PILL_H}" rx="15" fill="{C["ground"]}" stroke="{C["hair2"]}"/>')
            ix, iy = px + 12, py + (PILL_H - ICON) / 2
            if slug in icons:
                parts.append(f'<path transform="translate({ix:.1f},{iy:.1f}) scale({ICON / 24:.4f})" fill="{C["amber"]}" d="{icons[slug]}"/>')
            else:
                parts.append(f'<rect x="{ix + 3:.1f}" y="{iy + 3:.1f}" width="8" height="8" rx="1.5" fill="none" stroke="{C["amber"]}" stroke-width="1.5"/>')
            parts.append(f'<text x="{ix + ICON + 8:.1f}" y="{py + 20:.1f}" font-family="{SANS}" font-size="{FONT}" fill="{C["text"]}">{esc(name)}</text>')
            px += w + PILL_GAP
        py += PILL_H + PILL_GAP
    return "\n  ".join(parts)


def card_height(rows) -> float:
    return 52 + len(rows) * (PILL_H + PILL_GAP) - PILL_GAP + 18


def main() -> None:
    icons = json.loads((HERE / "stack_icons.json").read_text(encoding="utf-8"))
    laid = [(label, layout(tools)) for label, tools in STACK]
    total = sum(len(t) for _, t in STACK)
    head = 84
    parts, y = [], head
    for r in range(0, len(laid), COLS):
        band = laid[r:r + COLS]
        h = max(card_height(rows) for _, rows in band)
        for i, (label, rows) in enumerate(band):
            parts.append(card(PAD + i * (CARD_W + GAP), y, h, label, rows, icons))
        y += h + GAP
    height = y + PAD - GAP
    top = (f'<text x="{PAD}" y="50" font-family="{MONO}" font-size="13" letter-spacing="3" font-weight="700" fill="{C["amber"]}">INSTRUMENTATION</text>'
           f'<text x="{W - PAD}" y="50" text-anchor="end" font-family="{MONO}" font-size="12" letter-spacing="2" fill="{C["muted"]}">{total} TOOLS · {len(STACK)} SYSTEMS</text>'
           f'<line x1="{PAD}" y1="64" x2="{W - PAD}" y2="64" stroke="{C["hair"]}"/>')
    alt = "; ".join(f"{label.title()}: {', '.join(n for n, _ in tools)}" for label, tools in STACK)
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {height:.0f}" role="img" aria-label="{esc(alt)}">\n'
           f'  <rect x="1" y="1" width="{W - 2}" height="{height - 2:.0f}" rx="14" fill="{C["ground"]}" stroke="{C["hair2"]}"/>\n'
           f'  {top}\n  ' + "\n  ".join(parts) + "\n</svg>\n")
    (HERE / "stack.svg").write_text(svg, encoding="utf-8")
    (HERE / "stack-alt.txt").write_text(alt + "\n", encoding="utf-8")
    print(f"wrote stack.svg ({len(svg)} bytes, {total} tools)")


if __name__ == "__main__":
    main()
