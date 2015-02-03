#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# $Id$
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

"""Use several threads to download enclosures from RSS feeds.

See http://blog.doughellmann.com/2007/04/pymotw-queue.html
"""
#end_pymotw_header

# システムモジュール
from Queue import Queue
from threading import Thread
import time

# ローカルモジュール
import feedparser

# グローバル変数をセット
num_fetch_threads = 2
enclosure_queue = Queue()

# 実際のアプリではハードコーディングしない...
feed_urls = [ 'http://www.castsampler.com/cast/feed/rss/guest',
             ]


def downloadEnclosures(i, q):
    """This is the worker thread function.
    It processes items in the queue one after
    another.  These daemon threads go into an
    infinite loop, and only exit when
    the main thread ends.
    """
    while True:
        print '%s: Looking for the next enclosure' % i
        url = q.get()
        print '%s: Downloading:' % i, url
        # URL から実際にダウンロードせずに sleep で欺く
        time.sleep(i + 2)
        q.task_done()


# エンクロージャを取得してスレッドを設定する
for i in range(num_fetch_threads):
    worker = Thread(target=downloadEnclosures, args=(i, enclosure_queue,))
    worker.setDaemon(True)
    worker.start()

# フィードをダウンロードしてキューへエンクロージャの URL を追加する
for url in feed_urls:
    response = feedparser.parse(url, agent='fetch_podcasts.py')
    for entry in response['entries']:
        for enclosure in entry.get('enclosures', []):
            print 'Queuing:', enclosure['url']
            enclosure_queue.put(enclosure['url'])

# 全てのダウンロード処理が完了したことを表す、キューが空になるまで待つ
print '*** Main thread waiting'
enclosure_queue.join()
print '*** Done'
