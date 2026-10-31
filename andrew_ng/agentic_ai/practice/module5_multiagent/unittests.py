"""Self-contained local tests for the Module 5 assignment.

The tests use deterministic fake LLM responses, so they require neither API
keys nor network access. They can be called from notebook cells or run against
a notebook from the command line.
"""

from __future__ import annotations

import argparse
import ast
from contextlib import contextmanager
from datetime import datetime
import json
from pathlib import Path
from types import SimpleNamespace
from typing import Callable, Iterator

_TOPIC = "The ensemble Kalman filter for time series forecasting"
_RESEARCH_TASK = "Find three key references and summarize them briefly."
_WRITE_TASK = "Draft a concise summary explaining the core idea and typical applications."
_EDIT_TASK = "Reflect on the draft and improve its structure, clarity, and citations."
_LONG_RESPONSE = (
    "This deterministic response is long enough to represent a useful research or writing "
    "result while ensuring that local assignment tests never call an external model API."
)


class _FakeCompletions:
    def __init__(self, responses: list[str]):
        self._responses = iter(responses)
        self.calls: list[dict] = []

    def create(self, **kwargs):
        self.calls.append(kwargs)
        content = next(self._responses)
        message = SimpleNamespace(content=content, tool_calls=[])
        return SimpleNamespace(choices=[SimpleNamespace(message=message)])


class _FakeClient:
    def __init__(self, responses: list[str]):
        self.chat = SimpleNamespace(completions=_FakeCompletions(responses))


@contextmanager
def _patched_client(learner_func: Callable, responses: list[str]) -> Iterator[_FakeClient]:
    globals_dict = learner_func.__globals__
    sentinel = object()
    previous = globals_dict.get("CLIENT", sentinel)
    client = _FakeClient(responses)
    globals_dict["CLIENT"] = client
    try:
        yield client
    finally:
        if previous is sentinel:
            del globals_dict["CLIENT"]
        else:
            globals_dict["CLIENT"] = previous


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def _validate_messages(messages, task: str) -> None:
    _require(isinstance(messages, list) and len(messages) >= 1, "messages must be a non-empty list")
    roles = [message.get("role") for message in messages if isinstance(message, dict)]
    _require(all(role in {"system", "user", "assistant"} for role in roles), "every message must have a valid role")
    contents = [message.get("content") for message in messages if isinstance(message, dict)]
    _require(all(isinstance(content, str) and content.strip() for content in contents), "message content must be non-empty text")
    _require(any(task in content for content in contents), "messages must include the assigned task")


def test_planner_agent(learner_func: Callable) -> None:
    """Verify that the planner calls the model and parses a useful plan."""
    plan_text = repr([
        "Research foundational papers",
        "Draft a concise technical explanation",
        "Edit and generate the final Markdown report",
    ])
    with _patched_client(learner_func, [plan_text]) as client:
        output = learner_func(_TOPIC)

    _require(client.chat.completions.calls, "planner_agent must call CLIENT.chat.completions.create")
    call = client.chat.completions.calls[0]
    _require(call.get("model") is not None, "model must be passed to the client")
    _validate_messages(call.get("messages"), _TOPIC)
    _require(isinstance(output, list) and len(output) >= 3, "plan must contain at least three steps")
    _require(all(isinstance(step, str) for step in output), "every plan step must be a string")
    _require(any(word in output[-1].lower() for word in ("markdown", "md")), "final step must mention Markdown")
    print("✓ planner_agent")


