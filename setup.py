# -*- coding: utf-8 -*-
from __future__ import with_statement

from setuptools import setup, find_packages
import os

from sphinx_intl import __version__

install_requires = [
    'setuptools',
    'six',
    'click',
    'babel',
    'sphinx',
]

extras_require = {
    'transifex': [
        'transifex_client>=0.11'
    ],
    'test': [
        'pytest',
        'mock',
    ],
}

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()
description = \
    'Sphinx utility that make it easy to translate and to apply translation.'

setup(
    name='sphinx-intl',
    version=__version__,
    description=description,
    long_description=README,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "License :: OSI Approved :: BSD License",
        "Topic :: Documentation",
        "Topic :: Software Development :: Documentation",
        "Topic :: Text Processing :: General",
        "Topic :: Utilities",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    author="Takayuki SHIMIZUKAWA",
    author_email="shimizukawa@gmail.com",
    url="https://github.com/sphinx-doc/sphinx-intl",
    namespace_packages=[],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    extras_require=extras_require,
    entry_points="""\
    [console_scripts]
    sphinx-intl = sphinx_intl.commands:main
    """,
)
