# -*- coding: utf-8 -*-
# Copyright (c) 2015 PyLadies

import os.path

__author__ = "Lynn Root, PyLadies"
__version__ = "0.0.1.dev1"
__license__ = "MIT"

__email__ = "lynn@pyladies.com"
__description__ = "PyLadies Sphinx Theme"
__uri__ = "https://github.com/pyladies/doc-theme"


def get_path():
    """Return the path to this theme."""
    return os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
