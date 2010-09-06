..
    ===========================================================
    os.path -- Platform-independent manipulation of file names.
    ===========================================================

===================================================
os.path -- プラットホーム独自のファイル名を操作する
===================================================

..
    :synopsis: Platform-independent manipulation of file names.

.. module:: os.path
    :synopsis: プラットホーム独自のファイル名を操作する

..
    :Purpose: Parse, build, test, and otherwise work on file names and paths.
    :Python Version: 1.4 and later

:目的: ファイル名やパスに関連する解析、構築、テスト、その他
:Python バージョン: 1.4 以上

..
    Writing code to work with files on multiple platforms is easy using
    the functions included in the :mod:`os.path` module. Even programs not
    intended to be ported between platforms should use :mod:`os.path` for
    reliable filename parsing.

複数プラットホーム上のファイルを操作するコードを書くには :mod:`os.path` モジュールに含まれる関数を使用すると簡単です。そのプログラムが他プラットホーム間の移植性を考慮していなくても信頼性の高いファイル名の解析のために :mod:`os.path` を使用すべきです。

..
    Parsing Paths
    =============

パスを解析する
==============

..
    The first set of functions in os.path can be used to parse strings
    representing filenames into their component parts. It is important to
    realize that these functions do not depend on the paths actually
    existing; they operate solely on the strings.

os.path の関数の第1セットはファイル名をその要素の部品を表す文字列へ解析することに使用されます。これらの関数群は対象のパスが実際に存在するかどうかに関係なく、ただ単に文字列操作であることを理解することが重要です。

..
    Path parsing depends on a few variable defined in :mod:`os`:

解析するパスは :mod:`os` で定義されている少しの変数に依存します。

..
    * ``os.sep`` - The separator between portions of the path (e.g.,
      "``/``" or "``\``").

* ``os.sep`` - パスの区切りを表すセパレータ (例, "``/``" 又は "``\``")

..
    * ``os.extsep`` - The separator between a filename and the file
      "extension" (e.g., "``.``").

* ``os.extsep`` - ファイル名とその "拡張子" の間のセパレータ (例, "``.``")

..
    * ``os.pardir`` - The path component that means traverse the directory
      tree up one level (e.g., "``..``").

* ``os.pardir`` - 1階層上のディレクトリへ移動するパス要素 (例, "``..``")

..
    * ``os.curdir`` - The path component that refers to the current
      directory (e.g., "``.``").

* ``os.curdir`` - カレントディレクトリを参照するパス要素 (例, "``.``")

..
    ``split()`` breaks the path into 2 separate parts and returns the
    tuple. The second element is the last component of the path, and the
    first element is everything that comes before it.

``split()`` はパスを2つに分割してそのタプルを返します。2番目の要素はパスの最後の要素で、最初の要素はその前に来るパス全部です。

.. include:: ospath_split.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ospath_split.py'))
.. }}}
.. {{{end}}}

..
    ``basename()`` returns a value equivalent to the second part of the
    ``split()`` value.

``basename()`` は ``split()`` した値の2番目の要素と同じ値を返します。

.. include:: ospath_basename.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ospath_basename.py'))
.. }}}
.. {{{end}}}

..
    ``dirname()`` returns the first part of the split path:

``dirname()`` は ``split()`` したパスの最初の要素を返します。

.. include:: ospath_dirname.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ospath_dirname.py'))
.. }}}
.. {{{end}}}

..
    ``splitext()`` works like ``split()`` but divides the path on the
    extension separator, rather than the directory separator.

``splitext()`` は ``split()`` のように動作しますが、ディレクトリではなく拡張子をセパレータとしてパスを分割します。

.. include:: ospath_splitext.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ospath_splitext.py'))
.. }}}
.. {{{end}}}

..
    ``commonprefix()`` takes a list of paths as an argument and returns a
    single string that represents a common prefix present in all of the
    paths. The value may represent a path that does not actually exist,
    and the path separator is not included in the consideration, so the
    prefix might not stop on a separator boundary.

``commonprefix()`` は引数としてパスのリストを受け取り、その全てのパスに共通する接頭辞である1つの文字列を返します。その値は実際に存在しないパスを表したり、パスセパレータを考慮していなかったりするかもしれません。そのため、その接頭辞として使用する文字列はセパレータの境界で停止しない可能性があります。

.. include:: ospath_commonprefix.py
    :literal:
    :start-after: #end_pymotw_header

..
    In this example the common prefix string is ``/one/two/three``, even
    though one path does not include a directory named ``three``.

このサンプルでは、あるパスは ``three`` という名前のディレクトリを含まないけれど、共通の接頭辞は ``/one/two/three`` です。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ospath_commonprefix.py'))
.. }}}
.. {{{end}}}

..
    Building Paths
    ==============

