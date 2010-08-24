..
    =====================================================================
    functools -- Tools for making decorators and other function wrappers.
    =====================================================================

=============================================================
functools -- デコレータを作るためのツールとその他の関数ラッパ
=============================================================

..
    :synopsis: Tools for making decorators and other function wrappers.

.. module:: functools
    :synopsis: デコレータを作るためのツールとその他の関数ラッパ

..
    :Purpose: 
        The functools module includes tools for wrapping functions and other
        callable objects.
    :Python Version: new in 2.5

:目的: functools モジュールは関数やその他の呼び出し可能オブジェクトをラップするためのツールを提供します
:Python バージョン: 2.5 で新規追加

..
    The primary tool supplied by the functools module is the class
    ``partial``, which can be used to "wrap" a callable with default
    arguments. The resulting object is itself callable and can be treated
    as though it is the original function.  It takes all of the same
    arguments as the original callable and can be invoked with extra
    positional or named arguments as well.

functools モジュールで提供される主なツールは、デフォルト引数で呼び出し可能オブジェクトを "ラップ" するために使用される ``partial`` クラスです。その結果として返されるオブジェクトはそれ自身が呼び出し可能でオリジナルの関数を経由するように扱われます。オリジナルの呼び出し可能オブジェクトと同じ全ての引数を取り、さらに追加の位置引数やキーワード引数を受け取って実行することができます。

partial
=======

..
    This example shows two simple partial objects for the function
    ``myfunc()``.  Notice that ``show_details()`` prints the func, args,
    and keywords attributes of the partial object.

このサンプルは ``myfunc()`` 関数のために2つの単純な partial オブジェクトの説明をします。 ``show_details()`` は渡された関数、その引数と partial オブジェクトの keywords 属性を表示することに注目してください。

.. include:: functools_partial.py
    :literal:
    :start-after: #end_pymotw_header

..
    At the end of the example, the first partial created is invoked without
    passing a value for *a*, causing an exception.

このサンプルの最後で、最初に作成した partial オブジェクトの仮引数 *a* に値を渡さずに実行するので例外が発生します。

::

	$ python functools_partial.py
	myfunc:
		object: <function myfunc at 0x822b0>
		__name__: myfunc
		__doc__ 'Docstring for myfunc().'
		called myfunc with: ('a', 3)
	
	partial with named default:
		object: <functools.partial object at 0x880f0>
		__doc__ 'partial(func, *args, **keywords) - new function with partial application\n\tof the given arguments and keywords.\n'
		func: <function myfunc at 0x822b0>
		args: ()
		keywords: {'b': 4}
		called myfunc with: ('default a', 4)
		called myfunc with: ('override b', 5)
	
	partial with defaults:
		object: <functools.partial object at 0x88120>
		__doc__ 'partial(func, *args, **keywords) - new function with partial application\n\tof the given arguments and keywords.\n'
		func: <function myfunc at 0x822b0>
		args: ('default a',)
		keywords: {'b': 99}
		called myfunc with: ('default a', 99)
		called myfunc with: ('default a', 'override b')
	
	Insufficient arguments:
	Traceback (most recent call last):
	  File "functools_partial.py", line 49, in <module>
	    p1()
	TypeError: myfunc() takes at least 1 non-keyword argument (0 given)


update_wrapper
==============

..
    The partial object does not have ``__name__`` or ``__doc__``
    attributes by default. Losing those attributes for decorated functions
    makes them more difficult to debug. By using ``update_wrapper``, you
    can copy or add attributes from the original function to the partial
    object.

partial オブジェクトはデフォルトで ``__name__`` や ``__doc__`` 属性を持っていません。デコレートされた関数のそういった属性をなくしてしまうことはデバッグをより難しくしてしまいます。 ``update_wrapper`` を使用することでオリジナルの関数から partial オブジェクトに渡された属性をコピー又は追加することができます。

.. include:: functools_update_wrapper.py
    :literal:
    :start-after: #end_pymotw_header

..
    The attributes added to the wrapper are defined in
    ``functools.WRAPPER_ASSIGNMENTS``, while ``functools.WRAPPER_UPDATES``
    lists values to be modified.

