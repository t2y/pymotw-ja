.. _data-persistence:

..
    ================
    Data Persistence
    ================

==============
データの永続化
==============

..
    The standard library includes a variety of modules for persisting data.  The most common pattern for storing data from Python objects for reuse is to serialize them with :mod:`pickle` and then either write them directly to a file or store them using one of the many key-value pair database formats available with the *dbm* API.  If you don't care about the underlying dbm format, the best persistence interface is provided by :mod:`shelve`.  If you do care, you can use one of the other dbm-based modules directly.

標準ライブラリにはデータの永続化のために様々なモジュールがあります。再利用のために Python オブジェクトからデータを格納する最も一般的なパターンは :mod:`pickle` でシリアライズすることです。そして、そのデータをファイルへ直接的に書き込むか、 *dbm* API で利用できる多くの Key-Value 型のデータベースから1つを選択してそのデータを格納します。もし dbm フォーマットの下位層に関して考慮しないなら、 :mod:`shelve` が最も適切な永続化インタフェースを提供します。下位層を考慮するなら、直接的に他の dbm ベースのモジュールから選択できます。

.. toctree::
    :maxdepth: 1

    anydbm/index
    dbhash/index
    dbm/index
    dumbdbm/index
    gdbm/index
    pickle/index
    shelve/index
    whichdb/index
    sqlite3/index

..
    For serializing over the web, the :mod:`json` module may be a better choice since its format is more portable.

web 上でシリアライズするには、フォーマットの移植性の高さから :mod:`json` モジュールが最も良い選択です。

.. seealso::

    :ref:`article-data-persistence`
