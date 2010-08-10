..
    =========================================
    locale -- POSIX cultural localization API
    =========================================

==============================================
locale -- POSIX 文化のローカライゼーション API
==============================================

..
    :synopsis: POSIX cultural localization API

.. module:: locale
    :synopsis: POSIX 文化のローカライゼーション API

..
    :Purpose: POSIX cultural localization API
    :Python Version: 1.5, with extensions through 2.5 (this discussion assumes 2.5)

:目的: POSIX 文化のローカライゼーション API
:Python バージョン: 1.5 で追加され 2.5 で機能拡張(本稿の内容は 2.5 を想定)

..
    The locale module is part of Python's internationalization and
    localization support library. It provides a standard way to handle
    operations that may depend on the language or location of your
    users. For example, formatting numbers as currency, comparing strings
    for sorting, and working with dates. It does not cover translation
    (see the :mod:`gettext` module) or Unicode encoding.

locale モジュールは Python の国際化の仕組みの一部でローカライゼーションをサポートするライブラリです。それはユーザの国やその言語に依存する可能性のある操作を扱うための標準的な方法を提供します。例えば、通貨のフォーマット、ソートの文字列比較、日付操作があります。locale モジュールは翻訳( :mod:`gettext` モジュールを参照)やユニコードエンコーディングについては対象としていません。

..
    Changing the locale can have application-wide ramifications, so the
    recommended practice is to avoid changing the value in a library and to let
    the application set it one time. In the examples below, I will change the
    locale several times for illustration purposes. It is far more likely that
    your application will set the locale once at startup and not change it.

ロケールを変更することはアプリケーション全体に影響を与えることがあります。そのため、推奨プラクティスはライブラリにある値を変更しないことと、1度だけアプリケーションにロケールをセットさせることです。次にサンプルがあります。ここでは説明のために何度かロケールを変更しますが、アプリケーションは起動時に1度だけロケールを設定して、そのロケールを変更しない使用方法がずっと多いでしょう。

..
    Probing the Current Locale
    ==========================

カレントロケールを調べる
========================

..
    The most common way to let the user change the locale settings for an
    application is through an environment variable (LC_ALL, LC_CTYPE, LANG, or
    LANGUAGE, depending on your platform). The application then calls
    locale.setlocale() without a hard-coded value, and the environment value is
    used.

ユーザにアプリケーションのロケール設定を変更させる最も一般的な方法は環境変数(LC_ALL, LC_CTYPE, LANG や LANGUAGE 等プラットホームに依存)を通して行うことです。アプリケーションはハードコーディングされた値ではなく locale.setlocale() を呼び出します。そして、環境変数の値が使用されます。

.. include:: locale_env_example.py
    :literal:
    :start-after: #end_pymotw_header

..
    On my Mac running OS X 10.5, this produces output like:

私の Mac(OS X 10.5 を使用) では次のように出力します。

::

    $ python locale_env_example.py
    Environment settings:
           LC_ALL =
           LC_CTYPE =
           LANG =
           LANGUAGE =

    Default locale: (None, 'mac-roman')
    From environment: (None, None)
    {'currency_symbol': '',
    'decimal_point': '.',
    'frac_digits': 127,
    'grouping': [127],
    'int_curr_symbol': '',
    'int_frac_digits': 127,
    'mon_decimal_point': '',
    'mon_grouping': [127],
    'mon_thousands_sep': '',
    'n_cs_precedes': 127,
    'n_sep_by_space': 127,
    'n_sign_posn': 127,
    'negative_sign': '',
    'p_cs_precedes': 127,
    'p_sep_by_space': 127,
    'p_sign_posn': 127,
    'positive_sign': '',
    'thousands_sep': ''}

..
    Now if we run the same script with the LANG variable set, you can see that the
    locale and default encoding change accordingly:

今、LANG 環境変数をセットし直して同じスクリプトを実行すると、それに応じてデフォルトエンコーディングとロケールが変更されることを確認できます。

