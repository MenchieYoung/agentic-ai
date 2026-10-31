# M3 — Tool Use (Function Calling, Interview-Oriented Notes)

> Source basis: five local transcript files attributed to Module 3 course videos plus the locally stored lecture PDF.

## Module Overview
Tool use (a.k.a. **function calling**) = giving an LLM a set of functions it can **request to be executed**, so it can do what pure text generation can't (query real-time data, compute, look up a database, operate external services). The throughline: what tools are → how to create one (the underlying mechanism) → modern syntax (aisuite + JSON Schema) → code execution (writing code beats a pile of fine-grained tools) → MCP (standardized tool connectivity).

---

## 1. What are Tools

**Core definition (memorize):** **Tools are just code that the LLM can request to be executed.**

**Motivating example:** ask an LLM "what time is it?" and it says "Sorry, I don't have access to the current time." Give it a `get_current_time()` function and it can answer "It's 3:20pm."
```python
from datetime import datetime
def get_current_time():
    """Returns the current time as a string"""
    return datetime.now().strftime("%H:%M:%S")
```

**Key point (interview-frequent):** the **LLM decides on its own when to call a tool.** Ask "how much caffeine is in green tea?" and it won't call `get_current_time` — it just answers. In diagrams, a **dashed box** denotes the LLM autonomously deciding whether to call.

**More examples:**
| Prompt | Tool |
|---|---|
| Italian restaurants near Mountain View | `web_search(...)` |
| $500 at 5% for 10 years | `interest_calc(...)` or `eval("500*(1+0.05)**10")` → $814.45 |
| Customers who bought white sunglasses | `query_database(table="sales", product="sunglasses", color="white")` |

**Multiple tools + multiple turns (calendar agent):** "find a free Thursday slot and book with Alice" → the LLM first calls `check_calendar` to get open times → then `make_appointment` → replies "booked Thursday 3pm." Tool set includes `check_calendar` / `make_appointment` / `delete_appointment`.

---

## 2. Creating a Tool (the underlying mechanism)

**The essence:** tools are code the LLM can request to be executed. **The LLM doesn't call the function directly — it only outputs a "request," and your program executes it.**

**The early hand-written-prompt mechanism (an exam point for understanding function calling):**
The system prompt tells the LLM: "you have a tool `get_current_time`; to use it, return exactly `FUNCTION: get_current_time()`." Then the program checks:
```
if "FUNCTION" in output:        # string matching
    execute the function → feed the result (e.g. 08:00:00) + conversation history back to the LLM → LLM answers "It's 8am"
```
Parameterized version: the system prompt specifies `FUNCTION: get_current_time("timezone")`, the LLM returns `get_current_time("Pacific/Auckland")`, execution gives the New Zealand time.
```python
from datetime import datetime
from zoneinfo import ZoneInfo
def get_current_time(timezone):
    """Returns current time for the given time zone"""
    return datetime.now(ZoneInfo(timezone)).strftime("%H:%M:%S")
```
**Takeaway:** this is a **loop** — "LLM outputs a request → program executes → result fed back → LLM continues" (up to some number of turns).

---

## 3. Tool Syntax (aisuite + JSON Schema)

**The modern approach uses aisuite:** just pass your Python functions into `tools=[...]`; the function's **name and docstring are automatically described to the LLM**:
```python
import aisuite as ai
client = ai.Client()
response = client.chat.completions.create(
    model="openai:gpt-4o",
    messages=messages,
    tools=[get_current_time],
    max_turns=5,     # max back-and-forth rounds
)
```

**Under the hood — the JSON Schema of function calling (interview-frequent, must be able to explain):** these functions are auto-converted to a JSON Schema description fed to the LLM; `name` comes from the function name, `description` from the docstring, `parameters` from the signature:
```json
{ "type": "function",
  "function": {
    "name": "get_current_time",
    "description": "Returns current time for the given timezone.",
    "parameters": {
      "timezone": { "type": "string",
        "description": "The IANA time zone string, e.g., 'America/New_York'." }
    }
  }
}
```
**This is why functions need good docstrings and clear parameter descriptions — the LLM relies on them to decide when and how to call.**

