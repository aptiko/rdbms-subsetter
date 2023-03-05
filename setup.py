#!/usr/bin/env python
import os
import sys

try:
    from setuptools import find_packages, setup
except ImportError:
    from distutils.core import find_packages, setup

if sys.argv[-1] == "publish":
    # Clean existing build artifacts
    os.system("rm -rf dist")
    os.system("rm -rf build")
    os.system("rm -rf rdbms_subsetter.egg-info")

    # Build and publish
    os.system("python setup.py sdist bdist_wheel")
    os.system("twine upload dist/*")

    sys.exit()

curdir = os.path.dirname(os.path.realpath(__file__))
readme = open(os.path.join(curdir, "README.rst")).read()

setup(
    name="rdbms-subsetter",
    version="0.2.6.2",
    description="Generate consistent subset of an RDBMS",
    long_description=readme,
    author="Catherine Devlin",
    author_email="catherine.devlin@gsa.gov",
    url="https://github.com/aptiko/rdbms-subsetter",
    install_requires=[
        "blinker>=1.5,<1.6",
        "sqlalchemy>=1.4,<1.5",
        "geoalchemy2>=0.13,<0.14",
    ],
    license="GNU General Public License v3",
    keywords="database testing",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Database",
        "Topic :: Software Development :: Testing",
    ],
    packages=find_packages(include=["dialects", "rdbms_subsetter"]),
    entry_points={
        "console_scripts": [
            "rdbms-subsetter = rdbms_subsetter.subsetter:generate",
        ]
    },
)
