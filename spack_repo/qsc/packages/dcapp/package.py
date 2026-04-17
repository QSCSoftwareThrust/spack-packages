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
#     spack install dcapp
#
# You can edit this file again by typing:
#
#     spack edit dcapp
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack.package import *


class Dcapp(CMakePackage):
    """The DCA++ code provides a state of the art implementation of
    the dynamical cluster approximation (DCA) and its DCA++ extension.
    High scalability and portable performance allow to exploit today's leadership computing systems."""

    homepage = "https://github.com/CompFUSE/DCA"
    url = "https://github.com/CompFUSE/DCA/archive/refs/tags/v2.0.0-alpha.tar.gz"

    maintainers("PDoakORNL")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("BSD-3-Clause", checked_by="PDoakORNL")

    version("master", branch="master")
    version("v2.0.0-alpha")

    depends_on("cmake", type="build")
    depends_on("mpi")
    depends_on("llvm@21.0.0:", type="build")
    depends_on("fftw")
    depends_on("openblas threads=none")
    depends_on("hdf5+cxx")

    variant("cuda", default=False, description="enable CUDA support")
    variant("hip", default=False, description="eneable HIP support")

    with when("+cuda"):
        depends_on("cuda@12:12.9")

    with when("+hip"):
        depends_on("hip@6.0: +rocm")

    with when("+cuda" or "+hip"):
        depends_on("magma@2.10:")


    def install(self, spec, prefix):
        # FIXME: Unknown build system
        make()
        make("install")
