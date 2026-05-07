"""TeamArtemisIV.

An ML movie recomender.
"""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("SE489MLOpsTeamArtemisIV")
except PackageNotFoundError:
    __version__ = "0.0.0+unknown"

__author__ = "TeamArtemisIV"
__email__ = "AHERN255@depaul.edu"

__all__ = ["__version__", "__author__", "__email__"]
