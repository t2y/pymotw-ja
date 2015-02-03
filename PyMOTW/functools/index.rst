..
    ===============================================
     functools -- Tools for Manipulating Functions
    ===============================================

=============================================
functools -- 関数を巧みに操作するためのツール
=============================================

..
    :synopsis: Tools for working with functions.

.. module:: functools
    :synopsis: 関数を操作するためのツール

..
    :Purpose: Functions that operate on other functions.
    :Available In: 2.5 and later

:目的: 他の関数に影響する関数
:利用できるバージョン: 2.5 以上

..
    The :mod:`functools` module provides tools for working with functions
    and other callable objects, to adapt or extend them for new purposes
    without completely rewriting them.

:mod:`functools` モジュールは、関数やその他の呼び出し可能オブジェクトを完全に書き換えることなく新たな目的のために適応させたり、拡張したりするために操作するツールを提供します。

..
    Decorators
    ==========

デコレータ
==========

..
    The primary tool supplied by the :mod:`functools` module is the class
    :class:`partial`, which can be used to "wrap" a callable object with
    default arguments. The resulting object is itself callable, and can be
    treated as though it is the original function.  It takes all of the
    same arguments as the original, and can be invoked with extra
    positional or named arguments as well.

:mod:`functools` モジュールが提供する主なツールは、デフォルト引数で呼び出し可能オブジェクトを "ラップ" するために使用される :class:`partial` クラスです。その結果として返されるオブジェクトはそれ自身が呼び出し可能でオリジナルの関数を経由するように扱われます。オリジナルの呼び出し可能オブジェクトと同じ全引数を受け取り、さらに追加の位置引数やキーワード引数を受け取って実行することができます。

partial
-------

..
    This example shows two simple :class:`partial` objects for the
    function :func:`myfunc`.  Notice that :func:`show_details` prints the
    :attr:`func`, :attr:`args`, and :attr:`keywords` attributes of the
    partial object.

このサンプルは :func:`myfunc` 関数のための2つのシンプルな :class:`partial` オブジェクトの説明をします。 :func:`show_details` は渡された関数 :attr:`func` 、引数 :attr:`args` と partial オブジェクトの :attr:`keywords` 属性を表示することに注目してください。

.. include:: functools_partial.py
    :literal:
    :start-after: #end_pymotw_header

..
    At the end of the example, the first :class:`partial` created is
    invoked without passing a value for *a*, causing an exception.

このサンプルの最後で、最初に作成した :class:`partial` オブジェクトの仮引数 *a* に値を渡さずに実行するので例外が発生します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'functools_partial.py', ignore_error=True, break_lines_at=70))
.. }}}

::

	$ python functools_partial.py
	
	myfunc:
		object: <function myfunc at 0x100468c08>
		__name__: myfunc
		__doc__ 'Docstring for myfunc().'
		called myfunc with: ('a', 3)
	
	partial with named default:
		object: <functools.partial object at 0x10046b050>
		__doc__ 'partial(func, *args, **keywords) - new function with partial
	 application\n    of the given arguments and keywords.\n'
		func: <function myfunc at 0x100468c08>
		args: ()
		keywords: {'b': 4}
		called myfunc with: ('default a', 4)
		called myfunc with: ('override b', 5)
	
	partial with defaults:
		object: <functools.partial object at 0x10046b0a8>
		__doc__ 'partial(func, *args, **keywords) - new function with partial
	 application\n    of the given arguments and keywords.\n'
		func: <function myfunc at 0x100468c08>
		args: ('default a',)
		keywords: {'b': 99}
		called myfunc with: ('default a', 99)
		called myfunc with: ('default a', 'override b')
	
	Insufficient arguments:
	Traceback (most recent call last):
	  File "functools_partial.py", line 49, in <module>
	    p1()
	TypeError: myfunc() takes at least 1 argument (1 given)

.. {{{end}}}



update_wrapper
--------------

..
    The partial object does not have :attr:`__name__` or :attr:`__doc__`
    attributes by default, and without those attributes decorated
    functions are more difficult to debug. Using :func:`update_wrapper`,
    copies or adds attributes from the original function to the
    :class:`partial` object.

