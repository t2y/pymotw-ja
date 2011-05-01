..
    ##############################################################
    shelve -- Persistent storage of arbitrary Python objects
    ##############################################################

####################################################
shelve -- 任意の Python オブジェクトの永続ストレージ
####################################################

..
    :synopsis: Persistent storage of arbitrary Python objects

.. module:: shelve
    :synopsis: 任意の Python オブジェクトの永続ストレージ

..
    :Purpose: The shelve module implements persistent storage for arbitrary Python objects which can be pickled, using a dictionary-like API.

:目的: shelve モジュールは、ディクショナリのような API で pickle 化できる任意の Python オブジェクトの永続ストレージを実装する

..
    The :mod:`shelve` module can be used as a simple persistent storage
    option for Python objects when a relational database is overkill. The
    shelf is accessed by keys, just as with a dictionary. The values are
    pickled and written to a database created and managed by
    :mod:`anydbm`.

:mod:`shelve` モジュールは、関係データベースだと行き過ぎなときに Python オブジェクトの簡単な永続ストレージの選択肢として使用できます。シェルフはちょうどディクショナリのようにキーでアクセスできます。その値は pickle 化されて :mod:`anydbm` が作成、管理するデータベースへ書き込まれます。

..
    ====================
    Creating a new Shelf
    ====================

========================
新たなシェルフを作成する
========================

..
    The simplest way to use shelve is via the :class:`DbfilenameShelf`
    class. It uses anydbm to store the data. You can use the class
    directly, or simply call :func:`shelve.open()`:

:mod:`shelve` を使用する最も簡単な方法は :class:`DbfilenameShelf` を経由することです。それはデータを格納するために :mod:`anydbm` を使用します。そのクラスを直接使用するか、単純に :func:`shelve.open()` を呼び出します。

.. include:: shelve_create.py
    :literal:
    :start-after: #end_pymotw_header

..
    To access the data again, open the shelf and use it like a dictionary:

再度データへアクセスするには、シェルフをオープンしてディクショナリのように使用します。

.. include:: shelve_existing.py
    :literal:
    :start-after: #end_pymotw_header

..
    If you run both sample scripts, you should see:

両方のサンプルスクリプトを実行すると次のようになります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'shelve_create.py', trailing_newlines=False))
.. cog.out(run_script(cog.inFile, 'shelve_existing.py', include_prefix=False))
.. }}}
.. {{{end}}}

..
    The :mod:`dbm` module does not support multiple applications writing to the same
    database at the same time. If you know your client will not be modifying the
    shelf, you can tell shelve to open the database read-only.

:mod:`dbm` モジュールは、複数のアプリケーションから同時に同じデータベースへ書き込むのをサポートしません。クライアントアプリケーションがシェルフを変更しないなら、そのデータベースを読み込み専用でオープンするようにシェルフへ伝えることができます。

.. include:: shelve_readonly.py
    :literal:
    :start-after: #end_pymotw_header

..
    If your program tries to modify the database while it is opened read-only, an
    access error exception is generated. The exception type depends on the
    database module selected by anydbm when the database was created.

読み込み専用でオープンされたデータベースを変更しようとする場合、アクセスエラー例外が発生します。その例外の種類は、データベースの作成時に :mod:`anydbm` が選択したデータベースモジュールで変わります。

..
    ==========
    Write-back
    ==========

========================
ライトバック(Write-back)
========================

..
    Shelves do not track modifications to volatile objects, by default. That means
    if you change the contents of an item stored in the shelf, you must update the
    shelf explicitly by storing the item again.

シェルフはデフォルトで volatile オブジェクトの変更を保存しません。シェルフに格納された要素のコンテンツを変更するなら、再度その要素を格納して明示的にそのシェルフを更新しなければなりません。

.. include:: shelve_withoutwriteback.py
    :literal:
    :start-after: #end_pymotw_header

..
    In this example, the dictionary at 'key1' is not stored again, so when the
    shelf is re-opened, the changes have not been preserved.

