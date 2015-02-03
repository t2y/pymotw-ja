..
    =================================
    sched -- Generic event scheduler.
    =================================

=================================
sched -- 汎用イベントスケジューラ
=================================

..
    :synopsis: Generic event scheduler.

.. module:: sched
    :synopsis: 汎用イベントスケジューラ

..
    :Purpose: Generic event scheduler.
    :Available In: 1.4

:目的: 汎用イベントスケジューラ
:利用できるバージョン: 1.4 以上

..
    The :mod:`sched` module implements a generic event scheduler for
    running tasks at specific times. The scheduler class uses a *time*
    function to learn the current time, and a *delay* function to wait for
    a specific period of time. The actual units of time are not important,
    which makes the interface flexible enough to be used for many
    purposes.

:mod:`sched` モジュールは、特定時刻にタスクを実行する汎用イベントスケジューラを実装します。スケジューラクラスは、現在の時間を知るために *time*  関数を、一定時間待つために *delay* 関数を使用します。実際の時間の単位は、多目的に使用できるように柔軟なインターフェイスを設ければ重要ではありません。

..
    The *time* function is called without any arguments, and should return
    a number representing the current time. The *delay* function is called
    with a single integer argument, using the same scale as the time
    function, and should wait that many time units before returning. For
    example, the ``time.time()`` and ``time.sleep()`` functions meet these
    requirements.

*time* 関数は、引数なしで呼ばれ、現在の時間を表す数値を返します。 *delay* 関数は、 *time* 関数と同じ単位で1つの整数を引数に取り、時間単位分を待ちます。例えば、 :func:`time.time()` と :func:`time.sleep()` 関数はこれらの要件を満たします。

..
    To support multi-threaded applications, the delay function is called
    with argument 0 after each event is generated, to ensure that other
    threads also have a chance to run.

マルチスレッドアプリケーションをサポートするには、その他のスレッドの実行機会があることを保証するために、各イベントが生成された後で *delay* 関数の引数を0で呼び出します。

..
    Running Events With a Delay
    ===========================

イベントを遅延なく実行する
==========================

..
    Events can be scheduled to run after a delay, or at a specific
    time. To schedule them with a delay, use the ``enter()`` method, which
    takes 4 arguments:

イベントは、遅延後または一定時間後に実行するようにスケジュールできます。遅延させてスケジュールするには、4つの引数を受け取る :func:`enter()` を使用してください。

..
    * A number representing the delay
    * A priority value
    * The function to call
    * A tuple of arguments for the function

* 遅延を表す値
* 優先順位の値
* 呼び出す関数
* 関数の引数のタプル

..
    This example schedules 2 different events to run after 2 and 3 seconds
    respectively. When the event's time comes up, ``print_event()`` is
    called and prints the current time and the name argument passed to the
    event.

このサンプルでは、予定の違う2つのイベントがそれぞれ2後後と3秒後に実行されます。イベントを実行する時間がきたら、 :func:`print_event()` が呼び出されて、現在の時間とイベントに渡された ``name`` 引数を表示します。

.. include:: sched_basic.py
    :literal:
    :start-after: #end_pymotw_header

..
    The output will look something like this:

この結果出力は次のようになります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sched_basic.py'))
.. }}}

::

	$ python sched_basic.py
	
	START: 1361446599.49
	EVENT: 1361446601.49 first
	EVENT: 1361446602.49 second

.. {{{end}}}

..
    The time printed for the first event is 2 seconds after start, and the
    time for the second event is 3 seconds after start.

最初のイベントは開始して2秒後に、2番目のイベントは開始して3秒後に表示されます。

..
    Overlapping Events
    ==================

イベントを重複させる
====================

..
    The call to ``run()`` blocks until all of the events have been
    processed. Each event is run in the same thread, so if an event takes
    longer to run than the delay between events, there will be
    overlap. The overlap is resolved by postponing the later event. No
    events are lost, but some events may be called later than they were
    scheduled. In the next example, ``long_event()`` sleeps but it could
    just as easily delay by performing a long calculation or by blocking
    on I/O.

