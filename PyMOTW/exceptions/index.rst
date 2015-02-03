..
    ====================================
    exceptions -- Built-in error classes
    ====================================

====================================
exceptions -- ビルトインエラークラス
====================================

..
    :synopsis: ビルトインエラークラス

.. module:: exceptions
    :synopsis: ビルトインエラークラス

..
    :Purpose: The exceptions module defines the built-in errors used throughout the standard library and by the interpreter.
    :Available In: 1.5 and later

:目的: 例外モジュールはインタープリタや標準ライブラリで使用されるビルトインエラーを定義する
:利用できるバージョン: 1.5 以上

..
    Description
    ===========

説明
====

..
    In the past, Python has supported simple string messages as exceptions as well as classes.  Since 1.5, all of the standard library modules use classes for exceptions.  Starting with Python 2.5, string exceptions result in a DeprecationWarning, and support for string exceptions will be removed in the future.

これまでに Python はクラス同様に例外として単純な文字列のメッセージに対応していました。Python 1.5 以降、全ての標準ライブラリモジュールはクラス例外を使用します。Python 2.5 を使用すると文字列例外は DeprecationWarning を発生させます。そして、文字列例外のサポートは今後廃止される予定です。

..
    Base Classes
    ============

ベースクラス
============

..
    The exception classes are defined in a hierarchy, described in the standard library documentation.  In addition to the obvious organizational benefits, exception inheritance is useful because related exceptions can be caught by catching their base class.  In most cases, these base classes are not intended to be raised directly.

例外クラスは階層構造で定義されていて、標準ライブラリドキュメントに説明があります。明らかな階層化の利点に加えて、継承された例外のベースクラスを捕捉することで関連する例外をまとめて捕捉できるので例外の継承は役に立ちます。大半のケースでは、ベースクラスは直接発生させることを目的としていません。

BaseException
-------------

..
    Base class for all exceptions.  Implements logic for creating a string 
    representation of the exception using str() from the arguments passed 
    to the constructor.

全ての例外のベースクラスです。そのコンストラクタへ渡される引数から str() を使用してその例外の説明メッセージを作成するロジックを実装してください。

Exception
---------

..
    Base class for exceptions that do not result in quitting the running application.
    All user-defined exceptions should use Exception as a base class.

実行中のアプリケーションを終了させない例外のためのベースクラスです。全てのユーザ定義の例外はベースクラスとして Exception を使用すべきです。

StandardError
-------------

..
    Base class for built-in exceptions used in the standard library.

ビルトイン例外のベースクラスは標準ライブラリで使用されます。

ArithmeticError
---------------

..
    Base class for math-related errors.

数値関連のエラーのためのベースクラスです。

LookupError
-----------

..
    Base class for errors raised when something can't be found.

何かを発見したときに発生させるエラーのベースクラスです。

EnvironmentError
----------------

..
    Base class for errors that come from outside of Python (the operating
    system, filesystem, etc.).

Python の外部(オペレーティングシステム、ファイルシステム等)から発生するエラーのためのベースクラスです。

..
    Raised Exceptions
    =================

例外を発生させる
================

.. _exceptions-AssertionError:

AssertionError
--------------

..
    An AssertionError is raised by a failed ``assert`` statement.  

``assert`` 文が失敗したときに AssertionError が発生します。

.. include:: exceptions_AssertionError_assert.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'exceptions_AssertionError_assert.py', ignore_error=True))
.. }}}

::

	$ python exceptions_AssertionError_assert.py
	
	Traceback (most recent call last):
	  File "exceptions_AssertionError_assert.py", line 12, in <module>
	    assert False, 'The assertion failed'
	AssertionError: The assertion failed

.. {{{end}}}

..
    It is also used in the :mod:`unittest` module in methods like ``failIf()``.

``failIf()`` のようなメソッドで :mod:`unittest` モジュールでも使用されます。

.. include:: exceptions_AssertionError_unittest.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'exceptions_AssertionError_unittest.py', ignore_error=True))
.. }}}

::

	$ python exceptions_AssertionError_unittest.py
	
	F
	======================================================================
	FAIL: test (__main__.AssertionExample)
	----------------------------------------------------------------------
	Traceback (most recent call last):
	  File "exceptions_AssertionError_unittest.py", line 17, in test
	    self.failUnless(False)
	AssertionError: False is not true
	
	----------------------------------------------------------------------
	Ran 1 test in 0.000s
	
	FAILED (failures=1)

