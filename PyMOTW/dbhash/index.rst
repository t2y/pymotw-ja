..
    ====================================================
    dbhash -- DBM-style API for the BSD database library
    ====================================================

===========================================================
dbhash -- BSD データベースライブラリ向けの DBM スタイル API
===========================================================

..
    :synopsis: DBM-style API for the BSD database library

.. module:: dbhash
    :synopsis: BSD データベースライブラリ向けの DBM スタイル API

..
    :Purpose: Provides a dictionary-like API for accessing BSD ``db`` files.
    :Available In: 1.4 and later

:目的: BSD ``db`` ファイルへアクセスするディクショナリによく似た API を提供する
:利用できるバージョン: 1.4 以上

..
    The :mod:`dbhash` module is the primary backend for :mod:`anydbm`.  It uses the :mod:`bsddb` library to manage database files.  The semantics are the same as :mod:`anydbm`, so refer to the examples on that page for details.

:mod:`dbhash` モジュールは主に :mod:`anydbm` のバックエンドモジュールです。データベースファイルを管理するために :mod:`bsddb` ライブラリを使用します。その動作や仕組みは :mod:`anydbm` と同じなので、詳細はそちらのサンプルを参照してください。

.. seealso::

    `dbhash <http://docs.python.org/library/dbhash.html>`_
        .. The standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント

    :mod:`anydbm`
        .. The :mod:`anydbm` module.

        :mod:`anydbm` モジュール
