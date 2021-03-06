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

"""Echo server example for SocketServer

"""

__version__ = "$Id$"
#end_pymotw_header

import os
import SocketServer

class ForkingEchoRequestHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        # クライアントへ echo back する
        data = self.request.recv(1024)
        cur_pid = os.getpid()
        response = '%s: %s' % (cur_pid, data)
        self.request.send(response)
        return

class ForkingEchoServer(SocketServer.ForkingMixIn, SocketServer.TCPServer):
    pass

if __name__ == '__main__':
    import socket
    import threading

    address = ('localhost', 0) # カーネルにポート番号を割り当てさせる
    server = ForkingEchoServer(address, ForkingEchoRequestHandler)
    ip, port = server.server_address # 与えられたポート番号を調べる

    t = threading.Thread(target=server.serve_forever)
    t.setDaemon(True) # 終了時にハングアップしない
    t.start()
    print 'Server loop running in process:', os.getpid()

    # サーバへ接続する
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

    # データを送る
    message = 'Hello, world'
    print 'Sending : "%s"' % message
    len_sent = s.send(message)

    # レスポンスを受けとる
    response = s.recv(1024)
    print 'Received: "%s"' % response

    # クリーンアップ
    s.close()
    server.socket.close()
