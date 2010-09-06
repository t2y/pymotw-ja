..
    ==================================================
    tempfile -- Create temporary filesystem resources.
    ==================================================

======================================================
tempfile -- 一時的なファイルシステムリソースを作成する
======================================================

..
    :synopsis: Create temporary filesystem resources.

.. module:: tempfile
    :synopsis: 一時的なファイルシステムリソースを作成する

..
    :Purpose: Create temporary filesystem resources.
    :Python Version: Since 1.4 with major security revisions in 2.3

:目的: 一時的なファイルシステムリソースを作成する
:Python バージョン: 1.4 以上、2.3 で主要なセキュリティ修正が施された

..
    Many programs need to create files to write intermediate
    data. Creating files with unique names securely, so they cannot be
    guessed by someone wanting to break the application, is
    challenging. The :mod:`tempfile` module provides several functions for
    creating filesystem resources securely. :func:`TemporaryFile()` opens
    and returns an un-named file, :func:`NamedTemporaryFile()` opens and
    returns a named file, and :func:`mkdtemp()` creates a temporary
    directory and returns its name.

多くのプログラムで中間データを書き出すためにファイルを作成する必要性に迫られます。アプリケーションを壊したい攻撃者に推測されないように、セキュアでユニークな名前のファイルを作成することはプログラマの手腕を問われるところです。 :mod:`tempfile` モジュールはセキュアなファイルシステムリソースを作成するための機能を提供します。 :func:`TemporaryFile()` は無名ファイルをオープンして返します。 :func:`NamedTemporaryFile()` は名前のあるファイルをオープンして返します。 :func:`mkdtemp()` は一時的なディレクトリを作成してその名前を返します。

TemporaryFile
=============

..
    If your application needs a temporary file to store data, but does not
    need to share that file with other programs, the best option for
    creating the file is the :func:`TemporaryFile()` function. It creates
    a file, and on platforms where it is possible, unlinks it
    immediately. This makes it impossible for another program to find or
    open the file, since there is no reference to it in the filesystem
    table. The file created by :func:`TemporaryFile()` is removed
    automatically when it is closed.

あるアプリケーションがデータを保存するために一時的なファイルが必要な場合でも、その一時ファイルを他のプログラムと共有する必要はありません。一時ファイルを作成するために最適な選択は :func:`TemporaryFile()` 関数です。その関数はプラットホーム上にファイルを作成して即座にアンリンクします。ファイルシステムテーブルにそのファイルへの参照先がないため、他のプログラムがそのファイルをオープンしたり見つけたりすることは不可能です。 :func:`TemporaryFile()` が作成したファイルは、そのファイルを閉じるときに自動的に削除されます。

.. include:: tempfile_TemporaryFile.py
    :literal:
    :start-after: #end_pymotw_header

..
    This example illustrates the difference in creating a temporary file
    using a common pattern for making up a name, versus using the
    :func:`TemporaryFile()` function. Notice that the file returned by
    :func:`TemporaryFile` has no name.

この例は名前生成に一般的パターンを使用するのと :func:`TemporaryFile()` 関数を使用するのを比較して、一時ファイルを作成することの違いを表しています。 :func:`TemporaryFile` が返すファイルには名前がないことに注目してください。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'tempfile_TemporaryFile.py'))
.. }}}
.. {{{end}}}

..
    By default, the file handle is created with mode ``'w+b'`` so it
    behaves consistently on all platforms and your program can write to it
    and read from it.

デフォルトで一時ファイルは ``'w+b'`` モードで作成されます。そのため、全てのプラットホーム上で一貫して動作して、その一時ファイルに読み書きすることができます。

.. include:: tempfile_TemporaryFile_binary.py
    :literal:
    :start-after: #end_pymotw_header

..
    After writing, you have to rewind the file handle using :func:`seek()`
    in order to read the data back from it.

書き込み後、その一時ファイルからデータを読み込むために :func:`seek()` を使用してファイル位置を巻き戻す必要があります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'tempfile_TemporaryFile_binary.py'))
.. }}}
.. {{{end}}}

