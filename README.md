<img src="https://capsule-render.vercel.app/api?type=waving&color=0:6E56CF,50:8B7BD8,100:A78BFA&height=210&section=header&text=Vinicius%20Pereira&fontSize=54&fontColor=FFFFFF&fontAlignY=36&desc=AI%20systems%20that%20are%20grounded%2C%20tested%2C%20and%20honest&descSize=17&descAlignY=58&animation=fadeIn" width="100%" alt="Vinicius Pereira. AI systems that are grounded, tested, and honest." />

> **The model proposes, the code disposes.**<br>
> The model holds the conversation. Tested code makes every decision that matters.

I build retrieval, agents, MCP servers, voice, and automation with that one rule at the center. The flagships ship deterministic test suites that need no API key, show captured output from actual runs, and come with an architecture diagram; every README is honest about the trade-offs. Sixteen public projects, more than 200 deterministic tests, one rule.

<p align="center">
<img src="https://img.shields.io/badge/Python-6E56CF?style=flat-square&logo=python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/FastAPI-6E56CF?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI">
<img src="https://img.shields.io/badge/Pydantic-6E56CF?style=flat-square&logo=pydantic&logoColor=white" alt="Pydantic">
<img src="https://img.shields.io/badge/pytest-6E56CF?style=flat-square&logo=pytest&logoColor=white" alt="pytest">
<img src="https://img.shields.io/badge/Playwright-6E56CF?style=flat-square&logo=playwright&logoColor=white" alt="Playwright">
<img src="https://img.shields.io/badge/pandas-6E56CF?style=flat-square&logo=pandas&logoColor=white" alt="pandas">
<img src="https://img.shields.io/badge/Claude-6E56CF?style=flat-square&logo=anthropic&logoColor=white" alt="Claude">
<img src="https://img.shields.io/badge/Chroma-6E56CF?style=flat-square&logo=chromadb&logoColor=white" alt="Chroma">
<img src="https://img.shields.io/badge/SQLite-6E56CF?style=flat-square&logo=sqlite&logoColor=white" alt="SQLite">
<img src="https://img.shields.io/badge/Docker-6E56CF?style=flat-square&logo=docker&logoColor=white" alt="Docker">
<img src="https://img.shields.io/badge/n8n-6E56CF?style=flat-square&logo=n8n&logoColor=white" alt="n8n">
<img src="https://img.shields.io/badge/Twilio-6E56CF?style=flat-square&logo=twilio&logoColor=white" alt="Twilio">
<img src="https://img.shields.io/badge/GitHub%20Actions-6E56CF?style=flat-square&logo=githubactions&logoColor=white" alt="GitHub Actions">
</p>

<sub><a href="#the-house-rule-running">The rule, running</a> &middot; <a href="#flagships">Flagships</a> &middot; <a href="#retrieval-and-rag">Retrieval and RAG</a> &middot; <a href="#agents-and-tools">Agents and tools</a> &middot; <a href="#voice-and-automation">Voice and automation</a> &middot; <a href="#evaluation-and-quality">Evaluation and quality</a> &middot; <a href="#data-engineering-and-extraction">Data engineering and extraction</a> &middot; <a href="#stack">Stack</a> &middot; <a href="#how-i-work">How I work</a></sub>

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:6E56CF,50:8B7BD8,100:A78BFA&height=4" width="100%" alt="" />

## The house rule, running

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/safety-demo-dark.svg">
  <img src="assets/safety-demo-light.svg" alt="Three captured scenes on rotation: web-pilot's guardrails block a password field and an off-site jump, rag-chat abstains honestly below its measured retrieval floor, and doc-eval's gate blocks a release whose headline number improved." width="100%">
</picture>

<sub>Three scenes on rotation, all from captured runs: <a href="https://github.com/vinimabreu/web-pilot">web-pilot</a>'s guardrails blocking a credential field and an off-site jump (<code>examples/safety_demo.py</code>), <a href="https://github.com/vinimabreu/rag-chat">rag-chat</a> abstaining below its measured BM25 floor, and <a href="https://github.com/vinimabreu/doc-eval">doc-eval</a>'s gate failing a candidate that improved the headline number while losing a field. Each one is reproducible from its repo.</sub>

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:6E56CF,50:8B7BD8,100:A78BFA&height=2" width="100%" alt="" />

## Flagships

