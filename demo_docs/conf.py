# -*- coding: utf-8 -*-
#

import os
import sys


sys.path.append(os.path.abspath('.'))

# import pyladies_sphinx_theme

extensions = []
project = u'PyLadies Handbook'
copyright = u'2014-2015, PyLadies'

version = '2.1'
release = '2.1.0'

master_doc = 'index'
exclude_patterns = ['_build', '_']
source_suffix = '.rst'


# html_theme = "pyladies"
# html_theme_path = ["_themes"]
# html_theme_path = [pyladies_sphinx_theme.get_path()]
html_theme_path = [".."]
html_theme = 'pyladies_sphinx_theme'

# html_style = "css/pyladies.css"
html_title = "PyLadies Organizer Handbook"
html_short_title = "PyLadies Kit"
html_favicon = "_static/favicon.ico"
html_static_path = ['_static']
html_use_smartypants = True
html_logo = "_static/images/pylady_geek_greyblue_icon.png"
htmlhelp_basename = 'PyLadiesHandbookdoc'

latex_documents = [
    ('index', 'PyLadiesHandbook.tex', u'PyLadies Handbook Documentation',
     u'PyLadies', 'manual'),
]
man_pages = [
    ('index', 'pyladieshandbook', u'PyLadies Handbook Documentation',
     [u'PyLadies'], 1)
]
texinfo_documents = [
    ('index', 'PyLadiesHandbook', u'PyLadies Handbook Documentation',
     u'PyLadies', 'PyLadiesHandbook', 'One line description of project.',
     'Miscellaneous'),
]
