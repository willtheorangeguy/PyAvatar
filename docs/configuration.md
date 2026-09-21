# PyAvatar — Configuration

There is no configuration file, no settings dialog, and no command-line option. Customising
PyAvatar means editing `main.py`.

That is not the intended design — `PyAvatar/images.py` and `PyAvatar/links.py` exist to hold
image references and links respectively, and are **both empty**. Until they are filled in, the
account list lives inline.

## Adding an account

At the bottom of `avatars()`:

```python
accounts(PLACEHOLDER, "GitHub", "https://github.com")
accounts(PLACEHOLDER, "GitLab", "https://gitlab.com")
accounts(PLACEHOLDER, "Mastodon", "https://mastodon.social/@you")
```

`accounts(image, name, hyperlink)` takes:

| Argument | What |
|---|---|
| `image` | A `PhotoImage`, already constructed |
| `name` | The label under the image |
| `hyperlink` | Shown in blue and opened on click |

## Adding your own images

```python
MASTODON = PhotoImage(file="PyAvatar/images/mastodon.gif")
accounts(MASTODON, "Mastodon", "https://mastodon.social/@you")
```

Two constraints, both Tkinter's rather than this project's:

**Format.** `PhotoImage` reads **GIF and PNG only**. A JPEG raises `TclError: couldn't recognize
data in image file`. Convert first, or bring in Pillow — which would be this project's first
dependency.

**Lifetime.** Tkinter does not keep a reference to an image, so one held only by a local variable
can be garbage-collected while still on screen. The frame then renders empty, with no error. Bind
each image to a module-level name, as `PLACEHOLDER` is.

**Path.** Paths are resolved against the working directory, not the module, so they only work when
you run from the repository root. See [`internal/known-issues.md`](./internal/known-issues.md).

## Layout

Fixed in `main.py`:

| Value | Effect |
|---|---|
| 5 | Accounts per row before wrapping |
| `padx=5, pady=5` | Spacing between frames |
| `Consolas 20` | Title font |
| `fg="blue"` | Title and link colour |

The row and column counters are module-level globals mutated by `accounts()` — see
[Architecture](./architecture.md).

## Window title

```python
window.title("Online Account Avatars and Banners")
```
