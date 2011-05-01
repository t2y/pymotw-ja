..
    ==========================
     mmap -- Memory-map files
    ==========================

=============================
 mmap -- メモリマップファイル
=============================

..
    :synopsis: Memory-map files

.. module:: mmap
    :synopsis: メモリマップファイル

..
    :Purpose: Memory-map files instead of reading the contents directly.
    :Available In: 2.1 and later

:目的: 直接的なコンテンツ読み込みの代替となるメモリマップファイル
:利用できるバージョン: 2.1以上

..
    Memory-mapping a file uses the operating system virtual memory system
    to access the data on the filesystem directly, instead of using normal
    I/O functions.  Memory-mapping typically improves I/O performance
    because it does not involve a separate system call for each access and
    it does not require copying data between buffers -- the memory is
    accessed directly.

ファイルをメモリマッピングすることは、通常の I/O 関数の代わりに、直接ファイルシステム上のデータにアクセスするためにオペレーティングシステムの仮想的なメモリシステムを使用します。メモリマッピングは、アクセス毎に独立したシステムコールを呼び出さず、バッファ間でデータのコピーが必要ない(メモリに直接アクセスされる)ので一般的に I/O 性能が向上します。

..
    Memory-mapped files can be treated as mutable strings or file-like
    objects, depending on your need. A mapped file supports the expected
    file API methods, such as :func:`close`, :func:`flush`, :func:`read`,
    :func:`readline`, :func:`seek`, :func:`tell`, and :func:`write`. It
    also supports the string API, with features such as slicing and
    methods like :func:`find`.

メモリマップファイルは、あなたの必要性に応じて可変文字列、ファイルのようなオブジェクトとして扱うことができます。メモリマップファイルは :func:`close`, :func:`flush`, :func:`read`, :func:`readline`, :func:`seek`, :func:`tell` や :func:`write` のようなファイル API メソッドをサポートします。さらにスライシングや :func:`find` メソッドのような文字列 API もサポートします。

..
    All of the examples use the text file ``lorem.txt``, containing a bit
    of Lorem Ipsum. For reference, the text of the file is:

全てのサンプルは Lorem Ipsum を少し含む ``lorem.txt`` を使用します。参考までにテキストファイルは次になります。

.. include:: lorem.txt
    :literal:

.. note::
  ..
      There are differences in the arguments and behaviors for
      :func:`mmap` between Unix and Windows, which are not discussed
      below. For more details, refer to the standard library
      documentation.

  Unix と Windows では :func:`mmap` への引数とその振る舞いが違います。その違いについてはあまり説明しませんが、詳細はライブラリドキュメントを参照してください。

..
    Reading
    =======

読み込み
========

..
    Use the :func:`mmap` function to create a memory-mapped file.  The
    first argument is a file descriptor, either from the :func:`fileno`
    method of a :class:`file` object or from :func:`os.open`. The caller
    is responsible for opening the file before invoking :func:`mmap`, and
    closing it after it is no longer needed.

メモリマップファイルを作成するために :func:`mmap` 関数を使ってみましょう。最初の引数はファイルディスクリプタで :class:`file` オブジェクトの :func:`fileno` メソッドか、又は :func:`os.open` が返すファイルオブジェクトになります。 :func:`mmap` を呼び出す前にファイルをオープンすると、不要になったときにそのファイルをクローズする責任があることに注意してください。

..
    The second argument to :func:`mmap` is a size in bytes for the portion
    of the file to map. If the value is ``0``, the entire file is
    mapped. If the size is larger than the current size of the file, the
    file is extended.

:func:`mmap` への2番目の引数はマッピングするファイルのバイトサイズになります。もし2番目の引数に渡す値が ``0`` なら、ファイル全体がマッピングされます。もし2番目の引数のサイズがオープンするファイルのファイルサイズよりも大きい場合、そのファイルは拡張されます。

.. note::
  ..
      You cannot create a zero-length mapping under Windows. 

  Windows ではファイルサイズがゼロのマッピングを作成することはできません。

..
    An optional keyword argument, *access*, is supported by both
    platforms. Use :const:`ACCESS_READ` for read-only access,
    :const:`ACCESS_WRITE` for write-through (assignments to the memory go
    directly to the file), or :const:`ACCESS_COPY` for copy-on-write
    (assignments to memory are not written to the file).

