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
    :Purpose: Format and parse values that depend on location or language.
    :Available In: 1.5 and later

:目的: ロケーションや言語に依存する値の解析やフォーマット
:利用できるバージョン: 1.5 以上

..
    The :mod:`locale` module is part of Python's internationalization and
    localization support library. It provides a standard way to handle
    operations that may depend on the language or location of a user. For
    example, it handles formatting numbers as currency, comparing strings
    for sorting, and working with dates. It does not cover translation
    (see the :mod:`gettext` module) or Unicode encoding.

:mod:`locale` モジュールは Python の国際化の仕組みの一部でローカライゼーションをサポートするライブラリです。それはユーザの国やその言語に依存する可能性のある操作を扱うための標準的な方法を提供します。例えば、通貨のフォーマット、ソートの文字列比較、日付操作があります。locale モジュールは翻訳( :mod:`gettext` モジュールを参照)やユニコードエンコーディングについては対象としていません。

.. note::
  ..
      Changing the locale can have application-wide ramifications, so the
      recommended practice is to avoid changing the value in a library and
      to let the application set it one time. In the examples below, the
      locale is changed several times within a short program to highlight
      the differences in the settings of various locales. It is far more
      likely that your application will set the locale once at startup and
      not change it.

  ロケールを変更することはアプリケーション全体に影響を与えることがあります。そのため、推奨プラクティスはライブラリ内の値を変更しないことと、1度だけアプリケーションにロケールをセットさせることです。次にサンプルがあります。ここでは様々なロケールを設定することの違いを分かり易く説明するために何度かロケールを変更します。通常のアプリケーションは起動時に1度だけロケールを設定して、そのロケールを変更せずに使用することがずっと多いでしょう。

..
    Probing the Current Locale
    ==========================

カレントロケールを調べる
========================

..
    The most common way to let the user change the locale settings for an
    application is through an environment variable (:data:`LC_ALL`,
    :data:`LC_CTYPE`, :data:`LANG`, or :data:`LANGUAGE`, depending on the
    platform). The application then calls :func:`setlocale` without a
    hard-coded value, and the environment value is used.

ユーザにアプリケーションのロケール設定を変更させる最も一般的な方法は環境変数( :data:`LC_ALL`, :data:`LANG`, や :data:`LANGUAGE` 等プラットホームに依存)を通して行うことです。アプリケーションはハードコーディングされた値ではなく :func:`locale.setlocale` を呼び出します。そして、環境変数の値が使用されます。

.. include:: locale_env_example.py
    :literal:
    :start-after: #end_pymotw_header

..
    The :func:`localeconv` method returns a dictionary containing the
    locale's conventions.  The full list of value names and definitions is
    covered in the standard library documentation.

:func:`localeconv` メソッドはロケール規約を含む辞書を返します。値の名前と定義の完全なリストは標準ライブラリのドキュメントで説明されています。

..
    A Mac running OS X 10.6 with all of the variables unset produces this output:

私の MacOS X 10.6 では、全ての変数をアンセットすると次のように出力します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'export LANG=; export LC_CTYPE=; python locale_env_example.py', interpreter=None))
.. }}}

::

	$ export LANG=; export LC_CTYPE=; python locale_env_example.py
	
	Environment settings:
		LC_ALL = 
		LC_CTYPE = 
		LANG = 
		LANGUAGE = 
	
	Locale from environment: (None, None)
	
	Numeric formatting:
	
	  Decimal point      : "."
	  Grouping positions : []
	  Thousands separator: ""
	
	Monetary formatting:
	
	  International currency symbol             : "''"
	  Local currency symbol                     : '' ()
	  Symbol precedes positive value            : 127
	  Symbol precedes negative value            : 127
	  Decimal point                             : ""
	  Digits in fractional values               : 127
	  Digits in fractional values, international: 127
	  Grouping positions                        : []
	  Thousands separator                       : ""
	  Positive sign                             : ""
	  Positive sign position                    : Unspecified
	  Negative sign                             : ""
	  Negative sign position                    : Unspecified
	
	

.. {{{end}}}

..
    Running the same script with the :data:`LANG` variable set shows how
    the locale and default encoding change:

:data:`LANG` 環境変数をセットして同じスクリプトを実行すると、それに応じてデフォルトエンコーディングとロケールが変更されることを確認できます。

..
    France (``fr_FR``):

フランス (``fr_FR``):

.. {{{cog
.. cog.out(run_script(cog.inFile, 'LANG=fr_FR LC_CTYPE=fr_FR LC_ALL=fr_FR python locale_env_example.py', interpreter=None))
.. }}}

::

	$ LANG=fr_FR LC_CTYPE=fr_FR LC_ALL=fr_FR python locale_env_example.py
	
	Environment settings:
		LC_ALL = fr_FR
		LC_CTYPE = fr_FR
		LANG = fr_FR
		LANGUAGE = 
	
	Locale from environment: ('fr_FR', 'ISO8859-1')
	
	Numeric formatting:
	
	  Decimal point      : ","
	  Grouping positions : [127]
	  Thousands separator: ""
	
	Monetary formatting:
	
	  International currency symbol             : "'EUR '"
	  Local currency symbol                     : 'Eu' (Eu)
	  Symbol precedes positive value            : 0
	  Symbol precedes negative value            : 0
	  Decimal point                             : ","
	  Digits in fractional values               : 2
	  Digits in fractional values, international: 2
	  Grouping positions                        : [3, 3, 0]
	  Thousands separator                       : " "
	  Positive sign                             : ""
	  Positive sign position                    : Before value and symbol
	  Negative sign                             : "-"
	  Negative sign position                    : After value and symbol
	
	

.. {{{end}}}

..
    Spain (``es_ES``):

スペイン (``es_ES``):

.. {{{cog
.. cog.out(run_script(cog.inFile, 'LANG=es_ES LC_CTYPE=es_ES LC_ALL=es_ES python locale_env_example.py', interpreter=None))
.. }}}

::

	$ LANG=es_ES LC_CTYPE=es_ES LC_ALL=es_ES python locale_env_example.py
	
	Environment settings:
		LC_ALL = es_ES
		LC_CTYPE = es_ES
		LANG = es_ES
		LANGUAGE = 
	
	Locale from environment: ('es_ES', 'ISO8859-1')
	
	Numeric formatting:
	
	  Decimal point      : ","
	  Grouping positions : [127]
	  Thousands separator: ""
	
	Monetary formatting:
	
	  International currency symbol             : "'EUR '"
	  Local currency symbol                     : 'Eu' (Eu)
	  Symbol precedes positive value            : 1
	  Symbol precedes negative value            : 1
	  Decimal point                             : ","
	  Digits in fractional values               : 2
	  Digits in fractional values, international: 2
	  Grouping positions                        : [3, 3, 0]
	  Thousands separator                       : "."
	  Positive sign                             : ""
	  Positive sign position                    : Before value and symbol
	  Negative sign                             : "-"
	  Negative sign position                    : Before value and symbol
	
	

.. {{{end}}}

..
    Portgual (``pt_PT``):

ポルトガル (``pt_PT``):

.. {{{cog
.. cog.out(run_script(cog.inFile, 'LANG=pt_PT LC_CTYPE=pt_PT LC_ALL=pt_PT python locale_env_example.py', interpreter=None))
.. }}}

::

	$ LANG=pt_PT LC_CTYPE=pt_PT LC_ALL=pt_PT python locale_env_example.py
	
	Environment settings:
		LC_ALL = pt_PT
		LC_CTYPE = pt_PT
		LANG = pt_PT
		LANGUAGE = 
	
	Locale from environment: ('pt_PT', 'ISO8859-1')
	
	Numeric formatting:
	
	  Decimal point      : ","
	  Grouping positions : []
	  Thousands separator: " "
	
	Monetary formatting:
	
	  International currency symbol             : "'EUR '"
	  Local currency symbol                     : 'Eu' (Eu)
	  Symbol precedes positive value            : 0
	  Symbol precedes negative value            : 0
	  Decimal point                             : "."
	  Digits in fractional values               : 2
	  Digits in fractional values, international: 2
	  Grouping positions                        : [3, 3, 0]
	  Thousands separator                       : "."
	  Positive sign                             : ""
	  Positive sign position                    : Before value and symbol
	  Negative sign                             : "-"
	  Negative sign position                    : Before value and symbol
	
	

.. {{{end}}}

..
    Poland (``pl_PL``):

ポーランド (``pl_PL``):

.. {{{cog
.. cog.out(run_script(cog.inFile, 'LANG=pl_PL LC_CTYPE=pl_PL LC_ALL=pl_PL python locale_env_example.py', interpreter=None))
.. }}}

