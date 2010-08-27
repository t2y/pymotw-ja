..
    ==============================================================
    subprocess -- Spawn and communicate with additional processes.
    ==============================================================

========================================================
subprocess -- 新しくプロセスを生成してプロセスと通信する
========================================================

..
    :synopsis: Spawn and communicate with additional processes.

.. module:: subprocess
    :synopsis: 新しくプロセスを生成してプロセスと通信する

..
    :Purpose: Spawn and communicate with additional processes.
    :Python Version: New in 2.4

:目的: 新しくプロセスを生成してプロセスと通信する
:Python バージョン: 2.4 で新規追加

..
    The :mod:`subprocess` module provides a consistent interface to
    creating and working with additional processes. It offers a
    higher-level interface than some of the other available modules, and
    is intended to replace functions such as :func:`os.system`,
    :func:`os.spawn*`, :func:`os.popen*`, :func:`popen2.*` and
    :func:`commands.*`. To make it easier to compare subprocess with those
    other modules, the examples here re-create those used for
    :mod:`os` and :mod:`popen`.

:mod:`subprocess` モジュールは新しくプロセスを生成して、そのプロセスを扱う一貫したインタフェースを提供します。それは従来からある他のモジュールよりも高レベルなインタフェースを提供します。そして :func:`os.system`, :func:`os.spawn*`, :func:`os.popen*`, :func:`popen2.*` や :func:`commands.*` のような従来の関数の置き換えを目的としています。subprocess モジュールと他のモジュールとの比較を分かり易くするために :mod:`os` や :mod:`popen` を使用したサンプルを再作成して紹介します。

..
    The :mod:`subprocess` module defines one class, :class:`Popen` and a
    few wrapper functions which use that class. The constructor for
    :class:`Popen` takes several arguments to make it easier to set up the
    new process, and then communicate with it via pipes. I will
    concentrate on example code here; for a complete description of the
    arguments, refer to section 17.1.1 of the library documentation.

:mod:`subprocess` モジュールは :class:`Popen` とそのクラスを使用する複数のラッパ関数を定義します。 :class:`Popen` のコンストラクタは新たなプロセス生成を簡単にする複数の引数を受け取り、パイプを経由して生成したプロセスと通信します。本稿では全ての引数の説明は行いません。詳細は標準ライブラリドキュメントの 17.1.1 セクションを参照してください。

.. note::

    .. The API is roughly the same, but the underlying implementation is
       slightly different between Unix and Windows. All of the examples
       shown here were tested on Mac OS X. Your mileage on a non-Unix OS
       will vary.

    API は大雑把には同じですが Unix と Windows 環境の違いで低レイヤの実装は若干違います。本稿で紹介する全てのサンプルコードは Mac OS X でテストされています。非 Unix 環境ではその実行結果が変わるでしょう。

..
    Running External Command
    ========================

外部コマンドを実行する
======================

..
    To run an external command without interacting with it, such as one
    would do with :ref:`os.system() <os-system>`, Use the :func:`call()`
    function.

実行する外部コマンドのプロセスとやり取りしない :ref:`os.system() <os-system>` で実行されるような処理は :func:`call()` 関数を使用してください。

.. include:: subprocess_os_system.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'subprocess_os_system.py'))
.. }}}
.. {{{end}}}

..
    When *shell* is set to ``True``, shell variables in the command
    string are expanded:

引数 *shell* に ``True`` を渡すと、シェル変数がコマンド文字列内で展開されます。

.. include:: subprocess_shell_variables.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'subprocess_shell_variables.py'))
.. }}}
.. {{{end}}}

..
    Working with Pipes
    ==================

パイプと連携する
================

..
    By passing different arguments for *stdin*, *stdout*, and *stderr* it
    is possible to mimic the variations of :func:`os.popen()`.

*stdin*, *stdout* や *stderr* に違う引数を渡すことで :func:`os.popen()` に類似した変形処理を行うことができます。

popen
-----

..
    Reading from the output of a pipe:

パイプから出力を読み込みます。

.. include:: subprocess_popen_read.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, '-u subprocess_popen_read.py'))
.. }}}
.. {{{end}}}

..
    Writing to the input of a pipe:

パイプの入力を書き込みます。

.. include:: subprocess_popen_write.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, '-u subprocess_popen_write.py'))
.. }}}
.. {{{end}}}

popen2
------

..
    Reading and writing, as with popen2:

popen2 のように読み書きします。

.. include:: subprocess_popen2.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, '-u subprocess_popen2.py'))
.. }}}
.. {{{end}}}

popen3
------

..
    Separate streams for stdout and stderr, as with popen3:

popen3 のように標準出力と標準エラーのストリームを分割します。

.. include:: subprocess_popen3.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, '-u subprocess_popen3.py'))
.. }}}
.. {{{end}}}

popen4
------

