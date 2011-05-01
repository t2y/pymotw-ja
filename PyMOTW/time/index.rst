..
    =============================================
    time -- Functions for manipulating clock time
    =============================================

======================
time -- 時間を扱う関数
======================

..
    :synopsis: Functions for manipulating clock time

.. module:: time
    :synopsis: 時間を扱う関数

..
    :Purpose: Functions for manipulating clock time.
    :Available In: 1.4 or earlier

:目的: 時間を扱う関数
:利用できるバージョン: 1.4 以上

..
    The :mod:`time` module exposes C library functions for manipulating
    dates and times.  Since it is tied to the underlying C implementation,
    some details (such as the start of the epoch and maximum date value
    supported) are platform-specific.  Refer to the library documentation
    for complete details.

:mod:`time` モジュールは、日付と時間を扱う C 言語のライブラリ関数を提供します。それは C 言語の実装に関連付けられているので、(エポックの開始やサポートされている最大日付の値といった)詳細のいくつかははプラットフォーム固有になります。完全な詳細については、標準ライブラリドキュメントを参照してください。

..
    Wall Clock Time
    ===============

ウォールクロック時間
====================

..
    One of the core functions of the :mod:`time` module is :func:`time()`,
    which returns the number of seconds since the start of the epoch as a
    floating point value.

:mod:`time` モジュールのコア関数の1つは、小数でエポック秒を返す :func:`time()` です。

.. include:: time_time.py
    :literal:
    :start-after: #end_pymotw_header

..
    Although the value is always a float, actual precision is
    platform-dependent.

その値は必ず小数が返されますが、実際の精度はプラットフォームに依存しています。

::

    $ python time_time.py
    The time is: 1205079300.54

..
    The float representation is useful when storing or comparing dates,
    but not as useful for producing human readable representations. For
    logging or printing time :func:`ctime()` can be more useful.

小数表現は、値を保持したり日付を比較するのに便利ですが、人間が分かり易い表現ではありません。ログまたは時間を表示するには :func:`ctime()` の方が分かり易いです。

.. include:: time_ctime.py
    :literal:
    :start-after: #end_pymotw_header

..
    Here the second output line shows how to use :func:`ctime()` to format
    a time value other than the current time.

2行目の出力は、現在の時間以外の時間を表す :func:`ctime()` の使用方法を紹介します。

::

    $ python time_ctime.py
    The time is      : Sun Mar  9 12:18:02 2008
    15 secs from now : Sun Mar  9 12:18:17 2008

..
    Processor Clock Time
    ====================

プロセッサクロックタイム
========================

..
    While :func:`time()` returns a wall clock time, :func:`clock()`
    returns processor clock time.  The values returned from
    :func:`clock()` should be used for performance testing, benchmarking,
    etc. since they reflect the actual time used by the program, and can
    be more precise than the values from :func:`time()`.

:func:`time` がウォールクロックタイムを返す一方、 :func:`clock` はプロセッサクロックタイムを返します。 :func:`clock()` の値は、パフォーマンステスト、ベンチマーク等に使用されます。それはプログラムが使用した実際の時間が反映されるので :func:`time()` よりも精度の高い値になります。

.. include:: time_clock.py
    :literal:
    :start-after: #end_pymotw_header


..
    In this example, the formatted :func:`ctime()` is printed along with
    the floating point values from :func:`time()`, and :func:`clock()` for
    each iteration through the loop. If you want to run the example on
    your system, you may have to add more cycles to the inner loop or work
    with a larger amount of data to actually see a difference.

このサンプルでは、ループ処理でフォーマット済みの :func:`ctime()` と一緒に :func:`time()` と :func:`clock()` の値を表示します。自分のシステム上でこのサンプルを実行したいなら、違いが実際に分かるように内部ループ処理でもっとサイクルを追加するか、大量のデータを処理するように変更する必要があります。

::

    $ python time_clock.py
    Sun Mar  9 12:41:53 2008 : 1205080913.260 0.030
    Sun Mar  9 12:41:53 2008 : 1205080913.682 0.440
    Sun Mar  9 12:41:54 2008 : 1205080914.103 0.860
    Sun Mar  9 12:41:54 2008 : 1205080914.518 1.270
    Sun Mar  9 12:41:54 2008 : 1205080914.932 1.680

