..
    ==================================================
    shlex -- Lexical analysis of shell-style syntaxes.
    ==================================================

=================================
shlex -- シェルスタイルの字句解析
=================================

..
    :synopsis: Lexical analysis of shell-style syntaxes.

.. module:: shlex
    :synopsis: シェルスタイルの字句解析

..
    :Purpose: Lexical analysis of shell-style syntaxes.
    :Available In: 1.5.2, with additions in later versions

:目的: シェルスタイルの字句解析
:利用できるバージョン: 1.5.2, その後のバージョンで機能追加

..
    The shlex module implements a class for parsing simple shell-like syntaxes. It
    can be used for writing your own domain specific language, or for parsing
    quoted strings (a task that is more complex than it seems, at first).

:mod:`shlex` モジュールはシェルによく似たシンプルな構文で字句解析するクラスを実装します。それは独自のドメイン特化言語(DSL)を書いたり、引用符で囲まれた文字列(一目見て複雑に見えるタスク)を解析するために使用されます。

..
    Quoted Strings
    ==============

引用符で囲まれた文字列
======================

..
    A common problem when working with input text is to identify a sequence of
    quoted words as a single entity. Splitting the text on quotes does not always
    work as expected, especially if there are nested levels of quotes. Take the
    following text:

入力のテキストを解析するときの共通の課題は、1つの実体として引用符で囲まれたワードのシーケンスを認識することです。引用符でテキストを分割する方法は、いつもうまく行くとは限りません。特に引用符がネストされている場合です。次のテキストを見てください。

.. include:: quotes.txt
    :literal:

..
    A naive approach might attempt to construct a regular expression to
    find the parts of the text outside the quotes to separate them from
    the text inside the quotes, or vice versa. Such an approach would be
    unnecessarily complex and prone to errors resulting from edge cases
    like apostrophes or even typos. A better solution is to use a true
    parser, such as the one provided by the :mod:`shlex` module. Here is a
    simple example that prints the tokens identified in the input file:

すぐに思い付く方法は、引用符の内側のテキストから引用符の外側のテキスト部分を分離するために正規表現を組み立てても良いかもしれません。もしくはその逆の方法もあります。そういった方法は不必要に複雑になり、アポストロフィや誤字のようなエッジケースの場合にエラーを発生しがちです。もっと良い解決方法は、 :mod:`shlex` モジュールが提供するような本物のパーサを使用することです。次に入力ファイルで認識されたトークンを表示する簡単なサンプルを紹介します。

.. include:: shlex_example.py
    :literal:
    :start-after: #end_pymotw_header

..
    When run on data with embedded quotes, the parser produces the list of tokens
    we expect:

組み込みの引用符でそのデータを処理すると、このパーサは期待したトークンのリストを生成します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'shlex_example.py quotes.txt'))
.. }}}
.. {{{end}}}

..
    Isolated quotes such as apostrophes are also handled.  Given this
    input file:

アポストロフィのような独立した引用符も扱えます。次の入力を試してみてください。

.. include:: apostrophe.txt
    :literal:

..
    The token with the embedded apostrophe is no problem:

アポストロフィを持つトークンでも問題ありません。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'shlex_example.py apostrophe.txt'))
.. }}}
.. {{{end}}}

..
    Embedded Comments
    =================

組み込みコメント
================

..
    Since the parser is intended to be used with command languages, it needs to
    handle comments. By default, any text following a # is considered part of a
    comment, and ignored. Due to the nature of the parser, only single character
    comment prefixes are supported. The set of comment characters used can be
    configured through the commenters property.

パーサはコマンド言語で使用されることを意図しているのでコメントを扱う必要があります。デフォルトでは # に続く任意のテキストをコメントと見なして無視します。パーサの特性上、コメントの接頭辞は一文字のみがサポートされます。コメントの文字セットは commenters プロパティで設定されています。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'shlex_example.py comments.txt'))
.. }}}
.. {{{end}}}

Split
=====

..
    If you just need to split an existing string into component tokens,
    the convenience function :func:`split()` is a simple wrapper around
    the parser.

文字列をコメントトークンに分割する必要がある場合、便利な関数 :func:`split()` がパーサ周りでシンプルなラッパーになります。

.. include:: shlex_split.py
    :literal:
    :start-after: #end_pymotw_header

..
    The result is a list:

この実行結果はリストになります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'shlex_split.py'))
.. }}}
.. {{{end}}}


..
    Including Other Sources of Tokens
    =================================

トークンの他のソースを含める
============================

..
    The :class:`shlex` class includes several configuration properties
    which allow us to control its behavior. The *source* property
    enables a feature for code (or configuration) re-use by allowing one
    token stream to include another. This is similar to the Bourne shell
    ``source`` operator, hence the name.

:class:`shlex` クラスには、その動作を制御する複数の設定プロパティがあります。 *source* プロパティはコード(または設定)を再利用するために、1つのトークンストリームへ他のものを含められるようにします。これは Bourne シェルの ``source`` 演算子によく似ているので、その名前が付いています。

.. include:: shlex_source.py
    :literal:
    :start-after: #end_pymotw_header

..
    Notice the string ``source quotes.txt`` embedded in the original
    text. Since the source property of the lexer is set to "source", when
    the keyword is encountered the filename appearing in the next title is
    automatically included. In order to cause the filename to appear as a
    single token, the ``.`` character needs to be added to the list of
    characters that are included in words (otherwise "``quotes.txt``"
    becomes three tokens, "``quotes``", "``.``", "``txt``"). The output
    looks like:

