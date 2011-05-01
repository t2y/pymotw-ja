..
    ####################################################
    whichdb -- Identify DBM-style database formats
    ####################################################

###########################################################
whichdb -- DBM スタイルのデータベースフォーマットを確認する
###########################################################

..
    :synopsis: Identify DBM-style database formats

.. module:: whichdb
    :synopsis: DBM スタイルのデータベースフォーマットを確認する

..
    :Purpose: Examine existing DBM-style database file to determine what library should be used to open it.
    :Available In: 1.4 and later

:目的: どのライブラリをデータベースのオープンに使用すべきかを決定するために既存の DBM スタイルのデータベースファイルを調べる
:利用できるバージョン: 1.4 以上

..
    The :mod:`whichdb` module contains one function, ``whichdb()``.  It can be used to examine an existing database file to determine which dbm library should be used to open it.  It returns ``None`` if there is a problem opening the file, or the string name of the module to use to open the file.  If it can open the file but cannot determine the library to use, it returns the empty string.

:mod:`whichdb` モジュールは ``whichdb()`` という1つの関数を提供します。どの dbm ライブラリがオープンするために使用すべきかを決定するために既存のデータベースファイルを調べるために使用されます。もしファイルのオープンに問題があれば ``None`` か、ファイルのオープンに使用したモジュールの文字列名を返します。もしファイルがオープンできてもそのライブラリの使用を決定できない場合、空の文字列を返します。

.. include:: whichdb_whichdb.py
    :literal:
    :start-after: #end_pymotw_header

..
    Your results will vary, depending on what modules are available in your PYTHONPATH.

実行結果はあなたの環境の PYTHONPATH で利用可能なモジュール次第で変わるでしょう。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'whichdb_whichdb.py'))
.. }}}
.. {{{end}}}


.. seealso::

    `whichdb <http://docs.python.org/lib/module-whichdb.html>`_
        .. Standard library documentation for this module.
        
        本モジュールの標準ライブラリドキュメント

    :mod:`anydbm`
        .. The anydbm module uses the best available DBM implementation when creating new databases.

        anydbm モジュールは新しいデータベースを作成するときに最適な DBM 実装を使用します

    :mod:`shelve`
        .. The shelve module provides a mapping-style API for DBM databases.

        shelve モジュールは DBM データベースにマッピングスタイルの API を提供します