def test_research_agent(learner_func: Callable) -> None:
    """Verify tool configuration and both documented return modes."""
    with _patched_client(learner_func, [_LONG_RESPONSE, _LONG_RESPONSE]) as client:
        text_output = learner_func(_RESEARCH_TASK)
        tuple_output = learner_func(_RESEARCH_TASK, return_messages=True)

    _require(isinstance(text_output, str) and len(text_output) > 50, "default result must be a non-trivial string")
    _require(
        isinstance(tuple_output, tuple)
        and len(tuple_output) == 2
        and isinstance(tuple_output[0], str)
        and isinstance(tuple_output[1], list),
        "return_messages=True must return (text, messages)",
    )
    _require(len(client.chat.completions.calls) == 2, "each research request must call the model once")
    for call in client.chat.completions.calls:
        _require(call.get("model") is not None, "model must be passed to the client")
        _validate_messages(call.get("messages"), _RESEARCH_TASK)
        _require(isinstance(call.get("tools"), list) and len(call["tools"]) == 3, "all three research tools must be passed")
        _require(call.get("tool_choice") == "auto", "tool_choice must be 'auto'")
        _require(call.get("max_turns") == 6, "max_turns must be 6")
        prompt = call["messages"][0]["content"]
        _require(str(datetime.now().year) in prompt, "research prompt must include the current date")
    print("✓ research_agent")


def _test_writing_agent(learner_func: Callable, task: str, label: str) -> None:
    with _patched_client(learner_func, [_LONG_RESPONSE]) as client:
        output = learner_func(task)

    _require(client.chat.completions.calls, f"{label} must call CLIENT.chat.completions.create")
    call = client.chat.completions.calls[0]
    _require(call.get("model") is not None, "model must be passed to the client")
    messages = call.get("messages")
    _require(isinstance(messages, list) and len(messages) == 2, "system and user messages are required")
    _require(messages[0].get("role") == "system", "first message must be the system role")
    _require(messages[1].get("role") == "user", "second message must be the user role")
    _validate_messages(messages, task)
    _require(isinstance(output, str) and len(output) > 50, f"{label} must return non-trivial text")
    print(f"✓ {label}")


def test_writer_agent(learner_func: Callable) -> None:
    _test_writing_agent(learner_func, _WRITE_TASK, "writer_agent")


def test_editor_agent(learner_func: Callable) -> None:
    _test_writing_agent(learner_func, _EDIT_TASK, "editor_agent")


def _dummy_tool(*_args, **_kwargs):
    return [{"title": "Mock result"}]


def _load_functions(notebook_path: Path, names: list[str]) -> dict[str, Callable]:
    notebook = json.loads(notebook_path.read_text(encoding="utf-8"))
    research_tools = SimpleNamespace(
        arxiv_search_tool=_dummy_tool,
        tavily_search_tool=_dummy_tool,
        wikipedia_search_tool=_dummy_tool,
    )
    namespace: dict = {
        "ast": ast,
        "datetime": datetime,
        "json": json,
        "research_tools": research_tools,
    }
    found: dict[str, Callable] = {}

    for cell in notebook.get("cells", []):
        if cell.get("cell_type") != "code":
            continue
        source = "".join(cell.get("source", []))
        try:
            tree = ast.parse(source)
        except SyntaxError:
            continue
        for node in tree.body:
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name in names:
                module = ast.Module(body=[node], type_ignores=[])
                ast.fix_missing_locations(module)
                exec(compile(module, str(notebook_path), "exec"), namespace)
                found[node.name] = namespace[node.name]

    missing = sorted(set(names) - set(found))
    if missing:
        raise RuntimeError(f"Could not find graded functions: {', '.join(missing)}")
    return found


def main() -> int:
    parser = argparse.ArgumentParser(description="Run deterministic local tests for Module 5")
    parser.add_argument(
        "--notebook",
        type=Path,
        default=Path(__file__).with_name("C1M5_Assignment.ipynb"),
        help="Notebook to test (defaults to C1M5_Assignment.ipynb)",
    )
    args = parser.parse_args()
    notebook_path = args.notebook.resolve()
    if not notebook_path.is_file():
        parser.error(f"notebook not found: {notebook_path}")

    tests = [
        ("planner_agent", test_planner_agent),
        ("research_agent", test_research_agent),
        ("writer_agent", test_writer_agent),
        ("editor_agent", test_editor_agent),
    ]
    functions = _load_functions(notebook_path, [name for name, _ in tests])
    failures = 0
    for name, test in tests:
        try:
            test(functions[name])
        except Exception as exc:
            failures += 1
            print(f"✗ {name}: {exc}")

    if failures:
        print(f"\n{failures} of {len(tests)} local tests failed.")
        return 1
    print(f"\nAll {len(tests)} local tests passed. No API or network calls were made.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