..
    If you want the file to work in text mode, set *mode* to ``'w+t'``
    when you create it:

もしその一時ファイルをテキストモードで動作させたいなら、作成するときに ``'w+t'`` モードをセットしてください。

.. include:: tempfile_TemporaryFile_text.py
    :literal:
    :start-after: #end_pymotw_header

..
    The file handle treats the data as text:

その一時ファイルはテキストとしてデータを取り扱います。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'tempfile_TemporaryFile_text.py'))
.. }}}
.. {{{end}}}

NamedTemporaryFile
==================

..
    There are situations, however, where having a named temporary file is
    important. If your application spans multiple processes, or even
    hosts, naming the file is the simplest way to pass it between parts of
    the application. The :func:`NamedTemporaryFile()` function creates a
    file with a name, accessed from the name attribute.

しかし、名前のある一時的なファイルが重要になる状況もあります。アプリケーションが複数のプロセスやホストにまで及ぶなら、名前のある一時ファイルはアプリケーション間でそのデータをやり取りする最も簡単な方法です。 :func:`NamedTemporaryFile()` 関数は、名前属性からアクセスされる名前のある一時ファイルを作成します。

.. include:: tempfile_NamedTemporaryFile.py
    :literal:
    :start-after: #end_pymotw_header

..
    Even though the file is named, it is still removed after the handle is
    closed.

その一時ファイルに名前が付けられていても、その一時ファイルが閉じられると削除されます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'tempfile_NamedTemporaryFile.py'))
.. }}}
.. {{{end}}}

mkdtemp
=======

..
    If you need several temporary files, it may be more convenient to
    create a single temporary directory and then open all of the files in
    that directory.  To create a temporary directory, use
    :func:`mkdtemp()`.

複数の一時ファイルを必要とするなら、1つの一時ディレクトリを作成して、その一時ディレクトリ配下で全ファイルをオープンする方がもっと便利でしょう。一時ディレクトリを作成するために :func:`mkdtemp()` を使用してください。

.. include:: tempfile_mkdtemp.py
    :literal:
    :start-after: #end_pymotw_header

..
    Since the directory is not "opened" per se, you have to remove it
    yourself when you are done with it.

ディレクトリはそれ自身が "オープンされたモノ" ではないので使用後に自分でその一時ディレクトリを削除しなければなりません。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'tempfile_mkdtemp.py'))
.. }}}
.. {{{end}}}

..
    Predicting Names
    ================

名前を予測する
==============

..
    For debugging purposes, it is useful to be able to include some
    indication of the origin of the temporary files. While obviously less
    secure than strictly anonymous temporary files, including a
    predictable portion in the name lets you find the file to examine it
    while your program is using it. All of the functions described so far
    take three arguments to allow you to control the filenames to some
    degree. Names are generated using the formula::

デバッグ目的のために一時ファイルの名前を予測し易いようにしておくことは役に立ちます。名前のない一時ファイルよりも明らかにセキュアではないですが、名前に予測し易い文字列を含めることはプログラムがその一時ファイルを使用しているときに調査のためにファイルを見つけ易くします。全ての関数は、今のところ、ある程度はファイル名を扱えるように3つの引数を取ります。名前は定型的に生成されます。

::

    dir + prefix + random + suffix

..
    where all of the values except random can be passed as arguments to
    :func:`TemporaryFile()`, :func:`NamedTemporaryFile()`, and
    :func:`mkdtemp()`. For example:

random を除いた全ての値、つまり *dir* , *prefix* , *suffix* が :func:`TemporaryFile()` , :func:`NamedTemporaryFile()` や :func:`mkdtemp()` への引数として渡されます。例えば、

.. include:: tempfile_NamedTemporaryFile_args.py
    :literal:
    :start-after: #end_pymotw_header

..
    The *prefix* and *suffix* arguments are combined with a random string
    of characters to build the file name, and the *dir* argument is taken
    as-is and used as the location of the new file.

