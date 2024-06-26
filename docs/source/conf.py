# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'sphinxProject'
copyright = '2024, vijay'
author = 'vijay'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx_design"]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
html_theme_options = {
    "logo": {
        "text": "Go Lego",
    },
    "show_toc_level": '0'
}
html_logo = '_static/logo.png'
html_css_files = {
    'css/custom.css',
}

html_sidebars = {
   '**': ['localtoc.html'],
}

