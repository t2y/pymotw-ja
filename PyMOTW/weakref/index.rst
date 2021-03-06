..
    ====================================================
    weakref -- Garbage-collectable references to objects
    ====================================================

=======================================================
weakref -- オブジェクトのガベージコレクション可能な参照
=======================================================

..
    :synopsis: Refer to an "expensive" object, but allow it to be garbage collected if there are no other non-weak references.

.. module:: weakref
    :synopsis: "巨大な" オブジェクトを参照して、他に非弱参照のオブジェクトがない場合にガベージコレクションの対象にする

..
    :Purpose: Refer to an "expensive" object, but allow it to be garbage collected if there are no other non-weak references.
    :Available In: Since 2.1

:目的: "巨大な" オブジェクトを参照して、他に非弱参照のオブジェクトがない場合にガベージコレクションの対象にする
:利用できるバージョン: 2.1 以上

..
    The :mod:`weakref` module supports weak references to objects. A
    normal reference increments the reference count on the object and
    prevents it from being garbage collected. This is not always
    desirable, either when a circular reference might be present or when
    building a cache of objects that should be deleted when memory is
    needed.

:mod:`weakref` モジュールは、オブジェクトに対する弱参照をサポートします。通常の参照は、オブジェクトの参照カウンタを増加させて、そのオブジェクトがガベージコレクタの対象にならないようにします。これは必ずしも望ましいことではありません。例えば、循環参照が存在するとき、またはメモリが必要なときに削除すべきオブジェクトのキャッシュを作るとき等です。

..
    References
    ==========

参照
====

..
    Weak references to your objects are managed through the :class:`ref`
    class. To retrieve the original object, call the reference object.

オブジェクトに対する弱参照は :class:`ref` クラスを通して管理します。元のオブジェクトを取得するには、参照オブジェクトを呼び出します。

.. include:: weakref_ref.py
    :literal:
    :start-after: #end_pymotw_header

..
    In this case, since ``obj`` is deleted before the second call to the
    reference, the :class:`ref` returns ``None``.

この場合、 ``obj`` は2回目の参照オブジェクトの呼び出し前に削除されるので :class:`ref` は ``None`` を返します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'weakref_ref.py'))
.. }}}

::

	$ python weakref_ref.py
	
	obj: <__main__.ExpensiveObject object at 0x10046d410>
	ref: <weakref at 0x100467838; to 'ExpensiveObject' at 0x10046d410>
	r(): <__main__.ExpensiveObject object at 0x10046d410>
	deleting obj
	(Deleting <__main__.ExpensiveObject object at 0x10046d410>)
	r(): None

.. {{{end}}}

..
    Reference Callbacks
    ===================

参照コールバック
================

..
    The :class:`ref` constructor takes an optional second argument that
    should be a callback function to invoke when the referenced object is
    deleted.

:class:`ref` コンストラクタは、オプションで2番目の引数に参照されるオブジェクトが削除されたときに実行するコールバック関数を取ります。

.. include:: weakref_ref_callback.py
    :literal:
    :start-after: #end_pymotw_header

..
    The callback receives the reference object as an argument, after the
    reference is "dead" and no longer refers to the original object. This
    lets you remove the weak reference object from a cache, for example.

このコールバック関数は、元のオブジェクトに対する参照ではなくその参照が "dead" になった後で、引数として参照オブジェクトを受け取ります。例えば、これはキャッシュから弱参照オブジェクトを削除させます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'weakref_ref_callback.py'))
.. }}}

::

	$ python weakref_ref_callback.py
	
	obj: <__main__.ExpensiveObject object at 0x10046c610>
	ref: <weakref at 0x100468890; to 'ExpensiveObject' at 0x10046c610>
	r(): <__main__.ExpensiveObject object at 0x10046c610>
	deleting obj
	callback( <weakref at 0x100468890; dead> )
	(Deleting <__main__.ExpensiveObject object at 0x10046c610>)
	r(): None

.. {{{end}}}

..
    Proxies
    =======

プロキシ
========

..
    Instead of using :class:`ref` directly, it can be more convenient to
    use a proxy.  Proxies can be used as though they were the original
    object, so you do not need to call the :class:`ref` first to access
    the object.

