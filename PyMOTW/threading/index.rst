..
    ======================================
    threading -- Manage concurrent threads
    ======================================

=============================================
threading -- スレッドによる並列処理を管理する
=============================================

..
    :synopsis: Manage several concurrent threads of execution.

.. module:: threading
    :synopsis: スレッドによる並列処理を管理する

..
    :Purpose: Builds on the :mod:`thread` module to more easily manage several threads of execution.
    :Available In: 1.5.2 and later

:目的: :mod:`thread` モジュールを使用して複数スレッドの実行を簡単に管理する
:利用できるバージョン: 1.5.2 以上

..
    The :mod:`threading` module builds on the low-level features of
    :mod:`thread` to make working with threads even easier and more
    *pythonic*. Using threads allows a program to run multiple operations
    concurrently in the same process space.

:mod:`threading` モジュールは、スレッドを扱う :mod:`thread` の低レベルな機能をさらに簡単で *pythonic* に提供します。スレッドを使用すると、プログラムは1つのプロセス空間で複数の処理を並行に実行できます。

..
    Thread Objects
    ==============

Thread オブジェクト
===================

..
    The simplest way to use a :class:`Thread` is to instantiate it with a
    target function and call :func:`start()` to let it begin working.

:class:`Thread` を使用する最も簡単な方法は、実行させる関数と共に :class:`Thread` クラスをインスタンス化して、処理を開始させるために :func:`start()` を呼び出します。

.. include:: threading_simple.py
    :literal:
    :start-after: #end_pymotw_header

..
    The output is five lines with ``"Worker"`` on each:

それぞれのスレッドで出力される ``"Worker"`` が5行出力されます。

::

	$ python threading_simple.py

	Worker
	Worker
	Worker
	Worker
	Worker

..
    It useful to be able to spawn a thread and pass it arguments to tell
    it what work to do. This example passes a number, which the thread
    then prints.

スレッドを生成して、そのスレッドへどんな処理を実行させるのかを引数で渡せるのは便利です。このサンプルは数字を渡して、それぞれのスレッドが引数で渡された数を表示します。

.. include:: threading_simpleargs.py
    :literal:
    :start-after: #end_pymotw_header

..
    The integer argument is now included in the message printed by each
    thread:

引数の数字は、それぞれのスレッドが出力するメッセージに含まれています。

::

	$ python -u threading_simpleargs.py
    
    Worker: 0
    Worker: 1
    Worker: 2
    Worker: 3
    Worker: 4

..
    Determining the Current Thread
    ==============================

カレントスレッドを決める
========================

..
    Using arguments to identify or name the thread is cumbersome, and
    unnecessary.  Each :class:`Thread` instance has a name with a default
    value that can be changed as the thread is created. Naming threads is
    useful in server processes with multiple service threads handling
    different operations.

引数を使用してスレッドを識別したり名前付けしたりすることは、面倒であり不要です。それぞれの :class:`Thread` インスタンスは、デフォルトで名前をもっていて、スレッド生成時に変更できます。スレッドに名前を付けることは、別の処理を扱う複数のサービスをもつサーバプロセスで便利です。

.. include:: threading_names.py
    :literal:
    :start-after: #end_pymotw_header

..
    The debug output includes the name of the current thread on each
    line. The lines with ``"Thread-1"`` in the thread name column
    correspond to the unnamed thread :data:`w2`.

デバッグ出力にカレントスレッドの名前が含まれます。スレッド名のカラムに ``"Thread-1"`` がある行は、名前を付けていない :data:`w2` に対応するスレッドです。

.. {{{cog
.. cog.out(run_script(cog.inFile, '-u threading_names.py'))
.. }}}
.. {{{end}}}

..
    Most programs do not use :command:`print` to debug. The
    :mod:`logging` module supports embedding the thread name in every log
    message using the formatter code ``%(threadName)s``. Including thread
    names in log messages makes it easier to trace those messages back to
    their source.

ほとんどのプログラムは、デバッグに :command:`print` を使用しません。 :mod:`logging` モジュールは、 ``%(threadName)s`` というフォーマッタを使用して全てのログメッセージにスレッド名を組み込みます。ログメッセージにスレッド名を含めると、ソースを見返してトレースするのが簡単になります。

