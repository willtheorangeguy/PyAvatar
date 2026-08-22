# Known Issues — PyAvatar

Concrete defects and gaps found while writing this repository's documentation in
August 2026. **Nothing here was changed** — each one needs a code, configuration, or
licensing decision rather than a documentation one.

Ordered by severity. See [`docs/roadmap.md`](../roadmap.md) for the narrative version,
which also covers deliberate non-goals.

**5 open:** 1 high, 2 medium, 2 low.

## 1. The placeholder image path is relative to the working directory, so the installed command cannot start

**Severity:** High
**Where:** `main.py` -> `PLACEHOLDER = PhotoImage(file="PyAvatar/images/placeholder.gif")`

**What:** The path is resolved against the process's current working directory rather than against the module's location. `MANIFEST.in` does package `PyAvatar/images/*`, so the GIF ships correctly -- the file is present, and the code still cannot find it. `setup.py` and `setup.cfg` both declare the console script `python-avatar = main:avatars`.

**Why it matters:** An installed command is run from wherever the user happens to be, which is essentially never a checkout of this repository -- so `python-avatar` raises `TclError: couldn't open "PyAvatar/images/placeholder.gif"` and exits before the window appears. The package is published to PyPI, so this is the first thing every pip user encounters, and the error names a path that plainly exists inside the installed package, which points them at the wrong thing entirely. A PyInstaller one-file build has the same problem for the same reason: it unpacks to a temporary directory that is not the working directory.

**Suggested fix:** Resolve against the module: `Path(__file__).parent / "PyAvatar" / "images" / "placeholder.gif"`, or `importlib.resources.files("PyAvatar") / "images" / "placeholder.gif"` for the installed case. For a frozen build, fall back to `sys._MEIPASS` when it is set.

## 2. Three packaging files declare three different project names

**Severity:** Medium
**Where:** `setup.py`, `setup.cfg`, `pyproject.toml`

**What:** `setup.py` has `name="python-avatar"`, `setup.cfg` has `name = python-avatar`, and `pyproject.toml` has `name = "Python-Avatar"`. The repository, the window title, and the documentation all say PyAvatar, and the README previously linked to a fourth spelling, `pypi.org/project/PyAvatar/`. All three packaging files describe the same distribution, and which one is authoritative depends on which the build backend reads.

**Why it matters:** For a package published to PyPI by a workflow, the installed name is decided by whichever file wins -- a detail that can change with a setuptools upgrade rather than with a commit. Users are separately affected: `pip install PyAvatar` fails, and nothing in the project told them the real name. Having three overlapping build descriptions also means an edit to the obvious one can have no effect, which is a bad way to spend an afternoon.

**Suggested fix:** Consolidate on `pyproject.toml`, delete `setup.py` and `setup.cfg`, and pick one name. If the PyPI name must stay `python-avatar`, say so in the README rather than leaving it to be discovered.

## 3. README images used /blob/ URLs, so the logo and screenshot rendered as nothing

**Severity:** Medium
**Where:** `README.md` (fixed in this pass)

**What:** The logo and screenshot were referenced as `https://github.com/willtheorangeguy/PyAvatar/blob/main/docs/images/logo.png`. The `/blob/` path serves GitHub's HTML viewer, not the image bytes, so an `<img src>` pointing at it renders as a broken image. The README also linked to itself with URLs missing the `/blob/` segment entirely -- `https://github.com/willtheorangeguy/PyAvatar/main/README.md#git` -- which 404.

**Why it matters:** The logo and the screenshot are the first two things a visitor sees, and both were blank. This is not a rendering quirk of one viewer: `/blob/` returns HTML to every client, so the images were broken on github.com, on PyPI, and anywhere else the README is shown. Recorded here because the same mistake appears in several repositories in this org and is worth checking for as a class.

**Suggested fix:** Already corrected in this pass: the images now come from `raw.githubusercontent.com/willtheorangeguy/.github/main/icons/PyAvatar/`, and the self-referential links were replaced with relative paths. Note this depends on the `.github` repository staying public.

## 4. images.py and links.py are empty, and their tests assert only that they import

**Severity:** Low
**Where:** `PyAvatar/images.py`, `PyAvatar/links.py`, `tests/test_images.py`, `tests/test_links.py`

**What:** Both modules contain a docstring, a pylint disable, and a one-line comment -- no code. `test_images.py` and `test_links.py` assert that each imports successfully and that its docstring mentions one of 'link', 'website', or 'avatar'. `MANIFEST.in` packages both. `docs/TESTING.md` reported 86% coverage across the project.

**Why it matters:** The coverage figure is measuring nothing: a module with no executable statements is fully covered by importing it, so two of the five test files inflate a number that is meant to say how well `main.py` is exercised. The emptiness itself is expected -- `PLANNING.md` schedules the content for 0.2.0 and 0.3.0 -- but a passing test named `test_links` reads as though links are tested.

**Suggested fix:** Leave the modules; they are placeholders by design. Replace the two import-only tests with real assertions when the data lands, and until then either exclude the empty modules from coverage or stop quoting a project-wide percentage.

## 5. The layout counters are module-level globals that are never reset

**Severity:** Low
**Where:** `main.py` -> `row_count`, `column_count`, `accounts`

**What:** `row_count = 2` and `column_count = 1` are defined at module scope and mutated through `global` statements inside `accounts()`. Nothing resets them -- not `avatars()`, and not the end of a window's lifetime.

**Why it matters:** Calling `avatars()` a second time in one process continues numbering from wherever the previous call stopped, so a second window's accounts appear far down an otherwise empty grid. It does not bite in normal use, because the function is called once and blocks in `mainloop()`. It does affect the tests, where ordering between cases that call `avatars()` becomes significant in a way nothing declares, and it will bite the moment the account list becomes reloadable.

**Suggested fix:** Make them local to `avatars()` and pass the position through, or reset both at the top of `avatars()`. Either removes the need for the `global-statement` pylint disable at the top of the file.

---

## Also, across every repository

**`.bandit` is present on disk but untracked in git.** Verified in PyWorkout, treklogger,
skyscanner-cli, booking-cli, piggy, and aibot — the config file exists locally in each but
`git ls-files` does not know about it, so none of it reached GitHub.

The August 2026 security sweep therefore looks complete locally and landed nowhere. Worth
checking across all 44 repositories it covered.
