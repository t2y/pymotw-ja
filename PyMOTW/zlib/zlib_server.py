#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""

#__version__ = "$Id$"
#end_pymotw_header
import zlib
import logging
import SocketServer
import binascii

BLOCK_SIZE = 64

class ZlibRequestHandler(SocketServer.BaseRequestHandler):

    logger = logging.getLogger('Server')
    
    def handle(self):
        compressor = zlib.compressobj(1)
        
        # どのファイルをクライアントが要求しているかを調べる
        filename = self.request.recv(1024)
        self.logger.debug('client asked for: "%s"', filename)
        
        # 圧縮されるようにファイルのチャンクを送信する
        with open(filename, 'rb') as input:
            while True:            
                block = input.read(BLOCK_SIZE)
                if not block:
                    break
                self.logger.debug('RAW "%s"', block)
                compressed = compressor.compress(block)
                if compressed:
                    self.logger.debug('SENDING "%s"', binascii.hexlify(compressed))
                    self.request.send(compressed)
                else:
                    self.logger.debug('BUFFERING')
        
        # compressor でバッファされるデータを送信する
        remaining = compressor.flush()
        while remaining:
            to_send = remaining[:BLOCK_SIZE]
            remaining = remaining[BLOCK_SIZE:]
            self.logger.debug('FLUSHING "%s"', binascii.hexlify(to_send))
            self.request.send(to_send)
        return


if __name__ == '__main__':
    import socket
    import threading
    from cStringIO import StringIO

    logging.basicConfig(level=logging.DEBUG,
                        format='%(name)s: %(message)s',
                        )
    logger = logging.getLogger('Client')

    # サーバをセットアップして、別のスレッドで実行する
    address = ('localhost', 0) # カーネルにポートを要求する
    server = SocketServer.TCPServer(address, ZlibRequestHandler)
    ip, port = server.server_address # どのポートが与えられたかを調べる

    t = threading.Thread(target=server.serve_forever)
    t.setDaemon(True)
    t.start()

    # サーバへ接続する
    logger.info('Contacting server on %s:%s', ip, port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

    # ファイルを依頼する
    requested_file = 'lorem.txt'
    logger.debug('sending filename: "%s"', requested_file)
    len_sent = s.send(requested_file)

    # レスポンスを受け取る
    buffer = StringIO()
    decompressor = zlib.decompressobj()
    while True:
        response = s.recv(BLOCK_SIZE)
        if not response:
            break
        logger.debug('READ "%s"', binascii.hexlify(response))

        # decompressor に入力する消費されていないデータを含める
        to_decompress = decompressor.unconsumed_tail + response
        while to_decompress:
            decompressed = decompressor.decompress(to_decompress)
            if decompressed:
                logger.debug('DECOMPRESSED "%s"', decompressed)
                buffer.write(decompressed)
                # バッファオーバーフローに起因して消費されていないデータを探す
                to_decompress = decompressor.unconsumed_tail
            else:
                logger.debug('BUFFERING')
                to_decompress = None

    # decompressor バッファ内部に残っているデータを扱う
    remainder = decompressor.flush()
    if remainder:
        logger.debug('FLUSHED "%s"', remainder)
        buffer.write(reaminder)
    
    full_response = buffer.getvalue()
    lorem = open('lorem.txt', 'rt').read()
    logger.debug('response matches file contents: %s', full_response == lorem)

    # クリーンアップ
    s.close()
    server.socket.close()