.. include:: threading_names_log.py
    :literal:
    :start-after: #end_pymotw_header

..
    :mod:`logging` is also thread-safe, so messages from different threads
    are kept distinct in the output.

:mod:`logging` もまたスレッドセーフなので、別のスレッドからのメッセージは区別して出力します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'threading_names_log.py'))
.. }}}
.. {{{end}}}

..
    Daemon vs. Non-Daemon Threads
    =============================

デーモンと非デーモンスレッド
============================

..
    Up to this point, the example programs have implicitly waited to exit
    until all threads have completed their work. Sometimes programs spawn
    a thread as a *daemon* that runs without blocking the main program
    from exiting. Using daemon threads is useful for services where there
    may not be an easy way to interrupt the thread or where letting the
    thread die in the middle of its work does not lose or corrupt data
    (for example, a thread that generates "heart beats" for a service
    monitoring tool). To mark a thread as a daemon, call its
    :func:`setDaemon()` method with a boolean argument. The default is for
    threads to not be daemons, so passing True turns the daemon mode on.

これまでのサンプルプログラムは、全てのスレッドの処理が完了するまで明示的に終了するのを待っていました。終了しなくてもメインプログラムをブロッキングすることなく *daemon* としてスレッドを生成するときがあります。デーモンスレッドを使用することは、スレッドを中断する簡単な方法がない、もしくはデータを破損したり失ったりせずに処理の途中でスレッドを終了させるようなサービスで便利です(例えば、サービス監視ツールで "心電図" を生成するスレッド)。スレッドをデーモンにするには、その :func:`setDaemon()` メソッドにブーリアン値を渡して呼び出します。デフォルトでは、スレッドはデーモンではないので、デーモンモードを有効にするために True を渡します。

.. include:: threading_daemon.py
    :literal:
    :start-after: #end_pymotw_header

..
    Notice that the output does not include the ``"Exiting"`` message from
    the daemon thread, since all of the non-daemon threads (including the
    main thread) exit before the daemon thread wakes up from its two second
    sleep.

デーモンスレッドは2秒間の sleep から起きる前に全ての非デーモンスレッドは終了するので、結果の出力には、デーモンスレッドの ``"Exiting"`` のメッセージが含まれていないことに注意してください。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'threading_daemon.py'))
.. }}}
.. {{{end}}}

..
    To wait until a daemon thread has completed its work, use the
    :func:`join()` method.

デーモンスレッドの処理が完了するまで待つには、 :func:`join()` メソッドを使用してください。

.. include:: threading_daemon_join.py
    :literal:
    :start-after: #end_pymotw_header

..
    Waiting for the daemon thread to exit using :func:`join()` means it
    has a chance to produce its ``"Exiting"`` message.

:func:`join()` でデーモンスレッドの終了を待つことで ``"Exiting"`` メッセージを出力する機会ができました。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'threading_daemon_join.py'))
.. }}}
.. {{{end}}}

..
    By default, :func:`join()` blocks indefinitely. It is also possible to
    pass a timeout argument (a float representing the number of seconds to
    wait for the thread to become inactive). If the thread does not
    complete within the timeout period, :func:`join()` returns anyway.

デフォルトでは :func:`join()` は無期限にブロックします。また引数で ``timeout`` (スレッドが非アクティブになるために待つ秒を小数で表す)も渡せます。スレッドが ``timeout`` で設定した時間内に完了しなくても :func:`join()` が返されます。

.. include:: threading_daemon_join_timeout.py
    :literal:
    :start-after: #end_pymotw_header

..
    Since the timeout passed is less than the amount of time the daemon
    thread sleeps, the thread is still "alive" after :func:`join()`
    returns.

渡された ``timeout`` は、デーモンスレッドが sleep する時間よりも小さいので、 :func:`join()` が返された後でもスレッドはまだ "生きています" 。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'threading_daemon_join_timeout.py'))
.. }}}
.. {{{end}}}

..
    Enumerating All Threads
    =======================

全てのスレッドを列挙する
========================

..
    It is not necessary to retain an explicit handle to all of the daemon
    threads in order to ensure they have completed before exiting the main
    process. :func:`enumerate()` returns a list of active :class:`Thread`
    instances. The list includes the current thread, and since joining the
    current thread is not allowed (it introduces a deadlock situation), it
    must be skipped.

