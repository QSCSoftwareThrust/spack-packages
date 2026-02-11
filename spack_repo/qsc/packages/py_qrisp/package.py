# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install py-qrisp
#
# You can edit this file again by typing:
#
#     spack edit py-qrisp
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyQrisp(PythonPackage):
    """Qrisp is a high-level programming language for creating and compiling quantum algorithms.
    """

    homepage = "https://qrisp.eu"
    pypi = "qrisp/qrisp-0.7.19.tar.gz"

    maintainers("sethrj")

    license("EPL-2.0", checked_by="sethrj")

    version("0.7.19", sha256="27085566912dd101f61c8cb38f169e0da008dcbdb716586269c86ff75187ec16")

    depends_on("python@3.10:3.12", type=("build", "run"))
    # depends_on("py-pip@X.Y:", type="build")
    # depends_on("py-wheel@X.Y:", type="build")

    # FIXME: Add a build backend, usually defined in pyproject.toml. If no such file
    # exists, use setuptools.
    # depends_on("py-setuptools", type="build")
    # depends_on("py-hatchling", type="build")
    # depends_on("py-flit-core", type="build")
    # depends_on("py-poetry-core", type="build")

    # FIXME: Add additional dependencies if required.
    # depends_on("py-foo", type=("build", "run"))

    def config_settings(self, spec, prefix):
        # FIXME: Add configuration settings to be passed to the build backend
        # FIXME: If not needed, delete this function
        settings = {}
        return settings
