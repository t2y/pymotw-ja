..
    ====================================
    dircache -- Cache directory listings
    ====================================

==============================================
dircache -- ディレクトリの内容をキャッシュする
==============================================

..
    :synopsis: Cache directory listings

.. module:: dircache
    :synopsis: ディレクトリ内容をキャッシュする

..
    :Purpose: Cache directory listings, updating when the modification time of a directory changes.
    :Available In: 1.4 and later

:目的: ディレクトリの内容をキャッシュして、そのディレクトリの変更時に更新する
:利用できるバージョン: 1.4 以上

..
    Listing Directory Contents
    ==========================

ディレクトリの内容を表示する
============================

..
    The main function in the :mod:`dircache` API is :func:`listdir`, a
    wrapper around :func:`os.listdir` that caches the results and returns
    the same :class:`list` each time it is called with a given path, unless the
    modification date of the named directory changes.

:mod:`dircache` モジュール API の 主な関数は、 :func:`os.listdir` のラッパーである :func:`listdir` です。それは名前を持つディレクトリの更新時刻が変更されない限り、渡されたパスで呼び出される度にその結果をキャッシュして同じ :class:`list` を返します。

.. include:: dircache_listdir.py
    :literal:
    :start-after: #end_pymotw_header

..
    It is important to recognize that the exact same :class:`list` is
    returned each time, so it should not be modified in place.

毎回、厳密に同じ :class:`list` が返されるので、その対象ディレクトリが変更されていないことを認識するのが重要です。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'dircache_listdir.py'))
.. }}}
.. {{{end}}}

..
    If the contents of the directory changes, it is rescanned.

ディレクトリのコンテンツが変更される場合、再スキャンされます。

.. include:: dircache_listdir_file_added.py
    :literal:
    :start-after: #end_pymotw_header

..
    In this case the new file causes a new :class:`list` to be
    constructed.

このケースでは :class:`list` に新しいファイルが作成されます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'dircache_listdir_file_added.py'))
.. }}}
.. {{{end}}}

..
    It is also possible to reset the entire cache, discarding its contents so that
    each path will be rechecked.

それぞれのパスを再チェックするためにそのコンテンツを破棄して、完全にキャッシュをリセットすることもできます。

.. include:: dircache_reset.py
    :literal:
    :start-after: #end_pymotw_header

..
    After resetting, a new :class:`list` instance is returned.

リセットされた後で新たな :class:`list` インスタンスが返されます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'dircache_reset.py'))
.. }}}
.. {{{end}}}

..
    Annotated Listings
    ==================

自動的な表示
============

..
    The other interesting function provided by the dircache module is
    :func:`annotate`.  When called, :func:`annotate` modifies a
    :func:`list` such as is returned by :func:`listdir`, adding a ``'/'``
    to the end of the names that represent directories. 

:mod:`dircache` モジュールで提供されるその他の興味深い関数は :func:`annotate` です。 :func:`annotate` が呼び出されると、 :func:`listdir` が返すようにディレクトリ名の最後に ``'/'`` を追加して :func:`list` を変更します。

.. include:: dircache_annotate.py
    :literal:
    :start-after: #end_pymotw_header

..
    Unfortunately for Windows users, although :func:`annotate` uses
    :func:`os.path.join` to construct names to test, it always appends a
    ``'/'``, not :data:`os.sep`.

Windows ユーザには不幸なことに、 :func:`annotate` が調べる名前を作るために :func:`os.path.join` を使用しますが、 :data:`os.sep` ではなく必ず ``'/'`` を追加します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'dircache_annotate.py'))
.. }}}
.. {{{end}}}

.. seealso::

    `dircache <http://docs.python.org/library/dircache.html>`_
        .. The standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント
