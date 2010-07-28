..
    =========================================================
    optparse -- Command line option parser to replace getopt.
    =========================================================

=========================================================
optparse -- getopt に代わるコマンドラインオプションパーサ
=========================================================

..
    :synopsis: Command line option parser to replace getopt.

.. module:: optparse
    :synopsis: getopt に代わるコマンドラインオプションパーサ

..
    :Purpose: Command line option parser to replace getopt.
    :Python Version: 2.3

:目的: getopt に代わるコマンドラインオプションパーサ
:Python バージョン: 2.3

..
    The :mod:`optparse` module is a modern alternative for command line
    option parsing that offers several features not available in
    :mod:`getopt`, including type conversion, option callbacks, and
    automatic help generation. There are many more features to optparse
    than can be covered here, but hopefully this introduction will get you
    started if you are writing a command line program soon.

:mod:`optparse` モジュールはコマンドラインオプションを解析するためのモダンな代替方法で、データ型の変換、オプション処理のコールバック、自動ヘルプ生成といった :mod:`getopt` にはない機能を提供します。ここで説明する内容よりも optparse にはもっと多くの機能があります。とはいえ、あなたがコマンドラインオプションを使用するプログラムを今すぐに書こうとしているなら、この入門で十分始められることを期待します。

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
    of options to the :class:`OptionParser` constructor, but that form
    does not seem to be used as frequently.

通常 parser は1度だけ作成されます。そのオプションがコマンドラインで現れたときにどう処理するかに関しての情報と共に、各オプションは parser へ明示的に追加されます。 :class:`OptionParser` コンストラクタへオプションのリストを引数で渡すことも可能ですが、その方法はあまり使用されないと思います。

..
    Defining Options
    ================

オプションを定義する
====================

..
    Options should be added one at a time using the ``add_option()``
    method. Any un-named string arguments at the beginning of the argument
    list are treated as option names. To create aliases for an option, for
    example to have a short and long form of the same option, simply pass
    both names.

オプションは ``add_option()`` メソッドを使用して1度に1つだけ追加すべきです。引数リストの最初にある文字列はオプション名として扱います。あるオプションのエイリアスを作成するために、例えば、同じオプションを表す短いオプション名と長いオプション名を持つには単純に両方のオプション名を引数に渡します。

..
    Unlike :mod:`getopt`, which only parses the options, :func:`optparse`
    is a full option *processing* library. Options can trigger different
    actions, specified by the action argument to
    :func:`add_option()`. Supported actions include storing the argument
    (singly, or as part of a list), storing a constant value when the
    option is encountered (including special handling for true/false
    values for boolean switches), counting the number of times an option
    is seen, and calling a callback.

オプションの解析のみを行う :mod:`getopt` と違い :func:`optparse` は完全なオプション *処理* ライブラリです。オプションは違うアクションのトリガーになることができます。それは :func:`add_option()` への action 引数で指定されます。サポートされているアクションは、その引数を格納する(1つずつか、リストの一部)、定数の引数オプションが指定されたときに定数の値(真偽値を扱うために特化した操作も含む)を格納する、あるオプションが現れた回数をカウントする、そしてコールバック関数を呼び出すがあります。

..
    The default action is to store the argument to the option. In this
    case, if a type is provided, the argument value is converted to that
    type before it is stored. If the *dest* argument is provided, the
    option value is saved to an attribute of that name on the options
    object returned when the command line arguments are parsed.

デフォルトアクションはオプションへの引数を格納します。このケースでは、データ型が指定されたら、その引数の値が格納される前に指定したデータ型へ変換されます。 *dest* 引数が指定された場合、そのオプションの値はコマンドライン引数の解析時に返されるオプションオブジェクトのその名前の属性として保持されます。

..
    Parsing a Command Line
    ======================

コマンドラインを解析する
========================

..
    Once all of the options are defined, the command line is parsed by passing a
    sequence of argument strings to :func:`parse_args()`. By default, the arguments are
    taken from ``sys.argv[1:]``, but you can also pass your own list. The options are
    processed using the GNU/POSIX syntax, so option and argument values can be
    mixed in the sequence.

すべてのオプションが定義されると :func:`parse_args()` へコマンドラインの引数文字列を渡すことで解析されます。デフォルトでは、その引数は ``sys.argv[1:]`` から取得されますが、任意のリストで渡すこともできます。そのオプションは GNU/POSIX 構文を使用して処理され、オプションと引数の値はシーケンスにセットされます。

..
    The return value from :func:`parse_args()` is a two-part tuple
    containing an optparse.Values instance and the list of arguments to
    the command that were not interpreted as options. The Values instance
    holds the option values as attributes, so if your option ``dest`` is
    ``"myoption"``, you access the value as ``options.myoption``.

:func:`parse_args()` は optparse.Values インスタンスと、オプションと解釈されなかったコマンドへの引数リストの2つの値を持つタプルが返されます。その Values インスタンスは属性としてオプションの値を保持します。そのため、あなたのオプション ``dest`` が ``"myoption"`` なら ``options.myoption`` でアクセスします。

..
    Simple Examples
    ===============

簡単なサンプル
==============

..
    Here is a simple example with 3 different options: a boolean option
    (``-a``), a simple string option (``-b``), and an integer option
    (``-c``).

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
    Here is an implementation of the same example program used in the
    chapter about :mod:`getopt`:

:mod:`getopt` の章で使用したのと同じサンプルプログラムの実装があります。

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
    Option Callbacks
    ================

オプションコールバック
======================

..
    Beside saving the arguments for options directly, it is possible to
    define callback functions to be invoked when the option is encountered
    on the command line. Callbacks for options take 4 arguments: the
    :class:`Option` instance causing the callback, the option string from
    the command line, any argument value associated with the option, and
    the optparse.OptionParser instance doing the parsing work.

オプションの引数を直接保持することに加えて、コマンドラインでそのオプションが指定されたときに呼び出されるコールバック関数を定義することもできます。オプションのためのコールバック関数は4つの引数を取ります。それらはコールバックを呼び出す :class:`Option` インスタンス、コマンドラインからのオプションの文字列、そのオプションに渡される引数の値、オプションの解析を行う optparse.OptionParser インスタンスです。

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
    `optparse <http://docs.python.org/lib/module-optparse.html>`_
        Standard library documentation for this module.
    :mod:`getopt`
        The getopt module.

.. seealso::

    `optparse <http://docs.python.org/lib/module-optparse.html>`_
        本モジュールの標準ライブラリドキュメント

    :mod:`getopt`
        getopt モジュール
