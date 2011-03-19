..
    ========================
    filecmp -- Compare files
    ========================

=============================
filecmp -- ファイルを比較する
=============================

..
    :synopsis: Compare files and directories on the filesystem.

.. module:: filecmp
    :synopsis: ファイルシステム上のファイルやディレクトリを比較する

..
    :Purpose: Compare files and directories on the filesystem.
    :Python Version: 2.1 and later

:目的: ファイルシステム上のファイルやディレクトリを比較する
:Python バージョン: 2.1 以上

..
    Example Data
    ============

サンプルデータ
==============

..
    The examples in the discussion below use a set of test files created by ``filecmp_mkexamples.py``.

この記事のサンプルは、次の ``filecmp_mkexamples.py`` で作成したテストファイルを使用します。

.. include:: filecmp_mkexamples.py
    :literal:
    :start-after: #end_pymotw_header

.. We don't care about the output of the script that creates the example files.
.. {{{cog
.. workdir = path(cog.inFile).dirname()
.. examples = workdir / 'example'
.. examples.rmtree()
.. examples.mkdir()
.. mkexamples = workdir / 'filecmp_mkexamples.py'
.. sh('python %s' % mkexamples)
.. }}}
.. {{{end}}}


::

    $ ls -Rlast example
    total 0
    0 drwxr-xr-x  4 dhellmann  dhellmann  136 Apr 20 17:04 .
    0 drwxr-xr-x  9 dhellmann  dhellmann  306 Apr 20 17:04 ..
    0 drwxr-xr-x  8 dhellmann  dhellmann  272 Apr 20 17:04 dir1
    0 drwxr-xr-x  8 dhellmann  dhellmann  272 Apr 20 17:04 dir2

    example/dir1:
    total 32
    0 drwxr-xr-x  8 dhellmann  dhellmann  272 Apr 20 17:04 .
    0 drwxr-xr-x  4 dhellmann  dhellmann  136 Apr 20 17:04 ..
    0 drwxr-xr-x  2 dhellmann  dhellmann   68 Apr 20 17:04 common_dir
    8 -rw-r--r--  1 dhellmann  dhellmann   21 Apr 20 17:04 common_file
    0 drwxr-xr-x  2 dhellmann  dhellmann   68 Apr 20 17:04 dir_only_in_dir1
    8 -rw-r--r--  1 dhellmann  dhellmann   22 Apr 20 17:04 file_in_dir1
    8 -rw-r--r--  1 dhellmann  dhellmann   22 Apr 20 17:04 file_only_in_dir1
    8 -rw-r--r--  1 dhellmann  dhellmann   17 Apr 20 17:04 not_the_same

    example/dir2:
    total 24
    0 drwxr-xr-x  8 dhellmann  dhellmann  272 Apr 20 17:04 .
    0 drwxr-xr-x  4 dhellmann  dhellmann  136 Apr 20 17:04 ..
    0 drwxr-xr-x  2 dhellmann  dhellmann   68 Apr 20 17:04 common_dir
    8 -rw-r--r--  1 dhellmann  dhellmann   21 Apr 20 17:04 common_file
    0 drwxr-xr-x  2 dhellmann  dhellmann   68 Apr 20 17:04 dir_only_in_dir2
    0 drwxr-xr-x  2 dhellmann  dhellmann   68 Apr 20 17:04 file_in_dir1
    8 -rw-r--r--  1 dhellmann  dhellmann   22 Apr 20 17:04 file_only_in_dir2
    8 -rw-r--r--  1 dhellmann  dhellmann   17 Apr 20 17:04 not_the_same

..
    The same directory structure is repeated one time under the "common_dir"
    directories to give interesting recursive comparison options.

興味のある再帰比較オプションを試すために "common_dir" ディレクトリの配下には同じディレクトリ構造(dir1 と dir2)が置かれます。

..
    Comparing Files
    ===============

ファイルを比較する
==================

..
    The filecmp module includes functions and a class for comparing files and
    directories on the filesystem. If you need to compare two files, use the cmp()
    function.

:mod:`filecmp` モジュールは、ファイルシステム上のファイルやクラスを比較する関数やクラスを提供します。2つのファイルを比較するには :func:`cmp` 関数を使用してください。