.. {{{end}}}

.. _exceptions-AttributeError:

AttributeError
--------------

..
    When an attribute reference or assignment fails, AttributeError is
    raised.  For example, when trying to reference an attribute that does
    not exist:

属性の参照か割り当てが失敗したときに AttributeError が発生します。例えば、存在しない属性を参照しようとしたときに発生します。

.. include:: exceptions_AttributeError.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'exceptions_AttributeError.py', ignore_error=True))
.. }}}

::

	$ python exceptions_AttributeError.py
	
	Traceback (most recent call last):
	  File "exceptions_AttributeError.py", line 16, in <module>
	    print o.attribute
	AttributeError: 'NoAttributes' object has no attribute 'attribute'

.. {{{end}}}

..
    Or when trying to modify a read-only attribute:

又は読み込み専用属性を変更しようとしたときに発生します。

.. include:: exceptions_AttributeError_assignment.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'exceptions_AttributeError_assignment.py', ignore_error=True))
.. }}}

::

	$ python exceptions_AttributeError_assignment.py
	
	This is the attribute value
	Traceback (most recent call last):
	  File "exceptions_AttributeError_assignment.py", line 20, in <module>
	    o.attribute = 'New value'
	AttributeError: can't set attribute

.. {{{end}}}


EOFError
--------

..
    An EOFError is raised when a built-in function like ``input()`` or
    ``raw_input()`` do not read any data before encountering the end of
    their input stream.  The file methods like ``read()`` return an empty
    string at the end of the file.

``input()`` 又は ``raw_input()`` のようなビルトイン関数が入力ストリームの最後に遭遇する前にデータを読み込めないときに EOFError が発生します。 ``read()`` のような file メソッドはファイルの最後で空文字列を返します。

.. include:: exceptions_EOFError.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ echo hello | python PyMOTW/exceptions/exceptions_EOFError.py
    prompt:READ: hello
    prompt:Traceback (most recent call last):
      File "PyMOTW/exceptions/exceptions_EOFError.py", line 13, in <module>
        data = raw_input('prompt:')
    EOFError: EOF when reading a line


FloatingPointError
------------------

..
    Raised by floating point operations that result in errors, when
    floating point exception control (fpectl) is turned on.  Enabling
    :mod:`fpectl` requires an interpreter compiled with the
    ``--with-fpectl`` flag.  Using :mod:`fpectl` is `discouraged in the
    stdlib docs <http://docs.python.org/lib/module-fpectl.html>`_.

浮動小数点例外制御(fpectl)がオンのとき、最終的にエラーを引き起こす浮動小数点の操作で発生します。 :mod:`fpectl` を有効にするには ``--with-fpectl`` フラグをセットしてコンパイルされたインタープリタが必要です。 :mod:`fpectl` を使用することは `標準ライブラリドキュメントでは推奨されていません <http://docs.python.org/lib/module-fpectl.html>`_ 。

.. include:: exceptions_FloatingPointError.py
    :literal:
    :start-after: #end_pymotw_header


GeneratorExit
-------------

..
    Raised inside a generator the generator's ``close()`` method is called.

ジェネレータの ``close()`` メソッドが呼ばれるときにジェネレータ内部で発生します。

.. include:: exceptions_GeneratorExit.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'exceptions_GeneratorExit.py'))
.. }}}

::

	$ python exceptions_GeneratorExit.py
	
	Yielding 0
	0
	Exiting early

.. {{{end}}}

.. _exceptions-IOError:

IOError
-------

..
    Raised when input or output fails, for example if a disk fills up or
    an input file does not exist.

入力や出力が失敗するときに発生します。例えば、ディスクがいっぱいだったり、入力ファイルが存在しないときに発生します。

.. include:: exceptions_IOError.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'exceptions_IOError.py', ignore_error=True))
.. }}}

::

	$ python exceptions_IOError.py
	
	Traceback (most recent call last):
	  File "exceptions_IOError.py", line 12, in <module>
	    f = open('/does/not/exist', 'r')
	IOError: [Errno 2] No such file or directory: '/does/not/exist'

.. {{{end}}}

.. _exceptions-ImportError:

ImportError
-----------

..
    Raised when a module, or member of a module, cannot be imported.
    There are a few conditions where an ImportError might be raised.

