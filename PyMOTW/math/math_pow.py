#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Exponentiation
"""
#end_pymotw_header

import math

for x, y in [
    # 典型的な使用例
    (2, 3),
    (2.1, 3.2),

    # 必ず 1 になる
    (1.0, 5),
    (2.0, 0),

    # 数字ではない
    (2, float('nan')),

    # ルート
    (9.0, 0.5),
    (27.0, 1.0/3),
    ]:
    print '{:5.1f} ** {:5.3f} = {:6.3f}'.format(x, y, math.pow(x, y))
