..
    =====================================
    shutil -- High-level file operations.
    =====================================

================================
shutil -- 高レベルなファイル操作
================================

..
    :synopsis: High-level file operations.

.. module:: shutil
    :synopsis: 高レベルなファイル操作

..
    :Purpose: High-level file operations.
    :Python Version: 1.4 and later

:目的: 高レベルなファイル操作
:Python バージョン: 1.4 以上

..
    The :mod:`shutil` module includes high-level file operations such as
    copying, setting permissions, etc.

:mod:`shutil` モジュールは、コピーやパーミッション設定といった高レベルなファイル操作を提供します。

..
    Copying Files
    =============

ファイルをコピーする
====================

..
    :func:`copyfile()` copies the contents of the source to the
    destination. Raises :ref:`IOError <exceptions-IOError>` if you do not
    have permission to write to the destination file.  Because the
    function opens the input file for reading, regardless of its type,
    special files cannot be copied as new special files with
    :func:`copyfile()`.

:func:`copyfile()` はコピー元ファイルの内容をコピー先ファイルへコピーします。もしコピー先ファイルへの書き込みパーミッションがない場合、 :ref:`IOError <exceptions-IOError>` が発生します。この理由は、ファイル種別に関わらず、そのコピー元ファイルをオープンして読み込もうとしますが、 :func:`copyfile()` では特殊ファイルが新たなファイルとしてコピーされないからです。

.. include:: shutil_copyfile.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. run_script(cog.inFile, 'rm -rf *.copy', interpreter=None)
.. cog.out(run_script(cog.inFile, 'shutil_copyfile.py'))
.. }}}
.. {{{end}}}

..
    :func:`copyfile()` is written using the lower-level function
    :func:`copyfileobj()`. While the arguments to :func:`copyfile()` are
    file names, the arguments to :func:`copyfileobj()` are open file
    handles. The optional third argument is a buffer length to use for
    reading in chunks (by default, the entire file is read at one time).

:func:`copyfile()` は、低レベル関数に :func:`copyfileobj()` を使用して書き込みます。 :func:`copyfile()` への引数はファイル名であるのに対して、 :func:`copyfileobj()` への引数はオープンされたファイルハンドラです。オプションである3番目の引数はチャンクの読み込みに使用するバッファ長です(デフォルトでは、一度にファイル全てを読み込む)。

.. include:: shutil_copyfileobj.py
    :literal:
    :start-after: #end_pymotw_header

..
    The default behavior is to read using large blocks.  Use ``-1`` to
    read all of the input at one time or another positive integer to set
    your own block size.

デフォルトの動作は大きなブロックで読み込みます。その入力の全てを一度に読み込むには ``-1`` を、独自のブロックサイズで読み込むには自然数を指定してください。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'shutil_copyfileobj.py'))
.. }}}
.. {{{end}}}

..
    The :func:`copy()` function interprets the output name like the Unix
    command line tool ``cp``. If the named destination refers to a
    directory instead of a file, a new file is created in the directory
    using the base name of the source. The permissions of the file are
    copied along with the contents.

:func:`copy()` 関数は、Unix コマンドラインツールの ``cp`` のように出力ファイルの名前を解釈します。コピー先ファイルの名前がファイルではなくディレクトリなら、ソースファイルのベース名を使用してそのディレクトリ配下に新たなファイルが作成されます。そのファイルのパーミッションはコピー元ファイルと同じになります。

.. include:: shutil_copy.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. (path(cog.inFile).parent / 'example').rmtree()
.. cog.out(run_script(cog.inFile, 'shutil_copy.py'))
.. }}}
.. {{{end}}}

..
    :func:`copy2()` works like :func:`copy()`, but includes the access and
    modification times in the meta-data copied to the new file.

:func:`copy2()` は :func:`copy()` のように動作しますが、コピー元ファイルのアクセス時刻と更新時刻のメタデータもコピー先ファイルへ保持されます。

.. include:: shutil_copy2.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. (path(cog.inFile).parent / 'example').rmtree()
.. cog.out(run_script(cog.inFile, 'shutil_copy2.py'))
.. }}}
.. {{{end}}}

..
    Copying File Meta-data
    ======================

ファイルのメタデータをコピーする
================================

..
    By default when a new file is created under Unix, it receives
    permissions based on the umask of the current user. To copy the
    permissions from one file to another, use :func:`copymode()`.

デフォルトでは、Unix 環境で新たなファイルを作成するとき、そのファイルはカレントユーザの umask に基づいてパーミッションが決まります。あるファイルから別のファイルへそのパーミッションをコピーするには :func:`copymode()` を使用してください。

.. include:: shutil_copymode.py
    :literal:
    :start-after: #end_pymotw_header

..
    First, create a file to be modified:

まず変更対象のファイルを作成します。

.. include:: shutil_copymode.sh
    :literal:

..
    Then run the example script to change the permissions.

パーミッションを変更するサンプルスクリプトを実行します。

.. {{{cog
.. (path(cog.inFile).parent / 'file_to_change.txt').unlink()
.. cog.out(run_script(cog.inFile, 'shutil_copymode.py'))
.. }}}
.. {{{end}}}

..
    To copy other meta-data about the file (permissions, last access time,
    and last modified time), use :func:`copystat()`.


その他のファイルに関するメタデータ(パーミッション、最終アクセス時刻、最終更新時刻)をコピーするには :func:`copystat()` を使用してください。

.. include:: shutil_copystat.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. (path(cog.inFile).parent / 'file_to_change.txt').unlink()
.. cog.out(run_script(cog.inFile, 'shutil_copystat.py'))
.. }}}
.. {{{end}}}

..
    Working With Directory Trees
    ============================

ディレクトリツリーを扱う
========================

..
    :mod:`shutil` includes 3 functions for working with directory
    trees. To copy a directory from one place to another, use
    :func:`copytree()`. It recurses through the source directory tree,
    copying files to the destination. The destination directory must not
    exist in advance. The *symlinks* argument controls whether symbolic
    links are copied as links or as files. The default is to copy the
    contents to new files. If the option is true, new symlinks are created
    within the destination tree.

:mod:`shutil` モジュールは、ディレクトリツリーを扱う3つの関数を提供します。ある場所から別の場所へディレクトリをコピーするには、 :func:`copytree()` を使用してください。それはコピー元のディレクトリツリーを再帰的に辿り、コピー先へファイルをコピーします。コピー先のディレクトリは前もって存在していなければなりません。 *symlinks* 引数は、シンボリックリンクをリンクとしてコピーするか、ファイルとしてコピーするかを制御します。デフォルトは新しいファイルとしてコピーします。そのオプションが True の場合、コピー先ツリーに新たなシンボリックリンクが作成されます。

.. note::

  .. The documentation for :func:`copytree()` says it should be
     considered a sample implementation, rather than a tool. You may want
     to copy the implementation and make it more robust, or add features
     like a progress meter.

  :func:`copytree()` のドキュメントには、この関数はツールというよりサンプル実装と見なすようにと説明されています。その実装をコピーして、もっと堅牢にするか、進捗が分かるような機能を追加してください。

.. include:: shutil_copytree.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'shutil_copytree.py'))
.. }}}
.. {{{end}}}

..
    To remove a directory and its contents, use :func:`rmtree()`. Errors
    are raised as exceptions by default, but can be ignored if the second
    argument is true, and a special error handler function can be provided
    in the third argument.

ディレクトリとその中にあるファイルを削除するには :func:`rmtree()` を使用してください。デフォルトでは例外としてエラーが発生しますが、2番目の引数を True にすることでそのエラーは無視されます。そして、特殊なエラーハンドラ関数が3番目の引数で提供されます。

.. include:: shutil_rmtree.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'shutil_rmtree.py'))
.. }}}
.. {{{end}}}

..
    To move a file or directory from one place to another, use
    :func:`move()`. The semantics are similar to those of the Unix command
    ``mv``. If the source and destination are within the same filesystem,
    the source is simply renamed.  Otherwise the source is copied to the
    destination and then the source is removed.

ある場所から別の場所へファイルやディレクトリを移動するには :func:`move()` を使用してください。Unix コマンドの ``mv`` とほとんど同じ仕組みで動作します。同じファイルシステム上にコピー元とコピー先のファイルがある場合、そのコピー元が単純にリネームされます。それ以外の場合は、コピー先へコピーされた後でコピー元が削除されます。

.. include:: shutil_move.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. (path(cog.inFile).parent / 'example').rmtree()
.. d = [ f.unlink() for f in path(cog.inFile).parent.glob('example.*') ]
.. cog.out(run_script(cog.inFile, 'shutil_move.py'))
.. }}}
.. {{{end}}}


.. seealso::

    `shutil <http://docs.python.org/lib/module-shutil.html>`_
        .. Standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント

    :ref:`article-file-access`
        .. Other utilities for working with files.

        ファイルを扱うその他のモジュール