オリジナルのテキスト内に ``source quotes.txt`` という文字列があることに着目してください。レクサの source プロパティが "source" にセットされているので、そのキーワードを見つけたときに次にあるファイル名が自動的に読み込まれます。ファイル名を1つのトークンにするために ``.`` 文字をワードに含まれる文字リストへ追加する必要があります(言い換えると "``quotes.txt``" は "``quotes``", "``.``", "``txt``" の3つのトークンになります)。この出力は次のようになります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'shlex_source.py'))
.. }}}
.. {{{end}}}

..
    The "source" feature uses a method called :func:`sourcehook()` to load
    the additional input source, so you can subclass :class:`shlex` to
    provide your own implementation to load data from anywhere.

"source" 機能は、入力ソースを追加して読み込むために :func:`sourcehook()` というメソッドを使用します。そのため、独自実装で自由にデータを読み込ませるために :class:`shlex` をサブクラス化できます。

..
    Controlling the Parser
    ======================

パーサを管理する
================

..
    I have already given an example changing the *wordchars* value to
    control which characters are included in words. It is also possible to
    set the *quotes* character to use additional or alternative
    quotes. Each quote must be a single character, so it is not possible
    to have different open and close quotes (no parsing on parentheses,
    for example).

ワードに含まれる文字を管理するために *wordchars* を変更するサンプルを前節で紹介しました。さらに *quotes* 文字も追加や代替の引用符に変更することもできます。それぞれの引用符は一文字でなければならないので、始まりと終わりを表す引用符を違う文字にすることはできません(例えば、一対になっていないと解析されません)。

.. include:: shlex_table.py
    :literal:
    :start-after: #end_pymotw_header

..
    In this example, each table cell is wrapped in vertical bars:

このサンプルでは、それぞれの表のセルは縦線(|)で囲まれます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'shlex_table.py'))
.. }}}
.. {{{end}}}

..
    It is also possible to control the whitespace characters used to split words.
    If we modify the example in shlex_example.py to include period and comma, as
    follows:

さらにワードの分割に使用する空白文字を変更することもできます。shlex_example.py のサンプルにピリオドとカンマを含めるように変更するなら次のようにします。

.. include:: shlex_whitespace.py
    :literal:
    :start-after: #end_pymotw_header

..
    The results change to:

実行結果は次のように変わります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'shlex_whitespace.py quotes.txt'))
.. }}}
.. {{{end}}}


..
    Error Handling
    ==============

エラー制御
==========

..
    When the parser encounters the end of its input before all quoted
    strings are closed, it raises :ref:`ValueError
    <exceptions-ValueError>`. When that happens, it is useful to examine
    some of the properties of the parser maintained as it processes the
    input. For example, *infile* refers to the name of the file being
    processed (which might be different from the original file, if one
    file sources another). The *lineno* reports the line when the error is
    discovered. The *lineno* is typically the end of the file, which may
    be far away from the first quote. The *token* attribute contains the
    buffer of text not already included in a valid token. The
    :func:`error_leader()` method produces a message prefix in a style
    similar to Unix compilers, which enables editors such as emacs to
    parse the error and take the user directly to the invalid line.

全ての引用符が閉じられる前にパーサがその入力の終わりに到達するとき :ref:`ValueError <exceptions-ValueError>` が発生します。その入力を処理しようとするときにこの例外が発生するので、パーサのプロパティを調査するのに便利です。例えば、 *infile* は処理されるファイル名を参照します(ファイルソースが別のものである場合はオリジナルのファイルではない可能性があります)。 *lineno* はエラーが発生した行をレポートします。 *lineno* は通常、最初の引用符から離れてファイルの終わりになるかもしれません。 *token* 属性は有効なトークンではないテキストのバッファを含みます。 :func:`error_leader()` メソッドは、Unix コンパイラとよく似たメッセージ形式で接頭辞を生成します。このエラーメッセージは emacs のようなエディタでエラー解析できて無効な行を直接ユーザへ伝えます。

.. include:: shlex_errors.py
    :literal:
    :start-after: #end_pymotw_header

..
    The example above produces this output:

このサンプルは次のエラーになります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'shlex_errors.py', ignore_error=True))
.. }}}
.. {{{end}}}


..
    POSIX vs. Non-POSIX Parsing
    ===========================

POSIX 対 非 POSIX 解析
======================

..
    The default behavior for the parser is to use a backwards-compatible style
    which is not POSIX-compliant. For POSIX behavior, set the posix argument when
    constructing the parser.

パーサのデフォルトの動作は POSIX 準拠ではない後方互換性のあるスタイルを使用します。POSIX に準拠するには、パーサを構築するときに posix 引数に True をセットしてください。

.. include:: shlex_posix.py
    :literal:
    :start-after: #end_pymotw_header

..
    Here are a few examples of the differences in parsing behavior:

解析処理が違うサンプルは次のようになります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'shlex_posix.py'))
.. }}}
.. {{{end}}}


.. seealso::

    `shlex <http://docs.python.org/lib/module-shlex.html>`_
        .. Standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント

    :mod:`cmd`
        .. Tools for building interactive command interpreters.

        インタラクティブコマンドインタープリタのツール

    :mod:`optparse`
        .. Command line option parsing.

        コマンドラインオプション解析

    :mod:`getopt`
        .. Command line option parsing.

        コマンドラインオプション解析
