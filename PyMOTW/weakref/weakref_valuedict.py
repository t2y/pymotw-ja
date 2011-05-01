#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Demonstrate WeakValueDictionary.
"""
#end_pymotw_header

import gc
from pprint import pprint
import weakref

gc.set_debug(gc.DEBUG_LEAK)

class ExpensiveObject(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'ExpensiveObject(%s)' % self.name
    def __del__(self):
        print '(Deleting %s)' % self
        
def demo(cache_factory):
    # オブジェクトを保持して
    # 全ての弱参照がすぐに削除されないようにする
    all_refs = {}
    # 渡されたファクトリを使用するキャッシュ
    print 'CACHE TYPE:', cache_factory
    cache = cache_factory()
    for name in [ 'one', 'two', 'three' ]:
        o = ExpensiveObject(name)
        cache[name] = o
        all_refs[name] = o
        del o # 参照カウンタを減らす

    print 'all_refs =',
    pprint(all_refs)
    print 'Before, cache contains:', cache.keys()
    for name, value in cache.items():
        print '  %s = %s' % (name, value)
        del value # decref
        
    # キャッシュを除く全てのオブジェクトに対する参照を削除
    print 'Cleanup:'
    del all_refs
    gc.collect()

    print 'After, cache contains:', cache.keys()
    for name, value in cache.items():
        print '  %s = %s' % (name, value)
    print 'demo returning'
    return

demo(dict)
print
demo(weakref.WeakValueDictionary)
