# PyAvatar — Documentation

A Tkinter window that displays the avatars you use across the web, alongside links to where each
one lives.

```text
PyAvatar/
├── main.py               the window: layout, account frames, link handling
├── PyAvatar/
│   ├── images.py         intended to hold image references — currently empty
│   ├── links.py          intended to hold website and file links — currently empty
│   └── images/
│       └── placeholder.gif
├── tests/                pytest and unittest
├── PLANNING.md           what is left before 1.0
└── docs/                 this documentation
```

## Pages

- [Quickstart](./quickstart.md) — run it
- [Installation](./installation.md) — from source or from PyPI, and the catch
- [Configuration](./configuration.md) — adding your own accounts
- [Architecture](./architecture.md) — the window, the grid, the layout counters
- [Development](./development.md) — the packaging situation and the linting setup
- [Testing](./testing.md) — the suite
- [FAQ](./faq.md) — GIFs, PyPI names, why it looks unfinished
- [Troubleshooting](./troubleshooting.md) — missing images, Tkinter, the console script
- [Roadmap](./roadmap.md) — direction and non-goals
- [Known issues](./internal/known-issues.md) — recorded defects

## What state this is in

**Pre-release.** The interesting half — a scrolling grid of accounts with clickable links — works.
The content half does not exist: `images.py` and `links.py` are empty modules, and `main.py`
hardcodes two accounts (GitHub and GitLab) sharing one placeholder image.

`PLANNING.md` treats that as the plan rather than an oversight: 0.2.0 adds the images, 0.3.0 adds
the links, 1.0.0 is the first non-beta.

These docs describe what the code does now, and say plainly where the documented intent has not
been built.

## The idea

If you use the same handle across a dozen sites, keeping the avatar consistent means remembering
which ones you have updated. A window listing each account, its current avatar, and a link
straight to the settings page turns that into something you can see at a glance.
