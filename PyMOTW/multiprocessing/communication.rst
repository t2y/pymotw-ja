..
    ####################################################
    Communication between processes with multiprocessing
    ####################################################

################################
multiprocessing のプロセス間通信
################################

..
    Passing Messages to Processes
    =============================

.. _multiprocessing-queues:

プロセスへメッセージを渡す
==========================

..
    As with threads, a common use pattern for multiple processes is to
    divide a job up among several workers to run in parallel.  A simple
    way to do that with :mod:`multiprocessing` is to use Queues to pass
    messages back and forth.  Any pickle-able object can pass through a
    :mod:`multiprocessing` Queue.

スレッドのように、マルチプロセスの一般的な用途は並列で実行する複数のワーカーにジョブを分割することです。そういった処理を :mod:`multiprocessing` で実行する最も簡単な方法はメッセージを渡したり、返したりする Queue を使用することです。pickle でシリアライズ可能なオブジェクトは :mod:`multiprocessing` の Queue を通して渡すことができます。

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
    data from the queue and passing results back to the parent process.
    The *poison pill* technique is used to stop the workers.  After
    setting up the real tasks, the main program adds one "stop" value per
    worker to the job queue.  When a worker encounters the special value,
    it breaks out of its processing loop.

もっと複雑なサンプルとして、キューからデータを取り出して結果を親プロセスへ返す複数ワーカーを管理する方法を紹介します。 *poison pill* テクニックはワーカーを停止するために使用されます。実際のタスク設定後、メインプログラムはワーカー毎に "stop" 値をジョブキューへ追加します。ワーカーは特別な値に遭遇したときにその処理ループから脱出します。

.. include:: multiprocessing_producer_consumer.py
    :literal:
    :start-after: #end_pymotw_header

..
    Although the jobs enter the queue in order, since their execution is
    parallelized there is no guarantee about the order they will be
    completed.

ジョブは順番にキューへ追加されますが、追加されたジョブの実行は並列化されるのでジョブが完了する順番については保証されません。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'multiprocessing_producer_consumer.py'))
.. }}}
.. {{{end}}}


..
    Signaling between Processes with Event objects
    ==============================================

Event オブジェクトでプロセス間シグナルを送る
============================================

..
    Events provide a simple way to communicate state information between
    processes.  An event can be toggled between set and unset states.
    Users of the event object can wait for it to change from unset to set,
    using an optional timeout value.

イベントはプロセス間で状態に関する情報を通信する最も簡単な方法です。イベントは状態のセット/アンセットを切り替えることができます。Event オブジェクトを使用して、オプションのタイムアウト値でアンセットからセットへの変更イベントを待つことができます。

.. include:: multiprocessing_event.py
    :literal:
    :start-after: #end_pymotw_header

..
    When ``wait()`` times out it returns without an error.  The caller is
    responsible for checking the state of the event using ``is_set()``.

``wait()`` がタイムアウトするとき、イベントはエラーなく返します。呼び出し側は ``is_set()`` を使用してイベントの状態をチェックする責任があります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'multiprocessing_event.py'))
.. }}}
.. {{{end}}}

..
    Controlling access to resources with Lock
    =========================================

Lock でリソースへのアクセスを制御する
=====================================

..
    In situations when a single resource needs to be shared between
    multiple processes, a Lock can be used to avoid conflicting accesses.

複数のプロセス間で1つのリソースを共有する必要があるような状況で Lock は競合アクセスを避けるために使用されます。

.. include:: multiprocessing_lock.py
    :literal:
    :start-after: #end_pymotw_header

..
    In this example, the messages printed to stdout may be jumbled
    together if the two processes do not synchronize their access of the
    output stream with the lock.

このサンプルでは、2つのプロセスがロックを使用して出力ストリームへのアクセスを同期しないと標準出力へのメッセージはごちゃ混ぜになる可能性があります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'multiprocessing_lock.py'))
.. }}}
.. {{{end}}}

..
    Synchronizing threads with a Condition object
    =============================================

Condition オブジェクトでスレッドを同期する
==========================================

..
    Condition objects let you synchronize parts of a workflow so that some
    run in parallel but others run sequentially, even if they are in
    separate processes.

Condition オブジェクトは、たとえ独立したプロセスであっても、ワークフローの一部の処理は並列に実行されるように同期させて、その他の処理は連続的に実行させます。

.. include:: multiprocessing_condition.py
    :literal:
    :start-after: #end_pymotw_header

..
    In this example, two process run stage two of a job in parallel once
    the first stage is done.

このサンプルでは、2つのプロセスは stage_1 が完了した後で並列ジョブの stage_2 を実行します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'multiprocessing_condition.py'))
.. }}}
.. {{{end}}}

..
    Controlling concurrent access to resources with a Semaphore
    ===========================================================

Semaphore でリソースへの並列アクセスを制御する
==============================================

..
    Sometimes it is useful to allow more than one worker access to a
    resource at a time, while still limiting the overall number. For
    example, a connection pool might support a fixed number of
    simultaneous connections, or a network application might support a
    fixed number of concurrent downloads. A Semaphore is one way to manage
    those connections.

同時に1つのリソースへ2つ以上のワーカーからのアクセスを許容し、一方で全体のアクセス数を制限できると便利なときがあります。例えば、コネクションプールは同時接続数の最大数を制限するでしょうし、ネットワークアプリケーションは同時ダウンロード数の最大数を制限するでしょう。Semaphore はそういった接続を管理する方法の1つです。

.. include:: multiprocessing_semaphore.py
    :literal:
    :start-after: #end_pymotw_header

..
    In this example, the ActivePool class simply serves as a convenient
    way to track which process are running at a given moment. A real
    resource pool would probably allocate a connection or some other value
    to the newly active process, and reclaim the value when the task is
    done. Here, the pool is just used to hold the names of the active
    processes to show that only 3 are running concurrently.

このサンプルでは ActivePool クラスはどのプロセスがあるタイミングで実行中かを追跡する簡単で便利な方法を提供します。実際のリソースプールは、おそらくコネクションか、その他の値を新たにアクティブなプロセスへ割り当てます。そして、アクティブなプロセスに割り当てられた処理が完了したときに、そのコネクションか何らかの値を再利用します。ここでサンプルのプールは、3つのプロセスのみが並列実行しているということを示すためにアクティブなプロセス名を保持するために使用されます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'multiprocessing_semaphore.py'))
.. }}}
.. {{{end}}}

Managers
========

..
    In the previous example, the list of active processes is maintained
    centrally in the ActivePool instance via a special type of list object
    created by a Manager.  The Manager is responsible for coordinating
    shared information state between all of its users.  By creating the
    list through the manager, the list is updated in all processes when
    anyone modifies it.  Dictionaries are also supported.

先ほどのサンプルでは、アクティブなプロセスのリストは Manager によって作成されるリストオブジェクトの特別な型から ActivePool インスタンスで保持されます。Manager はその全てのユーザ間で共有する情報を調整する責任があります。Manager を通してリストを作成することで、あるプロセスがそのリストを変更したときに全てのプロセスでそのリストが更新されます。さらにディクショナリもサポートしています。

.. include:: multiprocessing_manager_dict.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'multiprocessing_manager_dict.py'))
.. }}}
.. {{{end}}}

Namespaces
==========

..
    In addition to dictionaries and lists, a Manager can create a shared
    Namespace.  Any named value added to the Namespace is visible across
    all of the clients.

ディクショナリやリストに加えて Manager は共有の Namespace を作成することができます。Namespace へ追加された名前付きの値は全てのクライアントからアクセスできます。

.. include:: multiprocessing_namespaces.py
    :literal:
    :start-after: #end_pymotw_header

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

.. {{{cog
.. cog.out(run_script(cog.inFile, 'multiprocessing_namespaces_mutable.py'))
.. }}}
.. {{{end}}}


Pool.map
========

..
    For simple cases where the work to be done can be broken up and
    distributed between workers, you do not have to manage the queue and
    worker processes yourself.  The Pool class maintains a fixed number of
    workers and passes them jobs.  The return values are collected and
    returned as a list.  The result is functionally equivalent to the
    built-in ``map()``, except that individual tasks run in parallel.

処理が分割できてワーカー間に分散される簡単なケースでは、キューとワーカープロセスそのものを管理する必要はありません。Pool クラスはワーカーの最大数を設けて、それらのワーカーへジョブを渡します。その返り値はリストとして集約されて返されます。そして、その結果は個々のタスクが並列に実行されることを除けば、ビルトイン関数の ``map()`` と機能的に同じです。

.. include:: multiprocessing_pool.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'multiprocessing_pool.py'))
.. }}}
.. {{{end}}}
