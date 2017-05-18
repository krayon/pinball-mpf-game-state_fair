# sphinx-doc config file

try:
    import sphinx_rtd_theme

except ImportError:
    sphinx_rtd_theme = None

source_suffix = '.rst'

master_doc = 'index'

project = 'State Fair Pinball'
copyright = '2016, The Mission Pinball Framework Team'
author = 'The Mission Pinball Framework Team'

version = '0.1'
release = '0.1.0'

language = None

exclude_patterns = []

pygments_style = 'none'
highlight_language = 'yaml'

todo_include_todos = True

# -- Options for HTML output ----------------------------------------------

if sphinx_rtd_theme:
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

html_logo = 'images/state_fair_medium.png'
# html_favicon = None
# html_static_path = ['_static']

# html_extra_path = []  # will be copied to root

html_last_updated_fmt = '%b %d, %Y'
html_use_smartypants = True
htmlhelp_basename = 'MissionPinballFrameworkdoc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    'preamble': r'''
        \setcounter{secnumdepth}{0}
        \usepackage{bera}
        \usepackage[defaultsans]{lato}
        \usepackage{inconsolata}
        \usepackage{ragged2e}
        \AtBeginDocument{\raggedright}
        \setcounter{tocdepth}{1}
        \pagenumbering{arabic}
        \renewcommand{\labelitemi}{$\bullet$}
        \renewcommand{\labelitemii}{$\bullet$}
        \renewcommand{\labelitemiii}{$\bullet$}
        \renewcommand{\labelitemiv}{$\bullet$}

        \usepackage{fancyhdr}
        \pagestyle{fancy}
        \fancyhf{}
        \rhead{\thepage}
        \lhead{{\leftmark} ({\nouppercase{\rightmark}})}
        \renewcommand{\headrulewidth}{.4pt}

        ''',

    'figure_align': 'H',

    'releasename': 'Version',

    }

# Change final False to True to not include the index.rst in the PDF
latex_documents = [
    (master_doc, 'StateFairPinball.tex',
     'State Fair Pinball Documentation',
     'The Mission Pinball Framework Team', 'report', False),
]

# latex_logo = '_static/images/mpf-logo-200.png'  # doesn't work with report class
# latex_use_parts = False
# latex_show_pagerefs = True
# latex_show_urls = 'inline'
# latex_appendices = []
# latex_domain_indices = True

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'statefairpinball',
     'State Fair Pinball Documentation',
     author, 'MissionPinballFramework', 'Awesome Pinball Software.',
     'Miscellaneous'),
]

# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright
epub_exclude_files = ['search.html']
epub_tocdepth = 2