メインプロセスが終了する前に、全てのデーモンスレッドが完了していることを保証するためにそういったデーモンスレッドの明示的なハンドラを保持する必要はありません。 :func:`enumerate()` は、アクティブな :class:`Thread` インスタンスのリストを返します。このリストには、カレントスレッドも含まれています。カレントスレッドを :func:`join()` することはできないので(デッドロックを発生させる)、カレントスレッドは読み飛ばさなければなりません。

.. include:: threading_enumerate.py
    :literal:
    :start-after: #end_pymotw_header

..
    Since the worker is sleeping for a random amount of time, the output
    from this program may vary. It should look something like this:

ワーカースレッドは乱数で与えた時間を sleep するので、このプログラムの出力結果は変わる可能性があります。例えば、次のようになります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'threading_enumerate.py'))
.. }}}
.. {{{end}}}

..
    Subclassing Thread
    ==================

スレッドをサブクラス化する
==========================

..
    At start-up, a :class:`Thread` does some basic initialization and then
    calls its :func:`run()` method, which calls the target function passed
    to the constructor. To create a subclass of :class:`Thread`, override
    :func:`run()` to do whatever is necessary.

開始時に :class:`Thread` は、基本的な初期化を行ってからコンストラクタへ渡された関数を呼び出す :func:`run()` メソッドを呼び出します。 :class:`Thread` のサブクラスを作成するには、必要な処理を行う :func:`run()` をオーバーライドしてください。

.. include:: threading_subclass.py
    :literal:
    :start-after: #end_pymotw_header

..
    The return value of :func:`run` is ignored.

:func:`run` の返り値は無視されます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'threading_subclass.py'))
.. }}}
.. {{{end}}}

..
    Because the *args* and *kwargs* values passed to the :class:`Thread`
    constructor are saved in private variables, they are not easily
    accessed from a subclass.  To pass arguments to a custom thread type,
    redefine the constructor to save the values in an instance attribute
    that can be seen in the subclass.

:class:`Thread` コンストラクタへ渡される *args* と *kwargs* の値はプライベートな変数に保存されるので、そういった引数はサブクラスから簡単にアクセスできません。カスタムスレッドへ引数を渡すには、サブクラスからみえるようにインスタンス変数に値を保存するようにコンストラクタを再定義します。

.. include:: threading_subclass_args.py
   :literal:
   :start-after: #end_pymotw_header

..
    :class:`MyThreadWithArgs` uses the same API as :class:`Thread`, but
    another class could easily change the constructor method to take more
    or different arguments more directly related to the purpose of the
    thread, as with any other class.

:class:`MyThreadWithArgs` は :class:`Thread` と同じ API を使用しますが、別のクラスです。そのコンストラクタメソッドはさらに引数を取る、もしくは任意のクラスのようにスレッドの目的に直結した別の引数を取るように簡単に変更できます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'threading_subclass_args.py'))
.. }}}
.. {{{end}}}

..
    Timer Threads
    =============

タイマースレッド
================

..
    One example of a reason to subclass :class:`Thread` is provided by
    :class:`Timer`, also included in :mod:`threading`. A :class:`Timer`
    starts its work after a delay, and can be canceled at any point within
    that delay time period.

:class:`Timer` は :class:`Thread` をサブクラス化する理由の1つでもあり、 :mod:`threading` で提供されています。 :class:`Timer` は処理の開始を遅延させて、遅延時間内であればいつでも中止できます。

.. include:: threading_timer.py
    :literal:
    :start-after: #end_pymotw_header

..
    Notice that the second timer is never run, and the first timer appears
    to run after the rest of the main program is done. Since it is not a
    daemon thread, it is joined implicitly when the main thread is done.

2番目のタイマーは決して実行されず、メインプログラムの残りの部分が終了した後で最初のタイマーが実行されて表示されることに注意してください。これはデーモンスレッドではないので、メインスレッドが終了したときに、暗黙的に ``join`` されます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'threading_timer.py'))
.. }}}
.. {{{end}}}

..
    Signaling Between Threads
    =========================

スレッド間でシグナルを送る
==========================

