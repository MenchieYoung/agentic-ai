# M1 — Introduction to Agentic Workflows (Interview-Oriented Notes)

> Source: all 8 video transcripts of Module 1 of Andrew Ng's *Agentic AI* course (Andrew's actual narration) + the lecture PDF. Transcripts are the primary source; the PDF supplies figures/benchmarks.

## Module Overview (the throughline in one line)
M1 answers four questions: **what is agentic AI → how autonomous (degrees of autonomy) → why it's useful (benefits) → how to build it (applications → task decomposition → evals → the four design patterns)**. Two core skills are hammered throughout the whole course: **task decomposition** and **a disciplined development process centered on evals and error analysis**. The running example across the course is a **research agent**.

---

## 1. Welcome (rarely asked directly, but memorize the key line)
- Andrew coined the term "agentic." Marketers slapped it on everything like a sticker, which made the hype skyrocket. But setting the hype aside, the number of genuinely valuable agentic applications is also growing fast.
- Deployed use cases: customer support agents, deep research (writing insightful research reports), processing tricky legal documents, suggesting possible medical diagnoses from patient input. Andrew: many projects his teams built **would be impossible without agentic workflows**.
- **The key quote (worth citing in interviews):** the biggest difference between people who are good at building agentic workflows and those who aren't is **the ability to drive a disciplined development process, specifically one focused on evals and error analysis.**

---

## 2. What is Agentic AI

**Core definition (memorize):** An agentic AI workflow is a process where an **LLM-based app executes multiple steps** to complete a task.

