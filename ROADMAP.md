# Roadmap

This roadmap tracks where Worlds-Smallest-Calc is today and where it is heading next. It is aimed at contributors and curious users who want a single place to see the project's direction.

## Vision

Keep the calculator honest: one line of Python that evaluates any expression, easy to paste into a terminal and easy to read. Everything added should make that core experience sturdier or more reachable, never longer for its own sake.

## Current state

- `Calc.py` is a one-line REPL: `while 1:print(eval(input()))`.
- Documentation is available in six languages: English, Chinese, Spanish, Russian, Japanese and Korean.
- The project is MIT licensed and distributed through a GitHub repository.
- There are no automated tests and no packaging metadata.

## Near term

Harden the core and make it easier to run.

- Add an exit path so users can leave the REPL without `Ctrl+C` (for example, an empty line or a `quit` command) while keeping the one-line spirit.
- Catch common input errors (syntax errors, division by zero, name errors) and print a short message instead of a Python traceback.
- Provide a minimal test script that exercises arithmetic, the exit path and the error handling.

## Mid term

Distribute the calculator more widely and document it more thoroughly.

- Add a `pyproject.toml` so the project can be installed with `pip` and published to PyPI.
- Add a `CONTRIBUTING.md` describing how to run the tests and how to add a new README translation.
- Add a GitHub Actions workflow that runs the tests on every push and pull request.
- Audit the six existing READMEs for translation parity and fix any drift between them.

## Long term

Grow the community and explore options without bloating the core.

- Optional companion files (a wrapper with the safety improvements, a GUI frontend) kept in separate files so `Calc.py` stays one line.
- A gallery of community-contributed one-liner calculators in other languages (JavaScript, Lua, Ruby) with links from the README.
- Periodic review of the roadmap: drop items that did not pull their weight and promote community requests.

## How to read this roadmap

- Items are not promised delivery dates; they are ordered by priority.
- Anything that changes the one-line core is treated as a breaking change and called out in the changelog.
- Suggestions belong on the issue tracker, not here. This file describes direction, not every idea.
