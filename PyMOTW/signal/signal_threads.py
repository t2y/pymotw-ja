#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""

__version__ = "$Id$"
#end_pymotw_header

import signal
import threading
import os
import time

def signal_handler(num, stack):
    print 'Received signal %d in %s' % (num, threading.currentThread())

signal.signal(signal.SIGUSR1, signal_handler)

def wait_for_signal():
    print 'Waiting for signal in', threading.currentThread()
    signal.pause()
    print 'Done waiting'

# シグナルを受け取らないスレッドを開始する
receiver = threading.Thread(target=wait_for_signal, name='receiver')
receiver.start()
time.sleep(0.1)

def send_signal():
    print 'Sending signal in', threading.currentThread()
    os.kill(os.getpid(), signal.SIGUSR1)

sender = threading.Thread(target=send_signal, name='sender')
sender.start()
sender.join()

# シグナルを確認するためにスレッドを待ちます(発生しない！)
print 'Waiting for', receiver
signal.alarm(2)
receiver.join()
