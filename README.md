<img src="assets/header.svg" width="100%" alt="Vinicius Pereira. AI systems that are grounded, tested, and honest." />

<img src="assets/brief.svg" width="100%" alt="The house rule: The model proposes, the code disposes. The model holds the conversation. Tested code makes every decision that matters. I build retrieval, agents, MCP servers, voice, and automation with that one rule at the center. The flagships ship deterministic test suites that need no API key and show captured output from actual runs; every README is honest about the trade-offs. The console below counts the public repos and the tests their READMEs state, fresh every weekday; one rule runs through all of them. My client work is under NDA and stays private. These public projects are built to the same standard, and show how I work: grounded, tested, and honest.">

<img src="assets/console.svg" width="100%" alt="Mission console, refreshed every weekday from public data: every public repo on a radar by launch date, the tests their READMEs state, the last launch, the last write-up, and the CI state of the six flagships.">

<p align="center">
  <a href="https://vinimabreu.dev/proof"><img src="assets/proof-anthropic.svg" alt="Paid bounty: Anthropic, security report, paid. Receipt on vinimabreu.dev/proof" width="49%"></a>
  <a href="https://vinimabreu.dev/proof"><img src="assets/proof-mongodb.svg" alt="Paid bounty: MongoDB, security report, resolved and paid. Receipt on vinimabreu.dev/proof" width="49%"></a>
  <a href="https://github.com/containers/crun/pull/2166"><img src="assets/proof-crun.svg" alt="Merged upstream: containers/crun pull request 2166" width="49%"></a>
  <a href="https://arxiv.org/abs/2607.18347"><img src="assets/proof-arxiv.svg" alt="Credited reviewer: arXiv 2607.18347, agentic commerce reference architecture" width="49%"></a>
</p>

<p align="center">
<a href="https://vinimabreu.dev"><img src="assets/button-portfolio.svg" alt="Open the full portfolio on vinimabreu.dev" width="560"></a>
</p>

<p align="center">
  <a href="#the-house-rule-running"><img src="assets/nav-the-house-rule-running.svg" alt="The house rule, running" height="30"></a>
  <a href="#the-free-handbook"><img src="assets/nav-the-free-handbook.svg" alt="The free handbook" height="30"></a>
  <a href="#invited-review"><img src="assets/nav-invited-review.svg" alt="Invited review" height="30"></a>
  <a href="#merged-upstream"><img src="assets/nav-merged-upstream.svg" alt="Merged upstream" height="30"></a>
  <a href="#ci-security"><img src="assets/nav-ci-security.svg" alt="CI security" height="30"></a>
  <a href="#flagships"><img src="assets/nav-flagships.svg" alt="Flagships" height="30"></a>
  <a href="#retrieval-and-rag"><img src="assets/nav-retrieval-and-rag.svg" alt="Retrieval and RAG" height="30"></a>
  <a href="#agents-and-tools"><img src="assets/nav-agents-and-tools.svg" alt="Agents and tools" height="30"></a>
  <a href="#voice-and-automation"><img src="assets/nav-voice-and-automation.svg" alt="Voice and automation" height="30"></a>
  <a href="#evaluation-and-quality"><img src="assets/nav-evaluation-and-quality.svg" alt="Evaluation and quality" height="30"></a>
  <a href="#data-engineering-and-extraction"><img src="assets/nav-data-engineering-and-extraction.svg" alt="Data engineering and extraction" height="30"></a>
  <a href="#stack"><img src="assets/nav-stack.svg" alt="Stack" height="30"></a>
  <a href="#how-i-work"><img src="assets/nav-how-i-work.svg" alt="How I work" height="30"></a>
</p>

<img src="assets/divider.svg" width="100%" alt="" />

## The house rule, running

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/safety-demo-dark.svg">
  <img src="assets/safety-demo-light.svg" alt="Three captured scenes on rotation: betorskip refuses a $84.00 return that Gemma worked out on its own, sequence-gate stops a send after the invoice is paid, refuses a replay and holds a message at 00:12 local time, and web-pilot's guardrails block a password field and an off-site jump." width="100%">
</picture>

<sub>Three scenes on rotation, all from captured runs: <a href="https://github.com/vinimabreu/betorskip">betorskip</a> refusing a $84.00 return that Gemma worked out on its own, because the slip only prints To Win $64.00 (the recorded model answer in <code>examples/readings</code>); <a href="https://github.com/vinimabreu/sequence-gate">sequence-gate</a> stopping a send after the invoice was paid, refusing a replay and holding a message at 00:12 in the contact's time zone (<code>examples/demo.py</code>, column spacing trimmed); and <a href="https://github.com/vinimabreu/web-pilot">web-pilot</a>'s guardrails blocking a credential field and an off-site jump (<code>examples/safety_demo.py</code>). Each one is reproducible from its repo.</sub>

<img src="assets/divider.svg" width="100%" alt="" />

## The free handbook

<a href="https://github.com/vinimabreu/ai-in-practice"><img src="assets/handbook.svg" width="100%" alt="Artificial Intelligence in Practice: a free 84-page handbook that walks from what is a token to working agents with tools. Local models, RAG, agents, MCP, fine-tuning, real API costs, security, prompting as a method, and how to test AI systems so they do not embarrass you in front of a customer. Written for people starting out in AI, with every example tested by hand. CC BY-NC-SA: share it, translate it, teach with it."></a>

<p align="center">
  <a href="https://github.com/vinimabreu/ai-in-practice/blob/main/Artificial_Intelligence_in_Practice.pdf"><img src="assets/chip-read-the-pdf.svg" alt="Read the PDF" height="34"></a>
  <a href="https://github.com/vinimabreu/ai-in-practice"><img src="assets/chip-star-the-repo.svg" alt="Star the repo" height="34"></a>
  <a href="https://dev.to/vinimabreu"><img src="assets/chip-chapters-on-devto.svg" alt="Chapters serialized on dev.to" height="34"></a>
</p>