全てのイベントが処理されるまで :func:`run()` の呼び出しはブロックします。それぞれのイベントは同じスレッドで実行されるので、あるイベントがイベント間の遅延時間よりも実行に時間がかかる場合に重複します。このイベントの重複は、それ以降のイベントを延期することで解決されます。イベントがなくなるわけではありませんが、予定した時間よりも遅れてイベントが実行される可能性があります。次の例では、 :func:`long_event()` は ``sleep`` しますが、時間のかかる計算を実行するか、I/O をブロッキングすることで簡単に遅延させられます。

.. include:: sched_overlap.py
    :literal:
    :start-after: #end_pymotw_header

..
    The result is the second event is run immediately after the first
    finishes, since the first event took long enough to push the clock
    past the desired start time of the second event.

その結果、最初のイベントは2番目のイベントの開始時刻を過ぎるまでかかるので、最初のイベント終了後すぐに2番目のイベントが実行されます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sched_overlap.py'))
.. }}}

::

	$ python sched_overlap.py
	
	START: 1361446602.55
	BEGIN EVENT : 1361446604.55 first
	FINISH EVENT: 1361446606.55 first
	BEGIN EVENT : 1361446606.55 second
	FINISH EVENT: 1361446608.55 second

.. {{{end}}}

..
    Event Priorities
    ================

イベントの優先度
================

..
    If more than one event is scheduled for the same time their priority values
    are used to determine the order they are run. 

同じ時間に1つ以上のイベントが予定されている場合、実行する順番を決めるために優先度の値が使用されます。

.. include:: sched_priority.py
    :literal:
    :start-after: #end_pymotw_header

..
    This example needs to ensure that they are scheduled for the exact
    same time, so the ``enterabs()`` method is used instead of
    ``enter()``. The first argument to ``enterabs()`` is the time to run
    the event, instead of the amount of time to delay.

このサンプルは、厳密に同じ時間に予定されていることを保証する必要があるので、 :func:`enter()` ではなく :func:`enterabs()` メソッドを使用します。 :func:`enterabs()` の最初の引数は、遅延の時間ではなくイベントを実行する時間です。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sched_priority.py'))
.. }}}

::

	$ python sched_priority.py
	
	START: 1361446608.62
	EVENT: 1361446610.62 second
	EVENT: 1361446610.62 first

.. {{{end}}}

..
    Canceling Events
    ================

イベントをキャンセルする
========================

..
    Both ``enter()`` and ``enterabs()`` return a reference to the event
    which can be used to cancel it later. Since ``run()`` blocks, the
    event has to be canceled in a different thread. For this example, a
    thread is started to run the scheduler and the main processing thread
    is used to cancel the event.

:func:`enter()` と :func:`enterabs()` の両方とも、後でキャンセルできるリファレンスを返します。 :func:`run()` はブロックしてしまうので、イベントは違うスレッドからキャンセルさせる必要があります。このサンプルでは、別のスレッドがスケジューラを実行するために開始されて、メイン処理のスレッドがそのイベントをキャンセルするために使用されます。

.. include:: sched_cancel.py
    :literal:
    :start-after: #end_pymotw_header

..
    Two events were scheduled, but the first was later canceled. Only the
    second event runs, so the counter variable is only incremented one
    time.

2つのイベントが予定されていましたが、最初のイベントはキャンセルされました。2番目のイベントのみ実行されるので、その ``counter`` 変数は1回だけインクリメントされます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sched_cancel.py'))
.. }}}

::

	$ python sched_cancel.py
	
	START: 1361446610.65
	EVENT: 1361446613.66 E2
	NOW: 1
	FINAL: 1

.. {{{end}}}


.. seealso::

    `sched <http://docs.python.org/lib/module-sched.html>`_
        .. Standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント

    :mod:`time`
        .. The time module.

        time モジュール