このサンプルでは、'key1' のディクショナリは再度、格納されていません。そのため、シェルフを再オープンするとその変更が保存されていません。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'shelve_create.py', trailing_newlines=False))
.. cog.out(run_script(cog.inFile, 'shelve_withoutwriteback.py', include_prefix=False))
.. }}}
.. {{{end}}}

..
    To automatically catch changes to volatile objects stored in the shelf, open
    the shelf with writeback enabled. The writeback flag causes the shelf to
    remember all of the objects retrieved from the database using an in-memory
    cache. Each cache object is also written back to the database when the shelf
    is closed. 

シェルフに格納された volatile オブジェクトに対する変更を自動的に捕捉するには、ライトバック(writeback)を有効にしてシェルフをオープンします。ライトバックフラグは、インメモリキャッシュでデータベースから取り出した全てのオブジェクトをシェルフに覚えさせます。また、それぞれのキャッシュオブジェクトは、シェルフがクローズされるときにデータベースへ書き込まれます。

.. include:: shelve_writeback.py
    :literal:
    :start-after: #end_pymotw_header

..
    Although it reduces the chance of programmer error, and can make object
    persistence more transparent, using writeback mode may not be desirable in
    every situation. The cache consumes extra memory while the shelf is open, and
    pausing to write every cached object back to the database when it is closed
    can take extra time. Since there is no way to tell if the cached objects have
    been modified, they are all written back. If your application reads data more
    than it writes, writeback will add more overhead than you might want.

これはプログラマによる人為的なエラーを減少させて、より透過的にオブジェクトを永続化させますが、ライトバックモードを使用することが全ての状況で望まれるわけではないかもしれません。キャッシュは、シェルフがオープンされている間、余分なメモリを消費します。そして、クローズされるときにキャッシュされたオブジェクトをデータベースへ書き込むために余分な時間がかかります。キャッシュされたオブジェクトが変更されたかを伝える方法がないので、そのキャッシュは全て書き込まれます。アプリケーションのデータが書き込みよりも読み込みが多い場合、ライトバックは想像以上にオーバーヘッドになるかもしれません。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'shelve_create.py', trailing_newlines=False))
.. cog.out(run_script(cog.inFile, 'shelve_writeback.py', include_prefix=False))
.. }}}
.. {{{end}}}


.. _shelve-shelf-types:

==============
特別なシェルフ
==============

..
    ====================
    Specific Shelf Types
    ====================

..
    The examples above all use the default shelf implementation. Using
    :func:`shelve.open()` instead of one of the shelf implementations
    directly is a common usage pattern, especially if you do not care what
    type of database is used to store the data. There are times, however,
    when you do care. In those situations, you may want to use
    :class:`DbfilenameShelf` or :class:`BsdDbShelf` directly, or even
    subclass :class:`Shelf` for a custom solution.

前節で紹介した全てのサンプルはデフォルトのシェルフの実装を使用します。シェルフ実装のデフォルトではなく :func:`shelve.open()` を使用するのは一般的な使用方法です。特にデータを格納するために使用されるデータベースを気にしない場合です。そうは言っても、気にするときもあります。そういった状況では :class:`DbfilenameShelf` か :class:`BsdDbShelf` を直接的に使用したり、もしくはカスタム目的で :class:`Shelf` をサブクラス化した方が良いかもしれません。

.. seealso::

    `shelve <http://docs.python.org/lib/module-shelve.html>`_
        .. Standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント

    :mod:`anydbm`
        .. The anydbm module.

        :mod:`anydbm` モジュール

    `feedcache <http://www.doughellmann.com/projects/feedcache/>`_
        .. The feedcache module uses shelve as a default storage option.

        デフォルトストレージオプションとして :mod:`shelve` を使用する feedcache モジュール

    `shove <http://pypi.python.org/pypi/shove/>`_
        .. Shove implements a similar API with more backend formats.

        バックエンドフォーマットでよく似た API を実装する shove モジュール

    :ref:`article-data-persistence`
        .. Other mechanisms for storing data using standard library modules.

        標準モジュールでデータを格納するその他の仕組み