<img src="assets/divider.svg" width="100%" alt="" />

## Invited review

<a href="https://arxiv.org/abs/2607.18347"><img src="assets/review.svg" width="100%" alt="Invited review, credited by name: A Decision-Centered Reference Architecture for Trustworthy Agentic Commerce, by Dimitrios S. Sfyris, founder of AspectSoft, published on arXiv 2607.18347. Credited for refining the separation between commercial eligibility and actor authority, payment artifacts treated as evidence rather than automatic permission, and the controls that keep AI-generated claims grounded, scoped, and verifiable."></a>

<img src="assets/divider.svg" width="100%" alt="" />

## Merged upstream

<a href="https://github.com/containers/crun/pull/2166"><img src="assets/upstream.svg" width="100%" alt="Merged upstream: containers/crun pull request 2166, reviewed and merged by the project maintainer."></a>

<details>
<summary><b>The bug in full</b></summary>

crun is the OCI runtime that Podman and CRI-O run containers with. Its passwd parser tested for a digit with `**s - '0' < 10`, a signed comparison with no lower bound: `**s` promotes to `int`, so every byte below `'0'` yields a negative value that is also below 10. Out of the 256 possible byte values, 186 kept the loop running and `'\0'` was one of them, so a passwd line whose uid field is empty walks the parser past the end of the buffer. The correct form was imported from musl in June 2020 and lost its `U` suffix 43 minutes later, in a commit that dropped it to silence `-Werror=sign-compare` on the Alpine build, which is where the affected path compiles. Traced back to that commit and fixed with an explicit range test that stays warning free without a cast. Reviewed and merged by the project maintainer.

</details>

<img src="assets/divider.svg" width="100%" alt="" />

## CI security

<a href="https://github.com/vinimabreu/taint-trail"><img src="assets/security.svg" width="100%" alt="taint-trail: the scanner finds the template; this follows the value after someone moves it. 707 tests, one dependency, no network, no key."></a>

<details>
<summary><b>How it follows the value</b></summary>

The usual fix for `${{ github.event.comment.body }}` inside a `run:` block is to move the value into `env:`, which removes the finding from every scanner that looks for templates in scripts and removes nothing from the job. This follows the value after the move: through `env:`, `with:`, step outputs and into the called action, recursively, until it dies as a discrete argument with no shell in between, reaches a shell, can spoof `$GITHUB_OUTPUT` through a static heredoc delimiter, or becomes opaque, in which case it says exactly where it stopped and why instead of guessing. Every verdict is a chain with a file and line at each hop, because that is what convinces a maintainer. Modelled on a real finding in coordinated disclosure. 707 tests, one dependency, no network, no key.

</details>

<img src="assets/divider.svg" width="100%" alt="" />

## Flagships

<p align="center">
  <a href="https://github.com/vinimabreu/revenue-loop"><img src="assets/payload-revenue-loop.svg" alt="revenue-loop: a won CRM deal reaches Google and Meta exactly once, or waits in quarantine; live CI state and last push" width="49%"></a>
  <a href="https://github.com/vinimabreu/sequence-gate"><img src="assets/payload-sequence-gate.svg" alt="sequence-gate: decides whether the next follow-up may fire, stopping before the send and never sending twice; live CI state and last push" width="49%"></a>
  <a href="https://github.com/vinimabreu/tenant-fence"><img src="assets/payload-tenant-fence.svg" alt="tenant-fence: multi-tenant RAG where entitlements filter before top-k, so no ranking can leak across customers; live CI state and last push" width="49%"></a>
  <a href="https://github.com/vinimabreu/langgraph-production"><img src="assets/payload-langgraph-production.svg" alt="langgraph-production: a LangGraph support agent with a human gate and a resume that runs exactly once; live CI state and last push" width="49%"></a>
  <a href="https://github.com/vinimabreu/taint-trail"><img src="assets/payload-taint-trail.svg" alt="taint-trail: follows an untrusted GitHub Actions value after it moves, until it dies or reaches a shell; live CI state and last push" width="49%"></a>
  <a href="https://github.com/vinimabreu/betorskip"><img src="assets/payload-betorskip.svg" alt="betorskip: a local Gemma reads the bet slip, and code checks every number and the slip's own arithmetic; live CI state and last push" width="49%"></a>
</p>


https://github.com/user-attachments/assets/9c36119b-a972-40bf-8418-8c00f87f98ab



<p align="center"><em>▶ 60-second profile reel</em></p>

<img src="assets/divider.svg" width="100%" alt="" />

## Retrieval and RAG

<img src="assets/sector-rag.svg" width="100%" alt="Citations you can click, an honest &quot;I don't know&quot;, retrieval quality that is measured rather than assumed, and a fence between customers that a ranking cannot climb over.">

<a href="https://github.com/vinimabreu/tenant-fence"><img src="assets/row-tenant-fence.svg" width="100%" alt="tenant-fence: Multi-tenant RAG retrieval where cross-tenant leakage is impossible by construction"></a>
<a href="https://github.com/vinimabreu/on-behalf"><img src="assets/row-on-behalf.svg" width="100%" alt="on-behalf: Permission-aware RAG that asks the source, as the user, at query time"></a>
<a href="https://github.com/vinimabreu/source-of-truth"><img src="assets/row-source-of-truth.svg" width="100%" alt="source-of-truth: One queryable base from scattered sources that flags conflicts, marks stale ones and abstains honestly"></a>
<a href="https://github.com/vinimabreu/rag-chat"><img src="assets/row-rag-chat.svg" width="100%" alt="rag-chat: Chat with your docs: grounded answers with clickable citations and an honest &quot;I don't know&quot;"></a>
<a href="https://github.com/vinimabreu/rag-quality"><img src="assets/row-rag-quality.svg" width="100%" alt="rag-quality: A RAG pipeline that measures retrieval quality instead of assuming it"></a>
<a href="https://github.com/vinimabreu/mini-rag"><img src="assets/row-mini-rag.svg" width="100%" alt="mini-rag: A small, working Retrieval-Augmented Generation API (FastAPI + Chroma + Claude)"></a>