partial オブジェクトはデフォルトで :attr:`__name__` や :attr:`__doc__` 属性を持っていません。デコレートされた関数のそういった属性をなくしてしまうことはデバッグをより難しくしてしまいます。 :func:`update_wrapper` を使用することでオリジナルの関数から :class:`partial` オブジェクトに渡された属性をコピー又は追加することができます。

.. include:: functools_update_wrapper.py
    :literal:
    :start-after: #end_pymotw_header

..
    The attributes added to the wrapper are defined in
    :const:`functools.WRAPPER_ASSIGNMENTS`, while
    :const:`functools.WRAPPER_UPDATES` lists values to be modified.

そのラッパへ追加される属性は :const:`functools.WRAPPER_ASSIGNMENTS` で定義されます。一方 :const:`functools.WRAPPER_UPDATES` は変更される値を表示します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'functools_update_wrapper.py', break_lines_at=70))
.. }}}

::

	$ python functools_update_wrapper.py
	
	myfunc:
		object: <function myfunc at 0x100468c80>
		__name__: myfunc
		__doc__ 'Docstring for myfunc().'
	
	raw wrapper:
		object: <functools.partial object at 0x10046c0a8>
		__name__: (no __name__)
		__doc__ 'partial(func, *args, **keywords) - new function with partial
	 application\n    of the given arguments and keywords.\n'
	
	Updating wrapper:
		assign: ('__module__', '__name__', '__doc__')
		update: ('__dict__',)
	
	updated wrapper:
		object: <functools.partial object at 0x10046c0a8>
		__name__: myfunc
		__doc__ 'Docstring for myfunc().'
	

.. {{{end}}}

..
    Other Callables
    ---------------

その他の呼び出し可能オブジェクト
--------------------------------

..
    Partials work with any callable object, not just standalone functions.

partial はメソッドやインスタンスも含め、どのような呼び出し可能オブジェクトでも動作します。

.. include:: functools_method.py
    :literal:
    :start-after: #end_pymotw_header

..
    This example creates partials from an instance, and methods of an
    instance.

このサンプルはインスタンスから partial やインスタンスのメソッドを作成します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'functools_method.py', break_lines_at=68))
.. }}}

::

	$ python functools_method.py
	
	meth1 straight:
		object: <bound method MyClass.meth1 of <__main__.MyClass object at 
	0x10046a3d0>>
		__name__: meth1
		__doc__ 'Docstring for meth1().'
		called meth1 with: (<__main__.MyClass object at 0x10046a3d0>, 'no d
	efault for a', 3)
	
	meth1 wrapper:
		object: <functools.partial object at 0x10046c158>
		__name__: meth1
		__doc__ 'Docstring for meth1().'
		called meth1 with: (<__main__.MyClass object at 0x10046a3d0>, 'a go
	es here', 4)
	
	meth2:
		object: <bound method MyClass.meth2 of <__main__.MyClass object at 
	0x10046a3d0>>
		__name__: meth2
		__doc__ 'Docstring for meth2'
		called meth2 with: (<__main__.MyClass object at 0x10046a3d0>, 'no d
	efault for c', 6)
	
	wrapped meth2:
		object: <functools.partial object at 0x10046c0a8>
		__name__: meth2
		__doc__ 'Docstring for meth2'
		called meth2 with: ('wrapped c', 'no default for c', 6)
	
	instance:
		object: <__main__.MyClass object at 0x10046a3d0>
		__name__: (no __name__)
		__doc__ 'Demonstration class for functools'
		called object with: (<__main__.MyClass object at 0x10046a3d0>, 'no 
	default for e', 6)
	
	instance wrapper:
		object: <functools.partial object at 0x10046c1b0>
		__name__: (no __name__)
		__doc__ 'partial(func, *args, **keywords) - new function with parti
	al application\n    of the given arguments and keywords.\n'
		called object with: (<__main__.MyClass object at 0x10046a3d0>, 'e g
	oes here', 7)

.. {{{end}}}


wraps
-----

..
    Updating the properties of a wrapped callable is especially useful
    when used in a decorator, since the transformed function ends up with
    properties of the original, "bare", function.

ラップされた呼び出し可能オブジェクトのプロパティ更新は、変換された関数が最終的にオリジナルのプロパティ、"bare"、関数になるのでデコレータで行うとかなり便利です。

.. include:: functools_wraps.py
    :literal:
    :start-after: #end_pymotw_header

..
    :mod:`functools` provides a decorator, :func:`wraps`, which applies
    :func:`update_wrapper` to the decorated function.

:mod:`functools` は :func:`wraps` という便利な関数を提供します。それはデコレートされた関数に対して :func:`update_wrapper` を適用します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'functools_wraps.py'))
.. }}}

