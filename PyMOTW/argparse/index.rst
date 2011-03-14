..
    =====================================================
    argparse -- Command line option and argument parsing.
    =====================================================

================================================
argparse -- コマンドラインオプションと引数の解析
================================================

..
    :synopsis: Command line option and argument parsing.

.. module:: argparse
    :synopsis: コマンドラインオプションと引数の解析

..
    :Purpose: Command line option and argument parsing.
    :Python Version: 2.7 and later

:目的: コマンドラインオプションと引数の解析
:Python バージョン: 2.7 以上

..
    The :mod:`argparse` module was added to Python 2.7 as a replacement
    for :mod:`optparse`.  The implementation of :mod:`argparse` supports
    features that would not have been easy to add to :mod:`optparse`, and
    that would have required backwards-incompatible API changes, so a new
    module was brought into the library instead.  :mod:`optparse` is still
    supported, but is not likely to receive new features.

:mod:`argparse` モジュールは :mod:`optparse` に置き換わるものとして Python 2.7 で追加されました。 :mod:`argparse` の実装は :mod:`optparse` へ簡単に追加されない機能を提供しますが、後方互換性のない API の変更を必要とします。そのために :mod:`optparse` に置き換わる新たなライブラリとして設けられました。 :mod:`optparse` もそのままサポートされますが、新しい機能が実装されることはないと思われます。

..
    Comparing with optparse
    =======================

optparse と比較する
===================

..
    The API for :mod:`argparse` is similar to the one provided by
    :mod:`optparse`, and in many cases :mod:`argparse` can be used as a
    straightforward replacement by updating the names of the classes and
    methods used.  There are a few places where direct compatibility could
    not be preserved as new features were added, however.

:mod:`argparse` の API は :mod:`optparse` が提供するものとよく似ています。そして、多くのケースでは :mod:`argparse` はクラス名やメソッドを変更すると、そのまま置き換えて使用できます。そうとは言え、そのままでは使用できない互換性のない新機能も少しだけあります。

..
    You will have to decide whether to upgrade existing programs on a
    case-by-case basis.  If you have written extra code to work around
    limitations of :mod:`optparse`, you may want to upgrade to reduce the
    amount of code you need to maintain.  New programs should probably use
    argparse, if it is available on all deployment platforms.

既存のプログラムをアップグレードするかどうかは、基本的にケースバイケースで決めます。 :mod:`optparse` では機能不足のためにワークアラウンドとしてのコードを書くぐらいなら、自分でメンテナンスするコード量を減らすために :mod:`argparse` へアップグレードした方が良いです。デプロイ対象の全てのプラットフォームで動作する場合、新しいプログラムには :mod:`argparse` を使った方が良いです。

..
    Setting up a Parser
    ===================

パーサを設定する
================

..
    The first step when using :mod:`argparse` is to create a parser object
    and tell it what arguments to expect.  The parser can then be used to
    process the command line arguments when your program runs.

:mod:`argparse` を使用するときに最初にすることは、パーサオブジェクトを作成して指定される引数をそのパーサオブジェクトへ伝えます。パーサオブジェクトはプログラムの実行時にコマンドライン引数を処理するために使用されます。

..
    The parser class is :class:`ArgumentParser`.  The constructor takes
    several arguments to set up the description used in the help text for
    the program and other global behaviors or settings.

パーサクラスは :class:`ArgumentParser` です。そのコンストラクタは、プログラムのヘルプ内容を作成したり、グローバルな動作や設定を行う複数の引数を取ります。

::

    import argparse
    parser = argparse.ArgumentParser(description='This is a PyMOTW sample program')


..
    Defining Arguments
    ==================

引数を定義する
==============

..
    :mod:`argparse` is a complete argument *processing* library. Arguments
    can trigger different actions, specified by the *action* argument to
    :func:`add_argument()`. Supported actions include storing the argument
    (singly, or as part of a list), storing a constant value when the
    argument is encountered (including special handling for true/false
    values for boolean switches), counting the number of times an argument
    is seen, and calling a callback.

:mod:`argparse` は完全な引数 *処理* ライブラリです。引数は :func:`add_argument()` への *action* 引数で指定されて様々なアクションのトリガーになります。サポートされるアクションは、(符号付き、またはリストの一部として)引数を格納する、引数が指定されたときに定数を格納する(true/false といったブーリアンに特化した操作を含む)、引数が指定された回数を数える、コールバック関数を呼び出す等があります。

..
    The default action is to store the argument value. In this case, if a
    type is provided, the value is converted to that type before it is
    stored. If the *dest* argument is provided, the value is saved to an
    attribute of that name on the Namespace object returned when the
    command line arguments are parsed.

