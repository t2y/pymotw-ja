..
    ========================================
    datetime -- Date/time value manipulation
    ========================================

===========================
datetime -- 日付/時間の操作
===========================

..
    :synopsis: Date/time value manipulation.

.. module:: datetime
    :synopsis: 日付/時間の操作

..
    :Purpose: The datetime module includes functions and classes for doing date and time parsing, formatting, and arithmetic.
    :Available In: 2.3 and later

:目的: datetime モジュールは、日付や時間を解析、書式設定、計算するための関数やクラスを提供する
:利用できるバージョン: 2.3 以上

..
    :mod:`datetime` contains functions and classes for working with dates
    and times, separatley and together.

:mod:`datetime` モジュールの関数やクラスは、単独で同時に日付や時間を扱います。

..
    Times
    =====

時間
====

..
    Time values are represented with the :class:`time` class. Times have
    attributes for hour, minute, second, and microsecond. They can also
    include time zone information. The arguments to initialize a
    :class:`time` instance are optional, but the default of ``0`` is
    unlikely to be what you want.

時間は :class:`time` クラスで表されます。 :class:`time` は、時・分・秒・マイクロ秒の属性をもちます。また、タイムゾーンの情報も含みます。 :class:`time` インスタンスを初期化する引数はオプションで選択できますが、デフォルトは望むものとは言い難い ``0`` になります。

.. include:: datetime_time.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'datetime_time.py'))
.. }}}

::

	$ python datetime_time.py
	
	01:02:03
	hour  : 1
	minute: 2
	second: 3
	microsecond: 0
	tzinfo: None

.. {{{end}}}

..
    A time instance only holds values of time, and not a date associated
    with the time.

:class:`time` インスタンスは、日付に関連付けられていない時間のみを保持します。

.. include:: datetime_time_minmax.py
    :literal:
    :start-after: #end_pymotw_header

..
    The *min* and *max* class attributes reflect the valid range of
    times in a single day.

*min* と *max* のクラス属性は、1日の時間の有効範囲を表します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'datetime_time_minmax.py'))
.. }}}

::

	$ python datetime_time_minmax.py
	
	Earliest  : 00:00:00
	Latest    : 23:59:59.999999
	Resolution: 0:00:00.000001

.. {{{end}}}

..
    The resolution for time is limited to whole microseconds.

:class:`time` の :attr:`resolution` で取得できるのはマイクロ秒までに制限されます。

.. include:: datetime_time_resolution.py
    :literal:
    :start-after: #end_pymotw_header

..
    In fact, using floating point numbers for the microsecond argument
    generates a :ref:`TypeError <exceptions-TypeError>`.

実際、マイクロ秒に小数を使用すると :ref:`TypeError <exceptions-TypeError>` が発生します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'datetime_time_resolution.py'))
.. }}}

::

	$ python datetime_time_resolution.py
	
	1.0 : 00:00:00.000001
	0.0 : 00:00:00
	0.1 : ERROR: integer argument expected, got float
	0.6 : ERROR: integer argument expected, got float

.. {{{end}}}

..
    Dates
    =====

日付
====

..
    Calendar date values are represented with the :class:`date`
    class. Instances have attributes for year, month, and day. It is easy
    to create a date representing today's date using the :func:`today()`
    class method.

カレンダーの日付は :class:`date` クラスで表されます。このインスタンスは、年・月・日の属性をもちます。 :func:`today()` クラスメソッドで簡単に今日の日付を表せます。

.. include:: datetime_date.py
    :literal:
    :start-after: #end_pymotw_header

..
    This example prints the current date in several formats:

このサンプルは複数のフォーマットで今日の日付を表示します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'datetime_date.py'))
.. }}}

::

	$ python datetime_date.py
	
	2013-02-21
	ctime: Thu Feb 21 00:00:00 2013
	tuple: time.struct_time(tm_year=2013, tm_mon=2, tm_mday=21, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=52, tm_isdst=-1)
	ordinal: 734920
	Year: 2013
	Mon : 2
	Day : 21

.. {{{end}}}

..
    There are also class methods for creating instances from integers
    (using proleptic Gregorian ordinal values, which starts counting from
    Jan. 1 of the year 1) or POSIX timestamp values.

(1年の1月1日から数え始める初期のグレゴリオ序数を使用して)整数からインスタンスを作成するクラスメソッドや POSIX タイムスタンプもあります。

.. include:: datetime_date_fromordinal.py
    :literal:
    :start-after: #end_pymotw_header

..
    This example illustrates the different value types used by
    :func:`fromordinal()` and :func:`fromtimestamp()`.

このサンプルは :func:`fromordinal()` と :func:`fromtimestamp()` が使用する値が違うことを説明します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'datetime_date_fromordinal.py'))
.. }}}

::

	$ python datetime_date_fromordinal.py
	
	o: 733114
	fromordinal(o): 2008-03-13
	t: 1361446545.52
	fromtimestamp(t): 2013-02-21

.. {{{end}}}

..
    As with :class:`time`, the range of date values supported can be
    determined using the *min* and *max* attributes.

