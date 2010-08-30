..
    ========================================================
    zlib -- Low-level access to GNU zlib compression library
    ========================================================

===================================================
zlib -- GNU zlib 圧縮ライブラリへの低レベルアクセス
===================================================

..
    :synopsis: Low-level access to GNU zlib compression library

.. module:: zlib
    :synopsis: GNU zlib 圧縮ライブラリへの低レベルアクセス

..
    :Purpose: Low-level access to GNU zlib compression library
    :Python Version: 2.5 and later

:目的: GNU zlib 圧縮ライブラリへの低レベルアクセス
:Python バージョン: 2.5 以上

..
    The :mod:`zlib` module provides a lower-level interface to many of the
    functions in the :mod:`zlib` compression library from GNU.

:mod:`zlib` モジュールは GNU :mod:`zlib` 圧縮ライブラリ関数群への低レベルなインタフェースを提供します。

..
    Working with Data in Memory
    ===========================

メモリ内のデータを扱う
======================

..
    The simplest way to work with :mod:`zlib` requires holding all of the
    data to be compressed or decompressed in memory, and then using
    :func:`compress()` and :func:`decompress()`.

:mod:`zlib` を使用する最も簡単な方法はメモリ内に全データを圧縮したり解凍したりするように要求することです。そうするには :func:`compress()` や :func:`decompress()` を使用します。

.. include:: zlib_memory.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'zlib_memory.py'))
.. }}}
.. {{{end}}}

..
    Notice that for short text, the compressed version can be longer.
    While the actual results depend on the input data, for short bits of
    text it is interesting to observe the compression overhead.

短いテキストを圧縮すると逆に長くなる可能性があることに注意してください。その実際の結果は入力値次第であるとはいえ、短いテキストで圧縮によるオーバヘッドを観察することはおもしろいです。

.. include:: zlib_lengths.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'zlib_lengths.py'))
.. }}}
.. {{{end}}}

..
    Working with Streams
    ====================

ストリームを扱う
================

..
    The in-memory approach has obvious drawbacks that make it impractical
    for real-world use cases.  The alternative is to use :class:`Compress`
    and :class:`Decompress` objects to manipulate streams of data, so that
    the entire data set does not have to fit into memory.

インメモリアプローチは現実の世界では実用的ではないという明らかな欠点があります。完全なデータセットをメモり内に読み込む必要がないように、代替手段としてデータのストリームを扱う :class:`Compress` と :class:`Decompress` オブジェクトを使用します。

..
    The simple server below responds to requests consisting of filenames
    by writing a compressed version of the file to the socket used to
    communicate with the client.  It has some artificial chunking in place
    to illustrate the buffering behavior that happens when the data passed
    to :func:`compress()` or :func:`decompress()` doesn't result in a
    complete block of compressed or uncompressed output.

次のシンプルサーバはファイル名を含むリクエストに対して、クライアントとの通信ソケットへそのファイルの圧縮版を書き込むことでレスポンスを返します。 :func:`compress()` 又は :func:`decompress()` へ渡されたデータに対して圧縮又は解凍した出力が完全なブロックではない場合に発生するバッファリングの動作を説明するために適当な位置に人為的なチャンクがあります。

..
    This server has obvious security implications.  Do not run it on a
    system on the open internet or in any environment where security
    might be an issue.

.. warning::

    このサーバは明らかにセキュリティに問題があります。インターネットやセキュリティが問題となる環境のシステムでこのサーバを実行してはいけません。

.. include:: zlib_server.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'zlib_server.py'))
.. }}}
.. {{{end}}}

..
    Mixed Content Streams
    =====================

混在したコンテキストストリーム
==============================

..
    The :class:`Decompress` class returned by :func:`decompressobj()` can
    also be used in situations where compressed and uncompressed data is
    mixed together.  After decompressing all of the data, the
    *unused_data* attribute contains any data not used.

:func:`decompressobj()` が返す :class:`Decompress` クラスは圧縮と非圧縮のデータが混在した状況でも使用することができます。そのデータを完全に解凍した後でその *unused_data* 属性に使用しなかったデータがあります。

.. include:: zlib_mixed.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'zlib_mixed.py'))
.. }}}
.. {{{end}}}

..
    Checksums
    =========

チェックサム
============

..
    In addition to compression and decompression functions, :mod:`zlib`
    includes two functions for computing checksums of data,
    :func:`adler32()` and :func:`crc32()`.  Neither checksum is billed as
    cryptographically secure, and they are only intended for use for data
    integrity verification.

圧縮や解凍の関数に加えて :mod:`zlib` はデータのチェックサムを算出するための :func:`adler32()` と :func:`crc32()` という2つの関数があります。チェックサムは暗号化によるセキュリティではなく、データの整合性検証の用途のみに使用されます。

..
    Both functions take the same arguments, a string of data and an
    optional value to be used as a starting point for the checksum.  They
    return a 32-bit signed integer value which can also be passed back on
    subsequent calls as a new starting point argument to produce a
    *running* checksum.

2つの関数は同じ引数を取ります。その引数はデータの文字列とそのチェックサムの開始地点として使用されるオプションの値です。その2つの関数は *実行* チェックサムを生成するために新たな開始地点として、その次に続く関数呼び出しへ渡すこともできる符号付き 32 bit 整数値を返します。

.. include:: zlib_checksums.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'zlib_checksums.py'))
.. }}}
.. {{{end}}}

..
    The Adler32 algorithm is said to be faster than a standard CRC, but I
    found it to be slower in my own tests.

Adler32 アルゴリズムは標準 CRC よりも速いと言われていますが、私のテストでは遅くなることを発見しました。

.. include:: zlib_checksum_tests.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'zlib_checksum_tests.py'))
.. }}}
.. {{{end}}}

..
    `zlib <http://docs.python.org/library/zlib.html>`_
        The standard library documentation for this module.
    :mod:`gzip`
        The gzip module includes a higher level (file-based) interface to the zlib library.
    http://www.zlib.net/
        Home page for zlib library.
    http://www.zlib.net/manual.html
        Complete zlib documentation.
    :mod:`bz2`
        The bz2 module provides a similar interface to the bzip2 compression library.

.. seealso::

    `zlib <http://docs.python.org/library/zlib.html>`_
        本モジュールの標準ライブラリドキュメント

    :mod:`gzip`
        gzip モジュールは zlib ライブラリに対する高レベル(ファイルベース)インタフェースを提供

    http://www.zlib.net/
        zlib ライブラリのホームページ

    http://www.zlib.net/manual.html
        完全な zlib ドキュメント

    :mod:`bz2`
        bz2 モジュールは bzip2 圧縮ライブラリに対するよく似たインタフェースを提供