デフォルトのアクションは引数の値を格納します。このケースでは、ある型を指定すると、その値は指定された型で変換してから格納されます。 *dest* 引数が指定された場合、コマンドライン引数が解析されるときに返す Namespace オブジェクトの属性名としてその値が保存されます。

..
    Parsing a Command Line
    ======================

コマンドラインを解析する
========================

..
    Once all of the arguments are defined, you can parse the command line
    by passing a sequence of argument strings to :func:`parse_args()`. By
    default, the arguments are taken from ``sys.argv[1:]``, but you can
    also pass your own list. The options are processed using the GNU/POSIX
    syntax, so option and argument values can be mixed in the sequence.

全ての引数を定義したら :func:`parse_args()` へ引数文字列のシーケンスを渡すことでコマンドラインを解析します。デフォルトでは、引数は ``sys.argv[1:]`` から取得しますが、独自のリストを渡すこともできます。オプションは GNU/POSIX 構文で処理されるので、オプションと引数の値はシーケンスに混在できます。

..
    The return value from :func:`parse_args()` is a :class:`Namespace`
    containing the arguments to the command. The object holds the argument
    values as attributes, so if your argument ``dest`` is ``"myoption"``,
    you access the value as ``args.myoption``.

:func:`parse_args()` からの返り値はコマンドへの引数を含む :class:`Namespace` オブジェクトです。 :class:`Namespace` オブジェクトは引数の値を属性として保持します。つまり ``dest`` が ``"myoption"`` の場合 ``args.myoption`` でその引数の値にアクセスできます。

..
    Simple Examples
    ===============

簡単なサンプル
==============

..
    Here is a simple example with 3 different options: a boolean option
    (``-a``), a simple string option (``-b``), and an integer option
    (``-c``).

ここに3つの異なるオプションを持つサンプルがあります。1つ目はブーリアンオプション(``-a``)、2つ目は文字列オプション(``-b``)、最後は整数オプション(``-c``)です。

.. include:: argparse_short.py
    :literal:
    :start-after: #end_pymotw_header

..
    There are a few ways to pass values to single character options. The
    example above uses two different forms, ``-bval`` and ``-c val``.

一文字オプションへ値を渡す方法は複数あります。このサンプルでは ``-bval`` と ``-c val`` の2つの形態で渡しています。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'argparse_short.py'))
.. }}}
.. {{{end}}}

..
    The type of the value associated with ``'c'`` in the output is an
    integer, since the :class:`ArgumentParser` was told to convert the
    argument before storing it.

出力結果の ``'c'`` に関連付けられた値の型は整数です。その値は :class:`ArgumentParser` が変換してから格納するからです。

..
    "Long" option names, with more than a single character in their name,
    are handled in the same way.

一文字オプションよりも "長い" オプション名も同様に処理されます。

.. include:: argparse_long.py
    :literal:
    :start-after: #end_pymotw_header

..
    And the results are similar:

その出力結果もよく似ています。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'argparse_long.py'))
.. }}}
.. {{{end}}}

..
    One area in which :mod:`argparse` differs from :mod:`optparse` is the
    treatment of non-optional argument values.  While :mod:`optparse`
    sticks to option parsing, :mod:`argparse` is a full command-line
    argument parser tool, and handles non-optional arguments as well.

:mod:`argparse` と :mod:`optparse` の違いの1つは、任意選択ではないオプションの扱いです。 :mod:`optparse` の場合、オプションを解析するために固定しますが、 :mod:`argparse` は完全なコマンドライン解析ツールなので、任意選択ではないオプションの引数をうまく扱います。

.. include:: argparse_arguments.py
   :literal:
   :start-after: #end_pymotw_header

..
    In this example, the "count" argument is an integer and the "units"
    argument is saved as a string.  If either is not provided on the
    command line, or the value given cannot be converted to the right
    type, an error is reported.

このサンプルでは、"count" 引数は整数で "units" 引数は文字列として保存されます。コマンドライン上でどちらも指定されないか、その値が適切な型に変換できない場合にエラーが発生します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'argparse_arguments.py 3 inches'))
.. cog.out(run_script(cog.inFile, 'argparse_arguments.py some inches', ignore_error=True, include_prefix=False))
.. cog.out(run_script(cog.inFile, 'argparse_arguments.py', ignore_error=True, include_prefix=False))
.. }}}
.. {{{end}}}

..
    Argument Actions
    ----------------

引数のアクション
----------------

..
    There are six built-in actions that can be triggered when an argument
    is encountered:

引数が指定されたときにトリガーとなる6つの組み込みアクションがあります。

..
    ``store``
      Save the value, after optionally converting it to a different type.
      This is the default action taken if none is specified expliclity.

``store``
  値を保存する、オプションで型が指定されたときは違う型へ変換する。これは明示的に指定されなかったときのデフォルトアクションです。

