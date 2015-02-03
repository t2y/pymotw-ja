#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann All rights reserved.
#
"""
"""
#end_pymotw_header

import asyncore
import logging
import socket

from asynchat_echo_handler import EchoHandler

class EchoServer(asyncore.dispatcher):
    """Receives connections and establishes handlers for each client.
    """
    
    def __init__(self, address):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind(address)
        self.address = self.socket.getsockname()
        self.listen(1)
        return

    def handle_accept(self):
        # クライアントがソケットへ接続したときに呼び出される
        client_info = self.accept()
        EchoHandler(sock=client_info[0])
        # 一度に一クライアントのみを扱うのでハンドラを設定したらクローズする
        # 普通はクローズせずにサーバは停止命令を受け取るか、永遠に実行される
        self.handle_close()
        return
    
    def handle_close(self):
        self.close()
