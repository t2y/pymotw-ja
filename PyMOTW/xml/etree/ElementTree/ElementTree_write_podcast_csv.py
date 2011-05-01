#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Convert XML list of podcasts to a CSV file.
"""
#end_pymotw_header

import csv
from xml.etree.ElementTree import iterparse
import sys

writer = csv.writer(sys.stdout, quoting=csv.QUOTE_NONNUMERIC)

group_name = ''

for (event, node) in iterparse('podcasts.opml', events=['start']):
    if node.tag != 'outline':
        # outline 以外を無視する
        continue
    if not node.attrib.get('xmlUrl'):
        # カレントグループを覚える
        group_name = node.attrib['text']
    else:
        # podcast エントリを出力する
        writer.writerow( (group_name, node.attrib['text'],
                          node.attrib['xmlUrl'],
                          node.attrib.get('htmlUrl', ''),
                          )
                         )
