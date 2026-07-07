<img src="https://capsule-render.vercel.app/api?type=waving&color=0:6E56CF,50:8B7BD8,100:A78BFA&height=210&section=header&text=Vinicius%20Pereira&fontSize=54&fontColor=FFFFFF&fontAlignY=36&desc=AI%20systems%20that%20are%20grounded%2C%20tested%2C%20and%20honest&descSize=17&descAlignY=58&animation=fadeIn" width="100%" alt="Vinicius Pereira. AI systems that are grounded, tested, and honest." />

> **The model proposes, the code disposes.**<br>
> The model holds the conversation. Tested code makes every decision that matters.

I build retrieval, agents, MCP servers, voice, and automation with that one rule at the center. The flagships ship deterministic test suites that need no API key, show captured output from actual runs, and come with an architecture diagram; every README is honest about the trade-offs. Twenty-nine public projects, more than 500 deterministic tests, one rule.

> My client work is under NDA and stays private. These public projects are built to the same standard, and show how I work: grounded, tested, and honest.

<p align="center">
<img src="https://img.shields.io/badge/Python-6E56CF?style=flat-square&logo=python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/FastAPI-6E56CF?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI">
<img src="https://img.shields.io/badge/Pydantic-6E56CF?style=flat-square&logo=pydantic&logoColor=white" alt="Pydantic">
<img src="https://img.shields.io/badge/pytest-6E56CF?style=flat-square&logo=pytest&logoColor=white" alt="pytest">
<img src="https://img.shields.io/badge/Playwright-6E56CF?style=flat-square&logo=playwright&logoColor=white" alt="Playwright">
<img src="https://img.shields.io/badge/pandas-6E56CF?style=flat-square&logo=pandas&logoColor=white" alt="pandas">
<img src="https://img.shields.io/badge/Tesseract%20OCR-6E56CF?style=flat-square" alt="Tesseract OCR">
<img src="https://img.shields.io/badge/Claude-6E56CF?style=flat-square&logo=anthropic&logoColor=white" alt="Claude">
<img src="https://img.shields.io/badge/Gemini-6E56CF?style=flat-square&logo=googlegemini&logoColor=white" alt="Google Gemini">
<img src="https://img.shields.io/badge/Google%20ADK-6E56CF?style=flat-square&logo=google&logoColor=white" alt="Google ADK (Agent Development Kit)">
<img src="https://img.shields.io/badge/A2A-6E56CF?style=flat-square" alt="A2A (Agent2Agent protocol)">
<img src="https://img.shields.io/badge/MCP-6E56CF?style=flat-square" alt="MCP (Model Context Protocol)">
<img src="https://img.shields.io/badge/Chroma-6E56CF?style=flat-square&logo=chromadb&logoColor=white" alt="Chroma">
<img src="https://img.shields.io/badge/SQLite-6E56CF?style=flat-square&logo=sqlite&logoColor=white" alt="SQLite">
<img src="https://img.shields.io/badge/Docker-6E56CF?style=flat-square&logo=docker&logoColor=white" alt="Docker">
<img src="https://img.shields.io/badge/n8n-6E56CF?style=flat-square&logo=n8n&logoColor=white" alt="n8n">
<img src="https://img.shields.io/badge/Twilio-6E56CF?style=flat-square&logo=twilio&logoColor=white" alt="Twilio">
<img src="https://img.shields.io/badge/Retell-6E56CF?style=flat-square" alt="Retell">
<img src="https://img.shields.io/badge/Streamlit-6E56CF?style=flat-square&logo=streamlit&logoColor=white" alt="Streamlit">
<img src="https://img.shields.io/badge/GitHub%20Actions-6E56CF?style=flat-square&logo=githubactions&logoColor=white" alt="GitHub Actions">
<img src="https://img.shields.io/badge/TypeScript-6E56CF?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript">
<img src="https://img.shields.io/badge/JavaScript-6E56CF?style=flat-square&logo=javascript&logoColor=white" alt="JavaScript">
<img src="https://img.shields.io/badge/React-6E56CF?style=flat-square&logo=react&logoColor=white" alt="React">
<img src="https://img.shields.io/badge/Next.js-6E56CF?style=flat-square&logo=nextdotjs&logoColor=white" alt="Next.js">
<img src="https://img.shields.io/badge/Vue.js-6E56CF?style=flat-square&logo=vuedotjs&logoColor=white" alt="Vue.js">
<img src="https://img.shields.io/badge/Node.js-6E56CF?style=flat-square&logo=nodedotjs&logoColor=white" alt="Node.js">
<img src="https://img.shields.io/badge/Vercel-6E56CF?style=flat-square&logo=vercel&logoColor=white" alt="Vercel">
<img src="https://img.shields.io/badge/Supabase-6E56CF?style=flat-square&logo=supabase&logoColor=white" alt="Supabase">
</p>

