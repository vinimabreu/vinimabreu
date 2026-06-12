# Vinicius Pereira

**AI systems that are grounded, tested, and honest, and the data pipelines behind them.**

I build retrieval, agents, MCP servers, voice, and automation with one rule running through all of it: the model proposes, the code disposes. The model holds the conversation; tested code makes every decision that matters. Every project below runs from real captured output, ships deterministic tests that need no API key, and comes with an architecture diagram and a README that is honest about the trade-offs.

### Retrieval and RAG
- **[rag-chat](https://github.com/vinimabreu/rag-chat):** a chat-with-your-docs widget with grounded answers, clickable citations, and an honest "I don't know", in a real chat UI.
- **[rag-quality](https://github.com/vinimabreu/rag-quality):** a RAG pipeline that measures its own retrieval quality instead of assuming it (BM25, dense, hybrid, and an eval harness).
- **[mini-rag](https://github.com/vinimabreu/mini-rag):** a small, working RAG API on FastAPI, Chroma and Claude. The clean baseline.

### Agents and tools
- **[web-pilot](https://github.com/vinimabreu/web-pilot):** a browser-use agent that proposes one action per step and lets code validate it against guardrails (domain allowlist, no credential fields, step budget) before the browser acts.
- **[multi-agent-analyst](https://github.com/vinimabreu/multi-agent-analyst):** a planner, worker, and verifier crew that answers questions no single source can, with citations or an honest refusal.
- **[sql-agent](https://github.com/vinimabreu/sql-agent):** plain English to SQL, with a real self-correction loop and defence-in-depth read-only safety.
- **[mcp-listings](https://github.com/vinimabreu/mcp-listings):** a Model Context Protocol server exposing live data to Claude as typed tools.

### Voice and automation
- **[voice-receptionist](https://github.com/vinimabreu/voice-receptionist):** an AI receptionist that books real appointments over Twilio, with every rule re-checked in code and every call logged.
- **[n8n-lead-triage](https://github.com/vinimabreu/n8n-lead-triage):** AI lead triage where n8n routes and a tested service decides; low confidence or any model failure routes to a human, never to silence.

### Evaluation and quality
- **[doc-eval](https://github.com/vinimabreu/doc-eval):** field-level evaluation and a CI release gate for LLM document extraction, built to block a regression before it ships.

### Data engineering and extraction
- **[pdf-extract](https://github.com/vinimabreu/pdf-extract):** PDFs into validated structured JSON, with pluggable OCR.
- **[docs-to-markdown](https://github.com/vinimabreu/docs-to-markdown):** any documentation or marketing site into a clean Markdown corpus, ready for RAG.
- **[ai-watcher](https://github.com/vinimabreu/ai-watcher):** watches feeds and turns new articles into structured AI summaries.
- **[bcb-data-pipeline](https://github.com/vinimabreu/bcb-data-pipeline):** daily ETL of Brazilian macro indicators from the central bank API.
- **[web-scraper](https://github.com/vinimabreu/web-scraper):** a Playwright scraper, SQLite storage, and a Streamlit dashboard, end to end.

### How I work
- **Grounded.** Answers cite their sources and refuse when the evidence is not there, because a confident wrong answer is worse than "I don't know".
- **Tested.** Deterministic suites that run with no API key and no network, so behaviour is proven, not hoped for.
- **Honest.** I tell you when something is not a free win. rag-quality ships the result showing the fancier retriever lost on the test corpus, because measuring beats assuming.

> "completed the work ahead of schedule and with accuracy. I would hire him again." (recent client review)

Open to AI engineering, RAG, agents, and data work. Based in Brazil, working with clients worldwide.
