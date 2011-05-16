.. _zipimport-ref:

=========================================================
zipimport -- ZIP アーカイブ内から Python コードを読み込む
=========================================================

..
    ======================================================
    zipimport -- Load Python code from inside ZIP archives
    ======================================================

..
    :synopsis: Load Python code from inside ZIP archives.

.. module:: zipimport
    :synopsis: ZIP アーカイブ内から Python コードを読み込む

..
    :Purpose: Load Python code from inside ZIP archives.
    :Available In: 2.3 and later

:目的: ZIP アーカイブ内から Python コードを読み込む
:利用できるバージョン: 2.3 以上

..
    The :mod:`zipimport` module implements the :class:`zipimporter` class,
    which can be used to find and load Python modules inside ZIP
    archives. The :class:`zipimporter` supports the "import hooks" API
    specified in :pep:`302`; this is how Python Eggs work.

:mod:`zipimport` モジュールは、ZIP アーカイブ内から Python モジュールを探して、そのモジュールを読み込む :class:`zipimporter` クラスを実装します。 :class:`zipimporter` は、 :pep:`302` で標準化された "import hooks" API をサポートします。これは Python Eggs の動作を説明するものです。

..
    You probably won't need to use the :mod:`zipimport` module directly,
    since it is possible to import directly from a ZIP archive as long as
    that archive appears in your :ref:`sys.path <sys-path>`. However, it
    is interesting to see the features available.

もしかしたら :mod:`zipimport` モジュールを直接的に使用する必要はないかもしれません。 :ref:`sys.path <sys-path>` にある ZIP アーカイブから直接インポートできるからです。とは言え、その機能をみていくのも興味深いものです。

..
    Example
    =======

サンプル
========

..
    For the examples this week, I'll reuse some of the code from last
    week's discussion of zipfile to create an example ZIP archive
    containing some Python modules. If you are experimenting with the
    sample code on your system, run ``zipimport_make_example.py`` before
    any of the rest of the examples. It will create a ZIP archive
    containing all of the modules in the example directory, along with
    some test data needed for the code below.

Python モジュールを含むサンプルの ZIP アーカイブを作成するために、今週のサンプルは、先週の :mod:`zipfile` の記事のコードを再利用します。自分のシステム上でサンプルコードで試してみたいなら、任意のサンプルを試す前に ``zipimport_make_example.py`` を実行してください。このスクリプトは、ソースコードに必要なテストデータと一緒に、対象ディレクトリの全てのモジュールを含む ZIP アーカイブを作成します。

.. include:: zipimport_make_example.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. # clean up pyc files in case the interpreter version has
.. # changed since the last build
.. [ p.unlink() for p in path(cog.inFile).parent.glob('*.pyc') ]
.. (path(cog.inFile).parent / 'zipimport_example.zip').unlink()
.. cog.out(run_script(cog.inFile, 'zipimport_make_example.py'))
.. }}}
.. {{{end}}}

..
    Finding a Module
    ================

モジュールを探す
================

..
    Given the full name of a module, :func:`find_module()` will try to
    locate that module inside the ZIP archive.

モジュールの完全な名前を渡すと、 :func:`find_module()` は ZIP アーカイブ内にあるモジュールを展開しようとします。

.. include:: zipimport_find_module.py
    :literal:
    :start-after: #end_pymotw_header

..
    If the module is found, the :class:`zipimporter` instance is
    returned. Otherwise, ``None`` is returned.

指定したモジュールが見つかると :class:`zipimporter` インスタンスが返されます。それ以外の場合は ``None`` 返されます。

.. {{{cog
.. (path(cog.inFile).parent / 'zipimport_example.zip').unlink()
.. run_script(cog.inFile, 'zipimport_make_example.py')
.. cog.out(run_script(cog.inFile, 'zipimport_find_module.py'))
.. }}}
.. {{{end}}}

..
    Accessing Code
    ==============

コードにアクセスする
====================

..
    The :func:`get_code()` method loads the code object for a module from
    the archive.

:func:`get_code()` メソッドは、アーカイブ内のモジュールのコードオブジェクトを読み込みます。

.. include:: zipimport_get_code.py
    :literal:
    :start-after: #end_pymotw_header

..
    The code object is not the same as a module object.

コードオブジェクトは、モジュールオブジェクトと同じではありません。

.. {{{cog
.. (path(cog.inFile).parent / 'zipimport_example.zip').unlink()
.. run_script(cog.inFile, 'zipimport_make_example.py')
.. cog.out(run_script(cog.inFile, 'zipimport_get_code.py'))
.. }}}
.. {{{end}}}

..
    To load the code as a usable module, use :func:`load_module()`
    instead.

普通に利用可能なモジュールとして読み込むには、 :func:`load_module()` を使用してください。

.. include:: zipimport_load_module.py
    :literal:
    :start-after: #end_pymotw_header

..
    The result is a module object as though the code had been loaded from a
    regular import:

この実行結果は、普通にインポートして読み込んだコードのようにモジュールオブジェクトになります。

.. {{{cog
.. (path(cog.inFile).parent / 'zipimport_example.zip').unlink()
.. run_script(cog.inFile, 'zipimport_make_example.py')
.. cog.out(run_script(cog.inFile, 'zipimport_load_module.py'))
.. }}}
.. {{{end}}}

..
    Source
    ======

ソース
======

..
    As with the :mod:`inspect` module, it is possible to retrieve the
    source code for a module from the ZIP archive, if the archive includes
    the source. In the case of the example, only
    ``zipimport_get_source.py`` is added to ``zipimport_example.zip`` (the
    rest of the modules are just added as the .pyc files).