**The intuition/analogy (Andrew's, interview-frequent):**
- **Non-agentic / zero-shot:** like asking a person to "type out an essay from the first word to the last in one go, without ever using backspace." People don't write their best that way, and neither do LLMs — though, remarkably, LLMs still do surprisingly well under that constraint.
- **Agentic workflow:** mirrors how people actually work — write an outline → decide if web research is needed → download pages → write a first draft → read it and find what needs revision → revise → ... iterate.
- **The core trade-off:** an agentic workflow **takes longer but delivers a much better work product.**

**In the essay workflow,** each step may call an LLM: use an LLM to write the outline → use an LLM to decide search terms (call a web search API) → feed downloaded pages to an LLM to write a first draft → use another LLM to reflect on what needs revising → optionally insert a **human-in-the-loop** step (let the LLM request human review of key facts) → revise.

**Running example (research agent):** enter a research topic (Andrew's example: "how do I build a new rocket company to compete with SpaceX") → the agent plans what research to do → calls web search and downloads pages → synthesizes & ranks findings → drafts an outline → an **editor agent** reviews for coherence → produces a comprehensive markdown report. Andrew has built many specialized research agents (legal compliance, healthcare, business product research), so the ideas transfer directly.

**Interview point:** be able to state the agentic vs zero-shot distinction, the definition, and the "slower but higher quality" trade-off.

---

## 3. Degrees of Autonomy

**Why "agentic" instead of "agent" (interview-frequent, shows depth):** a few years ago the AI community argued over "what counts as a true agent" (someone publishes "I built an agent," others say "that's not really an agent"). Andrew found this binary debate pointless, so he **used the adjective "agentic" rather than the noun "agent"** — acknowledging that systems can be agentic to **different degrees**. Stop debating whether something qualifies and just build. He popularized this via *The Batch* newsletter and social media, which helped the field move past the debate.

**The autonomy spectrum (example: "write an essay about black holes"):**
| Degree | Characteristics |
|---|---|
| **Less autonomous** | Fully deterministic, predetermined sequence of steps; tool calls (tool use) hard-coded by the engineer; autonomy is only in what text the LLM generates |
| **Semi-autonomous** | Agent makes some decisions, chooses tools; but tools are predefined |
| **Highly autonomous** | Agent decides the sequence of steps itself; can even **write new functions / create new tools on the fly** |

**Notational convention (used throughout the course, useful for diagram questions):**
- **Red** = user input (a query, or an input document)
- **Gray box** = a call to an LLM
- **Green box** = other software actions (web search API, executing code to fetch a page, etc.)

**Andrew's practical take:** there are tons of **high-value** applications being built at the less-autonomous end for businesses today; the highly-autonomous end is harder to control, more unpredictable, and still an area of active research.

---

## 4. Benefits of Agentic AI (three benefits)

**Three benefits:** ① performance (most important) ② parallelism (→ speed) ③ modularity.

**(1) Performance — the HumanEval coding benchmark (memorize the numbers):**
- GPT-3.5 writing code directly (non-agentic): **40%**
- GPT-4 writing code directly (non-agentic): **67%**
- **Key conclusion:** wrapping GPT-3.5 in an agentic workflow (write code + reflect to improve) pushes performance well above 67% — **the huge jump from GPT-3.5 to GPT-4 is still dwarfed by what an agentic workflow does on the older model.** This is the canonical "workflow beats model upgrade" argument.

**(2) Parallelism:** for the black-holes essay, you can run 3 LLMs in parallel to generate search terms → 9 pages total → **download all 9 pages in parallel** and feed them to an LLM. A human reads pages sequentially, so an agentic workflow can actually be faster than a human (even though it's slower than a single zero-shot call).

**(3) Modularity:** add/swap components freely — change the web search engine (Google, Bing, DuckDuckGo, Tavily, you.com — many are designed for LLMs to use), swap in a news search engine, or use different LLMs / providers for different steps.

**Interview point:** be able to recall 40% / 67% and summarize it as "the gain from an agentic workflow often exceeds the gain from upgrading the model."

---

## 5. Agentic AI Applications (by increasing difficulty — interviewers love "what tasks suit agents")

1. **Invoice processing (easy):** extract 4 fields — biller (TechFlow Solutions), biller address, amount due ($3,000), due date (Aug 20, 2025). Flow: input invoice → call a **PDF-to-text API** → LLM decides if it's even an invoice → extract fields → call a tool to update the database. **Clear process → easy and reliable.**
2. **Customer order inquiry (a bit harder):** ① extract key info (who, what they ordered, order number) ② look up customer records in the orders database ③ draft a response for human review (request-review tool queues it). Still a clear step-by-step process.
3. **General customer-service agent (harder, steps unknown):** e.g. "do you have black or blue jeans?" needs multiple planned inventory queries; "I'd like to return the beach towel I bought" needs verifying the purchase + checking the return policy (e.g. within 30 days + unused) → if allowed, issue a return packing slip + set the record to "return pending." **Required steps aren't known ahead of time — the LLM must plan them itself.**
4. **Computer use (hardest, cutting-edge):** e.g. check seat availability on two United flights SFO→DCA. The agent drives a browser, clicks page elements, fills forms, reasons over page content. When the United site fails, it navigates to Google Flights, then returns to United to confirm. Andrew admits agents often struggle with browsers (slow page loads confuse them, many pages are hard to parse accurately), so it's **not reliable enough for mission-critical use yet**, but an important future direction.

**Easy vs hard framework (interview-frequent, be able to reproduce):**
| Easier | Harder |
|---|---|
| Clear step-by-step process | Steps not known ahead of time (plan/solve as you go) |
| Standard operating procedure to codify | Must plan on the fly |
| Text-only assets | Rich multimodal input (sound/vision/audio) |

---

## 6. Task Decomposition (one of the two most core skills in the course)

**The core method (must be able to answer):** break down what a person/business does into **discrete steps**. For each step, keep asking: **can this step be done by ① one LLM, ② a short piece of code, ③ a function call, or ④ a tool?** If "no," ask "**how would I as a human do this step?**" and decompose it into smaller steps.

**Iterative decomposition of essay writing (Andrew's own experience):**
- Direct generation (1 step) → too surface-level, only obvious facts.
- Break into 3 steps (outline → web search → write) → Andrew did exactly this and the result felt **disjointed** (start, middle, end didn't feel consistent).
- So decompose "write" further: write a first draft → consider what needs revision → revise → a richer process.
- **Takeaway:** build an initial decomposition, then **iterate repeatedly** until satisfied.

**Building blocks (worth enumerating in interviews):**
- **Models:** LLMs / large multimodal models (generate text, decide what to call, extract info); specialized AI models (PDF→text, text-to-speech, image analysis).
- **Tools — APIs:** web search, real-time weather, send email, check calendar, ...
- **Tools — information retrieval:** database queries, RAG (retrieval augmented generation — look up the most relevant text in a large text database).
- **Tools — code execution:** let the LLM write code and run it on your machine; extremely broad capability.

**Interview point:** articulate the "for each step, can an LLM/tool do it? if not, decompose further" loop, and list the building blocks.

---

## 7. Evaluating Agentic AI (the most critical skill in the course; deep dive in M4)

**Andrew's core claim (interview quote):** across many teams, **the biggest predictor of who builds agentic workflows well is whether they can drive a disciplined evaluation process.**

**Methodology (counterintuitive but important):** **don't design evals in advance.** It's very hard to know ahead of time what will go wrong. Instead: **build the system first → read many outputs and manually find things you wish it did better → then work backward to define evals.**

**Example: competitor mentions** — many businesses don't want their agent mentioning competitors. Reading outputs, you find lines like "we're much better than our competitor ComproCo" / "Unlike RivalCo, we make returns easy."
- This is an **objective** metric: mentioned or not, black and white.
- Keep a named list of competitors (ComproCo, RivalCo, the other co) and **write code** to count the frequency/fraction of mentions.

**LLM-as-a-judge (subjective metrics):** LLMs output free text, so some criteria (like essay quality) are hard to score with code. Use another LLM to score, e.g. "assign this essay a quality score from 1 to 5, 5 is best." Example: the black-holes essay scores 3, the robot-fruit-harvesting essay scores 4.
- **Andrew's candid caveat (a plus in interviews):** LLMs are **actually not that good at 1–5 ratings**, and he rarely uses this himself; M4 covers better methods (e.g. rubrics).

**Two kinds of evals (preview of M4):** **end-to-end** (measure the whole agent's output) vs **component-level** (measure a single step) — each drives a different part of development.

**Error analysis:** read the intermediate outputs (aka **traces**) of each step to spot where it falls short. Evals + error analysis is a key skill (M4 focus).

---

## 8. Agentic Design Patterns (the four — the course framework)

The four patterns: **Reflection, Tool use, Planning, Multi-agent collaboration.**

**① Reflection:** have an LLM write code → construct a prompt asking it to "check the code for correctness, style, efficiency and give constructive criticism" → it points out problems → feed the critique back ("looks like a bug, fix it") → a better version. You can add external feedback (**run the code, feed back the error messages**, iterate to v3). You can also use a separate **critique agent** (an LLM given the persona "your role is to critique code") going back and forth with a coder agent. **Andrew stresses: it's not magic, not 100% reliable, but often gives a nice bump.**

**② Tool use:** give the LLM callable functions. E.g. "best coffee maker according to reviewers" → web search; "invest $100 at compound interest, what do I have at the end?" → code execution. Tools span information gathering / data analysis / productivity apps (email, calendar) / image processing. **The LLM decides which tools to call**, which lets it get much more done.

**③ Planning:** cites the **HuggingGPT** paper — "generate an image of a girl reading with the same pose as the boy in image X, then describe it in your voice" → the model decides on its own: pose-determination model → pose-to-image → image-to-text → text-to-speech. **The LLM decides the sequence of API calls** instead of the developer hard-coding it. Andrew: planning agents are **harder to control and more experimental**, but sometimes give delightful results.

**④ Multi-agent collaboration:** cites **ChatDev** (Chen Qian et al.) — role agents (CEO / programmer / tester / designer) collaborate like a virtual software company. Another example: a marketing brochure = researcher + marketer + editor. **Harder to control** (you don't always know what agents will do), but research shows **better outcomes** for complex tasks (writing biographies, choosing chess moves).

**Wrap-up:** an agentic workflow = building blocks + design patterns + eval-driven iteration. The next module dives into Reflection.

---

## Interview Q&A (M1)

**Q1: How does an agentic workflow differ from a direct (zero-shot) prompt?**
A: Zero-shot is a single linear generation (like "write it all at once, no backspace"); agentic is multi-step + iterative + can use tools and human review. Agentic is slower but much higher quality.

**Q2: Why does Andrew use "agentic" instead of "agent"?**
A: To end the binary "what is a true agent" debate. The adjective expresses that systems have **different degrees of autonomy**, letting people focus on building rather than defining.

**Q3: What are the benefits of agentic workflows? Any data?**
A: Performance (most important), parallelism for speed, modularity. HumanEval: GPT-3.5 direct 40%, GPT-4 direct 67%; wrapping GPT-3.5 in an agentic workflow exceeds 67% — **the workflow gain often beats a model upgrade.**

**Q4: What tasks suit / don't suit agentic AI?**
A: Suit — clear decomposable process, standard procedure to codify, text-only. Harder — steps unknown in advance (plan as you go), rich multimodal input, computer use (not reliable enough).

**Q5: How do you do task decomposition?**
A: Break into discrete steps; for each, ask "can an LLM / code / function call / tool do it?" — if not, think "how would a human do it" and decompose further; build an initial version then iterate. Building blocks: LLMs/multimodal models, specialized AI models, API tools, retrieval (DB/RAG), code execution.

**Q6: How do you evaluate an agentic system, and why not design evals up front?**
A: Build first, read outputs, manually find problems, then work backward to evals (you can't know in advance what will break). Objective criteria → write code (e.g. competitor mentions); subjective → LLM-as-judge (but 1–5 scoring is unreliable; M4 has better methods). Two kinds: end-to-end and component-level; pair with reading traces for error analysis.

**Q7: What are the four agentic design patterns, and which are harder to control?**
A: Reflection, Tool use, Planning, Multi-agent. Planning and Multi-agent are harder to control and more experimental but can do better on complex tasks.

**Q8: Why are evals / error analysis the most critical skill?**
A: Andrew calls it the biggest predictor of building agentic workflows well. Workflows need repeated iteration; evals give the improvement signal, and error analysis pinpoints which component is failing so you can decide efficiently what to fix.