---

## 4. Code Execution (interview-frequent comparison question)

**The pain point (memorize):** building a calculator, if you make a separate tool per operation (add/subtract/multiply/divide), then "square root of 2" needs yet another tool. Andrew's analogy: like adding a button on a scientific calculator for every function — **doesn't scale.**

**The better approach — let the LLM write and execute code:**
System prompt: "Write code to solve the user's query. Return your answer as Python code delimited with `<execute_python>` and `</execute_python>` tags."
The LLM returns `import math; print(math.sqrt(2))` → the program regex-extracts the code → `exec()` runs it → gets `1.4142135623730951` → the LLM answers "approximately 1.4142."

**Combined with reflection via external feedback** (same as M2): execute → get error → reflect → write v2.

**Security (Secure code execution, always mention):** directly `exec()`-ing LLM-generated code is **risky** (Andrew mentions real `rm *.py`-style accidents). Use a **sandbox (e.g. Docker, E2B)** to isolate it and prevent catastrophic errors. Andrew admits many developers don't use a sandbox, but that's not best practice.

---

## 5. MCP (Model Context Protocol)

**Proposed by Anthropic. The problem it solves (interview-frequent, be able to draw/explain):**
- If every app builds its own tools for every service → an **m × n** explosion (m apps × n services, e.g. Slack / Google Drive / GitHub / PostgreSQL).
- MCP lets each app connect to services via a **shared MCP server** → complexity drops to **m + n**.

**The ecosystem:**
- **Clients:** Cursor, Claude Desktop, Windsurf, plus "your app."
- **Servers:** Slack, GitHub, Google Drive, PostgreSQL, etc. — many built by the service providers themselves; you can also write your own.
- **Demo:** Claude Desktop connected to a GitHub MCP server → can get a README, list pull requests, etc.

**One-line memory:** MCP = a **standardized protocol** for tool connectivity, turning the m×n integration problem into m+n.

---

## Interview Q&A (M3)

**Q1: What is tool use / function calling? What's the essence of a tool?**
A: Giving an LLM a set of functions it can request to execute, so it can do what pure generation can't. Essence: **a tool is just code the LLM can request to be executed**; the LLM only outputs a call request, and the program executes it and feeds the result back.

**Q2: How does function calling work under the hood?**
A: Functions are turned into a JSON Schema (name from the function name, description from the docstring, parameters from the signature) described to the LLM; the LLM decides when to call and produces arguments; the program executes and feeds the result back, looping for some number of turns (max_turns). Hence docstrings and parameter descriptions matter.

**Q3: How does the LLM decide which tool to call?**
A: It matches each tool's name/description/parameters (JSON Schema) against the current task and autonomously decides whether and which to call — only when appropriate (it won't call get_current_time for a caffeine question).

**Q4: Why is code execution often better than a pile of fine-grained tools?**
A: Fine-grained tools don't scale — every new need requires a new tool (the calculator-button analogy). Letting the LLM write code lets it call any of the hundreds/thousands of functions in a language/library it's already seen used — far more expressive and extensible.

**Q5: What's risky about executing LLM-generated code, and what do you do?**
A: Risks like deleting files or wrecking the environment (the rm *.py accident). Use a sandbox (Docker / E2B) to isolate execution.

**Q6: What problem does MCP solve, and what's its core value?**
A: Proposed by Anthropic; turns the m×n integration explosion (m apps × n services) into m+n via a shared MCP server. Ecosystem: clients (Cursor/Claude Desktop/Windsurf) and servers (GitHub/Slack/Google Drive/PostgreSQL).

**Q7: What role does aisuite play in tool use?**
A: You pass Python functions directly into `tools=[...]`; it auto-generates the JSON Schema from the function name and docstring and handles the call loop (max_turns), eliminating the boilerplate of hand-writing schemas.
