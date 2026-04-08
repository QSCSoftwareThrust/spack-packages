# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage, generator
from spack.package import *


class Dmrgpp(CMakePackage):
    """DMRG++ is a free and open source implementation of the Density Matrix Renormalization Group (DMRG) algorithm."""

    homepage = "https://g1257.github.io/dmrgPlusPlus"
    git = "https://github.com/g1257/dmrgpp.git"
    url = "https://github.com/g1257/dmrgpp/archive/refs/tags/v7.00.tar.gz"

    maintainers("g1257", "PDoakORNL")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    # NOTE Their license is similar to the **3-Clause BSD License**
    license("UNKNOWN", checked_by="github_user1")

    version("7.00", sha256="912358b796dfe160251c5e05648891a2c0be31a513a0d28aec50de11c87fa846")
    patch("fixup-brittle-hardcoded-relative-path.patch", when="@7.00")

    version("develop", branch="master")

    depends_on("cmake@3.31:", type="build")
    depends_on("ninja", type="build")
    generator("ninja")

    depends_on("cxx", type="build")
    depends_on("c", type="build")

    depends_on("gsl")

    depends_on("blas")
    depends_on("lapack")

    variant("boost", default=True, description="enable Boost")
    depends_on("boost", when="+boost")

    # NOTE HDF5 currently required dependency
    depends_on("hdf5+cxx+hl")

    def my_define_from_variant(self, variant, PackageName):
        if not self.has_variant(variant):
            raise KeyError('"{0}" is not a variant of "{1}"'.format(variant, self.name))

        if self.spec.variants[variant].value:
            cmake_var = f"CMAKE_REQUIRE_FIND_PACKAGE_{PackageName}"
        else:
            cmake_var = f"CMAKE_DISABLE_FIND_PACKAGE_{PackageName}"

        return self.define(cmake_var, True)


    def cmake_args(self):
        args = [
            self.my_define_from_variant("boost", "Boost"),
        ]

        return args
