..
    ========================================================
     operator -- Functional interface to built-in operators
    ========================================================

=======================================================
 operator -- ビルトイン演算子に対する関数インタフェース
=======================================================

..
    :synopsis: Functional interface to built-in operators

.. module:: operator
    :synopsis: ビルトイン演算子に対する関数インタフェース

..
    :Purpose: Functional interface to built-in operators.
    :Available In: 1.4 and later

:目的: ビルトイン演算子に対する関数インタフェース
:利用できるバージョン: 1.4 以上

..
    Functional programming using iterators occasionally requires creating
    small functions for simple expressions. Sometimes these can be
    expressed as lambda functions, but some operations do not need to be
    implemented with custom functions at all. The :mod:`operator` module
    defines functions that correspond to built-in operations for
    arithmetic and comparison, as well as sequence and dictionary
    operations.

イテレータを折に触れて使用する関数プログラミングはシンプルな表現のために小さな関数を作成するように要求します。それは lambda 関数として表現されるときもありますが、幾つかの演算では全く独自の関数で実装される必要はありません。 :mod:`operator` モジュールはシーケンスやディクショナリの操作と同様に算術や比較演算のためにビルトイン演算に対応する関数を定義します。

..
    Logical Operations
    ==================

論理演算
========

..
    There are functions for determining the boolean equivalent for a
    value, negating that to create the opposite boolean value, and
    comparing objects to see if they are identical.

真偽値の評価、逆の真偽値を作成するための否定やそういった値が等価かどうかを確認するための比較オブジェクトを決定する関数があります。

.. include:: operator_boolean.py
    :literal:
    :start-after: #end_pymotw_header

..
    :func:`not_` includes the trailing underscore because :command:`not`
    is a Python keyword.  :func:`truth` applies the same logic used when
    testing an expression in an :command:`if` statement.  :func:`is_`
    implements the same check used by the :command:`is` keyword, and
    :func:`is_not` does the same test and returns the opposite answer.

:command:`not` は Python のキーワードなので :func:`not_` は最後にアンダースコアが続きます。 :func:`truth` は :command:`if` 文の式がテストされるときと同じロジックを適用します。 :func:`is_` は :command:`is` キーワードにより使用される同じチェックを実装します。そして :func:`is_not` は同じテストを行い逆の内容を返します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'operator_boolean.py'))
.. }}}

::

	$ python operator_boolean.py
	
	a = -1
	b = 5
	
	not_(a)     : False
	truth(a)    : True
	is_(a, b)   : False
	is_not(a, b): True

.. {{{end}}}

..
    Comparison Operators
    ====================

比較演算子
==========

..
    All of the rich comparison operators are supported.

実用に十分な比較演算子が全てサポートされています。

.. include:: operator_comparisons.py
    :literal:
    :start-after: #end_pymotw_header

..
    The functions are equivalent to the expression syntax using ``<``,
    ``<=``, ``==``, ``>=``, and ``>``.

それらの関数群は ``<``, ``<=``, ``==``, ``>=`` と ``>`` を使用する式の構文と等価です。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'operator_comparisons.py'))
.. }}}

::

	$ python operator_comparisons.py
	
	
	a = 1
	b = 5.0
	lt(a, b): True
	le(a, b): True
	eq(a, b): False
	ne(a, b): True
	ge(a, b): False
	gt(a, b): False

.. {{{end}}}


..
    Arithmetic Operators
    ====================

算術演算子
==========

..
    The arithmetic operators for manipulating numerical values are also supported.

数値の値を操作するために算術演算子もサポートされています。

.. include:: operator_math.py
    :literal:
    :start-after: #end_pymotw_header

.. note::
  ..
      There are two separate division operators: :func:`floordiv` (integer
      division as implemented in Python before version 3.0) and
      :func:`truediv` (floating point division).
    
    除算演算子は :func:`floordiv` (Python3 以前に Python で実装された整数除算) と :func:`truediv` (浮動小数点除算) の2つに分かれています。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'operator_math.py'))
.. }}}

