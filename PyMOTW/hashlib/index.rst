..
    ===================================================
    hashlib -- Cryptographic hashes and message digests
    ===================================================

===============================================
hashlib -- 暗号ハッシュとメッセージダイジェスト
===============================================

..
    :synopsis: Cryptographic hashes and message digests

.. module:: hashlib
    :synopsis: 暗号ハッシュとメッセージダイジェスト

..
    :Purpose: Cryptographic hashes and message digests
    :Available In: 2.5

:目的: 暗号ハッシュとメッセージダイジェスト
:利用できるバージョン: 2.5

..
    The :mod:`hashlib` module deprecates the separate :mod:`md5` and
    :mod:`sha` modules and makes their API consistent. To work with a
    specific hash algorithm, use the appropriate constructor function to
    create a hash object. Then you can use the same API to interact with
    the hash no matter what algorithm is being used.

:mod:`hashlib` モジュールは独立した :mod:`md5` と :mod:`sha` モジュールを廃止して、一貫した API を提供します。特定のハッシュアルゴリズムと連携するには、ハッシュオブジェクトを作成する適切なコンストラクタ関数を使用してください。その後は、どのアルゴリズムが使用されても同じ API でハッシュと対話的にやり取りできます。

..
    Since :mod:`hashlib` is "backed" by OpenSSL, all of of the algorithms
    provided by that library are available, including:

:mod:`hashlib` は内部で OpenSSL を使用するので OpenSSL が提供する次のような全てのアルゴリズムが利用可能です。

 * md5
 * sha1
 * sha224
 * sha256
 * sha384
 * sha512

..
    Sample Data
    ===========

サンプルデータ
==============

..
    All of the examples below use the same sample data:

全てのサンプルは次のサンプルデータを使用します。

.. include:: hashlib_data.py
    :literal:
    :start-after: #end_pymotw_header

..
    MD5 Example
    ===========

MD5 サンプル
============

..
    To calculate the MD5 digest for a block of data (here an ASCII
    string), create the hash object, add the data, and compute the digest.

あるデータブロック(ここでは ASCII 文字列)の MD5 ダイジェストを算出するには、ハッシュオブジェクトを作成して、そのデータを追加して、そのダイジェストを計算します。

.. include:: hashlib_md5.py
    :literal:
    :start-after: #end_pymotw_header

..
    This example uses the :func:`hexdigest()` method instead of
    :func:`digest()` because the output is formatted to be printed. If a
    binary digest value is acceptable, you can use :func:`digest()`.

このサンプルは :func:`digest()` の代わりに :func:`hexdigest()` メソッドを使用します。その理由はその出力が表示できるように整形されるからです。もしバイナリダイジェストが許容されるなら :func:`digest()` を使用できます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'hashlib_md5.py'))
.. }}}

::

	$ python hashlib_md5.py
	
	c3abe541f361b1bfbbcfecbf53aad1fb

.. {{{end}}}

..
    SHA1 Example
    ============

SHA1 サンプル
=============

..
    A SHA1 digest for the same data would be calculated in much the same way.

同じデータの SAH1 ダイジェストはほとんど同じ方法で計算されます。

.. include:: hashlib_sha1.py
    :literal:
    :start-after: #end_pymotw_header

..
    The digest value is different in this example because we changed the
    algorithm from MD5 to SHA1

アルゴリズムを MD5 から SHA1 に変更したので、このサンプルのダイジェストの値は違っています。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'hashlib_sha1.py'))
.. }}}

::

	$ python hashlib_sha1.py
	
	ac2a96a4237886637d5352d606d7a7b6d7ad2f29

.. {{{end}}}


new()
=====

..
    Sometimes it is more convenient to refer to the algorithm by name in a
    string rather than by using the constructor function directly. It is
    useful, for example, to be able to store the hash type in a
    configuration file. In those cases, use :func:`new()` to create a hash
    calculator.

コンストラクタ関数を直接使用するよりも名前でアルゴリズムを参照する方が便利なときがあります。例えば、設定ファイルにハッシュの種別を保存できると便利です。そういった場合は、ハッシュ算出機を作成するために :func:`new()` を使用してください。

.. include:: hashlib_new.py
    :literal:
    :start-after: #end_pymotw_header

..
    When run with a variety of arguments:

様々な引数で実行します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'hashlib_new.py sha1'))
.. cog.out(run_script(cog.inFile, 'hashlib_new.py sha256', include_prefix=False))
.. cog.out(run_script(cog.inFile, 'hashlib_new.py sha512', include_prefix=False))
.. cog.out(run_script(cog.inFile, 'hashlib_new.py md5', include_prefix=False))
.. }}}

::

	$ python hashlib_new.py sha1
	
	ac2a96a4237886637d5352d606d7a7b6d7ad2f29

	$ python hashlib_new.py sha256
	
	88b7404fc192fcdb9bb1dba1ad118aa1ccd580e9faa110d12b4d63988cf20332

	$ python hashlib_new.py sha512
	
	f58c6935ef9d5a94d296207ee4a7d9bba411539d8677482b7e9d60e4b7137f68d25f9747cab62fe752ec5ed1e5b2fa4cdbc8c9203267f995a5d17e4408dccdb4

	$ python hashlib_new.py md5
	
	c3abe541f361b1bfbbcfecbf53aad1fb

.. {{{end}}}

..
    Calling update() more than once
    ===============================

1度以上 update() を呼び出す
===========================

..
    The :func:`update()` method of the hash calculators can be called
    repeatedly. Each time, the digest is updated based on the additional
    text fed in. This can be much more efficient than reading an entire
    file into memory, for example.

ハッシュ計算機の :func:`update()` メソッドは何度も呼び出すことができます。毎回、テキストを追加して与えることでダイジェストを更新します。例えば、これはメモリにファイル全体を読み込むよりもずっと効率的です。

.. include:: hashlib_update.py
    :literal:
    :start-after: #end_pymotw_header

..
    This example is a little contrived because it works with such a small amount
    of text, but it illustrates how you could incrementally update a digest as
    data is read or otherwise produced.

このサンプルはサイズの小さいテキストを処理するので少し不自然な気がします。しかし、データが読み込まれる、もしくは別の方法で生成されるようにダイジェストを徐々に更新する方法を説明します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'hashlib_update.py'))
.. }}}

::

	$ python hashlib_update.py
	
	All at once : c3abe541f361b1bfbbcfecbf53aad1fb
	Line by line: c3abe541f361b1bfbbcfecbf53aad1fb
	Same        : True

.. {{{end}}}

.. seealso::

    `hashlib <http://docs.python.org/library/hashlib.html>`_
        .. The standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント

    `Voidspace: IronPython and hashlib <http://www.voidspace.org.uk/python/weblog/arch_d7_2006_10_07.shtml#e497>`_
        .. A wrapper for :mod:`hashlib` that works with IronPython.

        IronPython で動作する :mod:`hashlib` のラッパー

    :mod:`hmac`
        .. The :mod:`hmac` module.

        :mod:`hmac` モジュール