..
    Although the point of using multiple threads is to spin separate
    operations off to run concurrently, there are times when it is
    important to be able to synchronize the operations in two or more
    threads. A simple way to communicate between threads is using
    :class:`Event` objects. An :class:`Event` manages an internal flag
    that callers can either :func:`set()` or :func:`clear()`. Other
    threads can :func:`wait()` for the flag to be :func:`set()`,
    effectively blocking progress until allowed to continue.

複数スレッドを使用する本質的なところは、並列に実行するために処理を分離させることです。しかし、2つ以上のスレッドで処理を同期するのが重要なときがあります。スレッド間で通信する簡単な方法として :class:`Event` オブジェクトを使用します。 :class:`Event` は、 :func:`set()` か :func:`clear()` のどちらかで内部でフラグを管理します。他のスレッドは、後続の処理ができるようになるまで効率的にブロッキングして、そのフラグが :func:`set()` になるまで :func:`wait()` できます。

.. include:: threading_event.py
    :literal:
    :start-after: #end_pymotw_header

..
    The :func:`wait` method takes an argument representing the number of
    seconds to wait for the event before timing out.  It returns a boolean
    indicating whether or not the event is set, so the caller knows why
    :func:`wait` returned.  The :func:`isSet` method can be used
    separately on the event without fear of blocking.

:func:`wait` メソッドは、タイムアウトする前にイベントを待つ時間を表す秒を引数で取ります。これはイベントがセットされているかどうかを示すブーリアン値を返すので、呼び出し側は :func:`wait` が返された理由が分かります。 :func:`isSet` メソッドは、ブロッキングせずに個別のイベントで使用できます。

..
    In this example, :func:`wait_for_event_timeout` checks the event
    status without blocking indefinitely.  The :func:`wait_for_event`
    blocks on the call to :func:`wait`, which does not return until the
    event status changes.

このサンプルでは、 :func:`wait_for_event_timeout` はずっとブロッキングせずにイベントステータスを確認します。 :func:`wait_for_event` は、イベントステータスが変更されるまで返ってこない :func:`wait` の呼び出しをブロックします。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'threading_event.py'))
.. }}}
.. {{{end}}}

..
    Controlling Access to Resources
    ===============================

リソースへのアクセスを制御する
==============================

..
    In addition to synchronizing the operations of threads, it is also
    important to be able to control access to shared resources to prevent
    corruption or missed data. Python's built-in data structures (lists,
    dictionaries, etc.) are thread-safe as a side-effect of having atomic
    byte-codes for manipulating them (the GIL is not released in the
    middle of an update). Other data structures implemented in Python, or
    simpler types like integers and floats, don't have that protection. To
    guard against simultaneous access to an object, use a :class:`Lock`
    object.

スレッドの処理を同期することに加えて、データを破壊したり失わないように共有リソースへのアクセスを制御することも重要です。Python の組み込みデータ構造は、バイトコードの扱いがアトミックになる副作用からスレッドセーフです(GIL は途中で解放しません)。Python で実装された別のデータ構造、または整数や小数のようなシンプルな型はそういった保護機構がありません。そういったオブジェクトへの同時アクセスを防ぐには :class:`Lock` オブジェクトを使用してください。

.. include:: threading_lock.py
    :literal:
    :start-after: #end_pymotw_header

..
    In this example, the :func:`worker()` function increments a
    :class:`Counter` instance, which manages a :class:`Lock` to prevent
    two threads from changing its internal state at the same time. If the
    :class:`Lock` was not used, there is a possibility of missing a change
    to the value attribute.

このサンプルでは、 :func:`worker()` 関数は :class:`Counter` インスタンスを増加させます。これは2つのスレッドが同時にその内部状態を変更しないように :class:`Lock` を管理します。 :class:`Lock` を使用しないと :attr:`value` 属性の変更が失われる可能性があります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'threading_lock.py'))
.. }}}
.. {{{end}}}

..
    To find out whether another thread has acquired the lock without
    holding up the current thread, pass False for the *blocking* argument
    to :func:`acquire()`. In the next example, :func:`worker()` tries to
    acquire the lock three separate times, and counts how many attempts it
    has to make to do so. In the mean time, :func:`lock_holder` cycles
    between holding and releasing the lock, with short pauses in each
    state used to simulate load.