..
    Merged stdout and stderr, as with popen4:

popen4 のように標準出力と標準エラーを1つにマージします。

.. include:: subprocess_popen4.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, '-u subprocess_popen4.py'))
.. }}}
.. {{{end}}}

..
    Connecting Segments of a Pipe
    =============================

パイプのセグメントへ接続する
============================

..
    By creating separate Popen instances and chaining their inputs and outputs
    together, you can create your own pipeline of commands just as with the
    Unix shell.

独立した Popen インスタンスを生成して、それらの入力と出力を繋ぐことで、まさに Unix シェルのように独自のコマンドのパイプラインを作成することができます。

.. include:: subprocess_pipes.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, '-u subprocess_pipes.py'))
.. }}}
.. {{{end}}}

..
    Interacting with Another Command
    ================================

別のコマンドと相互にやり取りする
================================

..
    All of the above examples assume a limited amount of interaction. The
    :func:`communicate()` method reads all of the output and waits for
    child process to exit before returning. It is also possible to write
    to and read from the individual pipe handles used by the
    :class:`Popen` instance. A simple echo program that reads from
    standard input and writes to standard output illustrates this:

上述した全てのサンプルは制限のあるプロセス間のやり取りを前提としていました。 :func:`communicate()` メソッドは全ての出力から読み込み、値を返す前に子プロセスの終了を待ちます。また :class:`Popen` インスタンスによって使用される個々のパイプハンドラに読み書きすることもできます。標準入力から読み込んで標準出力へ書き込む単純な echo プログラムでこのことを説明します。

.. include:: repeater.py
    :literal:
    :start-after: #end_pymotw_header

..
    Make note of the fact that ``repeater.py`` writes to stderr when it
    starts and stops. That information can be used to show the lifetime of
    the child process. 

プログラムの開始時と終了時に ``repeater.py`` が標準エラーに書き込んでいる点に注意してください。この情報は子プロセスのライフタイムを表すために使用されます。

..
    The next interaction example uses the stdin and stdout file handles
    owned by the :class:`Popen` instance in different ways. In the first
    example, a sequence of 10 numbers are written to stdin of the process,
    and after each write the next line of output is read back. In the
    second example, the same 10 numbers are written but the output is read
    all at once using :func:`communicate()`.

次の標準入力と標準出力のやり取りのサンプルは違った方法で :class:`Popen` インスタンスが所有する標準入力と標準出力のファイルハンドラを使用します。最初のサンプルでは、10個の数値リストからプロセスの標準入力へ書き込んだ後、その次の行で標準出力から読み返されます。2番目のサンプルでは、同じ10個の数値リストから書き込まれますが :func:`communicate()` を使用して全ての出力をまとめて読み込みます。

.. include:: interaction.py
    :literal:
    :start-after: #end_pymotw_header

..
    Notice where the ``"repeater.py: exiting"`` lines fall in the output
    for each loop:

各ループで標準エラー出力の ``"repeater.py: exiting"`` 行が違う場所に出力されていることに注目してください。

.. {{{cog
.. cog.out(run_script(cog.inFile, '-u interaction.py'))
.. }}}
.. {{{end}}}

..
    Signaling Between Processes
    ===========================

プロセス間でシグナルを送る
==========================

..
    The :mod:`os` examples include a demonstration of :ref:`signaling
    between processes using os.fork() and os.kill()
    <creating-processes-with-os-fork>`. Since each :class:`Popen` instance
    provides a *pid* attribute with the process id of the child process,
    it is possible to do something similar with :mod:`subprocess`. For
    example, using this script for the child process to be executed by the
    parent process:

:mod:`os` のサンプルは :ref:`os.fork() や os.kill() を使用してシグナルを送る <creating-processes-with-os-fork>` デモも含みます。各 :class:`Popen` インスタンスは子プロセスのプロセス ID と一緒に *pid* 属性を提供するので :mod:`subprocess` でよく似た処理を行うことができます。例えば、親プロセスによって実行される子プロセスのために次のスクリプトを使用します。

.. include:: signal_child.py
    :literal:
    :start-after: #end_pymotw_header

..
    and this parent process:

親プロセスは次になります。

.. include:: signal_parent.py
    :literal:
    :start-after: #end_pymotw_header

..
    the output will look something like:

その結果出力は次のようになります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'signal_parent.py'))
.. }}}
.. {{{end}}}

.. _subprocess-process-groups:

..
    Process Groups / Sessions
    -------------------------

プロセスグループ / セッション
-----------------------------

..
    Because of the way the process tree works under Unix, if the process
    created by :mod:`Popen` spawns sub-processes, those children will not
    receive any signals sent to the parent.  That means, for example, it
    will be difficult to cause them to terminate by sending ``SIGINT`` or
    ``SIGTERM``.

