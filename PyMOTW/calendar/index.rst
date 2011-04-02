..
    ===========================
    calendar -- Work with dates
    ===========================

======================
calendar -- 日付の処理
======================

..
    :synopsis: The calendar module implements classes for working with dates to manage year/month/week oriented values.

.. module:: calendar
    :synopsis: calendar モジュールは年/月/週を管理する日付を処理するクラスを実装する 

..
    :Purpose: The calendar module implements classes for working with dates to manage year/month/week oriented values.
    :Python Version: 1.4, with updates in 2.5

:目的: calendar モジュールは年/月/週を管理する日付を処理するクラスを実装する 
:Python バージョン: 1.4 で追加、2.5 で拡張

..
    The calendar module defines the Calendar class, which encapsulates
    calculations for values such as the dates of the weeks in a given month or
    year. In addition, the TextCalendar and HTMLCalendar classes can produce
    pre-formatted output.

:mod:`calendar` モジュールは、特定の月または年のある週の日付といった計算をカプセル化する :class:`Calendar` クラスを定義します。さらに :class:`TextCalendar` と :class:`HTMLCalendar` クラスは、フォーマット済みの出力を生成できます。

..
    Formatting Examples
    ===================

フォーマットサンプル
====================

..
    A very simple example which produces formatted text output for a month
    using TextCalendar might use the prmonth() method.

:class:`TextCalendar` を使用して、ある月のフォーマット済みのテキスト出力を生成するには :func:`prmonth()` メソッドがとても簡単です。

.. include:: calendar_textcalendar.py
    :literal:
    :start-after: #end_pymotw_header

..
    The example configures TextCalendar to start weeks on Sunday,
    following the American convention. The default is to use the European
    convention of starting a week on Monday.

このサンプルはアメリカの規則に従い、週が日曜日から始まるように :class:`TextCalendar` を設定します。デフォルトは、週が月曜日から始まるヨーロッパの規則を使用します。

..
    The output looks like:

次のような結果になります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'calendar_textcalendar.py'))
.. }}}
.. {{{end}}}

..
    The HTML output for the same time period is slightly different, since there is
    no prmonth() method:

同じ期間を表す HTML 出力は、 :func:`prmonth()` メソッドがないのでわずかに違います。

.. include:: calendar_htmlcalendar.py
    :literal:
    :start-after: #end_pymotw_header

..
    The rendered output looks roughly the same, but is wrapped with HTML tags.  You can also see that each table cell has a class attribute corresponding to the day of the week.

レンダリングされた HTML 出力は大まかに同じように見えますが、HTML タグで囲まれます。さらにテーブルの各セルは、曜日に対するクラス属性をもちます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'calendar_htmlcalendar.py'))
.. }}}
.. {{{end}}}

..
    If you need to produce output in a format other than one of the available
    defaults, you can use :mod:`calendar` to calculate the dates and organize
    the values into week and month ranges, then iterate over the result yourself.
    The weekheader(), monthcalendar(), and yeardays2calendar() methods of Calendar
    are especially useful for that sort of work.

デフォルトで利用できるフォーマット以外の出力を生成する必要がある場合、 :mod:`calendar` で週と月の範囲に値をセットして日付を計算できます。そして、その実行結果を繰り返し処理できます。 :class:`Calendar` の :func:`weekheader()`, :func:`monthcalendar()`, :func:`yeardays2calendar()` メソッドは、特にそういった処理に便利です。

..
    Calling yeardays2calendar() produces a sequence of "month row" lists. Each
    list includes the months as another list of weeks. The weeks are lists of
    tuples made up of day number (1-31) and weekday number (0-6). Days that fall
    outside of the month have a day number of 0.

:func:`yeardays2calendar()` を呼び出すと、"月の行" のリストのシーケンスを生成します。それぞのリストには、週毎のリストが含まれています。週は日(1-31)と曜日(0-6)で構成されるタプルのリストです。その月に存在しない日は0になります。

.. include:: calendar_yeardays2calendar.py
    :literal:
    :start-after: #end_pymotw_header

..
    Calling yeardays2calendar(2007, 2) returns data for 2007, organized with 2
    months per row.

``yeardays2calendar(2007、2)`` を呼び出すと、2007年の1行につき2ヶ月分を構成するデータを返します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'calendar_yeardays2calendar.py'))
.. }}}
.. {{{end}}}

..
    This is equivalent to the data used by formatyear()

これは :func:`formatyear()` が使用するデータと同じです。

.. include:: calendar_formatyear.py
    :literal:
    :start-after: #end_pymotw_header

..
    which for the same arguments produces output like:

同じ引数を渡すと次のような出力を生成します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'calendar_formatyear.py'))
.. }}}
.. {{{end}}}

..
    If you want to format the output yourself for some reason (such as including
    links in HTML output), you will find the day_name, day_abbr, month_name, and
    month_abbr module attributes useful. They are automatically configured
    correctly for the current locale.

(HTML 出力にリンクを含めるといった)何らかの理由から自分で出力をフォーマットしたい場合、 :attr:`day_name`, :attr:`day_abbr`, :attr:`month_name`, :attr:`month_abbr` のモジュール属性が便利です。カレントロケールを検出して自動的に正しい設定を行ってくれます。

..
    Calculating Dates
    =================

日付計算
========

..
    Although the calendar module focuses mostly on printing full calendars in
    various formats, it also provides functions useful for working with dates in
    other ways, such as calculating dates for a recurring event. For example, the
    Python Atlanta User's Group meets the 2nd Thursday of every month. To
    calculate the dates for the meetings for a year, you could use the return
    value of monthcalendar().

:mod:`calendar` モジュールは、様々なフォーマットで完全なカレンダーを表示することを主な機能としていますが、その他にも定期的なイベント日程を計算するといった、日付を処理するのにも便利な関数も提供します。例えば、Python アトランタユーザグループは毎月第2木曜日にミーティングを行っています。年間のミーティング日程を計算するには :func:`monthcalendar()` の返り値を使用できます。

.. include:: calendar_monthcalendar.py
    :literal:
    :start-after: #end_pymotw_header

..
    Notice that some days are 0. Those are days of the week that overlap
    with the given month but which are part of another month.

日によっては 0 があることに注目してください。0 の日は指定された月が別の月と重複する週の日です。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'calendar_monthcalendar.py'))
.. }}}
.. {{{end}}}

..
    As mentioned earlier, the first day of the week is Monday. It is possible
    to change that by calling setfirstweekday(). On the other hand, since the
    calendar module includes constants for indexing into the date ranges returned
    by monthcalendar(), it is more convenient to skip that step in this case.

前節で説明したように週の最初の日は月曜日です。週の最初の曜日は :func:`setfirstweekday()` を呼び出すことで変更できます。別の方法としては、 :mod:`calendar` モジュールは :func:`monthcalendar()` が返す日付の範囲にインデクシングするための定数を含むので、この場合はその手順を省略してかなり便利です。

..
    To calculate the PyATL meeting dates for 2007, assuming the second Thursday of
    every month, we can use the 0 values to tell us whether the Thursday of the
    first week is included in the month (or if the month starts, for example on a
    Friday).

毎月第2木曜日と仮定した 2007 年の PyATL ミーティングの日程を計算するには、その月の最初の週に木曜日が含まれるかどうか(もしくは、月の最初の日が金曜日か等)を調べるのに 0 の値を使用できます。

.. include:: calendar_secondthursday.py
    :literal:
    :start-after: #end_pymotw_header

..
    So the PyATL meeting schedule for the year is:

2007 年の PyATL ミーティングのスケジュールは次になります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'calendar_secondthursday.py'))
.. }}}
.. {{{end}}}


.. seealso::

    `calendar <http://docs.python.org/library/calendar.html>`_
        .. The standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント

    :mod:`time`
        .. Lower-level time functions.

        低レベルの時間関数

    :mod:`datetime`
        .. Manipulate date values, including timestamps and time zones.

        タイムスタンプとタイムゾーンを含む日付を扱う
