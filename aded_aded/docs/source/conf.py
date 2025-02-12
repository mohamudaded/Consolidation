# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
import django

# Set up Django project path
sys.path.insert(0, os.path.abspath('../..'))  # Adjust to your project root
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "aded_aded.settings")
django.setup()

project = 'aded_aded'
copyright = '2025, Aded Mohamud'
author = 'Aded Mohamud'
release = '1.0'

# Sphinx extensions
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.autosummary",
]

templates_path = ["_templates"]

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "sphinx_rtd_theme"

autosummary_generate = True

# Use Napoleon to support Google-style and NumPy-style docstrings
napoleon_google_docstring = True
napoleon_numpy_docstring = False
