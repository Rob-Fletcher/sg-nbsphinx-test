# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#



# -- Project information -----------------------------------------------------

project = "test_project"
copyright = "2024, guy"
author = "developer guy"

# The short X.Y version.
version = "0.1"
# The full version, including alpha/beta/rc tags
release = "main"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.mathjax",
    "sphinx_gallery.gen_gallery",
    # "nbsphinx",
]

# build the templated autosummary files
autosummary_generate = True
numpydoc_show_class_members = False

# autosectionlabel throws warnings if section names are duplicated.
# The following tells autosectionlabel to not throw a warning for
# duplicated section names that are in different documents.
autosectionlabel_prefix_document = True

panels_add_bootstrap_css = False


mathjax_path = "https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"

# katex options
#
#

katex_prerender = True

napoleon_use_ivar = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

coverage_ignore_modules = []

coverage_ignore_functions = []

coverage_ignore_classes = []

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = [".rst"]

# The master toctree document.
master_doc = "index"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# Disable docstring inheritance
autodoc_inherit_docstrings = False

# Disable displaying type annotations, these can be very verbose
autodoc_typehints = "description"
autodoc_typehints_description_target = "documented"

# Set the order that members should be documented
autodoc_member_order = "bysource"

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"

html_theme_options = {
    "header_links_before_dropdown": 5,
    "show_toc_level": 1,
    "navbar_align": "content",
    "navbar_persistent": ["search-button"],
    # "navbar_center": ["version-switcher", "navbar-nav"],
    "footer_start": ["copyright"],
    "footer_center": ["sphinx-version"],
    "secondary_sidebar_items": {
        "**/*": ["page-toc", "edit-this-page", "sourcelink"],
    },
    # "switcher": {
    #     "json_url": json_url,
    #     "version_match": version_match,
    # },
    "back_to_top_button": False,
    "pygments_dark_style": "lightbulb",
    "pygments_light_style": "xcode",
}

html_sidebars = {
    "getting_started": [],
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]


intersphinx_mapping = {"<name>": ("https://docs.python.org/", None)}

# -- Options for sphinx gallery ---------------------------------------------

examples_dirs = ["examples"]
gallery_dirs = ["auto_examples"]

image_scrapers = ("matplotlib",)

sphinx_gallery_conf = {
    # "backreferences_dir": "gen_modules/backreferences",
    # "doc_module": ("sphinx_gallery", "numpy"),
    # "reference_url": {
    #     "sphinx_gallery": None,
    # },
    "examples_dirs": examples_dirs,
    "gallery_dirs": gallery_dirs,
    "image_scrapers": image_scrapers,
    "reset_modules": ("matplotlib",),
    # specify the order of examples to be according to filename
    # "within_subsection_order": "FileNameSortKey",
    "promote_jupyter_magic": False,
    # capture raw HTML or, if not present, __repr__ of last expression in
    # each code block
    "capture_repr": ("_repr_html_", "__repr__"),
    "matplotlib_animations": True,
    "image_srcset": ["2x"],
    "nested_sections": True,
    "show_api_usage": True,
}