::

	$ python functools_wraps.py
	
	myfunc:
		object: <function myfunc at 0x10046c050>
		__name__: myfunc
		__doc__ None
	
		myfunc: ('unwrapped, default b', 2)
		myfunc: ('unwrapped, passing b', 3)
	
	wrapped_myfunc:
		object: <function myfunc at 0x10046c0c8>
		__name__: myfunc
		__doc__ None
	
		decorated: ('decorated defaults', 1)
			myfunc: ('decorated defaults', 1)
		decorated: ('args to decorated', 4)
			myfunc: ('args to decorated', 4)

.. {{{end}}}

..
    Comparison
    ==========

比較
====

..
    Under Python 2, classes can define a :func:`__cmp__` method that
    returns ``-1``, ``0``, or ``1`` based on whether the object is less
    than, equal to, or greater than the item being compared.  Python 2.1
    introduces the *rich comparison* methods API, :func:`__lt__`,
    :func:`__le__`, :func:`__eq__`, :func:`__ne__`, :func:`__gt__`, and
    :func:`__ge__`, which perform a single comparison operation and return
    a boolean value.  Python 3 deprecated :func:`__cmp__` in favor of
    these new methods, so :mod:`functools` provides tools to make it
    easier to write Python 2 classes that comply with the new comparison
    requirements in Python 3.

Python 2 では、クラスは、そのオブジェクトが比較されるアイテムより小さい、等しい、大きいかに基づいて ``-1``, ``0`` または ``1`` を返す :func:`__cmp__` メソッドを定義できます。Python 2.1 では、1つの比較比較演算を実行してブーリーアン値を返す *拡張比較(rich comparison)* メソッド API である :func:`__lt__`, :func:`__le__`, :func:`__eq__`, :func:`__ne__`, :func:`__gt__` と :func:`__ge__` を導入しました。Python3 では、 :func:`__cmp__` はこれらのメソッドへ機能を引き継ぐので廃止されました。そのため :mod:`functools` モジュールは Python3 の新しい比較要求に応じた Python2 クラスを書き易くするツールを提供します。

..
    Rich Comparison
    ---------------

拡張比較(Rich Comparison)
-------------------------

..
    The rich comparison API is designed to allow classes with complex
    comparisons to implement each test in the most efficient way possible.
    However, for classes where comparison is relatively simple, there is
    no point in manually creating each of the rich comparison methods.
    The :func:`total_ordering` class decorator takes a class that provides
    some of the methods, and adds the rest of them.

拡張比較(rich comparison) API は、クラスが効率的な方法でテストを実装できるように複雑な比較を許容するように設計されています。しかし、比較が比較的シンプルなクラスのために、それぞれの拡張比較(rich comparison)メソッドを手動で作成しても意味がありません。 :func:`total_ordering` クラスデコレータは、幾つかのメソッドを提供して、そういったクラスに残りのメソッドを追加するクラスを扱います。

.. include:: functools_total_ordering.py
   :literal:
   :start-after: #end_pymotw_header

..
    The class must provide an implmentation of :func:`__eq__` and any one
    of the other rich comparison methods.  The decorator adds
    implementations of the other methods that work by using the
    comparisons provided.

クラスは :func:`__eq__` の実装とその他の拡張比較(rich comparison)メソッドのどれか1つを提供しなければなりません。デコレータは提供された比較機能を使用して動作する他のメソッドの実装を追加します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'functools_total_ordering.py'))
.. }}}

