..
    =========================================================
    optparse -- Command line option parser to replace getopt.
    =========================================================

=========================================================
optparse -- getopt に代わるコマンドラインオプションパーサ
=========================================================

..
    :synopsis: Command line option parser to replace :mod:`getopt`.

.. module:: optparse
    :synopsis: :mod:`getopt` に代わるコマンドラインオプションパーサ

..
    :Purpose: Command line option parser to replace :mod:`getopt`.
    :Python Version: 2.3

:目的: :mod:`getopt` に代わるコマンドラインオプションパーサ
:Python バージョン: 2.3

..
    The :mod:`optparse` module is a modern alternative for command line
    option parsing that offers several features not available in
    :mod:`getopt`, including type conversion, option callbacks, and
    automatic help generation. There are many more features to
    :mod:`optparse` than can be covered here, but this section will
    introduce some of the more commonly used capabilities.

:mod:`optparse` モジュールはコマンドラインオプションを解析するためのモダンな代替方法で、データ型の変換、オプション処理のコールバック、自動ヘルプ生成といった :mod:`getopt` にはない機能を提供します。ここで説明する内容よりも :mod:`optparse` にはもっと多くの機能があります。とはいえ、本稿ではより汎用的な機能の使用方法を紹介します。

..
    Creating an OptionParser
    ========================

OptionParser を作成する
=======================

..
    There are two phases to parsing options with :mod:`optparse`. First,
    the :class:`OptionParser` instance is constructed and configured with
    the expected options. Then a sequence of options is fed in and
    processed.

:mod:`optparse` を使用してオプションを解析するには2つの段階があります。先ずは :class:`OptionParser` インスタンスを構築して、使用するオプションを設定します。次にオプションが渡されて処理されます。

::

    import optparse
    parser = optparse.OptionParser()

..
    Usually, once the parser has been created, each option is added to the
    parser explicitly, with information about what to do when the option
    is encountered on the command line. It is also possible to pass a list
    of options to the :class:`OptionParser` constructor, but that form is
    not used as frequently.

通常 parser は1度だけ作成されます。そのオプションがコマンドラインで現れたときにどう処理するかに関しての情報と共に、各オプションは parser へ明示的に追加されます。 :class:`OptionParser` コンストラクタへオプションのリストを引数で渡すことも可能ですが、その方法はあまり使用されないと思います。

..
    Defining Options
    ----------------

オプションを定義する
--------------------

..
    Options should be added one at a time using the :func:`add_option()`
    method. Any un-named string arguments at the beginning of the argument
    list are treated as option names. To create aliases for an option
    (i.e., to have a short and long form of the same option), simply pass
    multiple names.

オプションは :func:``add_option()`` メソッドを使用して1度に1つだけ追加すべきです。引数リストの最初にある文字列はオプション名として扱います。あるオプションのエイリアスを作成するために(例えば、同じオプションを表す短いオプション名と長いオプション名を持つには)、単純に両方のオプション名を引数に渡します。

..
    Parsing a Command Line
    ----------------------

コマンドラインを解析する
------------------------

..
    After all of the options are defined, the command line is parsed by
    passing a sequence of argument strings to :func:`parse_args()`. By
    default, the arguments are taken from ``sys.argv[1:]``, but a list can
    be passed explicitly as well. The options are processed using the
    GNU/POSIX syntax, so option and argument values can be mixed in the
    sequence.

すべてのオプションが定義された後で :func:`parse_args()` へコマンドラインの引数文字列を渡すことで解析されます。デフォルトでは、その引数は ``sys.argv[1:]`` から取得されますが、任意のリストで明示的に渡すことができます。そのオプションは GNU/POSIX 構文を使用して処理されるので、オプションと引数の値はシーケンスに混在してセットされます。

..
    The return value from :func:`parse_args()` is a two-part tuple
    containing an :class:`Values` instance and the list of arguments to
    the command that were not interpreted as options. The default
    processing action for options is to store the value using the name
    given in the *dest* argument to :func:`add_option`.  The
    :class:`Values` instance returned by :func:`parse_args` holds the
    option values as attributes, so if an option's :data:`dest` is set to
    ``"myoption"``, the value is accessed as ``options.myoption``.