*prefix* と *suffix* の引数は、ファイル名生成のためにランダム文字列と組み合わせられます。そして、 *dir* 引数はそのままで新しいファイルの置き場所として使用されます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'tempfile_NamedTemporaryFile_args.py'))
.. }}}
.. {{{end}}}

..
    Temporary File Location
    =======================

一時ファイルの場所
==================

..
    If you don't specify an explicit destination using the *dir* argument,
    the actual path used for the temporary files will vary based on your
    platform and settings. The tempfile module includes two functions for
    querying the settings being used at runtime:

*dir* 引数へ明示的に場所を指定しないなら、その一時ファイルが置かれる実際のパスはプラットホームや設定次第で変わります。 tempfile モジュールには実行時に使用される設定を問い合わせる関数が2つあります。

.. include:: tempfile_settings.py
    :literal:
    :start-after: #end_pymotw_header

..
    :func:`gettempdir()` returns the default directory that will hold all
    of the temporary files and :func:`gettempprefix()` returns the string
    prefix for new file and directory names.

:func:`gettempdir()` は全ての一時ファイルに適用するデフォルトディレクトリを返します。 :func:`gettempprefix()` は新しいファイルとディレクトリ名のための接頭辞を返します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'tempfile_settings.py'))
.. }}}
.. {{{end}}}

..
    The value returned by :func:`gettempdir()` is set based on a
    straightforward algorithm of looking through a list of locations for
    the first place the current process can create a file. From the
    library documentation:

:func:`gettempdir()` が返す値は現在のプロセスがファイルを作成できるディレクトリリストの最初の場所を調べる線形アルゴリズムに基づいてセットされます。ライブラリドキュメントから引用します。

..
    Python searches a standard list of directories and sets tempdir to the
    first one which the calling user can create files in. The list is:

Python は標準のディレクトリリストを探して、ユーザがファイルを作成できる最初の場所を tempdir にセットします。そのディレクトリリストは次になります。

..
    1. The directory named by the ``TMPDIR`` environment variable.
    2. The directory named by the ``TEMP`` environment variable.
    3. The directory named by the ``TMP`` environment variable.
    4. A platform-specific location:
       * On RiscOS, the directory named by the ``Wimp$ScrapDir`` environment
         variable.
       * On Windows, the directories ``C:\TEMP``, ``C:\TMP``, ``\TEMP``,
         and ``\TMP``, in that order.
       * On all other platforms, the directories ``/tmp``, ``/var/tmp``,
         and ``/usr/tmp``, in that order.
    5. As a last resort, the current working directory.

1. 一時ディレクトリは TMPDIR 環境変数の名前になります。

2. 一時ディレクトリは TEMP 環境変数の名前になります。

3. 一時ディレクトリは TMP 環境変数の名前になります。

4. プラットホーム固有の場所:

    * RiscOS では一時ディレクトリは ``Wimp$ScrapDir`` 環境変数の名前になります。

    * Windows では一時ディレクトリは ``C:\TEMP`` , ``C:\TMP`` , ``\TEMP`` と ``\TMP`` の順番になります。

    * その他の全プラットホームでは一時ディレクトリは ``/tmp`` , ``/var/tmp`` と ``/usr/tmp`` の順番になります。

5. 最後の手段としてカレントディレクトリになります。

..
    If your program needs to use a global location for all temporary files
    that you need to set explicitly but do not want to set through one of
    these environment variables, you can set ``tempfile.tempdir``
    directly.

プログラムが全ての一時ファイルにこれらの環境変数をセットせずにグローバルな場所を明示的に必要とするなら、 ``tempfile.tempdir`` を直接的にセットすることができます。

.. include:: tempfile_tempdir.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'tempfile_tempdir.py'))
.. }}}
.. {{{end}}}
    
..
    `tempfile <http://docs.python.org/lib/module-tempfile.html>`_
        Standard library documentation for this module.
    :ref:`article-file-access`
        More modules for working with files.

.. seealso::

    `tempfile <http://docs.python.org/lib/module-tempfile.html>`_
        本モジュールの標準ライブラリドキュメント

    :ref:`article-file-access`
        ファイルと共に使用するその他のモジュール
