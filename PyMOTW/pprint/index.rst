..
   ======================================
   pprint -- Pretty-print data structures
   ======================================

===========================================
pprint -- データ構造を見やすい形で出力する
===========================================

..
    :synopsis: Pretty-print data structures

.. module:: pprint
    :synopsis: データ構造を見やすい形で出力する

..
    :Purpose: Pretty-print data structures
    :Available In: 1.4

:目的: データ構造を見やすい形で出力する
:利用できるバージョン: 1.4

..
   :mod:`pprint` contains a "pretty printer" for producing aesthetically
   pleasing representations of your data structures.  The formatter
   produces representations of data structures that can be parsed
   correctly by the interpreter, and are also easy for a human to
   read. The output is kept on a single line, if possible, and indented
   when split across multiple lines.

:mod:`pprint` はデータ構造の表現を見て美しい形で出力する "pretty printer" を提供します。そのフォーマッタはインタープリタが正しく解析したデータ構造の形を生成します。さらにそれは人間にとっても読み易いです。その出力はできるだけ1行でなされ、複数行にわたるときはインデントされます。

..
   The examples below all depend on ``pprint_data.py``, which contains:

全てのサンプルは ``pprint_data.py`` に依存しており、そのファイルは次のデータを含んでいます。

.. include:: pprint_data.py
    :literal:
    :start-after: #end_pymotw_header

..
   Printing
   ========

表示
====

..
   The simplest way to use the module is through the ``pprint()``
   function. It formats your object and writes it to the data stream
   passed as argument (or :ref:`sys.stdout <sys-input-output>` by
   default).

このモジュールを使う一番シンプルな方法は ``pprint()`` 関数を使うことです。この関数は引数として渡されたオブジェクトを整形して、その内容をデータストリーム(デフォルトでは :ref:`sys.stdout <sys-input-output>`)へ書き込みます。

.. include:: pprint_pprint.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'pprint_pprint.py'))
.. }}}
.. {{{end}}}

..
   Formatting
   ==========

体裁を整える
============

..
   If you need to format a data structure, but do not want to write it
   directly to a stream (for logging purposes, for example) you can use
   ``pformat()`` to build a string representation that can then be passed
   to another function.

データ構造の体裁を整える必要があるが、直接ストリームに書き出したくない場合(例えば、ログ目的)、別の関数へ渡せるようにそのデータ構造の文字列表現を組み立てる ``pformat()`` を使うことができます。

.. include:: pprint_pformat.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'pprint_pformat.py'))
.. }}}
.. {{{end}}}

..
   Arbitrary Classes
   =================

任意のクラス
============

..
   The ``PrettyPrinter`` class used by ``pprint()`` can also work with
   your own classes, if they define a ``__repr__()`` method.

``pprint()`` が使う ``PrettyPrinter`` クラスは ``__repr__()`` メソッドを定義すれば、独自のクラスと連携することもできます。

.. include:: pprint_arbitrary_object.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'pprint_arbitrary_object.py'))
.. }}}
.. {{{end}}}

..
   Recursion
   =========

再帰型のデータ
==============

..
   Recursive data structures are represented with a reference to the original
   source of the data, with the form ``<Recursion on typename with id=number>``. For
   example:

再帰的なデータ構造は ``<Recursion on typename with id=number>`` という形式でデータの元のソースへの参照として表現されます。例えば

.. include:: pprint_recursion.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'pprint_recursion.py'))
.. }}}
.. {{{end}}}


..
   Limiting Nested Output
   ======================

入れ子になった出力の制限
========================

..
   For very deep data structures, you may not want the output to include all of
   the details. It might be impossible to format the data properly, the formatted
   text might be too large to manage, or you may need all of it. In that case,
   the depth argument can control how far down into the nested data structure the
   pretty printer goes.

とても深い構造を持ったデータに対しては、全ての詳細を出力に含めたくないかもしれません。適切にデータの体裁を整えるのは不可能かもしれないし、体裁を整えた後のテキストデータは管理するには大きすぎるかもしれません。もしくは全ての詳細が必要かもしれません。そういった場合、pretty printer が入れ子になったデータ構造をどのぐらい辿るのかを depth 引数で制御することができます。

.. include:: pprint_depth.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'pprint_depth.py'))
.. }}}
.. {{{end}}}


..
   Controlling Output Width
   ========================

出力の幅の設定
==============

..
   The default output width for the formatted text is 80 columns. To adjust that
   width, use the width argument to ``pprint()``.

体裁を整えたテキストのデフォルト幅は 80 列です。その幅を調整するには ``pprint()`` の width 引数を使用してください。

.. include:: pprint_width.py
    :literal:
    :start-after: #end_pymotw_header


..
   Notice that when the width is too low to accommodate the formatted data
   structure, the lines are not truncated or wrapped if that would introduce
   invalid syntax.

体裁を整えたデータ構造を表示するのにその幅が狭すぎるとき、そのデータ構造が不正な構文であっても、その行が切り捨てられたり、まとめられたりはしないことに注意してください。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'pprint_width.py'))
.. }}}
.. {{{end}}}

.. seealso::

    `pprint <http://docs.python.org/lib/module-pprint.html>`_
        .. Standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント
