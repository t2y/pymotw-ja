..
    ========================================
    bisect -- Maintain lists in sorted order
    ========================================

======================================
bisect -- ソート済みのリストを保持する
======================================

..
    :synopsis: Maintains a list in sorted order without having to call sort each time an item is added to the list.

.. module:: bisect
    :synopsis: リストへ要素が追加されたときにソートせずにリスト内の順序を保持する

..
    :Purpose: Maintains a list in sorted order without having to call sort each time an item is added to the list.
    :Available In: 1.4

:目的: リストへ要素が追加されたときにソートせずにリスト内の順序を保持する
:利用できるバージョン: 1.4

..
    The bisect module implements an algorithm for inserting elements into a list
    while maintaining the list in sorted order. This can be much more efficient
    than repeatedly sorting a list, or explicitly sorting a large list after it is
    constructed.

:mod:`bisect` モジュールは、ソート済みのリストへ挿入する要素のアルゴリズムを実装します。これはリストを繰り返しソートする、もしくは作成後に巨大なリストを明示的にソートするよりもかなり効率が良いです。

..
    Example
    =======

サンプル
========

..
    Let's look at a simple example using bisect.insort(), which inserts items into
    a list in sorted order.

ソート済みのリストへ要素を挿入する :func:`bisect.insort` を使用する簡単なサンプルを見てみましょう。

.. include:: bisect_example.py
    :literal:
    :start-after: #end_pymotw_header

..
    The output for that script is:

このスクリプトの実行結果は次のようになります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'bisect_example.py'))
.. }}}
.. {{{end}}}

..
    The first column shows the new random number. The second column shows the
    position where the number will be inserted into the list. The remainder of
    each line is the current sorted list.

1番目の列は生成された乱数を、2番目の列はリストへ挿入された位置を表示します。行毎にカレントのソート済みリストも表示します。

..
    This is a simple example, and for the amount of data we are manipulating it
    might be faster to simply build the list and then sort it once. But for long
    lists, significant time and memory savings can be achieved using an insertion
    sort algorithm such as this.

これは簡単なサンプルで、いま扱っているデータ量では、単純にリストを作成してソートする方が速いかもしれません。しかし、巨大なリストでは、このような挿入ソートアルゴリズムを使用すると処理時間とメモリが節約できます。

..
    You probably noticed that the result set above includes a few repeated values
    (45 and 77). The bisect module provides 2 ways to handle repeats. New values
    can be inserted to the left of existing values, or to the right. The insort()
    function is actually an alias for insort_right(), which inserts after the
    existing value. The corresponding function insort_left() inserts before the
    existing value.

上述した結果セットは重複する値(45 と 77)を含んでいることに気付きます。 :mod:`bisect` モジュールは重複値を扱うのに2つの方法を提供します。新たな値が既存の値の左側か右側に挿入されます。 :func:`insert` 関数は、実際に既存の値の後に挿入する :func:`insort_right` のエイリアスです。対応する :func:`insort_left` は既存の値の前に挿入します。

..
    If we manipulate the same data using bisect_left() and insort_left(), we end
    up with the same sorted list but notice that the insert positions are
    different for the duplicate values.

:func:`insort_right` と :func:`insort_left` で同じデータを扱う場合、結局は同じソート済みのリストになりますが、重複した値の挿入位置が違っていることに気付きます。

.. include:: bisect_example2.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'bisect_example2.py'))
.. }}}
.. {{{end}}}

..
    In addition to the Python implementation, there is a faster C implementation
    available. If the C version is present, that implementation overrides the pure
    Python implementation automatically when you import the bisect module.

Python 実装に加えて、より高速な C 言語実装も利用できます。C 言語実装が存在するなら :mod:`bisect` をインポートするときにピュア Python 実装がオーバーライドされます。

.. seealso::

    `bisect <http://docs.python.org/library/bisect.html>`_
        .. The standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント

    `WikiPedia: Insertion Sort <http://en.wikipedia.org/wiki/Insertion_sort>`_
        .. A description of the insertion sort algorithm.

        挿入ソートアルゴリズムの説明

    :ref:`article-data-structures`
