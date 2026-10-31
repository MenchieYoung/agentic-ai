# M2 — Reflection Design Pattern (Interview-Oriented Notes)

> Source basis: five local transcript files attributed to Module 2 course videos plus the locally stored lecture PDF.

## Module Overview
**Reflection = having an LLM look back at and improve its own output**, and it's surprisingly simple to implement. The core intuition running throughout: reflection is **not magic and not 100% reliable**; pure self-reflection gives only a **modest** bump; but when you bring in **external feedback (feedback from outside the LLM)**, it becomes **much more powerful** — introduced in section 1, deepened in section 5.

---

## 1. Reflection to Improve Outputs

**Core workflow:** prompt to generate v1 → use the same LLM or **a different one** with a reflection prompt → produce v2. The simplest implementation is just a **hard-coded two-step** process.

**Intuition and examples:**
- **Improving an email (human analogy):** email v1 has three issues — "next month" isn't specific, a typo, and no signature; v2 adds specific dates (5th–7th), fixes the typo, adds the signature. Reflection is the natural "re-read and revise" humans do.
- **Code reflection (can be heterogeneous models):** an LLM writes v1 `do_task()` → an LLM (**which can be a different one, e.g. a reasoning/thinking model, better at finding bugs**) checks it and writes an improved v2.
- **Code reflection with external feedback (the key to the power):** actually **execute** v1 → get a real error like `SyntaxError: unterminated string literal (detected at line 1)` → feed the output + error log back → write a better v2. **The feedback comes from real execution, not the LLM's imagination.**

**Interview point:** minimal implementation = two prompts; external info sets the performance ceiling; reasoning models are good at finding bugs; the cost is it's slower.

---

## 2. Why Not Just Direct Generation

**Definitions:** direct generation = a single prompt that produces the answer in one go = **zero-shot** (0 examples in the prompt). Escalations: **one-shot / two-shot / few-shot** (1 / 2 / several input→output example pairs; "shot" = number of examples). Example: converting a date to MM/DD/YYYY with 0/1/2 examples.

**Empirical support (memorize the citation):** **Self-Refine (Madaan et al., 2023)** — reflection consistently beats direct generation across many tasks: sentiment reversal, dialogue response, code optimization, code readability, math reasoning, acronym generation, constrained generation. In the bar chart, light bars = zero-shot, dark bars = same model + reflection (dark generally higher); different colors = different models. **Caveat: mileage may vary (effect depends on task).**

**Tasks where reflection helps more:**
| Example | Problem | Reflection prompt |
|---|---|---|
| Complex nested JSON / generate an HTML table | Missing `>` | "Validate the HTML / structure" |
| Steps to brew tea | Missing steps | "Check the instructions for coherence and completeness" |
| Generating domain names (AI Fund used this for real) | Hard to pronounce / unintended meaning | "Is it easy to pronounce? Any negative connotations?" |

**Tips for writing reflection prompts (interview-frequent):** ① **clearly indicate the reflection action** ("Review your first draft...") ② **specify clear criteria to check** ③ optionally use **role-play** ("You are an expert data analyst...") ④ have it **write the next draft**. Read good open-source prompts for ideas.

---

## 3. Chart Generation Workflow (multimodal reflection)

**Scenario:** a coding lab using `coffee_sales.csv` (date / price / coffee_name / size): "compare Q1 coffee sales in 2024 vs 2025." The key twist: **let a multimodal LLM "see" its own generated chart** — the chart itself is the external feedback.

**Workflow:**
1. LLM writes Python code (matplotlib + pandas to filter Q1) → v1 code + plot.png (e.g. a hard-to-read stacked bar).
2. Execute v1 code.
3. Feed **v1 code + plot.png + conversation history** to a reflection LLM (role: expert data analyst): Step 1 critique the chart for **readability / clarity / completeness**; Step 2 write improved new code.
4. Execute the new code → plot_v2.png (e.g. separate 2024/2025 regular bars, clearer).

**Configuration flexibility:** the code-generation LLM and the reflection LLM can be different models; a reasoning model for reflection often works better.

---

## 4. Evaluating the Impact of Reflection (interview-frequent)

**Why evaluate:** reflection adds a step and slows things down, so quantify how much it actually helps before shipping. Two kinds:
- **Objective → code-based eval** (easier to manage)
- **Subjective → LLM-as-judge** (needs a tuned rubric)

