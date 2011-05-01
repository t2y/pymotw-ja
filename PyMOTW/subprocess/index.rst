..
    ==============================================
     subprocess -- Work with additional processes
    ==============================================

=========================================
 subprocess -- プロセスを生成して連携する
=========================================

..
    :synopsis: Work with additional processes

.. module:: subprocess
    :synopsis: プロセスを生成して連携する

..
    :Purpose: Spawn and communicate with additional processes.
    :Available In: 2.4 and later

:目的: 新しくプロセスを生成してプロセスと通信する
:利用できるバージョン: 2.4 以上

..
    The :mod:`subprocess` module provides a consistent interface to
    creating and working with additional processes. It offers a
    higher-level interface than some of the other available modules, and
    is intended to replace functions such as :func:`os.system`,
    :func:`os.spawn*`, :func:`os.popen*`, :func:`popen2.*` and
    :func:`commands.*`. To make it easier to compare :mod:`subprocess`
    with those other modules, many of the examples here re-create the ones
    used for :mod:`os` and :mod:`popen`.

:mod:`subprocess` モジュールは新しくプロセスを生成して、そのプロセスを扱う一貫したインタフェースを提供します。それは従来からある他のモジュールよりも高レベルなインタフェースを提供します。そして :func:`os.system`, :func:`os.spawn*`, :func:`os.popen*`, :func:`popen2.*` や :func:`commands.*` のような従来の関数の置き換えを目的としています。 :mod:`subprocess` モジュールと他のモジュールとの比較を分かり易くするために :mod:`os` や :mod:`popen` を使用したサンプルを再作成して紹介します。

..
    The :mod:`subprocess` module defines one class, :class:`Popen` and a
    few wrapper functions that use that class. The constructor for
    :class:`Popen` takes arguments to set up the new process so the parent
    can communicate with it via pipes.  It provides all of the
    functionality of the other modules and functions it replaces, and
    more. The API is consistent for all uses, and many of the extra steps
    of overhead needed (such as closing extra file descriptors and
    ensuring the pipes are closed) are "built in" instead of being handled
    by the application code separately.

:mod:`subprocess` モジュールは :class:`Popen` とそのクラスを使用する複数のラッパ関数を定義します。 :class:`Popen` のコンストラクタは新たなプロセス生成を簡単にする複数の引数を受け取り、パイプを経由してその親プロセスと通信します。それは他のモジュールの置き換えられる全ての機能や関数とそれ以上の機能を提供します。どんな利用方法に対応できるように API が構成されています。そして、必要な(ファイルディスクリプタやパイプのクローズを保証するような)オーバヘッドの追加ステップの多くは、そのアプリケーションコードが独立して扱わずに "ビルトイン" です。

.. note::
    ..
        The API is roughly the same, but the underlying implementation is
        slightly different between Unix and Windows. All of the examples
        shown here were tested on Mac OS X. Behavior on a non-Unix OS will
        vary.
    
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

..
    The command line arguments are passed as a list of strings, which
    avoids the need for escaping quotes or other special characters that
    might be interpreted by the shell.

コマンドライン引数は文字列のリストとして渡されます。それはエスケープする必要性やシェルが解釈する可能性がある他の特殊文字を避けます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'subprocess_os_system.py'))
.. }}}
.. {{{end}}}

..
    Setting the *shell* argument to a true value causes :mod:`subprocess`
    to spawn an intermediate shell process, and tell it to run the
    command.  The default is to run the command directly.

*shell* 引数に ``True`` をセットすると :mod:`subprocess` はシェルを介してプロセスを生成して、コマンド実行するようにそのプロセスに伝えます。デフォルトでは、コマンドは直接実行します。

.. include:: subprocess_shell_variables.py
    :literal:
    :start-after: #end_pymotw_header

..
    Using an intermediate shell means that variables, glob patterns, and
    other special shell features in the command string are processed
    before the command is run.

