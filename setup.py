from setuptools import setup, find_packages

import pytest_example

setup(
    name="pytest_example",
    version=pytest_example.__version__,
    description="Example Pytest Project",
    packages=find_packages(),
    install_requires=[],  # e.g. ['numpy >= 1.11.1', 'matplotlib >= 1.5.1']
)
