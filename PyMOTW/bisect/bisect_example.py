#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Exampe use of the bisect module.
"""
#end_pymotw_header
import bisect
import random

# ループの実行時に同じ疑似乱数になるように定数を使用する
random.seed(1)

# 20個の乱数を生成してソート順序を保持してリストへ挿入する
l = []
for i in range(1, 20):
    r = random.randint(1, 100)
    position = bisect.bisect(l, r)
    bisect.insort(l, r)
    print '%2d %2d' % (r, position), l