Unix 環境ではプロセスツリーという概念があり :class:`Popen` で生成したプロセスがサブプロセスを生成する場合、そういった子プロセスは親プロセスからのシグナルを決して受け取りません。例えば ``SIGINT`` か ``SIGTERM`` を送ることでその子プロセスを終了させることが難しいということになります。

.. include:: subprocess_signal_parent_shell.py
    :literal:
    :start-after: #end_pymotw_header

..
    Notice that the pid used to send the signal is different from the pid
    of the child of the shell script waiting for the signal because in
    this example, there are three separate processes interacting:

シグナルを送るために使用された pid はシグナルを待つシェルスクリプトの子プロセスの pid と違っています。というのは、このサンプルは3つの独立したプロセスが相互に関連して存在します。

..
    1. ``subprocess_signal_parent_shell.py``
    2. a Unix shell process running the script created by the main python
       program
    3. ``signal_child.py``

1. ``subprocess_signal_parent_shell.py``
2. スクリプトを実行する Unix シェルプロセスをメインプログラムが作成する
3. ``signal_child.py``

.. {{{cog
.. cog.out(run_script(cog.inFile, 'subprocess_signal_parent_shell.py'))
.. }}}
.. {{{end}}}

..
    The solution to this problem is to use a *process group* to associate
    the children so they can be signaled together.  The process group is
    created with ``os.setsid()``, setting the "session id" to the process
    id of the current process.  All child processes inherit the session
    id, and since we only want it set in the shell created by
    :class:`Popen` and its descendants we don't call it in the parent
    process.  Instead, we pass it to Popen as the *preexec_fn* argument so
    it is run after the ``fork()`` inside the new process, before it calls
    ``exec()``.

この問題の解決方法は、親プロセスと一緒にシグナルを受け取るために子プロセスと連携する *プロセスグループ* を使用することです。プロセスグループはカレントプロセスのプロセス ID に対して "セッション ID" をセットする ``os.setsid()`` で作成されます。全ての子プロセスはそのセッション ID を継承します。そして :class:`Popen` とその子孫によって作成されたシェルのみにセッション ID をセットしたいので親プロセスではセッション ID を呼び出しません。その代わり、生成した新しいプロセスが ``exec()`` を呼び出す前に、そのプロセス内部で ``fork()`` 後に実行されるように Popen への引数として *preexec_fn* にセッション ID を渡します。

.. include:: subprocess_signal_setsid.py
    :literal:
    :start-after: #end_pymotw_header

..
    To signal the entire process group, we use ``os.killpg()`` with the
    pid value from our :class:`Popen` instance.

プロセスグループ全体へシグナルを送るために :class:`Popen` インスタンスの pid 値で ``os.killpg()`` を使用します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'subprocess_signal_setsid.py'))
.. }}}
.. {{{end}}}

..
    Conclusions
    ===========

まとめ
======

..
    As you can see, :mod:`subprocess` can be much easier to work with than
    fork, exec, and pipes on their own. It provides all of the
    functionality of the other modules and functions it replaces, and
    more. The API is consistent for all uses and many of the extra steps
    of overhead needed (such as closing extra file descriptors, ensuring
    the pipes are closed, etc.) are "built in" instead of being handled by
    your code separately.

ご覧の通り :mod:`subprocess` はプロセス独自に fork, exec や pipe を扱うよりもずっと簡単です。それは置き換え対象の他モジュールの全関数とそれ以上の機能を提供します。コードを分割して扱う代わりに "組み込み" に必要な(追加のファイルディスクリプタをクローズする、パイプがクローズされることを保証する等)オーバヘッドの追加処理の大半や他の全ての用途に対して一貫した API を使用することができます。

.. seealso::

    `subprocess <http://docs.python.org/lib/module-subprocess.html>`_
        .. Standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント

    :mod:`os`
        .. Although many are deprecated, the functions for working with processes
           found in the os module are still widely used in existing code.

        多くの関数が非推奨ではありますが os モジュールのプロセスと連携する関数は既存コードに広く使用されています

    `UNIX SIgnals and Process Groups <http://www.frostbytes.com/~jimf/papers/signals/signals.html>`_
        .. A good description of UNIX signaling and how process groups work.

        Unix シグナルとプロセスグループの動作についての優れた説明です

    `Advanced Programming in the UNIX(R) Environment <http://www.amazon.com/Programming-Environment-Addison-Wesley-Professional-Computing/dp/0201433079/ref=pd_bbs_3/002-2842372-4768037?ie=UTF8&s=books&amp;qid=1182098757&sr=8-3>`_
        .. Covers working with multiple processes, such as handling signals, closing duplicated
           file descriptors, etc.

        複数プロセスでのシグナル操作、重複ファイルディスクリプタのクローズ等の扱いについて説明します

    :mod:`pipes`
        .. Unix shell command pipeline templates in the standard library.

        標準ライブラリの Unix シェルコマンドラインテンプレート

