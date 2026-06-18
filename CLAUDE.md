# CLAUDE.md

## Project Overview

PyAvatar is a cross-platform Python GUI application (Tkinter) for displaying and managing creative avatars across websites. Published on PyPI as `python-avatar`. Current version: 0.2.1 (Alpha).

## Repository Structure

```
main.py              # Primary app: avatars() builds the Tkinter GUI window
__main__.py          # Entry point for `python -m` execution
__init__.py          # Package init, exports avatars()
PyAvatar/
  images.py          # Image link variable storage (stub)
  links.py           # File/website link storage (stub)
  images/            # Avatar image assets (placeholder.gif)
tests/
  conftest.py        # Shared fixtures, MockTkinter for headless testing
  test_avatars.py    # Tests for avatar window creation
  test_images.py     # Tests for image module
  test_integration.py # Integration tests
  test_links.py      # Tests for links module
  test_main_pytest.py # Tests for main module
docs/                # User-facing documentation
.github/
  workflows/         # CI: pytest, pylint, CodeQL, PyPI deploy
  agents/            # GitHub agent configs
```

## Development Commands

```bash
# Install dev dependencies
pip install -r requirements.txt

# Run tests
pytest

# Run tests with coverage
pytest --cov=. --cov-report=term-missing

# Run specific test file
pytest tests/test_avatars.py

# Lint
pylint $(git ls-files '*.py')
```

## Dependencies

- **Runtime:** Python standard library only (tkinter, webbrowser)
- **Dev/Test:** pytest, pytest-cov, pytest-mock
- **Python versions:** 3.9, 3.10, 3.11, 3.12

## CI/CD

- **pytest.yml** — Runs tests on push/PR across Python 3.9–3.12, Ubuntu/Windows/macOS
- **pylint.yml** — Lints on push
- **codeql-analysis.yml** — Security analysis
- **push-to-pypi.yml** — Publishes to PyPI on release

## Code Conventions

- **Indentation:** 4 spaces, no tabs
- **Naming:** snake_case for functions/variables, PascalCase for classes, UPPER_CASE for constants
- **Comments:** Required on functions and significant code blocks
- **Style:** Pylint enforced; Black formatter configured
- **Versioning:** Semantic Versioning (MAJOR.MINOR.PATCH)

## Architecture Notes

- Single Tk window with grid-based layout
- Frame widgets per account; global `row_count`/`column_count` track layout position
- `webbrowser.open_new_tab()` for link handling via Tkinter bind()
- Tests mock all Tkinter components via `MockTkinter` in conftest.py for headless CI

## Test Configuration

Defined in `pytest.ini`:
- Discovery pattern: `tests/test_*.py`
- Markers: `unit`, `integration`, `slow`
- Coverage: enabled by default with term-missing + html + xml reports
- Current coverage: ~86%

## Package Build

```bash
python -m pip install --upgrade pip setuptools wheel
python -m build
```

Entry point command: `python-avatar` (defined in setup.py console_scripts).

## Key Files to Know

| File | Why it matters |
|------|---------------|
| `main.py` | All GUI logic lives here (~76 lines) |
| `tests/conftest.py` | MockTkinter fixture — required for headless test runs |
| `setup.py` / `pyproject.toml` | Package metadata and build config |
| `pytest.ini` | Test runner configuration |
| `requirements.txt` | Dev dependencies |
