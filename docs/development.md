# PyAvatar — Development

## Setup

```bash
git clone https://github.com/willtheorangeguy/PyAvatar
cd PyAvatar
pip install -r requirements.txt
python main.py
```

No runtime dependencies — Tkinter is standard library. `requirements.txt` covers the development
tools.

## Commands

```bash
python main.py     # run
pytest             # 23 tests, headless, sub-second
pylint main.py     # what CI lints with
```

Always run from the repository root; the placeholder image path depends on it.

## The packaging situation

Three descriptions of the same package coexist, and they disagree:

| File | Declares |
|---|---|
| `setup.py` | `name="python-avatar"` |
| `setup.cfg` | `name = python-avatar` |
| `pyproject.toml` | `name = "Python-Avatar"` |

The old README linked to a fourth spelling, `pypi.org/project/PyAvatar/`.

Which one wins depends on which the build backend reads, which is not something to leave to
chance for a published package. Recorded in
[`internal/known-issues.md`](./internal/known-issues.md); consolidating on `pyproject.toml` is
the modern answer.

The console entry point is `python-avatar = main:avatars`, declared in both `setup.py` and
`setup.cfg`.

`MANIFEST.in` packages `PyAvatar/images.py`, `PyAvatar/links.py`, and `PyAvatar/images/*` — so
the placeholder GIF does ship. The problem is that the code cannot find it once installed; see
[Architecture](./architecture.md).

## Code style

- **Pylint**, with per-file disables at the top of each module
  (`invalid-name`, `import-error`, `global-statement`).
- **Module docstring plus copyright header** on every file.
- `global-statement` is disabled because the layout counters are globals. If those ever become
  proper state, drop the disable rather than keeping it out of habit.

## Working on the account list

The eventual design is for `PyAvatar/images.py` and `PyAvatar/links.py` to hold the data, with
`main.py` reading from them — that is why they exist, why `MANIFEST.in` packages them, and why
they have tests. Both are currently empty.

Anything that fills them in should also give the two import-only tests something real to assert.

## Building an executable

PyInstaller, per the credits and the release artifacts. The image path is the thing to check in
a frozen build — a one-file bundle unpacks to a temporary directory, so a working-directory
relative path will not find the GIF there either.

## CI

| Workflow | Does |
|---|---|
| `pytest.yml` | Runs the suite |
| `pylint.yml` | Lints |
| `codeql-analysis.yml` | Security scan |
| `push-to-pypi.yml` | Publishes |

## Recording defects

Bugs found while working here go in [`internal/known-issues.md`](./internal/known-issues.md)
rather than being fixed in passing, unless fixing them is the job you are on.
