# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

sys.path.insert(0, os.path.abspath(".."))


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "EVars Loader"
copyright = "2022, Nikhil Reddy"
author = "Nikhil Reddy"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",  # automatically generate documentation for modules
    "sphinx.ext.githubpages",  # adds a .nojekyll file
    "autodocsumm",  # to generate tables of functions, attributes, methods, etc.
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_static_path = ["_static"]
html_theme = "sphinx_rtd_theme"
html_show_sphinx = False
html_show_sourcelink = False


autodoc_typehints = "description"
autodoc_class_signature = "separated"
autodoc_default_options = {"show-inheritance": True}
autodoc_member_order = "groupwise"
autodoc_type_aliases = {
    "Transformer": "Transformer",
    "Validator": "Validator",
    "EnvironmentVariableDefinitions": "EnvironmentVariableDefinitions",
    "EnvironmentVariableValues": "EnvironmentVariableValues",
}
autodoc_default_options = {"autosummary-members": True}
add_module_names = False
