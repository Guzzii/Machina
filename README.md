# Machina: Personal Assistant for Employee Benefits

## Dependency
The package has been tested on macOS and Linux so far. Below is the dependency of the project,
 - Python 3
 - Boost.Python library
 - C/C++ compiler

## Installation
### Mac OS X
#### 1. Install boost-python
The recommended method to intall `boost-python` is through `Homebrew`
```bash
$ brew install boost-python3
```
#### 2. Install Machina
```bash
$ python setup.py install
```
The command should build the binary file from c++ code, and the link it to python.

### Potential Installation Issues
#### 1. `boost-python36` library not found
Find the specific version of boost-python you have installed to your system. It might be
`boost-python`, `boost-python3` or `boost-python34`, etc. Then replace the correct version
at line 13 in `setup.py` file, and re-run the installation command.
