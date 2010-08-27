..
    ================================================
    difflib -- Compute differences between sequences
    ================================================

=======================================
difflib -- シーケンス間の差異を算出する
=======================================

..
    :synopsis: Library of tools for computing and working with differences between sequences, especially of lines in text files.

.. module:: difflib
    :synopsis: 特にテキストファイルの行単位での差異を算出するためのライブラリ

..
    :Purpose: Library of tools for computing and working with differences between sequences, especially of lines in text files.
    :Python Version: 2.1

:目的: 特にテキストファイルの行単位での差異を算出するためのライブラリ
:Python バージョン: 2.1

..
    The SequenceMatcher class compares any 2 sequences of values, as long
    as the values are hashable. It uses a recursive algorithm to identify
    the longest contiguous matching blocks from the sequences, eliminating
    "junk" values. The Differ class works on sequences of text lines and
    produces human-readable deltas, including differences within
    individual lines. The HtmlDiff class produces similar results
    formatted as an HTML table.

SequenceMatcher クラスはどのようなシーケンスであっても、その値がハッシュ化できるなら比較することができます。"不要な" 値を取り除きながら、シーケンスから最も長い隣接するマッチングブロックを識別するために再帰アルゴリズムを使用します。Differ クラスはテキスト行に対して動作し、個々のテキスト行単位の差異を含む人間が読み易い差分を生成します。HtmlDiff も HTML Table のようにフォーマットされた他のクラスとよく似た差分を生成します。

..
    Test Data
    =========

テストデータ
============

..
    The examples below will all use this common test data in the
    ``difflib_data.py`` module:

本稿で紹介する全てのサンプルは ``difflib_data.py`` モジュールの共通テストデータを使用します。

.. include:: difflib_data.py
    :literal:
    :start-after: #end_pymotw_header

..
    Differ Example
    ==============

Differ サンプル
===============

..
    Reproducing output similar to the diff command line tool is simple
    with the Differ class:

diff コマンドラインツールによく似た出力を再現させることは Differ クラスで簡単にできます。

.. include:: difflib_differ.py
    :literal:
    :start-after: #end_pymotw_header

..
    The output includes the original input values from both lists,
    including common values, and markup data to indicate what changes were
    made. Lines may be prefixed with ``-`` to indicate that they were in
    the first sequence, but not the second. Lines prefixed with ``+`` were
    in the second sequence, but not the first. If a line has an
    incremental change between versions, an extra line prefixed with ``?``
    is used to indicate where the change occurred within the line. If a
    line has not changed, it is printed with an extra blank space on the
    left column to make it line up with the other lines which may have
    other markup.

その出力は共通の値を含みつつ両方のリストのオリジナル入力値を含みます。そして、どのような変更があるのかを表すためにデータをマークアップします。1番目のシーケンスにはその入力値があったことを表すために行の先頭へ ``-`` が付けられるかもしれませんが、2番目にはありません。2番目のシーケンスには ``+`` が行の先頭へ付けられますが、1番目にはありません。ある行で文字が追加のみ行われたら、その行のどの位置かを表すために追加の行の先頭へ ``?`` が付けられます。もし何も変更がなければ、他のマークアップを持つかもしれない他の行を表示するために行の先頭には余分なスペースが表示されます。

..
    The beginning of both text segments is the same.

両方のテキストシーケンスの1行目は同じです。

::

     1:   Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Integer

..
    The second line has been changed to include a comma in the modified
    text. Both versions of the line are printed, with the extra
    information on line 4 showing the column where the text was modified,
    including the fact that the ``,`` character was added.

2行目はテキストにカンマを入れるように変更しました。両方のバージョンのテキスト行が表示されます。さらに4行目には、そのテキストで実際に ``,`` の文字が追加されたカラム位置を表す追加情報を表示します。

::

     2: - eu lacus accumsan arcu fermentum euismod. Donec pulvinar porttitor
     3: + eu lacus accumsan arcu fermentum euismod. Donec pulvinar, porttitor
     4: ?                                                         +
     5: 

..
    Lines 6-9 of the output shows where an extra space was removed.

その出力の6-9行目は余分なスペースが削除された位置を表示します。

::

     6: - tellus. Aliquam venenatis. Donec facilisis pharetra tortor.  In nec
     7: ?                                                             -
     8: 
     9: + tellus. Aliquam venenatis. Donec facilisis pharetra tortor. In nec

..
    Next a more complex change was made, replacing several words in a phrase.

次はあるフレーズ内の単語を置き換えるといったもっと複雑な変更が行われました。

::

    10: - mauris eget magna consequat convallis. Nam sed sem vitae odio
    11: ?                                              - --
    12: 
    13: + mauris eget magna consequat convallis. Nam cras vitae mi vitae odio
    14: ?                                            +++ +++++   +
    15: 

..
    The last sentence in the paragraph was changed significantly, so the
    difference is represented by simply removing the old version and adding the
    new (lines 20-23).

そして、そのパラグラフの最後の文章はかなり変更されました。そのため、その差分は単純に旧バージョンを削除して新バージョンを追加することで表現されます(20-23行目)。