<sub><a href="#the-house-rule-running">The rule, running</a> &middot; <a href="#the-free-handbook">Free handbook</a> &middot; <a href="#flagships">Flagships</a> &middot; <a href="#retrieval-and-rag">Retrieval and RAG</a> &middot; <a href="#agents-and-tools">Agents and tools</a> &middot; <a href="#voice-and-automation">Voice and automation</a> &middot; <a href="#evaluation-and-quality">Evaluation and quality</a> &middot; <a href="#data-engineering-and-extraction">Data engineering and extraction</a> &middot; <a href="#stack">Stack</a> &middot; <a href="#how-i-work">How I work</a></sub>

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:6E56CF,50:8B7BD8,100:A78BFA&height=4" width="100%" alt="" />

## The house rule, running

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/safety-demo-dark.svg">
  <img src="assets/safety-demo-light.svg" alt="Three captured scenes on rotation: web-pilot's guardrails block a password field and an off-site jump, rag-chat abstains honestly below its measured retrieval floor, and doc-eval's gate blocks a release whose headline number improved." width="100%">
</picture>

<sub>Three scenes on rotation, all from captured runs: <a href="https://github.com/vinimabreu/web-pilot">web-pilot</a>'s guardrails blocking a credential field and an off-site jump (<code>examples/safety_demo.py</code>), <a href="https://github.com/vinimabreu/rag-chat">rag-chat</a> abstaining below its measured BM25 floor, and <a href="https://github.com/vinimabreu/doc-eval">doc-eval</a>'s gate failing a candidate that improved the headline number while losing a field. Each one is reproducible from its repo.</sub>

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:6E56CF,50:8B7BD8,100:A78BFA&height=2" width="100%" alt="" />

## The free handbook

<table><tr><td width="170" valign="top">
<a href="https://github.com/vinimabreu/ai-in-practice"><img src="https://raw.githubusercontent.com/vinimabreu/ai-in-practice/main/assets/cover.png" width="160" alt="Artificial Intelligence in Practice, book cover"></a>
</td><td valign="top">

