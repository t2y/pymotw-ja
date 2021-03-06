#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Random choice
"""
#end_pymotw_header

import random
import itertools

def new_deck():
    return list(itertools.product(
            itertools.chain(xrange(2, 11), ('J', 'Q', 'K', 'A')),
            ('H', 'D', 'C', 'S'),
            ))

def show_deck(deck):
    p_deck = deck[:]
    while p_deck:
        row = p_deck[:13]
        p_deck = p_deck[13:]
        for j in row:
            print '%2s%s' % j,
        print

# カードが順番に並んだ新しいデッキを取得する
deck = new_deck()
print 'Initial deck:'
show_deck(deck)

# ランダムな順番にカードをシャッフルする
random.shuffle(deck)
print '\nShuffled deck:'
show_deck(deck)

# 5つのカードのうち4つを配る
hands = [ [], [], [], [] ]

for i in xrange(5):
    for h in hands:
        h.append(deck.pop())

# 手札のカードを表示する
print '\nHands:'
for n, h in enumerate(hands):
    print '%d:' % (n+1),
    for c in h:
        print '%2s%s' % c,
    print
    
# デッキに残っているカードを表示する
print '\nRemaining deck:'
show_deck(deck)
