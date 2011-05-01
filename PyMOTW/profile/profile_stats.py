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

# stats ファイルを5セット作成する
filenames = []
for i in range(5):
    filename = 'profile_stats_%d.stats' % i
    profile.run('print %d, fib_seq(20)' % i, filename)

# 1つのオブジェクトへ5つの stats ファイルを全て読み込む
stats = pstats.Stats('profile_stats_0.stats')
for i in range(1, 5):
    stats.add('profile_stats_%d.stats' % i)

# レポートのファイル名をクリーンアップする
stats.strip_dirs()

# 関数の累積時間によって統計をソートする
stats.sort_stats('cumulative')

stats.print_stats()
