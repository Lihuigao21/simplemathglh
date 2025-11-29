# -*- coding: utf-8 -*-
"""
setup.py for simplemathglh
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README.md as long description
this_dir = Path(__file__).parent
long_description = (this_dir / "Readme.md").read_text(encoding="utf-8")

setup(
    name="simplemathglh",
    version="0.1.1",  
    description="A simple library for basic math operations.",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="Lihui Gao",
    author_email="Lihuigao21@gmail.com",

    url="https://github.com/Lihuigao21/simplemathglh",   

    packages=find_packages(),

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    python_requires=">=3.6",
)