<details>
<summary><b>Full notes on these 6</b></summary>

**[tenant-fence](https://github.com/vinimabreu/tenant-fence)**<br>
One knowledge base, many customers, and an entitlement filter that runs before the candidate set is scored instead of after it. The wrong version ships beside the right one so the suite can demonstrate the leak rather than describe it: same corpus, same question, same account, three sections returned one way and none at all the other. 369 tests, 141 of them adversarial, and every number in the README read off the offline demo.

**[on-behalf](https://github.com/vinimabreu/on-behalf)**<br>
The other half of the fence: people inside the same organization, where the authority over who opens a document is Microsoft Graph or Google Drive, not the index. Every candidate is checked against the source at query time, as the signed-in user, through a modeled on-behalf-of token exchange, and enters the answer with its right named: a direct grant, a nested group, a sharing link, a site role. The index that copies ACLs at ingestion ships beside it, wrong by design, so the suite can demonstrate the leaks that a revoked grant, a group removal, and an expired sharing link each open. Fails closed, raises instead of silently filtering, 353 tests, no network, no key.

**[source-of-truth](https://github.com/vinimabreu/source-of-truth)**<br>
Centralizes scattered sources (markdown, FAQ, HTML, plaintext) into one queryable base that flags where two sources disagree, marks stale sources, and abstains honestly. Deterministic, no API key.

**[rag-chat](https://github.com/vinimabreu/rag-chat)**<br>
Chat-with-your-docs widget: grounded answers with clickable citations and a working chat UI. Key-free demo mode.

**[rag-quality](https://github.com/vinimabreu/rag-quality)**<br>
A RAG pipeline with its own eval harness (hit@k, MRR, recall@k): BM25, dense, and RRF hybrid retrieval, scored against a labeled corpus.

**[mini-rag](https://github.com/vinimabreu/mini-rag)**<br>
A small, working RAG API on FastAPI, Chroma, and Claude. The clean baseline.

</details>

<img src="assets/divider.svg" width="100%" alt="" />

## Agents and tools

<img src="assets/sector-agents.svg" width="100%" alt="Agents that can only do what their tool layer allows.">

<a href="https://github.com/vinimabreu/langgraph-production"><img src="assets/row-langgraph-production.svg" width="100%" alt="langgraph-production: A LangGraph support agent with the reliability layer around it"></a>
<a href="https://github.com/vinimabreu/whatran"><img src="assets/row-whatran.svg" width="100%" alt="whatran: What your coding agents ran in your terminal today, flagged by fixed rules and explained by a local Gemma"></a>
<a href="https://github.com/vinimabreu/dapraia"><img src="assets/row-dapraia.svg" width="100%" alt="dapraia: The hour to go outside tomorrow, in one line: your own words read by a local Gemma, the window picked by code"></a>
<a href="https://github.com/vinimabreu/betorskip"><img src="assets/row-betorskip.svg" width="100%" alt="betorskip: A local Gemma reads the bet slip; code checks every number and the slip's own arithmetic"></a>
<a href="https://github.com/vinimabreu/web-pilot"><img src="assets/row-web-pilot.svg" width="100%" alt="web-pilot: A browser-use agent where the model proposes one action and code disposes"></a>
<a href="https://github.com/vinimabreu/lead-quorum"><img src="assets/row-lead-quorum.svg" width="100%" alt="lead-quorum: Multi-agent lead qualifier on Google ADK + A2A that abstains instead of guessing"></a>
<a href="https://github.com/vinimabreu/multi-agent-analyst"><img src="assets/row-multi-agent-analyst.svg" width="100%" alt="multi-agent-analyst: A multi-agent crew that answers business questions no single source can"></a>
<a href="https://github.com/vinimabreu/sql-agent"><img src="assets/row-sql-agent.svg" width="100%" alt="sql-agent: Ask a database questions in plain English"></a>
<a href="https://github.com/vinimabreu/mcp-listings"><img src="assets/row-mcp-listings.svg" width="100%" alt="mcp-listings: An MCP (Model Context Protocol) server exposing a property-listings dataset to Claude as typed tools"></a>

<details>
<summary><b>Full notes on these 9</b></summary>

**[langgraph-production](https://github.com/vinimabreu/langgraph-production)**<br>
A LangGraph support agent with the reliability layer that decides whether it can ship. Routing is measured against labelled fixtures with a confusion matrix, and scored on the arguments rather than just the tool name, because choosing "issue refund" correctly means nothing if the amount is wrong. Irreversible tools stop for a human, approvals are single use, and the interrupt is measured in both directions, since stopping for nothing is how a gate stops meaning anything. The process can be killed at any of 208 points in a run and resumed from disk with the effect count unchanged, and where a window genuinely cannot be closed it holds the ticket for a human instead of guessing. A CI gate fails the build when any of those numbers moves. 373 tests, no network, no API key.

**[whatran](https://github.com/vinimabreu/whatran)**<br>
What the coding agents ran in your terminal today, read from the history that already records it: atuin's agent-tagged entries and Claude Code's own session files. Fixed rules decide what deserves a second look (`curl | sh`, `rm -rf` on something that is not a cache, a force push, a read of `.env`, `sudo` here or on a server over `ssh`), one simple command at a time and only from the part the shell actually runs, so a heredoc of test data or a commit message never counts. Gemma 4 on Ollama, on the same machine, writes the note, and the note is checked against the facts before anyone sees it: a command it quotes or a number it uses that the facts do not hold, and the note is withheld. Its first run on a real working day of mine raised 64 flags, 21 of them wrong; reading what runs brought the same day down to four entries. 318 tests, no dependencies, and the history never leaves the machine.

**[dapraia](https://github.com/vinimabreu/dapraia)**<br>
The hour to go outside tomorrow, in one line. You say how you like the beach in your own words ("pouco vento, maré baixa, pelo menos 2 horas"), and Gemma 4 on Ollama, on your own machine, turns them into rules that each have to quote the words they came from, with every number you wrote accounted for. Plain code then checks every daylight hour of an Open-Meteo forecast against those rules and picks the window; the model only writes the sentence of why, and that sentence is checked against the facts before you see it. The tide model was checked against the Brazilian Navy's official table: its low tides came 53 to 69 minutes early, and one measured shift brings all eight within 10 minutes. 344 tests, no dependencies.

**[betorskip](https://github.com/vinimabreu/betorskip)**<br>
Paste a bet slip, or point at a screenshot of one, and get BET, SKIP or CHECK by the bankroll rules you wrote down. Gemma 4 on Ollama, on your own machine, returns every number with the words it came from; plain code keeps only what the slip backs up, then checks the slip against itself: stake times odds is the return it prints, the legs multiply to the total, a "6-Fold" has six legs. That arithmetic put back a decimal point the OCR dropped (1747 for 17.47) and caught three misread legs on the same slip. On screenshots it had never seen, 17 of 24 verdicts were right, 6 came back for a look and one was wrong, and the README says which. It never says a bet will win. 134 tests, no dependencies. [Write-up](https://dev.to/vinimabreu/bet-or-skip-gemma-reads-the-bet-slip-on-my-laptop-and-the-slips-own-arithmetic-checks-gemma-eif).

**[web-pilot](https://github.com/vinimabreu/web-pilot)**<br>
Browser-use agent built on the house rule: the model proposes one action, code disposes. Closed action vocabulary, guardrails (domain allowlist, no credential or payment fields, step budget), full audit trace.

**[lead-quorum](https://github.com/vinimabreu/lead-quorum)**<br>
Distributed multi-agent lead qualifier on Google ADK and the A2A protocol: two readers on different Gemini models extract every lead independently as separate microservices, deterministic code scores it with a reason that provably sums to the number, and when the readings disagree on which rules fire it abstains instead of guessing. Deployed live on Cloud Run with an interactive demo, and recognized by DEV's ADK education track with the Cloud Run Badge.

**[multi-agent-analyst](https://github.com/vinimabreu/multi-agent-analyst)**<br>
Planner, self-correcting SQL agent, BM25 retriever, and a verifier crew. Cites evidence or honestly refuses.

**[sql-agent](https://github.com/vinimabreu/sql-agent)**<br>
Plain English to SQL, with a self-correction loop, on a read-only connection.

**[mcp-listings](https://github.com/vinimabreu/mcp-listings)**<br>
MCP server exposing a property-listings dataset to Claude as typed tools.

</details>

<img src="assets/divider.svg" width="100%" alt="" />

## Voice and automation

<img src="assets/sector-automation.svg" width="100%" alt="Conversation up front, a tested service underneath, and a human whenever confidence drops.">

<a href="https://github.com/vinimabreu/sequence-gate"><img src="assets/row-sequence-gate.svg" width="100%" alt="sequence-gate: Decide whether the next step of a follow-up sequence may fire"></a>
<a href="https://github.com/vinimabreu/ghl-bridge"><img src="assets/row-ghl-bridge.svg" width="100%" alt="ghl-bridge: Policy-gated bridge between a HighLevel workspace and AI automation"></a>
<a href="https://github.com/vinimabreu/revenue-loop"><img src="assets/row-revenue-loop.svg" width="100%" alt="revenue-loop: A won CRM deal reaches Google and Meta exactly once, or waits in quarantine"></a>
<a href="https://github.com/vinimabreu/conversion-preflight"><img src="assets/row-conversion-preflight.svg" width="100%" alt="conversion-preflight: Preflight agent for Google and Meta offline conversion uploads"></a>
<a href="https://github.com/vinimabreu/voice-receptionist"><img src="assets/row-voice-receptionist.svg" width="100%" alt="voice-receptionist: An AI phone receptionist for a multi-location business"></a>
<a href="https://github.com/vinimabreu/retell-sms-handler"><img src="assets/row-retell-sms-handler.svg" width="100%" alt="retell-sms-handler: Deterministic In-Call SMS for Retell voice agents"></a>
<a href="https://github.com/vinimabreu/n8n-lead-triage"><img src="assets/row-n8n-lead-triage.svg" width="100%" alt="n8n-lead-triage: AI lead triage in n8n: a tested service decides, and low confidence routes to a human"></a>
<a href="https://github.com/vinimabreu/make-failsafe"><img src="assets/row-make-failsafe.svg" width="100%" alt="make-failsafe: Error handling patterns for Make.com scenarios that refuse to die silently"></a>
<a href="https://github.com/vinimabreu/grounded-copy"><img src="assets/row-grounded-copy.svg" width="100%" alt="grounded-copy: Generate on-brand product copy from your catalog, and prove it didn't invent anything"></a>

<details>
<summary><b>Full notes on these 9</b></summary>

**[sequence-gate](https://github.com/vinimabreu/sequence-gate)**<br>
The service a follow-up sequence asks before every send. It answers whether the next step may fire, and the order of the checks is the design: stopping signals are read before anything else, so a contact who replied on Tuesday is not chased on Wednesday, and a store that cannot answer holds rather than sends. Idempotency keys on the case and the step rather than the provider's message id, so a replayed workflow cannot double-send; quiet hours are read on the contact's clock, including the two days a year that clock lies; frequency caps count across every sequence the contact is in; and an escalation ladder whose last rung is not a person is refused when the config loads. The three wrong implementations ship alongside and are run by the suite. 138 tests, importable n8n workflow and Make blueprint.

**[ghl-bridge](https://github.com/vinimabreu/ghl-bridge)**<br>
A policy-gated bridge between a CRM workspace and AI automation, built against the platform's documented API with a deterministic fake standing in for the account. Webhook idempotency keys on the event, so a redelivery with a fresh delivery id never doubles an effect. The gate auto-sends only inside policy (business hours by timezone, covered intent, no price commitments) and parks everything else as a draft with the reason named; a redundant guard raises instead of silently filtering if an unapproved send ever reaches the transport. 379 tests, no network, no key, no account.

**[revenue-loop](https://github.com/vinimabreu/revenue-loop)**<br>
The loop most advertising stacks leave open. A CRM knows which deals closed and for how much, the ad platforms know which clicks they served, and almost nobody owns the piece in between. A won deal reaches Google's Data Manager API and the Meta Conversions API exactly once, attributed to the click that earned it, or it is quarantined with the reason named. The same customer is hashed twice, because the two vendors normalise the same email differently, and one shared normaliser is silently wrong for every gmail address in the account: the upload succeeds, the match never happens, and the campaign just looks worse than it is. Six of Meta's own published vectors are reproduced in the suite, input and expected digest both. The deterministic key holds in two places, the store and the batch, so a CRM that fires its webhook twice in one run cannot double-count a deal and turn the next upsell into a refund that never happened. No attribution identifier is ever invented, and a template that never rendered is refused rather than uploaded. 734 tests, one runtime dependency, no network, no key, no account.

**[conversion-preflight](https://github.com/vinimabreu/conversion-preflight)**<br>
The check before that upload. An agent reads what Google and Meta document from a Sanity knowledge base built from their own pages, reads what the code declares about its own rules from structured documents in a Sanity dataset, and takes every normalized value and digest from the tested normaliser revenue-loop is built on, so a model never writes a hash. It flags what the platforms would accept and never match (a national phone with no country, a title left in a name, an invisible character) with the rule behind it, and it audits the code against the documentation, keeping what the platforms require apart from what the implementation declares. Building the knowledge base surfaced a bug in Google's own Python sample, which strips the dots from every address. Graded by code: 13 of 14 cases with the tools, 0 of 3 computed digests without them, and no digest invented in either run. 202 tests.

**[voice-receptionist](https://github.com/vinimabreu/voice-receptionist)**<br>
AI phone receptionist over Twilio: books against a live calendar, abstains on policy questions, logs every call.

**[retell-sms-handler](https://github.com/vinimabreu/retell-sms-handler)**<br>
Makes a Retell voice agent's In-Call SMS fire deterministically through a Conversation Flow function node: consent gated, the destination resolved in code, every send logged. FastAPI and Twilio.

**[n8n-lead-triage](https://github.com/vinimabreu/n8n-lead-triage)**<br>
n8n routes, a tested HTTP service decides. Low confidence or any model failure routes to a human, never to silence.

**[make-failsafe](https://github.com/vinimabreu/make-failsafe)**<br>
The same thesis on Make (ex Integromat): error routing for scenarios that refuse to die silently, backed by a tested decision service. Importable blueprints, 83 tests, and the order-export scenario verified live in a real workspace.

**[grounded-copy](https://github.com/vinimabreu/grounded-copy)**<br>
Generates on-brand product copy from your catalog, then checks every claim back against it: an invented price, spec, discount or material is flagged for review, nothing fabricated ships. Deterministic, key-free core.

</details>

<img src="assets/divider.svg" width="100%" alt="" />

## Evaluation and quality

<img src="assets/sector-evals.svg" width="100%" alt="A regression gets blocked before it ships, not discovered after.">

<a href="https://github.com/vinimabreu/confidence-gate"><img src="assets/row-confidence-gate.svg" width="100%" alt="confidence-gate: A trust gate for LLM output: auto-accept, human review, or abstain, on external signals"></a>
<a href="https://github.com/vinimabreu/bedrock"><img src="assets/row-bedrock.svg" width="100%" alt="bedrock: A natural-language-to-SQL data agent with a stability harness"></a>
<a href="https://github.com/vinimabreu/doc-eval"><img src="assets/row-doc-eval.svg" width="100%" alt="doc-eval: Field-level evaluation and release gate for LLM document extraction"></a>
<a href="https://github.com/vinimabreu/lead-qualifier"><img src="assets/row-lead-qualifier.svg" width="100%" alt="lead-qualifier: Qualify scraped leads with rules or an LLM, then measure the qualifier with an eval harness"></a>
<a href="https://github.com/vinimabreu/token-ledger"><img src="assets/row-token-ledger.svg" width="100%" alt="token-ledger: Per-query token ledger for LLM pipelines: record what the API reports, answer with one GROUP BY"></a>
<a href="https://github.com/vinimabreu/grounding-probe"><img src="assets/row-grounding-probe.svg" width="100%" alt="grounding-probe: Does the RAG answer use the retrieved context, or just agree with it? A counterfactual check"></a>
<a href="https://www.kaggle.com/benchmarks/vinimabreu/keep-the-number-you-wrote"><img src="assets/row-keep-the-number-you-wrote.svg" width="100%" alt="Keep the number you wrote: Kaggle benchmark: do models keep the number, the unit and the direction when a sentence becomes rules?"></a>

<details>
<summary><b>Full notes on these 7</b></summary>

**[confidence-gate](https://github.com/vinimabreu/confidence-gate)**<br>
The gate between an LLM's output and production. It validates the structure, then scores confidence from external signals instead of the model's own word (is the output grounded in the evidence, does it survive resampling, does it satisfy the schema), and routes each result to auto-accept, a human review queue with a full audit trail, or abstain. Calibrated on the cost of a false accept, not the acceptance rate, because a confident wrong answer is the expensive one. Zero runtime dependencies beyond Pydantic, the generator injected as a callable.

**[bedrock](https://github.com/vinimabreu/bedrock)**<br>
A natural-language-to-SQL data agent with a stability harness: it runs each question K times against a defended answer key, flags the ones that flap, and a CI gate blocks a candidate when reliability regresses. Deterministic, key-free demo.

**[doc-eval](https://github.com/vinimabreu/doc-eval)**<br>
Field-level evaluation and a CI release gate for LLM document extraction.

**[lead-qualifier](https://github.com/vinimabreu/lead-qualifier)**<br>
Qualifies scraped leads with rules or an injected LLM (a 0-100 score, a reason, keep or drop), then measures the qualifier itself: precision, recall, and f1 against a labeled set. Zero runtime dependencies.

**[token-ledger](https://github.com/vinimabreu/token-ledger)**<br>
The LLM bill is total input and output tokens across every call a query makes, not chunk math. Records what the provider's API reports, per call, and answers with one GROUP BY. Cache buckets kept disjoint so cost never double-charges, unknown models flagged unpriced not zeroed. Zero dependencies, dashboard included.

**[grounding-probe](https://github.com/vinimabreu/grounding-probe)**<br>
A RAG answer can be correct, cite the right chunk, and still come from the model's memory, with the citation decorative. This probe settles it counterfactually: drop, corrupt, swap, and paraphrase the evidence, re-run the same generator, and read whether the answer moves the way a grounded one must. Per-ablation receipts on every verdict, and the test suite runs the probe against three generators with known behavior, so it cannot pass by accident. Zero runtime dependencies, exit code gates CI.

**[Keep the number you wrote](https://www.kaggle.com/benchmarks/vinimabreu/keep-the-number-you-wrote)** (Kaggle benchmark)<br>
Do models keep the number, the unit and the direction when a plain sentence becomes rules? 40 sentences about going outside, in Portuguese and English, with knots, Fahrenheit, "12 da noite" and numbers that are not limits, graded against a hand-checked key on two prompts: units named only in the field, and units spelled out. Across eight models, six got all 40 with the units spelled out; without them, the misses were knots read as km/h, a wrong Fahrenheit conversion and midnight as hour 0, the same kind of error dapraia caught in a local Gemma. [Write-up](https://dev.to/vinimabreu/keep-the-number-you-wrote-40-beach-plans-8-models-and-where-the-knots-went-3fl2).

</details>

<img src="assets/divider.svg" width="100%" alt="" />

## Data engineering and extraction

<img src="assets/sector-data.svg" width="100%" alt="The layer underneath everything above: scrape, parse, validate, schedule.">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/indicators-dark.svg">
  <img src="assets/indicators-light.svg" alt="Live Central Bank of Brazil indicators rendered by this repo's scheduled pipeline" width="100%">
</picture>

<sub>Not a screenshot: live numbers from the Central Bank of Brazil, refreshed on weekdays by <a href="https://github.com/vinimabreu/vinimabreu/blob/main/.github/workflows/update-indicators.yml">a scheduled pipeline in this repo</a>, committed only when the data changes. The commit history is the proof.</sub>

<a href="https://github.com/vinimabreu/record-refinery"><img src="assets/row-record-refinery.svg" width="100%" alt="record-refinery: Raw business records in, a clean validated deduplicated dataset + a QA brief out"></a>
<a href="https://github.com/vinimabreu/pdf-extract"><img src="assets/row-pdf-extract.svg" width="100%" alt="pdf-extract: Turn PDF documents into validated structured JSON, with pluggable OCR and extraction"></a>
<a href="https://github.com/vinimabreu/docs-to-markdown"><img src="assets/row-docs-to-markdown.svg" width="100%" alt="docs-to-markdown: Scrape any documentation or marketing site into a clean Markdown corpus"></a>
<a href="https://github.com/vinimabreu/ai-watcher"><img src="assets/row-ai-watcher.svg" width="100%" alt="ai-watcher: Monitor RSS/Atom feeds and turn new articles into structured AI summaries"></a>
<a href="https://github.com/vinimabreu/bcb-data-pipeline"><img src="assets/row-bcb-data-pipeline.svg" width="100%" alt="bcb-data-pipeline: Daily ETL of Brazilian macroeconomic indicators (Selic, IPCA, FX) from the BCB SGS API"></a>
<a href="https://github.com/vinimabreu/web-scraper"><img src="assets/row-web-scraper.svg" width="100%" alt="web-scraper: Playwright scraper, SQLite storage and a Streamlit dashboard, end to end"></a>
<a href="https://github.com/vinimabreu/scrape-sentinel"><img src="assets/row-scrape-sentinel.svg" width="100%" alt="scrape-sentinel: The change-aware layer for any scraper"></a>
<a href="https://github.com/vinimabreu/repo-packager"><img src="assets/row-repo-packager.svg" width="100%" alt="repo-packager: Download GitHub repos and deliver clean, deterministic, verifiable ZIPs (manifest + sha256)"></a>
<a href="https://github.com/vinimabreu/cloudrun-pipeline"><img src="assets/row-cloudrun-pipeline.svg" width="100%" alt="cloudrun-pipeline: A data pipeline taken from a local script to a scheduled Cloud Run service, with health checks and retries"></a>
<a href="https://github.com/vinimabreu/crosswatch"><img src="assets/row-crosswatch.svg" width="100%" alt="crosswatch: Cross-source corroboration and scheduled scoring for data you cannot trust from one provider"></a>

<details>
<summary><b>Full notes on these 10</b></summary>

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

</details>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/revenue-demo-dark.svg">
  <img src="assets/revenue-demo-light.svg" alt="revenue-loop's offline demo: a won deal uploaded once to Google and Meta under one conversion key, a click that belongs to another contact quarantined on both, and a re-fired webhook that sends nothing" width="100%">
</picture>

<sub>Captured output: <a href="https://github.com/vinimabreu/revenue-loop">revenue-loop</a>'s offline demo (<code>python -m examples.loop_demo</code>, trimmed to three of its six steps). A won deal reaches Google and Meta once under one conversion key, a click captured for another contact is quarantined on both platforms instead of credited, and the CRM firing the same webhook again sends nothing. All data synthetic.</sub>

<img src="assets/divider.svg" width="100%" alt="" />

## Stack

<p>
<img src="assets/stack-core.svg" alt="Core" height="34"><br>
<img src="https://img.shields.io/badge/Python-0A0E14?style=for-the-badge&logo=python&logoColor=FFB000" alt="Python"> <img src="https://img.shields.io/badge/FastAPI-0A0E14?style=for-the-badge&logo=fastapi&logoColor=FFB000" alt="FastAPI"> <img src="https://img.shields.io/badge/Django%20%2B%20DRF-0A0E14?style=for-the-badge&logo=django&logoColor=FFB000" alt="Django + DRF"> <img src="https://img.shields.io/badge/Celery-0A0E14?style=for-the-badge&logo=celery&logoColor=FFB000" alt="Celery"> <img src="https://img.shields.io/badge/Flask-0A0E14?style=for-the-badge&logo=flask&logoColor=FFB000" alt="Flask"> <img src="https://img.shields.io/badge/Pydantic-0A0E14?style=for-the-badge&logo=pydantic&logoColor=FFB000" alt="Pydantic"> <img src="https://img.shields.io/badge/pytest-0A0E14?style=for-the-badge&logo=pytest&logoColor=FFB000" alt="pytest"> <img src="https://img.shields.io/badge/pandas-0A0E14?style=for-the-badge&logo=pandas&logoColor=FFB000" alt="pandas"> <img src="https://img.shields.io/badge/NumPy-0A0E14?style=for-the-badge&logo=numpy&logoColor=FFB000" alt="NumPy">
</p>

<p>
<img src="assets/stack-retrieval.svg" alt="Retrieval" height="34"><br>
<img src="https://img.shields.io/badge/Chroma-0A0E14?style=for-the-badge" alt="Chroma"> <img src="https://img.shields.io/badge/Qdrant-0A0E14?style=for-the-badge&logo=qdrant&logoColor=FFB000" alt="Qdrant"> <img src="https://img.shields.io/badge/pgvector-0A0E14?style=for-the-badge&logo=postgresql&logoColor=FFB000" alt="pgvector"> <img src="https://img.shields.io/badge/BM25%20%2B%20dense%20embeddings-0A0E14?style=for-the-badge" alt="BM25 + dense embeddings"> <img src="https://img.shields.io/badge/SQLite-0A0E14?style=for-the-badge&logo=sqlite&logoColor=FFB000" alt="SQLite">
</p>

<p>
<img src="assets/stack-models.svg" alt="Models" height="34"><br>
<img src="https://img.shields.io/badge/Claude%20API-0A0E14?style=for-the-badge&logo=anthropic&logoColor=FFB000" alt="Claude API"> <img src="https://img.shields.io/badge/OpenAI-0A0E14?style=for-the-badge&logo=openai&logoColor=FFB000" alt="OpenAI"> <img src="https://img.shields.io/badge/Gemini-0A0E14?style=for-the-badge&logo=googlegemini&logoColor=FFB000" alt="Gemini"> <img src="https://img.shields.io/badge/Ollama-0A0E14?style=for-the-badge&logo=ollama&logoColor=FFB000" alt="Ollama"> <img src="https://img.shields.io/badge/Gemma-0A0E14?style=for-the-badge&logo=google&logoColor=FFB000" alt="Gemma"> <img src="https://img.shields.io/badge/Llama-0A0E14?style=for-the-badge&logo=meta&logoColor=FFB000" alt="Llama"> <img src="https://img.shields.io/badge/Qwen-0A0E14?style=for-the-badge" alt="Qwen"> <img src="https://img.shields.io/badge/Mistral-0A0E14?style=for-the-badge&logo=mistralai&logoColor=FFB000" alt="Mistral"> <img src="https://img.shields.io/badge/LM%20Studio-0A0E14?style=for-the-badge" alt="LM Studio"> <img src="https://img.shields.io/badge/Hugging%20Face-0A0E14?style=for-the-badge&logo=huggingface&logoColor=FFB000" alt="Hugging Face">
</p>

<p>
<img src="assets/stack-agents.svg" alt="Agents" height="34"><br>
<img src="https://img.shields.io/badge/LangGraph-0A0E14?style=for-the-badge&logo=langgraph&logoColor=FFB000" alt="LangGraph"> <img src="https://img.shields.io/badge/LangChain-0A0E14?style=for-the-badge&logo=langchain&logoColor=FFB000" alt="LangChain"> <img src="https://img.shields.io/badge/CrewAI-0A0E14?style=for-the-badge&logo=crewai&logoColor=FFB000" alt="CrewAI"> <img src="https://img.shields.io/badge/MCP-0A0E14?style=for-the-badge&logo=modelcontextprotocol&logoColor=FFB000" alt="MCP"> <img src="https://img.shields.io/badge/Google%20ADK%20%2B%20A2A-0A0E14?style=for-the-badge&logo=google&logoColor=FFB000" alt="Google ADK + A2A">
</p>

<p>
<img src="assets/stack-extraction.svg" alt="Extraction" height="34"><br>
<img src="https://img.shields.io/badge/Playwright-0A0E14?style=for-the-badge&logo=playwright&logoColor=FFB000" alt="Playwright"> <img src="https://img.shields.io/badge/Selenium-0A0E14?style=for-the-badge&logo=selenium&logoColor=FFB000" alt="Selenium"> <img src="https://img.shields.io/badge/Scrapy-0A0E14?style=for-the-badge&logo=scrapy&logoColor=FFB000" alt="Scrapy"> <img src="https://img.shields.io/badge/Tesseract%20OCR-0A0E14?style=for-the-badge" alt="Tesseract OCR"> <img src="https://img.shields.io/badge/AWS%20Textract-0A0E14?style=for-the-badge" alt="AWS Textract">
</p>

<p>
<img src="assets/stack-automation.svg" alt="Automation" height="34"><br>
<img src="https://img.shields.io/badge/n8n-0A0E14?style=for-the-badge&logo=n8n&logoColor=FFB000" alt="n8n"> <img src="https://img.shields.io/badge/Make-0A0E14?style=for-the-badge&logo=make&logoColor=FFB000" alt="Make"> <img src="https://img.shields.io/badge/Clay-0A0E14?style=for-the-badge" alt="Clay"> <img src="https://img.shields.io/badge/Airtable-0A0E14?style=for-the-badge&logo=airtable&logoColor=FFB000" alt="Airtable"> <img src="https://img.shields.io/badge/Xero-0A0E14?style=for-the-badge&logo=xero&logoColor=FFB000" alt="Xero"> <img src="https://img.shields.io/badge/Dropbox-0A0E14?style=for-the-badge&logo=dropbox&logoColor=FFB000" alt="Dropbox"> <img src="https://img.shields.io/badge/PDFMonkey-0A0E14?style=for-the-badge" alt="PDFMonkey"> <img src="https://img.shields.io/badge/Microsoft%20365-0A0E14?style=for-the-badge" alt="Microsoft 365"> <img src="https://img.shields.io/badge/Twilio-0A0E14?style=for-the-badge&logo=twilio&logoColor=FFB000" alt="Twilio"> <img src="https://img.shields.io/badge/Retell-0A0E14?style=for-the-badge" alt="Retell"> <img src="https://img.shields.io/badge/ElevenLabs-0A0E14?style=for-the-badge&logo=elevenlabs&logoColor=FFB000" alt="ElevenLabs"> <img src="https://img.shields.io/badge/Streamlit-0A0E14?style=for-the-badge&logo=streamlit&logoColor=FFB000" alt="Streamlit">
</p>

<p>
<img src="assets/stack-full-stack-web.svg" alt="Full-stack web" height="34"><br>
<img src="https://img.shields.io/badge/TypeScript-0A0E14?style=for-the-badge&logo=typescript&logoColor=FFB000" alt="TypeScript"> <img src="https://img.shields.io/badge/JavaScript-0A0E14?style=for-the-badge&logo=javascript&logoColor=FFB000" alt="JavaScript"> <img src="https://img.shields.io/badge/React-0A0E14?style=for-the-badge&logo=react&logoColor=FFB000" alt="React"> <img src="https://img.shields.io/badge/Next.js-0A0E14?style=for-the-badge&logo=nextdotjs&logoColor=FFB000" alt="Next.js"> <img src="https://img.shields.io/badge/Vue-0A0E14?style=for-the-badge&logo=vuedotjs&logoColor=FFB000" alt="Vue"> <img src="https://img.shields.io/badge/Node.js-0A0E14?style=for-the-badge&logo=nodedotjs&logoColor=FFB000" alt="Node.js"> <img src="https://img.shields.io/badge/Vite-0A0E14?style=for-the-badge&logo=vite&logoColor=FFB000" alt="Vite"> <img src="https://img.shields.io/badge/Deno-0A0E14?style=for-the-badge&logo=deno&logoColor=FFB000" alt="Deno"> <img src="https://img.shields.io/badge/Capacitor-0A0E14?style=for-the-badge&logo=capacitor&logoColor=FFB000" alt="Capacitor"> <img src="https://img.shields.io/badge/Vercel-0A0E14?style=for-the-badge&logo=vercel&logoColor=FFB000" alt="Vercel"> <img src="https://img.shields.io/badge/Supabase-0A0E14?style=for-the-badge&logo=supabase&logoColor=FFB000" alt="Supabase">
</p>

<p>
<img src="assets/stack-identity-trust.svg" alt="Identity & trust" height="34"><br>
<img src="https://img.shields.io/badge/AWS%20Rekognition%20face%20match-0A0E14?style=for-the-badge" alt="AWS Rekognition face match"> <img src="https://img.shields.io/badge/document%20%2B%20liveness%20KYC%20flows-0A0E14?style=for-the-badge" alt="document + liveness KYC flows"> <img src="https://img.shields.io/badge/privacy--by--design%20under%20LGPD-0A0E14?style=for-the-badge" alt="privacy-by-design under LGPD">
</p>

<p>
<img src="assets/stack-ops.svg" alt="Ops" height="34"><br>
<img src="https://img.shields.io/badge/Docker-0A0E14?style=for-the-badge&logo=docker&logoColor=FFB000" alt="Docker"> <img src="https://img.shields.io/badge/GitHub%20Actions-0A0E14?style=for-the-badge&logo=githubactions&logoColor=FFB000" alt="GitHub Actions"> <img src="https://img.shields.io/badge/PostgreSQL-0A0E14?style=for-the-badge&logo=postgresql&logoColor=FFB000" alt="PostgreSQL"> <img src="https://img.shields.io/badge/Google%20Cloud%20Run-0A0E14?style=for-the-badge&logo=googlecloud&logoColor=FFB000" alt="Google Cloud Run">
</p>

<img src="assets/divider.svg" width="100%" alt="" />

## How I work

<img src="assets/how-i-work.svg" width="100%" alt="Grounded: answers cite their sources and refuse when the evidence is not there. Tested: deterministic suites that run with no API key and no network; CI gates catch regressions. Honest: trade-offs go in the README; rag-quality ships the eval showing hybrid retrieval was not a free win on its corpus.">

<img src="assets/quote-1.svg" width="100%" alt="Recent client review: He built a reusable, profile-driven Python data cleansing framework with strong architecture, clear documentation, automated tests, and disciplined output controls. [...] The final delivery was professional, well-structured, tested, and ready for the next productisation phase. I would confidently work with Vinicius again.">

<img src="assets/quote-2.svg" width="100%" alt="Another client review: completed the work ahead of schedule and with accuracy. I would hire him again.">

<img src="assets/cta.svg" width="100%" alt="Open to AI engineering, RAG, agents, and data work. RAG and LLM systems, agents and automations, scraping and data pipelines, all built with tests and CI. Based in Brazil, working with clients worldwide.">

<p align="center"><a href="https://vinimabreu.dev"><img src="assets/button-casestudies.svg" alt="Full portfolio and case studies at vinimabreu.dev" width="560"></a></p>

<img src="assets/divider.svg" width="100%" alt="" />