..
    France::

フランス::

    $ LANG=fr_FR python locale_env_example.py
    Environment settings:
           LC_ALL =
           LC_CTYPE =
           LANG = fr_FR
           LANGUAGE =

    Default locale: (None, 'mac-roman')
    From environment: ('fr_FR', 'ISO8859-1')
    {'currency_symbol': 'Eu',
    'decimal_point': ',',
    'frac_digits': 2,
    'grouping': [127],
    'int_curr_symbol': 'EUR ',
    'int_frac_digits': 2,
    'mon_decimal_point': ',',
    'mon_grouping': [3, 3, 0],
    'mon_thousands_sep': ' ',
    'n_cs_precedes': 0,
    'n_sep_by_space': 1,
    'n_sign_posn': 2,
    'negative_sign': '-',
    'p_cs_precedes': 0,
    'p_sep_by_space': 1,
    'p_sign_posn': 1,
    'positive_sign': '',
    'thousands_sep': ''}

..
    Spain::

スペイン::

    $ LANG=es_ES python locale_env_example.py
    Environment settings:
           LC_ALL =
           LC_CTYPE =
           LANG = es_ES
           LANGUAGE =

    Default locale: (None, 'mac-roman')
    From environment: ('es_ES', 'ISO8859-1')
    {'currency_symbol': 'Eu',
    'decimal_point': ',',
    'frac_digits': 2,
    'grouping': [127],
    'int_curr_symbol': 'EUR ',
    'int_frac_digits': 2,
    'mon_decimal_point': ',',
    'mon_grouping': [3, 3, 0],
    'mon_thousands_sep': '.',
    'n_cs_precedes': 1,
    'n_sep_by_space': 1,
    'n_sign_posn': 1,
    'negative_sign': '-',
    'p_cs_precedes': 1,
    'p_sep_by_space': 1,
    'p_sign_posn': 1,
    'positive_sign': '',
    'thousands_sep': ''}

..
    Portgual::

ポルトガル::

    $ LANG=pt_PT python locale_env_example.py
    Environment settings:
           LC_ALL =
           LC_CTYPE =
           LANG = pt_PT
           LANGUAGE =

    Default locale: (None, 'mac-roman')
    From environment: ('pt_PT', 'ISO8859-1')
    {'currency_symbol': 'Eu',
    'decimal_point': ',',
    'frac_digits': 2,
    'grouping': [127],
    'int_curr_symbol': 'EUR ',
    'int_frac_digits': 2,
    'mon_decimal_point': '.',
    'mon_grouping': [3, 3, 0],
    'mon_thousands_sep': '.',
    'n_cs_precedes': 0,
    'n_sep_by_space': 1,
    'n_sign_posn': 1,
    'negative_sign': '-',
    'p_cs_precedes': 0,
    'p_sep_by_space': 1,
    'p_sign_posn': 1,
    'positive_sign': '',
    'thousands_sep': ' '}

..
    Poland::

ポーランド::

    $ LANG=pl_PL python locale_env_example.py
    Environment settings:
           LC_ALL =
           LC_CTYPE =
           LANG = pl_PL
           LANGUAGE =

    Default locale: (None, 'mac-roman')
    From environment: ('pl_PL', 'ISO8859-2')
    {'currency_symbol': 'z?\x82',
    'decimal_point': ',',
    'frac_digits': 2,
    'grouping': [3, 3, 0],
    'int_curr_symbol': 'PLN ',
    'int_frac_digits': 2,
    'mon_decimal_point': ',',
    'mon_grouping': [3, 3, 0],
    'mon_thousands_sep': ' ',
    'n_cs_precedes': 1,
    'n_sep_by_space': 2,
    'n_sign_posn': 4,
    'negative_sign': '-',
    'p_cs_precedes': 1,
    'p_sep_by_space': 2,
    'p_sign_posn': 4,
    'positive_sign': '',
    'thousands_sep': ' '}

..
    Currency
    ========

通貨
====

..
    So you can see that the currency symbol setting changes, the character to
    separate whole numbers from decimal fractions, etc. Now let's use the
    different locales to print the same information formatted for each of these
    different locales (US dollars, Euros, and Polish złoty):

通貨記号の設定変更、小数の数字の区切りを表す文字等を見ることができます。それぞれの国の違うロケール(US ドル、ユーロとポーランドのズウォティ)でフォーマットされた同じ通貨情報を表示してみましょう。

.. include:: locale_currency_example.py
    :literal:
    :start-after: #end_pymotw_header

..
    The output is this small table:

結果はこの小さな表です。

::

    $ python locale_currency_example.py
                    USA: $1234.56
                 France: 1234,56 Eu
                  Spain: Eu 1234,56
               Portugal: 1234.56 Eu
                 Poland: zł 1234,56

..
    Formatting Numbers
    ==================

数値のフォーマット
==================

..
    Numbers not related to currency are also formatted differently
    depending on the locale.  In particular, the "grouping" character used
    to separate large numbers into readable chunks is changed:

通貨を表さない数値もロケールに依存して違うフォーマットになります。特に大きな数値を読み易くするため分割に使用される "区切り" 文字が変更されます。

.. include:: locale_grouping.py
   :literal:
   :start-after: #end_pymotw_header

..
    To format numbers without the currency symbol, use :func:`format`
    instead of :func:`currency`.

通貨記号なしで数値のフォーマットを使用するために :func:`currency` の代わりに :func:`format` を使用してください。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'locale_grouping.py'))
.. }}}
.. {{{end}}}


..
    Parsing Numbers
    ===============

数値の解析
==========

..
    Besides generating output in different formats, the locale module
    helps with parsing input. The :mod:`locale` module provides
    :func:`atoi` and :func:`atof` functions for converting the strings to
    integer and floating point values based on the locale's numerical
    formatting conventions.

違うフォーマットの出力を生成することに加えて、locale モジュールは入力の解析にも役立ちます。 :mod:`locale` はロケールの数値フォーマット変換に基づいて文字列から整数や浮動小数の値へ変換するために :func:`atoi` と :func:`atof` 関数を提供します。

.. include:: locale_atof_example.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python locale_atof_example.py
                    USA: 1234.56 => 1234.560000
                 France: 1234,56 => 1234.560000
                  Spain: 1234,56 => 1234.560000
               Portugal: 1234.56 => 1234.560000
                 Poland: 1234,56 => 1234.560000

..
    Dates and Times
    ===============

日付と時刻
==========

..
    Another important aspect of localization is date and time formatting:

その他にローカライゼーションの重要な表示として日付と時刻のフォーマットがあります。

.. include:: locale_date_example.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python locale_date_example.py
                    USA: Sun May 20 10:19:54 2007
                 France: Dim 20 mai 10:19:54 2007
                  Spain: dom 20 may 10:19:54 2007
               Portugal: Dom 20 Mai 10:19:54 2007
                 Poland: ndz 20 maj 10:19:54 2007

..
    This discussion only covers some of the high-level functions in the localize
    module. There are others which are lower level (``format_string()``) or which relate
    to managing the locale for your application (``resetlocale()``). As usual, you will
    want to refer to the Python library documentation for more details.

ここでの話題は locale モジュールの高レベル関数のみ説明します。低レベルの関数(``format_string()``)、アプリケーションでロケールを管理するために関連する関数(``resetlocale()``)といった関数群もあります。いつもの通り、あなたは Python のライブラリドキュメントでさらに詳細を確認したくなるでしょう。

..
    `locale <http://docs.python.org/library/locale.html>`_
        The standard library documentation for this module.
    :mod:`gettext`
        Message catalogs for translations.

.. seealso::

    `locale <http://docs.python.org/library/locale.html>`_
        本モジュールの標準ライブラリドキュメント

    :mod:`gettext`
        翻訳のためのメッセージカタログ
