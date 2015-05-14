import codecs
import os.path

from setuptools import setup

readme_path = os.path.join(os.path.dirname(__file__), 'README.rst')

with codecs.open(readme_path, encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='pyladies_sphinx_theme',
    version='0.1.dev0',
    description='A PyLadies theme for Sphinx',
    long_description=long_description,
    url='https://github.com/pyladies/doc-theme',
    author='PyLadies',
    license='MIT',
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
