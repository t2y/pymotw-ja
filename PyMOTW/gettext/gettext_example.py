#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann All rights reserved.
#
"""
"""
#end_pymotw_header

import gettext

# メッセージカタログへのアクセスを設定する
t = gettext.translation('gettext_example', 'locale', fallback=True)
_ = t.ugettext

print _('This message is in the script.')