**Example A — SQL agent (objective, memorize the data):** retail-database Q&A. Flow: LLM generates SQL → reflects to improve v1 → executes → answers. Eval: build a prompt + ground-truth dataset (e.g. "items sold in May 2025" → 1201, "most expensive item" → Airflow sneaker, "styles carried" → 14) and compare:
- **no reflection: 87% correct**
- **with reflection: 95% correct**
- **re-run the whole eval set each time you change the reflection prompt** for quick comparison.

**Example B — which chart is better (subjective):**
- Directly asking an LLM "which chart is better" **works poorly.**
- Known problems with pairwise comparison (interview-frequent): ① sensitive to wording, answers often not good ② disagrees with human experts ③ **position bias (LLM picks the first / A more often).**
- **Better = rubric-based scoring of a single chart:** have the LLM score each item **1 (true) / 0 (false)** and return JSON, e.g. ① has a clear title ② has axis labels ③ appropriate chart type ④ axes use an appropriate numeric range...
- **Key technique: don't have the LLM output a 1–5 score directly (poorly calibrated)**; instead sum multiple binary 0/1 criteria into a score — far more consistent.

**Summary:** objective → code eval, easy to manage; subjective → LLM-as-judge + rubric. Being able to eval is crucial for agentic workflows.

---

## 5. Using External Feedback (the strongest argument in this module)

**Core claim (interview quote):** reflection with external feedback is **far stronger** than using the LLM itself as the only feedback source.

**The performance curve (Andrew's figure — be able to reproduce):** x-axis = time spent on prompt engineering, y-axis = performance.
- Pure zero-shot prompt engineering: rises then **plateaus (diminishing returns).**
- Add reflection: a bump.
- Add external feedback: a higher trajectory.
- **Signal:** when prompt engineering hits diminishing returns, bring in reflection / external feedback.

**Sources of external feedback (worth enumerating):**
| Challenge | Example | Feedback source |
|---|---|---|
| Does the code run | Syntax/runtime error | Execute code, read output / error messages |
| Mentioning competitors | "We're better than RivalCo" | Pattern-match (regex) competitor names; feed back to rewrite |
| Fact-checking an essay | Taj Mahal dates (commissioned 1631 / finished 1648) | Web search results |
| Not following length limits | Essay over word limit | Word count tool |

**The common thread (interview point):** write **deterministic code** that produces **new facts/signals the LLM can't get on its own**, then feed that back to the reflecting LLM. Transition to M3: these "tools" are exactly the next module's tool use.

---

## Interview Q&A (M2)

**Q1: What is reflection? The minimal implementation?**
A: Having an LLM review and improve its own output. Minimal implementation = two prompts (generate v1 → reflect to get v2), can be hard-coded.

**Q2: Why not just use direct generation? Any evidence?**
A: Direct generation = zero-shot, prone to being surface-level/wrong. Self-Refine (Madaan 2023) shows reflection consistently wins across tasks, though mileage may vary.

**Q3: Difference between zero/one/few-shot?**
A: The number of example pairs given in the prompt — 0 / 1 / several.

**Q4: Why does external feedback make reflection stronger? Examples.**
A: Pure self-reflection gives only a modest bump; external feedback provides new facts the LLM can't get itself. Examples: run code and read errors, regex-match competitor names, web-search fact-check, word-count enforcement. The common thread is using deterministic code to produce new signals fed back in.

**Q5: How do you evaluate reflection's impact? Objective vs subjective?**
A: Objective = code-based eval + ground-truth dataset (SQL agent: 87%→95%); subjective = LLM-as-judge, but use a rubric.

**Q6: What are the pitfalls of using an LLM for pairwise comparison, and how do you mitigate them?**
A: Sensitive to wording, disagrees with experts, position bias (prefers the first). Mitigation: score a single chart with a rubric using multiple binary 0/1 criteria summed up — don't ask for a direct 1–5 score.

**Q7: How do you write a good reflection prompt?**
A: Clearly indicate the "review the first draft" action + specify concrete criteria + optionally role-play + have it write the next draft.

**Q8: Should the draft and the reflection use the same model or different ones?**
A: Either works; reflection often uses a reasoning/thinking model, which is better at finding bugs.

**Q9: What's the cost of reflection, and when should you add it?**
A: Slower, more complex, not guaranteed correct. Add reflection / external feedback when prompt engineering hits diminishing returns (the plateau).