..
    ``store_const``
      Save a value defined as part of the argument specification, rather
      than a value that comes from the arguments being parsed.  This is
      typically used to implement command line flags that aren't booleans.

``store_const``
  引数の解析結果からの値というよりも引数の仕様の一部として定義された値を保存する。これは通常ブーリアンではないコマンドラインのフラグの実装に使用される。

..
    ``store_true`` / ``store_false``
      Save the appropriate boolean value.  These actions are used to
      implement boolean switches.

``store_true`` / ``store_false``
  適切なブーリアン値を保存する。これらのアクションはブーリアンスイッチの実装に使用される。

..
    ``append``
      Save the value to a list.  Multiple values are saved if the argument
      is repeated.

``append``
  リストへ値を保存する。引数が繰り返されるときに複数の値が保存される。

..
    ``append_const``
      Save a value defined in the argument specification to a list.

``append_const``
  リストへの引数の仕様で定義された値を保存する。

..
    ``version``
      Prints version details about the program and then exits.

``version``
  プログラムに関するバージョンの詳細を表示して終了する。

.. include:: argparse_action.py
   :literal:
   :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'argparse_action.py -h'))
.. cog.out(run_script(cog.inFile, 'argparse_action.py -s value', include_prefix=False))
.. cog.out(run_script(cog.inFile, 'argparse_action.py -c', include_prefix=False))
.. cog.out(run_script(cog.inFile, 'argparse_action.py -t', include_prefix=False))
.. cog.out(run_script(cog.inFile, 'argparse_action.py -f', include_prefix=False))
.. cog.out(run_script(cog.inFile, 'argparse_action.py -a one -a two -a three', include_prefix=False))
.. cog.out(run_script(cog.inFile, 'argparse_action.py -B -A', include_prefix=False))
.. cog.out(run_script(cog.inFile, 'argparse_action.py --version', include_prefix=False))
.. }}}
.. {{{end}}}


..
    Option Prefixes
    ---------------

オプションの接頭辞
------------------

..
    The default syntax for options is based on the Unix convention of
    signifying command line switches using a prefix of "-".
    :mod:`argparse` supports other prefixes, so you can make your program
    conform to the local platform default (i.e., use "/" on Windows)
    or follow a different convention.

オプションのデフォルト構文は、"-" の接頭辞でコマンドラインスイッチを表す Unix の慣習に基づいています。 :mod:`argparse` はその他の接頭辞をサポートするので、プラットフォーム独自のデフォルトに準拠させる(例えば Windows では "/" を使う)といった異なる慣習をサポートできます。

.. include:: argparse_prefix_chars.py
   :literal:
   :start-after: #end_pymotw_header

..
    Set the *prefix_chars* parameter for the :class:`ArgumentParser` to a
    string containing all of the characters that should be allowed to
    signify options.  It is important to understand that although
    *prefix_chars* establishes the allowed switch characters, the
    individual argument definitions specify the syntax for a given switch.
    This gives you explicit control over whether options using different
    prefixes are aliases (such as might be the case for
    platform-independent command line syntax) or alternatives (e.g., using
    "``+``" to indicate turning a switch on and "``-``" to turn it off).
    In the example above, ``+a`` and ``-a`` are separate arguments, and
    ``//noarg`` can also be given as ``++noarg``, but not ``--noarg``.

:class:`ArgumentParser` の *prefix_chars* パラメータにオプションを表す文字を全て含む文字列をセットしてください。 *prefix_chars* はコマンドラインスイッチの文字を許容しますが、個別の引数定義はそのスイッチ文字の構文を指定することを理解することが重要です。これにより、明示的に違う接頭辞で使用するオプションがエイリアスなのか(プラットフォーム独自のコマンドライン構文のようなもの)、他の代替処理なのか(例えば "``+``" はフラグをオンにして "``-``" はオフにする)を管理します。上述したこのサンプルでは、 ``+a`` と ``-a`` は独立した別の引数であり、 ``//noarg`` と ``++noarg`` は同じ引数ですが ``--noarg`` は違います。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'argparse_prefix_chars.py -h'))
.. cog.out(run_script(cog.inFile, 'argparse_prefix_chars.py +a', include_prefix=False))
.. cog.out(run_script(cog.inFile, 'argparse_prefix_chars.py -a', include_prefix=False))
.. cog.out(run_script(cog.inFile, 'argparse_prefix_chars.py //noarg', include_prefix=False))
.. cog.out(run_script(cog.inFile, 'argparse_prefix_chars.py ++noarg', include_prefix=False))
.. cog.out(run_script(cog.inFile, 'argparse_prefix_chars.py --noarg', ignore_error=True, include_prefix=False))
.. }}}
.. {{{end}}}


..
    Sources of Arguments
    --------------------

引数のソース
------------