.. include:: filecmp_cmp.py
    :literal:
    :start-after: #end_pymotw_header

..
    By default, cmp() looks only at the information available from os.stat(). The
    shallow argument tells cmp() whether to look at the contents of the file, as
    well. The default is to perform a shallow comparison, without looking inside
    the files. Notice that files of the same size created at the same time seem to
    be the same if their contents are not compared.

デフォルトでは、 :func:`cmp` は :func:`os.stat` から利用できる情報のみを調べます。shallow 引数は、そのファイルの中身を調べるかを :func:`cmp` へ伝えます。デフォルトは、ファイルの中身を調べずに浅い比較を実行します。ファイルの中身を比較しない場合、全く同時に作成された同じサイズのファイルは同一と見なされることに注意してください。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'filecmp_cmp.py'))
.. }}}
.. {{{end}}}

..
    To compare a set of files in two directories without recursing, use
    filecmp.cmpfiles(). The arguments are the names of the directories and a list
    of files to be checked in the two locations. The list of common files should
    contain only filenames (directories always result in a mismatch) and
    the files must be present in both locations. The code below shows a simple way
    to build the common list. If you have a shorter formula, post it in the
    comments. The comparison also takes the shallow flag, just as with cmp().

再帰せずに2つのディレクトリ内のファイルセットを比較するには :func:`filecmp.cmpfiles` を使用してください。その引数はディレクトリの名前と、その2つのディレクトリでチェックするファイルのリストです。共通ファイルのリストはファイル名のみを含めます(ディレクトリは必ずミスマッチになります)。そして、そのファイルは両方のディレクトリに存在していなければなりません。次のコードは、共通リストを作成するシンプルな方法を紹介します。もっと短く書けるならコメントで教えてください。 :func:`cmp` と同様に、shallow フラグを受け取って比較することもできます。

.. include:: filecmp_cmpfiles.py
    :literal:
    :start-after: #end_pymotw_header

..
    cmpfiles() returns three lists of filenames for files that match, files that
    do not match, and files that could not be compared (due to permission problems
    or for any other reason).

:func:`cmpfiles` はマッチしたファイル、マッチしなかったファイル、(パーミッションや何らかの理由で)比較できなかったファイルのファイル名を含む3つのリストを返します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'filecmp_cmpfiles.py'))
.. }}}
.. {{{end}}}

..
    Using dircmp
    ============

dircmp を使用する
=================

..
    The functions described above are suitable for relatively simple comparisons,
    but for recursive comparison of large directory trees or for more complete
    analysis, the dircmp class is more useful. In its simplest use case, you can
    print a report comparing two directories with the report() method:

前節で紹介した関数は相対的にシンプルな比較に適していますが、巨大なディレクトリツリーの再帰的な比較、またはもっと複雑な解析には :class:`dircmp` クラスがさらに便利です。最も簡単な使用方法は、 :func:`report` メソッドで2つのディレクトリを比較するレポートを表示できます。

.. include:: filecmp_dircmp_report.py
    :literal:
    :start-after: #end_pymotw_header

..
    The output is a plain-text report showing the results of just the
    contents of the directories given, without recursing. In this case,
    the file "not_the_same" is thought to be the same because the contents
    are not being compared. There is no way to have dircmp compare the
    contents of files like cmp() can.

その実行結果は、再帰せずに渡されたディレクトリのコンテンツの比較結果を表示するプレーンテキストのレポートです。このケースでは、"not_the_same" というファイルが同一と見なされます。それはそのファイルの中身が比較されないからです。dircmp には :func:`cmp` のようなファイルの中身を比較する方法がありません。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'filecmp_dircmp_report.py'))
.. }}}
.. {{{end}}}

..
    For more detail, and a recursive comparison, use report_full_closure():

さらに詳細に、再帰的な比較を行うには :func:`report_full_closure` を使用してください。

.. include:: filecmp_dircmp_report_full_closure.py
    :literal:
    :start-after: #end_pymotw_header

..
    The output includes comparisons of all parallel subdirectories.

その実行結果は、全てのサブディレクトリを比較します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'filecmp_dircmp_report_full_closure.py'))
.. }}}
.. {{{end}}}

