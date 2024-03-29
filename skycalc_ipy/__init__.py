# Licensed under a 3-clause BSD style license - see LICENSE.rst

# Packages may add whatever they like to this file, but
# should keep this content at the top.
# ----------------------------------------------------------------------------
from ._astropy_init import *
# ----------------------------------------------------------------------------

# Enforce Python version check during package import.
# This is the same check as the one at the top of setup.py
import sys

__minimum_python_version__ = "2.7"

class UnsupportedPythonError(Exception):
    pass

if sys.version_info < tuple((int(val) for val in __minimum_python_version__.split('.'))):
    raise UnsupportedPythonError("skycalc_ipy does not support Python < {}".format(__minimum_python_version__))

if not _ASTROPY_SETUP_:
    # For egg_info test builds to pass, put package imports here.

    import warnings as _warnings
    from astropy.utils.exceptions import AstropyWarning as _AstropyWarning

    _warnings.simplefilter('ignore', category=_AstropyWarning)

    from . import ui
    from . import core

    from .ui import SkyCalc
