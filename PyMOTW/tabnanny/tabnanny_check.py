#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann.  All rights reserved.
#
"""Using tabnanny from your own code
"""
#end_pymotw_header

import sys
import tabnanny

# 冗長モードを有効にする
tabnanny.verbose = 1

for dirname in sys.argv[1:]:
    tabnanny.check(dirname)