別のスレッドがカレントスレッドを待たせずにロックを獲得しているかどうかを確認するには、 :func:`acquire()` の *blocking* 引数に False を渡してください。次のサンプルでは、 :func:`worker()` が3回ロックを獲得しようとして、何回そうしようとしたかを数えます。その一方で :func:`lock_holder` は負荷を模倣するためにロックを獲得したときと解放したときに少し一時停止して、ロックの獲得と解法を繰り返します。

.. include:: threading_lock_noblock.py
    :literal:
    :start-after: #end_pymotw_header

..
    It takes :func:`worker` more than three iterations to acquire the lock
    three separate times.

:func:`worker` は、3回のロックを獲得するために3回以上のループを繰り返します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'threading_lock_noblock.py'))
.. }}}
.. {{{end}}}

..
    Re-entrant Locks
    ----------------

再入可能なロック
----------------

..
    Normal :class:`Lock` objects cannot be acquired more than once, even
    by the same thread. This can introduce undesirable side-effects if a
    lock is accessed by more than one function in the same call chain.

普通の :class:`Lock` オブジェクトは、同じスレッドであっても複数回、獲得できません。ロックが同じコールチェーン内の複数の関数からアクセスされる場合、望ましくない副作用が発生します。

.. include:: threading_lock_reacquire.py
    :literal:
    :start-after: #end_pymotw_header

..
    In this case, since both functions are using the same global lock, and
    one calls the other, the second acquisition fails and would have
    blocked using the default arguments to :func:`acquire()`.

この場合、両方の関数は同じグローバルロックを使用するので、一方が他方を呼び出すと、2番目のロック獲得が失敗して :func:`acquire()` へのデフォルト引数を使用してブロックされます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'threading_lock_reacquire.py'))
.. }}}
.. {{{end}}}

..
    In a situation where separate code from the same thread needs to
    "re-acquire" the lock, use an :class:`RLock` instead.

同じスレッドから別のコードがロックを獲得する必要がある状況では、代わりに :class:`RLock` を使用してください。

.. include:: threading_rlock.py
    :literal:
    :start-after: #end_pymotw_header

..
    The only change to the code from the previous example was substituting
    :class:`RLock` for :class:`Lock`.

前のサンプルコードからの変更は :class:`Lock` を :class:`RLock` に置き換えただけです。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'threading_rlock.py'))
.. }}}
.. {{{end}}}

..
    Locks as Context Managers
    -------------------------

コンテキストマネージャとしてのロック
------------------------------------

..
    Locks implement the context manager API and are compatible with the
    :command:`with` statement.  Using :command:`with` removes the need to
    explicitly acquire and release the lock.

ロックは、コンテキストマネージャ API を実装して :command:`with` 文と互換性があります。 :command:`with` 文を使用すると、明示的にロックを獲得して解放する必要がなくなります。
    
.. include:: threading_lock_with.py
    :literal:
    :start-after: #end_pymotw_header

..
    The two functions :func:`worker_with()` and :func:`worker_no_with()`
    manage the lock in equivalent ways.

:func:`worker_with()` と :func:`worker_no_with()` の2つの関数は、同等の方法でロックを管理します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'threading_lock_with.py'))
.. }}}
.. {{{end}}}

..
    Synchronizing Threads
    =====================

スレッドを同期する
==================

..
    In addition to using :class:`Events`, another way of synchronizing
    threads is through using a :class:`Condition` object. Because the
    :class:`Condition` uses a :class:`Lock`, it can be tied to a shared
    resource. This allows threads to wait for the resource to be updated.
    In this example, the :func:`consumer()` threads :func:`wait()` for the
    :class:`Condition` to be set before continuing. The :func:`producer()`
    thread is responsible for setting the condition and notifying the
    other threads that they can continue.

:class:`Events` を使用することに加えて、 :class:`Condition` オブジェクトを使用してスレッドを同期する別の方法があります。 :class:`Condition` は :class:`Lock` を使用するので共有リソースに関連しています。これはスレッドにリソースが更新されるのを待たせます。このサンプルでは、 :func:`consumer()` スレッドは、処理を継続する前にセットされる :class:`Condition` を :func:`wait()` します。 :func:`producer()` スレッドは、状態をセットして別のスレッドが処理を継続できるように変更する責任をもちます。

