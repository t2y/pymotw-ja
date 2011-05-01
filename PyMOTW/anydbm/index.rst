..
    =======================================
    anydbm -- Access to DBM-style databases
    =======================================

================================================
anydbm -- DBM スタイルのデータベースへのアクセス
================================================

..
    :synopsis: anydbm provides a generic dictionary-like interface to DBM-style, string-keyed databases

.. module:: anydbm
    :synopsis: anydbm は DBM スタイルという文字列をキーとするデータベースに対してディクショナリによく似たインタフェースを提供する

..
    :Purpose: anydbm provides a generic dictionary-like interface to DBM-style, string-keyed databases
    :Available In: 1.4 and later

:目的: anydbm は DBM スタイルという文字列をキーとするデータベースに対してディクショナリによく似たインタフェースを提供する
:利用できるバージョン: 1.4 以上

..
    anydbm is a front-end for DBM-style databases that use simple string
    values as keys to access records containing strings.  It uses the
    :mod:`whichdb` module to identify :mod:`dbhash`, :mod:`gdbm`, and
    :mod:`dbm` databases, then opens them with the appropriate module.  It
    is used as a backend for :mod:`shelve`, which knows how to store
    objects using :mod:`pickle`.

:mod:`anydbm` モジュールは、文字列を含むレコードへアクセスするためにシンプルな文字列をキーとする DBM スタイルのデータベースのフロントエンドです。それは :mod:`whichdb` モジュールで :mod:`dbhash`, :mod:`gdbm`, :mod:`dbm` の中からデータベースを識別して、その適切なモジュールでデータベースをオープンします。そして :mod:`pickle` でオブジェクトを格納する :mod:`shelve` モジュールのバックエンドとして使用されます。

..
    Creating a New Database
    =======================

新たなデータベースを作成する
============================

..
    The storage format for new databases is selected by looking for each
    of these modules in order:

新しいデータベースのストレージフォーマットは次の順番でそれぞれのモジュールを調べて選択されます。

- :mod:`dbhash`
- :mod:`gdbm`
- :mod:`dbm`
- :mod:`dumbdbm`

..
    The :func:`open` function takes *flags* to control how the database
    file is managed.  To create a new database when necessary, use
    ``'c'``.  To always create a new database, use ``'n'``.

:func:`open` 関数は、データベースファイルを管理するために *flags* を取ります。必要に応じて新たなデータベースを作成するには ``'c'`` を、毎回新たなデータベースを作成するには ``'n'`` を使用してください。

.. include:: anydbm_new.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. workdir = path(cog.inFile).dirname()
.. sh("cd %s; rm -f /tmp/example.db" % workdir)
.. cog.out(run_script(cog.inFile, 'anydbm_new.py'))
.. }}}
.. {{{end}}}

..
    In this example, the file is always re-initialized.  To see what type
    of database was created, we can use :mod:`whichdb`.

このサンプルでは、example.db のファイルは毎回、初期化されます。どのデータベースが作成されるかを調べるには :mod:`whichdb` を使用します。

.. include:: anydbm_whichdb.py
    :literal:
    :start-after: #end_pymotw_header

..
    Your results may vary, depending on what modules are installed on your
    system.

実行環境にインストールされたモジュール次第で実行結果は変わる可能性があります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'anydbm_whichdb.py'))
.. }}}
.. {{{end}}}


..
    Opening an Existing Database
    ============================

既存のデータベースをオープンする
================================

..
    To open an existing database, use *flags* of either ``'r'`` (for
    read-only) or ``'w'`` (for read-write).  You don't need to worry about
    the format, because existing databases are automatically given to
    :mod:`whichdb` to identify.  If a file can be identified, the
    appropriate module is used to open it.

既存のデータベースをオープンするには、 *flags* に ``'r'`` (読み込み専用)か ``'w'`` (読み書き) のどちらかを指定してください。既存のデータベースは自動的に :mod:`whichdb` で識別されるのでフォーマットに関して心配する必要はありません。ファイルが識別されると、適切なモジュールがそのファイルをオープンするために使用されます。

.. include:: anydbm_existing.py
    :literal:
    :start-after: #end_pymotw_header

..
    Once open, ``db`` is a dictionary-like object, with support for the
    usual methods:

オープンされた ``db`` はディクショナリによく似たオブジェクトで、ディクショナリで普通に使うメソッドをサポートしています。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'anydbm_existing.py'))
.. }}}
.. {{{end}}}

..
    Error Cases
    ===========

エラーケース
============

..
    The keys of the database need to be strings.

データベースのキーは文字列でなければなりません。

.. include:: anydbm_intkeys.py
    :literal:
    :start-after: #end_pymotw_header

..
    Passing another type results in a :ref:`TypeError
    <exceptions-TypeError>`.

文字列以外の型を渡すと :ref:`TypeError <exceptions-TypeError>` が発生します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'anydbm_intkeys.py', ignore_error=True))
.. }}}
.. {{{end}}}

..
    Values must be strings or ``None``.

値は文字列か ``None`` でなければなりません。

.. include:: anydbm_intvalue.py
    :literal:
    :start-after: #end_pymotw_header

..
    A similar :ref:`TypeError <exceptions-TypeError>` is raised if a value
    is not a string.

値が文字列ではない場合も :ref:`TypeError <exceptions-TypeError>` が発生します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'anydbm_intvalue.py', ignore_error=True))
.. }}}
.. {{{end}}}

.. seealso::

    Module :mod:`shelve`
        .. Examples for the :mod:`shelve` module, which uses :mod:`anydbm` to store data.

        データを格納するために :mod:`anydbm` を使用する :mod:`shelve` モジュールのサンプル

    `anydbm <http://docs.python.org/library/anydbm.html>`_
        .. The standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント

    :ref:`article-data-persistence`
        .. Descriptions of other modules for storing data.

        データを格納するその他のモジュールの説明
