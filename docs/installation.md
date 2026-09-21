# PyAvatar — Installation

## Requirements

| | |
|---|---|
| Python | 3.x with Tkinter |
| Dependencies | None — standard library only |

Tkinter ships with Python on Windows and macOS. On Debian and Ubuntu it is a separate package:

```bash
sudo apt install python3-tk
```

## From source

```bash
git clone https://github.com/willtheorangeguy/PyAvatar
cd PyAvatar
python main.py
```

**Stay in the repository root.** The placeholder image is loaded as
`PyAvatar/images/placeholder.gif` — relative to the working directory, not to the module — so
`python /path/to/PyAvatar/main.py` from elsewhere raises a `TclError` about a missing file.

## From PyPI

```bash
pip install python-avatar
python-avatar
```

Two things to know before you rely on this.

**The name.** The project is `python-avatar` on PyPI even though the repository, the window, and
the documentation all say PyAvatar. `pyproject.toml` gives a third spelling, `Python-Avatar`. See
[`internal/known-issues.md`](./internal/known-issues.md).

**The console script has the same path problem**, and it bites harder here — an installed command
is run from wherever you happen to be, which is almost never a checkout of this repository. In
practice, run from source until that is fixed.

## As an executable

Prebuilt Windows launchers are attached to
[releases](https://github.com/willtheorangeguy/PyAvatar/releases/latest), built with PyInstaller.
No Python needed.

## Verify

```bash
python main.py
```

A window with two accounts and a placeholder image in each. If the window appears with empty
frames, see [Troubleshooting](./troubleshooting.md) — that is the Tkinter image-reference
problem, not a missing file.

## Run the tests

```bash
pip install pytest
pytest
```

23 tests, in well under a second. `tests/conftest.py` mocks Tkinter, so no display is needed —
they run fine over SSH and in CI. See [Testing](./testing.md).
