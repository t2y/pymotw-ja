#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann All rights reserved.
#
"""
"""
#end_pymotw_header

import resource
import sys
import signal
import time

# CPU 時間リミットが実行されたときに
# 通知するシグナルハンドラを設定する
def time_expired(n, stack):
    print 'EXPIRED :', time.ctime()
    raise SystemExit('(time ran out)')

signal.signal(signal.SIGXCPU, time_expired)

# CPU 時間リミットを調整する
soft, hard = resource.getrlimit(resource.RLIMIT_CPU)
print 'Soft limit starts as  :', soft

resource.setrlimit(resource.RLIMIT_CPU, (1, hard))

soft, hard = resource.getrlimit(resource.RLIMIT_CPU)
print 'Soft limit changed to :', soft
print

# 意味のない処理で CPU 時間を消費する
print 'Starting:', time.ctime()
for i in range(200000):
    for i in range(200000):
        v = i * i

# この処理は実行されない
print 'Exiting :', time.ctime()
