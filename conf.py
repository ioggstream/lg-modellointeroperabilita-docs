#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# -- PROJECT Variables ----------------------------------------------------
settings_project_name = u"Linee Guida Modello di Interoperabilità"
settings_copyright_copyleft = "Agenzia per l'Italia Digitale"
settings_editor_name = "Agenzia per l'Italia Digitale"
settings_doc_version = 'Bozza in consultazione'
settings_doc_release = 'Bozza in consultazione'
settings_basename = 'lg-modellointeroperabilita-docs'
settings_file_name = 'lg-modellointeroperabilita-docs'
settings_discourse_url = 'https://forum.italia.it/'

# -- No need to change below here

import sys, os
docs_italia_theme = __import__("docs-italia-theme")
from recommonmark.transform import AutoStructify
from recommonmark.parser import CommonMarkParser

# -- RTD configuration ------------------------------------------------

# on_rtd is whether we are on readthedocs.org, this line of code grabbed from docs.readthedocs.org
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

# This is used for linking and such so we link to the thing we're building
rtd_version = os.environ.get('READTHEDOCS_VERSION', 'latest')
if rtd_version not in ['stable', 'latest']:
    rtd_version = 'stable'

rtd_project = os.environ.get('READTHEDOCS_PROJECT', '')

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.ifconfig',
    'docs-italia-theme',
    'sphinxcontrib.discourse'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
#source_parsers = {
#    '.md': CommonMarkParser,
#}

source_suffix = ['.rst', '.md']

# The encoding of source files.
#source_encoding = 'utf-8-sig'
source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = settings_project_name
copyright = settings_copyright_copyleft

# URL of Discourse instance used by sphinxcontrib.discourse extension
discourse_url = settings_discourse_url

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = settings_doc_version
# The full version, including alpha/beta/rc tags.
release = settings_doc_release

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = 'it'

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['.DS_Store', 'README', 'README.md', '.venv*']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# -- AutoStructify --------------------------------------------------------
def setup(app):
    app.add_config_value('recommonmark_config', {
        'auto_toc_tree_section': 'Contents',
        'enable_eval_rst': True,
        'enable_auto_doc_ref': True
    }, True)
    app.add_transform(AutoStructify)


# -- Options for HTML output ----------------------------------------------
html_theme = 'docs-italia-theme'

html_theme_path = [docs_italia_theme.get_html_theme_path()]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    # This option can be used with docs-italia-theme to customise how the versions "badge" is shown:
    # 'False': default (alabaster) badge | 'True': custom (italia) badge
    'custom_versions_badge': 'True',
}
# -- ReadTheDoc requirements and local template generation---------------------

# on_rtd is whether we are on readthedocs.org, this line of code grabbed from docs.readthedocs.org
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:  # only import and set the theme if we're building docs locally
    html_theme = 'docs-italia-theme'
    #html_theme_path = ["themes", ]
else:
    # Override default css to get a larger width for ReadTheDoc build
    html_context = {
        'css_files': [
            '_static/css/theme.css',
            '_static/css/badge_only.css',
        ],
    }


# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = settings_project_name

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = "images/logo.png"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%d/%m/%Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = settings_basename + 'doc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
'papersize': 'a4paper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  ('index', settings_file_name + '.tex', settings_project_name,
   settings_copyright_copyleft, 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = "media/agid-logo.png"

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
latex_show_pagerefs = False

# If true, show URL addresses after external links.
latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', settings_file_name, settings_project_name,
     [settings_editor_name], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', settings_file_name, settings_project_name,
   settings_copyright_copyleft, settings_project_name, settings_project_name,
   'Miscellaneous'),
]

numfig = True
