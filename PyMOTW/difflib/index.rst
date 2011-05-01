..
    ==============================
     difflib -- Compare sequences
    ==============================

===============================
difflib -- シーケンスを比較する
===============================

..
    :synopsis: Compare sequences, especially lines of text.

.. module:: difflib
    :synopsis: 特にテキストファイルの行単位での、シーケンスを比較する

..
    :Purpose: Compare sequences, especially lines of text.
    :Available In: 2.1 and later

:目的: 特にテキストファイルの行単位での、シーケンスを比較する
:利用できるバージョン: 2.1 以上

..
    The :mod:`difflib` module contains tools for computing and working
    with differences between sequences.  It is especially useful for
    comparing text, and includes functions that produce reports using
    several common difference formats.

:mod:`difflib` モジュールはシーケンス間の差異を算出するためのツールを提供します。特にテキストの比較に便利で、複数の共通 diff フォーマットを用いたレポートを生成する機能があります。

..
    The examples below will all use this common test data in the
    ``difflib_data.py`` module:

本稿で紹介する全てのサンプルは ``difflib_data.py`` モジュールの共通テストデータを使用します。

.. include:: difflib_data.py
    :literal:
    :start-after: #end_pymotw_header

..
    Comparing Bodies of Text
    ========================

テキストの内容を比較する
========================

..
    The :class:`Differ` class works on sequences of text lines and
    produces human-readable *deltas*, or change instructions, including
    differences within individual lines.

Differ クラスはテキスト行に対して処理を行い、テキスト行単位の差異を含んだ人間が読み易い *差分* 、または変更命令を生成します。

..
    The default output produced by :class:`Differ` is similar to the
    :command:`diff` command line tool is simple with the :class:`Differ`
    class.  It includes the original input values from both lists,
    including common values, and markup data to indicate what changes were
    made. 

:class:`Differ` が生成するデフォルト出力は :command:`diff` コマンドツールによく似ています。共通の値や何が変更されているかを表すマークアップデータを含みつつ、両方のリストからのオリジナルの入力値も含みます。

..
    * Lines prefixed with ``-`` indicate that they were in the first
      sequence, but not the second.
    * Lines prefixed with ``+`` were in the second sequence, but not the
      first. 
    * If a line has an incremental difference between versions, an extra
      line prefixed with ``?`` is used to highlight the change within the
      new version.
    * If a line has not changed, it is printed with an extra blank space
      on the left column so that it it lines up with the other lines that
      may have differences.

* 1番目のシーケンスにはその入力値があったことを表すために行の先頭へ ``-`` が付けられるかもしれませんが、2番目にはありません。
* 2番目のシーケンスには ``+`` が行の先頭へ付けられますが、1番目にはありません。
* ある行で文字の追加のみ行われたら、その行のどの位置かを表すために追加の行の先頭へ ``?`` が付けられます。
* もし何も変更がなければ、他の行が何かのマークアップを持つ可能性があるので行の先頭には余分なスペースが表示されます。

..
    To compare text, break it up into a sequence of individual lines and
    pass the sequences to :func:`compare`.

テキストを比較するには、行単位でシーケンスを分割して :func:`compare` にそのシーケンスを渡します。

.. include:: difflib_differ.py
    :literal:
    :start-after: #end_pymotw_header

..
    The beginning of both text segments in the sample data is the same, so
    the first line is printed without any extra annotation.

サンプルデータの両方のテキストの1行目は同じなので、最初の行は先頭に何もマークアップされずに表示されます。

::

     1:   Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Integer

..
    The second line of the data has been changed to include a comma in the
    modified text. Both versions of the line are printed, with the extra
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
    The :func:`ndiff` function produces essentially the same output.

ndiff() 関数は基本的に同じ出力を生成します。

.. include:: difflib_ndiff.py
    :literal:
    :start-after: #end_pymotw_header

..
    The processing is specifically tailored for working with text data and
    eliminating "noise" in the input.

その処理は特に入力の "ノイズ" を取り除いてテキストデータを扱うことに適しています。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'difflib_ndiff.py'))
.. }}}
.. {{{end}}}

..
    Other Output Formats
    --------------------

他の出力フォーマット
--------------------

..
    While the :class:`Differ` class shows all of the input lines, a
    *unified diff* only includes modified lines and a bit of context. In
    Python 2.3, the :func:`unified_diff` function was added to produce
    this sort of output:

:class:`Differ` クラスは全ての入力行を表示しますが、 *unified 形式の diff* は変更された行と前後の数行のみを含みます。Python 2.3 では、unified 形式の出力を生成するために :func:`unified_diff` 関数が追加されました。

