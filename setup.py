# -*- coding: utf-8 -*-
# Copyright (c) 2015 PyLadies

import io
import os.path
import re

from setuptools import setup


NAME = "pyladies-sphinx-theme"
META_PATH = os.path.join("pyladies_sphinx_theme", "__init__.py")


HERE = os.path.abspath(os.path.dirname(__file__))


def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for fl in filenames:
        with io.open(fl, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)


META_FILE = read(META_PATH)


def find_meta(meta):
    """
    Extract __*meta*__ from META_FILE.
    """
    meta_match = re.search(
        r"^__{meta}__ = ['\"]([^'\"]*)['\"]".format(meta=meta),
        META_FILE, re.M
    )
    if meta_match:
        return meta_match.group(1)
    raise RuntimeError("Unable to find __{meta}__ string.".format(meta=meta))


long_description = read('README.rst', 'docs/changelog.rst')


setup(
    name="pyladies-sphinx-theme",
    version=find_meta("version"),
    description=find_meta("description"),
    long_description=long_description,
    url=find_meta("uri"),
    author=find_meta("author"),
    license=find_meta("license"),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Sphinx :: Theme',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Documentation :: Sphinx',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ],
    keywords='pyladies sphinx theme documentation docs',
    packages=['pyladies_sphinx_theme'],
    install_requires=['sphinx'],
    package_data={'pyladies_sphinx_theme': [
        'theme.conf',
        '*.html',
        'static/css/*.css',
    ]},
    zip_safe=False,
)
