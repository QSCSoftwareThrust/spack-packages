# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyQiskit(PythonPackage):
    """
    Qiskit is an open-source SDK for working with quantum computers at the level of extended quantum circuits, operators, and primitives.

    This library is the core component of Qiskit, which contains the building blocks for creating and working with quantum circuits, quantum operators, and primitive functions (Sampler and Estimator). It also contains a transpiler that supports optimizing quantum circuits, and a quantum information toolbox for creating advanced operators.

    For more details on how to use Qiskit, refer to the documentation located here:

    https://quantum.cloud.ibm.com/docs/
    """
    
    git = "https://github.com/Qiskit/qiskit.git"
    pypi = "qiskit/qiskit-2.3.0.tar.gz"

    version("2.3.0", sha256="e0a00c6681b8d04171c5cdb928837d992676f8aa4a07c390d446e54babaf6c1e")
    
    license("Apache-2.0")

    depends_on("py-setuptools-rust@1.12.0:", type="build")
    depends_on("py-dill@0.3.9:", type=("build", "run"))
    depends_on("py-numpy@2.4.2:", type=("build", "run"))
    depends_on("py-rustworkx@0.15.1:", type=("build", "run"))
    depends_on("py-scipy@1.17.0:", type=("build", "run"))
    depends_on("py-stevedore@5.4.0:", type=("build", "run"))
    depends_on("py-typing-extensions@4.15.0:", type=("build", "run"))