**[Artificial Intelligence in Practice](https://github.com/vinimabreu/ai-in-practice)**: a free 84-page handbook that walks from "what is a token" to working agents with tools. Local models, RAG, agents, MCP, fine-tuning, real API costs, security, prompting as a method, and how to test AI systems so they do not embarrass you in front of a customer. Written for people starting out in AI, with every example tested by hand. CC BY-NC-SA: share it, translate it, teach with it.

<sub><a href="https://github.com/vinimabreu/ai-in-practice/blob/main/Artificial_Intelligence_in_Practice.pdf">Read the PDF</a> &middot; <a href="https://github.com/vinimabreu/ai-in-practice">Star the repo</a> &middot; <a href="https://dev.to/vinimabreu">Chapters serialized on dev.to</a></sub>

</td></tr></table>

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:6E56CF,50:8B7BD8,100:A78BFA&height=2" width="100%" alt="" />

## Flagships

<p align="center">
  <a href="https://github.com/vinimabreu/bedrock"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/flagship-bedrock-dark.svg"><img src="assets/flagship-bedrock-light.svg" alt="bedrock: a NL-to-SQL data agent that proves it answers the same right thing every run" width="49%"></picture></a>
  <a href="https://github.com/vinimabreu/rag-chat"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/flagship-rag-chat-dark.svg"><img src="assets/flagship-rag-chat-light.svg" alt="rag-chat: chat with your docs, grounded answers with clickable citations" width="49%"></picture></a>
  <a href="https://github.com/vinimabreu/web-pilot"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/flagship-web-pilot-dark.svg"><img src="assets/flagship-web-pilot-light.svg" alt="web-pilot: a browser-use agent with guardrails enforced in code" width="49%"></picture></a>
  <a href="https://github.com/vinimabreu/voice-receptionist"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/flagship-voice-receptionist-dark.svg"><img src="assets/flagship-voice-receptionist-light.svg" alt="voice-receptionist: an AI phone receptionist that books appointments against a live calendar" width="49%"></picture></a>
  <a href="https://github.com/vinimabreu/scrape-sentinel"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/flagship-scrape-sentinel-dark.svg"><img src="assets/flagship-scrape-sentinel-light.svg" alt="scrape-sentinel: turn any scraper output into new, changed, and removed since the last run" width="49%"></picture></a>
  <a href="https://github.com/vinimabreu/lead-qualifier"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/flagship-lead-qualifier-dark.svg"><img src="assets/flagship-lead-qualifier-light.svg" alt="lead-qualifier: qualify scraped leads with rules or an LLM and measure the qualifier with an eval harness" width="49%"></picture></a>
</p>

<sub><a href="https://github.com/vinimabreu/bedrock">bedrock</a> &middot; <a href="https://github.com/vinimabreu/rag-chat">rag-chat</a> &middot; <a href="https://github.com/vinimabreu/web-pilot">web-pilot</a> &middot; <a href="https://github.com/vinimabreu/voice-receptionist">voice-receptionist</a> &middot; <a href="https://github.com/vinimabreu/scrape-sentinel">scrape-sentinel</a> &middot; <a href="https://github.com/vinimabreu/lead-qualifier">lead-qualifier</a></sub>

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:6E56CF,50:8B7BD8,100:A78BFA&height=2" width="100%" alt="" />

## Retrieval and RAG

*Citations you can click, an honest "I don't know", and retrieval quality that is measured, not assumed.*

**[source-of-truth](https://github.com/vinimabreu/source-of-truth)**<br>
Centralizes scattered sources (markdown, FAQ, HTML, plaintext) into one queryable base that flags where two sources disagree, marks stale sources, and abstains honestly. Deterministic, no API key.

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

**[lead-quorum](https://github.com/vinimabreu/lead-quorum)**<br>
Distributed multi-agent lead qualifier on Google ADK and the A2A protocol: two readers on different Gemini models extract every lead independently as separate microservices, deterministic code scores it with a reason that provably sums to the number, and when the readings disagree on which rules fire it abstains instead of guessing.

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

**[retell-sms-handler](https://github.com/vinimabreu/retell-sms-handler)**<br>
Makes a Retell voice agent's In-Call SMS fire deterministically through a Conversation Flow function node: consent gated, the destination resolved in code, every send logged. FastAPI and Twilio.

**[n8n-lead-triage](https://github.com/vinimabreu/n8n-lead-triage)**<br>
n8n routes, a tested HTTP service decides. Low confidence or any model failure routes to a human, never to silence.

**[grounded-copy](https://github.com/vinimabreu/grounded-copy)**<br>
Generates on-brand product copy from your catalog, then checks every claim back against it: an invented price, spec, discount or material is flagged for review, nothing fabricated ships. Deterministic, key-free core.

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:6E56CF,50:8B7BD8,100:A78BFA&height=2" width="100%" alt="" />

## Evaluation and quality

*A regression gets blocked before it ships, not discovered after.*

**[bedrock](https://github.com/vinimabreu/bedrock)**<br>
A natural-language-to-SQL data agent with a stability harness: it runs each question K times against a defended answer key, flags the ones that flap, and a CI gate blocks a candidate when reliability regresses. Deterministic, key-free demo.

**[doc-eval](https://github.com/vinimabreu/doc-eval)**<br>
Field-level evaluation and a CI release gate for LLM document extraction.

**[lead-qualifier](https://github.com/vinimabreu/lead-qualifier)**<br>
Qualifies scraped leads with rules or an injected LLM (a 0-100 score, a reason, keep or drop), then measures the qualifier itself: precision, recall, and f1 against a labeled set. Zero runtime dependencies.

**[token-ledger](https://github.com/vinimabreu/token-ledger)**<br>
The LLM bill is total input and output tokens across every call a query makes, not chunk math. Records what the provider's API reports, per call, and answers with one GROUP BY. Cache buckets kept disjoint so cost never double-charges, unknown models flagged unpriced not zeroed. Zero dependencies, dashboard included.

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

**[scrape-sentinel](https://github.com/vinimabreu/scrape-sentinel)**<br>
The change-aware layer for any scraper: turns a list of records into new, changed, and removed since the last run, then alerts and stores a snapshot. Zero runtime dependencies.

**[repo-packager](https://github.com/vinimabreu/repo-packager)**<br>
Downloads GitHub repos and delivers clean, deterministic ZIPs: strips build noise and credential files, builds a byte-for-byte reproducible archive, and writes a manifest with the sha256 and the rule that removed each file. Standard library only.

**[cloudrun-pipeline](https://github.com/vinimabreu/cloudrun-pipeline)**<br>
Takes a pipeline from a local script to a deployed service that runs on a schedule, with health checks, run history, and retries. Built for Google Cloud Run.

**[crosswatch](https://github.com/vinimabreu/crosswatch)**<br>
Cross-source corroboration and scheduled scoring for data you cannot trust from one provider: two sources confirm each other or the row is excluded, every score ships a plain-language reason that provably sums to the number, and a config-driven scheduler runs it all on cadence with a kill switch. Zero runtime dependencies.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/sentinel-demo-dark.svg">
  <img src="assets/sentinel-demo-light.svg" alt="scrape-sentinel diffing two runs of a product catalog: one new product, one removed, and one with a price drop and a stock change" width="100%">
</picture>

<sub>Captured output: <a href="https://github.com/vinimabreu/scrape-sentinel">scrape-sentinel</a> diffing two runs of a product catalog. It reports what is new, gone, and changed down to the field, then alerts and stores a snapshot. Reproducible from the repo's offline demo.</sub>

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:6E56CF,50:8B7BD8,100:A78BFA&height=2" width="100%" alt="" />

## Stack

**Core** &nbsp;Python &middot; FastAPI &middot; Flask &middot; Pydantic &middot; pytest<br>
**Retrieval** &nbsp;Chroma &middot; BM25 + dense embeddings &middot; SQLite<br>
**Models** &nbsp;Anthropic Claude API &middot; Google Gemini &middot; MCP (Model Context Protocol) &middot; Google ADK + A2A<br>
**Extraction** &nbsp;Playwright &middot; pandas &middot; Tesseract OCR &middot; AWS Textract (optional adapter)<br>
**Automation** &nbsp;n8n &middot; Twilio &middot; Retell &middot; Streamlit<br>
**Full-stack web** &nbsp;TypeScript &middot; JavaScript &middot; React &middot; Next.js &middot; Vue &middot; Node.js &middot; Vercel &middot; Supabase<br>
**Ops** &nbsp;Docker &middot; GitHub Actions &middot; Google Cloud Run

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:6E56CF,50:8B7BD8,100:A78BFA&height=2" width="100%" alt="" />

## How I work

| Grounded | Tested | Honest |
| --- | --- | --- |
| Answers cite their sources and refuse when the evidence is not there. | Deterministic suites that run with no API key and no network; CI gates catch regressions. | Trade-offs go in the README: rag-quality ships the eval showing hybrid retrieval was not a free win on its corpus. |

> "He built a reusable, profile-driven Python data cleansing framework with strong architecture, clear documentation, automated tests, and disciplined output controls. [...] The final delivery was professional, well-structured, tested, and ready for the next productisation phase. I would confidently work with Vinicius again."
>
> <sub>recent client review</sub>

> "completed the work ahead of schedule and with accuracy. I would hire him again."
>
> <sub>another client review</sub>

<p align="center">
  <b>Open to AI engineering, RAG, agents, and data work.</b><br>
  RAG and LLM systems, agents and automations, scraping and data pipelines, all built with tests and CI.<br>
  Based in Brazil, working with clients worldwide.
</p>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:6E56CF,50:8B7BD8,100:A78BFA&height=110&section=footer" width="100%" alt="" />
