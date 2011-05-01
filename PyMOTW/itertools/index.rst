..
    =====================================================
    itertools -- Iterator functions for efficient looping
    =====================================================

=====================================================
itertools -- 効率的なループ処理のためのイテレータ関数
=====================================================

..
    :synopsis: Iterator functions for efficient looping

.. module:: itertools
    :synopsis: 効率的なループ処理のためのイテレータ関数

..
    :Purpose:
        The itertools module includes a set of functions for working with iterable
        (sequence-like) data sets. 
    :Available In: 2.3

:目的: itertools モジュールは繰り返し可能な(シーケンスのような)データセットを扱う関数を提供する
:利用できるバージョン: 2.3

..
    The functions provided are inspired by similar features of the "lazy
    functional programming language" Haskell and SML. They are intended to
    be fast and use memory efficiently, but also to be hooked together to
    express more complicated iteration-based algorithms.

"lazy functional programming language" の Haskell や SML の類似機能からアイディアを得た関数が提供されています。それらの関数は高速且つ省メモリですが、イテレーションベースのアルゴリズムを複雑化させてしまうこともあります。

..
    Iterator-based code may be preferred over code which uses lists for
    several reasons. Since data is not produced from the iterator until it
    is needed, all of the data is not stored in memory at the same
    time. Reducing memory usage can reduce swapping and other side-effects
    of large data sets, increasing performance.

イテレータベースのコードの方が複数の理由でリストを使用するコードよりも推奨されます。イテレータで扱うデータは必要になるまで生成されないので、全てのデータを同時にメモリ内には格納されません。メモリ使用量が減少するということはパフォーマンスに影響を与えるスワッピングやその他の巨大なデータセットを扱うときの副作用を小さくします。

..
    Merging and Splitting Iterators
    ===============================

イテレータのマージと分割
========================

..
    The ``chain()`` function takes several iterators as arguments and
    returns a single iterator that produces the contents of all of them as
    though they came from a single sequence.

``chain()`` 関数は引数として複数のイテレータを受け取って、それらが1つのシーケンスであるかのように、全てのコンテンツを生成する1つのイテレータを返します。

.. include:: itertools_chain.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'itertools_chain.py'))
.. }}}
.. {{{end}}}

..
    ``izip()`` returns an iterator that combines the elements of several
    iterators into tuples. It works like the built-in function ``zip()``,
    except that it returns an iterator instead of a list.

``izip()`` 関数は引数で受け取った複数のイテレータの要素をタプルに結合するイテレータを返します。それはリストの代わりにイテレータを返すということを除けばビルトイン関数 ``zip()`` のように動作します。

.. include:: itertools_izip.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'itertools_izip.py'))
.. }}}
.. {{{end}}}

..
    The ``islice()`` function returns an iterator which returns selected
    items from the input iterator, by index. It takes the same arguments
    as the slice operator for lists: start, stop, and step. The start and
    step arguments are optional.

``islice()`` 関数は入力イテレータからインデックスで選択された要素を返すイテレータを返します。それはリストのスライシングのように開始、停止、ステップといった同じ引数を取ります。開始とステップの引数はオプションです。

.. include:: itertools_islice.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'itertools_islice.py'))
.. }}}
.. {{{end}}}

..
    The ``tee()`` function returns several independent iterators (defaults
    to 2) based on a single original input. It has semantics similar to
    the Unix `tee <http://unixhelp.ed.ac.uk/CGI/man-cgi?tee>`__ utility,
    which repeats the values it reads from its input and writes them to a
    named file and standard output.

``tee()`` 関数はオリジナルの入力イテレータを1つ受け取って、複数の独立したイテレータを返します(デフォルトは2つ)。それはその入力イテレータから読み込まれた値を繰り返してファイルや標準出力に書き込む Unix の `tee <http://unixhelp.ed.ac.uk/CGI/man-cgi?tee>`__ ユーティリティによく似た動作をします。

.. include:: itertools_tee.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'itertools_tee.py'))
.. }}}
.. {{{end}}}

..
    Since the new iterators created by ``tee()`` share the input, you
    should not use the original iterator any more. If you do consume
    values from the original input, the new iterators will not produce
    those values:

