#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""

__version__ = "$Id$"
#end_pymotw_header

import linecache

# sys.path を検索して linecache モジュールを探す
module_line = linecache.getline('linecache.py', 3)
print '\nMODULE : ', module_line