..
    Using differences in your program
    =================================

プログラム内で差異を使用する
============================

..
    Besides producing printed reports, dircmp calculates useful lists of files you
    can use in your programs directly. Each of the following attributes is
    calculated only when requested, so instantiating a dircmp does not incur a lot
    of extra overhead.

レポートの作成に加えて、dircmp は直接プログラム内で利用可能な便利なファイルリストを算出します。それぞれの属性はそれが要求されたときのみ算出されるので、dircmp をインスタンス化するのはそう大きなオーバーヘッドになりません。

..
    The files and subdirectories contained in the directories being compared are
    listed in left_list and right_list:

比較対象のディレクトリを含むサブディレクトリとファイルは :attr:`left_list` と :attr:`right_list` で表示されます。

.. include:: filecmp_dircmp_list.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'filecmp_dircmp_list.py'))
.. }}}
.. {{{end}}}

..
    The inputs can be filtered by passing a list of names to ignore to the
    constructor. By default the names RCS, CVS, and tags are ignored.

無視するファイル名のリストをコンストラクタへ渡すことでその入力をフィルタできます。デフォルトでは、RCS, CVS や tags が無視されます。

.. include:: filecmp_dircmp_list_filter.py
    :literal:
    :start-after: #end_pymotw_header

..
    In this case, the "common_file" is left out of the list of files to be
    compared.

このケースでは、"common_file" が比較対象外のファイルリストにあります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'filecmp_dircmp_list_filter.py'))
.. }}}
.. {{{end}}}

..
    The set of files common to both input directories is maintained in common, and
    the files unique to each directory are listed in left_only, and right_only.

両方の入力ディレクトリの共通ファイルは :attr:`common` で保持されます。それぞれのディレクトリにしか存在しないファイルは :attr:`left_only` や :attr:`right_only` で表示されます。

.. include:: filecmp_dircmp_membership.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'filecmp_dircmp_membership.py'))
.. }}}
.. {{{end}}}

..
    The common members can be further broken down into files, directories and
    "funny" items (anything that has a different type in the two directories or
    where there is an error from os.stat()).

:attr:`common` の仲間には、さらにファイル、ディレクトリ、"funny" (2つのディレクトリ、または :func:`os.stat` からエラーが発生した場所で異なる型を持つ) の要素に分割されます。

.. include:: filecmp_dircmp_common.py
    :literal:
    :start-after: #end_pymotw_header

..
    In the example data, the item named "file_in_dir1" is a file in one directory
    and a subdirectory in the other, so it shows up in the "funny" list.

このサンプルデータでは、"file_in_dir1" という要素はディレクトリ内にあるファイルであり、且つサブディレクトリです。そのため "funny" リストに表示されます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'filecmp_dircmp_common.py'))
.. }}}
.. {{{end}}}

..
    The differences between files are broken down similarly:

ファイル間の差異は同様に分割されます。

.. include:: filecmp_dircmp_diff.py
    :literal:
    :start-after: #end_pymotw_header

..
    Remember, the file "not_the_same" is only being compared via os.stat, and the contents are not examined.

"not_the_same" は :func:`os.stat` のみで比較されたファイルであり、そのファイルの中身は調べないことを覚えておいてください。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'filecmp_dircmp_diff.py'))
.. }}}
.. {{{end}}}

..
    Finally, the subdirectories are also mapped to new dircmp objects in the
    attribute subdirs to allow easy recursive comparison.

最後に、再帰的な比較が簡単にできるようにサブディレクトリは :attr:`subdirs` 属性で新たな dircmp オブジェクトを取得することもできます。

.. include:: filecmp_dircmp_subdirs.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python filecmp_dircmp_subdirs.py
    Subdirectories:
    {'common_dir': <filecmp.dircmp instance at 0x85da0>}

.. seealso::

    `filecmp <http://docs.python.org/library/filecmp.html>`_
        .. The standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント

    :ref:`os-directories` from :mod:`os`
        .. Listing the contents of a directory.

        ディレクトリのコンテンツを表示する

    :mod:`difflib`
        .. Computing the differences between two sequences.

        2つのシーケンス間の差異を算出する
