# PyAvatar — Troubleshooting

## `TclError: couldn't open "PyAvatar/images/placeholder.gif"`

The most common failure. The path is relative to the **working directory**, not to the module, so
the application only starts from the repository root.

```bash
cd /path/to/PyAvatar
python main.py
```

The installed `python-avatar` command hits this for the same reason, and there is no working
directory it can reasonably assume. Run from source until it is fixed — see
[`internal/known-issues.md`](./internal/known-issues.md).

## `TclError: couldn't recognize data in image file`

The image is not a GIF or a PNG. Tkinter's `PhotoImage` reads nothing else without Pillow.
Convert it.

## The window opens with empty frames

The image was loaded and then garbage-collected. Tkinter holds no reference of its own, so a
`PhotoImage` assigned to a local variable can vanish while still on screen — no error, just a
blank frame.

Assign it to a module-level name, as `PLACEHOLDER` is.

## `ModuleNotFoundError: No module named 'tkinter'`

Tkinter is bundled with Python on Windows and macOS but packaged separately on many Linux
distributions:

```bash
sudo apt install python3-tk        # Debian, Ubuntu
sudo dnf install python3-tkinter   # Fedora
```

## `pip install PyAvatar` says no matching distribution

The PyPI name is `python-avatar`:

```bash
pip install python-avatar
```

## The window shows only two accounts

That is all there is — see [FAQ](./faq.md). Add your own in `main.py`, per
[Configuration](./configuration.md).

## Accounts appear far down the window, or in odd positions

`row_count` and `column_count` are module-level globals that are never reset. Calling `avatars()`
twice in one process continues the numbering from where the first call finished. Reset both
before calling again.

## Nothing happens when I click a link

`link()` calls `webbrowser.open_new`, which needs a browser it can find. On a headless or minimal
Linux install there may be none; check `python -c "import webbrowser; webbrowser.open('https://example.com')"`.

## The window will not close

`window.mainloop()` blocks until the window is closed. If it is unresponsive, the process is
likely wedged elsewhere — Ctrl+C in the terminal that launched it.

## `pytest` collects nothing

Run it from the repository root. The tests add the `PyAvatar` directory to `sys.path` relative to
their own location, so they work from there.

## Tests pass but the app is broken

Expected, and worth understanding: `conftest.py` mocks Tkinter entirely, so the suite checks the
code's structure rather than what appears on screen. A layout that is wrong visually still
passes. See [Testing](./testing.md).

## Still stuck

[Open an issue](https://github.com/willtheorangeguy/PyAvatar/issues/new/choose), or ask on the
[Discord](https://discord.gg/Cjwt8DRfr3). Include your OS, Python version, and the working
directory you launched from — that last one explains most reports.
