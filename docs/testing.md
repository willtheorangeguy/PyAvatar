# PyAvatar — Testing

```bash
pip install pytest
pytest
```

23 tests, well under a second. `tests/conftest.py` replaces Tkinter with a mock, so nothing opens
a window and no display is required — the suite runs over SSH and in CI unchanged.

## Layout

| File | Covers |
|---|---|
| `test_avatars.py` | Window creation, the title label, account frames, the link handler, the layout globals |
| `test_main_pytest.py` | The same ground in pytest style — window creation, `mainloop`, callables, module structure |
| `test_integration.py` | Imports, function existence, package structure |
| `test_images.py` | That `PyAvatar/images.py` imports and has a docstring |
| `test_links.py` | That `PyAvatar/links.py` imports and has a docstring |
| `conftest.py` | The Tkinter mock and shared fixtures |

Two styles coexist — `unittest.TestCase` classes and bare pytest functions — because the suite
grew in both. Pytest runs both, so it works; new tests should pick the pytest style, which the
rest of the sweep uses.

## The Tkinter mock

`conftest.py` defines a `MockTkinter` with stubbed `pack`, `grid`, and `bind`, and installs it in
`sys.modules` before `main` is imported. Tests can then call `avatars()` without a display and
assert on what was constructed.

This is why the suite is fast and why it runs anywhere. It also means the tests verify the code's
**structure**, not its appearance: a layout that is wrong on screen still passes.

## What the coverage figure means

Coverage sits around 86%, and that number is more flattering than it sounds.
`PyAvatar/images.py` and `PyAvatar/links.py` contain no executable code, so importing them
reports full coverage of nothing. `test_images.py` and `test_links.py` assert only that each
imports and has a docstring.

Those two files are placeholders for data that has not been written yet, so the tests are
placeholders too. Worth knowing before treating 86% as a measure of how well `main.py` is
tested.

## The layout globals

`row_count` and `column_count` live at module level and are never reset, so a test that calls
`avatars()` leaves them where the previous test left them. Ordering effects follow. Anything
added that calls `avatars()` more than once should reset both explicitly.

## Adding tests

- Prefer pytest style.
- Use the `conftest.py` mock rather than constructing real widgets.
- Reset `main.row_count` and `main.column_count` if your test calls `avatars()`.
- When `images.py` and `links.py` gain real content, replace their import-only tests with ones
  that assert on the data.

## CI

`.github/workflows/pytest.yml` runs the suite; `pylint.yml` lints; `codeql-analysis.yml` scans;
`push-to-pypi.yml` publishes. Each has a badge in the README.
