"""Artemis Movie Recomender.

A movie recomender that looks at review data and gives recomendations for movies to watch.
"""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("SE489MLOpsTeamArtemisIV")
except PackageNotFoundError:
    __version__ = "0.0.0+unknown"

__author__ = "TeamAtremisIV by Anjan, Sakshi, Joshua, Angel."
__email__ = "AHERN255@depaul.edu ABASAVAR@depaul.edu SGORKHAL@depaul.edu JCHANDR2@depaul.edu"

__all__ = ["__version__", "__author__", "__email__"]
