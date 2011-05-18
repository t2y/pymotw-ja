#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Loading data from a zipfile.
"""
#end_pymotw_header

import pkgutil
import zipfile
import sys

# カレントディレクトリからコードとローカルのファイルシステムに
# 存在しない名前を使用するテンプレートを含む ZIP ファイルを作成する
with zipfile.PyZipFile('pkgwithdatainzip.zip', mode='w') as zf:
    zf.writepy('.')
    zf.write('pkgwithdata/templates/base.html',
             'pkgwithdata/templates/fromzip.html',
             )

# インポートパスへ ZIP ファイルを追加する
sys.path.insert(0, 'pkgwithdatainzip.zip')

# ZIP アーカイブから来ていることを表示するために pkgwithdata をインポートする
import pkgwithdata
print 'Loading pkgwithdata from', pkgwithdata.__file__

# テンプレートの本文を表示する
print '\nTemplate:'
print pkgutil.get_data('pkgwithdata', 'templates/fromzip.html').encode('utf-8')
