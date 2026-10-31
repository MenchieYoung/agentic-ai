"""Self-contained local tests for the Module 3 assignment.

These tests replace the course-platform-only ``dlai_grader`` dependency with
deterministic fake model responses. They exercise tool-call bookkeeping,
reflection JSON handling, and HTML conversion without API keys or network use.
"""

from __future__ import annotations

import argparse
import ast
from contextlib import contextmanager
import json
from pathlib import Path
from types import SimpleNamespace
from typing import Callable, Iterator

_PROMPT = "Radio observations of recurrent novae"
_DUMMY_REPORT = (
    "This is a sufficiently detailed research report about recurrent novae. "
    "It contains claims, context, and references that an academic reviewer can evaluate."
)
_REFLECTION = (
    "Strengths: clear scope. Limitations: limited evidence. Suggestions: add citations. "
    "Opportunities: compare additional observations."
)
_REVISED_REPORT = (
    "This revised report adds clearer evidence, citations, and a structured comparison "
    "of recurrent-nova observations across multiple studies and observing periods."
)
_HTML = "<html><body><h1>Research report</h1><p>Revised content with citations.</p></body></html>"


class _FakeCompletions:
    def __init__(self, messages: list[SimpleNamespace]):
        self._messages = iter(messages)
        self.calls: list[dict] = []

    def create(self, **kwargs):
        self.calls.append(kwargs)
        return SimpleNamespace(choices=[SimpleNamespace(message=next(self._messages))])


class _FakeClient:
    def __init__(self, messages: list[SimpleNamespace]):
        self.chat = SimpleNamespace(completions=_FakeCompletions(messages))


def _message(content: str | None, tool_calls: list | None = None) -> SimpleNamespace:
    return SimpleNamespace(content=content, tool_calls=[] if tool_calls is None else tool_calls)


@contextmanager
def _patched_globals(learner_func: Callable, **replacements) -> Iterator[None]:
    globals_dict = learner_func.__globals__
    sentinel = object()
    previous = {key: globals_dict.get(key, sentinel) for key in replacements}
    globals_dict.update(replacements)
    try:
        yield
    finally:
        for key, value in previous.items():
            if value is sentinel:
                del globals_dict[key]
            else:
                globals_dict[key] = value


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def test_generate_research_report_with_tools(learner_func: Callable) -> None:
    """Verify model arguments and the tool-result message without real tool calls."""
    fake_call = SimpleNamespace(
        id="call-1",
        function=SimpleNamespace(name="arxiv_search_tool", arguments='{"query": "novae"}'),
    )
    client = _FakeClient([
        _message(None, [fake_call]),
        _message(_DUMMY_REPORT),
    ])
    fake_result = [{"title": "A mock paper"}]

    with _patched_globals(
        learner_func,
        CLIENT=client,
        TOOL_MAPPING={"arxiv_search_tool": lambda **_: fake_result},
    ):
        output = learner_func(_PROMPT)

    calls = client.chat.completions.calls
    _require(len(calls) == 2, "the function must continue after a tool call and request a final answer")
    first = calls[0]
    _require(first.get("model") is not None, "model must be passed to the client")
    _require(isinstance(first.get("messages"), list), "messages must be passed to the client")
    _require(isinstance(first.get("tools"), list) and len(first["tools"]) == 2, "both tool definitions must be passed")
    _require(first.get("tool_choice") == "auto", "tool_choice must be 'auto'")

    second_messages = calls[1].get("messages")
    tool_messages = [m for m in second_messages if isinstance(m, dict) and m.get("role") == "tool"]
    _require(len(tool_messages) == 1, "a tool-result message with role='tool' must be appended")
    tool_message = tool_messages[0]
    _require(tool_message.get("tool_call_id") == "call-1", "tool_call_id must match the model request")
    _require(tool_message.get("name") == "arxiv_search_tool", "tool message must include the tool name")
    _require(json.loads(tool_message.get("content", "null")) == fake_result, "tool result must be JSON encoded")
    _require(isinstance(output, str) and len(output) > 50, "the final report must be a non-trivial string")
    print("✓ generate_research_report_with_tools")