あるモジュール、又はモジュールのメンバがインポートできないときに発生します。ImportError が発生する個所には複数の条件があります。

..
    1. If a module does not exist.

1. モジュールが存在しない場合

.. include:: exceptions_ImportError_nomodule.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'exceptions_ImportError_nomodule.py', ignore_error=True))
.. }}}

::

	$ python exceptions_ImportError_nomodule.py
	
	Traceback (most recent call last):
	  File "exceptions_ImportError_nomodule.py", line 12, in <module>
	    import module_does_not_exist
	ImportError: No module named module_does_not_exist

.. {{{end}}}

..
    2. If ``from X import Y`` is used and Y cannot be found inside the
    module X, an ImportError is raised.

2. ``from X import Y`` が使用されてモジュール X の内部で Y が見つからなかった場合

.. include:: exceptions_ImportError_missingname.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'exceptions_ImportError_missingname.py', ignore_error=True))
.. }}}

::

	$ python exceptions_ImportError_missingname.py
	
	Traceback (most recent call last):
	  File "exceptions_ImportError_missingname.py", line 12, in <module>
	    from exceptions import MadeUpName
	ImportError: cannot import name MadeUpName

.. {{{end}}}


IndexError
----------

..
    An IndexError is raised when a sequence reference is out of range.

IndexError はシーケンスの範囲外を参照したときに発生します。

.. include:: exceptions_IndexError.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'exceptions_IndexError.py', ignore_error=True))
.. }}}

::

	$ python exceptions_IndexError.py
	
	Traceback (most recent call last):
	  File "exceptions_IndexError.py", line 13, in <module>
	    print my_seq[3]
	IndexError: list index out of range

.. {{{end}}}

.. _exceptions-KeyError:

KeyError
--------

..
    Similarly, a KeyError is raised when a value is not found as a key of a dictionary.

同様に KeyError は辞書のキーが見つからなかったときに発生します。

.. include:: exceptions_KeyError.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'exceptions_KeyError.py', ignore_error=True))
.. }}}

::

	$ python exceptions_KeyError.py
	
	Traceback (most recent call last):
	  File "exceptions_KeyError.py", line 13, in <module>
	    print d['c']
	KeyError: 'c'

.. {{{end}}}

.. _exceptions-KeyboardInterrupt:

KeyboardInterrupt
-----------------

..
    A KeyboardInterrupt occurs whenever the user presses Ctrl-C (or
    Delete) to stop a running program.  Unlike most of the other
    exceptions, KeyboardInterrupt inherits directly from BaseException to
    avoid being caught by global exception handlers that catch Exception.

ユーザが実行中のプログラムを停止するために Ctrl-C (又は Delete) を押下すると KeyboardInterrupt が発生します。その他のほとんどの例外と違い、Exception を捕捉するグローバルな例外ハンドラによって捕捉されないように KeyboardInterrupt は BaseException から直接継承します。

.. include:: exceptions_KeyboardInterrupt.py
    :literal:
    :start-after: #end_pymotw_header

..
    Pressing Ctrl-C at the prompt causes a KeyboardInterrupt exception.

プロンプトで Ctrl-C を押下すると KeyboardInterrupt 例外を引き起こします。

::

    $ python exceptions_KeyboardInterrupt.py
    Press Return or Ctrl-C: ^CCaught KeyboardInterrupt


MemoryError
-----------

..
    If your program runs out of memory and it is possible to recover (by
    deleting some objects, for example), a MemoryError is raised.

実行中のプログラムがメモリ不足になったら、MemoryError を発生させてリカバリ(例えば、オブジェクトを削除する)することができます。

.. include:: exceptions_MemoryError.py
    :literal:
    :start-after: #end_pymotw_header

.. This takes a while to run, so don't bother with cog.

::

	$ python exceptions_MemoryError.py
	python(49670) malloc: *** mmap(size=1073745920) failed (error code=12)
	*** error: can't allocate region
	*** set a breakpoint in malloc_error_break to debug
	python(49670) malloc: *** mmap(size=1073745920) failed (error code=12)
	*** error: can't allocate region
	*** set a breakpoint in malloc_error_break to debug
	python(49670) malloc: *** mmap(size=1073745920) failed (error code=12)
	*** error: can't allocate region
	*** set a breakpoint in malloc_error_break to debug
	0 1
	0 2
	0 3
	(error, discarding existing list)
	1 1
	1 2
	1 3
	(error, discarding existing list)
	2 1
	2 2
	2 3
	(error, discarding existing list)