直接 :class:`ref` を使用する代わりに、プロキシを使用する方がもっと便利です。プロキシは元のオブジェクトを扱うように使用できるので、そのオブジェクトへアクセスする前に :class:`ref` を呼び出す必要はありません。

.. include:: weakref_proxy.py
    :literal:
    :start-after: #end_pymotw_header

..
    If the proxy is access after the referent object is removed, a
    :class:`ReferenceError` exception is raised.

参照されたオブジェクトが削除された後でこのプロキシにアクセスすると、 :class:`ReferenceError` 例外が発生します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'weakref_proxy.py', ignore_error=True))
.. }}}

::

	$ python weakref_proxy.py
	
	via obj: My Object
	via ref: My Object
	via proxy: My Object
	(Deleting <__main__.ExpensiveObject object at 0x10046b490>)
	via proxy:
	Traceback (most recent call last):
	  File "weakref_proxy.py", line 26, in <module>
	    print 'via proxy:', p.name
	ReferenceError: weakly-referenced object no longer exists

.. {{{end}}}

..
    Cyclic References
    =================

循環参照
========

..
    One use for weak references is to allow cyclic references without preventing
    garbage collection. This example illustrates the difference between using
    regular objects and proxies when a graph includes a cycle.

弱参照の使用法の1つは、ガベージコレクションを妨げずに循環参照できることです。このサンプルは、循環するグラフを含むときに普通のオブジェクトとプロキシを使用することの違いを説明します。

..
    First, we need a :class:`Graph` class that accepts any object given to
    it as the "next" node in the sequence. For the sake of brevity, this
    :class:`Graph` supports a single outgoing reference from each node,
    which results in boring graphs but makes it easy to create cycles. The
    function :func:`demo()` is a utility function to exercise the graph
    class by creating a cycle and then removing various references.

まずシーケンスの "次" ノードとして渡された任意のオブジェクトをもつ :class:`Graph` クラスが必要です。簡単にするために、この :class:`Graph` は、各ノードから1つの外向きの参照をサポートします。つまらないグラフですが、簡単に循環参照を作成します。関数 :func:`demo()` は、循環参照を作成した後で様々な参照を削除することで、グラフのクラスにアクセスするユーテリティ関数です。

.. include:: weakref_graph.py
   :literal:
   :start-after: #end_pymotw_header

..
    Now we can set up a test program using the :mod:`gc` module to help us
    debug the leak. The ``DEBUG_LEAK`` flag causes :mod:`gc` to print
    information about objects that cannot be seen other than through the
    reference the garbage collector has to them.

ここでメモリリークをデバッグするときに便利な :mod:`gc` モジュールを使用したテストプログラムがあります。 ``DEBUG_LEAK`` フラグは、 :mod:`gc` モジュールを経由しないと見れないガベージコレクタがもつ参照先であるオブジェクトに関する情報を表示します。

.. include:: weakref_cycle.py
   :literal:
   :start-after: #end_pymotw_header

..
    Even after deleting the local references to the :class:`Graph`
    instances in :func:`demo()`, the graphs all show up in the garbage
    list and cannot be collected.  The dictionaries in the garbage list
    hold the attributes of the :class:`Graph` instances. We can forcibly
    delete the graphs, since we know what they are:

:func:`demo()` で :class:`Graph` インスタンスに対するローカル参照を削除した後でさえ、そのグラフはガベージリストに表示されて、ガベージコレクションされません。このガベージリストのディクショナリは、 :class:`Graph` インスタンスの属性を保持します。このグラフはそれが何なのかを知っているので強制的に削除できます。

.. {{{cog
.. cog.out(run_script(cog.inFile, '-u weakref_cycle.py'))
.. }}}

