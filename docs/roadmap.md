# PyAvatar — Roadmap

Direction, not a schedule. `PLANNING.md` holds the version checklist; defects are in
[`internal/known-issues.md`](./internal/known-issues.md). This page is about what the app is
*for*.

## Where it is

The window works: a grid of account frames, each with an image, a name, and a clickable link,
wrapping five to a row. Twenty-three tests cover it, headlessly.

The content does not exist. Two hardcoded placeholder accounts share one placeholder image, and
the modules meant to hold the real data are empty.

## Planned

From `PLANNING.md`:

| Version | Goal |
|---|---|
| 0.2.0 | Add all avatar images |
| 0.3.0 | Add all avatar links |
| 1.0.0 | First non-beta release |

## Considered

**Resolving image paths against the module.** The single change that would make the installed
`python-avatar` command work at all.

**One package name.** `setup.py`, `setup.cfg`, and `pyproject.toml` currently disagree.

**Moving the account list out of `main.py`.** `images.py` and `links.py` exist for exactly this
and are empty; until they are filled, adding an account means editing the function that draws the
window.

**Real content in `docs/configuration.md`'s place.** The old `CUSTOMIZATION.md` said only that it
would be written when the app was finished; the customisation that *is* possible today is now
documented instead.

**A scrollable window.** The grid grows downward with no scrolling, so a long account list
eventually runs off screen.

**Banners as well as avatars.** The window title promises both; only one image per account is
supported.

## Non-goals

**Fetching avatars from the sites themselves.** That would mean API keys, OAuth, and rate limits
for every service — an enormous surface for a window that displays local files. There is no
network code here and none planned.

**Editing avatars.** It displays; it does not upload or crop. Each link goes to the settings page
where the site itself does that better.

**Runtime dependencies.** Tkinter only. Pillow would buy JPEG support and is still not worth
being the first dependency.

**A web version.** The point is a local window over local files.

## Contributing

Issues and pull requests welcome — see the
[Contributing Guide](https://github.com/willtheorangeguy/.github/blob/main/CONTRIBUTING.md), or
the [Discord](https://discord.gg/Cjwt8DRfr3). Filling in `images.py` and `links.py` is the work
that unblocks everything else.
