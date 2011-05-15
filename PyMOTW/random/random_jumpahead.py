#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Random class.
"""
#end_pymotw_header

import random
import time

r1 = random.Random()
r2 = random.Random()

# r1 から r2 を強制的に別の乱数周期にする
r2.setstate(r1.getstate())
r2.jumpahead(1024)

for i in xrange(3):
    print '%04.3f  %04.3f' % (r1.random(), r2.random())
