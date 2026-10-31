# Agentic AI (Andrew Ng / DeepLearning.AI) — Interview-Oriented Overview + Index

- **Course:** Agentic AI — DeepLearning.AI, instructor Andrew Ng
- **Course link:** https://learn.deeplearning.ai/courses/agentic-ai/information

**How to use these notes (two layers):**

- **This file = interview overview + index + cross-module cheat sheet + rapid-fire Q&A.** Skim this one before an interview to answer most questions.
- **`M1_notes.md … M5_notes.md` = detailed per-module notes (the video-explanation layer).** When a point is fuzzy, open the relevant module for Andrew's intuition, worked examples, and that module's interview Q&A.

**Source basis:** these notes were synthesized from the 32 local transcript files attributed to the course videos and the five locally stored lecture PDFs. Consult the current DeepLearning.AI course platform for authoritative course content.

---

## The whole course in one line

**Agentic AI = using an LLM to run a multi-step, iterative, tool-using workflow to complete a task.**

Two things run through the entire course:

- **Two core skills:** task decomposition, and a disciplined development process centered on evals / error analysis.
- **Four design patterns (the framework):** Reflection, Tool use, Planning, Multi-agent.

Andrew's recurring interview quote:

> The biggest predictor of who builds agentic workflows well is whether they can drive a disciplined development process focused on evals and error analysis.

He also states plainly: **interviews are often assessing exactly the skills taught in this course.**

---

## Module index (click into the detailed notes)

| Module | Topic | Core in one line | Detailed notes |
|---|---|---|---|
| **M1** | Introduction to agentic workflows | what is agentic, degrees of autonomy, benefits, task decomposition, intro to evals, the four patterns | [M1_notes.md](M1_notes.md) |
| **M2** | Reflection design pattern | have the LLM review and improve its own output; external feedback makes reflection much stronger | [M2_notes.md](M2_notes.md) |
| **M3** | Tool use (function calling) | a tool is code the LLM can request to execute; JSON Schema, code execution, MCP | [M3_notes.md](M3_notes.md) |
| **M4** | Practical tips (evals & error analysis) | eval-driven development, read traces, the 2×2 eval, component-level evals, improvement levers | [M4_notes.md](M4_notes.md) |
| **M5** | Patterns for highly autonomous agents | planning (incl. code execution), multi-agent, communication patterns | [M5_notes.md](M5_notes.md) |

---

## The four design patterns — cheat sheet (memorize)

| Pattern | One line | Key mechanism | Control difficulty |
|---|---|---|---|
| **Reflection** | LLM critiques and improves its own output | generate v1 → reflect → v2; stronger with external feedback (run code, read errors) | Low, easy to implement |
| **Tool use** | Give the LLM callable functions to extend it | function calling / JSON Schema; LLM picks tools; code execution; MCP | Medium |
| **Planning** | LLM produces and executes a multi-step plan itself | JSON plan or **express the plan as code**; for tasks with unknown steps | High, experimental |
| **Multi-agent** | Multiple role agents collaborate | manager coordinates workers; patterns linear/hierarchical/all-to-all | High, unpredictable |

---

## Key cross-module data / conclusions (cite in interviews)

- **HumanEval coding benchmark** (M1): GPT-3.5 direct 40%, GPT-4 direct 67%; wrapping GPT-3.5 in an agentic workflow exceeds 67% → **the workflow gain often beats a model upgrade.**
- **Self-Refine (Madaan et al., 2023)** (M2): reflection consistently beats direct generation across tasks (mileage may vary).
- **SQL agent reflection eval** (M2): no reflection 87% → with reflection 95%.
- **Code actions > JSON > plain text** (M5, Wang et al.): having the LLM express plans as code yields the highest success rate.
- **MCP** (M3, Anthropic): turns the **m×n** integration explosion (m apps × n services) into **m+n.**
- **PII redaction comparison** (M4): Llama 3.1 8B fails to follow the format and misses PII; the frontier model gets it all right → large models follow instructions better.
- **Error rates need not sum to 100%** (M4): in error analysis per component, errors aren't mutually exclusive.

---

## Glossary (interview-ready terms)

