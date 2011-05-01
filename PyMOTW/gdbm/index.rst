..
    ##############################################
    gdbm -- GNU's version of the dbm library
    ##############################################

##############################################
gdbm -- dbm ライブラリの GNU バージョン
##############################################

..
    :synopsis: GNU's version of the dbm library

.. module:: gdbm
    :synopsis: dbm ライブラリの GNU バージョン

..
    :Purpose: GNU's version of the dbm library
    :Available In: 1.4 and later

:目的: dbm ライブラリの GNU バージョン
:利用できるバージョン: 1.4 以上

..
    :mod:`gdbm` is GNU's updated version of the :mod:`dbm` library.  It follows the same semantics as the other DBM implementations described under :mod:`anydbm`, with a few changes to the *flags* supported by ``open()``.

:mod:`gdbm` は :mod:`dbm` ライブラリの GNU バージョンです。それは :mod:`anydbm` のその他の DBM 実装と同じ仕組みで動作します。 ``open()`` でサポートされる *flags* に少し違いがあります。

..
    Besides the standard ``'r'``, ``'w'``, ``'c'``, and ``'n'`` flags, ``gdbm.open()`` supports:
    * ``'f'`` to open the database in *fast* mode. In fast mode, writes to the database are not synchronized.
    * ``'s'`` to open the database in *synchronized* mode. Changes to the database are written to the file as they are made, rather than being delayed until the database is closed or synced explicitly.
    * ``'u'`` to open the database unlocked.

標準の ``'r'``, ``'w'``, ``'c'``, ``'n'`` フラグに加えて ``gdbm.open()`` がサポートされます。

    * ``'f'`` は *fast* モードでデータベースをオープンします。fast モードでは、同期せずにデータベースへ書き込みます。
    * ``'s'`` は *synchronized* モードでデータベースをオープンします。データベースに対する変更は、データベースがクローズされるか、明示的に同期するまで遅延するのではなく、すぐにファイルへ書き込みます。
    * ``'u'`` はアンロック状態でデータベースをオープンします。

.. seealso::

    `gdbm <http://docs.python.org/library/gdbm.html>`_
        .. The standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント

    :mod:`dbm`
        .. The :mod:`dbm` module.

        :mod:`dbm` モジュール
    
    :mod:`anydbm`
        .. The :mod:`anydbm` module.

        :mod:`anydbm` モジュール
