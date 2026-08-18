# PyAvatar — Architecture

One file does the work. Two more are placeholders for the data it will eventually read.

```
main.py
 └── avatars()
      ├── Tk() window, title label
      ├── PLACEHOLDER = PhotoImage(...)
      ├── link(url)              → webbrowser.open_new
      ├── accounts(img, name, url) → one Frame, gridded
      └── window.mainloop()
```

## `avatars()`

The entry point, and the whole application. It builds the window, defines two nested helpers,
calls `accounts()` once per account, and enters the Tkinter main loop.

Being a single function is why the account list has to be edited inline: there is no data
structure to add to, only more calls.

## `accounts(image, name, hyperlink)`

Builds one frame:

| Widget | Placement |
|---|---|
| `Label(image=...)` | `pack(side=TOP)` |
| `Label(text=name)` | `pack(side=BOTTOM)` |
| `Label(text=hyperlink, fg="blue", cursor="hand2")` | `pack(side=BOTTOM)` |

The link label binds `<Button-1>` to `link(hyperlink)`, which is what makes plain text behave
like a hyperlink — Tkinter has no link widget, so a label plus a cursor plus a click binding is
the idiom.

Note the two layout managers in play: `pack` **inside** each frame, `grid` for the frames
**within** the window. Mixing them in one container hangs Tkinter; keeping them in separate
containers, as here, is correct and deliberate.

## The layout counters

```python
row_count = 2
column_count = 1

def accounts(...):
    global row_count
    global column_count
    if column_count <= 5:
        account.grid(row=row_count, column=column_count, ...)
        column_count += 1
    else:
        row_count += 1
        column_count = 1
        account.grid(row=row_count, column=column_count, ...)
```

Module-level globals, mutated on every call. `row_count` starts at 2 because row 1 holds the
title.

The consequence worth knowing: **they are never reset**. Calling `avatars()` a second time in one
process continues numbering from wherever the first call stopped, so a second window's accounts
appear far down an otherwise empty grid. It never bites in normal use — the function is called
once and blocks in `mainloop` — but it does bite the tests, which is why `tests/conftest.py`
exists.

## `link(url)`

`webbrowser.open_new(url)`. No allowlist and no validation, which is fine while every URL is a
literal in the source, and worth revisiting if links ever come from a file.

## `images.py` and `links.py`

Both are docstring and comment only:

```python
"""PyAvatar - sort and display avatars by website."""
# Holds image link variables for each avatar
```

They are the intended home for the account data, and the reason `MANIFEST.in` packages them. Until
they are filled in, they are empty modules that the test suite imports and asserts have
docstrings. See [Testing](./testing.md) and
[`internal/known-issues.md`](./internal/known-issues.md).

## The placeholder image

```python
PLACEHOLDER = PhotoImage(file="PyAvatar/images/placeholder.gif")
```

GIF, because Tkinter's `PhotoImage` reads GIF and PNG and nothing else without Pillow.

The path is relative to the **working directory**, not the module, so the application only runs
from the repository root — including when installed as the `python-avatar` console script. That
is the most consequential defect here; see
[`internal/known-issues.md`](./internal/known-issues.md).

## Packaging

Three descriptions of the same package coexist: `setup.py`, `setup.cfg`, and `pyproject.toml`.
They do not agree on the name. See [Development](./development.md).
