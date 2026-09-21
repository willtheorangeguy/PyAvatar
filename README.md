<!-- Logo -->
<h1 align="center">
  <img src="https://raw.githubusercontent.com/willtheorangeguy/.github/main/icons/PyAvatar/logo.png" height="250px" width="400px" alt="PyAvatar">
  <br>
  PyAvatar
  <br>
</h1>

<!-- Copy -->
<h4 align="center">A desktop window showing every avatar you use, and where you use it — so they stay consistent across the web.</h4>

<!-- Badges -->
<div align="center">
  <img alt="PyPI Build State" src="https://github.com/willtheorangeguy/PyAvatar/actions/workflows/push-to-pypi.yml/badge.svg">
  <img alt="PyTest State" src="https://github.com/willtheorangeguy/PyAvatar/actions/workflows/pytest.yml/badge.svg">
  <img alt="Pylint State" src="https://github.com/willtheorangeguy/PyAvatar/actions/workflows/pylint.yml/badge.svg">
  <img alt="CodeQL State" src="https://github.com/willtheorangeguy/PyAvatar/actions/workflows/codeql-analysis.yml/badge.svg">
  <img alt="GitHub Version" src="https://img.shields.io/github/v/release/willtheorangeguy/PyAvatar?include_prereleases">
  <img alt="GitHub Issues" src="https://img.shields.io/github/issues/willtheorangeguy/PyAvatar">
  <img alt="GitHub Pull Requests" src="https://img.shields.io/github/issues-pr/willtheorangeguy/PyAvatar">
</div>

<!-- Navigation -->
<p align="center">
  <a href="#status">Status</a> •
  <a href="#key-features">Key Features</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#documentation">Documentation</a> •
  <a href="#support">Support</a> •
  <a href="#contributing">Contributing</a> •
  <a href="#credits">Credits</a> •
  <a href="#license">License</a>
</p>

<!-- Screenshot -->
<div align="center">
  <img src="https://raw.githubusercontent.com/willtheorangeguy/.github/main/icons/PyAvatar/main.png" alt="PyAvatar window">
</div>

## Status

**Pre-release, and incomplete on purpose.** The window, the grid layout, and the clickable links all work. The avatars themselves do not exist yet: `PyAvatar/images.py` and `PyAvatar/links.py` are empty, two placeholder accounts are hardcoded in `main.py`, and both share one placeholder image.

[`PLANNING.md`](PLANNING.md) tracks what remains — adding the images (0.2.0) and the links (0.3.0) before a 1.0.

Everything below describes what runs today. See [`docs/roadmap.md`](docs/roadmap.md) for what does not.

## Key Features

- A Tkinter window listing accounts in a five-column grid, wrapping as it fills.
- Each account shows an image, a name, and a link that opens in your browser.
- Pure standard library — Tkinter only, nothing to install beyond Python.
- Cross-platform: Windows, macOS, Linux.

## Installation

```bash
git clone https://github.com/willtheorangeguy/PyAvatar
cd PyAvatar
python main.py
```

Running from the repository root matters — see [`docs/installation.md`](docs/installation.md).

## Usage

Launch it and the window lists your accounts. Click a link to open that site.

Adding your own accounts means editing `main.py` today; see [`docs/configuration.md`](docs/configuration.md).

## Documentation

Full documentation lives in [`docs/`](docs/index.md):
[Quickstart](docs/quickstart.md) · [Installation](docs/installation.md) · [Configuration](docs/configuration.md) · [Architecture](docs/architecture.md) · [Development](docs/development.md) · [Testing](docs/testing.md) · [FAQ](docs/faq.md) · [Troubleshooting](docs/troubleshooting.md) · [Roadmap](docs/roadmap.md)

## Support

Open a [GitHub Discussion](https://github.com/willtheorangeguy/PyAvatar/discussions/new), file an [issue](https://github.com/willtheorangeguy/PyAvatar/issues/new/choose), or join the [Discord](https://discord.gg/Cjwt8DRfr3).

## Contributing

Please contribute using [GitHub Flow](https://guides.github.com/introduction/flow). Create a branch, add commits, and [open a pull request](https://github.com/willtheorangeguy/PyAvatar/compare).

See the org-wide [Contributing Guide](https://github.com/willtheorangeguy/.github/blob/main/CONTRIBUTING.md) and [Code of Conduct](https://github.com/willtheorangeguy/.github/blob/main/CODE_OF_CONDUCT.md).

## Credits

This software uses the following open source packages, projects, services or websites:

<!-- Credits Table -->
<table>
  <tr>
    <th align="center"><img src="https://applets.imgix.net/https%3A%2F%2Fassets.ifttt.com%2Fimages%2Fchannels%2F2107379463%2Ficons%2Fmonochrome_large.png?w=240&h=240&s=8a19bbc158996d098e2fb18310ba7f33" width="150" height="150" alt="GitHub"/></th>
    <th align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/182px-Python-logo-notext.svg.png" width="150" height="150" alt="PSF"/></th>
    <th align="center"><img src="https://pyinstaller.readthedocs.io/en/v4.2/_static/pyinstaller-draft1a.ico" width="150" height="150" alt="PyInstaller"/></th>
  </tr>
  <tr>
    <td align="center">GitHub</td>
    <td align="center">Python Software Foundation</td>
    <td align="center">PyInstaller</td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/">Web</a> - <a href="https://github.com/pricing">Plans</a></td>
    <td align="center"><a href="https://www.python.org/">Web</a> - <a href="https://psfmember.org/civicrm/contribute/transact?reset=1&id=2">Donate</a></td>
    <td align="center"><a href="https://pyinstaller.readthedocs.io/en/stable/">Web</a> - <a href="https://www.pyinstaller.org/funding.html#funding-by-individuals">Donate</a></td>
  </tr>
</table>

Sponsor [@willtheorangeguy](https://github.com/willtheorangeguy) on [PayPal](https://paypal.me/wvdg44?country.x=CA&locale.x=en_US).

## License

MIT — see [`LICENSE.md`](LICENSE.md).
