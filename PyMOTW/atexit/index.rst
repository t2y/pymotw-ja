..
    =======================================================
    atexit -- Call functions when a program is closing down
    =======================================================

============================================
atexit -- プログラムの終了時に関数を呼び出す
============================================

..
    :synopsis: Register function(s) to be called when a program is closing down.

.. module:: atexit
    :synopsis: プログラムの終了時に呼び出される関数を登録する

..
    :Purpose: Register function(s) to be called when a program is closing down.
    :Available In: 2.1.3 and later

:目的: プログラムの終了時に呼び出される関数を登録する
:利用できるバージョン: 2.1.3 以上

..
    The atexit module provides a simple interface to register functions to be
    called when a program closes down normally. The sys module also provides a
    hook, sys.exitfunc, but only one function can be registered there. The atexit
    registry can be used by multiple modules and libraries simultaneously.

:mod:`atexit` モジュールは、プログラムが正常終了するときに呼び出される関数を登録するためのシンプルなインタフェースを提供します。 :mod:`sys` モジュールにも :func:`sys.exitfunc` というフックを提供しますが、その関数で登録できるのは1つの関数のみです。 :mod:`atexit` モジュールで登録すると同時に複数のモジュールやライブラリで使用できます。

..
    Examples
    ========

サンプル
========

..
    A simple example of registering a function via atexit.register() looks like:

:func:`atexit.register` 経由で関数を登録する簡単なサンプルは次のようになります。

.. include:: atexit_simple.py
    :literal:
    :start-after: #end_pymotw_header

..
    Since the program doesn't do anything else, all_done() is called right away:

このプログラムは他に何もしないので、すぐに :func:`all_done` が呼び出されます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'atexit_simple.py'))
.. }}}

::

	$ python atexit_simple.py
	
	Registering
	Registered
	all_done()

.. {{{end}}}

..
    It is also possible to register more than one function, and to pass arguments.
    That can be useful to cleanly disconnect from databases, remove temporary
    files, etc. Since it is possible to pass arguments to the registered
    functions, we don't even need to keep a separate list of things to clean up --
    we can just register a clean up function more than once.

さらに1つ以上の関数を登録したり引数を渡すこともできます。一時ファイルを削除する等、データベースからクリーンに切断するのに便利です。登録された関数へ引数を渡すこともできるので、クリーンアップするモノをリストに独立させて保持する必要もありません。つまり、その都度クリーンアップ関数を登録すれば良いだけです。

.. include:: atexit_multiple.py
    :literal:
    :start-after: #end_pymotw_header

..
    Notice that order in which the exit functions are called is the reverse of
    the order they are registered. This allows modules to be cleaned up in the
    reverse order from which they are imported (and therefore register their
    atexit functions), which should reduce dependency conflicts.

exit 関数が呼びされる順序は、登録された順序とは逆の順序で呼び出されることに注意してください。これは依存による競合を減らすために、インポートされた(関数を atexit に登録された)順序の逆でモジュールにクリーンアップさせます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'atexit_multiple.py'))
.. }}}

::

	$ python atexit_multiple.py
	
	my_cleanup(third)
	my_cleanup(second)
	my_cleanup(first)

.. {{{end}}}

..
    When are atexit functions not called?
    =====================================

どんなときに atexit 関数が呼び出されないの？
============================================

..
    The callbacks registered with atexit are not invoked if:

atexit で登録されたコールバック関数が実行されないのは次のような場合です。

..
    * the program dies because of a signal

* プログラムがシグナルで終了する場合

..
    * os._exit() is invoked directly

* :func:`os._exit` が直接実行される場合

..
    * a Python fatal error is detected (in the interpreter)

* Python の(インタープリタで)致命的エラーが検出される場合

..
    To illustrate a program being killed via a signal, we can modify one
    of the examples from the :mod:`subprocess` article. There are 2 files
    involved, the parent and the child programs. The parent starts the
    child, pauses, then kills it:

シグナルで kill されるプログラムを説明するために、 :mod:`subprocess` モジュールの記事からサンプルの1つを変更します。親と子の2つのプログラムが実行されます。親プログラムは子プログラムを開始して、一時中断して、その子プログラムを kill します。

.. include:: atexit_signal_parent.py
    :literal:
    :start-after: #end_pymotw_header

..
    The child sets up an atexit callback, to prove that it is not called.

