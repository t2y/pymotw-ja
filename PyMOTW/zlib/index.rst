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
    :Available In: 2.5 and later

:目的: GNU zlib 圧縮ライブラリへの低レベルアクセス
:利用できるバージョン: 2.5 以上

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

::

	$ python zlib_memory.py
	
	Original     : 26 This is the original text.
	Compressed   : 32 789c0bc9c82c5600a2928c5485fca2ccf4ccbcc41c8592d48a123d007f2f097e
	Decompressed : 26 This is the original text.

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

::

	$ python zlib_lengths.py
	
	      len(data)  len(compressed)
	---------------  ---------------
	              0                8 *
	             26               32 *
	             52               35 
	             78               35 
	            104               36 
	            130               36 
	            156               36 
	            182               36 
	            208               36 
	            234               36 
	            260               36 
	            286               36 
	            312               37 
	            338               37 
	            364               38 
	            390               38 
	            416               38 
	            442               38 
	            468               38 
	            494               38 

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

::

	$ python zlib_server.py
	
	Client: Contacting server on 127.0.0.1:56229
	Client: sending filename: "lorem.txt"
	Server: client asked for: "lorem.txt"
	Server: RAW "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Donec
	"
	Server: SENDING "7801"
	Server: RAW "egestas, enim et consectetuer ullamcorper, lectus ligula rutrum "
	Server: BUFFERING
	Client: READ "7801"
	Server: RAW "leo, a
	elementum elit tortor eu quam. Duis tincidunt nisi ut ant"
	Client: BUFFERING
	Server: BUFFERING
	Server: RAW "e. Nulla
	facilisi. Sed tristique eros eu libero. Pellentesque ve"
	Server: BUFFERING
	Server: RAW "l arcu. Vivamus
	purus orci, iaculis ac, suscipit sit amet, pulvi"
	Server: BUFFERING
	Server: RAW "nar eu,
	lacus. Praesent placerat tortor sed nisl. Nunc blandit d"
	Server: BUFFERING
	Server: RAW "iam egestas
	dui. Pellentesque habitant morbi tristique senectus "
	Server: BUFFERING
	Server: RAW "et netus et
	malesuada fames ac turpis egestas. Aliquam viverra f"
	Server: BUFFERING
	Server: RAW "ringilla
	leo. Nulla feugiat augue eleifend nulla. Vivamus mauris"
	Server: BUFFERING
	Server: RAW ". Vivamus sed
	mauris in nibh placerat egestas. Suspendisse poten"
	Server: BUFFERING
	Server: RAW "ti. Mauris massa. Ut
	eget velit auctor tortor blandit sollicitud"
	Server: BUFFERING
	Server: RAW "in. Suspendisse imperdiet
	justo.
	"
	Server: BUFFERING
	Server: FLUSHING "5592418edb300c45f73e050f60f80e05ba6c8b0245bb676426c382923c22e9f3f70bc94c1ac00b9b963eff7fe4b73ea4921e9e95f66e7d906b105789954a6f2e"
	Server: FLUSHING "25245206f1ae877ad17623318d8dbef62665919b78b0af244d2b49bc5e4a33aea58f43c64a06ad7432bda5318d8c819e267d255ec4a44a0b14a638451f784892"
	Client: READ "5592418edb300c45f73e050f60f80e05ba6c8b0245bb676426c382923c22e9f3f70bc94c1ac00b9b963eff7fe4b73ea4921e9e95f66e7d906b105789954a6f2e"
	Server: FLUSHING "de932b7aa53a85b6a27bb6a0a6ae94b0d94236fa31bb2c572e6aa86ff44b768aa11efa9e4232ba4f21d30b5e37fa2966e8243e7f9e62c4a3e4467ff4e49abe1c"
	Client: DECOMPRESSED "Lorem ipsum dolor sit amet, conse"
	Server: FLUSHING "39e0b18fa22b299784247159c913d90f587be239d24e6d3c6dae8be1ac437db038e4e94041067f467198826d9b765ba18b71dba1b62b23f29de1b227dcbff87b"
	Client: READ "25245206f1ae877ad17623318d8dbef62665919b78b0af244d2b49bc5e4a33aea58f43c64a06ad7432bda5318d8c819e267d255ec4a44a0b14a638451f784892"
	Server: FLUSHING "e38b065252ede3a2ffa5428f3b4d106f181022c652d9c49377a62b06387d53e4c0d43e3a6cf4c500052d4f3d650c1c1c18a84e7e18c403255d256f0aeb9cb709"
	Client: DECOMPRESSED "ctetuer adipiscing elit. Donec
	egestas, enim et consectetuer ullamcorper, lectus ligula rutrum leo, a
	elementum elit tortor eu"
	Server: FLUSHING "d044afd2607f72fe24459513909fdf480807b346da90f5f2f684f04888d9a41fd05277a1a3074821f2f7fbadcaeed0ff1d73a962ce666e6296b9098f85f8c0e6"
	Client: READ "de932b7aa53a85b6a27bb6a0a6ae94b0d94236fa31bb2c572e6aa86ff44b768aa11efa9e4232ba4f21d30b5e37fa2966e8243e7f9e62c4a3e4467ff4e49abe1c"
	Server: FLUSHING "dd4c8b46eeda5e45b562d776058dbfe9d1b7e51f6f370ea5"
	Client: DECOMPRESSED " quam. Duis tincidunt nisi ut ante. Nulla
	facilisi. Sed tristique eros eu libero. Pellentesque vel arcu. Vivamus
	p"
	Client: READ "39e0b18fa22b299784247159c913d90f587be239d24e6d3c6dae8be1ac437db038e4e94041067f467198826d9b765ba18b71dba1b62b23f29de1b227dcbff87b"
	Client: DECOMPRESSED "urus orci, iaculis ac, suscipit sit amet, pulvinar eu,
	lacus. Praesent placerat tortor sed nisl. Nunc blandit diam egestas
	dui. Pellentesque "
	Client: READ "e38b065252ede3a2ffa5428f3b4d106f181022c652d9c49377a62b06387d53e4c0d43e3a6cf4c500052d4f3d650c1c1c18a84e7e18c403255d256f0aeb9cb709"
	Client: DECOMPRESSED "habitant morbi tristique senectus et netus et
	malesuada fames ac turpis egestas. Aliquam viverra fringilla
	leo. Nulla feugiat aug"
	Client: READ "d044afd2607f72fe24459513909fdf480807b346da90f5f2f684f04888d9a41fd05277a1a3074821f2f7fbadcaeed0ff1d73a962ce666e6296b9098f85f8c0e6"
	Client: DECOMPRESSED "ue eleifend nulla. Vivamus mauris. Vivamus sed
	mauris in nibh placerat egestas. Suspendisse potenti. Mauris massa. Ut
	eget velit auctor tortor blandit s"
	Client: READ "dd4c8b46eeda5e45b562d776058dbfe9d1b7e51f6f370ea5"
	Client: DECOMPRESSED "ollicitudin. Suspendisse imperdiet
	justo.
	"
	Client: response matches file contents: True

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

::

	$ python zlib_mixed.py
	
	Decompressed matches lorem: True
	Unused data matches lorem : True

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

::

	$ python zlib_checksums.py
	
	Adler32:   1865879205
	       :    118955337
	CRC-32 :   1878123957
	       :  -1940264325

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

::

	$ python zlib_checksum_tests.py
	
	Adler32, separate:	1.07 usec/pass
	Adler32, running:	1.10 usec/pass
	CRC-32, separate:	9.78 usec/pass
	CRC-32, running:	9.73 usec/pass

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