シェルを介することで、コマンド文字列内の変数、glob パターンやその他の特殊なシェル機能がコマンドの実行前に処理されることになります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'subprocess_shell_variables.py'))
.. }}}
.. {{{end}}}

..
    Error Handling
    --------------

エラーハンドリング
------------------

..
    The return value from :func:`call` is the exit code of the program.
    The caller is responsible for interpreting it to detect errors.  The
    :func:`check_call` function works like :func:`call` except that the
    exit code is checked, and if it indicates an error happened then a
    :class:`CalledProcessError` exception is raised.

:func:`call` の返り値はそのプログラムの終了コードです。呼び出し側はエラーを検出するためにその終了コードを調べる責任があります。 :func:`check_call` 関数はその終了コードを確認すること以外は :func:`call` のように動作します。そして、もしエラーが発生した場合 :class:`CalledProcessError` 例外が発生します。

.. include:: subprocess_check_call.py
   :literal:
   :start-after: #end_pymotw_header

..
    The :command:`false` command always exits with a non-zero status code,
    which :func:`check_call` interprets as an error.

:command:`false` コマンドは常にゼロではないステータスコードで終了します。それは :func:`check_call` がエラーとして解釈します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'subprocess_check_call.py', ignore_error=True, break_lines_at=70))
.. }}}
.. {{{end}}}

..
    Capturing Output
    ----------------

出力を取得する
--------------

..
    The standard input and output channels for the process started by
    :func:`call` are bound to the parent's input and output.  That means
    the calling programm cannot capture the output of the command.  Use
    :func:`check_output` to capture the output for later processing.

:func:`call` が生成するプロセスの標準入力や標準出力のチャンネルは親の入出力に束縛されます。これは呼び出すプログラムはコマンドの出力を取得できないことを意味します。後続の処理のためにその出力を取得するために :func:`check_output` を使用してください。

.. include:: subprocess_check_output.py
   :literal:
   :start-after: #end_pymotw_header

..
    The ``ls -1`` command runs successfully, so the text it prints to
    standard output is captured and returned.

``ls -1`` コマンドは正常に実行するので、標準出力へ表示するテキストが取得されて返されます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'subprocess_check_output.py'))
.. }}}
.. {{{end}}}

..
    This script runs a series of commands in a subshell.  Messages are
    sent to standard output and standard error before the commands exit
    with an error code.

このスクリプトはサブシェル内で一連のコマンドを実行します。メッセージはコマンドがエラーコードで終了する前に標準出力と標準エラーに送られます。

.. include:: subprocess_check_output_error.py
   :literal:
   :start-after: #end_pymotw_header

..
    The message to standard error is printed to the console, but the
    message to standard output is hidden.

標準エラーへのメッセージはコンソールに表示されますが、標準出力へのメッセージは隠蔽されています。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'subprocess_check_output_error.py', ignore_error=True, break_lines_at=70))
.. }}}
.. {{{end}}}

..
    To prevent error messages from commands run through
    :func:`check_output` from being written to the console, set the
    *stderr* parameter to the constant :const:`STDOUT`.

エラーメッセージが :func:`check_output` を経由して実行されるコマンドからコンソールに書き込まれないようにするために *stderr* パラメータに定数 :const:`STDOUT` をセットします。

.. include:: subprocess_check_output_error_trap_output.py
   :literal:
   :start-after: #end_pymotw_header

..
    Now the error and standard output channels are merged together so if
    the command prints error messages, they are captured and not sent to
    the console.

いま、そのエラーと標準出力のチャンネルは一緒にまとめられます。そのため、コマンドがエラーメッセージを表示するなら、そのメッセージは取得されてコンソールには送られません。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'subprocess_check_output_error_trap_output.py', ignore_error=True, break_lines_at=70))
.. }}}
.. {{{end}}}



..
    Working with Pipes Directly
    ===========================