::

	$ python operator_math.py
	
	a = -1
	b = 5.0
	c = 2
	d = 6
	
	Positive/Negative:
	abs(a): 1
	neg(a): 1
	neg(b): -5.0
	pos(a): -1
	pos(b): 5.0
	
	Arithmetic:
	add(a, b)     : 4.0
	div(a, b)     : -0.2
	div(d, c)     : 3
	floordiv(a, b): -1.0
	floordiv(d, c): 3
	mod(a, b)     : 4.0
	mul(a, b)     : -5.0
	pow(c, d)     : 64
	sub(b, a)     : 6.0
	truediv(a, b) : -0.2
	truediv(d, c) : 3.0
	
	Bitwise:
	and_(c, d)  : 2
	invert(c)   : -3
	lshift(c, d): 128
	or_(c, d)   : 6
	rshift(d, c): 1
	xor(c, d)   : 4

.. {{{end}}}


..
    Sequence Operators
    ==================

シーケンス演算子
================

..
    The operators for working with sequences can be divided into four
    groups for building up sequences, searching for items, accessing
    contents, and removing items from sequences.

シーケンスで動作する演算子は4つのグループに分けられます。それらはシーケンスの構築、要素の検索、中身へのアクセス、シーケンスから要素を削除するものです。

.. include:: operator_sequences.py
    :literal:
    :start-after: #end_pymotw_header

..
    Some of these operations, such as :func:`setitem` and :func:`delitem`,
    modify the sequence in place and do not return a value.

そういった演算子には :func:`setitem` や :func:`delitem` のように特定位置のシーケンスを変更して値を返さないものがあります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'operator_sequences.py'))
.. }}}

::

	$ python operator_sequences.py
	
	a = [1, 2, 3]
	b = ['a', 'b', 'c']
	
	Constructive:
	  concat(a, b): [1, 2, 3, 'a', 'b', 'c']
	  repeat(a, 3): [1, 2, 3, 1, 2, 3, 1, 2, 3]
	
	Searching:
	  contains(a, 1)  : True
	  contains(b, "d"): False
	  countOf(a, 1)   : 1
	  countOf(b, "d") : 0
	  indexOf(a, 5)   : 0
	
	Access Items:
	  getitem(b, 1)            : b
	  getslice(a, 1, 3)        : [2, 3]
	  setitem(b, 1, "d")       : None , after b = ['a', 'd', 'c']
	  setslice(a, 1, 3, [4, 5]): None , after a = [1, 4, 5]
	
	Destructive:
	  delitem(b, 1)    : None , after b = ['a', 'c']
	  delslice(a, 1, 3): None , after a = [1]

.. {{{end}}}


..
    In-place Operators
    ==================

インプレース演算子
==================

..
    In addition to the standard operators, many types of objects support
    "in-place" modification through special operators such as ``+=``. There are
    equivalent functions for in-place modifications, too:

標準演算子に加えて、多くのオブジェクト型が ``+=`` のような特種な演算子を通して入力データを直接書き換える "インプレース" 処理をサポートします。インプレース処理と同等の関数もあります。

.. include:: operator_inplace.py
    :literal:
    :start-after: #end_pymotw_header

..
    These examples only demonstrate a few of the functions. Refer to the stdlib
    documentation for complete details.

このサンプルはインプレース処理を行う関数を少しだけ紹介します。その他の関数の詳細は標準ライブラリを参照してください。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'operator_inplace.py'))
.. }}}

::

	$ python operator_inplace.py
	
	a = -1
	b = 5.0
	c = [1, 2, 3]
	d = ['a', 'b', 'c']
	
	a = iadd(a, b) => 4.0
	
	c = iconcat(c, d) => [1, 2, 3, 'a', 'b', 'c']

.. {{{end}}}

..
    Attribute and Item "Getters"
    ============================

属性と要素の "ゲッタ"
=====================

..
    One of the most unusual features of the :mod:`operator` module is the
    concept of *getters*. These are callable objects constructed at
    runtime to retrieve attributes of objects or contents from
    sequences. Getters are especially useful when working with iterators
    or generator sequences, where they are intended to incur less overhead
    than a lambda or Python function.

