=========
 Counter
=========

..
    A :class:`Counter` is a container that keeps track of how many times
    equivalent values are added.  It can be used to implement the same
    algorithms for which bag or multiset data structures are commonly used
    in other languages.

:class:`Counter` は同じ値が何回追加されたかの記録し続けるコンテナです。他言語では一般的なバッグまたはマルチセットデータ構造のために同じアルゴリズムを実装するために使用されます。

..
    Initializing
    ============

初期化
======

..
    :class:`Counter` supports three forms of initialization.  Its
    constructor can be called with a sequence of items, a dictionary
    containing keys and counts, or using keyword arguments mapping string
    names to counts.

:class:`Counter` は3通り初期化をサポートします。そのコンストラクタは要素のシーケンス、キーと数を含むディクショナリ、文字列名と数をマッピングするキーワード引数のどれかで呼び出されます。

.. include:: collections_counter_init.py
   :literal:
   :start-after: #end_pymotw_header

..
    The results of all three forms of initialization are the same.

3通りの初期化による結果は全て同じです。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'collections_counter_init.py'))
.. }}}

::

	$ python collections_counter_init.py
	
	Counter({'b': 3, 'a': 2, 'c': 1})
	Counter({'b': 3, 'a': 2, 'c': 1})
	Counter({'b': 3, 'a': 2, 'c': 1})

.. {{{end}}}

..
    An empty :class:`Counter` can be constructed with no arguments and
    populated via the :func:`update` method.

空の :class:`Counter` インスタンスはは引数無しで作成して :func:`update` メソッドで値を追加します。

.. include:: collections_counter_update.py
   :literal:
   :start-after: #end_pymotw_header

..
    The count values are increased based on the new data, rather than
    replaced.  In this example, the count for ``a`` goes from ``3`` to
    ``4``.

カウンタの数値は置き換えられるのではなく新しいデータに基づいて増加します。このサンプルでは ``a`` に対する数値が ``3`` から ``4`` になります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'collections_counter_update.py'))
.. }}}

::

	$ python collections_counter_update.py
	
	Initial : Counter()
	Sequence: Counter({'a': 3, 'b': 2, 'c': 1, 'd': 1})
	Dict    : Counter({'d': 6, 'a': 4, 'b': 2, 'c': 1})

.. {{{end}}}

..
    Accessing Counts
    ================

カウンタにアクセスする
======================

..
    Once a :class:`Counter` is populated, its values can be retrieved
    using the dictionary API.

:class:`Counter` が追加されると、その数値はディクショナリ API を使用して取り出すことができます。

.. include:: collections_counter_get_values.py
   :literal:
   :start-after: #end_pymotw_header

..
    :class:`Counter` does not raise :ref:`KeyError <exceptions-KeyError>`
    for unknown items.  If a value has not been seen in the input (as with
    ``e`` in this example), its count is ``0``.

:class:`Counter` は不明な要素に対して :ref:`KeyError <exceptions-KeyError>` を発生させません。もし入力に対する数値(このサンプルの ``e`` のように)が存在しないなら、その数値は ``0`` です。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'collections_counter_get_values.py'))
.. }}}

::

	$ python collections_counter_get_values.py
	
	a : 3
	b : 2
	c : 1
	d : 1
	e : 0

.. {{{end}}}

..
    The :func:`elements` method returns an iterator that produces all of
    the items known to the :class:`Counter`.

:func:`elements` メソッドは :class:`Counter` に対して全ての要素を生成するイテレータを返します。

.. include:: collections_counter_elements.py
   :literal:
   :start-after: #end_pymotw_header

..
    The order of elements is not guaranteed, and items with counts less
    than zero are not included.

要素の順番は保証されず、また要素の数がゼロ以下のときは含まれません。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'collections_counter_elements.py'))
.. }}}

::

	$ python collections_counter_elements.py
	
	Counter({'e': 3, 'm': 1, 'l': 1, 'r': 1, 't': 1, 'y': 1, 'x': 1, 'z': 0})
	['e', 'e', 'e', 'm', 'l', 'r', 't', 'y', 'x']

.. {{{end}}}

..
    Use :func:`most_common` to produce a sequence of the *n* most
    frequently encountered input values and their respective counts.

最も頻度の高い入力値とその文字の現れた回数 *n* のシーケンスを生成するために :func:`most_common` を使用してください。

.. include:: collections_counter_most_common.py
   :literal:
   :start-after: #end_pymotw_header

..
    This example counts the letters appearing in all of the words in the
    system dictionary to produce a frequency distribution, then prints the
    three most common letters.  Leaving out the argument to
    :func:`most_common` produces a list of all the items, in order of
    frequency.

このサンプルは頻度分布を生成するためにシステム辞書の全ての単語に現れる文字を数えます。それから最も頻度の高いトップ3を表示します。 :func:`most_common` に引数を渡さないと、頻度の高い順番に全ての要素のリストを生成します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'collections_counter_most_common.py'))
.. }}}

::

	$ python collections_counter_most_common.py
	
	Most common:
	e:  235331
	i:  201032
	a:  199554

.. {{{end}}}

..
    Arithmetic
    ==========

算術演算
========

..
    :class:`Counter` instances support arithmetic and set operations for
    aggregating results.

:class:`Counter` インスタンスは集約した結果のために算術演算や集合演算をサポートします。

.. include:: collections_counter_arithmetic.py
   :literal:
   :start-after: #end_pymotw_header

..
    Each time a new :class:`Counter` is produced through an operation, any
    items with zero or negative counts are discarded.  The count for ``a``
    is the same in :data:`c1` and :data:`c2`, so subtraction leaves it at
    zero.

ある演算により新しい :class:`Counter` が生成される毎に、ゼロかマイナスの数値を持つ要素は破棄されます。 ``a`` の数値は :data:`c1` と :data:`c2` で同じ数なので、引き算をするとゼロになります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'collections_counter_arithmetic.py'))
.. }}}

::

	$ python collections_counter_arithmetic.py
	
	C1: Counter({'b': 3, 'a': 2, 'c': 1})
	C2: Counter({'a': 2, 'b': 1, 'e': 1, 'h': 1, 'l': 1, 'p': 1, 't': 1})
	
	Combined counts:
	Counter({'a': 4, 'b': 4, 'c': 1, 'e': 1, 'h': 1, 'l': 1, 'p': 1, 't': 1})
	
	Subtraction:
	Counter({'b': 2, 'c': 1})
	
	Intersection (taking positive minimums):
	Counter({'a': 2, 'b': 1})
	
	Union (taking maximums):
	Counter({'b': 3, 'a': 2, 'c': 1, 'e': 1, 'h': 1, 'l': 1, 'p': 1, 't': 1})

.. {{{end}}}