直接的にパイプと連携する
========================

..
    By passing different arguments for *stdin*, *stdout*, and *stderr* it
    is possible to mimic the variations of :func:`os.popen()`.

*stdin*, *stdout* や *stderr* に違う引数を渡すことで :func:`os.popen()` に類似した変形処理を行うことができます。


popen
-----

..
    To run a process and read all of its output, set the *stdout* value to
    :const:`PIPE` and call :func:`communicate`.

プロセスを実行してその全出力を読むには *stdout* に :const:`PIPE` をセットして :func:`communicate` を呼び出します。

.. include:: subprocess_popen_read.py
    :literal:
    :start-after: #end_pymotw_header

..
    This is similar to the way :func:`popen` works, except that the
    reading is managed internally by the :class:`Popen` instance.

これは、その読み込みが :class:`Popen` インスタンスによって内部的に管理されること以外は :func:`popen` の動作とよく似ています。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'subprocess_popen_read.py'))
.. }}}
.. {{{end}}}

..
    To set up a pipe to allow the calling program to write data to it, set
    *stdin* to :const:`PIPE`.

呼び出すプログラムからパイプにデータを書き込めるようにするには *stdin* に :const:`PIPE` をセットしてください。

.. include:: subprocess_popen_write.py
    :literal:
    :start-after: #end_pymotw_header

..
    To send data to the standard input channel of the process one time,
    pass the data to :func:`communicate`.  This is similar to using
    :func:`popen` with mode ``'w'``.

一度にプロセスの標準入力チャンネルへデータを送ることは :func:`communicate` へデータを渡します。これは :func:`popen` を ``'w'`` モードで使用するのによく似ています。

.. {{{cog
.. cog.out(run_script(cog.inFile, '-u subprocess_popen_write.py'))
.. }}}
.. {{{end}}}

popen2
------

..
    To set up the :class:`Popen` instance for reading and writing, use a
    combination of the previous techniques.

読み書きのために :class:`Popen` インスタンスを設定するには、前述したテクニックを組み合わせてください。

.. include:: subprocess_popen2.py
    :literal:
    :start-after: #end_pymotw_header

..
    This sets up the pipe to mimic :func:`popen2`.

これは :func:`popen2` によく似たパイプを設定します。

.. {{{cog
.. cog.out(run_script(cog.inFile, '-u subprocess_popen2.py'))
.. }}}
.. {{{end}}}

popen3
------

..
    It is also possible watch both of the streams for stdout and stderr,
    as with :func:`popen3`.

さらに :func:`popen3` のように stdout や stderr の両方のストリームを監視することもできます。

.. include:: subprocess_popen3.py
    :literal:
    :start-after: #end_pymotw_header

..
    Reading from stderr works the same as with stdout.  Passing
    :const:`PIPE` tells :class:`Popen` to attach to the channel, and
    :func:`communicate` reads all of the data from it before returning.

stderr からの読み込みは stdout と同じです。 :const:`PIPE` を渡すことはそのチャンネルにアタッチするために :class:`Popen` へ伝えます。そして :func:`communicate` は返される前にそこから全てのデータを読み込みます。

.. {{{cog
.. cog.out(run_script(cog.inFile, '-u subprocess_popen3.py'))
.. }}}
.. {{{end}}}

popen4
------

..
    To direct the error output from the process to its standard output
    channel, use :const:`STDOUT` for *stderr* instead of :const:`PIPE`.

プロセスの標準出力チャンネルへそのプロセスのエラー出力を繋ぐには、 :const:`PIPE` ではなく *stderr* に :const:`STDOUT` をセットしてください。

.. include:: subprocess_popen4.py
    :literal:
    :start-after: #end_pymotw_header

..
    Combining the output in this way is similar to how :func:`popen4`
    works.