::

    16:   pellentesque interdum. Sed consequat viverra nisl. Suspendisse arcu
    17:   metus, blandit quis, rhoncus ac, pharetra eget, velit. Mauris
    18:   urna. Morbi nonummy molestie orci. Praesent nisi elit, fringilla ac,
    19:   suscipit non, tristique vel, mauris. Curabitur vel lorem id nisl porta
    20: - adipiscing. Suspendisse eu lectus. In nunc. Duis vulputate tristique
    21: - enim. Donec quis lectus a justo imperdiet tempus.
    22: + adipiscing. Duis vulputate tristique enim. Donec quis lectus a justo
    23: + imperdiet tempus. Suspendisse eu lectus. In nunc.

..
    The ndiff() function produces essentially the same output. The processing is
    specifically tailored to working with text data and eliminating "noise" in the
    input.

ndiff() 関数は基本的に同じ出力を生成します。その処理は特に入力の "ノイズ" を取り除いてテキストデータを扱うことに適しています。

.. include:: difflib_ndiff.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'difflib_ndiff.py'))
.. }}}
.. {{{end}}}

..
    Other Diff Formats
    ==================

他の Diff フォーマット
======================

..
    Where the Differ class shows all of the inputs, a unified diff only includes
    modified lines and a bit of context. In version 2.3, a unified_diff() function
    was added to produce this sort of output:

Differ クラスは全ての入力行を表示しますが、unified 形式の diff は変更された行と前後の数行のみを含みます。バージョン 2.3 では、unified 形式の出力を生成するために unified_diff() 関数が追加されました。

.. include:: difflib_unified.py
    :literal:
    :start-after: #end_pymotw_header

..
    The output should look familiar to users of svn or other version control
    tools:

svn 又は他のバージョン管理ツールのユーザはその出力に見覚えがあるでしょう。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'difflib_unified.py'))
.. }}}
.. {{{end}}}

..
    Using context_diff() produces similar readable output:

context_diff() を使用するとよく似た読み易い出力を生成します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'difflib_context.py'))
.. }}}
.. {{{end}}}

..
    HTML Output
    ===========

HTML 出力
=========

..
    HtmlDiff (new in Python 2.4) produces HTML output with the same information as
    the Diff class. This example uses make_table(), but the make_file() method
    produces a fully-formed HTML file as output.

HtmlDiff (Python 2.4 で追加) は Diff クラスと同じ情報で HTML 出力を生成します。このサンプルは make_table() を使用しますが、make_file() メソッドを使用すると完全な HTML フォーマットのファイルを出力します。

.. include:: difflib_html.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'difflib_html.py'))
.. }}}
.. {{{end}}}

..
    Junk Data
    =========

不要なデータ
============

..
    All of the functions that produce diff sequences accept arguments to
    indicate which lines should be ignored, and which characters within a
    line should be ignored. This can be used to ignore markup or
    whitespace changes in two versions of file, for example.

diff シーケンスを生成する全ての関数は無視すべき行と行内の文字を表す引数を受け取ります。ファイルの2つのバージョン間でマークアップ、又はスペースの変更を無視するために使用されます。

.. include:: difflib_junk.py
    :literal:
    :start-after: #end_pymotw_header

..
    The default for Differ is to not ignore any
    lines or characters explicitly, but to rely on the SequenceMatcher's ability
    to detect noise. The default for ndiff is to ignore space and tab characters.

Differ のデフォルトはどのような行や印字可能文字も無視しませんが、ノイズを検出するために SequenceMatcher の機能に依存します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'difflib_junk.py'))
.. }}}
.. {{{end}}}

SequenceMatcher
===============

..
    SequenceMatcher, which implements the comparison algorithm, can be used with
    sequences of any type of object as long as the object is hashable. For
    example, two lists of integers can be compared, and using get_opcodes() a set
    of instructions for converting the original list into the newer can be
    printed:

比較アルゴリズムを実装する SequenceMatcher は、オブジェクトがハッシュ化できる限り、どのようなオブジェクト型のシーケンスでも使用できます。例えば、2つの整数値リストを比較することができます。そして、get_opcodes() を使用して、 オリジナルのリストを新たなリストへ変換する命令セットを表示します。

.. include:: difflib_seq.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'difflib_seq.py'))
.. }}}
.. {{{end}}}

..
    You can use SequenceMatcher with your own classes, as well as built-in types.

ビルトイン型と同様に独自クラスで SequenceMatcher を使用することもできます。

..
    `difflib <http://docs.python.org/library/difflib.html>`_
        The standard library documentation for this module. 
    `Pattern Matching: The Gestalt Approach <http://www.ddj.com/documents/s=1103/ddj8807c/>`_
        Discussion of a similar algorithm by John W. Ratcliff and D. E. Metzener published in Dr. Dobb's Journal in July, 1988.
    :ref:`article-text-processing`

.. seealso::

    `difflib <http://docs.python.org/library/difflib.html>`_
        本モジュールの標準ライブラリドキュメント
 
    `パターンマッチング: Gestalt アプローチ <http://www.ddj.com/documents/s=1103/ddj8807c/>`_
        1998年7月 Dr. Dobb のジャーナルに John W. Ratcliff と D. E. Metzener による似たようなアルゴリズムの議論が発表されました。

    :ref:`article-text-processing`