..
    In the examples so far, the list of arguments given to the parser have
    come from a list passed in explicitly, or were taken implicitly from
    :ref:`sys.argv <sys-argv>`.  Passing the list explicitly is useful
    when you are using :mod:`argparse` to process command line-like
    instructions that do not come from the command line (such as in a
    configuration file).

これまでのサンプルでは、パーサへ渡される引数のリストは明示的に渡したリストか、 :ref:`sys.argv <sys-argv>` から暗黙的に受け取ります。パーサへ渡すリストを明示的に渡すことは :mod:`argparse` で(設定ファイルのような)コマンドラインではない、よく似た命令を処理するのに便利です。

.. include:: argparse_with_shlex.py
   :literal:
   :start-after: #end_pymotw_header

..
    :mod:`shlex` makes it easy to split the string stored in the
    configuration file.

:mod:`shlex` モジュールは設定ファイルから読み込んだ文字列を簡単に分割します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'argparse_with_shlex.py'))
.. }}}
.. {{{end}}}

..
    An alternative to processing the configuration file yourself is to
    tell :mod:`argparse` how to recognize an argument that specifies an
    input file containing a set of arguments to be processed using
    *fromfile_prefix_chars*.

設定ファイルを処理する代替方法として *fromfile_prefix_chars* で処理対象の引数セットを含む入力ファイルを指定する引数の認識方法を :mod:`argparse` へ伝えます。

.. include:: argparse_fromfile_prefix_chars.py
   :literal:
   :start-after: #end_pymotw_header

..
    This example stops when it finds an argument prefixed with ``@``, then
    reads the named file to find more arguments.  For example, an input
    file ``argparse_fromfile_prefix_chars.txt`` contains a series of
    arguments, one per line:

このサンプルは ``@`` の接頭辞を持つ引数を見つけると停止して、その名前のファイルを読み込んで引数を探します。例えば ``argparse_fromfile_prefix_chars.txt`` という入力ファイルは、1行につき1引数の引数セットを持ちます。

.. include:: argparse_fromfile_prefix_chars.txt
   :literal:

..
    The output produced when processing the file is:

この入力ファイルを処理した出力結果です。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'argparse_fromfile_prefix_chars.py'))
.. }}}
.. {{{end}}}

..
    Automatically Generated Options
    ===============================

自動生成されるオプション
========================

..
    :mod:`argparse` will automatically add options to generate help and
    show the version information for your application, if configured to do
    so.

:mod:`argparse` は、設定済みの場合、自動的にヘルプを生成するオプションを追加してアプリケーションのバージョン情報を表示します。

..
    The *add_help* argument to :class:`ArgumentParser` controls the
    help-related options.

:class:`ArgumentParser` の *add_help* 引数はヘルプ関連のオプションを管理します。

.. include:: argparse_with_help.py
   :literal:
   :start-after: #end_pymotw_header

..
    The help options (``-h`` and ``--help``) are added by default, but can
    be disabled by setting *add_help* to false.

ヘルプオプション (``-h`` や ``--help``) はデフォルトで追加されますが、 *add_help* に false をセットすることで非表示にできます。

.. include:: argparse_without_help.py
   :literal:
   :start-after: #end_pymotw_header

..
    Although ``-h`` and ``--help`` are defacto standard option names for
    requesting help, some applications or uses of :mod:`argparse` either
    don't need to provide help or need to use those option names for other
    purposes.

``-h`` や ``--help`` はヘルプを見たいときのデファクトスタンダードなオプション名ですが、アプリケーションや :mod:`argparse` の用途によっては、ヘルプを提供する必要がないときや他の目的でそのオプション名を使用したいときがあります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'argparse_with_help.py -h'))
.. cog.out(run_script(cog.inFile, 'argparse_without_help.py -h', ignore_error=True, include_prefix=False))
.. }}}
.. {{{end}}}

..
    The version options (``-v`` and ``--version``) are added when
    *version* is set in the :class:`ArgumentParser` constructor.

バージョンオプション (``-v`` や ``--version``) は :class:`ArgumentParser` のコンストラクタに *version* がセットされるときに追加されます。

.. include:: argparse_with_version.py
   :literal:
   :start-after: #end_pymotw_header

..
    Both forms of the option print the program's version string, then
    cause it to exit immediately.

どちらのオプションを使用してもプログラムのバージョン文字列を表示してから終了します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'argparse_with_version.py -h'))
.. cog.out(run_script(cog.inFile, 'argparse_with_version.py -v', include_prefix=False))
.. cog.out(run_script(cog.inFile, 'argparse_with_version.py --version', include_prefix=False))
.. }}}
.. {{{end}}}

..
    Parser Organization
    ===================

パーサ構築
==========

..
    :mod:`argparse` includes several features for organizing your argument
    parsers, to make implementation easier or to improve the usability of
    the help output.