この方法で出力を組み合わせることは :func:`popen4` の動作方法によく似ています。

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
    Multiple commands can be connected into a *pipeline*, similar to the
    way the Unix shell works, by creating separate :class:`Popen`
    instances and chaining their inputs and outputs together.  The
    :attr:`stdout` attribute of one :class:`Popen` instance is used as the
    *stdin* argument for the next in the pipeline, instead of the constant
    :const:`PIPE`.  The output is read from the :attr:`stdout` handle for
    the final command in the pipeline.

独立した :class:`Popen` インスタンスを作成して、その入力と出力を一緒に繋ぐことで、複数のコマンドは Unix シェルが扱うのとよく似た方法で *pipeline* に接続することができます。ある :class:`Popen` インスタンスの :attr:`stdout` 属性は、 :const:`PIPE` 定数の代わりにパイプラインの次の *stdin* 属性として使用されます。最終的な出力はパイプラインの最後のコマンドの :attr:`stdout` ハンドラからの読み込みます。

.. include:: subprocess_pipes.py
    :literal:
    :start-after: #end_pymotw_header

..
    This example reproduces the command line ``cat index.rst | grep
    ".. include" | cut -f 3 -d:``, which reads the reStructuredText source
    file for this section and finds all of the lines that include other
    files, then prints only the filenames.

このサンプルは ``cat index.rst | grep ".. include" | cut -f 3 -d:`` のコマンドラインを再現します。それは本セクションの reStructuredText ソースファイルを読み込み、全行から他のファイルの "include" を探して、そのファイル名のみを表示します。

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

上述した全てのサンプルは制限のあるプロセス間のやり取りを前提としていました。 :func:`communicate()` メソッドは全ての出力を読み込み、値を返す前に子プロセスの終了を待ちます。また :class:`Popen` インスタンスが使用する個々のパイプハンドラに読み書きすることもできます。標準入力から読み込んで標準出力へ書き込むシンプルな echo プログラムでこのことを説明します。

.. include:: repeater.py
    :literal:
    :start-after: #end_pymotw_header

..
    The script, ``repeater.py``, writes to stderr when it starts and
    stops. That information can be used to show the lifetime of the child
    process.

プログラムの開始時と終了時に ``repeater.py`` スクリプトが標準エラーに書き込みます。この情報は子プロセスのライフタイムを表すために使用されます。

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
    The ``"repeater.py: exiting"`` lines come at different points in the
    output for each loop style.

ループ毎に標準エラー出力の ``"repeater.py: exiting"`` 行が違う場所に出力されます。

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
    parent process

:mod:`os` のサンプルは :ref:`os.fork() や os.kill() を使用してシグナルを送る <creating-processes-with-os-fork>` デモも含みます。各 :class:`Popen` インスタンスは子プロセスのプロセス ID と一緒に *pid* 属性を提供するので :mod:`subprocess` でよく似た処理を行うことができます。例えば、親プロセスによって実行される子プロセスのために次のスクリプトを使用します。

.. include:: signal_child.py
    :literal:
    :start-after: #end_pymotw_header

..
    combined with this parent process

親プロセスで結合されます。

.. include:: signal_parent.py
    :literal:
    :start-after: #end_pymotw_header

..
    the output is:

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
    will be difficult to cause them to terminate by sending
    :const:`SIGINT` or :const:`SIGTERM`.

Unix 環境ではプロセスツリーという概念があり :mod:`Popen` で生成したプロセスがサブプロセスを生成する場合、そういった子プロセスは親プロセスからのシグナルを決して受け取りません。例えば :const:`SIGINT` か :const:`SIGTERM` を送ることでその子プロセスを終了させることが難しいということになります。

.. include:: subprocess_signal_parent_shell.py
    :literal:
    :start-after: #end_pymotw_header

..
    The pid used to send the signal does not match the pid of the child of
    the shell script waiting for the signal because in this example, there
    are three separate processes interacting:

