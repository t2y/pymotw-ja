#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""

__version__ = "$Id$"
#end_pymotw_header

import profile
import pstats
from profile_fibonacci_memoized import fib, fib_seq

# 1つのオブジェクトへ5つの stats ファイルを全て読み込む
stats = pstats.Stats('profile_stats_0.stats')
for i in range(1, 5):
    stats.add('profile_stats_%d.stats' % i)
stats.strip_dirs()
stats.sort_stats('cumulative')

# "(fib" を含む行のみに出力を制限する
stats.print_stats('\(fib')