def test_reflection_and_rewrite(learner_func: Callable) -> None:
    """Verify structured reflection for both supported input forms."""
    for report in (
        _DUMMY_REPORT,
        [{"role": "assistant", "content": _DUMMY_REPORT}],
    ):
        response_json = json.dumps({"reflection": _REFLECTION, "revised_report": _REVISED_REPORT})
        client = _FakeClient([_message(response_json)])
        with _patched_globals(learner_func, CLIENT=client):
            output = learner_func(report)

        call = client.chat.completions.calls[0]
        messages = call.get("messages")
        _require(call.get("model") is not None, "model must be passed to the client")
        _require(call.get("temperature") is not None, "temperature must be passed to the client")
        _require(isinstance(messages, list) and len(messages) == 2, "system and user messages are required")
        user_prompt = messages[1].get("content") if isinstance(messages[1], dict) else None
        _require(isinstance(user_prompt, str) and _DUMMY_REPORT in user_prompt, "user prompt must include the report")
        _require(isinstance(output, dict), "reflection_and_rewrite must return a dictionary")
        _require(set(output) >= {"reflection", "revised_report"}, "result must include both required keys")
        lower = output["reflection"].lower()
        for heading in ("strengths", "limitations", "suggestions", "opportunities"):
            _require(heading in lower, f"reflection must include {heading}")
        _require(len(output["revised_report"]) > 50, "revised report must be non-trivial")
    print("✓ reflection_and_rewrite")


def test_convert_report_to_html(learner_func: Callable) -> None:
    """Verify HTML conversion for raw text and message-list inputs."""
    for report in (
        _DUMMY_REPORT,
        [{"role": "assistant", "content": _DUMMY_REPORT}],
    ):
        client = _FakeClient([_message(_HTML)])
        with _patched_globals(learner_func, CLIENT=client):
            output = learner_func(report)

        _require(client.chat.completions.calls, "the function must call CLIENT.chat.completions.create")
        call = client.chat.completions.calls[0]
        messages = call.get("messages")
        _require(call.get("model") is not None, "model must be passed to the client")
        _require(call.get("temperature") is not None, "temperature must be passed to the client")
        _require(isinstance(messages, list) and len(messages) == 2, "system and user messages are required")
        user_prompt = messages[1].get("content") if isinstance(messages[1], dict) else None
        _require(isinstance(user_prompt, str) and _DUMMY_REPORT in user_prompt, "user prompt must include the report")
        _require(isinstance(output, str), "convert_report_to_html must return a string")
        lower = output.lower()
        _require(any(tag in lower for tag in ("<html", "<h1", "<p", "</")), "output must look like HTML")
    print("✓ convert_report_to_html")


def _parse_input(value):
    if isinstance(value, list):
        for message in reversed(value):
            if isinstance(message, dict) and message.get("role") == "assistant" and message.get("content"):
                return message["content"]
        raise ValueError("No assistant text found in messages")
    return str(value)


def _load_functions(notebook_path: Path, names: list[str]) -> dict[str, Callable]:
    notebook = json.loads(notebook_path.read_text(encoding="utf-8"))
    research_tools = SimpleNamespace(
        arxiv_tool_def={"type": "function", "function": {"name": "arxiv_search_tool"}},
        tavily_tool_def={"type": "function", "function": {"name": "tavily_search_tool"}},
        parse_input=_parse_input,
    )
    namespace: dict = {"json": json, "research_tools": research_tools}
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
    parser = argparse.ArgumentParser(description="Run deterministic local tests for Module 3")
    parser.add_argument(
        "--notebook",
        type=Path,
        default=Path(__file__).with_name("C1M3_Assignment.ipynb"),
        help="Notebook to test (defaults to C1M3_Assignment.ipynb)",
    )
    args = parser.parse_args()
    notebook_path = args.notebook.resolve()
    if not notebook_path.is_file():
        parser.error(f"notebook not found: {notebook_path}")

    tests = [
        ("generate_research_report_with_tools", test_generate_research_report_with_tools),
        ("reflection_and_rewrite", test_reflection_and_rewrite),
        ("convert_report_to_html", test_convert_report_to_html),
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
