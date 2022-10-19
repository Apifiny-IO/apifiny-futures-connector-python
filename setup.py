#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
====================================
@File    :  setup.py
@Time    :  2022/07/06 19:15:30
@Author  :  LiuKeCode@hotmail.com
@Desc    :  None
====================================
"""
# here put the import lib

import os
from setuptools import setup, find_packages

with open(
    os.path.join(os.path.dirname(__file__), "requirements.txt"), "r"
) as fh:
    requirements = fh.readlines()

NAME = "apifiny-futures"
DESCRIPTION = (
    "This is a library that works as a connector to Apifiny Futures OPEN API."
)
AUTHOR = "Apifiny"
URL = "https://github.com/Apifiny-IO/apifiny-futures-connector-python"
VERSION = None

about = {}

with open("README.md", "r") as fh:
    about["long_description"] = fh.read()

root = os.path.abspath(os.path.dirname(__file__))

if not VERSION:
    with open(os.path.join(root, "apifiny_futures", "__version__.py")) as f:
        exec(f.read(), about)
else:
    about["__version__"] = VERSION

setup(
    name=NAME,
    version=about["__version__"],
    license="MIT",
    description=DESCRIPTION,
    long_description=about["long_description"],
    long_description_content_type="text/markdown",
    author=AUTHOR,
    maintainer="Liuke",
    url=URL,
    keywords=["apifiny", "api", "unified APIs", "connect", "market data", "cryptocurrency", "tickdata", "spot",
              "futures", "orderbook data",
              "executed transactions data", "history market data", "real time market data", "fix protocol",
              "websocket api", "http api", "rest api", "fix api"],
    install_requires=[req for req in requirements],
    packages=find_packages(exclude=("tests",)),
    package_data={'': ['*.yaml'], },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Financial and Insurance Industry",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.7",
)
