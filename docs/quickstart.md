# PyAvatar — Quickstart

## Run it

```bash
git clone https://github.com/willtheorangeguy/PyAvatar
cd PyAvatar
python main.py
```

**Run it from the repository root.** The placeholder image is loaded from
`PyAvatar/images/placeholder.gif` as a path relative to the working directory, so launching from
anywhere else fails immediately. See [`internal/known-issues.md`](./internal/known-issues.md).

Nothing to install: Tkinter ships with Python.

## What you get

A window titled *Online Account Avatars and Banners* containing:

- A heading.
- One frame per account, laid out five to a row, wrapping downward.
- In each frame: the image, the account name, and the URL in blue.

Clicking a URL opens it in your default browser.

## What is there today

Two accounts, hardcoded in `main.py`, both using the same placeholder image:

```python
accounts(PLACEHOLDER, "GitHub", "https://github.com")
accounts(PLACEHOLDER, "GitLab", "https://gitlab.com")
```

That is the whole dataset. Real avatars are what 0.2.0 is for — see [Roadmap](./roadmap.md).

## Adding your own

Add a call for each account:

```python
accounts(PLACEHOLDER, "Mastodon", "https://mastodon.social/@you")
```

For your own image, load it first — and note **Tkinter's `PhotoImage` only reads GIF and PNG**,
so a JPEG avatar has to be converted:

```python
MASTODON = PhotoImage(file="PyAvatar/images/mastodon.gif")
accounts(MASTODON, "Mastodon", "https://mastodon.social/@you")
```

Keep a reference to every `PhotoImage` in a variable that outlives the call — Tkinter does not,
and a garbage-collected image renders as an empty frame with no error.

More in [Configuration](./configuration.md).

## Installing it as a command

```bash
pip install python-avatar
python-avatar
```

This currently fails unless your working directory happens to be a checkout of the repository,
for the path reason above.