``tee()`` が生成する新たなイテレータはそのオリジナルの入力イテレータを共有するので、生成後はオリジナルの入力イテレータを使用してはいけません。もしオリジナルの入力イテレータから値を取り出すと、新たなイテレータはその取り出された値を生成しません。

.. include:: itertools_tee_error.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'itertools_tee_error.py'))
.. }}}
.. {{{end}}}

..
    Converting Inputs
    =================

入力を変換する
==============

..
    The ``imap()`` function returns an iterator that calls a function on
    the values in the input iterators, and returns the results. It works
    like the built-in ``map()``, except that it stops when any input
    iterator is exhausted (instead of inserting ``None`` values to
    completely consume all of the inputs).

``imap()`` 関数は入力イテレータの値を引数にして関数を呼び出すイテレータを返します。そして呼び出されたその関数の結果を返します。それは入力イテレータの値がなくなったときに停止するいうこと(代わりに ``None`` を追加する)を除けば ``map()`` 関数のように動作します。

..
    In the first example, the lambda function multiplies the input values
    by 2. In a second example, the lambda function multiplies 2 arguments,
    taken from separate iterators, and returns a tuple with the original
    arguments and the computed value.

最初のサンプルでは lambda 関数は入力値を2倍します。2番目のサンプルでは lambda 関数は引数で渡される2つのイテレータから受け取った2つの引数の乗算を行います。そしてオリジナルの引数と算出された値のタプルを返します。

.. include:: itertools_imap.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'itertools_imap.py'))
.. }}}
.. {{{end}}}

..
    The ``starmap()`` function is similar to ``imap()``, but instead of
    constructing a tuple from multiple iterators it splits up the items in
    a single iterator as arguments to the mapping function using the ``*``
    syntax. Where the mapping function to imap() is called f(i1, i2), the
    mapping function to starmap() is called ``f(*i)``.

``starmap()`` 関数は ``imap()`` 関数によく似ていますが、複数のイテレータを持つタプルを構築する代わりにマッピングする関数への引数として ``*`` 構文で1つのイテレータ内にある要素を分割して渡します。imap() にマッピングされる関数が f(i1, i2) のように引数を渡して呼び出す場合 starmap() にマッピングされる関数は ``f(*i)`` になります。

.. include:: itertools_starmap.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'itertools_starmap.py'))
.. }}}
.. {{{end}}}

..
    Producing New Values
    ====================

新たな値を生成する
==================

..
    The ``count()`` function returns an interator that produces
    consecutive integers, indefinitely. The first number can be passed as
    an argument, the default is zero. There is no upper bound argument
    (see the built-in ``xrange()`` for more control over the result
    set). In this example, the iteration stops because the list argument
    is consumed.

``count()`` 関数は無限に連続した整数を生成するイテレータを返します。開始の数のデフォルトはゼロで引数として渡すことができます。上限の引数はありません(結果セットの詳細な制御はビルトイン関数 ``xrange()`` を参照)。このサンプルでは、リストの引数の要素がなくなるとそのイテレーションが停止します。

.. include:: itertools_count.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'itertools_count.py'))
.. }}}
.. {{{end}}}

..
    The ``cycle()`` function returns an iterator that repeats the contents
    of the arguments it is given indefinitely. Since it has to remember
    the entire contents of the input iterator, it may consume quite a bit
    of memory if the iterator is long. In this example, a counter variable
    is used to break out of the loop after a few cycles.

``cycle()`` 関数は引数のコンテンツを無限に繰り返すイテレータを返します。入力イテレータの完全なコンテンツを覚えておく必要があるので、そのイテレータが大きい場合に少しメモリを消費する可能性があります。このサンプルでは数回サイクルした後でループを脱出するためにカウンタ変数が使用されます。

.. include:: itertools_cycle.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'itertools_cycle.py'))
.. }}}
.. {{{end}}}

..
    The ``repeat()`` function returns an iterator that produces the same
    value each time it is accessed. It keeps going forever, unless the
    optional times argument is provided to limit it.

``repeat()`` 関数はアクセスされると毎回同じ値を生成するイテレータを返します。オプションの引数で上限値を渡さない限り無限に値を返します。

