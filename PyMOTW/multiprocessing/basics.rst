..
    ######################
    multiprocessing Basics
    ######################

######################
multiprocessing の基本
######################

..
    The simplest way to spawn a second is to instantiate a
    :class:`Process` object with a target function and call :func:`start`
    to let it begin working.

サブプロセスを使用する最も簡単な方法は対象関数と共に :class:`Process` オブジェクトをインスタンス化することで、その処理を開始させるために :func:`start` を呼び出してください。

.. include:: multiprocessing_simple.py
    :literal:
    :start-after: #end_pymotw_header

..
    The output includes the word "Worker" printed five times, although it
    may not be entirely clean depending on the order of execution.

その出力結果は実行した順番通りかどうかよく分かりませんが "Worker" という単語を5回表示します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'multiprocessing_simple.py'))
.. }}}

::

	$ python multiprocessing_simple.py
	
	Worker
	Worker
	Worker
	Worker
	Worker

.. {{{end}}}

..
    It usually more useful to be able to spawn a process with arguments to
    tell it what work to do.  Unlike with :mod:`threading`, to pass
    arguments to a :mod:`multiprocessing` :class:`Process` the argument
    must be able to be serialized using :mod:`pickle`.  This example
    passes each worker a number so the output is a little more interesting.

実行する処理を引数で渡してプロセスを生成できるので本当にかなり便利です。 :mod:`threading` とは違い :mod:`multiprocessing` の :class:`Process` へ引数を渡すには、その引数は :mod:`pickle` でシリアライズ可能でなければなりません。このサンプルは出力結果がもう少し面白くなるように各ワーカーへ数値を渡します。

.. include:: multiprocessing_simpleargs.py
    :literal:
    :start-after: #end_pymotw_header

..
    The integer argument is now included in the message printed by each worker:

引数として渡された整数は各ワーカーでメッセージに含めて表示されます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'multiprocessing_simpleargs.py'))
.. }}}

::

	$ python multiprocessing_simpleargs.py
	
	Worker: 0
	Worker: 1
	Worker: 2
	Worker: 3
	Worker: 4

.. {{{end}}}

..
    Importable Target Functions
    ===========================

インポート可能な対象関数
========================

..
    One difference between the :mod:`threading` and :mod:`multiprocessing`
    examples is the extra protection for ``__main__`` used in the
    :mod:`multiprocessing` examples.  Due to the way the new processes are
    started, the child process needs to be able to import the script
    containing the target function.  Wrapping the main part of the
    application in a check for ``__main__`` ensures that it is not run
    recursively in each child as the module is imported.  Another approach
    is to import the target function from a separate script.

:mod:`threading` と :mod:`multiprocessing` のサンプルの違いの1つは :mod:`multiprocessing` のサンプルで使用されている ``__main__``  の追加の保護機構です。新しいプロセスが開始されるために、子プロセスは対象関数を実装したスクリプトファイルをインポートできる必要があります。そのアプリケーションの ``__main__`` をチェックして main 処理をラッピングすることで、そのモジュールをインポートされてそれぞれの子プロセスで再起的に実行されないことを保証します。別の方法としては、別のスクリプトファイルから対象関数をインポートすることです。

..
    For example, this main program:

例えば、このメインプログラムは次のようになります。

.. include:: multiprocessing_import_main.py
    :literal:
    :start-after: #end_pymotw_header

..
    uses this worker function, defined in a separate module:

分割したモジュールで定義されているワーカー関数を使用します。

.. include:: multiprocessing_import_worker.py
    :literal:
    :start-after: #end_pymotw_header

..
    and produces output like the first example above:

そして前のセクションで紹介した最初のサンプルと同じ出力を表示します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'multiprocessing_import_main.py'))
.. }}}

::

	$ python multiprocessing_import_main.py
	
	Worker
	Worker
	Worker
	Worker
	Worker

.. {{{end}}}

..
    Determining the Current Process
    ===============================

カレントプロセスを決定する
==========================

..
    Passing arguments to identify or name the process is cumbersome, and
    unnecessary.  Each :class:`Process` instance has a name with a default
    value that can be changed as the process is created. Naming processes
    is useful for keeping track of them, especially in applications with
    multiple types of processes running simultaneously.

プロセスに識別子や名前を付けたりすることは全く不要で面倒なだけです。それぞれの :class:`Process` インスタンスはプロセスの生成時に変更可能な名前とデフォルト値を持っています。名前付けプロセスはそういったプロセスを追跡するのに便利で、特に同時に実行中のプロセスが複数の型を持つアプリケーションで有効です。

.. include:: multiprocessing_names.py
    :literal:
    :start-after: #end_pymotw_header

..
    The debug output includes the name of the current process on each
    line. The lines with ``Process-3`` in the name column correspond to
    the unnamed process ``worker_1``.

デバッグ出力は行単位にカレントプロセスの名前が表示されます。名前に ``Process-3`` がある行は名前が付けられていないプロセス ``worker_2`` に対応します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'multiprocessing_names.py'))
.. }}}

::

	$ python multiprocessing_names.py
	
	worker 1 Starting
	worker 1 Exiting
	Process-3 Starting
	Process-3 Exiting
	my_service Starting
	my_service Exiting

.. {{{end}}}

..
    Daemon Processes
    ================

デーモンプロセス
================

..
    By default the main program will not exit until all of the children
    have exited. There are times when starting a background process that
    runs without blocking the main program from exiting is useful, such as
    in services where there may not be an easy way to interrupt the
    worker, or where letting it die in the middle of its work does not
    lose or corrupt data (for example, a task that generates "heart beats"
    for a service monitoring tool). 

デフォルトでは、メインプログラムは全ての子プロセスが終了するまで終了しません。終了からメインプログラムをブロッキングせずにバックグラウンドプロセスを開始するのは便利なときがあります。このようなサービスは、ワーカーと相互にやり取りする簡単な方法がない可能性がある、もしくはデータを破損したり失ったりせずに処理の途中で終了させるようなサービスです(例えば、サービス監視ツールの "心電図" のような処理を生成するタスク)。

..
    To mark a process as a daemon, set its :attr:`daemon` attribute with a
    boolean value. The default is for processes to not be daemons, so
    passing True turns the daemon mode on.

デーモンとしてプログラムをマークするには :attr:`daemon` 属性にブーリアン値を設定してください。デフォルトでは、プロセスはデーモンにならないのでデーモンモードに切り替えるために True を渡します。

.. include:: multiprocessing_daemon.py
    :literal:
    :start-after: #end_pymotw_header

..
    The output does not include the "Exiting" message from the daemon
    process, since all of the non-daemon processes (including the main
    program) exit before the daemon process wakes up from its 2 second
    sleep.

全ての非デーモンプロセス(メインプログラムも含む)はデーモンプロセスが2秒間のスリープから復帰する前に終了するので、その出力結果はデーモンプロセスから表示される "Exiting" メッセージを含んでいません。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'multiprocessing_daemon.py'))
.. }}}

::

	$ python multiprocessing_daemon.py
	
	Starting: daemon 13866
	Starting: non-daemon 13867
	Exiting : non-daemon 13867

.. {{{end}}}

..
    The daemon process is terminated automatically before the main program
    exits, to avoid leaving orphaned processes running.  You can verify
    this by looking for the process id value printed when you run the
    program, and then checking for that process with a command like
    ``ps``.

デーモンプロセスは、実行プロセスが孤児として残ってしまわないようにメインプログラムが終了する前に自動的に終了します。プログラムを実行するときに表示したプロセス ID の値を覚えておき ``ps`` のようなコマンドでそのプロセスを調べることで検証することができます。

..
    Waiting for Processes
    =====================

プロセスを待つ
==============

..
    To wait until a process has completed its work and exited, use the
    :func:`join` method.

あるプロセスが処理を実行した後で完全に終了するまで待つには :func:`join` メソッドを使用してください。

.. include:: multiprocessing_daemon_join.py
    :literal:
    :start-after: #end_pymotw_header

..
    Since the main process waits for the daemon to exit using
    :func:`join`, the "Exiting" message is printed this time.

メインプロセスは :func:`join` で終了するデーモンを待つので、今回は "Exiting" メッセージが表示されます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'multiprocessing_daemon_join.py'))
.. }}}

