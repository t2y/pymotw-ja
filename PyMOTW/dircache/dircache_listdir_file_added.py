#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""

__version__ = "$Id$"
#end_pymotw_header

import dircache
import os

path = '/tmp'
file_to_create = os.path.join(path, 'pymotw_tmp.txt')

# ディレクトリのコンテンツを調べる
first = dircache.listdir(path)

# 新しいファイルを作成する
open(file_to_create, 'wt').close()

# ディレクトリを再スキャンする
second = dircache.listdir(path)

# 作成したファイルを削除する
os.unlink(file_to_create)

print 'Identical :', first is second
print 'Equal     :', first == second
print 'Difference:', list(set(second) - set(first))
