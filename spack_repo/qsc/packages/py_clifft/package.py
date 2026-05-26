# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyClifft(PythonPackage):
    """Clifft is a fast exact simulator for near-Clifford quantum circuits.

    It accepts Stim-format circuits, extends them with non-Clifford gates,
    and compiles them into bytecode executed by a high-performance
    Schroedinger Virtual Machine. The main simulation cost scales with the
    active dimension of the dense state vector rather than directly with
    the total number of physical qubits."""

    homepage = "https://unitaryfoundation.github.io/clifft/"
    pypi = "clifft/clifft-0.4.1.tar.gz"
    git = "https://github.com/unitaryfoundation/clifft.git"

    maintainers("bachase")

    license("Apache-2.0", checked_by="bachase")

    version("main", branch="main")
    version("0.4.1", sha256="518c9d961a8e0caf4ff2eb90bdff30ece2fa4a982764d1b2e0a462d4f77319ef")

    depends_on("cxx", type="build")

    depends_on("python@3.12:", type=("build", "run"))

    depends_on("cmake@3.20:", type="build")
    depends_on("py-scikit-build-core@0.10:", type="build")
    depends_on("py-nanobind@2:", type="build")
    depends_on("py-setuptools-scm@8:", type="build")

    depends_on("py-numpy@1.26:", type=("build", "run"))