シグナルを送るために使用された pid はシグナルを待つシェルスクリプトの子プロセスの pid と違っています。というのは、このサンプルは3つの独立したプロセスが相互に関連して存在します。

..
    1. ``subprocess_signal_parent_shell.py``
    2. The Unix shell process running the script created by the main python
       program.
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
    created with :func:`os.setsid`, setting the "session id" to the
    process id of the current process.  All child processes inherit the
    session id, and since it should only be set set in the shell created
    by :class:`Popen` and its descendants, :func:`os.setsid` should not be
    called in the parent process.  Instead, the function is passed to
    :class:`Popen` as the *preexec_fn* argument so it is run after the
    :func:`fork` inside the new process, before it uses :func:`exec` to
    run the shell.

この問題の解決方法は、親プロセスと一緒にシグナルを受け取るために子プロセスと連携する *プロセスグループ* を使用することです。プロセスグループはカレントプロセスのプロセス ID に対して "セッション ID" をセットする :func:`os.setsid` で作成されます。全ての子プロセスはそのセッション ID を継承します。そして :class:`Popen` とその子孫によって作成されたシェルのみにセッション ID をセットすべきなので :func:`os.setsid` を親プロセスで呼び出してはいけません。その代わり、その関数は *preexec_fn* 引数として :class:`Popen` へ渡されます。そのため、生成した新しいプロセスがシェルを実行するために :func:`exec` を呼び出す前に、そのプロセス内部で :func:`fork` した後で実行されます。

.. include:: subprocess_signal_setsid.py
    :literal:
    :start-after: #end_pymotw_header

..
    The sequence of events is:

イベントの順番は次のようになります。

..
    1. The parent program instantiates :class:`Popen`.
    2. The :class:`Popen` instance forks a new process.
    3. The new process runs :func:`os.setsid`.
    4. The new process runs :func:`exec` to start the shell.
    5. The shell runs the shell script.
    6. The shell script forks again and that process execs Python.
    7. Python runs ``signal_child.py``.
    8. The parent program signals the process group using the pid of the shell.
    9. The shell and Python processes receive the signal.  The shell
       ignores it.  Python invokes the signal handler.

1. 親プログラムが :class:`Popen` をインスタンス化する。
2. :class:`Popen` インスタンスが新しいプロセスを fork する。
3. 新しいプロセスが :func:`os.setsid` を実行する。
4. 新しいプロセスがシェルを開始するために :func:`exec` を実行する。
5. シェルがシェルスクリプトを実行する。
6. シェルスクリプトが再度 fork して、そのプロセスが Python を exec する。
7. Python は ``signal_child.py`` を実行する。
8. 親プログラムはシェルの pid を使用するプロセスグループへシグナルを送る。
9. シェルと Python のプロセスグループはシグナルを受け取る。シェルはそのシグナルを無視する。Python はシグナルハンドラを実行する。

..
    To signal the entire process group, use :func:`os.killpg` with the pid
    value from the :class:`Popen` instance.

プロセスグループへシグナルを送るには :class:`Popen` インスタンスからの pid 値を用いて :func:`os.killpg` を使用してください。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'subprocess_signal_setsid.py'))
.. }}}
.. {{{end}}}


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

        UNIX シグナル操作、プロセスグループの動作方法の優れた解説があります

    `Advanced Programming in the UNIX(R) Environment <http://www.amazon.com/Programming-Environment-Addison-Wesley-Professional-Computing/dp/0201433079/ref=pd_bbs_3/002-2842372-4768037?ie=UTF8&s=books&amp;qid=1182098757&sr=8-3>`_
        .. Covers working with multiple processes, such as handling signals, closing duplicated
           file descriptors, etc.

        複数プロセスでのシグナル操作、重複ファイルディスクリプタのクローズ等の扱いについて説明します

    :mod:`pipes`
        .. Unix shell command pipeline templates in the standard library.

        標準ライブラリの Unix シェルコマンドラインテンプレート
