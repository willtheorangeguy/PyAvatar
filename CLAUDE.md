# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

**Run the application:**
```bash
python main.py
# or
python -m PyAvatar
# or (if installed)
python-avatar
```

**Run tests:**
```bash
pytest                                          # all tests with coverage
pytest tests/test_avatars.py                   # single file
pytest tests/test_avatars.py::TestAvatarsFunction::test_avatars_window_creation  # single test
pytest -m unit                                 # by marker (unit, integration, slow)
```

**Lint:**
```bash
pylint $(git ls-files '*.py')
```

**Build and publish:**
```bash
pip install build
python -m build
```

Install dev dependencies: `pip install -r requirements.txt`

## Architecture

The project is a Tkinter GUI app with a deliberately minimal structure intended to grow into a full avatar manager.

**Entry points:**
- `main.py` — contains the entire GUI logic in a single `avatars()` function; this is what runs the app
- `__main__.py` — thin wrapper calling `avatars()` to support `python -m PyAvatar`
- `__init__.py` — re-exports `avatars` from `main` for package-level import

**PyAvatar/ subpackage** — currently stub files reserved for future data:
- `images.py` — intended to hold image path/URL variables per account
- `links.py` — intended to hold website URL variables per account
- `images/placeholder.gif` — the only actual asset; loaded at runtime via relative path `"PyAvatar/images/placeholder.gif"`

**GUI layout:** Uses Tkinter grid. Global variables `row_count` and `column_count` in `main.py` track current grid position. The inner `accounts()` function increments these globals to place each account frame into columns 1–5 per row, then wraps to the next row.

**Adding a new account** requires calling `accounts(image, name, url)` inside `avatars()`. Until `images.py` and `links.py` are populated, the `PLACEHOLDER` PhotoImage is used for every entry.

## Testing

Tests run headlessly — `conftest.py` injects a `MockTkinter` class into `sys.modules["tkinter"]` before any imports, replacing all Tk widgets with no-op mocks. This means:
- Tests do not open a display or window
- `window.mainloop()` is a no-op in test runs
- PhotoImage loading does not touch the filesystem

All test files include `# pylint: skip-file` at the top. `main.py` suppresses `invalid-name`, `import-error`, and `global-statement` pylint rules via a module-level disable comment.

Code style is enforced by pylint and formatted by Black (configured in `.deepsource.toml`). Indentation is 4 spaces.

## Project Status

This is an early alpha (v0.2.1). The `PyAvatar/images.py` and `PyAvatar/links.py` modules are empty stubs — accounts are currently hardcoded in `main.py` with placeholder images. The roadmap in `PLANNING.md` targets populating images (v0.2.0), links (v0.3.0), and a final release (v1.0.0).