NameError
---------

..
    NameErrors are raised when your code refers to a name that does not
    exist in the current scope.  For example, an unqualified variable
    name.

カレントスコープに存在しない名前を参照するときに NameErrors が発生します。例えば、資格のない変数名です。

.. include:: exceptions_NameError.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'exceptions_NameError.py', ignore_error=True))
.. }}}

::

	$ python exceptions_NameError.py
	
	Traceback (most recent call last):
	  File "exceptions_NameError.py", line 15, in <module>
	    func()
	  File "exceptions_NameError.py", line 13, in func
	    print unknown_name
	NameError: global name 'unknown_name' is not defined

.. {{{end}}}

.. _exceptions-NotImplementedError:

NotImplementedError
-------------------

..
    User-defined base classes can raise NotImplementedError to indicate
    that a method or behavior needs to be defined by a subclass,
    simulating an *interface*.

サブクラスで定義する必要のあるメソッド又は振る舞いを表すために、 *インタフェース* を模倣してユーザ定義のベースクラスは NotImplementedError を発生させます。

.. include:: exceptions_NotImplementedError.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'exceptions_NotImplementedError.py', ignore_error=True))
.. }}}

::

	$ python exceptions_NotImplementedError.py
	
	SubClass doing something!
	Traceback (most recent call last):
	  File "exceptions_NotImplementedError.py", line 27, in <module>
	    BaseClass().do_something()
	  File "exceptions_NotImplementedError.py", line 18, in do_something
	    raise NotImplementedError(self.__class__.__name__ + '.do_something')
	NotImplementedError: BaseClass.do_something

.. {{{end}}}

..
   :mod:`abc` - Abstract base classes

.. seealso::

   :mod:`abc` - 抽象基底クラス

OSError
-------

..
    OSError serves as the error class for the :mod:`os` module, and is
    raised when an error comes back from an os-specific function.

OSError は :mod:`os` モジュールのエラークラスとして OS に特化した機能からエラーが返されるときに発生します。

.. include:: exceptions_OSError.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'exceptions_OSError.py', ignore_error=True))
.. }}}

::

	$ python exceptions_OSError.py
	
	0 /dev/ttys000
	1
	Traceback (most recent call last):
	  File "exceptions_OSError.py", line 15, in <module>
	    print i, os.ttyname(i)
	OSError: [Errno 25] Inappropriate ioctl for device

.. {{{end}}}


.. _exceptions-OverflowError:

OverflowError
-------------

..
    When an arithmetic operation exceeds the limits of the variable type,
    an OverflowError is raise.  Long integers allocate more space as
    values grow, so they end up raising MemoryError.  Floating point
    exception handling is not standardized, so floats are not checked.
    Regular integers are converted to long values as needed.

数値の操作が変数のデータ型の最大値を超えるときに OverflowError が発生します。long int は巨大な値のためにより多くの領域を割り当てます。そのため、最終的には MemoryError が発生します。浮動小数点の例外は標準化されていないので浮動小数はチェックされません。必要に応じて普通の int 型から long 型へ変換されます。

.. include:: exceptions_OverflowError.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'exceptions_OverflowError.py', ignore_error=True))
.. }}}

::

	$ python exceptions_OverflowError.py
	
	Regular integer: (maxint=9223372036854775807)
	No overflow for  <type 'long'> i = 27670116110564327421
	
	Long integer:
	 0 1
	10 1024
	20 1048576
	30 1073741824
	40 1099511627776
	50 1125899906842624
	60 1152921504606846976
	70 1180591620717411303424
	80 1208925819614629174706176
	90 1237940039285380274899124224
	
	Floating point values:
	0 1.23794003929e+27
	1 1.53249554087e+54
	2 2.34854258277e+108
	3 5.5156522631e+216
	Overflowed after  5.5156522631e+216 (34, 'Result too large')

.. {{{end}}}


ReferenceError
--------------

..
    When a :mod:`weakref` proxy is used to access an object that has
    already been garbage collected, a ReferenceError occurs.

ガベージコレクトされたオブジェクトへ :mod:`weakref` プロキシを使用してアクセスするときに ReferenceError が発生します。

.. include:: exceptions_ReferenceError.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'exceptions_ReferenceError.py', ignore_error=True))
.. }}}

