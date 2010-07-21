..
    ====================================
    array -- Sequence of fixed-type data
    ====================================

array -- データ型固定のシーケンス
=================================

.. module:: array
    :synopsis: データ型を数値に固定したシーケンスを効率良く管理する

..
    :Purpose: Manage sequences of fixed-type numerical data efficiently.
    :Python Version: 1.4 and later

:目的: データ型を数値に固定したシーケンスを効率良く管理する
:Python バージョン: 1.4 以上

..
    The :mod:`array` module defines a sequence data structure that looks
    very much like a ``list`` except that all of the members have to be of
    the same type.  The types supported are listed in the `standard
    library documentation <http://docs.python.org/library/array.html>`_.
    They are all numeric or other fixed-size primitive types such as
    bytes.

:mod:`array` モジュールは全ての要素が同じデータ型でなければいけないことを除けば ``list`` そっくりのシーケンスデータ構造を定義します。 `標準ライブラリドキュメント <http://docs.python.org/library/array.html>`_ にサポートされているデータ型が記載されています。サポートされているデータ型は全て数値か、バイト型のような古くからある固定長のデータ型になります。

..
    array Initialization
    ====================

アレイの初期化
==============

..
    An :class:`array` is instantiated with an argument describing the type
    of data to be allowed, and possibly an initial sequence of data to
    store in the array.

:class:`array` は許容されたデータ型を表す引数と、おそらくはアレイに格納する初期データシーケンスと一緒にインスタンス化されます。

.. include:: array_string.py
    :literal:
    :start-after: #end_pymotw_header

..
    In this example, the array is configured to hold a sequence of bytes
    and is initialized with a simple string.

この例のアレイはバイト列を持つように設定されて単純な文字列で初期化されます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'array_string.py'))
.. }}}

::

	$ python array_string.py
	As string: This is the array.
	As array : array('c', 'This is the array.')
	As hex   : 54686973206973207468652061727261792e

.. {{{end}}}

..
    Manipulating Arrays
    ===================

アレイを巧みに扱う
==================

..
    An :class:`array` can be extended and otherwise manipulated in the
    same ways as other Python sequences.

:class:`array` は伸長できて、さらに他の Python シーケンスと同様に巧みに扱えます。

.. include:: array_sequence.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'array_sequence.py'))
.. }}}

::

	$ python array_sequence.py
	Initial : array('i', [0, 1, 2, 3, 4])
	Extended: array('i', [0, 1, 2, 3, 4, 0, 1, 2, 3, 4])
	Slice   : array('i', [3, 4, 0])
	Iterator: [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 0), (6, 1), (7, 2), (8, 3), (9, 4)]

.. {{{end}}}

..
    Arrays and Files
    ================

アレイとファイル
================

..
    The contents of an array can be written to and read from files using
    built-in methods coded efficiently for that purpose.

アレイのコンテンツは効率的にコーディングされたビルトインメソッドを使用して、アレイへの書き込みとファイルからの読み込みを行うことができます。

.. include:: array_file.py
    :literal:
    :start-after: #end_pymotw_header

..
    This example illustrates reading the data "raw", directly from the
    binary file, versus reading it into a new array and converting the
    bytes to the appropriate types.

このサンプルは、直接バイナリファイルから "raw" データを読み込むのと、新たなアレイに格納してバイト型から適切な型へ変換するのを対比して説明しています。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'array_file.py'))
.. }}}

::

	$ python array_file.py
	A1: array('i', [0, 1, 2, 3, 4])
	Raw Contents: 0000000001000000020000000300000004000000
	A2: array('i', [0, 1, 2, 3, 4])

.. {{{end}}}

..
    Alternate Byte Ordering
    =======================

バイトオーダの代替
==================

..
    If the data in the array is not in the native byte order, or needs to
    be swapped before being written to a file intended for a system with a
    different byte order, it is easy to convert the entire array without
    iterating over the elements from Python.

アレイ内のデータがネイティブのバイトオーダではない、又は違うバイトオーダを持つシステムで使用するファイルへ書き込まれる前にスワップ処理を行う必要がある場合、Python からその要素のスワップ処理を繰り返し適用せずにアレイ全体を簡単に変換できます。

.. include:: array_byteswap.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'array_byteswap.py'))
.. }}}

::

	$ python array_byteswap.py
	    A1 hex         A1     A2 hex         A2
	---------- ---------- ---------- ----------
	  00000000          0   00000000          0
	  01000000          1   00000001   16777216
	  02000000          2   00000002   33554432
	  03000000          3   00000003   50331648
	  04000000          4   00000004   67108864

.. {{{end}}}

..
    `array <http://docs.python.org/library/array.html>`_
        The standard library documentation for this module.
    :mod:`struct`
        The struct module.
    `Numerical Python <http://www.scipy.org>`_
        NumPy is a Python library for working with large datasets efficiently.
    :ref:`article-data-structures`

.. seealso::

    `array <http://docs.python.org/library/array.html>`_
        本モジュールの標準ライブラリドキュメント

    :mod:`struct`
        struct モジュール

    `Numerical Python <http://www.scipy.org>`_
        NumPy は巨大なデータセットを効率的に扱うための Python ライブラリ

    :ref:`article-data-structures`
