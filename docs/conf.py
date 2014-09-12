# -*- coding: utf-8 -*-
import os
import sys


import alabaster
import ablog

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.ifconfig',
    'sphinx.ext.extlinks',
    # Ipython requires simply ipython be installed:
    'IPython.sphinxext.ipython_directive',
    'IPython.sphinxext.ipython_console_highlighting',
    'alabaster',
    'ablog'
]


# PROJECT

version = release = ablog.__version__
project = u'Mobile-First'
copyright = u'2014, Yarko Tymciurak'
master_doc = 'index'
source_suffix = '.rst'
exclude_patterns = ['_build', 'Esens']


# HTML OUTPUT

html_title = "yarko.github.io/mobile-first"
html_static_path = ['_static']
html_use_index = False
html_domain_indices = False
html_show_sourcelink = True
html_favicon = '_static/ablog.ico'

todo_include_todos = True

# ABLOG

templates_path = [ablog.get_html_templates_path()]

if os.environ.get('READTHEDOCS', None) == 'True':
    skip_pickling = True

blog_title = 'Mobile First, Unconnected'
blog_baseurl = 'http://yarko.github.io/mobile-first'
# blog_baseurl = 'http://localhost:8000'
blog_locations = {
    'Chicago': ('Chicago, IL', None),
    'SF': ('San Francisco, CA', None),
}
# disqus_shortname = 'ahmetbakan'
# disqus_pages = False
fontawesome_css_file = 'css/font-awesome.css'


# THEME

html_style = 'alabaster.css'
html_theme = 'alabaster'
html_sidebars = {
   '**': ['about.html',
          'postcard.html', 'recentposts.html',
          'tagcloud.html', 'categories.html',
          'archives.html',
          'searchbox.html']
}
html_theme_path = [alabaster.get_path()]
html_theme_options = {
    'travis_button': False,
    'github_button': False,
    'github_user': 'yarko',
    'github_repo': 'mobile-first',
    'description': False,#'Mobile First, Unconnected',
    'logo': 'logo.png',
}

# SPHINX

intersphinx_mapping = {
    'python': ('http://docs.python.org', None),
    'sphinx': ('http://sphinx-doc.org', None),
    'prody': ('http://prody.csb.pitt.edu', None),
    'matplotlib': ('http://matplotlib.org', None),
    'numpy': ('http://docs.scipy.org/doc/numpy', None),
    'scipy': ('http://docs.scipy.org/doc/scipy/reference', None),
}
extlinks = {
    'wiki': ('http://en.wikipedia.org/wiki/%s', ''),
    'pdb': ('http://www.pdb.org/pdb/explore/explore.do?structureId=%s', ''),
    'pfam': ('http://pfam.sanger.ac.uk/family/%s', ''),
    'pfamprotein': ('http://pfam.sanger.ac.uk/protein/%s', ''),
    'uniprot': ('http://www.uniprot.org/uniprot/%s', ''),
    'pdbhet': ('http://www.pdb.org/pdb/ligand/ligandsummary.do?hetId=%s', ''),
    'pubmed': ('http://www.ncbi.nlm.nih.gov/pubmed/%s', 'PMID: '),
}



rst_epilog = '''
.. _Sphinx: http://sphinx-doc.org
.. _ABlog: http://ablog.readthedocs.org
.. _Python: http://python.org
.. _pip: http://www.pip-installer.org
.. _Disqus: http://disqus.com
.. _Werkzeug: http://werkzeug.pocoo.org
.. _GitHub: https://github.com
.. _PyPI: https://pypi.python.org/pypi/ablog
.. _Read The Docs: https://readthedocs.org
.. _ProDy: http://prody.csb.pitt.edu
.. _NMWiz: http://prody.csb.pitt.edu/nmwiz
.. _DruGUI: http://prody.csb.pitt.edu/drugui
.. _Evol: http://prody.csb.pitt.edu/evol
.. _Matplotlib: http://matplotlib.org
.. _Meze: https://github.com/abakan/mezzanine-meze
.. _Mezzanine: http://mezzanine.jupo.org
.. _NumPy: http://www.numpy.org
.. _IPython: http://ipython.org
.. _Napi: http://napi.rtfd.org
.. _Django: https://www.djangoproject.com
.. _Google Scholar: http://scholar.google.com/citations?user=-QAYVgMAAAAJ&hl=en
'''

import re
from sphinx import addnodes


event_sig_re = re.compile(r'([a-zA-Z-]+)\s*\((.*)\)')

def parse_event(env, sig, signode):
    m = event_sig_re.match(sig)
    if not m:
        signode += addnodes.desc_name(sig, sig)
        return sig
    name, args = m.groups()
    signode += addnodes.desc_name(name, name)
    plist = addnodes.desc_parameterlist()
    for arg in args.split(','):
        arg = arg.strip()
        plist += addnodes.desc_parameter(arg, arg)
    signode += plist
    return name


def setup(app):
    from sphinx.ext.autodoc import cut_lines
    from sphinx.util.docfields import GroupedField
    app.connect('autodoc-process-docstring', cut_lines(4, what=['module']))
    app.add_object_type('confval', 'confval',
                        objname='configuration value',
                        indextemplate='pair: %s; configuration value')
    fdesc = GroupedField('parameter', label='Parameters',
                         names=['param'], can_collapse=True)
    app.add_object_type('event', 'event', 'pair: %s; event', parse_event,
                        doc_field_types=[fdesc])