.. include:: difflib_unified.py
    :literal:
    :start-after: #end_pymotw_header

..
    The output should look familiar to users of subversion or other
    version control tools:

subversion 又は他のバージョン管理ツールのユーザはその出力に見覚えがあるでしょう。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'difflib_unified.py'))
.. }}}
.. {{{end}}}

..
    Using :func:`context_diff` produces similar readable output:

:func:`context_diff` を使用するとよく似た読み易い出力を生成します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'difflib_context.py'))
.. }}}
.. {{{end}}}

..
    HTML Output
    -----------

HTML 出力
---------

..
    :class:`HtmlDiff` produces HTML output with the same information as
    :class:`Diff`. 

:class:`HtmlDiff` は :class:`Diff` と同じような情報を HTML で生成します。

.. include:: difflib_html.py
    :literal:
    :start-after: #end_pymotw_header

..
    This example uses :func:`make_table`, which only returns the
    :const:`table` tag containing the difference information.  The
    :func:`make_file` method produces a fully-formed HTML file as output.

このサンプルは :func:`make_table` を使用して、差異情報を含んだ :const:`table` タグのみを返します。 :func:`make_file` メソッドを使用すると完全な HTML フォーマットのファイルを出力します。

.. note::

  .. The output is not included here because it is very verbose.

  その出力はあまりに冗長なのでここでは紹介しません。

..
    Junk Data
    =========

不要なデータ
============

..
    All of the functions that produce difference sequences accept
    arguments to indicate which lines should be ignored, and which
    characters within a line should be ignored. These parameters can be
    used to skip over markup or whitespace changes in two versions of a
    file, for example.

diff シーケンスを生成する全ての関数は、無視すべき行と行内の文字を表す引数を受け取ります。そういった引数は、ファイルの2つのバージョン間でマークアップかスペースの変更を無視するために使用されます。

.. include:: difflib_junk.py
    :literal:
    :start-after: #end_pymotw_header

..
    The default for :class:`Differ` is to not ignore any lines or
    characters explicitly, but to rely on the ability of
    :class:`SequenceMatcher` to detect noise. The default for
    :func:`ndiff` is to ignore space and tab characters.

:class:`Differ` のデフォルトはどのような行や印字可能文字も無視しませんが、ノイズを検出するために :class:`SequenceMatcher` の機能に依存します。 :func:`ndiff` のデフォルトはスペースやタブ文字を無視します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'difflib_junk.py'))
.. }}}
.. {{{end}}}

..
    Comparing Arbitrary Types
    =========================

任意の型を比較する
==================

..
    The :class:`SequenceMatcher` class compares two sequences of any
    types, as long as the values are hashable. It uses an algorithm to
    identify the longest contiguous matching blocks from the sequences,
    eliminating "junk" values that do not contribute to the real data.

:class:`SequenceMatcher` は、オブジェクトがハッシュ化できる限り、どのようなオブジェクト型のシーケンスでも比較します。それは実際のデータに影響しない "不要な" 値を取り除いて、そのシーケンスからもっとも長いマッチングブロックを識別するアルゴリズムを使用します。

.. include:: difflib_seq.py
    :literal:
    :start-after: #end_pymotw_header

..
    This example compares two lists of integers and uses
    :func:`get_opcodes` to derive the instructions for converting the
    original list into the newer version.  The modifications are applied
    in reverse order so that the list indexes remain accurate after items
    are added and removed.

このサンプルは2つの整数値リストを比較します。そして :func:`get_opcodes` を使用して、 オリジナルのリストを新たなリストへ変換する命令セットを表示します。その変更は、リストの要素が追加・削除された後でインデックスが正確に維持されるように逆の順番で適用されます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'difflib_seq.py'))
.. }}}
.. {{{end}}}

..
    :class:`SequenceMatcher` works with custom classes, as well as
    built-in types, as long as they are hashable.

:class:`SequenceMatcher` は、それらハッシュ化できる限り、ビルトイン型と同様に独自クラスで動作します。

.. seealso::

    `difflib <http://docs.python.org/library/difflib.html>`_
        .. The standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント

    `Pattern Matching: The Gestalt Approach <http://www.ddj.com/documents/s=1103/ddj8807c/>`_
        .. Discussion of a similar algorithm by John W. Ratcliff and D. E. Metzener published in Dr. Dobb’s Journal in July, 1988.

        1998年7月 Dr. Dobb のジャーナルに John W. Ratcliff と D. E. Metzener による似たようなアルゴリズムの議論が発表されました。

    :ref:`article-text-processing`






