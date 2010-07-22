..
    =================================
    glob -- Filename pattern matching
    =================================

======================================
glob -- ファイル名のパターンマッチング
======================================

..
    :synopsis: Use Unix shell rules to fine filenames matching a pattern.

.. module:: glob
    :synopsis: ファイル名のパターンマッチングに適した Unix シェルのルールを使用する

..
    :Purpose: Use Unix shell rules to fine filenames matching a pattern.
    :Python Version: 1.4

:目的: ファイル名のパターンマッチングに適した Unix シェルのルールを使用する
:Python バージョン: 1.4

..
    Even though the glob API is very simple, the module packs a lot of
    power. It is useful in any situation where your program needs to look
    for a list of files on the filesystem with names matching a
    pattern. If you need a list of filenames that all have a certain
    extension, prefix, or any common string in the middle, use :mod:`glob`
    instead of writing code to scan the directory contents yourself.

glob API はとてもシンプルですが、このモジュールは大きなチカラを秘めています。glob はあるパターンにマッチする名前でファイルシステム上のファイルリストを探すプログラムのどんな状況においても役に立ちます。もし特定の拡張子、接尾辞、又は中間に共通の文字列を持った全ファイル名のリストが必要なら、自分でディレクトリのコンテンツを精査するコードを書く代わりに :mod:`glob` を使用してください。

..
    The pattern rules for glob are not regular expressions. Instead, they
    follow standard Unix path expansion rules. There are only a few
    special characters: two different wild-cards, and character ranges are
    supported. The patterns rules are applied to segments of the filename
    (stopping at the path separator, ``/``). Paths in the pattern can be
    relative or absolute. Shell variable names and tilde (``~``) are not
    expanded.

glob のパターンルールは正規表現ではありません。その代わり、標準 Unix パス拡張ルールに準拠します。数個だけ特殊な文字があり、2種類の異なるワイルドカード、文字範囲がサポートされます。そのパターンルールはファイル名の部分に対して適用されます(パス区切り文字 ``/`` で停止します)。そのパターンのパスは絶対パスか相対パスです。シェル変数名やチルダ(``~``)は展開されません。

..
    Example Data
    ============

サンプルデータ
==============

..
    The examples below assume the following test files are present in the
    current working directory:

次のテストファイルがカレントのワークディレクトリに存在すると仮定してください。

.. {{{cog
.. from paver.path import path
.. outdir = path(cog.inFile).dirname() / 'dir'
.. outdir.rmtree()
.. cog.out(run_script(cog.inFile, 'glob_maketestdata.py'))
.. }}}
.. {{{end}}}

..
   Use ``glob_maketestdata.py`` in the sample code to create these
   files if you want to run the examples.

.. note::

   サンプルコードを実行したいなら、これらのファイルを作成するために ``glob_maketestdata.py`` を実行してください。

..
    Wildcards
    =========

ワイルドカード
==============

..
    An asterisk (``*``) matches zero or more characters in a segment of a
    name. For example, ``dir/*``.

アスタリスク(``*``)は名前の一部にあるゼロ個以上の文字にマッチします。例えば ``dir/*`` です。

.. include:: glob_asterisk.py
    :literal:
    :start-after: #end_pymotw_header

..
    The pattern matches every pathname (file or directory) in the directory dir,
    without recursing further into subdirectories.

そのパターンは dir ディレクトリ内の全てのパス名(ファイル又はディレクトリ)にマッチします。そして、サブディレクトリは再帰的にマッチしません。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'glob_asterisk.py'))
.. }}}
.. {{{end}}}

..
    To list files in a subdirectory, you must include the subdirectory in the
    pattern:

サブディレクトリにあるファイルを表示するためには、そのパターンにサブディレクトリを含めなければなりません。

.. include:: glob_subdir.py
    :literal:
    :start-after: #end_pymotw_header

..
    The first case above lists the subdirectory name explicitly, while the second
    case depends on a wildcard to find the directory.

1番目のケースは明確なサブディレクトリの名前で表示します。一方、2番目のケースはそのディレクトリを探すためにワイルドカードに依存します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'glob_subdir.py'))
.. }}}
.. {{{end}}}

..
    The results, in this case, are the same. If there was another subdirectory,
    the wildcard would match both subdirectories and include the filenames from
    both.

このサンプルの結果はどちらも同じです。もし別のサブディレクトリがあったら、ワイルドカードが両方のサブディレクトリにマッチしてそれらのファイルを表示したでしょう。

..
    Single Character Wildcard
    =========================

1文字のワイルドカード
=====================

..
    The other wildcard character supported is the question mark
    (``?``). It matches any single character in that position in the
    name. For example,

サポートされている他のワイルドカード文字としてはてなマーク(``?``)があります。それは名前の指定した位置に存在するどんな1文字にもマッチします。例えば、

.. include:: glob_question.py
    :literal:
    :start-after: #end_pymotw_header

..
    Matches all of the filenames which begin with "file", have one more character
    of any type, then end with ".txt".

"file" で始まって、何か1文字があり、".txt" で終わる全てのファイル名にマッチします。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'glob_question.py'))
.. }}}
.. {{{end}}}

..
    Character Ranges
    ================

文字範囲
========

..
    When you need to match a specific character, use a character range instead of
    a question mark. For example, to find all of the files which have a digit in
    the name before the extension:

特定の文字をマッチさせる必要があるとき、はてなマークの代わりに文字範囲を使用してください。例えば、拡張子の前に数字を持つ名前の全ファイルを見つけるために使用します。

.. include:: glob_charrange.py
    :literal:
    :start-after: #end_pymotw_header

..
    The character range ``[0-9]`` matches any single digit. The range is
    ordered based on the character code for each letter/digit, and the
    dash indicates an unbroken range of sequential characters. The same
    range value could be written ``[0123456789]``.

文字範囲 ``[0-9]`` は1つの数字にマッチします。その範囲はそれぞれの文字/数字のコード表の順番に基づき、そのダッシュ記号は連続した文字の範囲であることを表します。この文字範囲は ``[0123456789]`` と書くこともできます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'glob_charrange.py'))
.. }}}
.. {{{end}}}

..
    `glob <http://docs.python.org/library/glob.html>`_
        The standard library documentation for this module.
    `Pattern Matching Notation <http://www.opengroup.org/onlinepubs/000095399/utilities/xcu_chap02.html#tag_02_13>`_
        An explanation of globbing from The Open Group's Shell Command Language specification.
    :mod:`fnmatch`
        Filename matching implementation.
    :ref:`article-file-access`
        Other tools for working with files.

.. seealso::

    `glob <http://docs.python.org/library/glob.html>`_
        本モジュールの標準ライブラリドキュメント

    `パターンマッチング覚え書き <http://www.opengroup.org/onlinepubs/000095399/utilities/xcu_chap02.html#tag_02_13>`_
        Open Group のシェルコマンド言語仕様の glob の説明

    :mod:`fnmatch`
        ファイル名マッチングの実装

    :ref:`article-file-access`
        ファイルと共に使用するその他のモジュール
