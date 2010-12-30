..
   ======================================
   pprint -- Pretty-print data structures
   ======================================

===========================================
pprint -- データ構造を見やすい形で出力する
===========================================

.. module:: pprint
    :synopsis: データ構造を見やすい形で出力する

..
   :Purpose: Pretty-print data structures
   :Python Version: 1.4

:目的: データ構造を見やすい形で出力する
:Python バージョン: 1.4

..
   :mod:`pprint` contains a "pretty printer" for producing aesthetically
   pleasing representations of your data structures.  The formatter
   produces representations of data structures that can be parsed
   correctly by the interpreter, and are also easy for a human to
   read. The output is kept on a single line, if possible, and indented
   when split across multiple lines.

:mod:`pprint` はあなたのデータ構造を美しく、安心出来るような形で出力する "pretty printer" を含んでいます。インタプリタによって、正しく解析されうるデータ構造を正しく、そして人が見やすい形で出力してくれます。出力は可能ならば1行でなされ、複数行にまたぐときはインデントされます。

..
   The examples below all depend on ``pprint_data.py``, which contains:

以下の例は ``pprint_data.py`` に依存しており、そのファイルは以下のデータを含んでいます。

.. include:: pprint_data.py
    :literal:
    :start-after: #end_pymotw_header

..
   Printing
   ========

出力
====

..
   The simplest way to use the module is through the ``pprint()``
   function. It formats your object and writes it to the data stream
   passed as argument (or :ref:`sys.stdout <sys-input-output>` by
   default).

このモジュールを使う一番シンプルな方法は ``pprint()`` 関数を使うことです。この関数は、あなたのオブジェクトをフォーマットし直し、命令として渡されたデータストリームに書き出します。(デフォルトでは :ref:`sys.stdout <sys-input-output>` )

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
=============

..
   If you need to format a data structure, but do not want to write it
   directly to a stream (for logging purposes, for example) you can use
   ``pformat()`` to build a string representation that can then be passed
   to another function.

データ構造の体裁を整える必要があるが、直接ストリームに書き出したくない場合(ログなどの目的で)、 ``pformat()`` 関数は別の関数が扱えるように文字表現を組み立ててくれます。

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
===============

..
   The ``PrettyPrinter`` class used by ``pprint()`` can also work with
   your own classes, if they define a ``__repr__()`` method.

``pprint()`` が使っている ``PrettyPrinter`` クラスは ``__repr__()`` メソッドが定義されていれば、あなたの自身のクラスとも働きます。

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
================

..
   Recursive data structures are represented with a reference to the original
   source of the data, with the form ``<Recursion on typename with id=number>``. For
   example:

再帰的なデータ構造は、 ``<Recursion on typename with id=number>`` という形式を用いてデータの元のソースへの参照として表現されます。例えば

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

制限した入れ子の出力
======================

..
   For very deep data structures, you may not want the output to include all of
   the details. It might be impossible to format the data properly, the formatted
   text might be too large to manage, or you may need all of it. In that case,
   the depth argument can control how far down into the nested data structure the
   pretty printer goes.

とでも深い構造を持ったデータに対しては、あなたはすべての詳細を出力に含めたいと思わないかもしれません。適切にデータの体裁を整えるのは不可能かもしれないし、体裁を整えた後のテキストデータは管理するには大きすぎるかもしれないし、また詳細まですべて必要かもしれません。この場合、pretty printer がどこまで深く入れ子になったデータを見るのか、命令によってコントロールすることができます。

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
=================

..
   The default output width for the formatted text is 80 columns. To adjust that
   width, use the width argument to ``pprint()``.

体裁を整えた後のテキストのデフォルトでの幅は、80列です。幅を合わせるためには、幅の命令を ``pprint()`` に入力してください。

.. include:: pprint_width.py
    :literal:
    :start-after: #end_pymotw_header


..
   Notice that when the width is too low to accommodate the formatted data
   structure, the lines are not truncated or wrapped if that would introduce
   invalid syntax.

体裁を整えた後のデータ構造を表現するのに、幅が狭すぎた場合、構文エラーを導く場合は出力データは省略されたりまとめられたりはしません。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'pprint_width.py'))
.. }}}
.. {{{end}}}

.. seealso::

    `pprint <http://docs.python.org/lib/module-pprint.html>`_
        このモジュールの基本ドキュメンテーション
