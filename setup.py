#!/usr/bin/env python3
""" Setup script for the {{ cookiecutter.app_name }} application.
"""
from os import walk
from pathlib import Path

from setuptools import find_packages
from setuptools import setup

# venv/lib/python3.8/site-packages/_bbpath.pth

_config = {
    "name": "bitbake",
    "url": "https://github.com/NGenetzky/bitbake",
    "author": "ngenetzky",
    "author_email": "nathan@genetzky.us",
    "package_dir": {"": "lib"},
    "packages": find_packages("lib"),
    "py_modules": ["codegen", "pyinotify"],
    "scripts": [
        "bin/bitbake",
        "bin/bitbake-diffsigs",
        "bin/bitbake-dumpsig",
        "bin/bitbake-hashclient",
        "bin/bitbake-hashserv",
        "bin/bitbake-layers",
        "bin/bitbake-prserv",
        "bin/bitbake-selftest",
        "bin/bitbake-worker",
        "bin/bitdoc",
        "bin/git-make-shallow",
        "bin/toaster",
        "bin/toaster-eventreplay",
    ],
    # "entry_points": {
    #     "console_scripts": ("{{ cookiecutter.cli_script }} = {{ cookiecutter.app_name }}.cli:main",),
    # },
    # "data_files": ("etc/",),
    "data_files": [("lib/python3.8/site-packages/", ["conf/bitbake_bbpath.pth"])],
    "zip_safe": False,
}


def main() -> int:
    """Execute the setup command."""
    # def data_files(*paths):
    #     """ Expand path contents for the `data_files` config variable.  """
    #     for path in map(Path, paths):
    #         if path.is_dir():
    #             for root, _, files in walk(str(path)):
    #                 yield root, tuple(str(Path(root, name)) for name in files)
    #         else:
    #             yield str(path.parent), (str(path),)
    #     return

    # def version():
    #     """ Get the local package version. """
    #     namespace = {}
    #     path = Path("src", _config["name"], "__version__.py")
    #     exec(path.read_text(), namespace)
    #     return namespace["__version__"]

    # _config.update({
    #     "data_files": list(data_files(*_config["data_files"])),
    #     "version": version(),
    # })
    setup(**_config)
    return 0


# Make the script executable.

if __name__ == "__main__":
    raise SystemExit(main())