<p align="center">
  <a href="https://github.com/vinimabreu/rag-chat"><picture><source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api/pin/?username=vinimabreu&repo=rag-chat&bg_color=00000000&hide_border=true&title_color=A78BFA&text_color=9DA7B3&icon_color=A78BFA"><img src="https://github-readme-stats.vercel.app/api/pin/?username=vinimabreu&repo=rag-chat&bg_color=00000000&hide_border=true&title_color=6E56CF&text_color=57606A&icon_color=6E56CF" alt="rag-chat: chat with your docs, grounded answers with clickable citations" width="49%"></picture></a>
  <a href="https://github.com/vinimabreu/web-pilot"><picture><source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api/pin/?username=vinimabreu&repo=web-pilot&bg_color=00000000&hide_border=true&title_color=A78BFA&text_color=9DA7B3&icon_color=A78BFA"><img src="https://github-readme-stats.vercel.app/api/pin/?username=vinimabreu&repo=web-pilot&bg_color=00000000&hide_border=true&title_color=6E56CF&text_color=57606A&icon_color=6E56CF" alt="web-pilot: a browser-use agent with guardrails enforced in code" width="49%"></picture></a>
  <a href="https://github.com/vinimabreu/voice-receptionist"><picture><source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api/pin/?username=vinimabreu&repo=voice-receptionist&bg_color=00000000&hide_border=true&title_color=A78BFA&text_color=9DA7B3&icon_color=A78BFA"><img src="https://github-readme-stats.vercel.app/api/pin/?username=vinimabreu&repo=voice-receptionist&bg_color=00000000&hide_border=true&title_color=6E56CF&text_color=57606A&icon_color=6E56CF" alt="voice-receptionist: an AI phone receptionist that books appointments against a live calendar" width="49%"></picture></a>
  <a href="https://github.com/vinimabreu/doc-eval"><picture><source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api/pin/?username=vinimabreu&repo=doc-eval&bg_color=00000000&hide_border=true&title_color=A78BFA&text_color=9DA7B3&icon_color=A78BFA"><img src="https://github-readme-stats.vercel.app/api/pin/?username=vinimabreu&repo=doc-eval&bg_color=00000000&hide_border=true&title_color=6E56CF&text_color=57606A&icon_color=6E56CF" alt="doc-eval: field-level evaluation and a CI release gate for LLM extraction" width="49%"></picture></a>
</p>

<sub><a href="https://github.com/vinimabreu/rag-chat">rag-chat</a> &middot; <a href="https://github.com/vinimabreu/web-pilot">web-pilot</a> &middot; <a href="https://github.com/vinimabreu/voice-receptionist">voice-receptionist</a> &middot; <a href="https://github.com/vinimabreu/doc-eval">doc-eval</a></sub>

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:6E56CF,50:8B7BD8,100:A78BFA&height=2" width="100%" alt="" />

## Retrieval and RAG

*Citations you can click, an honest "I don't know", and retrieval quality that is measured, not assumed.*