:func:`parse_args()` は :class:`Values` インスタンスとオプションと見なされないコマンドの引数リストの2つの値を持つタプルを返します。オプションのデフォルトアクションは :func:`add_option` への *dest* 引数に渡される名前を使用してその値を保持します。 :func:`parse_args()` が返す :class:`Values` インスタンスは属性としてオプションの値を保持します。そのため、もしオプションの :data:`dest` が ``"myoption"`` の場合、その値は ``options.myoption`` でアクセスします。

..
    Short and Long-Form Options
    ===========================

短いオプション名と長いオプション名
==================================

..
    Here is a simple example with three different options: a boolean
    option (``-a``), a simple string option (``-b``), and an integer
    option (``-c``).

3つの異なるオプションを使用する簡単なサンプルを紹介します。ブーリアンオプション (``-a``)、シンプルな文字列オプション (``-b``)、そして整数オプション (``-c``) です。

.. include:: optparse_short.py
    :literal:
    :start-after: #end_pymotw_header

..
    The options on the command line are parsed with the same rules that
    :func:`getopt.gnu_getopt()` uses, so there are two ways to pass values
    to single character options. The example above uses both forms,
    ``-bval`` and ``-c val``.

コマンドラインオプションは :func:`getopt.gnu_getopt()` を使用するのと同じルールで解析されます。そのため、1文字オプションへ値を渡す方法が2つあります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'optparse_short.py'))
.. }}}
.. {{{end}}}

..
    Notice that the type of the value associated with ``'c'`` in the
    output is an integer, since the :class:`OptionParser` was told to
    convert the argument before storing it.

実行後の出力の ``'c'`` に対する値のデータ型が整数型であることに注意してください。それは :class:`OptionParser` クラスがその値を格納する前にその引数を変換して保持するからです。

..
    Unlike with :mod:`getopt`, "long" option names are not handled any
    differently by :mod:`optparse`:

:mod:`getopt` と違い、 :mod:`optparse` は "長い" オプション名を別処理として扱いません。

.. include:: optparse_long.py
    :literal:
    :start-after: #end_pymotw_header

..
    And the results are similar:

その出力結果も似ています。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'optparse_long.py'))
.. }}}
.. {{{end}}}

..
    Comparing with getopt
    =====================

getopt と比較する
=================

..
    Since :mod:`optparse` is supposed to replace :mod:`getopt`, this
    example re-implements the same example program used in the section
    about :mod:`getopt`:

:mod:`optparse` は :mod:`getopt` を置き換えるためにサポートされたので、このサンプルは :mod:`getopt`: のセクションで使用した同じサンプルプログラムを再実装します。

.. include:: optparse_getoptcomparison.py
    :literal:
    :start-after: #end_pymotw_header

..
    Notice how the options ``-o`` and ``--output`` are aliased by being
    added at the same time. Either option can be used on the command line.
    The short form:

オプション ``-o`` と ``--output`` が同時に追加されるようにエイリアス化する方法に注意してください。どちらか一方のオプションがコマンドラインで使用されます。短いオプション名で実行します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'optparse_getoptcomparison.py -o output.txt'))
.. }}}
.. {{{end}}}

..
    or the long form:

又は、長いオプション名で実行します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'optparse_getoptcomparison.py --output output.txt'))
.. }}}
.. {{{end}}}

..
    Any unique prefix of the long option can also be used:

長いオプション名のユニークな接頭辞も使用することができます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'optparse_getoptcomparison.py --out output.txt'))
.. }}}
.. {{{end}}}


..
    Option Values
    =============

オプション値
============

..
    The default processing action is to store the argument to the option.
    If a type is provided, the argument value is converted to that type
    before it is stored.

デフォルトのアクション処理はオプションに対する引数を保持するためのものです。もし型が提供されるなら、引数の値はその値が保持される前に指定された型に変換されます。

..
    Setting Defaults
    ----------------

デフォルト値の設定
------------------

..
    Since options are by definition optional, applications should
    establish default behavior when an option is not given on the command
    line.  A default value for an individual option can be provided when
    the option is defined.

オプションの指定は任意なので、アプリケーションはコマンドラインでオプションが与えられなかったときにデフォルトの振る舞いを定義すべきです。個々のオプションのデフォルト値はそのオプションが定義されたときに提供されます。

.. include:: optparse_default.py
   :literal:
   :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'optparse_default.py'))
.. cog.out(run_script(cog.inFile, 'optparse_default.py -o "different value"', include_prefix=False))
.. }}}
.. {{{end}}}

