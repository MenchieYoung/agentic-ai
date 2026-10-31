# M4 — Practical Tips for Building Agentic AI (Evals & Error Analysis, Interview-Oriented Notes)

> Source basis: seven local transcript files attributed to Module 4 course videos plus the locally stored lecture PDF. The transcript attributes the description "you'll find most useful" for long-term agentic building to Andrew Ng.

## Module Overview (core methodology)
M4 covers the **engineering practice** — the part interviewers are most likely to drill into. The core:
1. **Eval-driven development** — build a quick-and-dirty prototype first, look at outputs to find error modes, then build a small eval to track.
2. **Read traces to do error analysis** — tally error rates per component to locate the bottleneck.
3. **The two-axis 2×2 evaluation framework.**
4. **A systematic list of improvement levers** (non-LLM vs LLM components).
5. **The Build ↔ Analyze loop** (non-linear).

---

## 1. Evaluations

**Development philosophy (interview quote):** it's hard to know in advance what will/won't work → **build a quick-and-dirty prototype safely and responsibly, look at outputs to set priorities**; the anti-pattern is theorizing for weeks without building. **An eval = test examples + a scoring method.** Build it after you spot a recurring error mode; **start with 10–20 examples** and expand iteratively.

**Example 1 — invoice due date (objective + per-example ground truth):**
Problem: confusing invoice date with due date. Method: ① manually label the true due dates of 10–20 invoices ② have the prompt require a uniform output format `YYYY/MM/DD` ③ regex-extract the date from the LLM response ④ compare to ground truth.
```python
date_pattern = r'\d{4}/\d{2}/\d{2}'
extracted = re.findall(date_pattern, llm_response)
if extracted == actual_date: num_correct += 1
```

**Example 2 — marketing copy length (objective + no per-example GT):**
Instagram caption must be ≤ 10 words, but outputs come in at 17/14/11 words. Build 10–20 test tasks, count words in code and compare to the threshold (the threshold is always 10, so no per-example GT):
```python
word_count = len(text.split())
if word_count <= 10: num_correct += 1
```

**Example 3 — research agent (subjective + per-example GT):**
The black-holes essay misses a high-profile news result; the robot-harvesting essay misses the leading equipment company. Method: ① an expert picks **3–5 gold-standard talking points** per topic (per-example GT) ② use an **LLM-as-a-judge** to count how many are present ③ each prompt scores 0–5. Because phrasing varies, regex won't work, so use a judge returning JSON (score + explanation).

**The two-axis framework (2×2 grid — memorize):**
| | **Per-example ground truth** | **No per-example ground truth** |
|---|---|---|
| **objective (code)** | invoice date extraction | marketing copy length |
| **LLM-as-judge (subjective)** | counting gold-standard talking points | grading a chart with a rubric |
(All of these are **end-to-end evals**: from query to final output.)

