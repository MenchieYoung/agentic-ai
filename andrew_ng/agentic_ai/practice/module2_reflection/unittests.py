"""Self-contained local tests for the Module 2 assignment.

The notebook imports this module and passes each completed function to the
matching ``test_*`` helper. The command-line runner can also extract the graded
functions from a notebook and test them without API keys or network calls.
"""

from __future__ import annotations

import argparse
import ast
from contextlib import contextmanager
import json
from pathlib import Path
from types import SimpleNamespace
from typing import Callable, Iterator

_DRAFT_IN = "How external feedback improves reflection"
_DRAFT_TEXT = "A" * 120
_FEEDBACK = "Improve the structure, clarity, supporting evidence, and conclusion."
_LONG_RESPONSE = (
    "This deterministic mock response is intentionally longer than one hundred "
    "characters so the local test can verify the assignment's return contract "
    "without making a paid language-model request."
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


def _request_prompt(client: _FakeClient) -> str | None:
    call = client.chat.completions.calls[0]
    messages = call.get("messages")
    if not isinstance(messages, list) or not messages:
        return None
    first = messages[0]
    return first.get("content") if isinstance(first, dict) else None


def test_generate_draft(learner_func: Callable) -> None:
    """Verify the prompt and return contract without calling an LLM."""
    _require(callable(learner_func), "generate_draft must be callable")
    with _patched_client(learner_func, [_LONG_RESPONSE]) as client:
        output = learner_func(_DRAFT_IN)

    prompt = _request_prompt(client)
    _require(isinstance(prompt, str) and prompt.strip(), "prompt must be a non-empty string")
    _require(_DRAFT_IN in prompt, "prompt must include the requested topic")
    _require(isinstance(output, str), "generate_draft must return a string")
    _require(len(output) > 100, "generate_draft must return more than 100 characters")
    print("✓ generate_draft")


def test_reflect_on_draft(learner_func: Callable) -> None:
    """Verify that reflection sends the original draft to the model."""
    _require(callable(learner_func), "reflect_on_draft must be callable")
    with _patched_client(learner_func, [_LONG_RESPONSE]) as client:
        output = learner_func(_DRAFT_TEXT)

    prompt = _request_prompt(client)
    _require(isinstance(prompt, str) and prompt.strip(), "prompt must be a non-empty string")
    _require(_DRAFT_TEXT in prompt, "reflection prompt must include the draft")
    _require(isinstance(output, str), "reflect_on_draft must return a string")
    print("✓ reflect_on_draft")


def test_revise_draft(learner_func: Callable) -> None:
    """Verify that revision uses both the draft and its feedback."""
    _require(callable(learner_func), "revise_draft must be callable")
    with _patched_client(learner_func, [_LONG_RESPONSE]) as client:
        output = learner_func(_DRAFT_TEXT, _FEEDBACK)

    _require(client.chat.completions.calls, "revise_draft must call CLIENT.chat.completions.create")
    prompt = _request_prompt(client)
    _require(isinstance(prompt, str) and prompt.strip(), "prompt must be a non-empty string")
    _require(_DRAFT_TEXT in prompt, "revision prompt must include the original draft")
    _require(_FEEDBACK in prompt, "revision prompt must include the reflection feedback")
    _require(isinstance(output, str), "revise_draft must return a string")
    _require(len(output) > 100, "revise_draft must return more than 100 characters")
    print("✓ revise_draft")


def _load_functions(notebook_path: Path, names: list[str]) -> dict[str, Callable]:
    notebook = json.loads(notebook_path.read_text(encoding="utf-8"))
    namespace: dict = {}
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
    parser = argparse.ArgumentParser(description="Run deterministic local tests for Module 2")
    parser.add_argument(
        "--notebook",
        type=Path,
        default=Path(__file__).with_name("C1M2_Assignment.ipynb"),
        help="Notebook to test (defaults to C1M2_Assignment.ipynb)",
    )
    args = parser.parse_args()
    notebook_path = args.notebook.resolve()
    if not notebook_path.is_file():
        parser.error(f"notebook not found: {notebook_path}")

    tests = [
        ("generate_draft", test_generate_draft),
        ("reflect_on_draft", test_reflect_on_draft),
        ("revise_draft", test_revise_draft),
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
    print(f"\nAll {len(tests)} local tests passed. No API calls were made.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