::

	$ python multiprocessing_daemon_join.py
	
	Starting: non-daemon
	Exiting : non-daemon
	Starting: daemon
	Exiting : daemon

.. {{{end}}}

..
    By default, :func:`join` blocks indefinitely. It is also possible to
    pass a timeout argument (a float representing the number of seconds to
    wait for the process to become inactive). If the process does not
    complete within the timeout period, :func:`join` returns anyway.

デフォルトでは :func:`join` は無限にブロッキングします。さらにタイムアウト(小数はプロセスが非アクティブになるのを待つ秒数)を引数で渡すこともできます。もしプロセスがタイムアウトの時間内で完了しなかったら、いずれにしても :func:`join` から返されます。

.. include:: multiprocessing_daemon_join_timeout.py
    :literal:
    :start-after: #end_pymotw_header

..
    Since the timeout passed is less than the amount of time the daemon
    sleeps, the process is still "alive" after :func:`join` returns.

渡されたそのタイムアウトの時間はデーモンがスリープしている時間よりも短いので、そのプロセスは :func:`join` が返された後もまだ "実行中" です。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'multiprocessing_daemon_join_timeout.py'))
.. }}}

::

	$ python multiprocessing_daemon_join_timeout.py
	
	Starting: non-daemon
	Exiting : non-daemon
	d.is_alive() True

.. {{{end}}}

..
    Terminating Processes
    =====================

プロセスを終了する
==================

..
    Although it is better to use the *poison pill* method of signaling to
    a process that it should exit (see :ref:`multiprocessing-queues`), if
    a process appears hung or deadlocked it can be useful to be able to
    kill it forcibly.  Calling :func:`terminate` on a process object kills
    the child process.

プロセスへ終了シグナルを送る *poison pill* メソッドを使用するのは良い方法ではありますが(:ref:`multiprocessing-queues` を参照)、もしプロセスがハングアップ又はデッドロックした場合、強制的にプロセスを kill できるとさらに便利です。プロセスオブジェクトで :func:`terminate` を呼び出すと子プロセスを kill します。

.. include:: multiprocessing_terminate.py
    :literal:
    :start-after: #end_pymotw_header

.. note::

    ..  It is important to :func:`join` the process after terminating it
        in order to give the background machinery time to update the
        status of the object to reflect the termination.

    プロセスの終了を反映するために、オブジェクトのステータスを更新するバックグラウンド機構のために終了後に :func:`join` することが重要です。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'multiprocessing_terminate.py'))
.. }}}

::

	$ python multiprocessing_terminate.py
	
	BEFORE: <Process(Process-1, initial)> False
	DURING: <Process(Process-1, started)> True
	TERMINATED: <Process(Process-1, started)> True
	JOINED: <Process(Process-1, stopped[SIGTERM])> False

.. {{{end}}}

..
    Process Exit Status
    ===================

プロセスの終了ステータス
========================

..
    The status code produced when the process exits can be accessed via
    the :attr:`exitcode` attribute.

プロセスの終了が :attr:`exitcode` 属性を経由してアクセスされるときにステータスコードが生成されます。

..
    For :attr:`exitcode` values

:attr:`exitcode` の値とは、

..
    * ``== 0`` -- no error was produced
    * ``> 0`` -- the process had an error, and exited with that code
    * ``< 0`` -- the process was killed with a signal of ``-1 * exitcode``

* ``== 0`` -- エラーが発生しなかった
* ``> 0`` -- エラーが発生して、その値で終了した
* ``< 0`` -- プロセスが ``-1 * exitcode`` のシグナルで kill された

.. include:: multiprocessing_exitcode.py
    :literal:
    :start-after: #end_pymotw_header

..
    Processes that raise an exception automatically get an
    :attr:`exitcode` of 1.

例外が発生するプロセスは自動的に :attr:`exitcode` が 1 になります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'multiprocessing_exitcode.py', break_lines_at=68))
.. }}}

