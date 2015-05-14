PyLadies Sphinx Theme
=====================

A PyLadies theme for docs that use Sphinx_/`Read the Docs`_.

.. _Sphinx: http://sphinx-doc.org/
.. _Read the Docs: https://readthedocs.org/


How to use this theme
---------------------

To use this theme:

#. Install the theme.
   Run ``pip install pyladies-sphinx-theme``.

#. Modify your Sphinx project's ``conf.py`` to use the theme:

   * Import ``pyladies_sphinx_theme``.
   * Add ``pyladies_sphinx_theme.get_path()`` to the ``html_theme_path`` list.
   * Set ``html_theme`` to ``'pyladies_sphinx_theme'``.

   Typically, ``conf.py`` will contain the following lines:

   ::

      import pyladies_sphinx_theme

      html_theme_path = [pyladies_sphinx_theme.get_path()]

      html_theme = 'pyladies_sphinx_theme'

   If you want to use the theme with Read the Docs (or other automated build
   tools), consider adding ``pyladies_sphinx_theme`` to your
   ``requirements.txt`` or ``setup.py`` requirements.

#. Rebuild your documentation (typically by running ``make html``).

Now your documentation has a shiny new look.