:mod:`argparse` は、ヘルプの内容をもっと分かり易くしたり、引数パーサを簡単に実装する機能をいくつか提供します。

..
    Sharing Parser Rules
    --------------------

パーサルールを共有する
----------------------

..
    It is common to need to implement a suite of command line programs
    that all take a set of arguments, and then specialize in some way.
    For example, if the programs all need to authenticate the user before
    taking any real action, they would all need to support ``--user`` and
    ``--password`` options.  Rather than add the options explicitly to
    every :class:`ArgumentParser`, you can define a "parent" parser with
    the shared options, and then have the parsers for the individual
    programs inherit from its options.

全ての引数セットを受け取るコマンドラインプログラムを実装する必要があるのは同じです。その後で様々な方法で定義します。例えば、任意の実アクションを行う前にユーザを認証する必要があるなら、そのプログラムは ``--user`` と ``--password`` オプションをサポートする必要があります。全ての :class:`ArgumentParser` クラスへ明示的にそういったオプションを追加するよりも、共有オプションとして "親" パーサを定義します。そうして、その親パーサから継承された個別のプログラムが引数を解析します。

..
    The first step is to set up the parser with the shared argument
    definitions.  Since each subsequent user of the parent parser is going
    to try to add the same help options, causing an exception, we turn off
    automatic help generation in the base parser.

まず行うことは共有の引数定義として親パーサを設定することです。親パーサがそれぞれの子パーサで同じヘルプオプションを追加しようとして例外が発生するので、親パーサの自動ヘルプ生成をオフにします。

.. include:: argparse_parent_base.py
   :literal:
   :start-after: #end_pymotw_header

..
    Next, create another parser with *parents* set:

次に *parents* をセットして別のパーサを作成してください。

.. include:: argparse_uses_parent.py
   :literal:
   :start-after: #end_pymotw_header

..
    And the resulting program takes all three options:

結果としてこのプログラムは3つのオプションがあります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'argparse_uses_parent.py -h'))
.. }}}
.. {{{end}}}


..
    Conflicting Options
    -------------------

オプションの競合
----------------

..
    The previous example pointed out that adding two argument handlers to
    a parser using the same argument name causes an exception.  Change the
    conflict resolution behavior by passing a *conflict_handler*.  The two
    built-in handlers are ``error`` (the default), and ``resolve``, which
    picks a handler based on the order they are added.

前節で紹介したサンプルは、同じ引数の名前でパーサへ2つの引数ハンドラを追加することで例外を発生させると説明しました。 *conflict_handler* へ渡すことで競合を解決するように変更してください。2つの組み込みハンドラ ``error`` (デフォルト) と ``resolve`` があり、追加される順番に基づいてハンドラを選択します。

.. include:: argparse_conflict_handler_resolve.py
   :literal:
   :start-after: #end_pymotw_header

..
    Since the last handler with a given argument name is used, in this
    example the stand-alone option ``-b`` is masked by the alias for
    ``--long-b``.

指定した引数名は最後に追加されたハンドラで使用されるので、このサンプルの独自オプション ``-b`` は ``--long-b`` のエイリアスとして扱われます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'argparse_conflict_handler_resolve.py'))
.. }}}
.. {{{end}}}

..
    Switching the order of the calls to :func:`add_argument` unmasks the
    stand-alone option:

:func:`add_argument` を呼び出す順番を変更することで独立したオプションとして扱います。

.. include:: argparse_conflict_handler_resolve2.py
   :literal:
   :start-after: #end_pymotw_header

..
    Now both options can be used together.

これで両方のオプションを一緒に使用できます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'argparse_conflict_handler_resolve2.py'))
.. }}}
.. {{{end}}}

..
    Argument Groups
    ---------------

引数グループ
------------

..
    :mod:`argparse` combines the argument definitions into "groups."  By
    default, it uses two groups, with one for options and another for
    required position-based arguments.

:mod:`argparse` は "groups" 内に引数定義を組み合わせます。デフォルトは2つのグループを使用します。1つはオプションのため、もう1つは必須の位置ベースの引数のためです。

.. include:: argparse_default_grouping.py
   :literal:
   :start-after: #end_pymotw_header

..
    The grouping is reflected in the separate "positional arguments" and
    "optional arguments" section of the help output:

このグルーピングは、ヘルプ内容で "positional arguments" と "optional arguments" の独立したセクションに分割されます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'argparse_default_grouping.py -h'))
.. }}}
.. {{{end}}}

..
    You can adjust the grouping to make it more logical in the help, so
    that related options or values are documented together.  The
    shared-option example from earlier could be written using custom
    grouping so that the authentication options are shown together in the
    help.

ヘルプ内容に関連するオプション、もしくは値が一緒に説明されるように論理的に分かり易いグルーピングにできます。前節で紹介した共有オプションのサンプルを、ヘルプの認証オプションの説明が一緒に表示されるようにカスタムグルーピングで書き直してみます。