::

	$ python multiprocessing_exitcode.py
	
	Starting process for exit_error
	Starting process for exit_ok
	Starting process for return_value
	Starting process for raises
	Starting process for terminated
	Process raises:
	Traceback (most recent call last):
	  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python
	2.7/multiprocessing/process.py", line 258, in _bootstrap
	    self.run()
	  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python
	2.7/multiprocessing/process.py", line 114, in run
	    self._target(*self._args, **self._kwargs)
	  File "multiprocessing_exitcode.py", line 24, in raises
	    raise RuntimeError('There was an error!')
	RuntimeError: There was an error!
	exit_error.exitcode = 1
	exit_ok.exitcode = 0
	return_value.exitcode = 0
	raises.exitcode = 1
	terminated.exitcode = -15

.. {{{end}}}

..
    Logging
    =======

ロギング
========

..
    When debugging concurrency issues, it can be useful to have access to
    the internals of the objects provided by :mod:`multiprocessing`.
    There is a convenient module-level function to enable logging called
    :func:`log_to_stderr`.  It sets up a logger object using
    :mod:`logging` and adds a handler so that log messages are sent to the
    standard error channel.

並列処理の不具合をデバッグするとき :mod:`multiprocessing` が提供した内部オブジェクトへアクセスできるとデバッグがやり易いです。 :func:`log_to_stderr` という、ロギングを有効にする便利なモジュールレベルの関数があります。その関数は :mod:`logging` を使用してロガーオブジェクトを設定して、ログメッセージが標準エラー経由で送られるようにハンドラを追加します。

.. include:: multiprocessing_log_to_stderr.py
    :literal:
    :start-after: #end_pymotw_header

..
    By default the logging level is set to ``NOTSET`` so no messages are
    produced.  Pass a different level to initialize the logger to the
    level of detail you want.

デフォルトでは、ログレベルはメッセージを生成しない ``NOTSET`` に設定されています。あなたが望む詳細レベルを渡してロガーを初期化してください。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'multiprocessing_log_to_stderr.py'))
.. }}}

::

	$ python multiprocessing_log_to_stderr.py
	
	[INFO/Process-1] child process calling self.run()
	Doing some work
	[INFO/Process-1] process shutting down
	[DEBUG/Process-1] running all "atexit" finalizers with priority >= 0
	[DEBUG/Process-1] running the remaining "atexit" finalizers
	[INFO/Process-1] process exiting with exitcode 0
	[INFO/MainProcess] process shutting down
	[DEBUG/MainProcess] running all "atexit" finalizers with priority >= 0
	[DEBUG/MainProcess] running the remaining "atexit" finalizers

.. {{{end}}}

..
    To manipulate the logger directly (change its level setting or add
    handlers), use :func:`get_logger`.

直接的にロガーを操作する(その設定レベルを変更する、又はハンドラを追加する)には :func:`get_logger` を使用してください。

.. include:: multiprocessing_get_logger.py
    :literal:
    :start-after: #end_pymotw_header

..
    The logger can also be configured through the :mod:`logging`
    configuration file API, using the name ``multiprocessing``.

``multiprocessing`` を使用して、ロガーは :mod:`logging` の設定ファイル API を通して設定することもできます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'multiprocessing_get_logger.py'))
.. }}}

::

	$ python multiprocessing_get_logger.py
	
	[INFO/Process-1] child process calling self.run()
	Doing some work
	[INFO/Process-1] process shutting down
	[INFO/Process-1] process exiting with exitcode 0
	[INFO/MainProcess] process shutting down

.. {{{end}}}

..
    Subclassing Process
    ===================

プロセスをサブクラス化する
==========================

..
    Although the simplest way to start a job in a separate process is to
    use :class:`Process` and pass a target function, it is also possible
    to use a custom subclass.

独立したプロセスのジョブを開始する最も簡単な方法は :class:`Process` クラスを使用して対象関数を引数で渡すことですが、カスタムサブクラスを使用することもできます。

.. include:: multiprocessing_subclass.py
    :literal:
    :start-after: #end_pymotw_header

..
    The derived class should override :meth:`run` to do its work.

派生クラスは処理を行うために :meth:`run` をオーバライドすべきです。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'multiprocessing_subclass.py'))
.. }}}

::

	$ python multiprocessing_subclass.py
	
	In Worker-1
	In Worker-2
	In Worker-3
	In Worker-4
	In Worker-5

.. {{{end}}}
