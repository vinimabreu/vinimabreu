# Vinicius Pereira

**AI systems that are grounded, tested, and honest, and the data pipelines behind them.**

> **The model proposes, the code disposes.**<br>
> The model holds the conversation. Tested code makes every decision that matters.

I build retrieval, agents, MCP servers, voice, and automation with that one rule at the center. The flagships ship deterministic test suites that need no API key, show captured output from actual runs, and come with an architecture diagram; every README is honest about the trade-offs.

<sub><a href="#flagships">Flagships</a> &middot; <a href="#retrieval-and-rag">Retrieval and RAG</a> &middot; <a href="#agents-and-tools">Agents and tools</a> &middot; <a href="#voice-and-automation">Voice and automation</a> &middot; <a href="#evaluation-and-quality">Evaluation and quality</a> &middot; <a href="#data-engineering-and-extraction">Data engineering and extraction</a> &middot; <a href="#stack">Stack</a> &middot; <a href="#how-i-work">How I work</a></sub>

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:6E56CF,50:8B7BD8,100:A78BFA&height=4" width="100%" alt="" />

## Flagships

<p align="center">
  <a href="https://github.com/vinimabreu/rag-chat"><picture><source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api/pin/?username=vinimabreu&repo=rag-chat&bg_color=00000000&hide_border=true&title_color=A78BFA&text_color=9DA7B3&icon_color=A78BFA"><img src="https://github-readme-stats.vercel.app/api/pin/?username=vinimabreu&repo=rag-chat&bg_color=00000000&hide_border=true&title_color=6E56CF&text_color=57606A&icon_color=6E56CF" alt="rag-chat: chat with your docs, grounded answers with clickable citations" width="49%"></picture></a>
  <a href="https://github.com/vinimabreu/web-pilot"><picture><source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api/pin/?username=vinimabreu&repo=web-pilot&bg_color=00000000&hide_border=true&title_color=A78BFA&text_color=9DA7B3&icon_color=A78BFA"><img src="https://github-readme-stats.vercel.app/api/pin/?username=vinimabreu&repo=web-pilot&bg_color=00000000&hide_border=true&title_color=6E56CF&text_color=57606A&icon_color=6E56CF" alt="web-pilot: a browser-use agent with guardrails enforced in code" width="49%"></picture></a>
  <a href="https://github.com/vinimabreu/voice-receptionist"><picture><source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api/pin/?username=vinimabreu&repo=voice-receptionist&bg_color=00000000&hide_border=true&title_color=A78BFA&text_color=9DA7B3&icon_color=A78BFA"><img src="https://github-readme-stats.vercel.app/api/pin/?username=vinimabreu&repo=voice-receptionist&bg_color=00000000&hide_border=true&title_color=6E56CF&text_color=57606A&icon_color=6E56CF" alt="voice-receptionist: an AI phone receptionist that books appointments against a live calendar" width="49%"></picture></a>
  <a href="https://github.com/vinimabreu/doc-eval"><picture><source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api/pin/?username=vinimabreu&repo=doc-eval&bg_color=00000000&hide_border=true&title_color=A78BFA&text_color=9DA7B3&icon_color=A78BFA"><img src="https://github-readme-stats.vercel.app/api/pin/?username=vinimabreu&repo=doc-eval&bg_color=00000000&hide_border=true&title_color=6E56CF&text_color=57606A&icon_color=6E56CF" alt="doc-eval: field-level evaluation and a CI release gate for LLM extraction" width="49%"></picture></a>
</p>

<sub><a href="https://github.com/vinimabreu/rag-chat">rag-chat</a> &middot; <a href="https://github.com/vinimabreu/web-pilot">web-pilot</a> &middot; <a href="https://github.com/vinimabreu/voice-receptionist">voice-receptionist</a> &middot; <a href="https://github.com/vinimabreu/doc-eval">doc-eval</a></sub>

## Retrieval and RAG

*Citations you can click, an honest "I don't know", and retrieval quality that is measured, not assumed.*

**[rag-chat](https://github.com/vinimabreu/rag-chat)**<br>
Chat-with-your-docs widget: grounded answers with clickable citations and a working chat UI. Key-free demo mode.

**[rag-quality](https://github.com/vinimabreu/rag-quality)**<br>
A RAG pipeline with its own eval harness (hit@k, MRR, recall@k): BM25, dense, and RRF hybrid retrieval, scored against a labeled corpus.

**[mini-rag](https://github.com/vinimabreu/mini-rag)**<br>
A small, working RAG API on FastAPI, Chroma, and Claude. The clean baseline.

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

## Voice and automation

*Conversation up front, a tested service underneath, and a human whenever confidence drops.*

**[voice-receptionist](https://github.com/vinimabreu/voice-receptionist)**<br>
AI phone receptionist over Twilio: books against a live calendar, abstains on policy questions, logs every call.

**[n8n-lead-triage](https://github.com/vinimabreu/n8n-lead-triage)**<br>
n8n routes, a tested HTTP service decides. Low confidence or any model failure routes to a human, never to silence.

## Evaluation and quality

*A regression gets blocked before it ships, not discovered after.*

**[doc-eval](https://github.com/vinimabreu/doc-eval)**<br>
Field-level evaluation and a CI release gate for LLM document extraction.

## Data engineering and extraction

*The layer underneath everything above: scrape, parse, validate, schedule.*

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

## Stack

**Core** &nbsp;Python &middot; FastAPI &middot; Pydantic &middot; pytest<br>
**Retrieval** &nbsp;Chroma &middot; BM25 + dense embeddings &middot; SQLite<br>
**Models** &nbsp;Anthropic Claude API &middot; MCP (Model Context Protocol)<br>
**Extraction** &nbsp;Playwright &middot; pandas &middot; Tesseract OCR &middot; AWS Textract (optional adapter)<br>
**Automation** &nbsp;n8n &middot; Twilio &middot; Streamlit<br>
**Ops** &nbsp;Docker &middot; GitHub Actions

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

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:6E56CF,50:8B7BD8,100:A78BFA&height=4" width="100%" alt="" />
