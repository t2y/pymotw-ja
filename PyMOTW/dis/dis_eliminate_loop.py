#!/usr/bin/env python
# encoding: utf-8

import operator
import itertools

class Dictionary(object):

    def __init__(self, words):
        self.by_letter = {}
        self.load_data(words)

    def load_data(self, words):
        # 文字で配置する
        grouped = itertools.groupby(words, key=operator.itemgetter(0))
        # 配置された単語セットを保存する
        self.by_letter = dict((group[0][0], group) for group in grouped)
        
