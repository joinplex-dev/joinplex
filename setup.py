"""Setup to install the Joinplex package.
"""
from setuptools import setup

requirements = [
    "pandas",
]

setup(use_scm_version=True, setup_requires=["setuptools_scm"])
