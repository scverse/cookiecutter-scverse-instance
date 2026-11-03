# Installation

You need to have Python 3.12 or newer installed on your system.
If you don't have Python installed, we recommend installing [uv][].

We recommend managing dependencies in project-specific virtual environments to avoid dependency conflicts.
This is most convenient using package managers such as [uv][].
Choose from the options below to install cookiecutter-scverse-instance:

<!--
1. Add the latest release of `cookiecutter-scverse-instance` from [PyPI][] to your `uv` project:

   ```bash
   uv add cookiecutter-scverse-instance
   ```

1. Install the latest release into a [standard virtual environment][venv]:

   ```bash
   (after activating your venv)
   pip install cookiecutter-scverse-instance
   ```

-->

1. Install the latest development version:

   ```bash
   pip install git+https://github.com/scverse/cookiecutter-scverse-instance.git  # (or `uv add`)
   ```

To work on cookiecutter-scverse-instance itself, see {doc}`contributing`.

[uv]: https://github.com/astral-sh/uv
[pypi]: https://pypi.org/project/cookiecutter-scverse-instance
[venv]: https://docs.python.org/3/tutorial/venv.html