::

	$ python exceptions_ReferenceError.py
	
	BEFORE: obj
	(Deleting <__main__.ExpensiveObject object at 0x10046e4d0>)
	AFTER:
	Traceback (most recent call last):
	  File "exceptions_ReferenceError.py", line 26, in <module>
	    print 'AFTER:', p.name
	ReferenceError: weakly-referenced object no longer exists

.. {{{end}}}

.. _exceptions-RuntimeError:

RuntimeError
------------

..
    A RuntimeError exception is used when no other more specific exception
    applies.  The interpreter does not raise this exception itself very
    often, but some user code does.

他に適切な例外がないときに RuntimeError 例外が使用されます。インタープリタはこの例外を滅多に発生させませんが、ユーザコードによっては RuntimeError を発生させます。


StopIteration
-------------

..
    When an iterator is done, it's ``next()`` method raises StopIteration.
    This exception is not considered an error.

イテレータが終了したときに、そのイテレータの ``next()`` メソッドは StopIteration を発生させます。この例外はエラーと見なされません。

.. include:: exceptions_StopIteration.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'exceptions_StopIteration.py', ignore_error=True))
.. }}}

::

	$ python exceptions_StopIteration.py
	
	<listiterator object at 0x10045f650>
	0
	1
	2
	Traceback (most recent call last):
	  File "exceptions_StopIteration.py", line 19, in <module>
	    print i.next()
	StopIteration

.. {{{end}}}


SyntaxError
-----------

..
    A SyntaxError occurs any time the parser finds source code it does not
    understand.  This can be while importing a module, invoking ``exec``,
    or calling ``eval()``.  Attributes of the exception can be used to
    find exactly what part of the input text caused the exception.

パーサが解析できないソースコードを見つけたときに SyntaxError が発生します。この例外はモジュールのインポート、 ``exec`` を実行したり、 ``eval()`` を呼び出したりするときに発生する可能性があります。例外の属性はこの例外を引き起こしたのがソースコードのどのテキストなのかを厳密に見つけるために使用されます。

.. include:: exceptions_SyntaxError.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'exceptions_SyntaxError.py', ignore_error=True))
.. }}}

::

	$ python exceptions_SyntaxError.py
	
	Syntax error <string> (1-10): five times three
	invalid syntax (<string>, line 1)

.. {{{end}}}


SystemError
-----------

..
    When an error occurs in the interpreter itself and there is some
    chance of continuing to run successfully, it raises a SystemError.
    SystemErrors probably indicate a bug in the interpreter and should be
    reported to the maintainer.

インタープリタそのものでエラーが発生しても正常に実行を継続する可能性があるときに SystemError が発生します。SystemErrors は、おそらくはインタープリタのバグを表し、メンテナへ報告すべきです。

.. _exceptions-SystemExit:

SystemExit
----------

..
    When ``sys.exit()`` is called, it raises SystemExit instead of exiting
    immediately.  This allows cleanup code in ``try:finally`` blocks to
    run and special environments (like debuggers and test frameworks) to
    catch the exception and avoid exiting.

``sys.exit()`` が呼び出されるとき、即時終了する代わりに SystemExit が発生します。これは ``try:finally`` ブロックのクリーンアップコードの実行、例外を捕捉するための(デバッガやテストフレームワークのような)特別な環境や処理を終了させないようにします。

.. _exceptions-TypeError:

TypeError
---------

..
    TypeErrors are caused by combining the wrong type of objects, or
    calling a function with the wrong type of object.

誤ったオブジェクトのデータ型を結合する、又は誤ったオブジェクトのデータ型で関数を呼び出すことで TypeErrors が発生します。

.. include:: exceptions_TypeError.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'exceptions_TypeError.py', ignore_error=True))
.. }}}

::

	$ python exceptions_TypeError.py
	
	Traceback (most recent call last):
	  File "exceptions_TypeError.py", line 12, in <module>
	    result = ('tuple',) + 'string'
	TypeError: can only concatenate tuple (not "str") to tuple

.. {{{end}}}


UnboundLocalError
-------------------

..
    An UnboundLocalError is a type of NameError specific to local variable
    names.

UnboundLocalError はローカル変数の名前に特化した NameError の一種です。

.. include:: exceptions_UnboundLocalError.py
    :literal:
    :start-after: #end_pymotw_header