そのラッパへ追加される属性は ``functools.WRAPPER_ASSIGNMENTS`` で定義されます。一方 ``functools.WRAPPER_UPDATES`` は変更される値を表示します。

::

	$ python functools_update_wrapper.py
	myfunc:
		object: <function myfunc at 0x82230>
		__name__: myfunc
		__doc__ 'Docstring for myfunc().'
	
	raw wrapper:
		object: <functools.partial object at 0x7bfc0>
		__name__: (no __name__)
		__doc__ 'partial(func, *args, **keywords) - new function with partial application\n\tof the given arguments and keywords.\n'
	
	Updating wrapper:
		assign: ('__module__', '__name__', '__doc__')
		update: ('__dict__',)
	
	updated wrapper:
		object: <functools.partial object at 0x7bfc0>
		__name__: myfunc
		__doc__ 'Docstring for myfunc().'

..
    Methods and Other Callables
    ===========================

メソッドとその他の呼び出し可能オブジェクト
==========================================

..
    Partials work with any callable object, including methods and instances.

partial はメソッドやインスタンスも含め、どのような呼び出し可能オブジェクトでも動作します。

.. include:: functools_method.py
    :literal:
    :start-after: #end_pymotw_header

::

	$ python functools_method.py
	meth1 straight:
		object: <bound method MyClass.meth1 of <__main__.MyClass object at 0x85b10>>
		__name__: meth1
		__doc__ 'Docstring for meth1().'
		called meth1 with: (<__main__.MyClass object at 0x85b10>, 'no default for a', 3)
	
	meth1 wrapper:
		object: <functools.partial object at 0x88300>
		__name__: meth1
		__doc__ 'Docstring for meth1().'
		called meth1 with: (<__main__.MyClass object at 0x85b10>, 'a goes here', 4)
	
	meth2:
		object: <bound method MyClass.meth2 of <__main__.MyClass object at 0x85b10>>
		__name__: meth2
		__doc__ 'Docstring for meth2'
		called meth2 with: (<__main__.MyClass object at 0x85b10>, 'no default for c', 6)
	
	wrapped meth2:
		object: <functools.partial object at 0x88270>
		__name__: meth2
		__doc__ 'Docstring for meth2'
		called meth2 with: ('wrapped c', 'no default for c', 6)
	
	instance:
		object: <__main__.MyClass object at 0x85b10>
		__name__: (no __name__)
		__doc__ 'Demonstration class for functools'
		called object with: (<__main__.MyClass object at 0x85b10>, 'no default for e', 6)
	
	instance wrapper:
		object: <functools.partial object at 0x88330>
		__name__: (no __name__)
		__doc__ 'partial(func, *args, **keywords) - new function with partial application\n\tof the given arguments and keywords.\n'
		called object with: (<__main__.MyClass object at 0x85b10>, 'e goes here', 7)

wraps
=====

..
    Updating the properties of a wrapped callable is especially useful
    when used in a decorator, since the decorated function ends up with
    properties of the original, "raw", function. :mod:`functools` provides
    a convenience function, ``wraps()``, to be used as a decorator itself
    and to apply ``update_wrapper()`` automatically.

ラップされた呼び出し可能オブジェクトのプロパティ更新は、decorated 関数が最終的にオリジナルの "raw" 関数のプロパティになるのでデコレータで行うとかなり便利です。 :mod:`functools` は ``wraps()`` という便利な関数を提供します。それはデコレータのように使用されて自動的に ``update_wrapper()`` を適用します。

.. include:: functools_wraps.py
    :literal:
    :start-after: #end_pymotw_header

::

	$ python functools_wraps.py
	myfunc:
		object: <function myfunc at 0x82330>
		__name__: myfunc
		__doc__ None
	
		myfunc: ('unwrapped, default b', 2)
		myfunc: ('unwrapped, passing b', 3)
	
	wrapped_myfunc:
		object: <function myfunc at 0x82370>
		__name__: myfunc
		__doc__ None
	
		decorated: ('decorated defaults', 1)
			myfunc: ('decorated defaults', 1)
		decorated: ('args to decorated', 4)
			myfunc: ('args to decorated', 4)

.. seealso::

    `functools <http://docs.python.org/library/functools.html>`_
        .. The standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント
