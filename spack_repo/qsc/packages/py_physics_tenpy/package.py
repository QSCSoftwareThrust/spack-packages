# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPhysicsTenpy(PythonPackage):
    """Simulation of quantum many-body systems with tensor networks in
        Python."""

    homepage = "https://github.com/tenpy/tenpy"
    pypi = "physics_tenpy/physics_tenpy-1.1.0.tar.gz"
    git = "https://github.com/tenpy/tenpy.git"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    license("Apache-2.0", checked_by="cferenba")

    version("main", branch="main")
    version("1.1.0", sha256="dd9001d387c0b12ab34da29a5874a406b3c7a38d0513c7dcbfb8d41df0db446b")
    version("1.0.7", sha256="8a6ff318844ac57ae2ca893a5b2d4239eccb3ed11ab0863314ea5260510a27ac")

    depends_on("cxx", type="build")

    depends_on("python@3.10:", type=("build", "run"))

    depends_on("py-setuptools@77.0.3:", type="build")
    depends_on("py-cython@3.0:", type="build")

    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))

    depends_on("py-pytest", type="test")

