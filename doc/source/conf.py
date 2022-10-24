from datetime import datetime

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
year = datetime.today().year
project = "Joinplex"
copyright = f"{year}, Nathan McDougall"
author = "Nathan McDougall"
release = "0.0"
version = "0.0.0"

master_doc = "index"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx_toggleprompt",
    "sphinx.ext.napoleon",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.coverage",
    "sphinx.ext.doctest",
    "sphinx.ext.extlinks",
    "sphinx.ext.ifconfig",
    "sphinx.ext.intersphinx",
    "sphinx.ext.linkcode",
    "sphinx.ext.mathjax",
    "sphinx.ext.todo",
]

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]
html_theme_options = {
    "github_url": "https://github.com/joinplex-dev/joinplex",
    "pygment_light_style": "tango",
    "pygment_dark_style": "monokai",
    "logo": {
        "image_light": "https://github.com/joinplex-dev/brand/blob/main/img/png/512/joinplex_full_lightbg.png?raw=true",
        "image_dark": "https://github.com/joinplex-dev/brand/blob/main/img/png/512/joinplex_full_darkbg.png?raw=true",
        "alt_text": "Joinplex Documentation - Index",
    },
    "favicons": [
        {
            "rel": "icon",
            "sizes": "16x16",
            "href": "https://github.com/joinplex-dev/brand/blob/main/img/png/16/joinplex_icon_darkbg.png?raw=true",
        },
        {
            "rel": "icon",
            "sizes": "32x32",
            "href": "https://github.com/joinplex-dev/brand/blob/main/img/png/32/joinplex_icon_darkbg.png?raw=true",
        },
        {
            "rel": "apple-touch-icon",
            "sizes": "180x180",
            "href": "https://github.com/joinplex-dev/brand/blob/main/img/png/180/joinplex_icon_darkbg.png?raw=true",
            "color": "#000000",
        },
    ],
}


def linkcode_resolve(domain, info):
    if domain != "py":
        return None
    if not info["module"]:
        return None
    filename = info["module"].replace(".", "/")
    return "https://github.com/joinplex-dev/joinplex/%s.py" % filename
