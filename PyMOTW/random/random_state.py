#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Save and restore state
"""
#end_pymotw_header

import random
import os
import cPickle as pickle

if os.path.exists('state.dat'):
    # 以前に保存された状態を復元する
    print 'Found state.dat, initializing random module'
    with open('state.dat', 'rb') as f:
        state = pickle.load(f)
    random.setstate(state)
else:
    # 良く知られた開始状態を使用する
    print 'No state.dat, seeding'
    random.seed(1)

# 乱数を生成する
for i in xrange(3):
    print '%04.3f' % random.random()

# 次回のために状態を保存する
with open('state.dat', 'wb') as f:
    pickle.dump(random.getstate(), f)

# さらに乱数を生成する
print '\nAfter saving state:'
for i in xrange(3):
    print '%04.3f' % random.random()
