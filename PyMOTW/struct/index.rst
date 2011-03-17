..
    ==================================
    struct -- Working with Binary Data
    ==================================

==============================
struct -- バイナリデータを扱う
==============================

..
    :synopsis: Convert between strings and binary data.

.. module:: struct
    :synopsis: 文字列とバイナリデータを変換する

..
    :Purpose: Convert between strings and binary data.
    :Python Version: 1.4 and later 

:目的: 文字列とバイナリデータを変換する
:Python バージョン: 1.4 以上

..
    The :mod:`struct` module includes functions for converting between
    strings of bytes and native Python data types such as numbers and
    strings.

:mod:`struct` モジュールはバイト文字列と、数値や文字列といったネイティブの Python データ型を変換する関数を提供します。

..
    Functions vs. Struct Class
    ==========================

関数 対 Struct クラス
=====================

..
    There are a set of module-level functions for working with structured
    values, and there is also the :class:`Struct` class (new in Python
    2.5).  Format specifiers are converted from their string format to a
    compiled representation, similar to the way regular expressions are.
    The conversion takes some resources, so it is typically more efficient
    to do it once when creating a :class:`Struct` instance and call
    methods on the instance instead of using the module-level functions.
    All of the examples below use the :class:`Struct` class.

構造化された値を扱うモジュールレベルの関数セットに加えて :class:`Struct` クラス(Python 2.5 で追加)もあります。フォーマット指定子は、正規表現のように文字列フォーマットからコンパイルされた表現に変換されます。その変換処理はリソースを消費します。そのため :class:`Struct` インスタンスを作成して、モジュールレベルの関数を使用せずにインスタンスメソッドを呼び出す方が普通は効率が良いです。この後の全サンプルは :class:`Struct` クラスを使用します。

..
    Packing and Unpacking
    =====================

パックとアンパック
==================

..
    Structs support *packing* data into strings, and *unpacking* data from
    strings using format specifiers made up of characters representing the
    type of the data and optional count and endian-ness indicators.  For
    complete details, refer to `the standard library documentation
    <http://docs.python.org/library/struct.html>`__.

:class:`Struct` は文字列へデータを *パック* します。そして、そのデータ型の特性により表現されるフォーマット指定子を用いて、文字列からデータを *アンパック* します。また、オプションでサイズやエンディアンも指定できます。詳細は `標準ライブラリドキュメント <http://docs.python.org/library/struct.html>`__ を参照してください。

..
    In this example, the format specifier calls for an integer or long
    value, a two character string, and a floating point number.  The
    spaces between the format specifiers are included here for clarity,
    and are ignored when the format is compiled.

このサンプルでは、フォーマット指定子は整数(int か long)、2文字の文字列、浮動小数で呼び出されます。フォーマット指定子の間にスペースが含まれていますが、そのフォーマットがコンパイルされるときに無視されます。

.. include:: struct_pack.py
    :literal:
    :start-after: #end_pymotw_header

..
    The example converts the packed value to a sequence of hex bytes for
    printing with ``binascii.hexlify()``, since some of the characters are
    nulls.

このサンプルは、パックされた値を ``binascii.hexlify()`` で表示するために16進数のバイトシーケンスに変換します。文字によってはヌル(null)になります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'struct_pack.py'))
.. }}}
.. {{{end}}}

..
    If we pass the packed value to :func:`unpack`, we get basically the
    same values back (note the discrepancy in the floating point value).

:func:`unpack` にパックされた値を渡すと、基本的には同じ値が返されます(浮動小数が不一致なのに注意)。

.. include:: struct_unpack.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'struct_unpack.py'))
.. }}}
.. {{{end}}}

..
    Endianness
    ==========

エンディアン
============

..
    By default values are encoded using the native C library notion of
    "endianness".  It is easy to override that choice by providing an
    explicit endianness directive in the format string.

デフォルトでは、値はネイティブの C 言語ライブラリの "エンディアン" 表記でエンコードされます。それはフォーマット文字列にエンディアンディレクティブを明示的に指定することで簡単にオーバーライドできます。

.. include:: struct_endianness.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'struct_endianness.py'))
.. }}}
.. {{{end}}}

..
    Buffers
    =======

バッファ
========

..
    Working with binary packed data is typically reserved for highly
    performance sensitive situations or passing data into and out of
    extension modules.  In such situations, you can optimize by avoiding
    the overhead of allocating a new buffer for each packed structure.
    The :meth:`pack_into` and :meth:`unpack_from` methods support writing
    to pre-allocated buffers directly.

パックされたバイナリデータを扱うのは、普通は高いパフォーマンスを要求されるか、拡張モジュールの外部でデータを受け渡すときです。そういった状況では、それぞれのパックされた構造でバッファを割り当てないことでオーバーヘッドを減らして最適化できます。 :meth:`pack_into` と :meth:`unpack_from` メソッドは、あらかじめ割り当てられたバッファに直接書き込めます。

.. include:: struct_buffers.py
    :literal:
    :start-after: #end_pymotw_header

..
    The *size* attribute of the :class:`Struct` tells us how big the
    buffer needs to be.

:class:`Struct` の *size* 属性は必要なバッファがどのぐらいかを伝えます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'struct_buffers.py'))
.. }}}
.. {{{end}}}


.. seealso::

    `struct <http://docs.python.org/library/struct.html>`_
        .. The standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント

    :mod:`array`
        .. The array module, for working with sequences of fixed-type values.

        型を固定した値のシーケンスを扱う :mod:`array` モジュール

    :mod:`binascii`
        .. The binascii module, for producing ASCII representations of binary data.

        バイナリデータの ASCII 表現を生成する :mod:`binascii` モジュール

    `WikiPedia: Endianness <http://en.wikipedia.org/wiki/Endianness>`_
        .. Explanation of byte order and endianness in encoding.

        エンコーディングのエンディアンとバイトオーダの説明

    :ref:`article-data-structures`
        .. More tools for working with data structures.

        データ構造と連携すつその他のツール