..
    Create the "authentication" group with :func:`add_argument_group` and
    then add each of the authentication-related options to the group,
    instead of the base parser.

:func:`add_argument_group` で "authentication" グループを作成して、基本パーサではなく、そのグループへ認証関連のオプションを追加してください。

.. include:: argparse_parent_with_group.py
   :literal:
   :start-after: #end_pymotw_header

..
    The program using the group-based parent lists it in the *parents*
    value, just as before.

グループベースの親パーサを使用するこのプログラムは、 *parents* に親パーサを指定して変更前のプログラム同様に表示します。

.. include:: argparse_uses_parent_with_group.py
   :literal:
   :start-after: #end_pymotw_header

..
    The help output now shows the authentication options together.

ヘルプ内容は認証オプションを一緒に表示するようになりました。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'argparse_uses_parent_with_group.py -h'))
.. }}}
.. {{{end}}}

..
    Mutually Exclusive Options
    --------------------------

相互排他オプション
------------------

..
    Defining mutually exclusive options is a special case of the option
    grouping feature, and uses :func:`add_mutually_exclusive_group`
    instead of :func:`add_argument_group`.

相互排他オプションの定義はグルーピング機能の特殊ケースです。 :func:`add_argument_group` ではなく :func:`add_mutually_exclusive_group` を使用してください。

.. include:: argparse_mutually_exclusive.py
   :literal:
   :start-after: #end_pymotw_header

..
    :mod:`argparse` enforces the mutal exclusivity for you, so that only
    one of the options from the group can be given.

:mod:`argparse` は、グループのどれか1つだけが指定されるように相互排他性を強制します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'argparse_mutually_exclusive.py -h'))
.. cog.out(run_script(cog.inFile, 'argparse_mutually_exclusive.py -a', include_prefix=False))
.. cog.out(run_script(cog.inFile, 'argparse_mutually_exclusive.py -b', include_prefix=False))
.. cog.out(run_script(cog.inFile, 'argparse_mutually_exclusive.py -a -b', ignore_error=True, include_prefix=False))
.. }}}
.. {{{end}}}

..
    Nesting Parsers
    ---------------

パーサをネストする
------------------

..
    The parent parser approach described above is one way to share options
    between related commands.  An alternate approach is to combine the
    commands into a single program, and use subparsers to handle each
    portion of the command line.  The result works in the way ``svn``,
    ``hg``, and other programs with multiple command line actions, or
    sub-commands, does.

前節で説明した親パーサの方法は関連コマンド間でオプションを共有する1つの方法です。代替の方法として、1つのプログラム内にコマンドを組み合わせて、コマンドラインの各部分を扱うサブパーサを使用する方法があります。その結果は、複数のコマンドラインアクション、もしくはサブコマンドが行う ``svn`` や ``hg`` コマンドのように動作します。

..
    A program to work with directories on the filesystem might define
    commands for creating, deleting, and listing the contents of a
    directory like this:

ファイルシステム上のディレクトリを扱うプログラムは、次のように作成、削除、そしてディレクトリ内のコンテンツを表示するコマンドを定義します。

.. include:: argparse_subparsers.py
   :literal:
   :start-after: #end_pymotw_header

..
    The help output shows the named subparsers as "commands" that can be
    specified on the command line as positional arguments.

ヘルプ内容は、位置引数としてコマンドライン上で指定できる "commands" と名付けられたサブパーサを表示します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'argparse_subparsers.py -h'))
.. }}}
.. {{{end}}}

..
    Each subparser also has its own help, describing the arguments and
    options for that command.

さらに、それぞれのサブパーサはそのコマンドのオプションと引数を説明する独自のヘルプを持ちます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'argparse_subparsers.py create -h'))
.. }}}
.. {{{end}}}

..
    And when the arguments are parsed, the :class:`Namespace` object
    returned by :func:`parse_args` includes only the values related to the
    command specified.

そして、引数が解析されるときに :func:`parse_args` が返す :class:`Namespace` オブジェクトは指定されたそのコマンドのみに関連する値を含みます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'argparse_subparsers.py delete -r foo'))
.. }}}
.. {{{end}}}


..
    Advanced Argument Processing
    ============================

高度な引数処理
==============

..
    The examples so far have shown simple boolean flags, options with
    string or numerical arguments, and positional arguments.
    :mod:`argparse` supports sophisticated argument specification for
    variable-length argument list, enumerations, and constant values as
    well.

これまでのサンプルはシンプルなブーリアンフラグ、文字か数値のオプション、位置引数を紹介しました。 :mod:`argparse` は、可変長の引数リスト、列挙、定数値を便利に洗練された仕様でサポートします。