::

	$ python -u weakref_cycle.py
	
	Setting up the cycle
	
	Set up graph:
	one.set_next(two (<class 'weakref_graph.Graph'>))
	two.set_next(three (<class 'weakref_graph.Graph'>))
	three.set_next(one->two->three (<class 'weakref_graph.Graph'>))
	
	Graphs:
	one->two->three->one
	two->three->one->two
	three->one->two->three
	Collecting...
	Unreachable objects: 0
	Garbage:[]
	
	After 2 references removed:
	one->two->three->one
	Collecting...
	Unreachable objects: 0
	Garbage:[]
	
	Removing last reference:
	Collecting...
	gc: uncollectable <Graph 0x10046ff50>
	gc: uncollectable <Graph 0x10046ff90>
	gc: uncollectable <Graph 0x10046ffd0>
	gc: uncollectable <dict 0x100363060>
	gc: uncollectable <dict 0x100366460>
	gc: uncollectable <dict 0x1003671f0>
	Unreachable objects: 6
	Garbage:[Graph(one),
	 Graph(two),
	 Graph(three),
	 {'name': 'one', 'other': Graph(two)},
	 {'name': 'two', 'other': Graph(three)},
	 {'name': 'three', 'other': Graph(one)}]
	
	Breaking the cycle and cleaning up garbage
	
	one.set_next(None (<type 'NoneType'>))
	(Deleting two)
	two.set_next(None (<type 'NoneType'>))
	(Deleting three)
	three.set_next(None (<type 'NoneType'>))
	(Deleting one)
	one.set_next(None (<type 'NoneType'>))
	
	Collecting...
	Unreachable objects: 0
	Garbage:[]

.. {{{end}}}

..
    And now let's define a more intelligent :class:`WeakGraph` class that
    knows not to create cycles using regular references, but to use a
    :class:`ref` when a cycle is detected.

今度は普通の参照を使用して循環参照を作成しないもっと賢い :class:`WeakGraph` クラスを定義しましょう。しかし、循環参照が削除されるときは :class:`ref` を使用します。

.. include:: weakref_weakgraph.py
   :literal:
   :start-after: #end_pymotw_header

..
    Since the :class:`WeakGraph` instances use proxies to refer to objects
    that have already been seen, as :func:`demo()` removes all local
    references to the objects, the cycle is broken and the garbage
    collector can delete the objects for us.

:class:`WeakGraph` インスタンスは、既に見たことがあるオブジェクトを参照するためにプロキシを使用するので、 :func:`demo()` がこのオブジェクトの全てのローカル属性を削除して、循環参照が壊れて、ガベージコレクタはこのオブジェクトを削除します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'weakref_weakgraph.py'))
.. }}}

::

	$ python weakref_weakgraph.py
	
	Set up graph:
	one.set_next(two (<class '__main__.WeakGraph'>))
	two.set_next(three (<class '__main__.WeakGraph'>))
	three.set_next(one->two->three (<type 'weakproxy'>))
	
	Graphs:
	one->two->three
	two->three->one->two
	three->one->two->three
	Collecting...
	Unreachable objects: 0
	Garbage:[]
	
	After 2 references removed:
	one->two->three
	Collecting...
	Unreachable objects: 0
	Garbage:[]
	
	Removing last reference:
	(Deleting one)
	one.set_next(None (<type 'NoneType'>))
	(Deleting two)
	two.set_next(None (<type 'NoneType'>))
	(Deleting three)
	three.set_next(None (<type 'NoneType'>))
	Collecting...
	Unreachable objects: 0
	Garbage:[]

.. {{{end}}}

..
    Caching Objects
    ===============

キャッシュオブジェクト
======================

..
    The :class:`ref` and :class:`proxy` classes are considered "low
    level". While they are useful for maintaining weak references to
    individual objects and allowing cycles to be garbage collected, if you
    need to create a cache of several objects the
    :class:`WeakKeyDictionary` and :class:`WeakValueDictionary` provide a
    more appropriate API.

:class:`ref` と :class:`proxy` クラスは "低レベル" なものと考えられます。そういったクラスが個々のオブジェクトに対する弱参照を保持して循環参照をガベージコレクションできるものの、オブジェクトのキャッシュを作成する必要があるなら、 :class:`WeakKeyDictionary` と :class:`WeakValueDictionary` がもっと適切な API を提供します。

..
    As you might expect, the :class:`WeakValueDictionary` uses weak
    references to the values it holds, allowing them to be garbage
    collected when other code is not actually using them.

