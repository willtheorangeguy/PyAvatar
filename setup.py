"""Setup file for PyAvatar."""

# pylint: disable=invalid-name, import-error

from setuptools import setup, find_packages


def readme():
    """Read the README.md file."""
    with open("README.md", encoding="UTF-8") as f:
        return f.read()


setup(
    name="python-avatar",
    version="0.2.1",
    description="Easily display all of your creative avatars \
        to keep them consistent across websites.",
    long_description=readme(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
    ],
    keywords="avatar web accounts gui",
    url="https://github.com/Dog-Face-Development/PyAvatar",
    author="willtheorangeguy",
    packages=find_packages(where="PyAvatar"),
    package_dir={"": "PyAvatar"},
    include_package_data=True,
    py_modules=["main"],
    entry_points={"console_scripts": ["python-avatar=main:avatars"]},
)
