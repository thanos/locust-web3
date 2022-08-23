"""Sphinx configuration."""
project = "Locust Web3 Client"
author = "thanos vassilakis"
copyright = "2022, thanos vassilakis"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