期待通り、 :class:`WeakValueDictionary` は保持するオブジェクトに対する弱参照を使用します。そして、別のコードが実際にそういったオブジェクトを使用しないときにガベージコレクションできるようにします。

..
    To illustrate the difference between memory handling with a regular
    dictionary and :class:`WeakValueDictionary`, let's go experiment with
    explicitly calling the garbage collector again:

普通のディクショナリと :class:`WeakValueDictionary` を使用することでメモリ操作の違いを説明するために、再度ガベージコレクタを呼び出して実験してみましょう。

.. include:: weakref_valuedict.py
    :literal:
    :start-after: #end_pymotw_header

..
    Notice that any loop variables that refer to the values we are caching must be
    cleared explicitly to decrement the reference count on the object. Otherwise
    the garbage collector would not remove the objects and they would remain in
    the cache. Similarly, the all_refs variable is used to hold references to
    prevent them from being garbage collected prematurely.

キャッシュしている値を参照する任意のループ変数は、そのオブジェクトの参照カウンタを減らすために明示的にクリアしなければならないことに注意してください。それ以外は、ガベージコレクタはそのオブジェクトを削除せずにキャッシュに残ったままになります。同様に ``all_ref`` 変数は、途中でガベージコレクションされないようにそのオブジェクトに対する参照を保持するために使用されます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'weakref_valuedict.py'))
.. }}}

::

	$ python weakref_valuedict.py
	
	CACHE TYPE: <type 'dict'>
	all_refs ={'one': ExpensiveObject(one),
	 'three': ExpensiveObject(three),
	 'two': ExpensiveObject(two)}
	Before, cache contains: ['three', 'two', 'one']
	  three = ExpensiveObject(three)
	  two = ExpensiveObject(two)
	  one = ExpensiveObject(one)
	Cleanup:
	After, cache contains: ['three', 'two', 'one']
	  three = ExpensiveObject(three)
	  two = ExpensiveObject(two)
	  one = ExpensiveObject(one)
	demo returning
	(Deleting ExpensiveObject(three))
	(Deleting ExpensiveObject(two))
	(Deleting ExpensiveObject(one))
	
	CACHE TYPE: weakref.WeakValueDictionary
	all_refs ={'one': ExpensiveObject(one),
	 'three': ExpensiveObject(three),
	 'two': ExpensiveObject(two)}
	Before, cache contains: ['three', 'two', 'one']
	  three = ExpensiveObject(three)
	  two = ExpensiveObject(two)
	  one = ExpensiveObject(one)
	Cleanup:
	(Deleting ExpensiveObject(three))
	(Deleting ExpensiveObject(two))
	(Deleting ExpensiveObject(one))
	After, cache contains: []
	demo returning

.. {{{end}}}

..
    The WeakKeyDictionary works similarly but uses weak references for the keys
    instead of the values in the dictionary.

:class:`WeakKeyDictionary` は同様に動作しますが、ディクショナリの値ではなく、キーの弱参照を使用します。

..
    The library documentation for weakref contains this warning:

:mod:`weakref` の標準ライブラリドキュメントには次の警告があります。

.. warning::

    .. Caution: Because a WeakValueDictionary is built on top of a Python
       dictionary, it must not change size when iterating over it. This can be
       difficult to ensure for a WeakValueDictionary because actions performed by
       the program during iteration may cause items in the dictionary to vanish
       "by magic" (as a side effect of garbage collection).

    注意: :class:`WeakValueDictionary` は Python のディクショナリの上で作成されるので、繰り返し処理するときにサイズを変更してはいけません。 :class:`WeakValueDictionary` が繰り返し処理されるとき、プログラムが行うアクションがディクショナリの要素を (ガベージコレクションの副作用として) "魔法のように" 消してしまう可能性があるので、サイズ変更を保証するのが難しくなります。

.. seealso::

    `weakref <http://docs.python.org/lib/module-weakref.html>`_
        .. Standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント

    :mod:`gc`
        .. The gc module is the interface to the interpreter's garbage collector.

        インタープリタのガベージコレクタのインタフェース
