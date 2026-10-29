# M5 — Patterns for Highly Autonomous Agents (Planning & Multi-Agent, Interview-Oriented Notes)

> Source: all 6 video transcripts of Module 5 of Andrew Ng's *Agentic AI* course + the lecture PDF.

## Module Overview
M5 covers **highly autonomous agents**: no longer hard-coding the sequence of steps — letting the system decide for itself. Two main themes: **Planning** and **Multi-agent**. A core trade-off runs throughout: **give up some control (harder to control / you don't know at runtime what will happen) in exchange for a much wider range of tasks.**

---

## 1. Planning Workflows

**Core concept:** give the LLM a set of tool descriptions + have it **produce a step-by-step plan itself**, then execute it step by step. Suited to **tasks whose steps aren't known in advance.**

**Sunglasses retail customer-service example (runs through the module):** inventory is in a database. A user asks "do you have any round sunglasses in stock under $100?" — a complex query: look through descriptions for round ones, check what's in stock, check what's under $100. Give the LLM tools: `get_item_descriptions` / `check_inventory` / `process_item_return` / `get_item_price` / `check_past_transactions` / `process_item_sale`...

**The planning prompt:** `"You have access to the following tools {descriptions}. Return a step-by-step plan to carry out the user's request."` The LLM produces a plan: ① `get_item_descriptions` to find round ones ② `check_inventory` for stock ③ `get_item_price` for <$100.

**Execution mechanism (interview key):** take the Step 1 text + tools + user query + background context → have an LLM execute step 1 (calling `get_item_descriptions`) → **step 1's output + step 2's instructions** are fed to the next LLM call → ... → one final LLM call produces the user-facing answer. Andrew notes real plans are more detailed than these one-line descriptions, but the skeleton is "have an LLM write a multi-step plan, then execute each step in turn with the right surrounding context."

**Another example (return):** "return the gold-frame glasses I purchased but not the metal-frame ones" → the LLM comes up with a different plan: `check_past_transactions` to find what they bought → `get_item_descriptions` to find the gold-frame ones → `process_item_return`. **Same tools, different request, the LLM orchestrates a different order** — that's the power of planning.

**Email assistant example:** "reply to Bob's dinner invitation in New York saying I'll attend, then archive his email" → tools `search_email` / `move_email` / `delete_email` / `send_email` → plan: ① `search_email` to find Bob's email mentioning dinner + New York ② `send_email` to confirm attendance ③ `move_email` to the archive.

**Andrew's practical take (interview plus):** planning is already very successful in **highly agentic coding systems** (ask it to write complex software and it produces a checklist — "build component 1, then 2..." — executed step by step). But in other domains planning is still **more experimental and not in widespread use**; the main difficulty is being **hard to control** — as a developer you don't know at runtime what plan it will produce.

---

## 2. Creating and Executing LLM Plans

**Core technique: format the plan as JSON.** Why? So **downstream code can parse each step unambiguously** and execute reliably; and leading LLMs are now good at generating JSON.

Prompt: `"You have access to the following tools {...}. Create a step-by-step plan in JSON format."` and describe the JSON structure. Output looks like:
```json
{ "plan": [
  { "step": 1, "description": "Find round sunglasses",
    "tool": "get_item_descriptions", "args": {"query": "round sunglasses"} },
  { "step": 2, "description": "Check available stock",
    "tool": "check_inventory", "args": {"items": "results from step 1"} }
]}
```

**Format reliability ranking (Andrew's words, worth citing):** **JSON ≈ XML (both good) > Markdown (a bit ambiguous) > plain text (least reliable).** Prefer JSON or XML to make the plan unambiguous.

---

## 3. Planning with Code Execution (one of the module's most important insights)

**Core idea:** instead of having the LLM emit a JSON plan executed one step at a time, **have the LLM write code directly**, with the code itself expressing the multi-step plan ("call this function, then that one"); executing the code carries out the complex plan.

**Why you need it — the trap of pure tool-based planning (interview-frequent):**
Scenario: process a coffee-machine sales spreadsheet with a pile of fine-grained tools (`get_column_max` / `get_column_mean` / `filter_rows` / `get_column_min` / `sum_rows`...).
- "Which month had the highest hot-chocolate sales?" → `filter_rows` for January + stats → February → ... → December → take the max. Extremely tedious.
- "How many unique transactions last week?" → existing tools insufficient, so you build `get_unique_entries`.
- "Amounts of the last 5 transactions?" → yet another new tool.
- **Conclusion:** this approach is **brittle, inefficient, and endlessly chasing edge cases by adding more tools.**

**The fix:** prompt `"Write code to solve the user's query. Return your answer as Python code delimited with <execute_python> and </execute_python> tags."` The LLM writes **pandas** code: load the CSV → parse the date column → sort → head(5) → print the price column.
- **Why it's powerful (Andrew's key explanation, a depth point):** a programming language (+ pandas) has **hundreds or thousands of built-in functions**, and the LLM has seen **lots of training data on when to call them.** Letting the LLM write code lets it freely pick and chain from that huge library to express a rich plan.

**Empirical support:** cites **Xinyao Wang et al.** (CodeAct / "Executable Code Actions Elicit Better LLM Agents") — **code-as-action > writing JSON then translating to actions > plain-text plan.** Writing code has the highest success rate across most models/tasks.

**Caveat (always mention):** as in M3, executing LLM-generated code calls for a **sandbox**; Andrew admits many developers skip it, but that's not best practice.

**Summary:** highly agentic software coders are planning's most successful application; other domains are still maturing. Giving up some control greatly expands the range of what the model will try.

---

## 4. Multi-Agentic Workflows

**Why multiple agents? (interview-frequent, Andrew's analogy):** people ask "isn't it just the same LLM prompted over and over, one computer?" Analogy: ① even on a single CPU, developers decompose work into multiple processes/threads because it's easier to reason about; ② for a complex task, instead of "who's the one person I'd hire," think "would it make sense to hire a team with 3–4 roles." **This mental frame helps decompose a complex task into subtasks you build one at a time.**

**Tasks that naturally decompose by role:**
| Task | Team roles |
|---|---|
| Create marketing assets | researcher, graphic designer, writer |
| Write a research article | researcher, statistician, lead writer, editor |
| Prepare a legal case | associate, paralegal, investigator |

**Marketing team example (throughline)** — each agent's task and tools:
- **researcher:** analyze market trends, research competitors; tool = **web search.**
- **graphic designer:** create visualizations and artwork; tools = image generation/manipulation APIs, or **code execution to generate charts** (like the coffee-machine example).
- **writer:** turn research into report text and marketing copy; tool = **none** (the LLM's native ability suffices).

**How to build one agent:** prompt an LLM to play the role (e.g. "You are a research agent, expert at analyzing market trends and competitors, carry out online research..."). In diagrams, a **purple box denotes an agent.**

**Linear plan:** give "create a summer marketing campaign for sunglasses" to the researcher → produces a trends & competitor report → feed to the graphic designer → produces visualizations + artwork → feed to the writer → writes the final brochure.
**Advantage (interview point):** when building each agent you can **focus on one thing at a time** (I perfect the graphic designer while a collaborator builds the researcher/writer, then we string them together); and agents can be **reused** (a graphic designer built for brochures can generalize to social posts, webpage illustrations).

**Planning with multiple agents:** **replace the "tools (green boxes)" in planning with "agents (purple boxes)."** Prompt: `"You are a marketing manager and have the following team of agents {descriptions}. Return a step-by-step plan."` The LLM (manager) produces: ① ask the researcher to research trends ② ask the graphic designer to create images ③ ask the writer to write the report ④ review/reflect on it once.
**Key view:** the LLM producing the plan on the left is actually a **fourth agent — the marketing manager** — setting direction and delegating to the other three. So it becomes a set of four agents: **one manager coordinating three workers.**

---

## 5. Communication Patterns for Multi-Agent Systems

**Analogy:** just as designing a company's org chart is complex, designing communication patterns for multi-agent systems is complex too. It's an **active research area.**

**The two most common (know these cold):**
1. **Linear:** researcher → graphic designer → writer, outputs passed down the line.
2. **Hierarchical (manager in the center):** one manager coordinates multiple workers. In practice it's simpler to have the researcher pass results **back to the manager**, who then forwards to the graphic designer, rather than workers passing directly to each other.

**Two advanced ones (less common, but know them):**
3. **Deeper hierarchy:** the researcher under the manager itself calls a web researcher + fact checker; the writer has a style writer + citation checker. Agents calling sub-agents, multiple levels. Much more complex than a one-level hierarchy, used less.
4. **All-to-all:** any agent can message any other at any time; implemented by prompting each agent that there are other agents it can call, messages land in the receiver's context, and the receiver replies when it decides. Agents "talk in a crowd" until all declare done (or the writer decides it's good enough), then produce the final output. **Results are hard to predict** — suited to cases that tolerate some chaos / don't need tight control (if the brochure is bad, just run it again).

**Engineering note:** there are many **software frameworks** that make building multi-agent systems and implementing these patterns relatively easy.

---

## 6. Conclusion (whole-course recap)

Andrew's recap:
- **M1:** agentic AI enables applications that weren't possible before; introduces the four design patterns.
- **M2 Reflection:** simple, often gives a nice performance boost.
- **M3 Tool use / function calling:** expands what the LLM can do, with code execution as an important special case.
- **M4 Evals & error analysis:** drives the disciplined build ↔ analyze process — Andrew considers M4 the "most useful" material for building agentic systems long-term.
- **M5 Planning & multi-agent:** more powerful but harder to control/predict.

**Interview quote (Andrew's words):** when he and other teams interview candidates, they're **often assessing exactly the skills taught in this course** — so it can open professional opportunities. Closing line: "use them responsibly, and go build cool stuff."

---

## Interview Q&A (M5)

**Q1: What is the planning design pattern, and when do you use it?**
A: Give the LLM tool descriptions and have it produce a step-by-step plan, then execute it step by step. Suited to tasks whose steps aren't known in advance. During execution, each prior step's output + the next step's instructions are fed to the LLM.

**Q2: Why format the plan as JSON? What other formats exist?**
A: JSON lets downstream code parse it unambiguously and execute reliably, and LLMs are good at JSON. Reliability: JSON ≈ XML > Markdown > plain text.

**Q3: What is planning with code execution, and why is it often better than many fine-grained tools?**
A: Have the LLM write code (e.g. pandas) that expresses the multi-step plan and execute it. Pure fine-grained tools are brittle / inefficient / require endlessly adding tools for edge cases; a programming language has hundreds of built-in functions the LLM knows well, so code chains them expressively. Wang et al. show code-action > JSON > plain text. Remember the sandbox.

**Q4: Why use multi-agent instead of one LLM prompted repeatedly?**
A: Analogy to a single CPU still using multiple processes, and hiring a multi-role team for a complex task. Benefits: decompose complex tasks, each agent focuses on one thing (easy to build in parallel), agents are reusable.

**Q5: How do you build a concrete agent (e.g. the graphic designer)?**
A: Prompt an LLM to play the role and equip it with the tools that role needs (the graphic designer needs image generation/manipulation APIs or code execution for charts; the writer needs no extra tools).

**Q6: What communication patterns do multi-agent systems have, and their traits?**
A: Most common: linear (pipeline) and hierarchical (manager coordinating workers); advanced: deeper hierarchy (agents calling sub-agents) and all-to-all (fully connected, unpredictable, for chaos-tolerant cases).

**Q7: What's the core cost of planning / multi-agent?**
A: **Harder to control, you don't know at runtime what will happen, results hard to predict.** The payoff is a much larger range of tasks and flexibility. Planning is most mature in agentic coding; other domains are still developing.