:mod:`operator` モジュールで最も独特な機能の1つは *ゲッタ* の概念です。オブジェクトの属性、又はシーケンスから要素を取り出すために実行時に構築された呼び出し可能オブジェクトです。ゲッタは lambda 又は Python 関数よりもオーバーヘッドを少なくする目的でイテレータかジェネレータと一緒に使用すると特に便利です。

.. include:: operator_attrgetter.py
    :literal:
    :start-after: #end_pymotw_header

..
    Attribute getters work like ``lambda x, n='attrname': getattr(x, n)``:

属性のゲッタは ``lambda x, n='attrname': getattr(x, n)`` のように動作します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'operator_attrgetter.py'))
.. }}}

::

	$ python operator_attrgetter.py
	
	[MyObj(0), MyObj(1), MyObj(2), MyObj(3), MyObj(4)]
	[0, 1, 2, 3, 4]

.. {{{end}}}

..
    While item getters work like ``lambda x, y=5: x[y]``:

要素のゲッタは ``lambda x, y=5: x[y]`` のように動作します。

.. include:: operator_itemgetter.py
    :literal:
    :start-after: #end_pymotw_header

..
    Item getters work with mappings as well as sequences.

要素のゲッタはシーケンスと同様にマッピングされて動作します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'operator_itemgetter.py'))
.. }}}

::

	$ python operator_itemgetter.py
	
	Dictionaries:
	[{'val': 0}, {'val': 1}, {'val': 2}, {'val': 3}, {'val': 4}]
	[0, 1, 2, 3, 4]
	
	Tuples:
	[(0, 0), (1, 2), (2, 4), (3, 6), (4, 8)]
	[0, 2, 4, 6, 8]

.. {{{end}}}

..
    Combining Operators and Custom Classes
    ======================================

演算子とカスタムクラスを組み合わせる
====================================

..
    The functions in the :mod:`operator` module work via the standard
    Python interfaces for their operations, so they work with user-defined
    classes as well as the built-in types.

:mod:`operator` モジュールの関数は演算のために標準の Python インタフェース経由で動作します。そのため、ビルトイン型と同様にユーザ定義クラスで動作します。

.. include:: operator_classes.py
    :literal:
    :start-after: #end_pymotw_header

..
    Refer to the Python reference guide for a complete list of the special
    methods used by each operator.

それぞれの演算子で使用される特殊メソッドの完全なリストは Python リファレンスガイドを参照してください。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'operator_classes.py'))
.. }}}

::

	$ python operator_classes.py
	
	Comparison:
	Testing MyObj(1) < MyObj(2)
	True
	
	Arithmetic:
	Adding MyObj(1) + MyObj(2)
	MyObj(3)

.. {{{end}}}


..
    Type Checking
    =============

型チェック
==========

..
    Besides the actual operators, there are functions for testing API
    compliance for mapping, number, and sequence types. 

実際の演算子に加えて、マッピング、数値やシーケンスのデータ型のためにテスト API 準拠の関数があります。

.. include:: operator_typechecking.py
    :literal:
    :start-after: #end_pymotw_header

..
    The tests are not perfect, since the interfaces are not strictly
    defined, but they do provide some idea of what is supported.

サンプルのテストはインタフェースが厳密に定義されていないので完璧ではありません。しかし、そういったインタフェースの何がサポートされているかのアイディアを与えてくれます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'operator_typechecking.py'))
.. }}}

::

	$ python operator_typechecking.py
	
	isMappingType(o): False
	isMappingType(t): True
	isNumberType(o): False
	isNumberType(t): True
	isSequenceType(o): False
	isSequenceType(t): True

.. {{{end}}}

..
    :mod:`abc` includes :ref:`abstract base classes
    <abc-collection-types>` that define the APIs for collection types.

:mod:`abc` はコレクション型の API を定義する :ref:`抽象基底クラス <abc-collection-types>` を含みます。


.. seealso::

    `operator <http://docs.python.org/lib/module-operator.html>`_
        .. Standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント

    :mod:`functools`
        .. Functional programming tools, including the
           :func:`total_ordering` decorator for adding rich comparison
           methods to a class.

        関数プログラミングツールで、拡張比較(rich comparison)メソッドをクラスに追加する :func:`total_ordering` デコレータを提供します

    :mod:`itertools`
        .. Iterator operations.

        イテレータの操作
