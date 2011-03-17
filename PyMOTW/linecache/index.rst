..
    ========================================
    linecache -- Read text files efficiently
    ========================================

===============================================
linecache -- テキストファイルを効率的に読み込む
===============================================

..
    :synopsis: Retrieve lines of text from files or imported python modules, holding a cache of the results to make reading many lines from the same file more efficient.

.. module:: linecache
    :synopsis: ファイルまたはインポートされた Python モジュールからテキストの行を取り出して、同じファイルから効率的に多くの行を読み込むキャッシュを保持する

..
    :Purpose: Retrieve lines of text from files or imported python modules, holding a cache of the results to make reading many lines from the same file more efficient.
    :Python Version: 1.4

:目的: ファイルまたはインポートされた Python モジュールからテキストの行を取り出して、同じファイルから効率的に多くの行を読み込むキャッシュを保持する
:Python バージョン: 1.4

..
    The linecache module is used extensively throughout the Python standard
    library when dealing with Python source files. The implementation of the cache
    simply holds the contents of files, parsed into separate lines, in a
    dictionary in memory. The API returns the requested line(s) by indexing into a
    list. The time savings is from (repeatedly) reading the file and parsing lines
    to find the one desired. This is especially useful when looking for multiple
    lines from the same file, such as when producing a traceback for an error
    report.

:mod:`linecache` モジュールは、Python のソースファイルを扱うときに Python 標準ライブラリ全体で広く使用されています。そのキャッシュの実装は、メモリ内のディクショナリへ解析した行単位で、単純にファイルのコンテンツを保持します。その API はリストにインデクシングすることで要求された行を返します。これにより、ファイルを(何回も)読み込んでから、必要な部分を見つけるために行を解析する時間を節約します。特にエラーリポートのためにトレースバック情報を生成するようなときに、同じファイルから複数行を探すと便利です。

..
    Test Data
    =========

テストデータ
============

..
    We will use some text produced by the Lorem Ipsum generator as sample input.

サンプルの入力として、ロレイムイプサム生成機で作成したテキストを使用します。

.. include:: linecache_data.py
    :literal:
    :start-after: #end_pymotw_header

..
    Reading Specific Lines
    ======================

特定の行を読み込む
==================

..
    Reading the 5th line from the file is a simple one-liner.
    Notice that the line numbers in the linecache module start with 1, but if we
    split the string ourselves we start indexing the array from 0. We also need to
    strip the trailing newline from the value returned from the cache.

ファイルから5行目を読み込むには1行のコードで済みます。 :mod:`linecache` モジュールの行番号は 1 から始まりますが、もしそのオリジナルの文字列を :func:`split` するなら、その配列に 0 からインデクシングされることに注意してください。さらにキャッシュから返される値から行末の改行を取り除く必要もあります。

.. include:: linecache_getline.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'linecache_getline.py'))
.. }}}
.. {{{end}}}

..
    Handling Blank Lines
    ====================

空行の扱い
==========

..
    Next let's see what happens if the line we want is empty:

次に空行だったときに何が起こるかを見てみましょう。

.. include:: linecache_empty_line.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'linecache_empty_line.py'))
.. }}}
.. {{{end}}}

..
    Error Handling
    ==============

エラー制御
==========

..
    If the requested line number falls out of the range of valid lines in the
    file, linecache returns an empty string. 

要求された行がファイルの有効な行範囲になかった場合、 :mod:`linecache` は空行を返します。

.. include:: linecache_out_of_range.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'linecache_out_of_range.py'))
.. }}}
.. {{{end}}}

..
    The module never raises an exception, even if the file does not exist:

そのファイルが存在していなかったとしても :mod:`linecache` モジュールは決して例外を発生させません。

.. include:: linecache_missing_file.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'linecache_missing_file.py'))
.. }}}
.. {{{end}}}

..
    Python Source
    =============

Python のソースファイル
=======================

..
    Since :mod:`linecache` is used so heavily when producing tracebacks,
    one of the key features is the ability to find Python source modules
    in the :ref:`import path <sys-path>` by specifying the base name of
    the module. The cache population code in :mod:`linecache` searches
    ``sys.path`` for the module if it cannot find the file directly.

:mod:`linecache` はトレースバック情報を生成するときによく使用されるので、目玉機能の1つは、モジュールの名前を指定して :ref:`import path <sys-path>` から Python のソースモジュールを見つける機能です。 :mod:`linecache` のキャッシュ生成コードは、直接的にそのファイルを見つけられなかったときに ``sys.path`` からそのモジュールを探します。

.. include:: linecache_path_search.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'linecache_path_search.py'))
.. }}}
.. {{{end}}}
    
.. seealso::

    `linecache <http://docs.python.org/library/linecache.html>`_
        .. The standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント

    http://www.ipsum.com/
        .. Lorem Ipsum generator.

        ロレイムイプサム生成機

    :ref:`article-file-access`
        .. Other tools for working with files.

        ファイルと連携するその他のツール