:class:`time` クラスと同様に、日付の有効範囲は *min* と *max* 属性で決められます。

.. include:: datetime_date_minmax.py
    :literal:
    :start-after: #end_pymotw_header

..
    The resolution for dates is whole days.

:class:`date` の :attr:`resolution` で取得できるのは丸一日です。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'datetime_date_minmax.py'))
.. }}}

::

	$ python datetime_date_minmax.py
	
	Earliest  : 0001-01-01
	Latest    : 9999-12-31
	Resolution: 1 day, 0:00:00

.. {{{end}}}

..
    Another way to create new date instances uses the :func:`replace()`
    method of an existing date. For example, you can change the year,
    leaving the day and month alone.

新たな :class:`date` インスタンスを作成する別の方法は、既存の :class:`date` の :func:`replace()` メソッドを使用します。例えば、日と月はそのままで年を変更できます。

.. include:: datetime_date_replace.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'datetime_date_replace.py'))
.. }}}

::

	$ python datetime_date_replace.py
	
	d1: 2008-03-12
	d2: 2009-03-12

.. {{{end}}}

..
    timedeltas
    ==========

タイムデルタ
============

..
    Using :func:`replace()` is not the only way to calculate future/past
    dates. You can use :mod:`datetime` to perform basic arithmetic on date
    values via the :class:`timedelta` class. Subtracting dates produces a
    :class:`timedelta`, and a :class:`timedelta` can be added or
    subtracted from a date to produce another date. The internal values
    for a :class:`timedelta` are stored in days, seconds, and
    microseconds.

:func:`replace()` を使用することだけが未来/過去の日付を計算する方法ではありません。 :mod:`datetime` の :class:`timedelta` を使用して基本的な日付計算ができます。日付の引き算をすると :class:`timedelta` を生成します。 :class:`timedelta` は足し算や引き算により別の日付を生成します。 :class:`timedelta` の内部的な値は、日・秒・マイクロ秒で格納されます。

.. include:: datetime_timedelta.py
    :literal:
    :start-after: #end_pymotw_header

..
    Intermediate level values passed to the constructor are converted into
    days, seconds, and microseconds.

コンストラクタへ渡される中間の値は、日、秒、マイクロ秒に変換されます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'datetime_timedelta.py'))
.. }}}

::

	$ python datetime_timedelta.py
	
	microseconds: 0:00:00.000001
	milliseconds: 0:00:00.001000
	seconds     : 0:00:01
	minutes     : 0:01:00
	hours       : 1:00:00
	days        : 1 day, 0:00:00
	weeks       : 7 days, 0:00:00

.. {{{end}}}

..
    Date Arithmetic
    ===============

日付計算
========

..
    Date math uses the standard arithmetic operators. This example with
    date objects illustrates using :class:`timedelta` objects to compute
    new dates, and subtracting date instances to produce timedeltas
    (including a negative delta value).

日付の計算は標準の算術演算子を使用します。 :class:`date` オブジェクトを扱うこのサンプルは、新しい日付を計算する :class:`timedelta` オブジェクトの使い方と、(マイナスのデルタ値を含む) :class:`timedelta` を生成する :class:`date` インスタンスの引き算を説明します。

.. include:: datetime_date_math.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'datetime_date_math.py'))
.. }}}

::

	$ python datetime_date_math.py
	
	Today    : 2013-02-21
	One day  : 1 day, 0:00:00
	Yesterday: 2013-02-20
	Tomorrow : 2013-02-22
	tomorrow - yesterday: 2 days, 0:00:00
	yesterday - tomorrow: -2 days, 0:00:00

.. {{{end}}}

..
    Comparing Values
    ================

値の比較
========

..
    Both date and time values can be compared using the standard operators
    to determine which is earlier or later.

:class:`date` と :class:`time` の両方とも、どちらの日時が早いか、遅いかを標準の演算子で比較できます。

.. include:: datetime_comparing.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'datetime_comparing.py'))
.. }}}

::

	$ python datetime_comparing.py
	
	Times:
		t1: 12:55:00
		t2: 13:05:00
		t1 < t2: True
	Dates:
		d1: 2013-02-21
		d2: 2013-02-22
		d1 > d2: False

.. {{{end}}}

..
    Combining Dates and Times
    =========================

日付と時間を組み合わせる
========================

..
    Use the :class:`datetime` class to hold values consisting of both date
    and time components. As with :class:`date`, there are several
    convenient class methods to make creating :class:`datetime` instances
    from other common values.

:class:`date` と :class:`time` の両方の値を保持するには :class:`datetime` クラスを使用してください。 :class:`date` と同様に、その他の共通の値から :class:`datetime` インスタンスを作成する便利なクラスメソッドがあります。

.. include:: datetime_datetime.py
    :literal:
    :start-after: #end_pymotw_header

..
    As you might expect, the :class:`datetime` instance has all of the
    attributes of both a date and a time object.

予想通り、 :class:`datetime` インスタンスは :class:`date` と :class:`time` オブジェクトの全ての属性をもちます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'datetime_datetime.py'))
.. }}}