::

	$ python functools_total_ordering.py
	
	Methods:
	
	[('__eq__', <unbound method MyObject.__eq__>),
	 ('__ge__', <unbound method MyObject.__ge__>),
	 ('__gt__', <unbound method MyObject.__gt__>),
	 ('__init__', <unbound method MyObject.__init__>),
	 ('__le__', <unbound method MyObject.__le__>),
	 ('__lt__', <unbound method MyObject.__lt__>)]
	
	Comparisons:
	
	a < b :
	  testing __gt__(1, 2)
	  testing __eq__(1, 2)
	  result of a < b: True
	
	a <= b:
	  testing __gt__(1, 2)
	  result of a <= b: True
	
	a == b:
	  testing __eq__(1, 2)
	  result of a == b: False
	
	a >= b:
	  testing __gt__(1, 2)
	  testing __eq__(1, 2)
	  result of a >= b: False
	
	a > b :
	  testing __gt__(1, 2)
	  result of a > b: False

.. {{{end}}}

..
    Collation Order
    ---------------

照合順序
--------

..
    Since old-style comparison functions are deprecated in Python 3, the
    :data:`cmp` argument to functions like :func:`sort` are also no longer
    supported.  Python 2 programs that use comparison functions can use
    :func:`cmp_to_key` to convert them to a function that returns a
    *collation key*, which is used to determine the position in the final
    sequence.

旧スタイルの比較関数は Python3 で廃止されるので :func:`sort` のような関数に対する :data:`cmp` 引数も今後はサポートされません。比較関数を使用する Python2 プログラムは、 *照合キー* を返す関数に対して比較関数を変換するために :func:`cmp_to_key` を使用することができます。それは最終的なシーケンスの位置を決めるために使用されます。

.. include:: functools_cmp_to_key.py
   :literal:
   :start-after: #end_pymotw_header

.. note::
  ..
      Normally :func:`cmp_to_key` would be used directly, but in this
      example an extra wrapper function is introduced to print out more
      information as the key function is being called.

  通常 :func:`cmp_to_key` は直接使用されますが、このサンプルでは、そのキー関数が呼び出されるときにより詳細な情報を表示するために拡張ラッパ関数が提供されています。
  
..
    The output shows that :func:`sorted` starts by calling
    :func:`get_key_wrapper` for each item in the sequence to produce a
    key.  The keys returned by :func:`cmp_to_key` are instances of a class
    defined in :mod:`functools` that implements the rich comparison API
    based on the return value of the provided old-style comparison
    function.  After all of the keys are created, the sequence is sorted
    by comparing the keys.

キーを生成するためにシーケンス内の要素毎に :func:`get_key_wrapper` を呼び出すことで :func:`sorted` が開始することを出力結果が示しています。 :func:`cmp_to_key` が返すキーは、旧スタイルの比較関数で提供された返り値に基づいて拡張比較(rich comparison) API を実装する :mod:`functools` で定義されたクラスのインスタンスです。全てのキーが作成された後、そのシーケンスはその作成されたキーを比較することでソートされます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'functools_cmp_to_key.py'))
.. }}}

::

	$ python functools_cmp_to_key.py
	
	key_wrapper(MyObject(5)) -> <functools.K object at 0x100466558>
	key_wrapper(MyObject(4)) -> <functools.K object at 0x100466590>
	key_wrapper(MyObject(3)) -> <functools.K object at 0x1004665c8>
	key_wrapper(MyObject(2)) -> <functools.K object at 0x100466600>
	key_wrapper(MyObject(1)) -> <functools.K object at 0x100466638>
	comparing MyObject(4) and MyObject(5)
	comparing MyObject(3) and MyObject(4)
	comparing MyObject(2) and MyObject(3)
	comparing MyObject(1) and MyObject(2)
	MyObject(1)
	MyObject(2)
	MyObject(3)
	MyObject(4)
	MyObject(5)

.. {{{end}}}



.. seealso::

    `functools <http://docs.python.org/library/functools.html>`_
        .. The standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント
    
    `Rich comparison methods <http://docs.python.org/reference/datamodel.html#object.__lt__>`__
        .. Description of the rich comparison methods from the Python Reference Guide.

        Python リファレンスガイドの拡張比較(rich comparison)メソッドの説明
