# PyAvatar — FAQ

### Why does it only show two accounts?

Because that is all there is. `main.py` hardcodes GitHub and GitLab as placeholders, and the two
modules meant to hold the real data — `PyAvatar/images.py` and `PyAvatar/links.py` — are empty.

`PLANNING.md` schedules the images for 0.2.0 and the links for 0.3.0. It is unfinished on
purpose.

### Why do both accounts have the same picture?

They share `placeholder.gif`, for the same reason.

### Why GIF and not PNG or JPEG?

Tkinter's `PhotoImage` reads GIF and PNG only. JPEG raises `TclError: couldn't recognize data in
image file`. Converting is easier than adding Pillow, which would be this project's first
dependency.

### `pip install PyAvatar` does not work.

The PyPI name is `python-avatar`. The repository, the window title, and the docs all say
PyAvatar, and `pyproject.toml` says `Python-Avatar` — three names for one package. Recorded in
[`internal/known-issues.md`](./internal/known-issues.md).

### Why must I run it from the repository root?

The placeholder image is loaded from `PyAvatar/images/placeholder.gif`, a path relative to the
working directory rather than to the module. Run from elsewhere and Tkinter cannot find it.

This also breaks the installed `python-avatar` command, which is normally run from wherever you
happen to be. See [`internal/known-issues.md`](./internal/known-issues.md).

### My image loaded but the frame is empty.

Tkinter does not keep a reference to a `PhotoImage`, so one held only by a local variable can be
garbage-collected while still displayed — leaving a blank frame and no error. Assign it to a
module-level name.

### Does it fetch my avatars from those websites?

No. There is no network code at all. It displays local image files and opens links in your
browser; nothing is downloaded and nothing is uploaded.

### Does it need internet access?

Only when you click a link, and then it is your browser doing the work.

### Can I use it as a library?

`main:avatars` is the only entry point and it builds and blocks on a window. It is an
application, not a library.

### Why is coverage 86% when so little is implemented?

Because `images.py` and `links.py` have no executable code, so importing them counts as full
coverage of nothing. See [Testing](./testing.md).

### Is there a Windows executable?

Yes, attached to [releases](https://github.com/willtheorangeguy/PyAvatar/releases/latest), built
with PyInstaller. No Python required.

### Can I add more than five accounts per row?

Change the `if column_count <= 5` test in `main.py`. See [Configuration](./configuration.md).