::

	$ LANG=pl_PL LC_CTYPE=pl_PL LC_ALL=pl_PL python locale_env_example.py
	
	Environment settings:
		LC_ALL = pl_PL
		LC_CTYPE = pl_PL
		LANG = pl_PL
		LANGUAGE = 
	
	Locale from environment: ('pl_PL', 'ISO8859-2')
	
	Numeric formatting:
	
	  Decimal point      : ","
	  Grouping positions : [3, 3, 0]
	  Thousands separator: " "
	
	Monetary formatting:
	
	  International currency symbol             : "'PLN '"
	  Local currency symbol                     : 'z\xc5\x82' (zł)
	  Symbol precedes positive value            : 1
	  Symbol precedes negative value            : 1
	  Decimal point                             : ","
	  Digits in fractional values               : 2
	  Digits in fractional values, international: 2
	  Grouping positions                        : [3, 3, 0]
	  Thousands separator                       : " "
	  Positive sign                             : ""
	  Positive sign position                    : After value
	  Negative sign                             : "-"
	  Negative sign position                    : After value
	
	

.. {{{end}}}

..
    Currency
    ========

通貨
====

..
    The example output above shows that changing the locale updates the
    currency symbol setting and the character to separate whole numbers
    from decimal fractions.  This example loops through several different
    locales to print a positive and negative currency value formatted for
    each locale:

上述したサンプルの出力は、ロケール設定を変更すると通貨記号の設定や小数の数字の区切り文字を更新することを表します。このサンプルは複数の異なるロケール設定を行って、ロケール毎の正負の通貨の値を表示します。

.. include:: locale_currency_example.py
    :literal:
    :start-after: #end_pymotw_header

..
    The output is this small table:

結果はこの小さな表です。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'locale_currency_example.py'))
.. }}}

::

	$ python locale_currency_example.py
	
	                 USA:   $1234.56   -$1234.56
	              France: 1234,56 Eu  1234,56 Eu-
	               Spain: Eu 1234,56  -Eu 1234,56
	            Portugal: 1234.56 Eu  -1234.56 Eu
	              Poland: zł 1234,56  zł 1234,56-

.. {{{end}}}

..
    Formatting Numbers
    ==================

数値のフォーマット
==================

..
    Numbers not related to currency are also formatted differently
    depending on the locale.  In particular, the *grouping* character used
    to separate large numbers into readable chunks is changed:

通貨を表さない数値もロケールに依存して違うフォーマットになります。特に大きな数値を読み易くするため分割に使用される *区切り* 文字が変更されます。

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

::

	$ python locale_grouping.py
	
	              Locale         Integer                Float
	                 USA         123,456           123,456.78
	              France          123456            123456,78
	               Spain          123456            123456,78
	            Portugal          123456            123456,78
	              Poland         123 456           123 456,78

.. {{{end}}}


..
    Parsing Numbers
    ===============

数値の解析
==========

..
    Besides generating output in different formats, the :mod:`locale`
    module helps with parsing input. It includes :func:`atoi` and
    :func:`atof` functions for converting the strings to integer and
    floating point values based on the locale's numerical formatting
    conventions.

違うフォーマットの出力を生成することに加えて :mod:`locale` モジュールは入力の解析にも役立ちます。それはロケールの数値フォーマット変換に基づいて文字列から整数や浮動小数の値へ変換するために :func:`atoi` と :func:`atof` 関数を提供します。

.. include:: locale_atof_example.py
    :literal:
    :start-after: #end_pymotw_header

..
    The grouping and decimal separator values 

数字の括りや小数の区切りは次のようになります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'locale_atof_example.py'))
.. }}}

::

	$ python locale_atof_example.py
	
	                 USA:  1,234.56 => 1234.560000
	              France:   1234,56 => 1234.560000
	               Spain:   1234,56 => 1234.560000
	            Portugal:   1234.56 => 1234.560000
	              Poland:  1 234,56 => 1234.560000

.. {{{end}}}

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

.. {{{cog
.. cog.out(run_script(cog.inFile, 'locale_date_example.py'))
.. }}}

::

	$ python locale_date_example.py
	
	                 USA: Thu Feb 21 06:35:54 2013
	              France: Jeu 21 fév 06:35:54 2013
	               Spain: jue 21 feb 06:35:54 2013
	            Portugal: Qui 21 Fev 06:35:54 2013
	              Poland: czw 21 lut 06:35:54 2013

.. {{{end}}}

..
    This discussion only covers some of the high-level functions in the
    :mod:`locale` module. There are others which are lower level
    (:func:`format_string`) or which relate to managing the locale for
    your application (:func:`resetlocale`).

ここでの話題は :mod:`locale` モジュールの高レベル関数のみ説明します。低レベルの関数(:func:`format_string`)、アプリケーションでロケールを管理するために関連する関数(:func:`resetlocale`)といった関数群もあります。いつもの通り、あなたは Python のライブラリドキュメントでさらに詳細を確認したくなるでしょう。

.. seealso::

    `locale <http://docs.python.org/library/locale.html>`_
        .. The standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント

    :mod:`gettext`
        .. Message catalogs for translations.

        翻訳のためのメッセージカタログ