**[rag-chat](https://github.com/vinimabreu/rag-chat)**<br>
Chat-with-your-docs widget: grounded answers with clickable citations and a working chat UI. Key-free demo mode.

**[rag-quality](https://github.com/vinimabreu/rag-quality)**<br>
A RAG pipeline with its own eval harness (hit@k, MRR, recall@k): BM25, dense, and RRF hybrid retrieval, scored against a labeled corpus.

**[mini-rag](https://github.com/vinimabreu/mini-rag)**<br>
A small, working RAG API on FastAPI, Chroma, and Claude. The clean baseline.

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:6E56CF,50:8B7BD8,100:A78BFA&height=2" width="100%" alt="" />

## Agents and tools

*Agents that can only do what their tool layer allows.*

**[web-pilot](https://github.com/vinimabreu/web-pilot)**<br>
Browser-use agent built on the house rule: the model proposes one action, code disposes. Closed action vocabulary, guardrails (domain allowlist, no credential or payment fields, step budget), full audit trace.

**[multi-agent-analyst](https://github.com/vinimabreu/multi-agent-analyst)**<br>
Planner, self-correcting SQL agent, BM25 retriever, and a verifier crew. Cites evidence or honestly refuses.

**[sql-agent](https://github.com/vinimabreu/sql-agent)**<br>
Plain English to SQL, with a self-correction loop, on a read-only connection.

**[mcp-listings](https://github.com/vinimabreu/mcp-listings)**<br>
MCP server exposing a property-listings dataset to Claude as typed tools.

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:6E56CF,50:8B7BD8,100:A78BFA&height=2" width="100%" alt="" />

## Voice and automation

*Conversation up front, a tested service underneath, and a human whenever confidence drops.*

**[voice-receptionist](https://github.com/vinimabreu/voice-receptionist)**<br>
AI phone receptionist over Twilio: books against a live calendar, abstains on policy questions, logs every call.

**[n8n-lead-triage](https://github.com/vinimabreu/n8n-lead-triage)**<br>
n8n routes, a tested HTTP service decides. Low confidence or any model failure routes to a human, never to silence.

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:6E56CF,50:8B7BD8,100:A78BFA&height=2" width="100%" alt="" />

## Evaluation and quality

*A regression gets blocked before it ships, not discovered after.*

**[doc-eval](https://github.com/vinimabreu/doc-eval)**<br>
Field-level evaluation and a CI release gate for LLM document extraction.

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:6E56CF,50:8B7BD8,100:A78BFA&height=2" width="100%" alt="" />

## Data engineering and extraction

*The layer underneath everything above: scrape, parse, validate, schedule.*

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/indicators-dark.svg">
  <img src="assets/indicators-light.svg" alt="Live Central Bank of Brazil indicators rendered by this repo's scheduled pipeline" width="100%">
</picture>

<sub>Not a screenshot: live numbers from the Central Bank of Brazil, refreshed on weekdays by <a href="https://github.com/vinimabreu/vinimabreu/blob/main/.github/workflows/update-indicators.yml">a scheduled pipeline in this repo</a>, committed only when the data changes. The commit history is the proof.</sub>

**[record-refinery](https://github.com/vinimabreu/record-refinery)**<br>
Raw business records in, a clean deduplicated dataset plus a QA brief out. Email, phone, and url validated in code, with an optional model-proposed canonical name for fuzzy dedup.

**[pdf-extract](https://github.com/vinimabreu/pdf-extract)**<br>
PDFs into validated structured JSON, with pluggable OCR.

**[docs-to-markdown](https://github.com/vinimabreu/docs-to-markdown)**<br>
Any documentation or marketing site into a clean Markdown corpus, ready for RAG.

**[ai-watcher](https://github.com/vinimabreu/ai-watcher)**<br>
Watches RSS feeds and turns new articles into structured AI summaries with Claude.

**[bcb-data-pipeline](https://github.com/vinimabreu/bcb-data-pipeline)**<br>
Daily ETL of Brazilian macro indicators from the central bank API, on pandas and GitHub Actions.

**[web-scraper](https://github.com/vinimabreu/web-scraper)**<br>
A Playwright scraper, SQLite storage, and a Streamlit dashboard, end to end.

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:6E56CF,50:8B7BD8,100:A78BFA&height=2" width="100%" alt="" />

## Stack

**Core** &nbsp;Python &middot; FastAPI &middot; Pydantic &middot; pytest<br>
**Retrieval** &nbsp;Chroma &middot; BM25 + dense embeddings &middot; SQLite<br>
**Models** &nbsp;Anthropic Claude API &middot; MCP (Model Context Protocol)<br>
**Extraction** &nbsp;Playwright &middot; pandas &middot; Tesseract OCR &middot; AWS Textract (optional adapter)<br>
**Automation** &nbsp;n8n &middot; Twilio &middot; Streamlit<br>
**Ops** &nbsp;Docker &middot; GitHub Actions

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:6E56CF,50:8B7BD8,100:A78BFA&height=2" width="100%" alt="" />

## How I work

| Grounded | Tested | Honest |
| --- | --- | --- |
| Answers cite their sources and refuse when the evidence is not there. | Deterministic suites that run with no API key and no network; CI gates catch regressions. | Trade-offs go in the README: rag-quality ships the eval showing hybrid retrieval was not a free win on its corpus. |

> "completed the work ahead of schedule and with accuracy. I would hire him again."
>
> <sub>recent client review</sub>

<p align="center">
  <b>Open to AI engineering, RAG, agents, and data work.</b><br>
  Based in Brazil, working with clients worldwide.
</p>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:6E56CF,50:8B7BD8,100:A78BFA&height=110&section=footer" width="100%" alt="" />