- **agentic workflow:** a process where an LLM executes multiple steps to complete a task (vs zero-shot single-pass generation).
- **degrees of autonomy:** less / semi / highly autonomous; highly autonomous can create new tools.
- **task decomposition:** break a task into discrete steps; for each, ask "can an LLM/code/tool do it?"
- **human-in-the-loop:** insert human review at critical steps.
- **reflection:** the LLM critiques and improves its own output.
- **external feedback:** feedback from outside the LLM (code errors, web search, word count, regex matching).
- **zero/one/few-shot:** prompt with 0/1/several example pairs.
- **tool use / function calling:** give the LLM functions it can request to execute; under the hood it's JSON Schema.
- **aisuite:** a library that takes a Python function directly as a tool and auto-generates its schema.
- **code execution + sandbox:** let the LLM write and run code; isolate risk with a sandbox (Docker/E2B).
- **MCP (Model Context Protocol):** a standardized tool-connectivity protocol (clients / servers).
- **evals:** objective (code-checked) vs subjective (LLM-as-judge); end-to-end vs component-level.
- **LLM-as-judge:** use another LLM to score; watch for **position bias**; **sum binary 0/1 rubric criteria** rather than scoring 1–5 directly.
- **ground truth:** the correct answer; per-example GT = each example has its own correct answer.
- **error analysis / traces / spans:** read intermediate outputs to find the bottleneck; trace = all intermediate outputs, span = a single step's output.
- **planning:** the LLM produces a step-by-step plan (JSON / code) itself and executes it.
- **multi-agent:** multiple role agents collaborate; communication patterns = linear / hierarchical / deeper hierarchy / all-to-all.

---

## Rapid-fire cross-module interview Q&A

**Q: What is agentic AI, and how is it different from just prompting an LLM?**
A: An LLM-based app that executes **multiple steps** to complete a task — iterative, tool-using, can insert human review. Vs zero-shot single-pass generation. Slower but much higher quality.

**Q: Why are agentic workflows worth it (any data)?**
A: Performance (HumanEval 40%/67%; wrapping in a workflow beats upgrading the model), parallelism for speed, modularity.

**Q: How do you turn a complex task into an agentic workflow?**
A: Task decomposition — break into discrete steps; for each ask "can an LLM / code / function call / tool do it?"; if not, think "how would a human do it" and decompose further; build an initial version then iterate.

**Q: What are the four design patterns, when to use each, and which are hard to control?**
A: Reflection (improve own output, easy), Tool use (extend capability, medium), Planning (self-plans, high/experimental), Multi-agent (role agents collaborate, high/unpredictable).

**Q: How does reflection work, and how do you make it stronger?**
A: Generate → reflect → improve; adding external feedback (run code and read errors, web-search fact-check, word count, regex competitor check) is far stronger than pure self-reflection.

**Q: How does function calling work under the hood?**
A: Functions are turned into JSON Schema (name/description/parameters from the function name, docstring, signature) described to the LLM; the LLM decides to call and produces arguments; the program executes and feeds results back, looping some number of turns.

**Q: Why is code execution better than many fine-grained tools? Risks?**
A: Fine-grained tools don't scale and need constant additions for edge cases; writing code lets the LLM call hundreds of library functions it knows. Risk = executing arbitrary code; needs a sandbox.

**Q: What is MCP and what does it solve?**
A: Anthropic's standardized tool-connectivity protocol; turns m×n integration into m+n; ecosystem has clients (Cursor/Claude Desktop) and servers (GitHub/Slack/PostgreSQL).

**Q: How do you evaluate an agent?**
A: Build a prototype first, look at outputs to find error modes, then build a 10–20-example eval; use the 2×2 framework (objective/judge × with/without per-example GT); end-to-end + component-level. Use a rubric for subjective evals to avoid position bias.

**Q: How do you do error analysis and prioritize?**
A: Read traces (trace/span), tally per-component error rates in a spreadsheet (needn't sum to 100%), prioritize by "high frequency × fixability."

**Q: After locating a bottleneck component, how do you improve it?**
A: Non-LLM: tune hyperparameters / swap provider; LLM: improve prompt/few-shot, try a new model, split the step, fine-tune (last resort).

**Q: How do you optimize latency and cost?**
A: Quality first, optimize later (quality > cost > latency); time/price each step to locate hotspots; parallelize, swap to a smaller/faster model, swap to a cheaper component.

**Q: How does planning work, and why express a plan as code?**
A: Have the LLM produce a step-by-step plan (JSON is most reliable) and execute it; or write code directly — more expressive, and Wang et al. show the highest success rate. For tasks with unknown steps.

**Q: Why multi-agent, and what communication patterns exist?**
A: Analogy of hiring a multi-role team; eases decomposition, division of labor, reuse. Patterns: linear, hierarchical (manager coordinates workers — the two most common), deeper hierarchy, all-to-all (unpredictable).

**Q: What's the single most important engineering habit for building agentic systems?**
A: The Build ↔ Analyze loop; drive it with evals and build the habit of reading traces. Beginners only build and under-analyze, wasting weeks on components that don't move the result.

---

## Where the source material lives

- Lecture PDFs: `lectures/agentic_ai_M1~M5_*.pdf` (renamed by module title)
- Video transcripts: `lectures/transcripts/M1~M5/` (.txt files named by section number)
- Detailed notes: `notes/M1~M5_notes.md`

*Last updated: 2026-10-28 — built from 32 video transcripts + 5 lecture PDFs*