オプションのキーワード引数である *access* は、両方のプラットホームに対応しています。read-only には :const:`ACCESS_READ` を、write-through (直接ファイルへ書き込まれるようにメモリを割り当てる)には :const:`ACCESS_WRITE` を、copy-on-write (ファイルへ書き込まれないようにメモリを割り当てる)には const:`ACCESS_COPY` を使用してください。

.. include:: mmap_read.py
    :literal:
    :start-after: #end_pymotw_header

..
    The file pointer tracks the last byte accessed through a slice
    operation.  In this example, the pointer moves ahead 10 bytes after
    the first read.  It is then reset to the beginning of the file by the
    slice operation, and moved ahead 10 bytes again by the slice.  After
    the slice operation, calling :func:`read` again gives the bytes 11-20
    in the file.

ファイルポインタはスライシング操作によってアクセスされた最後のバイト位置を追跡します。このサンプルでは、最初の読み込みの後、そのポインタが10バイト前に進みます。それからスライシング操作によりファイルの先頭にリセットされて、再度スライスされて10バイト前に進みます。スライシング操作の後、再度 :func:`read` を呼び出すとファイルの11-20バイトの部分を読み込みます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'mmap_read.py'))
.. }}}
.. {{{end}}}

..
    Writing
    =======

書き込み
========

..
    To set up the memory mapped file to receive updates, start by opening
    it for appending with mode ``'r+'`` (not ``'w'``) before mapping
    it. Then use any of the API method that change the data
    (:func:`write`, assignment to a slice, etc.).

更新を受け取るようにメモリマップファイルを設定するために、そのファイルをマッピングする前に読み書きモード ``'r+'`` (``'w'`` ではない) でオープンしてください。それから、そのデータを変更する様々な API メソッド(:func:`write` やスライスの割当等)を使用してください。

..
    Here's an example using the default access mode of
    :const:`ACCESS_WRITE` and assigning to a slice to modify part of a
    line in place:

:const:`ACCESS_WRITE` のデフォルトアクセスモードを使用して、ある行の一部を変更するスライスを割り当てる例があります。

.. include:: mmap_write_slice.py
    :literal:
    :start-after: #end_pymotw_header

..
    The word "consectetuer" is replaced in the middle of the first line:

単語 "consectetuer" は最初の行の中間で置換されました。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'mmap_write_slice.py'))
.. }}}
.. {{{end}}}

..
    ACCESS_COPY Mode
    ----------------

ACCESS_COPY モード
------------------

..
    Using the access setting :const:`ACCESS_COPY` does not write changes
    to the file on disk

ディスク上のファイルに変更を書き込まないようにするには :const:`ACCESS_COPY` モードを使用してください。

.. include:: mmap_write_copy.py
    :literal:
    :start-after: #end_pymotw_header

..
    It is necessary to rewind the file handle in this example separately
    from the mmap handle because the internal state of the two objects is
    maintained separately.

このサンプルでは、mmap ハンドラとは別にファイルハンドラを巻き戻す必要があります。それは2つのオブジェクトの内部状態が独立して保持されるからです。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'mmap_write_copy.py'))
.. }}}
.. {{{end}}}

..
    Regular Expressions
    ===================

正規表現
========

..
    Since a memory mapped file can act like a string, it can be used with
    other modules that operate on strings, such as regular
    expressions. This example finds all of the sentences with "nulla" in
    them.

メモリマップファイルは文字列のように動作するので、正規表現などの文字列を操作する他のモジュールと一緒に使用できます。この例は "nulla" を含む全ての文を見つけます。

.. include:: mmap_regex.py
    :literal:
    :start-after: #end_pymotw_header

..
    Because the pattern includes two groups, the return value from
    :func:`findall` is a sequence of tuples. The :command:`print`
    statement pulls out the sentence match and replaces newlines with
    spaces so the result prints on a single line.

正規表現でマッチさせる2つのグループを含むパターンなので :func:`findall` からの戻り値はタプルのシーケンスになります。 :command:`print` 文は改行をスペースに置換した match の文を取り出して、その結果を1行で表示します。


.. {{{cog
.. cog.out(run_script(cog.inFile, 'mmap_regex.py'))
.. }}}
.. {{{end}}}


.. seealso::

    `mmap <http://docs.python.org/lib/module-mmap.html>`_
        .. Standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント

    :mod:`os`
        .. The os module.

        os モジュール

    :mod:`contextlib`
        .. Use the :func:`closing` function to create a context manager
           for a memory mapped file.

        メモリマップファイルのコンテキストマネージャを作成するには :func:`closing` 関数を使用してください

    :mod:`re`
        .. Regular expressions.

        正規表現
