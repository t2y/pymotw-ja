#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Convert XML list of podcasts to a CSV file.
"""
#end_pymotw_header

import csv
from xml.etree.ElementTree import XMLTreeBuilder
import sys

class PodcastListToCSV(object):

    def __init__(self, outputFile):
        self.writer = csv.writer(outputFile, quoting=csv.QUOTE_NONNUMERIC)
        self.group_name = ''
        return

    def start(self, tag, attrib):
        if tag != 'outline':
            # outline 以外を無視する
            return
        if not attrib.get('xmlUrl'):
            # カレントグループを覚える
            self.group_name = attrib['text']
        else:
            # podcast エントリを出力する
            self.writer.writerow( (self.group_name, attrib['text'],
                                   attrib['xmlUrl'],
                                   attrib.get('htmlUrl', ''),
                                   )
                                  )

    def end(self, tag):
        # 閉じタグを無視する
        pass
    def data(self, data):
        # ノード内部のデータを無視する
        pass
    def close(self):
        # 特別な処理は何もしない
        return


target = PodcastListToCSV(sys.stdout)
parser = XMLTreeBuilder(target=target)
with open('podcasts.opml', 'rt') as f:
    for line in f:
        parser.feed(line)
parser.close()
