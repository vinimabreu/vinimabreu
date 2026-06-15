"""Generate GitHub social-preview cards (1280x640 PNG) for every repo.

    python3 assets/make_social_cards.py

Renders one brand-purple card per repository via Playwright (Chromium
screenshot of an inline HTML template) into ~/Desktop/social-cards/.
Upload each at the repo's Settings > Social preview. Needs Playwright
(pip install playwright && playwright install chromium).
"""

from pathlib import Path

from playwright.sync_api import sync_playwright

OUT = Path.home() / "Desktop" / "social-cards"

REPOS = {
    "retell-sms-handler": "An In-Call SMS for your Retell voice agent that fires every time, with consent logged and the number resolved in code",
    "grounded-copy": "On-brand product copy from your catalog, with every invented spec, price or claim caught before it ships",
    "source-of-truth": "Scattered sources in, one trustworthy answer out, with cross-source conflicts and stale sources flagged",
    "record-refinery": "Raw business records in, a clean validated deduplicated dataset and a QA brief out",
    "rag-chat": "Chat with your docs: grounded answers, clickable citations, an honest \"I don't know\"",
    "web-pilot": "A browser-use agent whose guardrails are enforced in code, not in the prompt",
    "voice-receptionist": "An AI phone receptionist that books against a live calendar and logs every call",
    "doc-eval": "Field-level evaluation and a CI release gate for LLM document extraction",
    "multi-agent-analyst": "A planner, worker, verifier crew that cites its evidence or honestly refuses",
    "sql-agent": "Plain English to SQL, with a real self-correction loop, on a read-only connection",
    "mcp-listings": "An MCP server exposing live data to Claude as typed tools",
    "n8n-lead-triage": "n8n routes, a tested service decides, a human catches the rest",
    "rag-quality": "A RAG pipeline that measures its own retrieval quality instead of assuming it",
    "mini-rag": "A small, working RAG API on FastAPI, Chroma and Claude",
    "pdf-extract": "PDF documents into validated structured JSON, with pluggable OCR",
    "docs-to-markdown": "Any documentation site into a clean Markdown corpus, ready for RAG",
    "ai-watcher": "Watches feeds and turns new articles into structured AI summaries",
    "bcb-data-pipeline": "Daily ETL of Brazilian macro indicators from the central bank API",
    "web-scraper": "A Playwright scraper, SQLite storage and a Streamlit dashboard, end to end",
}

TEMPLATE = """<!DOCTYPE html>
<html><head><style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{
    width: 1280px; height: 640px; background: #0D1117;
    font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
    display: flex; flex-direction: column; justify-content: space-between;
  }}
  .bar {{ height: 14px; width: 100%;
    background: linear-gradient(90deg, #6E56CF, #8B7BD8, #A78BFA); }}
  .main {{ padding: 0 90px; }}
  .owner {{ color: #8B949E; font-size: 26px; margin-bottom: 18px; }}
  h1 {{ color: #E6EDF3; font-size: 76px; font-weight: 700;
       letter-spacing: -2px; margin-bottom: 30px; }}
  h1 span {{ color: #A78BFA; }}
  .desc {{ color: #9DA7B3; font-size: 32px; line-height: 1.45;
           max-width: 1050px; }}
  .foot {{ padding: 0 90px 46px; color: #6E56CF; font-size: 26px;
           font-weight: 600; }}
</style></head>
<body>
  <div class="bar"></div>
  <div class="main">
    <div class="owner">github.com/vinimabreu</div>
    <h1><span>&gt;</span> {name}</h1>
    <div class="desc">{desc}</div>
  </div>
  <div class="foot">the model proposes, the code disposes</div>
</body></html>"""


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1280, "height": 640})
        for name, desc in REPOS.items():
            page.set_content(TEMPLATE.format(name=name, desc=desc))
            page.screenshot(path=str(OUT / f"{name}.png"))
            print(f"wrote {name}.png")
        browser.close()
    print(f"\n{len(REPOS)} cards em {OUT}")


if __name__ == "__main__":
    main()