..
    The difference between the global NameError and the UnboundLocal is
    the way the name is used.  Because the name "local_val" appears on the
    left side of an expression, it is interpreted as a local variable
    name.

グローバルな NameError と UnboundLocal の違いはその名前の使用方法です。"local_val" という名前が式の左側に現れるのでローカル変数の名前として解釈されます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'exceptions_UnboundLocalError.py', ignore_error=True))
.. }}}

::

	$ python exceptions_UnboundLocalError.py
	
	Global name error: global name 'unknown_global_name' is not defined
	Local name error: local variable 'local_val' referenced before assignment

.. {{{end}}}

.. _exceptions-UnicodeError:

UnicodeError
------------

..
    :class:`UnicodeError` is a subclass of :class:`ValueError` and is
    raised when a Unicode problem occurs.  There are separate subclasses
    for :class:`UnicodeEncodeError`, :class:`UnicodeDecodeError`, and
    :class:`UnicodeTranslateError`.

:class:`UnicodeError` は :class:`ValueError` のサブクラスでユニコードに関する問題で発生します。さらに :class:`UnicodeEncodeError`, :class:`UnicodeDecodeError` や :class:`UnicodeTranslateError` といったサブクラスに分割されます。

.. _exceptions-ValueError:

ValueError
----------

..
    A ValueError is used when a function receives a value that has the
    right type but an invalid value.

ある関数の受け取る値が正しい型で不正な値を持つときに ValueError が発生します。

.. include:: exceptions_ValueError.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'exceptions_ValueError.py', ignore_error=True))
.. }}}

::

	$ python exceptions_ValueError.py
	
	Traceback (most recent call last):
	  File "exceptions_ValueError.py", line 12, in <module>
	    print chr(1024)
	ValueError: chr() arg not in range(256)

.. {{{end}}}

.. _exceptions-ZeroDivisionError:

ZeroDivisionError
-----------------

..
    When zero shows up in the denominator of a division operation, a
    ZeroDivisionError is raised.

除算の分母がゼロのとき ZeroDivisionError が発生します。

.. include:: exceptions_ZeroDivisionError.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'exceptions_ZeroDivisionError.py', ignore_error=True))
.. }}}

::

	$ python exceptions_ZeroDivisionError.py
	
	Traceback (most recent call last):
	  File "exceptions_ZeroDivisionError.py", line 12, in <module>
	    print 1/0
	ZeroDivisionError: integer division or modulo by zero

.. {{{end}}}

.. _exceptions-warning:

..
    Warning Categories
    ==================

警告のカテゴリ
==============

..
    There are also several exceptions defined for use with the :mod:`warnings` module.

:mod:`warnings` モジュールと一緒に使用する複数の例外もあります。

..
    Warning
      The base class for all warnings.

Warning
  全ての warnings のベースクラス

..
    UserWarning
      Base class for warnings coming from user code.

UserWarning
  ユーザコードから返される warnings のベースクラス

.. _exceptions-DeprecationWarning:

..
    DeprecationWarning
      Used for features no longer being maintained.

DeprecationWarning
  今後はメンテナンスされない機能に使用される

..
    PendingDeprecationWarning
      Used for features that are soon going to be deprecated.

PendingDeprecationWarning
  すぐに廃止予定の機能に使用される

..
    SyntaxWarning
      Used for questionable syntax.

SyntaxWarning
  怪しい構文に使用される

.. _exceptions-RuntimeWarning:

..
    RuntimeWarning
      Used for events that happen at runtime that might cause problems.

RuntimeWarning
  実行時に問題を引き起こすかもしれないイベントに使用される

..
    FutureWarning
      Warning about changes to the language or library that are coming at a later time.

FutureWarning
  言語又はライブラリがその後に変更されることに関して警告する

..
    ImportWarning
      Warn about problems importing a module.

ImportWarning
  モジュールインポートの問題に関して警告する

..
    UnicodeWarning
      Warn about problems with unicode text.

UnicodeWarning
  ユニコードテキストの問題に関して警告する

..
    `exceptions <http://docs.python.org/library/exceptions.html>`_
        The standard library documentation for this module.
    :mod:`warnings`
        Non-error warning messages.

.. seealso::

    `exceptions <http://docs.python.org/library/exceptions.html>`_
        本モジュールの標準ライブラリドキュメント

    :mod:`warnings`
        エラーではない警告メッセージ