..
    Defaults can also be loaded after the options are defined using
    keyword arguments to :func:`set_defaults`.

また、デフォルト値はオプションが定義された後で :func:`set_defaults` に対するキーワード引数を使用して読み込むこともできます。

.. include:: optparse_set_defaults.py
   :literal:
   :start-after: #end_pymotw_header

..
    This form is useful when loading defaults from a configuration file or
    other source, instead of hard-coding them.

この方法は、ハードコーディングせずに設定ファイルか、その他のソースファイルからデフォルト値を読み込むときに便利です。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'optparse_set_defaults.py'))
.. cog.out(run_script(cog.inFile, 'optparse_set_defaults.py -o "different value"', include_prefix=False))
.. }}}
.. {{{end}}}

..
    All defined options are available as attributes of the :class:`Values`
    instance returned by :func:`parse_args` so applications do not need to
    check for the presence of an option before trying to use its value.
    
定義された全オプションは :func:`parse_args` が返す :class:`Values` インスタンスの属性として利用できます。そのため、アプリケーションはその値を使用しようとする前にオプションの存在を確認する必要がありません。

.. include:: optparse_no_default.py
   :literal:
   :start-after: #end_pymotw_header

..
    If no default value is given for an option, and the option is not
    specified on the command line, its value is ``None``.

もしオプションのデフォルト値がなく、コマンドラインでも指定されなかった場合、その値は ``None`` になります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'optparse_no_default.py'))
.. cog.out(run_script(cog.inFile, 'optparse_no_default.py -o "different value"', include_prefix=False))
.. }}}
.. {{{end}}}

..
    Type Conversion
    ---------------

型変換
------

..
    :mod:`optparse` will convert option values from strings to integers,
    floats, longs, and complex values.  To enable the conversion, specify
    the *type* of the option as an argument to :func:`add_option`.

:mod:`optparse` はオプションの値を文字列から整数、小数、長整数や複雑な値へ変換します。変換を行うためには、 :func:`add_option` に対する引数としてオプションの *type* を指定します。

.. include:: optparse_types.py
   :literal:
   :start-after: #end_pymotw_header

..
    If an option's value cannot be converted to the specified type, an
    error is printed and the program exits.

もしオプションの値が指定された型に変換できない場合、エラーを表示してプログラムを終了します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'optparse_types.py -i 1 -f 3.14 -l 1000000 -c 1+2j'))
.. cog.out(run_script(cog.inFile, 'optparse_types.py -i a', ignore_error=True, include_prefix=False))
.. }}}
.. {{{end}}}

..
    Custom conversions can be created by subclassing the :class:`Option`
    class.  See the standard library documentation for complete details.

:class:`Option` クラスをサブクラス化することでカスタム変換を行うことができます。詳細は標準ライブラリドキュメントを参照してください。

..
    Enumerations
    ------------

選択肢
------

..
    The :const:`choice` type provides validation using a list of candidate
    strings.  Set *type* to choice and provide the list of valid values
    using the *choices* argument to :func:`add_option`.

:const:`choice` 型は候補文字列のリストを使用するバリデーションを提供します。 *type* に choise をセットして :func:`add_option` に対する *choises* 引数に有効な値リストを指定します。

.. include:: optparse_choice.py
   :literal:
   :start-after: #end_pymotw_header

..
    Invalid inputs result in an error message that shows the allowed list
    of values.

不正な入力を行うと、許容される値リストのエラーメッセージを表示します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'optparse_choice.py -c a'))
.. cog.out(run_script(cog.inFile, 'optparse_choice.py -c b', include_prefix=False))
.. cog.out(run_script(cog.inFile, 'optparse_choice.py -c d', include_prefix=False, ignore_error=True, break_lines_at=70))
.. }}}
.. {{{end}}}

..
    Option Actions
    ==============

オプションのアクション
======================

..
    Unlike :mod:`getopt`, which only *parses* the options, :mod:`optparse`
    is a full option *processing* library. Options can trigger different
    actions, specified by the action argument to
    :func:`add_option()`. Supported actions include storing the argument
    (singly, or as part of a list), storing a constant value when the
    option is encountered (including special handling for true/false
    values for boolean switches), counting the number of times an option
    is seen, and calling a callback.  The default action is
    :const:`store`, and does not need to be specified explicitly.

オプションの解析のみを行う :mod:`getopt` と違い :mod:`optparse` は完全なオプション *処理* ライブラリです。オプションは違うアクションのトリガーになることができます。それは :func:`add_option()` への action 引数で指定されます。サポートされているアクションは、その引数を格納する(1つずつか、リストの一部)、定数の引数オプションが指定されたときに定数の値(真偽値を扱うために特化した操作も含む)を格納する、あるオプションが現れた回数をカウントする、そしてコールバック関数を呼び出すがあります。デフォルトアクションは :const:`store` で、明示的に指定する必要はありません。

..
    Constants
    ---------

定数
----

..
    When options represent a selection of fixed alternatives, such as
    operating modes of an application, creating separate explicit options
    makes it easier to document them.  The :const:`store_const` action is
    intended for this purpose.  

アプリケーションの操作モードのような、オプションがある選択範囲に固定されるとき、それを分かり易くするために明示的に独立したオプションを作成します。 :const:`store_const` アクションはこの目的に適しています。

.. include:: optparse_store_const.py
   :literal:
   :start-after: #end_pymotw_header

..
    The :const:`store_const` action associates a constant value in the
    application with the option specified by the user.  Several options
    can be configured to store different constant values to the same
    *dest* name, so the application only has to check a single setting.

:const:`store_const` アクションは、ユーザが指定したオプションでアプリケーションの定数を関連付けます。同じ *dest* 名に対して違う定数値を格納するために複数のオプションが設定されるので、アプリケーションは1つの設定のみを確認する必要があります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'optparse_store_const.py'))
.. cog.out(run_script(cog.inFile, 'optparse_store_const.py --fire', include_prefix=False))
.. }}}
.. {{{end}}}

..
    Boolean Flags
    -------------

ブーリアンフラグ
----------------

..
    Boolean options are implemented using special actions for storing true
    and false constant values.

ブーリアンオプションは True や False の定数値を格納する特別なアクションを使用して実装されます。

.. include:: optparse_boolean.py
   :literal:
   :start-after: #end_pymotw_header

..
    True and false versions of the same flag can be created by configuring
    their *dest* name to the same value.

同じフラグの True や Faslse バージョンは同じ値に対する *dest* 名を設定することで作成されます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'optparse_boolean.py'))
.. cog.out(run_script(cog.inFile, 'optparse_boolean.py -t', include_prefix=False))
.. cog.out(run_script(cog.inFile, 'optparse_boolean.py -f', include_prefix=False))
.. }}}
.. {{{end}}}

..
    Repeating Options
    -----------------

繰り返しオプション
------------------

..
    There are three ways to handle repeated options.  The default is to
    overwrite any existing value so that the last option specified is
    used.  The :const:`store` action works this way.

繰り返しオプションを扱うために3つの方法があります。デフォルトは指定された最後のオプションを使用するように既存の値を上書きすることです。 :const:`store` アクションはこの方法で動作します。

..
    Using the :const:`append` action, it is possible to accumulate values
    as an option is repeated, creating a list of values.  Append mode is
    useful when multiple responses are allowed, and specifying them
    separately is easier for the user than constructing a parsable syntax.

:const:`append` アクションを使用すると、オプションが繰り返されると値を蓄積することができます。追加モードは複数の応答が返されるときに便利で、ユーザは解析可能な構文を構築するよりも簡単に指定できます。

.. include:: optparse_append.py
   :literal:
   :start-after: #end_pymotw_header

..
    The order of the values given on the command line is preserved, in
    case it is important for the application.

コマンドラインで与えられた値の順番は保持されます。それはアプリケーションによっては重要なときがあります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'optparse_append.py'))
.. cog.out(run_script(cog.inFile, 'optparse_append.py -o a.out', include_prefix=False))
.. cog.out(run_script(cog.inFile, 'optparse_append.py -o a.out -o b.out', include_prefix=False))
.. }}}
.. {{{end}}}

..
    Sometimes it is enough to know how many times an option was given, and
    the associated value is not needed.  For example, many applications
    allow the user to repeat the ``-v`` option to increase the level of
    verbosity of their output.  The :const:`count` action increments a
    value each time the option appears.

1つのオプションが何回与えられたかを知りたくて関連付けられた値が必要ではないときがあります。例えば、多くのアプリケーションは出力の冗長レベルを上げるために ``-v`` オプションを繰り返すことができます。 :const:`count` アクションはそのオプションが現れる毎にその値が増加します。

.. include:: optparse_count.py
   :literal:
   :start-after: #end_pymotw_header

..
    Since the ``-v`` option doesn't take an argument, it can be repeated
    using the syntax ``-vv`` as well as through separate individual
    options.

``-v`` オプションは引数を受け取らないので、個別にオプションが指定されたときと同様に ``-vv`` といった構文で繰り返すことができます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'optparse_count.py'))
.. cog.out(run_script(cog.inFile, 'optparse_count.py -v', include_prefix=False))
.. cog.out(run_script(cog.inFile, 'optparse_count.py -v -v', include_prefix=False))
.. cog.out(run_script(cog.inFile, 'optparse_count.py -vv', include_prefix=False))
.. cog.out(run_script(cog.inFile, 'optparse_count.py -q', include_prefix=False))
.. }}}
.. {{{end}}}

..
    Callbacks
    ---------

コールバック
------------

..
    Beside saving the arguments for options directly, it is possible to
    define callback functions to be invoked when the option is encountered
    on the command line. Callbacks for options take four arguments: the
    :class:`Option` instance causing the callback, the option string from
    the command line, any argument value associated with the option, and
    the :class:`OptionParser` instance doing the parsing work.

オプションの引数を直接保持することに加えて、コマンドラインでそのオプションが指定されたときに呼び出されるコールバック関数を定義することもできます。オプションのためのコールバック関数は4つの引数を取ります。それらはコールバックを呼び出す :class:`Option` インスタンス、コマンドラインからのオプションの文字列、そのオプションに渡される引数の値、オプションの解析を行う :class:`OptionParser` インスタンスです。

.. include:: optparse_callback.py
    :literal:
    :start-after: #end_pymotw_header

..
    In this example, the ``--with`` option is configured to take a string
    argument (other types such as integers and floats are support as
    well).

このサンプルでは ``--with`` オプションが文字列の引数を取るように設定されています(同様に整数型や浮動小数点型のようなデータ型もサポートされています)。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'optparse_callback.py'))
.. }}}
.. {{{end}}}

..
    Callbacks can be configured to take multiple arguments using the *nargs*
    option.

コールバックは *nargs* オプションを使用して複数の引数を取得して設定することができます。

.. include:: optparse_callback_nargs.py
    :literal:
    :start-after: #end_pymotw_header

..
    In this case, the arguments are passed to the callback function as a tuple via
    the value argument.

このケースでは、引数は value 引数で1つのタプルとしてコールバック関数へ渡されます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'optparse_callback_nargs.py'))
.. }}}
.. {{{end}}}

..
    Help Messages
    =============

ヘルプメッセージ
================

..
    The :class:`OptionParser` automatically includes a help option to all
    option sets, so the user can pass ``--help`` on the command line to
    see instructions for running the program. The help message includes
    all of the options with an indication of whether or not they take an
    argument. It is also possible to pass help text to
    :class:`add_option()` to give a more verbose description of an option.

:class:`OptionParser` は自動的に全てのオプションセットに対して ``--help`` オプションを追加します。そのため、ユーザはコマンドラインで ``--help`` を指定することで、プログラム実行のためのヘルプを確認することができます。

.. include:: optparse_help.py
    :literal:
    :start-after: #end_pymotw_header

..
    The options are listed in alphabetical order, with aliases included on
    the same line. When the option takes an argument, the ``dest`` name is
    included as an argument name in the help output. The help text is
    printed in the right column.

.. Doug's reply
    Defining an option like this:
    parse.add_option('--with', dest='argument_name', action='store')
    and running the program like:
    myscript.py --with=value
    stores the string "value" in an attribute "argument_name" on the options object you get back from parsing the command line.
    So the "dest name" is the name of the destination for the option's value.

オプションは同行にエイリアスも追加してアルファベット順に表示されます。そのオプションが引数を取るとき ``dest`` にセットした名前はヘルプ出力において引数の名前になります。ヘルプのテキストは右側のカラムに表示されます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'optparse_help.py --help'))
.. }}}
.. {{{end}}}

..
    The name ``WITH`` printed with the option ``--with`` comes from the
    destination variable for the option.  For cases where the internal
    variable name is descriptive enough to serve in the documentation, the
    *metavar* argument can be used to set a different name.

そのオプションが対象とする変数として ``WITH`` という名前が ``--with`` オプションと一緒に表示されます。プログラム内の変数名がそのドキュメントを提供するのに適切な場合は違う名前をセットするために *metavar* 引数を使用します。

