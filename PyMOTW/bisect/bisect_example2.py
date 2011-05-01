#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Example of using bisect_left
"""
#end_pymotw_header
import bisect
import random

# シードをリセットする
random.seed(1)

# bisect_left と insort_left を使用する
l = []
for i in range(1, 20):
    r = random.randint(1, 100)
    position = bisect.bisect_left(l, r)
    bisect.insort_left(l, r)
    print '%2d %2d' % (r, position), l