**Tips for designing evals:** ① quick & dirty to start is fine ② **iterate the eval**: when it fails to capture human judgment (a human thinks the new system is better but the score didn't move) → expand examples or change the scoring method ③ focus on where it's **worse than a human expert.**

---

## 2. Error Analysis & Prioritizing

**Definition:** when the system performs poorly, **systematically figure out which component is most to blame.** One of the biggest predictors of an efficient team.

**Method (interview-frequent, be able to explain):** **don't go by gut; look at traces.**
- Terms: **trace = all intermediate outputs of one run**; **span = the output of a single step** (from observability).
- In a **spreadsheet**, **look only at unsatisfactory examples**, annotate which component failed, and compute percentages.

**Research agent example (memorize the data):** stages = generate search terms → web search → fetch → pick best 5 → write essay. Tally:
- search terms unsatisfactory: **5%** (experts approve the search terms)
- web search results unsatisfactory: **45%** (returns too many blogs/kid-science like "Astro Kid News," not enough papers) ← **the biggest bottleneck**
- **Attribution trap:** if the inputs are all low-quality articles, don't blame the "pick best 5" step (garbage in).

**Prioritization formula (interview point):** **high error frequency × you have an idea how to fix it** → prioritize. For the research agent: focus on web search (swap engine, tune result count / date range).

---

## 3. More Error Analysis Examples

**Example A — invoice processing:** suspect stages = PDF-to-text vs LLM extraction. Take 10–100 erroneous examples and do spreadsheet attribution: PDF-to-text wrong **15%**, LLM data extraction wrong **87%** → focus on the LLM extraction, not PDF-to-text.
**Important (interview point):** per-component error rates **need not sum to 100%**, because errors aren't mutually exclusive (one example may fail at multiple stages).

**Example B — customer email:** flow = LLM reads email → writes DB query → fetches order → drafts reply. Tally: **75%** of errors from the SQL query (wrong table, etc.), ~**30%** of drafted emails have issues (didn't address order details, defensive tone), the database is mostly correct (~4%) → fix the query first, improve the email-drafting prompt second.

---

## 4. Component-Level Evaluations

**Why you need it (interview point):** **end-to-end eval is expensive** — changing one thing forces a full-chain re-run; and noise from other components drowns out a small improvement's signal.

**Method — evaluate only the web search component:**
- Build a **gold-standard list of web pages.**
- Write code to measure overlap between returned results and the gold standard, e.g. **F1-score.**
- Track it while tuning that component's hyperparameters (swap Google / Bing / DuckDuckGo / Tavily / You.com, change result count, date range).
- **Still run the end-to-end eval at the end** to confirm overall improvement.

**Benefits:** clearer signal, avoids end-to-end noise, lets multiple teams work in parallel each on one component metric, faster iteration on smaller problems.

---

## 5. How to Address Problems You Identify (improvement levers)

**Improving non-LLM components:**
- **Tune hyperparameters:** web search (result count, date range); RAG (similarity threshold, chunk size); ML models (detection threshold, trading off false positives / false negatives).
- **Replace the component:** swap the search engine / RAG provider.

**Improving LLM components (interview-frequent list):**
1. **Improve the prompt:** add more explicit instructions; add one or more concrete examples (**few-shot**).
2. **Try a new model:** try several LLMs and pick the best with evals (**aisuite / AI Suite makes swapping easy**).
3. **Split up the step (task decomposition):** break into smaller steps, or into generation + reflection.
4. **Fine-tune:** the **last resort** — complex and expensive, only for a mature app already at 90–95% where you want to squeeze the last few points, and you have internal data.

**PII redaction comparison (instruction following, a good interview case):** given a customer-support summary containing PII (date, Jessica Alvarez, SSN, address, ticket number), asked to "identify all PII and classify it, redact with `*****`, separate the list and redacted text with `REDACTED:`":
- **Llama 3.1 8B** (small open-weight): didn't follow the format, missed a name, only partially redacted the address.
- **A frontier large model (GPT-5):** followed the format correctly, identified and redacted all PII.
- **Conclusion:** frontier large models are better at **following instructions**; small models can handle simple facts but follow instructions poorly; different providers have different strengths.

**Developing model intuition (how you'd answer "how do you pick a model"):** play with new models often (closed + open), keep a personal eval set, read lots of other people's prompts, try different models in real workflows (look at traces + component/end-to-end evals to feel the performance/price/speed trade-offs).

---

## 6. Latency & Cost Optimization

**Principle (interview quote):** **quality first, optimize later**; priority is **quality > cost > latency.** Andrew lived through a user explosion making cost a problem — a "good problem to have."

**Latency:** time each step to locate the slow one. Example (research agent): search terms 7s, web search 5s, a step 3s, a step 11s, final essay average 18s. Levers: **parallelize** (e.g. parallel web fetch), swap a slow LLM step for a **smaller model / faster provider** (specialized hardware emits tokens fast).

**Cost:** price each stage; three cost types —
- **LLM steps:** pay per token (e.g. token $0.0004 / $0.009).
- **API tools:** pay per call (e.g. web search $0.016, $0.002).
- **Compute steps:** pay for server capacity (e.g. PDF-to-text $0.03).
**Value:** per-step costs often **clearly tell you which components aren't worth optimizing**; when cost becomes a problem, measure per-step cost/latency first, then choose what to optimize.

---

## 7. Development Process Summary

**Two activities you switch between (non-linear, must be able to answer):**
```
Build side:   build end-to-end system → build evals / compute metrics → improve individual component
Analyze side: examine outputs + read traces → error analysis → component-level evals
```
- **Build (write code to improve) ↔ Analysis (error analysis / build evals to decide what to fix)** — switch back and forth.
- Analysis "doesn't feel like progress" but is **equally important.**
- **Maturity path:** quick & dirty end-to-end → look at outputs + read traces (gut sense) → build an end-to-end eval (10–20 examples) → disciplined error analysis tallying subpar frequency per component → build component-level evals.
- **Common beginner mistake:** only building, little analyzing — ends up spending weeks improving a component that doesn't affect the result.
- Tooling note: there are trace-monitoring / logging / cost tools out there, but workflows are custom, so Andrew still builds lots of custom evals.

**Closing:** implementing even a slice of this already puts you ahead of most developers; M5 covers advanced patterns for highly autonomous agents.

---

## Interview Q&A (M4)

**Q1: How do you evaluate an agent? Where do you start?**
A: Build quick-and-dirty, look at outputs to find a recurring error mode → build an eval (examples + scoring), start with 10–20 and iterate; use the 2×2 to pick a scoring method; shift from "trusting your eyes" to "trusting the metric."

**Q2: Objective eval vs LLM-as-judge — how to choose?**
A: Deterministically checkable (invoice date, copy length) → objective (code); open-ended with many phrasings (talking-point coverage, chart quality) → judge.

**Q3: What is per-example ground truth?**
A: Whether each example has its own correct answer. Has it: invoice date, gold-standard talking points; doesn't: copy length (single threshold), a shared rubric for charts.

**Q4: How do you do error analysis?**
A: Read traces (trace = all intermediate outputs, span = single-step output) → look only at unsatisfactory examples → spreadsheet attribution per component → prioritize by "error frequency × fixability." Note per-component percentages need not sum to 100% (errors aren't exclusive). Examples: research agent 5%/45%; email 75%/30%.

**Q5: Component-level vs end-to-end eval — why the former?**
A: E2E is expensive (one change = full re-run) and noise drowns small improvements; component-level gives a clear signal, lets you tune just that component, and lets teams parallelize. Web search often uses F1-score; still run e2e to confirm.

**Q6: After locating a weak component, what are the improvement levers?**
A: Non-LLM: tune hyperparameters (RAG threshold/chunk size, detection threshold, search result count/date) or swap provider. LLM: improve prompt / few-shot, try a new model, split the step, fine-tune (last resort).

**Q7: How do large vs small models differ in an agent?**
A: Frontier large models are better at instruction following. PII redaction case: Llama 3.1 8B didn't follow the format and missed PII; the frontier model got it right. Providers have different strengths; build intuition by trying many and reading prompts.

**Q8: How do you optimize latency and cost?**
A: Quality first, optimize later (quality>cost>latency). Benchmark per step by timing (7/5/3/11/18s) / pricing (per token, per API call, per compute); levers: parallelize, swap to a smaller/faster model, swap to a cheaper component; the per-step data tells you what's not worth optimizing.

**Q9: What does an efficient development process look like, and what do beginners get wrong?**
A: Build ↔ Analyze, back and forth, non-linear. Maturity path: quick&dirty → read traces → end-to-end eval → disciplined error analysis → component-level eval. Beginners only build and under-analyze, wasting effort on components that don't move the result.

**Q10: Why build a quick-and-dirty prototype first?**
A: It's hard to predict in advance what will/won't work; looking at real outputs directly tells you the error modes, what eval to build, and what to focus evaluation on. The anti-pattern is theorizing for weeks without building.