.. include:: optparse_metavar.py
   :literal:
   :start-after: #end_pymotw_header

..
    The value is printed exactly as it is given, without any changes to
    capitalization or punctuation.

大文字もしくは句読点への変更を行わず、その値が与えられたものとして正確に表示されます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'optparse_metavar.py -h'))
.. }}}
.. {{{end}}}

..
    Organizing Options
    ------------------

オプションを構成する
--------------------

..
    Many applications include sets of related options.  For example,
    :command:`rpm` includes separate options for each of its operating
    modes.  :mod:`optparse` uses *option groups* to organize options in
    the help output.  The option values are all still saved in a single
    :class:`Values` instance, so the namespace for option names is still
    flat.

多くのアプリケーションは関連するオプションセットを含みます。例えば :command:`rpm` コマンドはそれぞれの操作モードに応じた独立したオプションを含みます。 :mod:`optparse` はヘルプ出力のオプションを構成するために *option groups* を使用します。それでも全てのオプションの値は1つの :class:`Values` インスタンスに保存されます。そのため、オプション名の名前空間もフラットな状態です。

.. include:: optparse_groups.py
   :literal:
   :start-after: #end_pymotw_header

..
    Each group has its own section title and description, and the options
    are displayed together.

それぞれのグループはタイトルと説明の独自セクションを持ちます。また、そのオプションは一緒に表示されます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'optparse_groups.py -h'))
.. }}}
.. {{{end}}}

..
    Application Settings
    --------------------

アプリケーション設定
--------------------

..
    The automatic help generation facilities support configuration
    settings to control several aspects of the help output.  The program's
    *usage* string, which shows how the positional arguments are expected,
    can be set when the :class:`OptionParser` is created.

自動的なヘルプ生成機能は複数のヘルプ出力の外観を扱うための設定をサポートしています。プログラムの *usage* 文字列は、 :class:`OptionParser` が作成されたときに引数の位置がどうであるかを表示します。

.. include:: optparse_usage.py
   :literal:
   :start-after: #end_pymotw_header

..
    The literal value ``%prog`` is expanded to the name of the program at
    runtime, so it can reflect the full path to the script.  If the script
    is run by :command:`python`, instead of running directly, the script
    name is used.

``%prog`` というリテラルは実行時にプログラムの名前に展開されます。そのため、スクリプトに対するフルパスが反映されます。 :command:`python` コマンドでそのスクリプトを実行する場合、直接的に実行されずにそのスクリプト名が使用されます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'optparse_usage.py -h'))
.. }}}
.. {{{end}}}

..
    The program name can be changed using the *prog* argument.

プログラム名は *prog* 引数を使用して変更することができます。

.. include:: optparse_prog.py
   :literal:
   :start-after: #end_pymotw_header

..
    It is generally a bad idea to hard-code the program name in this way,
    though, because if the program is renamed the help will not reflect
    the change.

この方法のようにプログラム名をハードコーディングすることは一般的には悪い考えです。とは言うものの、もしプログラムがリネームされるなら、そのヘルプはその名前変更に影響を受けません。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'optparse_prog.py -h'))
.. }}}
.. {{{end}}}

..
    The application version can be set using the *version* argument.  When
    a value is provided, :mod:`optparse` automatically adds a
    ``--version`` option to the parser.

アプリケーションのバージョンは *version* 引数を使用して設定します。バージョンが指定されたときに :mod:`optparse` は自動的にパーサへ ``--version`` オプションを追加します。

.. include:: optparse_version.py
   :literal:
   :start-after: #end_pymotw_header

..
    When the user runs the program with the ``--version`` option,
    :mod:`optparse` prints the version string and then exits.

ユーザが ``--version`` オプションでそのプログラムを実行するとき :mod:`optparse` はバージョン文字列を表示して終了します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'optparse_version.py -h'))
.. cog.out(run_script(cog.inFile, 'optparse_version.py --version', include_prefix=False))
.. }}}
.. {{{end}}}

.. seealso::

    `optparse <http://docs.python.org/lib/module-optparse.html>`_
        .. Standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント

    :mod:`getopt`
        .. The getopt module, replaced by optparse.

        optparse により置き換えられる getopt モジュール

    :mod:`argparse`
        .. Newer replacement for optparse.

        optparse に置き換わる新たなモジュール
