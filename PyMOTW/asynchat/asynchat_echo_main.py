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

from asynchat_echo_server import EchoServer
from asynchat_echo_client import EchoClient

logging.basicConfig(level=logging.DEBUG,
                    format='%(name)s: %(message)s',
                    )

address = ('localhost', 0) # カーネルにポート番号を割り当てさせる
server = EchoServer(address)
ip, port = server.address # 与えられたポート番号を調べる

message_data = open('lorem.txt', 'r').read()
client = EchoClient(ip, port, message=message_data)

asyncore.loop()
