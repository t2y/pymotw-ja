..
    ###############################
    Communication Between Processes
    ###############################

##############
プロセス間通信
##############

..
    As with threads, a common use pattern for multiple processes is to
    divide a job up among several workers to run in parallel.  Effective
    use of multiple processes usually requires some communication between
    them, so that work can be divided and results can be aggregated.

スレッドのように、マルチプロセスの一般的な用途は並列で実行する複数のワーカーにジョブを分割することです。複数プロセスの効率的に使用するには普通はプロセス間通信を必要とします。そのため、その処理は分割されて結果が集約されます。

.. _multiprocessing-queues:

..
    Passing Messages to Processes
    =============================

プロセスへメッセージを渡す
==========================

..
    A simple way to communicate between process with
    :mod:`multiprocessing` is to use a :class:`Queue` to pass messages
    back and forth.  Any pickle-able object can pass through a
    :class:`Queue`.

:mod:`multiprocessing` でプロセス間通信を行う最も簡単な方法はメッセージを渡したり、返したりする :class:`Queue` を使用することです。pickle でシリアライズ可能なオブジェクトは :class:`Queue` を経由して渡すことができます。

.. include:: multiprocessing_queue.py
    :literal:
    :start-after: #end_pymotw_header

..
    This short example only passes a single message to a single worker,
    then the main process waits for the worker to finish.

この短いサンプルは1つのワーカーに対して1つのメッセージを渡しているだけで、メイン処理はワーカーの終了を待ちます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'multiprocessing_queue.py'))
.. }}}
.. {{{end}}}

..
    A more complex example shows how to manage several workers consuming
    data from a :class:`JoinableQueue` and passing results back to the
    parent process.  The *poison pill* technique is used to stop the
    workers.  After setting up the real tasks, the main program adds one
    "stop" value per worker to the job queue.  When a worker encounters
    the special value, it breaks out of its processing loop.  The main
    process uses the task queue's :func:`join` method to wait for all of
    the tasks to finish before processin the results.

もっと複雑なサンプルとして :class:`JoinableQueue` からデータを取り出して結果を親プロセスへ返す複数ワーカーを管理する方法を紹介します。 *poison pill* テクニックはワーカーを停止するために使用されます。実際のタスク設定後、メインプログラムはワーカー毎に "stop" 値をジョブキューへ追加します。ワーカーは特別な値に遭遇したときにその処理ループから脱出します。メインプロセスは、その結果を処理する前に全タスクの終了を待つためにタスクキューの :func:`join` メソッドを使用します。

.. include:: multiprocessing_producer_consumer.py
    :literal:
    :start-after: #end_pymotw_header

..
    Although the jobs enter the queue in order, since their execution is
    parallelized there is no guarantee about the order they will be
    completed.

ジョブは順番にキューへ追加されますが、追加されたジョブの実行は並列化されるのでジョブが完了する順番については保証されません。

.. {{{cog
.. cog.out(run_script(cog.inFile, '-u multiprocessing_producer_consumer.py'))
.. }}}
.. {{{end}}}


..
    Signaling between Processes
    ===========================

プロセス間でシグナルを送る
==========================

..
    The :class:`Event` class provides a simple way to communicate state
    information between processes.  An event can be toggled between set
    and unset states.  Users of the event object can wait for it to change
    from unset to set, using an optional timeout value.

:class:`イベント` クラスはプロセス間で状態に関する情報を通信する最も簡単な方法です。イベントは状態のセット/アンセットを切り替えることができます。Event オブジェクトを使用して、オプションのタイムアウト値でアンセットからセットへの変更イベントを待つことができます。

.. include:: multiprocessing_event.py
    :literal:
    :start-after: #end_pymotw_header

..
    When :func:`wait` times out it returns without an error.  The caller
    is responsible for checking the state of the event using
    :func:`is_set`.

:func:`wait` がタイムアウトするとき、イベントはエラーなく返します。呼び出し側は :func:`is_set` を使用してイベントの状態をチェックする責任があります。

.. {{{cog
.. cog.out(run_script(cog.inFile, '-u multiprocessing_event.py'))
.. }}}
.. {{{end}}}

..
    Controlling Access to Resources
    ===============================

リソースへのアクセスを制御する
==============================

..
    In situations when a single resource needs to be shared between
    multiple processes, a :class:`Lock` can be used to avoid conflicting
    accesses.

複数のプロセス間で1つのリソースを共有する必要があるような状況で :class:`Lock` は競合アクセスを避けるために使用されます。

.. include:: multiprocessing_lock.py
    :literal:
    :start-after: #end_pymotw_header

..
    In this example, the messages printed to the console may be jumbled
    together if the two processes do not synchronize their access of the
    output stream with the lock.

このサンプルでは、2つのプロセスがロックを使用して出力ストリームへのアクセスを同期しないとコンソールへのメッセージはごちゃ混ぜになる可能性があります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'multiprocessing_lock.py'))
.. }}}
.. {{{end}}}

..
    Synchronizing Operations
    ========================

同期オペレーション
==================

..
    :class:`Condition` objects can be used to synchronize parts of a
    workflow so that some run in parallel but others run sequentially,
    even if they are in separate processes.

:class:`Condition` オブジェクトは、たとえ独立したプロセスであっても、ワークフローの一部の処理は並列に実行されるように同期させて、その他の処理は連続的に実行させます。

.. include:: multiprocessing_condition.py
    :literal:
    :start-after: #end_pymotw_header

..
    In this example, two process run the second stage of a job in
    parallel, but only after the first stage is done.

このサンプルでは、2つのプロセスはジョブの2番目の stage を並列で実行しますが、1番目の stage が実行された後でのみです。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'multiprocessing_condition.py'))
.. }}}
.. {{{end}}}

..
    Controlling Concurrent Access to Resources
    ==========================================

リソースへの並列アクセスを制御する
==================================

..
    Sometimes it is useful to allow more than one worker access to a
    resource at a time, while still limiting the overall number. For
    example, a connection pool might support a fixed number of
    simultaneous connections, or a network application might support a
    fixed number of concurrent downloads. A :class:`Semaphore` is one way
    to manage those connections.

同時に1つのリソースへ2つ以上のワーカーからのアクセスを許容し、一方で全体のアクセス数を制限できると便利なときがあります。例えば、コネクションプールは同時接続数の最大数を制限するでしょうし、ネットワークアプリケーションは同時ダウンロード数の最大数を制限するでしょう。 :class:`Semaphore` はそういった接続を管理する方法の1つです。

.. include:: multiprocessing_semaphore.py
    :literal:
    :start-after: #end_pymotw_header

..
    In this example, the :class:`ActivePool` class simply serves as a
    convenient way to track which processes are running at a given
    moment. A real resource pool would probably allocate a connection or
    some other value to the newly active process, and reclaim the value
    when the task is done. Here, the pool is just used to hold the names
    of the active processes to show that only three are running
    concurrently.

このサンプルでは :class:`ActivePool` クラスはどのプロセスがあるタイミングで実行中かを追跡する簡単で便利な方法を提供します。実際のリソースプールは、おそらくコネクションか、その他の値を新たにアクティブなプロセスへ割り当てます。そして、アクティブなプロセスに割り当てられた処理が完了したときに、そのコネクションか何らかの値を再利用します。ここでサンプルのプールは、3つのプロセスのみが並列実行しているということを示すためにアクティブなプロセス名を保持するために使用されます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'multiprocessing_semaphore.py'))
.. }}}
.. {{{end}}}

..
    Managing Shared State
    =====================

共有状態を管理する
==================

..
    In the previous example, the list of active processes is maintained
    centrally in the :class:`ActivePool` instance via a special type of
    list object created by a :class:`Manager`.  The :class:`Manager` is
    responsible for coordinating shared information state between all of
    its users.

先ほどのサンプルでは、アクティブなプロセスのリストは :class:`Manager` によって作成されるリストオブジェクトの特別な型から :class:`ActivePool` インスタンスで保持されます。 :class:`Manager` はその全てのユーザ間で共有する情報を調整する責任があります。

.. include:: multiprocessing_manager_dict.py
    :literal:
    :start-after: #end_pymotw_header

..
    By creating the list through the manager, it is shared and updates are
    seen in all processes.  Dictionaries are also supported.

マネージャ経由でリストを作成することで全てのプロセスで共有されて更新されます。ディクショナリもサポートされます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'multiprocessing_manager_dict.py'))
.. }}}
.. {{{end}}}

..
    Shared Namespaces
    =================

共有ネームスペース
==================

..
    In addition to dictionaries and lists, a :class:`Manager` can create a
    shared :class:`Namespace`.

ディクショナリやリストに加えて :class:`Manager` は共有 :class:`Namespace` を作成することができます。

.. include:: multiprocessing_namespaces.py
    :literal:
    :start-after: #end_pymotw_header

..
    Any named value added to the :class:`Namespace` is visible to all of
    the clients that receive the :class:`Namespace` instance.

class:`Namespace` へ追加された名前付きの値は :class:`Namespace` インスタンスを受け取る全てのクライアントから見えます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'multiprocessing_namespaces.py'))
.. }}}
.. {{{end}}}

..
    It is important to know that *updates* to the contents of mutable
    values in the namespace are *not* propagated automatically.

Namespace に追加された可変コンテンツを *更新* しても自動的に伝播 *しない* ということを知っておくことが重要です。

.. include:: multiprocessing_namespaces_mutable.py
    :literal:
    :start-after: #end_pymotw_header

..
    To update the list, attach it to the namespace object again.

リストを更新するために、再度ネームスペースオブジェクトへそのリストをアタッチしてください。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'multiprocessing_namespaces_mutable.py'))
.. }}}
.. {{{end}}}

..
    Process Pools
    =============

プロセスプール
==============

..
    The :class:`Pool` class can be used to manage a fixed number of
    workers for simple cases where the work to be done can be broken up
    and distributed between workers independently.  The return values from
    the jobs are collected and returned as a list.  The pool arguments
    include the number of processes and a function to run when starting
    the task process (invoked once per child).

:class:`Pool` クラスは、対象処理が分解されて独立したワーカーに分散される単純な状況でワーカー数を指定して管理するために使用されます。そのジョブからの返り値は集められてリストとして返されます。pool 引数はタスクプロセスを開始するときに実行する関数やプロセスの数です(1つの子プロセスにつき1回実行される)。

.. include:: multiprocessing_pool.py
    :literal:
    :start-after: #end_pymotw_header

..
    The result of the :func:`map` method is functionally equivalent to the
    built-in :func:`map`, except that individual tasks run in parallel.
    Since the pool is processing its inputs in parallel, :func:`close` and
    :func:`join` can be used to synchronize the main process with the task
    processes to ensure proper cleanup.

:func:`map` メソッドの結果は、並列に個々のタスクが実行されること以外は機能的に組み込み関数の :func:`map` と機能的には同じです。プールは並列にその入力を処理するので :func:`close` や :func:`join` は、適切なクリーンアップを保証するためにメインプロセスにタスクプロセスを同期するために使用されます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'multiprocessing_pool.py'))
.. }}}
.. {{{end}}}

..
    By default :class:`Pool` creates a fixed number of worker processes
    and passes jobs to them until there are no more jobs.  Setting the
    *maxtasksperchild* parameter tells the pool to restart a worker
    process after it has finished a few tasks.  This can be used to avoid
    having long-running workers consume ever more system resources.

デフォルトでは :class:`Pool` は指定された数のワーカープロセスを作成します。そして、ジョブがなくなるまでそのワーカープロセスへジョブを渡します。 *maxtasksperchild* パラメータをセットすることは、数個のタスクが終了した後でワーカープロセスを再起動するようにプールへ伝えます。これは長時間実行中のワーカーがそれ以上にシステムリソースを消費しないようにするために行われます。

.. include:: multiprocessing_pool_maxtasksperchild.py
   :literal:
   :start-after: #end_pymotw_header

..
    The pool restarts the workers when they have completed their allotted
    tasks, even if there is no more work.  In this output, eight workers
    are created, even though there are only 10 tasks, and each worker can
    complete two of them at a time.

プールは割り当てたタスクを完了したときに、もし処理が無かったとしてもワーカーを再起動します。この出力では、8個のワーカーが作成されますが、10個のタスクしかないので、それぞれのワーカーのうち2つが同時に完了します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'multiprocessing_pool_maxtasksperchild.py'))
.. }}}
.. {{{end}}}