..
    Typically, the processor clock doesn't tick if your program isn't doing
    anything.

通常はプログラム内で何もしない場合、プロセッサクロックは時を刻みません。

.. include:: time_clock_sleep.py
    :literal:
    :start-after: #end_pymotw_header

..
    In this example, the loop does very little work by going to sleep
    after each iteration. The :func:`time()` value increases even while
    the app is asleep, but the :func:`clock()` value does not.

このサンプルのループ処理は、ループ毎に :func:`sleep()` することで小さな処理を実装します :func:`time()` の値は、アプリケーションが :func:`sleep()` 中であっても増加しますが、 :func:`clock()` の値は違います。

::

    $ python time_clock_sleep.py
    Sun Mar  9 12:46:36 2008 1205081196.20 0.02
    Sleeping 6
    Sun Mar  9 12:46:42 2008 1205081202.20 0.02
    Sleeping 5
    Sun Mar  9 12:46:47 2008 1205081207.20 0.02
    Sleeping 4
    Sun Mar  9 12:46:51 2008 1205081211.20 0.02
    Sleeping 3
    Sun Mar  9 12:46:54 2008 1205081214.21 0.02
    Sleeping 2

..
    Calling :func:`sleep()` yields control from the current thread and
    asks it to wait for the system to wake it back up. If your program has
    only one thread, this effectively blocks the app and it does no work.

:func:`sleep()` を呼び出すと、カレントスレッドから制御が移動して、戻って処理を続行するためにシステムに待つように求めます。プログラムが1つのスレッドのみなら、これはアプリケーションを効率的にブロックして処理を行いません。

struct_time
===========

..
    Storing times as elapsed seconds is useful in some situations, but
    there are times when you need to have access to the individual fields
    of a date (year, month, etc.). The :mod:`time` module defines
    :class:`struct_time` for holding date and time values with components
    broken out so they are easy to access. There are several functions
    that work with :class:`struct_time` values instead of floats.

経過した秒数を保持しておくと状況によって役に立ちますが、 :mod:`date` の個々のフィールド(年、月等)へアクセス必要があるときもあります。 :mod:`time` モジュールは、分割したコンポーネントに日付と時間の値を保持する :class:`struct_time` クラスを定義しているので、簡単にアクセスできます。また小数ではなく :class:`struct_time` の値を処理する関数があります。

.. include:: time_struct.py
    :literal:
    :start-after: #end_pymotw_header

..
    :func:`gmtime()` returns the current time in UTC. :func:`localtime()`
    returns the current time with the current time zone
    applied. :func:`mktime()` takes a :class:`struct_time` and converts it
    to the floating point representation.

:func:`gmtime()` は UTC で現在の時間を返します。 :func:`localtime()` は現在のタイムゾーンで現在の時間を返します。 :func:`mktime()` は :class:`struct_time` を受け取り、それを小数表現に変換します。

::

    $ python time_struct.py
    gmtime   : (2008, 3, 9, 16, 58, 19, 6, 69, 0)
    localtime: (2008, 3, 9, 12, 58, 19, 6, 69, 1)
    mktime   : 1205081899.0

    Day of month: 9
     Day of week: 6
     Day of year: 69

..
    Parsing and Formatting Times
    ============================

時間を解析して整形する
======================

..
    The two functions :func:`strptime()` and :func:`strftime()` convert
    between struct_time and string representations of time values. There
    is a long list of formatting instructions available to support input
    and output in different styles. The complete list is documented in the
    library documentation for the time module.
    
:func:`strptime()` と :func:`strftime()` の2つの関数は、時間の値による表現を :class:`struct_time` と文字列の間で変換します。異なるスタイルで入力と出力をサポートするために利用できるフォーマットのリストがあります。完全なリストは :mod:`time` モジュールの標準ライブラリドキュメントに記載されています。

..
    This example converts the current time from a string, to a
    :class:`struct_time` instance, and back to a string.

このサンプルは文字列の現在の時間を :class:`struct_time` インスタンスに変換してから文字列へ戻します。

.. include:: time_strptime.py
    :literal:
    :start-after: #end_pymotw_header

..
    The output string is not exactly like the input, since the day of the
    month is prefixed with a zero.

月の日付はゼロが接頭辞に付くので、入力と文字列の出力は厳密に同じではありません。

::

    $ python time_strptime.py
    Sun Mar  9 13:01:19 2008
    (2008, 3, 9, 13, 1, 19, 6, 69, -1)
    Sun Mar 09 13:01:19 2008

..
    Working with Time Zones
    =======================

タイムゾーンを扱う
==================

..
    The functions for determining the current time depend on having the time zone
    set, either by your program or by using a default time zone set for the
    system. Changing the time zone does not change the actual time, just the way
    it is represented.

現在の時間を決める関数は、実行するプログラムか、システムのデフォルトタイムゾーンを使用するかのどちらかのタイムゾーンに依存します。タイムゾーンを変更しても実際の時間は変更されません。ただ表現の方法が変わるだけです。

..
    To change the time zone, set the environment variable ``TZ``, then
    call :func:`tzset()`.  Using TZ, you can specify the time zone with a
    lot of detail, right down to the start and stop times for daylight
    savings time. It is usually easier to use the time zone name and let
    the underlying libraries derive the other information, though.

タイムゾーンを変更するには、環境変数 ``TZ``  をセットしてから :func:`tzset()` を呼び出してください。 ``TZ`` を使用すると、多くの詳細をもつタイムゾーンを指定できます。すぐにサマータイムを開始して終了させてみましょう。ライブラリにその他の情報も派生してしまいますが、普通はタイムゾーン名を使用する方が簡単です。

..
    This example program changes the time zone to a few different values
    and shows how the changes affect other settings in the time module.

このサンプルでは、タイムゾーンを変更して :mod:`time` モジュールの他の設定にどのような影響があるかを表示します。

.. include:: time_timezone.py
    :literal:
    :start-after: #end_pymotw_header

..
    My default time zone is US/Eastern, so setting TZ to that has no
    effect. The other zones used change the tzname, daylight flag, and
    timezone offset value.

私のデフォルトのタイムゾーンは ``US/Eastern`` なので ``TZ`` を設定しても何の影響もありません。別のlタイムゾーンでは :attr:`tzname` 、 :attr:`dailight` フラグや :attr:`offset` の値を変更します。

::

    $ python time_timezone.py
    Default :
        TZ    : (not set)
        tzname: ('EST', 'EDT')
        Zone  : 18000 (5)
        DST   : 1
        Time  : Sun Mar  9 13:06:53 2008

    US/Eastern :
        TZ    : US/Eastern
        tzname: ('EST', 'EDT')
        Zone  : 18000 (5)
        DST   : 1
        Time  : Sun Mar  9 13:06:53 2008

    US/Pacific :
        TZ    : US/Pacific
        tzname: ('PST', 'PDT')
        Zone  : 28800 (8)
        DST   : 1
        Time  : Sun Mar  9 10:06:53 2008

    GMT :
        TZ    : GMT
        tzname: ('GMT', 'GMT')
        Zone  : 0 (0)
        DST   : 0
        Time  : Sun Mar  9 17:06:53 2008

    Europe/Amsterdam :
        TZ    : Europe/Amsterdam
        tzname: ('CET', 'CEST')
        Zone  : -3600 (-1)
        DST   : 1
        Time  : Sun Mar  9 18:06:53 2008

.. seealso::

    `time <http://docs.python.org/lib/module-time.html>`_
        .. Standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント

    :mod:`datetime`
        .. The datetime module includes other classes for doing calculations with dates and times.

        日付と時間の計算をするクラスを提供する datetime モジュール

    :mod:`calendar`
        .. Work with higher-level date functions to produce calendars or
           calculate recurring events.

        カレンダーを生成したり、定期的なイベントを計算したりする高レベルな日付関数
