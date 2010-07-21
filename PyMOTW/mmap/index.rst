..
    ==================================================================
    mmap -- Memory-map files instead of reading the contents directly.
    ==================================================================

==================================================================
mmap -- 直接的なコンテンツ読み込みの代替となるメモリマップファイル
==================================================================

..
    :synopsis: Memory-map files instead of reading the contents directly.

.. module:: mmap
    :synopsis: 直接的なコンテンツ読み込みの代替となるメモリマップファイル

..
    :Purpose: Memory-map files instead of reading the contents directly.
    :Python Version: 2.1 and later

:目的: 直接的なコンテンツ読み込みの代替となるメモリマップファイル
:Python バージョン: 2.1以上

..
    Use the ``mmap()`` function to create a memory-mapped file. There are differences
    in the arguments and behaviors for ``mmap()`` between Unix and Windows, which are
    not discussed below. For more details, refer to the library documentation.

メモリマップファイルを作成するために ``mmap()`` 関数を使ってみましょう。Unix と Windows では ``mmap()`` への引数とその動作に違いがあります。その違いについてはあまり議論されていませんが、次の通りです。詳細についてはライブラリドキュメントを参照してください。

..
    The first argument is a fileno, either from the ``fileno()`` method of a file
    object or from ``os.open()``. Since you have opened the file before calling
    ``mmap()``, you are responsible for closing it.

最初の引数 fileno は、ファイルオブジェクトの ``fileno()`` メソッドか、又は ``os.open()`` が返すファイルオブジェクトになります。 ``mmap()`` を呼び出す前にファイルを開くと、そのファイルを閉じる責任があることに注意してください。

..
    The second argument to ``mmap()`` is a size in bytes for the portion of the file
    to map. If the value is 0, the entire file is mapped. You cannot create a
    zero-length mapping under Windows. If the size is larger than the current size
    of the file, the file is extended.

``mmap()`` への2番目の引数はマッピングするファイルのバイトサイズになります。もし2番目の引数に渡す値がゼロなら、ファイル全体がマッピングされます。Windows ではファイルサイズがゼロのマッピングを作成することはできません。また、2番目の引数のサイズが開こうとしているファイルのファイルサイズよりも大きい場合、そのファイルは拡張されます。

..
    An optional keyword argument, access, is supported by both platforms. Use
    ACCESS_READ for read-only access, ACCESS_WRITE for write-through (assignments
    to the memory go directly to the file), or ACCESS_COPY for copy-on-write
    (assignments to memory are not written to the file).

オプションのキーワード引数である access は、両方のプラットホームに対応しています。read-only には ACCESS_READ を、write-through (直接ファイルへ書き込まれるようにメモリを割り当てる)には ACCESS_WRITE を、copy-on-write (ファイルへ書き込まれないようにメモリを割り当てる)には ACCESS_COPY を使用してください。

..
    File and String API
    ===================

ファイルと文字列 API
====================

..
    Memory-mapped files can be treated as mutable strings or file-like objects,
    depending on your need. A mapped file supports the expected file API methods,
    such as close(), flush(), read(), readline(), seek(), tell(), and write(). It
    also supports the string API, with features such as slicing and methods like
    find().

メモリマップファイルはファイルのようなオブジェクトか、変更可能な文字列として必要に応じて扱うことができます。1つのマップファイルは、 close(), flush(), read(), readline(), seek(), tell() と write() のように、容易に予想されるファイル API メソッドに対応します。また、スライシングや find() メソッドのような機能を持つ文字列 API にも対応します。

..
    Sample Data
    ===========

サンプルデータ
==============

..
    All of the examples use the text file lorem.txt, containing a bit of Lorem
    Ipsum. For reference, the text of the file is:

全ての例はロレム・イプサムを含む小さなテキストファイル lorem.txt を使用します。参考までにそのファイルのテキストは次の通りです。

.. include:: lorem.txt
    :literal:

..
    Reading
    =======

読み込み
========

..
    To map a file for read-only access, make sure to pass ``access=mmap.ACCESS_READ``:

read-only アクセスのためにファイルをマッピングするには ``access=mmap.ACCESS_READ`` を引数に渡してください。

.. include:: mmap_read.py
    :literal:
    :start-after: #end_pymotw_header

