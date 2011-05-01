..
    ================================
    dbm -- Simple database interface
    ================================

===========================================
dbm -- シンプルなデータベースインタフェース
===========================================

..
    :synopsis: Simple database interface

.. module:: dbm
    :synopsis: シンプルなデータベースインタフェース

..
    :Purpose: Provides an interface to the Unix (n)dbm library.
    :Available In: 1.4 and later

:目的: Unix (n)dbm ライブラリのインタフェースを提供する
:利用できるバージョン: 1.4 以上

..
    The :mod:`dbm` module provides an interface to one of the dbm
    libraries, depending on how the module was configured during
    compilation.

:mod:`dbm` モジュールは、コンパイル時にどのモジュールが設定されたかで dbm ライブラリのインタフェースを提供します。

..
    Examples
    ========

サンプル
========

..
    The ``library`` attribute identifies the library being used, by name.

``library`` 属性は名前から使用されるライブラリを識別します。

.. include:: dbm_library.py
    :literal:
    :start-after: #end_pymotw_header

..
    Your results will depend on what library ``configure`` was able to
    find when the interpreter was built.

この実行結果は、インタープリタがビルドされたときに ``configure`` がどのライブラリを見つけるかで変わります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'dbm_library.py'))
.. }}}
.. {{{end}}}

..
    The :func:`open()` function follows the same semantics as the
    :mod:`anydbm` module.

:func:`open()` 関数は :mod:`anydbm` モジュールの動作や仕組みと同じです。

.. seealso::

    `dbm <http://docs.python.org/library/dbm.html>`_
        .. The standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント

    :mod:`anydbm`
        .. The :mod:`anydbm` module.

        :mod:`anydbm` モジュール