::

	$ python datetime_datetime.py
	
	Now    : 2013-02-21 06:35:45.658505
	Today  : 2013-02-21 06:35:45.659381
	UTC Now: 2013-02-21 11:35:45.659396
	year : 2013
	month : 2
	day : 21
	hour : 6
	minute : 35
	second : 45
	microsecond : 659677

.. {{{end}}}

..
    Just as with date, datetime provides convenient class methods for
    creating new instances. It also includes :func:`fromordinal()` and
    :func:`fromtimestamp()`. In addition, :func:`combine()` can be useful
    if you already have a date instance and time instance and want to
    create a datetime.

:class:`date` と同様に、 :class:`datetime` は、新たなインスタンスを作成する便利なクラスメソッドを提供します。 :func:`fromordinal()` や :func:`fromtimestamp()` もあります。さらに :func:`combine()` は、既に :class:`date` と :class:`time` インスタンスがあって :class:`datetime` を作成したいときに便利です。

.. include:: datetime_datetime_combine.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'datetime_datetime_combine.py'))
.. }}}

::

	$ python datetime_datetime_combine.py
	
	t : 01:02:03
	d : 2013-02-21
	dt: 2013-02-21 01:02:03

.. {{{end}}}

..
    Formatting and Parsing
    ======================

フォーマットと解析
==================

..
    The default string representation of a datetime object uses the `ISO
    8601`_ format (``YYYY-MM-DDTHH:MM:SS.mmmmmm``). Alternate formats can
    be generated using :func:`strftime()`. Similarly, if your input data
    includes timestamp values parsable with :func:`time.strptime()`, then
    :func:`datetime.strptime()` is a convenient way to convert them to
    datetime instances.

:class:`datetime` オブジェクトのデフォルトの文字列表現は、 `ISO 8601`_ フォーマット (``YYYY-MM-DDTHH:MM:SS.mmmmmm``) を使用します。 :func:`strftime()` を使用して別のフォーマットも生成できます。同様に、入力データが :func:`time.strptime()` で解析できるタイムスタンプをもつ場合、 :func:`datetime.strptime()` はそのタイムスタンプを :class:`datetime` インスタンスに変換するのに便利です。

.. include:: datetime_datetime_strptime.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'datetime_datetime_strptime.py'))
.. }}}

::

	$ python datetime_datetime_strptime.py
	
	ISO     : 2013-02-21 06:35:45.707450
	strftime: Thu Feb 21 06:35:45 2013
	strptime: Thu Feb 21 06:35:45 2013

.. {{{end}}}

..
    Time Zones
    ==========

タイムゾーン
============

..
    Within :mod:`datetime`, time zones are represented by subclasses of
    :class:`tzinfo`. Since :class:`tzinfo` is an abstract base class, you
    need to define a subclass and provide appropriate implementations for
    a few methods to make it useful. Unfortunately, :mod:`datetime` does
    not include any actual implementations ready to be used, although the
    documentation does provide a few sample implementations. Refer to the
    standard library documentation page for examples using fixed offsets
    as well as a DST-aware class and more details about creating your own
    class.  pytz_ is also a good source for time zone implementation
    details.

:mod:`datetime` モジュールの内部で、タイムゾーンは :class:`tzinfo` のサブクラスで表されます。 :class:`tzinfo` は抽象ベースクラスなので、サブクラスを定義して便利なメソッドをもつ適切な実装を提供する必要があります。標準ライブラリドキュメントではサンプル実装が提供されていますが、残念ながら :mod:`datetime` 内には実際の実装は含まれていません。独自クラスの作成に関する詳細と DST 対応クラスと同様に固定長のオフセットを使用するサンプルについては、標準ライブラリドキュメントを参照してください。 pytz_ もタイムゾーンの実装の詳細を調べるのに良い情報源です。

.. seealso::

    `datetime <http://docs.python.org/lib/module-datetime.html>`_
        .. The standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント

    :mod:`calendar`
        .. The :mod:`calendar` module.

        :mod:`calendar` モジュール

    :mod:`time`
        .. The :mod:`time` module.

        :mod:`time` モジュール

    `dateutil <http://labix.org/python-dateutil>`_
        .. dateutil from Labix extends the datetime module with additional features.

        Labix の :mod:`datetime` を機能拡張する dateutil モジュール

    `WikiPedia: Proleptic Gregorian calendar <http://en.wikipedia.org/wiki/Proleptic_Gregorian_calendar>`_
        .. A description of the Gregorian calendar system.

        グレゴリアンカレンダシステムの説明

    pytz_
        .. World Time Zone database

        世界のタイムゾーンデータベース

    `ISO 8601`_
        .. The standard for numeric representation of Dates and Time

        日付と時間の数値表現の標準規格

.. _ISO 8601: http://www.iso.org/iso/support/faqs/faqs_widely_used_standards/widely_used_standards_other/date_and_time_format.htm

.. _pytz: http://pytz.sourceforge.net/