..
    Variable Argument Lists
    -----------------------

変数の引数リスト
----------------

..
    You can configure a single argument defintion to consume multiple
    arguments on the command line being parsed.  Set *nargs* to one of
    these flag values, based on the number of required or expected
    arguments:

コマンドライン上で複数の引数を解析するのに1つの引数定義で設定できます。必須引数、もしくは期待される引数の数に基づいて次のフラグ値の1つを *nargs* にセットしてください。

..
    =======  =======
    Value    Meaning
    =======  =======
     ``N``    The absolute number of arguments (e.g., ``3``).
     ``?``    0 or 1 arguments
     ``*``    0 or all arguments
     ``+``    All, and at least one, argument
    =======  =======

=======  ==============================
値       説明
=======  ==============================
 ``N``    引数の絶対数 (例 ``3``)
 ``?``    0 か 1 の引数
 ``*``    0 か任意の引数
 ``+``    少なくとも1つ以上の任意の引数
=======  ==============================

.. include:: argparse_nargs.py
   :literal:
   :start-after: #end_pymotw_header

..
    The parser enforces the argument count instructions, and generates an
    accurate syntax diagram as part of the command help text.

このパーサは引数の数を強制して、ヘルプ内容に正確な構文図を生成します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'argparse_nargs.py -h'))
.. cog.out(run_script(cog.inFile, 'argparse_nargs.py', include_prefix=False))
.. cog.out(run_script(cog.inFile, 'argparse_nargs.py --three', include_prefix=False, ignore_error=True))
.. cog.out(run_script(cog.inFile, 'argparse_nargs.py --three a b c', include_prefix=False))
.. cog.out(run_script(cog.inFile, 'argparse_nargs.py --optional', include_prefix=False))
.. cog.out(run_script(cog.inFile, 'argparse_nargs.py --optional with_value', include_prefix=False))
.. cog.out(run_script(cog.inFile, 'argparse_nargs.py --all with multiple values', include_prefix=False))
.. cog.out(run_script(cog.inFile, 'argparse_nargs.py --one-or-more with_value', include_prefix=False))
.. cog.out(run_script(cog.inFile, 'argparse_nargs.py --one-or-more with multiple values', include_prefix=False))
.. cog.out(run_script(cog.inFile, 'argparse_nargs.py --one-or-more', ignore_error=True, include_prefix=False))
.. }}}
.. {{{end}}}

..
    Argument Types
    --------------

引数の型
--------

..
    :mod:`argparse` treats all argument values as strings, unless you tell
    it to convert the string to another type.  The *type* parameter to
    :func:`add_argument` expects a converter function used by the
    :class:`ArgumentParser` to transform the argument value from a string
    to some other type.

:mod:`argparse` は、明示的に文字列を別の型に変換しない限り、文字列として全ての引数の値を扱います。 :func:`add_argument` への *type* パラメータは、文字列から別の型へ引数の値を変換するために :class:`ArgumentParser` が使用する変換関数を指定します。

.. include:: argparse_type.py
   :literal:
   :start-after: #end_pymotw_header

..
    Any callable that takes a single string argument can be passed as
    *type*, including built-in types like :func:`int`, :func:`float`, and
    :func:`file`.

一文字引数を取る任意の呼び出し可能オブジェクトは、 :func:`int`, :func:`float`, :func:`file` といった組み込み型を含めて *type* に渡されます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'argparse_type.py -i 1'))
.. cog.out(run_script(cog.inFile, 'argparse_type.py -f 3.14', include_prefix=False))
.. cog.out(run_script(cog.inFile, 'argparse_type.py --file argparse_type.py', include_prefix=False))
.. }}}
.. {{{end}}}

..
    If the type conversion fails, :mod:`argparse` raises an exception.
    :ref:`TypeError <exceptions-TypeError>` and :ref:`ValueError
    <exceptions-ValueError>` exceptions are trapped automatically and
    converted to a simple error message for the user.  Other exceptions,
    such as the :ref:`IOError <exceptions-IOError>` in the example below
    where the input file does not exist, must be handled by the caller.

型変換が失敗した場合、 :mod:`argparse` は例外を発生させます。 :ref:`TypeError <exceptions-TypeError>` と :ref:`ValueError <exceptions-ValueError>` 例外は、自動的にトラップされてユーザへ簡易エラーメッセージを表示します。次のサンプルの、入力ファイルが存在しないときに発生する :ref:`IOError <exceptions-IOError>` といったその他の例外は呼び出し側で扱わなければなりません。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'argparse_type.py -i a', ignore_error=True))
.. cog.out(run_script(cog.inFile, 'argparse_type.py -f 3.14.15', ignore_error=True, include_prefix=False))
.. cog.out(run_script(cog.inFile, 'argparse_type.py --file does_not_exist.txt', ignore_error=True, include_prefix=False))
.. }}}
.. {{{end}}}

