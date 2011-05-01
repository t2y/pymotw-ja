.. _deque:

=======
 Deque
=======

..
    A double-ended queue, or :class:`deque`, supports adding and removing
    elements from either end. The more commonly used stacks and queues are
    degenerate forms of deques, where the inputs and outputs are
    restricted to a single end.

両端キューまたは :class:`deque` は両端から要素の追加や削除をサポートします。一般的に使用されるスタックやキューはその入出力を1つの終端のみに制限するように deque を退化させたものです。

.. include:: collections_deque.py
    :literal:
    :start-after: #end_pymotw_header

..
    Since deques are a type of sequence container, they support some of
    the same operations that lists support, such as examining the contents
    with :func:`__getitem__`, determining length, and removing elements
    from the middle by matching identity.

deque はシーケンス型のコンテナなので、 :func:`__getitem__` でコンテンツを調べる、長さを決定する、識別子でマッチした中間の要素を削除するといったリストがサポートする操作のいくつかをサポートします。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'collections_deque.py'))
.. }}}
.. {{{end}}}

..
    Populating
    ==========

追加
====

..
    A deque can be populated from either end, termed "left" and "right" in the
    Python implementation.

deque は Python 実装では "左側" や "右側" と呼びどちらかの一端から追加されます。

.. include:: collections_deque_populating.py
    :literal:
    :start-after: #end_pymotw_header

..
    Notice that :func:`extendleft` iterates over its input and performs
    the equivalent of an :func:`appendleft` for each item. The end result
    is the :class:`deque` contains the input sequence in reverse order.

:func:`extendleft` は入力シーケンスを処理することと、各要素に :func:`appendleft` を実行することは等価であることに注意してください。最終結果はその入力シーケンスを逆順に含んだ :class:`deque` になります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'collections_deque_populating.py'))
.. }}}
.. {{{end}}}

..
    Consuming
    =========

消費
====

..
    Similarly, the elements of the :class:`deque` can be consumed from
    both or either end, depending on the algorithm being applied.

同様に :class:`deque` の要素は適用されるアルゴリズム次第で両端か、どちらか一方の端から消費されます。

.. include:: collections_deque_consuming.py
    :literal:
    :start-after: #end_pymotw_header

..
    Use :func:`pop` to remove an item from the "right" end of the
    :class:`deque` and :func:`popleft` to take from the "left" end.

:class:`deque` の "右側" から要素を取り出すには :func:`pop` を、"左側" から取り出すには :func:`popleft` を使用してください。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'collections_deque_consuming.py'))
.. }}}
.. {{{end}}}

..
    Since deques are thread-safe, the contents can even be consumed from
    both ends at the same time from separate threads.

deque はスレッドセーフなので、そのコンテンツは別々のスレッドで同時に両端から消費されても大丈夫です。

.. include:: collections_deque_both_ends.py
    :literal:
    :start-after: #end_pymotw_header

..
    The threads in this example alternate between each end, removing items
    until the :class:`deque` is empty.

このサンプルのスレッドは :class:`deque` が空になるまで両端から交互に要素を削除します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'collections_deque_both_ends.py'))
.. }}}
.. {{{end}}}

..
    Rotating
    ========

ローテート
==========

..
    Another useful capability of the :class:`deque` is to rotate it in
    either direction, to skip over some items.

別の :class:`deque` の便利な機能は要素を読み飛ばすために一方の端へローテートすることです。

.. include:: collections_deque_rotate.py
    :literal:
    :start-after: #end_pymotw_header

..
    Rotating the :class:`deque` to the right (using a positive rotation)
    takes items from the right end and moves them to the left
    end. Rotating to the left (with a negative value) takes items from the
    left end and moves them to the right end.  It may help to visualize
    the items in the deque as being engraved along the edge of a dial.

:class:`deque` を(正のローテーションを使用して)右端へローテートすると、右端から要素を取り出して左端へその取り出した要素を移動します。(負の値で)左端へローテートすると、左端から要素を取り出して右端へその取り出した要素を移動します。それは目盛盤の端を刻み込むように deque の要素を視覚化する助けになるかもしれません。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'collections_deque_rotate.py'))
.. }}}
.. {{{end}}}

.. seealso::

    `WikiPedia: Deque <http://en.wikipedia.org/wiki/Deque>`_
        .. A discussion of the deque data structure.

        deque データ構造の説明

    `Deque Recipes <http://docs.python.org/lib/deque-recipes.html>`_
        .. Examples of using deques in algorithms from the standard library documentation.

        標準ライブラリドキュメントの deque を使用するアルゴリズムのサンプル