子プログラムは、コールバック関数が呼び出されないことを証明するために atexit にコールバック関数を登録します。

.. include:: atexit_signal_child.py
    :literal:
    :start-after: #end_pymotw_header

..
    When run, the output should look something like this:

実行すると、その実行結果は次のようになります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'atexit_signal_parent.py'))
.. }}}

::

	$ python atexit_signal_parent.py
	
	CHILD: Registering atexit handler
	CHILD: Pausing to wait for signal
	PARENT: Pausing before sending signal...
	PARENT: Signaling child

.. {{{end}}}

..
    Note that the child does not print the message embedded in not_called().

子プログラムは登録した :func:`not_called` のメッセージを表示しないことを確認してください。

..
    Similarly, if a program bypasses the normal exit path it can avoid having the
    atexit callbacks invoked.

同様に、プログラムが正常終了しない場合に atexit のコールバック関数は実行されません。

.. include:: atexit_os_exit.py
    :literal:
    :start-after: #end_pymotw_header

..
    Since we call os._exit() instead of exiting normally, the callback is not
    invoked. 

正常終了する代わりに :func:`os._exit` を呼び出すので、登録されたコールバック関数は実行されません。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'atexit_os_exit.py'))
.. }}}

::

	$ python atexit_os_exit.py
	

.. {{{end}}}

..
    If we had instead used sys.exit(), the callbacks would still have been called.

もし代わりに :func:`sys.exit` を使用した場合、登録されたコールバック関数も実行されます。

.. include:: atexit_sys_exit.py
    :literal:
    :start-after: #end_pymotw_header


.. {{{cog
.. cog.out(run_script(cog.inFile, 'atexit_sys_exit.py'))
.. }}}

::

	$ python atexit_sys_exit.py
	
	Registering
	Registered
	Exiting...
	all_done()

.. {{{end}}}

..
    Simulating a fatal error in the Python interpreter is left as an exercise to
    the reader.

同様に、Python インタープリタの致命的エラーは読者の練習問題として残しておきます。

..
    Exceptions in atexit Callbacks
    ==============================

atexit コールバック関数の例外
=============================

..
    Tracebacks for exceptions raised in atexit callbacks are printed to the
    console and the last exception raised is re-raised to be the final error
    message of the program.

atexit のコールバック関数内で発生した例外のトレースバック情報はコンソールに表示されます。そして、最後に発生した例外がプログラムの最後のエラーメッセージになり再発生します。

.. include:: atexit_exception.py
    :literal:
    :start-after: #end_pymotw_header

..
    Notice again that the registration order controls the execution order. If an
    error in one callback introduces an error in another (registered earlier, but
    called later), the final error message might not be the most useful error
    message to show the user.

登録された順序が実行順序を制御することに再注目してください。1つのコールバック関数のエラーがもう一方のエラーを発生させる場合(先に登録されても後に呼び出される)、最後のエラーメッセージはユーザへ表示する適切なエラーメッセージではない可能性があります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'atexit_exception.py'))
.. }}}

::

	$ python atexit_exception.py
	
	Error in atexit._run_exitfuncs:
	Traceback (most recent call last):
	  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/atexit.py", line 24, in _run_exitfuncs
	    func(*targs, **kargs)
	  File "atexit_exception.py", line 37, in exit_with_exception
	    raise RuntimeError(message)
	RuntimeError: Registered second
	Error in atexit._run_exitfuncs:
	Traceback (most recent call last):
	  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/atexit.py", line 24, in _run_exitfuncs
	    func(*targs, **kargs)
	  File "atexit_exception.py", line 37, in exit_with_exception
	    raise RuntimeError(message)
	RuntimeError: Registered first
	Error in sys.exitfunc:
	Traceback (most recent call last):
	  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/atexit.py", line 24, in _run_exitfuncs
	    func(*targs, **kargs)
	  File "atexit_exception.py", line 37, in exit_with_exception
	    raise RuntimeError(message)
	RuntimeError: Registered first

.. {{{end}}}

..
    In general you will probably want to handle and quietly log all exceptions in
    your cleanup functions, since it is messy to have a program dump errors on
    exit.

一般的に、終了時にプログラムのダンプエラーを持つのは厄介なので、クリーンアップ関数内で全ての例外を完全にログ出力すると良いかもしれません。

.. seealso::

    `atexit <http://docs.python.org/library/atexit.html>`_
        .. The standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント

