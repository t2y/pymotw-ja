..
    ==========================================
    Queue -- A thread-safe FIFO implementation
    ==========================================

=====================================
Queue -- スレッドセーフな FIFO の実装
=====================================

..
    :synopsis: Provides a thread-safe FIFO implementation

.. module:: Queue
    :synopsis: スレッドセーフな FIFO の実装を提供する

..
    :Purpose: Provides a thread-safe FIFO implementation
    :Available In: at least 1.4

:目的: スレッドセーフな FIFO の実装を提供する
:利用できるバージョン: 1.4 以上

..
    The :mod:`Queue` module provides a FIFO implementation suitable for
    multi-threaded programming. It can be used to pass messages or other
    data between producer and consumer threads safely. Locking is handled
    for the caller, so it is simple to have as many threads as you want
    working with the same Queue instance. A Queue's size (number of
    elements) may be restricted to throttle memory usage or processing.

:mod:`Queue` モジュールは、マルチスレッドプログラミングに適した FIFO の実装を提供します。それはメッセージかその他のデータを渡して安全にスレッドを実行するために使用されます。呼び出し側をロックすることで、同じキューインスタンスで多くのスレッドと連携するのが簡単になります。Queue のサイズ(要素数)は、メモリ使用量または処理を調整するために制限される可能性があります。

.. note::

    .. This discussion assumes you already understand the general nature
       of a queue. If you don't, you may want to read some of the
       references before continuing.

    この記事はあなたが既に一般的なキューの特性を理解していることを前提としています。もしそうではないなら、この後の記事を読む前に他の参考文献を読んでみてください。

..
    Basic FIFO Queue
    ================

基本的な FIFO キュー
====================

..
    The ``Queue`` class implements a basic first-in, first-out container.
    Elements are added to one "end" of the sequence using ``put()``, and
    removed from the other end using ``get()``.

``Queue`` クラスは基本的な先入先出のコンテナを実装します。要素は :func:`put` でシーケンスの "一端" に追加され、 :func:`get` でもう一方の端から削除されます。

.. include:: Queue_fifo.py
   :literal:
   :start-after: #end_pymotw_header

..
    This example uses a single thread to illustrate that elements are
    removed from the queue in the same order they are inserted.

このサンプルは、追加された順番でキューから要素が削除されるのを説明するためにシングルスレッドで実行します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'Queue_fifo.py'))
.. }}}

::

	$ python Queue_fifo.py
	
	0
	1
	2
	3
	4

.. {{{end}}}

..
    LIFO Queue
    ==========

LIFO キュー
===========

..
    In contrast to the standard FIFO implementation of ``Queue``, the
    ``LifoQueue`` uses last-in, first-out ordering (normally associated
    with a stack data structure).

標準的な ``Queue`` の FIFO 実装と比較して、 ``LifoQueue`` は後入先出の順番になります(通常はスタックのデータ構造と関連します)。

.. include:: Queue_lifo.py
   :literal:
   :start-after: #end_pymotw_header

..
    The item most recently ``put()`` into the queue is removed by
    ``get()``.

:func:`put` でキューへ追加された最新の要素が :func:`get` で削除されます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'Queue_lifo.py'))
.. }}}

::

	$ python Queue_lifo.py
	
	4
	3
	2
	1
	0

.. {{{end}}}

.. _Queue-PriorityQueue:

優先キュー
==========

..
    Priority Queue
    ==============

..
    Sometimes the processing order of the items in a queue needs to be
    based on characteristics of those items, rather than just the order
    they are created or added to the queue.  For example, print jobs from
    the payroll department may take precedence over a code listing printed
    by a developer.  ``PriorityQueue`` uses the sort order of the contents
    of the queue to decide which to retrieve.

その要素が作成されてキューへ追加された順番よりも、そのキュー内の要素の特性に基づいて処理しなければならないときがあります。例えば、人事部からのお仕事の表示は、開発者が優先度を高くしてリストに表示するかもしれません。 ``PriorityQueue`` は、要素の取り出しを決定するキューのコンテンツのソート順序を使用します。

.. include:: Queue_priority.py
   :literal:
   :start-after: #end_pymotw_header

..
    In this single-threaded example, the jobs are pulled out of the queue
    in strictly priority order.  If there were multiple threads consuming
    the jobs, they would be processed based on the priority of items in
    the queue at the time ``get()`` was called.

このシングルスレッドのサンプルでは、そのお仕事は厳密に優先順序をもってキューから取り出されます。マルチスレッドでそのお仕事を処理する場合、 :func:`get` が呼び出されたときにキューの要素の優先順序に基づいて処理されます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'Queue_priority.py'))
.. }}}

::

	$ python Queue_priority.py
	
	New job: Mid-level job
	New job: Low-level job
	New job: Important job
	Processing job: Important job
	Processing job: Mid-level job
	Processing job: Low-level job

.. {{{end}}}


..
    Using Queues with Threads
    =========================

スレッドでキューを使用する
==========================

..
    As an example of how to use the Queue class with multiple threads, we
    can create a very simplistic podcasting client. This client reads one
    or more RSS feeds, queues up the enclosures for download, and
    processes several downloads in parallel using threads. It is
    simplistic and unsuitable for actual use, but the skeleton
    implementation gives us enough code to work with to provide an example
    of using the Queue module.

マルチスレッドで Queue クラスを使用するサンプルとして、とてもシンプルな podcast クライアントを作成します。このクライアントは、1つかそれ以上の RSS フィードを読み込み、ダウンロードするためにそのエンクロージャをキューに追加します。そして、スレッドを使用して複数のコンテンツを並行にダウンロードします。これは実用においては単純過ぎて不適切ですが、そのプロトタイプ実装は :mod:`Queue` モジュールと連携するサンプルコードとして十分です。

.. include:: fetch_podcasts.py
    :literal:
    :start-after: #end_pymotw_header

..
    First, we establish some operating parameters. Normally these would
    come from user inputs (preferences, a database, whatever). For our
    example we hard code the number of threads to use and the list of URLs
    to fetch.

まず操作用のパラメータを設計します。通常はユーザ入力(優先度、データベース、対象)です。サンプルでは、取得する URL リストとスレッドの数をハードコーディングしています。

..
    Next, we need to define the function ``downloadEnclosures()`` that
    will run in the worker thread, processing the downloads. Again, for
    illustration purposes this only simulates the download. To actually
    download the enclosure, you might use :mod:`urllib` or
    :mod:`urllib2`. In this example, we simulate a download delay by
    sleeping a variable amount of time, depending on the thread id.

次に ワーカースレッドで実行して、ダウンロードを行う :func:`downloadEnclosures()` を定義する必要があります。今回は説明目的なのでこの処理はダウンロードを模倣します。実際にはエンクロージャをダウンロードするために :mod:`urllib` か :mod:`urllib2` を使用すると良いです。このサンプルでは、スレッド ID からその秒を sleep することでダウンロードによる遅延を模倣します。

..
    Once the threads' target function is defined, we can start the worker
    threads. Notice that downloadEnclosures() will block on the statement
    ``url = q.get()`` until the queue has something to return, so it is
    safe to start the threads before there is anything in the queue.

スレッドの target 引数に関数を指定すると、ワーカースレッドが開始します。 :func:`downloadEnclosures` は、キューが何か返すまで ``url = q.get()`` のコードをブロックすることに注意してください。そのため、キューに何かある状態で安全にそのスレッドを開始します。 

..
    The next step is to retrieve the feed contents (using Mark Pilgrim's
    `feedparser`_ module) and enqueue the URLs of the enclosures. As soon
    as the first URL is added to the queue, one of the worker threads
    should pick it up and start downloading it. The loop below will
    continue to add items until the feed is exhausted, and the worker
    threads will take turns dequeuing URLs to download them.

次のステップは、フィードコンテンツを取り出して(Mark Pilgrim の `feedparser`_ モジュールを使用します)、エンクロージャの URL をキューへ追加することです。最初の URL がキューへ追加されると同時に、ワーカースレッドの1つがその要素を取り出してダウンロードを開始します。そのループ処理はフィードがなくなるまで要素を追加し続けます。そして、ワーカースレッドは、ダウンロードするために URL をキューから取り出して終了します。

..
    And the only thing left to do is wait for the queue to empty out
    again, using ``join()``.

最後に残された唯一の処理は :func:`join` でキューが空になるまで待つことです。

..
    If you run the sample script, you should see output something like
    this:

サンプルスクリプトを実行すると、次のような実行結果を確認できます。

::

    0: Looking for the next enclosure
    1: Looking for the next enclosure
    Queuing: http://http.earthcache.net/htc-01.media.globix.net/COMP009996MOD1/Danny_Meyer.mp3
    Queuing: http://feeds.feedburner.com/~r/drmoldawer/~5/104445110/moldawerinthemorning_show34_032607.mp3
    Queuing: http://www.podtrac.com/pts/redirect.mp3/twit.cachefly.net/MBW-036.mp3
    Queuing: http://media1.podtech.net/media/2007/04/PID_010848/Podtech_calacaniscast22_ipod.mp4
    Queuing: http://media1.podtech.net/media/2007/03/PID_010592/Podtech_SXSW_KentBrewster_ipod.mp4
    Queuing: http://media1.podtech.net/media/2007/02/PID_010171/Podtech_IDM_ChrisOBrien2.mp3
    Queuing: http://feeds.feedburner.com/~r/drmoldawer/~5/96188661/moldawerinthemorning_show30_022607.mp3
    *** Main thread waiting
    0: Downloading: http://http.earthcache.net/htc-01.media.globix.net/COMP009996MOD1/Danny_Meyer.mp3
    1: Downloading: http://feeds.feedburner.com/~r/drmoldawer/~5/104445110/moldawerinthemorning_show34_032607.mp3
    0: Looking for the next enclosure
    0: Downloading: http://www.podtrac.com/pts/redirect.mp3/twit.cachefly.net/MBW-036.mp3
    1: Looking for the next enclosure
    1: Downloading: http://media1.podtech.net/media/2007/04/PID_010848/Podtech_calacaniscast22_ipod.mp4
    0: Looking for the next enclosure
    0: Downloading: http://media1.podtech.net/media/2007/03/PID_010592/Podtech_SXSW_KentBrewster_ipod.mp4
    0: Looking for the next enclosure
    0: Downloading: http://media1.podtech.net/media/2007/02/PID_010171/Podtech_IDM_ChrisOBrien2.mp3
    1: Looking for the next enclosure
    1: Downloading: http://feeds.feedburner.com/~r/drmoldawer/~5/96188661/moldawerinthemorning_show30_022607.mp3
    0: Looking for the next enclosure
    1: Looking for the next enclosure
    *** Done

..
    The actual output will depend on whether anyone modifies the
    subscriptions in the guest account on http://www.CastSampler.com.

実際の実行結果は http://www.CastSampler.com のゲストアカウントのサブスクリプションを誰かが変更すると変わります。

.. seealso::

    `Queue <http://docs.python.org/lib/module-Queue.html>`_
        .. Standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント

    :ref:`deque` from :mod:`collections`
        .. collections includes a deque (double-ended queue) class

        deque (両端キュー) クラスを提供する :mod:`collections` モジュール
    
    *Wikipedia: Queue data structures*
        http://en.wikipedia.org/wiki/Queue_(data_structure)

    *Wikipedia: FIFO*
        http://en.wikipedia.org/wiki/FIFO

    `feedparser`_
        .. Mark Pilgrim's feedparser module (http://www.feedparser.org/).

        Mark Pilgrim の feedparser モジュール (http://www.feedparser.org/).
    
    :ref:`article-data-structures`
        .. Other complex data structures in the standard library.

        標準ライブラリのその他の複雑なデータ構造

.. _feedparser: http://www.feedparser.org/