..
    To limit an input argument to a value within a pre-defined set, use
    the *choices* parameter.

あらかじめ定義された値セットに入力する引数を制限するには *choices* パラメータを使用してください。

.. include:: argparse_choices.py
   :literal:
   :start-after: #end_pymotw_header

..
    If the argument to ``--mode`` is not one of the allowed values, an
    error is generated and processing stops.

``--mode`` への引数が定義済みの値ではない場合、エラーが発生して処理を中断します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'argparse_choices.py -h'))
.. cog.out(run_script(cog.inFile, 'argparse_choices.py --mode read-only', include_prefix=False))
.. cog.out(run_script(cog.inFile, 'argparse_choices.py --mode invalid', include_prefix=False, ignore_error=True, break_lines_at=71))
.. }}}
.. {{{end}}}

..
    File Arguments
    --------------

ファイル引数
------------

..
    Although :class:`file` objects can instantiated with a single string
    argument, that does not allow you to specify the access mode.
    :class:`FileType` gives you a more flexible way of specifying that an
    argument should be a file, including the mode and buffer size.

:class:`file` オブジェクトは一文字引数でインスタンス化できますが、アクセスモードの指定ができません。 :class:`FileType` は、引数として渡されるファイルのアクセスモードやバッファサイズを指定するといったもっと柔軟な方法を提供します。

.. include:: argparse_FileType.py
   :literal:
   :start-after: #end_pymotw_header

..
    The value associated with the argument name is the open file handle.
    You are responsible for closing the file yourself when you are done
    with it.

引数名で関連付けられた値はオープンされたファイルハンドラです。そのファイルを使い終えたときに自分でクローズする責任があります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'argparse_FileType.py -h'))
.. cog.out(run_script(cog.inFile, 'argparse_FileType.py -i argparse_FileType.py -o temporary_file.txt', include_prefix=False))
.. cog.out(run_script(cog.inFile, 'argparse_FileType.py -i no_such_file.txt', include_prefix=False, ignore_error=True))
.. }}}
.. {{{end}}}

..
    Custom Actions
    --------------

カスタムアクション
------------------

..
    In addition to the built-in actions described earlier, you can define
    custom actions by providing an object that implements the Action API.
    The object passed to :func:`add_argument` as *action* should take
    parameters describing the argument being defined (all of the same
    arguments given to :func:`add_argument`) and return a callable object
    that takes as parameters the *parser* processing the arguments, the
    *namespace* holding the parse results, the *value* of the argument
    being acted on, and the *option_string* that triggered the action.

前節で説明した組み込みアクションに加えて、アクション API を実装するオブジェクトを提供することでカスタムアクションを定義できます。 *action* として :func:`add_argument` へ渡すオブジェクトは、定義された引数(:func:`add_argument` へ渡される全ての引数と同じ)を表示するパラメータを取ります。そして、引数を処理する *parser* 、解析した結果を保持する *namespace* 、実行後の引数の *value* 、アクションをトリガーする *option_string* をパラメータとして受け取る呼び出し可能オブジェクトを返します。

..
    A class :class:`Action` is provided as a convenient starting point for
    defining new actions.  The constructor handles the argument
    definitions, so you only need to override :func:`__call__` in the
    subclass.

:class:`Action` クラスは新しいアクションを定義するために便利な仕組みを提供します。そのコンストラクタは引数定義を扱います。そのため、サブクラスで :func:`__call__` のみオーバーライドする必要があります。

.. include:: argparse_custom_action.py
   :literal:
   :start-after: #end_pymotw_header

..
    The type of *values* depends on the value of *nargs*.  If the argument
    allows multiple values, *values* will be a list even if it only
    contains one item.

*values* の型は *nargs* の値に依存します。その引数が複数の値を許容する場合、 *values* は1つの要素のみであってもリストになります。

..
    The value of *option_string* also depends on the original argument
    specifiation.  For positional, required, arguments, *option_string* is
    always ``None``.

さらに *option_string* の値もオリジナルの引数仕様に依存します。位置、必須、引数、 *option_string* は常に ``None`` です。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'argparse_custom_action.py'))
.. }}}
.. {{{end}}}




.. more direct comparison with optparse?

.. seealso::

    `argparse <http://docs.python.org/library/argparse.html>`_
        .. The standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント

    `original argparse <http://pypi.python.org/pypi/argparse>`__
        .. The PyPI page for the version of argparse from outside of the
           standard libary.  This version is compatible with older
           versions of Python, and can be installed separately.

        標準ライブラリではない argparse の PyPI ページ、これは古い Python バージョンと互換性があり独立してインストールされる

    :mod:`ConfigParser`
        .. Read and write configuration files.

        設定ファイルを読み書きする