.. include:: threading_condition.py
    :literal:
    :start-after: #end_pymotw_header

..
    The threads use :command:`with` to acquire the lock associated with
    the :class:`Condition`. Using the :func:`acquire()` and
    :func:`release()` methods explicitly also works.

スレッドは :class:`Condition` に関連付けられたロックを獲得する :command:`with` 文を使用します。 :func:`acquire()` と :func:`release()` メソッドを明示的に使用しても同様に動作します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'threading_condition.py'))
.. }}}
.. {{{end}}}

..
    Limiting Concurrent Access to Resources
    =======================================

リソースへの同時アクセスを制限する
==================================

..
    Sometimes it is useful to allow more than one worker access to a
    resource at a time, while still limiting the overall number. For
    example, a connection pool might support a fixed number of
    simultaneous connections, or a network application might support a
    fixed number of concurrent downloads. A :class:`Semaphore` is one way
    to manage those connections.

アクセスできる全体の数を制限しながら、複数のワーカーから1つのリソースへ同時にアクセスできると便利なときがあります。例えば、コネクションプールは同時接続数の最大数を制限したり、ネットワークアプリケーションは同時ダウンロード数の最大数を制限します。 :class:`Semaphore` はそういったコネクション数を制御する方法の1つです。

.. include:: threading_semaphore.py
    :literal:
    :start-after: #end_pymotw_header

..
    In this example, the :class:`ActivePool` class simply serves as a
    convenient way to track which threads are able to run at a given
    moment. A real resource pool would allocate a connection or some other
    value to the newly active thread, and reclaim the value when the
    thread is done. Here it is just used to hold the names of the active
    threads to show that only five are running concurrently.

このサンプルでは、 :class:`ActivePool` クラスは、どのスレッドがあるタイミングで実行できるかを追跡する簡単で便利な方法を提供します。実際のリソースプールはコネクションか、新たなアクティブスレッドへの他の値を割り合てて、スレッドが終了したときにその値を再利用します。2つのスレッドのみ並列に実行されているのを表すために、アクティブなスレッドの名前を保持するだけのサンプルがあります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'threading_semaphore.py'))
.. }}}
.. {{{end}}}

..
    Thread-specific Data
    ====================

スレッド固有のデータ
====================

..
    While some resources need to be locked so multiple threads can use
    them, others need to be protected so that they are hidden from view in
    threads that do not "own" them. The :func:`local()` function creates
    an object capable of hiding values from view in separate threads.

リソースによってはロックにより複数のスレッドでも利用できますが、その他のリソースを "所有" していないスレッドからみえないように保護する必要があります。 :func:`local()` 関数は、別のスレッドからみえない値を保持するオブジェクトを作成します。

.. include:: threading_local.py
    :literal:
    :start-after: #end_pymotw_header

..
    Notice that ``local_data.value`` is not present for any thread until
    it is set in that thread.

``local_data.value`` は、そのスレッドでセットされるまで他のスレッドからみると存在しないことに注意してください。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'threading_local.py'))
.. }}}
.. {{{end}}}

..
    To initialize the settings so all threads start with the same value,
    use a subclass and set the attributes in :func:`__init__`.

全てのスレッドが同じ値で開始されるように設定を初期化するには、サブクラス化して :func:`__init__` で :attr:`value` 属性をセットしてください。

.. include:: threading_local_defaults.py
    :literal:
    :start-after: #end_pymotw_header

..
    :func:`__init__` is invoked on the same object (note the :func:`id`
    value), once in each thread.

:func:`__init__` は、それぞれのスレッドで一度だけ同じオブジェクト(:func:`id` の値に着目)で実行されます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'threading_local_defaults.py'))
.. }}}
.. {{{end}}}

.. seealso::
    
    `threading <http://docs.python.org/lib/module-threading.html>`_
        .. Standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント

    :mod:`thread`
        .. Lower level thread API.

        低レベルスレッド API
    
    :mod:`Queue`
        .. Thread-safe Queue, useful for passing messages between threads.

        スレッド間でメッセージパッシングに便利なスレッドセーフなキュー

    :mod:`multiprocessing`
        .. An API for working with processes that mirrors the :mod:`threading` API.

        :mod:`threading` API のようにマルチプロセスで動作する API