パスを構築する
==============

..
    Besides taking existing paths apart, you will frequently need to build paths
    from other strings.

既存パスを分解した上で他の文字列からパスを構築する機会がよくあります。

..
    To combine several path components into a single value, use ``join()``:

複数のパスの要素を1つの文字列に結合するために ``join()`` を使用してください。

.. include:: ospath_join.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ospath_join.py'))
.. }}}
.. {{{end}}}

..
    It's also easy to work with paths that include "variable" components
    that can be expanded automatically. For example, ``expanduser()``
    converts the tilde (``~``) character to a user's home directory.

さらに自動的に展開される "変数" 要素を含むパスを操作することも簡単です。例えば ``expanduser()`` はチルダ (``~``) 文字をユーザのホームディレクトリに変換します。

.. include:: ospath_expanduser.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ospath_expanduser.py'))
.. }}}
.. {{{end}}}

..
    ``expandvars()`` is more general, and expands any shell environment
    variables present in the path.

``expandvars()`` はもっと一般的に、パスに存在するシェルの環境変数を展開します。

.. include:: ospath_expandvars.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ospath_expandvars.py'))
.. }}}
.. {{{end}}}

..
    Normalizing Paths
    =================

パスを標準化する
================

..
    Paths assembled from separate strings using ``join()`` or with
    embedded variables might end up with extra separators or relative path
    components. Use ``normpath()`` to clean them up:

分割された文字列から ``join()`` を使用する、又は組み込み変数と共に最後に余分なセパレータが付く、又は要素の相対パスからパスが構成されたとします。そういったパスをクリーンアップするには ``normpath()`` を使用してください。

.. include:: ospath_normpath.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ospath_normpath.py'))
.. }}}
.. {{{end}}}

..
    To convert a relative path to a complete absolute filename, use
    ``abspath()``.

相対パスから絶対パスのファイル名に変換するには ``abspath()`` を使用してください。

.. include:: ospath_abspath.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ospath_abspath.py'))
.. }}}
.. {{{end}}}

..
    File Times
    ==========

ファイル日付
============

..
    Besides working with paths, os.path also includes some functions for
    retrieving file properties, which can be more convenient than calling
    ``os.stat()``:

パスの操作に加えて os.path は ``os.stat()`` を呼び出すよりももっと便利なファイルプロパティを取り出す関数も含みます。

.. include:: ospath_properties.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ospath_properties.py'))
.. }}}
.. {{{end}}}

..
    Testing Files
    =============

ファイルをテストする
====================

..
    When your program encounters a path name, it often needs to know
    whether the path refers to a file or directory. If you are working on
    a platform that supports it, you may need to know if the path refers
    to a symbolic link or mount point. You will also want to test whether
    the path exists or not.  :mod:`os.path` provides functions to test all
    of these conditions.

あなたのプログラムがパス名に遭遇したとき、そのパス名はファイルかディレクトリを参照しているか調べる必要があることがよくあります。あなたがファイルかディレクトリの調査をサポートするプラットホーム上で操作するなら、そのパスはシンボリックリンクを参照するかマウントポイントかを知る必要があるかもしれません。さらにパスが存在するかどうかをテストしたいときもあるでしょう。 :mod:`os.path` はこういった全ての条件をテストする関数を提供します。

.. include:: ospath_tests.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. run_script(cog.inFile, 'rm -f broken_link', interpreter='')
.. cog.out(run_script(cog.inFile, 'ln -s /does/not/exist broken_link', interpreter='', trailing_newlines=False))
.. cog.out(run_script(cog.inFile, 'ospath_tests.py', include_prefix=False))
.. }}}
.. {{{end}}}

..
    Traversing a Directory Tree
    ===========================

ディレクトリツリーを移動する
============================

..
    ``os.path.walk()`` traverses all of the directories in a tree and
    calls a function you provide passing the directory name and the names
    of the contents of that directory. This example produces a recursive
    directory listing, ignoring ``.svn`` directories.

``os.path.walk()`` はツリーの全ディレクトリを移動して、ディレクトリ名を渡してそのディレクトリのコンテンツの名前を提供する関数を呼び出します。このサンプルは ``.svn`` ディレクトリを無視して再起的にディレクトリを辿ってコンテンツを生成します。

.. include:: ospath_walk.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. run_script(cog.inFile, 'rm -rf example', interpreter='')
.. cog.out(run_script(cog.inFile, 'ospath_walk.py'))
.. }}}
.. {{{end}}}


.. seealso::

    `os.path <http://docs.python.org/lib/module-os.path.html>`_
        .. Standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント

    :mod:`os`
        .. The os module is a parent of os.path.

        os.path の親にあたる os モジュール

    :ref:`article-file-access`
        .. Other tools for working with files.

        ファイルを操作する他のツール
