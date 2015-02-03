#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann All rights reserved.
#
"""
"""
#end_pymotw_header

import decimal

# コンテキストを制限された精度で設定する
c = decimal.getcontext().copy()
c.prec = 3

# 定数を作成
pi = c.create_decimal('3.1415')

# 定数の値は丸められる
print 'PI:', pi

# 定数を使用した結果はグローバルコンテキストを使用する
print 'RESULT:', decimal.Decimal('2.01') * pi
