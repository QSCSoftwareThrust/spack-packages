# Quantum Science Center Spack repository

This repository is for rapid development and deployment of quantum
science software using the [Spack HPC package manager](https://spack.readthedocs.io/en/latest/).

# Usage

Currently this project is just getting started so it's assumed you're on the SE
team developing a new package.

## Adding this package repository to Spack

Assuming you have already set up Spack (see [the Spack getting started page](https://spack.readthedocs.io/en/latest/getting_started.html)):

```sh
$ spack repo add https://github.com/QSCSoftwareThrust/spack-packages.git
```

This clones the repository to your local spack package repo: you can find the
location with `spack location --repo` or `spack repo list`. You can treat it
like a normal git repository.

## Creating a new package

Follow the [spack packaging guidelines](https://spack.readthedocs.io/en/latest/packaging_guide_creation.html), but use the `-N qsc` flag to `spack create` to indicate the new package belongs in this repository.

### Example: qrisp

This package is available [at PyPI](https://pypi.org/project/qrisp/#qrisp-0.7.19.tar.gz), which provides a link to a tar.gz file.

```console
$ spack create -N qsc https://files.pythonhosted.org/packages/.../qrisp-0.7.19.tar.gz
==> This looks like a URL for qrisp
==> Fetching https://files.pythonhosted.org/packages/.../qrisp-0.7.19.tar.gz
    [100%]  588.25 KB @    4.7 MB/s
==> This package looks like it uses the python build system
==> Changing package name from qrisp to py-qrisp
==> Created template for py-qrisp package
==> Created package file: /.../spack_repo/qsc/packages/py_qrisp/package.py
```

The package file is then opened for editing.
- The SHA256 hash should match the one on the PyPI package page
- Tell Copilot to update the spack package recipe from the
  `setup.cfg`/`setup.py` files (some projects will use `.toml`, but this one
  doesn't seem to.)

## Installing a QSC package

To be added.

# Environments

Future work will add concrete environments for relevant HPC and QHPC systems.
