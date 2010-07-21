#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2007 Doug Hellmann.
#
#
#                         All Rights Reserved
#
# Permission to use, copy, modify, and distribute this software and
# its documentation for any purpose and without fee is hereby
# granted, provided that the above copyright notice appear in all
# copies and that both that copyright notice and this permission
# notice appear in supporting documentation, and that the name of Doug
# Hellmann not be used in advertising or publicity pertaining to
# distribution of the software without specific, written prior
# permission.
#
# DOUG HELLMANN DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE,
# INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS, IN
# NO EVENT SHALL DOUG HELLMANN BE LIABLE FOR ANY SPECIAL, INDIRECT OR
# CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS
# OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT,
# NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN
# CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#

"""Simple examples with StringIO module

See http://blog.doughellmann.com/2007/04/pymotw-stringio-and-cstringio.html

"""

__module_id__ = "$Id$"
#end_pymotw_header

# このプラットホーム上で利用可能な最も良い実装を探す
try:
    from cStringIO import StringIO
except:
    from StringIO import StringIO

# バッファへ書き込む
output = StringIO()
output.write('This goes into the buffer. ')
print >>output, 'And so does this.'

# 書き込まれた値を取り出す
print output.getvalue()

output.close() # バッファメモリを廃棄する

# 読み込みバッファを初期化する
input = StringIO('Inital value for read buffer')

# バッファから読み込む
print input.read()