..
    In this example, even though the call to ``read()`` advances the file pointer, the
    slice operation still gives us the same first 10 bytes because the file
    pointer is reset. The file pointer tracks the last access, so after using the
    slice operation to give us the first 10 bytes for the second time, calling
    read gives the next 10 bytes in the file.

この例ではファイルポインタを前に進める ``read()`` を呼び出したとしても、そのファイルポインタはリセットされるのでスライシング操作は同じ最初の10バイトを返します。そのファイルポインタは最後のアクセスを追跡していて、2回目に呼び出すために最初の10バイトを返すスライシング操作を行った後で ``read()`` を呼び出すとそのファイルの次の10バイトを返します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'mmap_read.py'))
.. }}}

::

	$ python mmap_read.py
	First 10 bytes via read : Lorem ipsu
	First 10 bytes via slice: Lorem ipsu
	2nd   10 bytes via read : m dolor si

.. {{{end}}}

..
    Writing
    =======

書き込み
========

..
    If you need to write to the memory mapped file, start by opening it for
    reading and appending (not with 'w', but 'r+') before mapping it. Then use any
    of the API method which change the data (write(), assignment to a slice,
    etc.).

メモリマップファイルへ書き込む必要がある場合、そのファイルをマッピングする前に読み書きモード('w' ではなく 'r+' )でそのメモリマップファイルを開いてください。それから、そのデータを変更する様々な API メソッド(write() やスライスの割当等)を使用してください。

..
    Here's an example using the default access mode of ACCESS_WRITE and assigning
    to a slice to modify part of a line in place:

ACCESS_WRITE のデフォルトアクセスモードを使用して、ある行の一部を変更するスライスを割り当てる例があります。

.. include:: mmap_write_slice.py
    :literal:
    :start-after: #end_pymotw_header

..
    As you can see here, the word shown in bold is replaced in the middle of the
    first line:

ご覧の通り、最初の行の中間にある単語が置換されました。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'mmap_write_slice.py'))
.. }}}

::

	$ python mmap_write_slice.py
	Looking for    : consectetuer
	Replacing with : reutetcesnoc
	Before: Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Donec
	After : Lorem ipsum dolor sit amet, reutetcesnoc adipiscing elit. Donec

.. {{{end}}}

..
    ACCESS_COPY Mode
    ================

ACCESS_COPY モード
==================

..
    Using the ACCESS_COPY mode does not write changes to the file on disk. 

ディスク上のファイルに変更を書き込まないようにするには ACCESS_COPY モードを使用してください。

.. include:: mmap_write_copy.py
    :literal:
    :start-after: #end_pymotw_header

..
    Note, in this example, that it was necessary to rewind the file handle
    separately from the mmap handle.

この例では mmap ハンドラとは別にファイルハンドラを巻き戻す必要があることに注意してください。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'mmap_write_copy.py'))
.. }}}

::

	$ python mmap_write_copy.py
	Memory Before: Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Donec
	File Before  : Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Donec
	
	Memory After : Lorem ipsum dolor sit amet, reutetcesnoc adipiscing elit. Donec
	File After   : Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Donec

.. {{{end}}}

..
    Regular Expressions
    ===================

正規表現
========

..
    Since a memory mapped file can act like a string, you can use it with other
    modules that operate on strings, such as regular expressions. This example
    finds all of the sentences with "nulla" in them.

メモリマップファイルは文字列のように動作するので、正規表現などの文字列を操作する他のモジュールと一緒に使用できます。この例は "nulla" を含む全ての文を見つけます。

.. include:: mmap_regex.py
    :literal:
    :start-after: #end_pymotw_header

..
    Since the pattern includes two groups, the return value from findall() is a
    sequence of tuples. The print statement pulls out the sentence match and
    replaces newlines with spaces so the result prints on a single line.

正規表現でマッチさせる2つのグループを含むパターンなので、findall() からの戻り値はタプルのシーケンスになります。print 文は改行をスペースに置換した match の文を取り出して、その結果を1行で表示します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'mmap_regex.py'))
.. }}}

::

	$ python mmap_regex.py
	Nulla facilisi.
	Nulla feugiat augue eleifend nulla.

.. {{{end}}}

..
    `mmap <http://docs.python.org/lib/module-mmap.html>`_
        Standard library documentation for this module.
    :mod:`os`
        The os module.

.. seealso::

    `mmap <http://docs.python.org/lib/module-mmap.html>`_
        本モジュールの標準ライブラリドキュメント

    :mod:`os`
        os モジュール
