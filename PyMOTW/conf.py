#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Configuration file for Sphinx-generated documentation.
"""

__version__ = "$Id$"

source_suffix = '.txt'

project = 'Python Module of the Week'
copyright = 'Doug Hellmann'
version = 'VERSION'
release = 'VERSION'

html_title = 'Python Module of the Week'
html_short_title = 'PyMOTW'
html_additional_pages = {}
html_use_modindex = True

# Ignore some subdirectories entirely
exclude_trees = [
    'glob/dir',
    'zipimport/example_package',
    ]

# Ignore README files and other files commonly used but not part of the docs
import glob
unused_docs = [ 
    'cmd/cmd_file',
    'mmap/lorem', 
    'mmap/lorem_copy', 
    'shlex/apostrophe', 
    'shlex/comments',
    'shlex/quotes',
    'weakref/trace',
    ]
ignore_base_names = [ 'README' ]
for base in ignore_base_names:
    unused_docs.extend(n[:-4] for n in glob.glob('*/%s.txt' % base))
