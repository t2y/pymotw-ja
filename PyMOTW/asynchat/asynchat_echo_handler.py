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


class EchoHandler(asynchat.async_chat):
    """Handles echoing messages from a single client.
    """

    # 並列にメッセージを送受信するのを説明するために
    # 人為的にバッファサイズを減少させる
    ac_in_buffer_size = 64
    ac_out_buffer_size = 64
    
    def __init__(self, sock):
        self.received_data = []
        self.logger = logging.getLogger('EchoHandler')
        asynchat.async_chat.__init__(self, sock)
        # ECHO コマンドを探すのを開始する
        self.process_data = self._process_command
        self.set_terminator('\n')
        return

    def collect_incoming_data(self, data):
        """Read an incoming message from the client and put it into our outgoing queue."""
        self.logger.debug('collect_incoming_data() -> (%d bytes)\n"""%s"""', len(data), data)
        self.received_data.append(data)

    def found_terminator(self):
        """The end of a command or message has been seen."""
        self.logger.debug('found_terminator()')
        self.process_data()
    
    def _process_command(self):        
        """We have the full ECHO command"""
        command = ''.join(self.received_data)
        self.logger.debug('_process_command() "%s"', command)
        command_verb, command_arg = command.strip().split(' ')
        expected_data_len = int(command_arg)
        self.set_terminator(expected_data_len)
        self.process_data = self._process_message
        self.received_data = []
    
    def _process_message(self):
        """We have read the entire message to be sent back to the client"""
        to_echo = ''.join(self.received_data)
        self.logger.debug('_process_message() echoing\n"""%s"""', to_echo)
        self.push(to_echo)
        # 一度に一つだけ処理するので応答を送信した後で切断する
        self.close_when_done()
