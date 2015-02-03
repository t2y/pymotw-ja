#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann All rights reserved.
#
"""
"""
#end_pymotw_header

import asynchat
import logging
import socket


class EchoClient(asynchat.async_chat):
    """Sends messages to the server and receives responses.
    """

    # 並列にメッセージを送受信するのを説明するために
    # 人為的にバッファサイズを減少させる
    ac_in_buffer_size = 64
    ac_out_buffer_size = 64
    
    def __init__(self, host, port, message):
        self.message = message
        self.received_data = []
        self.logger = logging.getLogger('EchoClient')
        asynchat.async_chat.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.logger.debug('connecting to %s', (host, port))
        self.connect((host, port))
        return
        
    def handle_connect(self):
        self.logger.debug('handle_connect()')
        # コマンドを送る
        self.push('ECHO %d\n' % len(self.message))
        # データを送る
        self.push_with_producer(EchoProducer(self.message, buffer_size=self.ac_out_buffer_size))
        # データがそのまま送り返されるはずなのでデータ長をターミネイタにセットする
        self.set_terminator(len(self.message))
    
    def collect_incoming_data(self, data):
        """Read an incoming message from the client and put it into our outgoing queue."""
        self.logger.debug('collect_incoming_data() -> (%d)\n"""%s"""', len(data), data)
        self.received_data.append(data)

    def found_terminator(self):
        self.logger.debug('found_terminator()')
        received_message = ''.join(self.received_data)
        if received_message == self.message:
            self.logger.debug('RECEIVED COPY OF MESSAGE')
        else:
            self.logger.debug('ERROR IN TRANSMISSION')
            self.logger.debug('EXPECTED "%s"', self.message)
            self.logger.debug('RECEIVED "%s"', received_message)
        return

class EchoProducer(asynchat.simple_producer):

    logger = logging.getLogger('EchoProducer')

    def more(self):
        response = asynchat.simple_producer.more(self)
        self.logger.debug('more() -> (%s bytes)\n"""%s"""', len(response), response)
        return response
