# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyQrisp(PythonPackage):
    """Qrisp is a high-level programming language for creating and compiling quantum algorithms."""

    homepage = "https://qrisp.eu"
    pypi = "qrisp/qrisp-0.7.19.tar.gz"

    maintainers("sethrj")

    license("EPL-2.0", checked_by="sethrj")

    version("0.7.19", sha256="27085566912dd101f61c8cb38f169e0da008dcbdb716586269c86ff75187ec16")


    depends_on("py-setuptools@42:", type="build")
    depends_on("py-wheel", type="build")

    depends_on("python@3.10:3.12", type=("build", "run"))
    depends_on("py-numpy@2.0:", type=("build", "run"))
    depends_on("py-sympy@:1.13", type=("build", "run"))
    depends_on("py-qiskit@0.44.0:", type=("build", "run"))
    depends_on("py-matplotlib@3.5.1:", type=("build", "run"))
    depends_on("py-scipy@1.10.0:", type=("build", "run"))
    depends_on("py-numba", type=("build", "run"))
    depends_on("py-networkx", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
    depends_on("py-dill", type=("build", "run"))
    depends_on("py-flask@:2.3.0", type=("build", "run"))
    depends_on("py-waitress", type=("build", "run"))
    depends_on("py-pyyaml", type=("build", "run"))
    depends_on("py-requests", type=("build", "run"))
    depends_on("py-psutil", type=("build", "run"))
    depends_on("py-jax@0.7.1", type=("build", "run"))
    depends_on("py-jaxlib@0.7.1", type=("build", "run"))