.. include:: itertools_repeat.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'itertools_repeat.py'))
.. }}}
.. {{{end}}}

..
    It is useful to combine ``repeat()`` with ``izip()`` or ``imap()``
    when invariant values need to be included with the values from the
    other iterators.

定数が他のイテレータからの値と一緒に含まれる必要があるとき ``izip()`` 又は ``imap()`` で ``repeat()`` を結合すると便利です。

.. include:: itertools_repeat_izip.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'itertools_repeat_izip.py'))
.. }}}
.. {{{end}}}

.. include:: itertools_repeat_imap.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'itertools_repeat_imap.py'))
.. }}}
.. {{{end}}}

..
    Filtering
    =========

フィルタリング
==============

..
    The ``dropwhile()`` function returns an iterator that returns elements
    of the input iterator after a condition becomes false for the first
    time. It does not filter every item of the input; after the condition
    is false the first time, all of the remaining items in the input are
    returned.

``dropwhile()`` 関数は条件が最初に False になった後で入力イテレータの要素を返すイテレータを返します。その条件が False になった後では各要素がフィルタされず、入力イテレータの残りの要素が返されます。

.. include:: itertools_dropwhile.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'itertools_dropwhile.py'))
.. }}}
.. {{{end}}}

..
    The opposite of ``dropwhile()``, ``takewhile()`` returns an iterator
    that returns items from the input iterator as long as the test
    function returns true.

``dropwhile()`` とは逆の機能で ``takewhile()`` 関数はテスト関数が True を返す限り入力イテレータから要素を返すイテレータを返します。

.. include:: itertools_takewhile.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'itertools_takewhile.py'))
.. }}}
.. {{{end}}}

..
    ``ifilter()`` returns an iterator that works like the built-in
    ``filter()`` does for lists, including only items for which the test
    function returns true. It is different from ``dropwhile()`` in that
    every item is tested before it is returned.

``ifilter()`` 関数は、テスト関数が True を返すときのみ要素を含める、ビルトイン関数の ``filter()`` のように動作するイテレータを返します。 ``dropwhile()`` との違いは全要素に対してテスト関数で判定を行ってその要素を返します。

.. include:: itertools_ifilter.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'itertools_ifilter.py'))
.. }}}
.. {{{end}}}

..
    The opposite of ``ifilter()``, ``ifilterfalse()`` returns an iterator
    that includes only items where the test function returns false.

``ifilter()`` とは逆の機能で ``ifilterfalse()`` 関数はテスト関数が False を返すときのみ要素を含めるイテレータを返します。

.. include:: itertools_ifilterfalse.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'itertools_ifilterfalse.py'))
.. }}}
.. {{{end}}}

.. _itertools-groupby:

..
    Grouping Data
    =============

データのグループ化
==================

..
    The ``groupby()`` function returns an iterator that produces sets of
    values grouped by a common key.

``groupby()`` 関数は共通のキーでグループ化された値セットを生成するイテレータを返します。

..
    This example from the standard library documentation shows how to group keys
    in a dictionary which have the same value:

標準ライブラリドキュメントで紹介されているこのサンプルは同じ値を持つ辞書のキーをグループ化します。

.. include:: itertools_groupby.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'itertools_groupby.py'))
.. }}}
.. {{{end}}}

..
    This more complicated example illustrates grouping related values based on
    some attribute. Notice that the input sequence needs to be sorted on the key
    in order for the groupings to work out as expected.

これは複数の属性をベースに関連する値をグループ化することを紹介した複雑なサンプルです。期待した通りに動作するグルーピングのために入力シーケンスがキーの順番通りにソートされている必要があることに注意してください。

.. include:: itertools_groupby_seq.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'itertools_groupby_seq.py'))
.. }}}
.. {{{end}}}



.. seealso::

    `itertools <http://docs.python.org/library/itertools.html>`_
        .. The standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント

    `The Standard ML Basis Library <http://www.standardml.org/Basis/>`_
        .. The library for SML.

        SML のライブラリ

    `Definition of Haskell and the Standard Libraries <http://www.haskell.org/definition/>`_
        .. Standard library specification for the functional language Haskell.

        関数型言語 Haskell の標準ライブラリ仕様