:mod:`inspect` と同様に、ZIP アーカイブがソースコードを含む場合、そのアーカイブからモジュールのソースコードを取り出せます。このサンプルでは、 ``zipimport_get_source.py`` のみ ``zipimport_example.zip`` に追加されています (その他のモジュールは .pyc ファイルのみを追加しています) 。

.. include:: zipimport_get_source.py
    :literal:
    :start-after: #end_pymotw_header

..
    If the source for a module is not available, :func:`get_source()`
    returns ``None``.

モジュールのソースが利用できない場合、 :func:`get_source()` は ``None`` を返します。

.. {{{cog
.. (path(cog.inFile).parent / 'zipimport_example.zip').unlink()
.. run_script(cog.inFile, 'zipimport_make_example.py')
.. cog.out(run_script(cog.inFile, 'zipimport_get_source.py'))
.. }}}
.. {{{end}}}

..
    Packages
    ========

パッケージ
==========

..
    To determine if a name refers to a package instead of a regular module, use
    :func:`is_package()`.

普通のモジュールではなく、ある名前がパッケージを参照するかどうかを調べるには、 :func:`is_package()` を使用してください。

.. include:: zipimport_is_package.py
    :literal:
    :start-after: #end_pymotw_header

..
    In this case, ``zipimport_is_package`` came from a module and the
    ``example_package`` is a package.

このサンプルでは、 ``zipimport_is_package`` はモジュールであり、 ``example_package`` はパッケージです。

.. {{{cog
.. (path(cog.inFile).parent / 'zipimport_example.zip').unlink()
.. run_script(cog.inFile, 'zipimport_make_example.py')
.. cog.out(run_script(cog.inFile, 'zipimport_is_package.py'))
.. }}}
.. {{{end}}}

..
    Data
    ====

データ
======

..
    There are times when source modules or packages need to be distributed
    with non-code data. Images, configuration files, default data, and
    test fixtures are just a few examples of this. Frequently, the module
    ``__path__`` attribute is used to find these data files relative to
    where the code is installed.

ソースモジュールやパッケージが、ソースコード以外のデータと一緒に配布されることもあります。例えば、画像、設定ファイル、デフォルトのデータ、テストのフィクスチャなどです。よくやるのは、そのモジュールの ``__file__`` 属性が、ソースコードのインストース場所に関連するデータファイルを探すのに使用されます。

..
    For example, with a normal module you might do something like:

例えば、通常のモジュールと一緒に次のようにするかもしれません。

.. include:: zipimport_get_data_nozip.py
    :literal:
    :start-after: #end_pymotw_header

..
    The output will look something like this, with the path changed based on where
    the PyMOTW sample code is on your filesystem.

この出力結果は次のように、ファイルシステム上の PyMOTW のサンプルコードに基づいたパスに変更されます。

.. {{{cog
.. (path(cog.inFile).parent / 'zipimport_example.zip').unlink()
.. run_script(cog.inFile, 'zipimport_make_example.py')
.. cog.out(run_script(cog.inFile, 'zipimport_get_data_nozip.py'))
.. }}}
.. {{{end}}}

..
    If the ``example_package`` is imported from the ZIP archive instead of
    the filesystem, that method does not work:

``example_package`` が、ファイルシステムではなく ZIP アーカイブからインポートされる場合、そのモジュールは動作しません。

.. include:: zipimport_get_data_zip.py
    :literal:
    :start-after: #end_pymotw_header

..
    The ``__file__`` of the package refers to the ZIP archive, and not a directory. So
    we cannot just build up the path to the ``README.txt`` file.

パッケージの ``__file__`` は、ディレクトリではなく ZIP アーカイブを参照するので、単純に ``README.txt`` ファイルへのパスを構築できません。

.. {{{cog
.. (path(cog.inFile).parent / 'zipimport_example.zip').unlink()
.. run_script(cog.inFile, 'zipimport_make_example.py')
.. cog.out(run_script(cog.inFile, 'zipimport_get_data_zip.py', ignore_error=True))
.. }}}
.. {{{end}}}

..
    Instead, we need to use the :func:`get_data()` method. We can access
    :class:`zipimporter` instance which loaded the module through the
    ``__loader__`` attribute of the imported module:

その代わりに :func:`get_data()` メソッドを使用する必要があります。インポートされたモジュールの ``__loader__`` 属性を通して、そのモジュールを読み込んだ :class:`zipimporter` インスタンスにアクセスできます。

.. include:: zipimport_get_data.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. (path(cog.inFile).parent / 'zipimport_example.zip').unlink()
.. run_script(cog.inFile, 'zipimport_make_example.py')
.. cog.out(run_script(cog.inFile, 'zipimport_get_data.py'))
.. }}}
.. {{{end}}}

..
    The ``__loader__`` is not set for modules not imported via
    :mod:`zipimport`.

``__loader__`` は、 :mod:`zipimport` 経由でインポートされていないモジュールにはセットされません。

.. seealso::

    `zipimport <http://docs.python.org/lib/module-zipimport.html>`_
        .. Standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント

    :mod:`imp`
        .. Other import-related functions.

        その他のインポート関連の機能

    :pep:`302`
        .. New Import Hooks

        新たなインポートフック

    :mod:`pkgutil`
        .. Provides a more generic interface to :func:`get_data`.

        :func:`get_data` に対するより汎用的なインタフェースを提供
