# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pysysml2',
 'pysysml2.cli',
 'pysysml2.grammar',
 'pysysml2.grammar.distpy',
 'pysysml2.modeling']

package_data = \
{'': ['*'], 'pysysml2.grammar': ['distj/*']}

install_requires = \
['antlr4-python3-runtime==4.10',
 'anytree>=2.8.0,<3.0.0',
 'graphviz>=0.20.1,<0.21.0',
 'numpy>=1.24.2,<2.0.0',
 'openpyxl>=3.1.1,<4.0.0',
 'pandas>=1.5.3,<2.0.0',
 'typer>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['pysysml2 = pysysml2.cli.__main__:app']}

setup_kwargs = {
    'name': 'pysysml2',
    'version': '0.1.1',
    'description': 'Python based parser for the SysML 2.0 textual modeling language.',
    'long_description': "# PySysML2\n\nPySysML2 is a Python-based parser for the SysML 2.0 textual modeling language. Its main purpose is to parse a SysML 2.0 textual model into a Python object, and then transform that model into various data structures useful for data science and analysis.\n\n## Dependencies\n\nPySysML2 has the following dependencies:\n\n- anytree: provides the tree data structure, the basis for the Python model class\n- graphviz: renders images of graphs\n- numpy: numerical analysis package\n- pandas: data analysis package, provides the DataFrame data structure\n- openpyxl: allows Pandas to export to Excel\n- antlr4: provides the language parsing workbench\n\nNote that some of these packages (specifically Anytree, Graphviz, and Antlr4) are not available on Anaconda. Also, Pandas does not automatically install the required OpenPyxl module for exporting Excel, so that must be done separately.\n\n## Installation\n\nSee the [Development section](#development) for installation instructions if you are a developer.\n\n### Install From Source\n\n```console\ngit clone git@github.com:TrekkieByDay/PySysML2.git\n\ncd PySysML2/\n\npip install .\n```\n\n## Usage\n\n### CLI\n\nAfter installation, the `pysysml2` CLI tool should be available. The following demonstrates using the `pysysml2 export` command to export the SysML 2.0 textual model file to various output file formats.\n```console\n❯ pysysml2 export examples/models/model_test_1.sysml2 --output-dir out/ --format json,txt,csv,xlsx,dot,png\nUsing output directory: /Users/delannmt/Workspace/Projects/react/sysml/PySysML2/tmp\nExporting to JSON...\nExporting to txt...\nExporting to csv...\nExporting to xlsx...\nExporting to dot...\nExporting to png...\n```\n\nFor more information about the `pysysml2 export` command, use the `--help` option:\n```console\n❯ pysysml2 export --help\nUsage: pysysml2 export [OPTIONS] MODEL_FILE\n\n  Export a SysML v2 model to various file formats.\n\nArguments:\n  MODEL_FILE  The sysml2 model file.  [required]\n\nOptions:\n  --format TEXT          One or more comma-separated output file formats.\n                         Supported formats: json,txt,csv,xlsx,dot,png\n                         [default: json]\n  -o, --output-dir PATH  The output directory for the generated file(s).\n                         Defaults to current directory.\n  --help                 Show this message and exit.\n```\n\n### Python API Examples\n\nThe `examples/` directory contains an example Python script using `pysysml2` to export sample SysML 2.0 textual models to various output file formats. \n\n### Jupyter Notebook\n\nPySysML2 can be used through Jupyter notebooks. Check the [PySysML2_notebook.ipynb](PySysML2_notebook.ipynb) notebook to test the parsing functionality using the provided SysML 2.0 models.\n\n## Project Structure\n\nThe `pysysml2` directory contains all the code. It is divided into the `grammar` and `modeling` packages.\n\nThe `grammar` package contains all the Antlr4 parsing code. The primary artifact of interest is the `SysML.g4` grammar source file, which defines the basic elements of SysML 2.0 that PySysML2 implements. This file is used by the stand-alone Antlr4 command-line application that generates the language parsing Python code. Everything in the `distpy`, `.antlr`, and `distj` directories is auto-generated, and only `distpy` is required for PySysML2. The `sysml2_model_visitor.py` module is an extension of the generated `SysML2Visitor.py` and is the interface between the language parse tree from the textual model and the PySysML2 toolset.\n\nThe `modeling` package contains the SysML 2.0 modeling implementation and export tools. The `element` module implements model elements, and the `model` module implements a SysML 2.0 model class built from element objects. All export functions are in `model.py`.\n\n## Development\n\n### Setup Poetry\n\nTo use PySysML2 with Poetry, follow these steps:\n\n1. Install Poetry by following the instructions in the [official documentation](https://python-poetry.org/docs/#installation). **TLDR:** run the following command:\n```\ncurl -sSL https://install.python-poetry.org | python3 -\n```\n\n2. In the root directory of the project repository, run the following command to install all the required dependencies:\n```\npoetry install\n```\n\nThis will install the main dependencies specified in the `pyproject.toml` file.\n\n#### Development Group\n\nPySysML2 has a `dev` group in its `pyproject.toml` file that contains the dependencies required for development and testing. To install these dependencies, run the following command in the root directory of the cloned repository:\n\n```\npoetry install --group=dev\n```\n\nThis will install the development dependencies, including packages such as `pytest`.\n\n### Using Poetry\n\nBy default, Poetry creates a virtual environment for each project, so all the\ndependencies are installed locally to that environment. This ensures that different\nprojects can have different dependencies and versions installed without interfering\nwith each other.\n\nTo execute a command inside the virtual environment, use the `poetry run` command.\nFor instance, to run the tests for this project, run the following command:\n```\npoetry run pytest\n```\n\nTo activate the virtual environment, run the following command:\n```\npoetry shell\n```\n\nTo exit the virtual environment, use `exit`:\n```\nexit\n```\n\n### poetry2setup\n\nFor the convenience of users installing from source without Poetry, developers can\ngenerate the `setup.py` file from the `pyproject.toml` using the `poetry2setup` tool\n(requires [Poetry dev group installation](#development-group)):\n```\npoetry run poetry2setup >> setup.py\n```\n\n### poetry2conda\n\nTo support Anaconda distribution, developers can generate the conda environment file\nfrom the `pyproject.toml` using the `poetry2conda`\n(requires [Poetry dev groupinstallation](#development-group)):\n```\npoetry run poetry2conda pyproject.toml environment.yaml\n```\n\n### Why use Poetry?\n\nPoetry is a Python packaging and dependency management tool that helps simplify the process of building, packaging, and distributing Python projects. It provides a simple and intuitive way to manage project dependencies, handle virtual environments, and create distributable packages.\n\nUsing Poetry has several benefits:\n\n- **Dependency management**: Poetry simplifies dependency management by allowing you to easily install, uninstall, and upgrade packages, and automatically resolving dependencies between packages.\n- **Virtual environments**: Poetry creates and manages virtual environments for each project, ensuring that different projects can have different dependencies and versions installed without interfering with each other.\n- **Package building and publishing**: Poetry provides a simple way to build and publish packages to PyPI, as well as other package indexes such as your company's private package index.\n- **PEP standards compliance**: Poetry is designed to comply with the Python Enhancement Proposal (PEP) standards, which helps ensure compatibility with other Python tools and libraries.\n\n### How Poetry helps follow PEP standards\n\nPEP standards are a set of guidelines and recommendations for how to structure, package, and distribute Python code. These standards help ensure that Python packages are well-designed, easy to use, and compatible with other Python tools and libraries.\n\nPoetry is designed to follow the PEP standards, which makes it easier to create Python packages that are compliant with these guidelines. Here are some ways in which Poetry helps follow PEP standards:\n\n- [PEP 517](https://peps.python.org/pep-0517/)/[518](https://peps.python.org/pep-0518/) compliance: Poetry uses the PEP 517/518 standards for building and packaging Python projects, including build isolation to ensure that builds are reproducible and do not rely on the developer's environment. These standards help ensure compatibility with other Python tools such as pip and setuptools.\n- [pyproject.toml](https://pip.pypa.io/en/stable/reference/build-system/pyproject-toml/): Poetry uses a pyproject.toml configuration file to manage project settings and dependencies. This file conforms to the [PEP 621](https://peps.python.org/pep-0621/) standard, which provides a standard way to define project metadata and dependencies.\n- [PEP 440](https://peps.python.org/pep-0440/) versioning: Poetry uses the PEP 440 standard for versioning packages, which provides a standard way to version and compare package versions.\n- [PEP 508](https://peps.python.org/pep-0508/) dependencies: Poetry supports PEP 508-style dependencies, which allows you to specify dependencies with more detail and flexibility than standard requirements.txt files.",
    'author': 'Keith Lucas',
    'author_email': 'ke.le.luc@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
