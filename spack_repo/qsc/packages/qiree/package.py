# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Qiree(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://github.com/ORNL-QCI/qiree"
    url = "https://github.com/ORNL-QCI/qiree/archive/refs/tags/v0.1.0.tar.gz"

    maintainers("sethrj")

    license("Apache-2.0 WITH LLVM-exception", checked_by="sethrj")

    version("0.1.0", sha256="8fdb974a7b85908341207b983dcd4fa3f996193f7ae843945f93eae4da655513")

    variant("lightning", default=False, description="enable pennylane lightning")
    variant("qsim", default=True, description="enable qsim")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("llvm@14:")
    depends_on("py-pennylane-lightning", when="+lightning")

    # QSim requires gtest to configure...
    depends_on("googletest", type="build", when="+qsim")

    def cmake_args(self):
        args = [
            self.define_from_variant("QIREE_USE_LIGHTNING", "lightning"),
            self.define_from_variant("QIREE_USE_QSIM", "qsim"),
            ]
        return args
