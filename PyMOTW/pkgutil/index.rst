..
    ==============================
     pkgutil -- Package Utilities
    ==============================

=====================================
 pkgutil -- パッケージユーティリティ
=====================================

..
    :synopsis: Package utilities

.. module:: pkgutil
    :synopsis: パッケージユーティリティ

..
    :Purpose: Add to the module search path for a specific package and work with resources included in a package.
    :Available In: 2.3 and later

:目的: モジュール検索パスに特定パッケージを追加して、パッケージのリソースを扱う
:利用できるバージョン: 2.3 以上

..
    The :mod:`pkgutil` module includes functions for working with Python
    packages.  :func:`extend_path` changes the import path for sub-modules
    of the package, and :func:`get_data` provides access to file resources
    distributed with the package.

:mod:`pkgutil` モジュールは、Python パッケージを扱う機能を提供します。 :func:`extend_path` はパッケージのサブモジュールのインポートパスを変更し、 :func:`get_data` はパッケージとして配布されたファイルリソースへのアクセスを提供します。

..
    Package Import Paths
    ====================

パッケージのインポートパス
==========================

..
    The :func:`extend_path` function is used to modify the search path for
    modules in a given package to include other directories in
    :ref:`sys.path <sys-path>`. This can be used to override installed
    versions of packages with development versions, or to combine
    platform-specific and shared modules into a single package namespace.

:func:`extend_path` 関数は、 :ref:`sys.path <sys-path>` の他のディレクトリを追加するために、任意のパッケージの検索パスを変更するのに使用されます。これは、パッケージの開発バージョンでインストール済みバージョンを上書きしたり、1つのパッケージの名前空間内に共有モジュールやプラットフォーム固有のものを組み合わせたりするのに使用されます。

..
    The most common way to call :func:`extend_path` is by adding these two
    lines to the ``__init__.py`` inside the package:

:func:`extend_path` を呼び出す最も一般的な方法は、次の2行をパッケージの ``__init__.py`` へ追加します。

::

    import pkgutil
    __path__ = pkgutil.extend_path(__path__, __name__)

..
    :func:`extend_path` scans ``sys.path`` for directories that include a
    subdirectory named for the package given as the second argument.  The
    list of directories is combined with the path value passed as the
    first argument and returned as a single list, suitable for use as the
    package import path.

:func:`extend_path` は、第二引数で渡された任意のパッケージのサブディレクトリ名を含むディレクトリのために ``sys.path`` を調べます。ディレクトリのリストは、第一引数で渡されたパスと組み合わせて、パッケージのインポートパスに利用できる1つのリストを返します。

..
    An example package called :mod:`demopkg` includes these files:

:mod:`demopkg` というサンプルパッケージは、次のファイルを含みます。

::

    $ find demopkg1 -name '*.py'
    demopkg1/__init__.py
    demopkg1/shared.py

``demopkg1/__init__.py`` は次の通りです。

.. include:: demopkg1/__init__.py
    :literal:
    :start-after: #end_pymotw_header

..
    The :command:`print` statements shows the search path before and after
    it is modified, to highlight the difference.

変更による違いを分かりやすくするために :command:`print` 文で変更前後の検索パスを表示します。

..
    And an ``extension`` directory, with add-on features for
    :mod:`demopkg`, contains

:mod:`demopkg` の拡張機能を含む ``extension`` ディレクトリは次の通りです。

::

    $ find extension -name '*.py'
    extension/__init__.py
    extension/demopkg1/__init__.py
    extension/demopkg1/not_shared.py

..
    A simple test program imports the :mod:`demopkg1` package:

簡単なテストプログラムは :mod:`demopkg1` パッケージをインポートします。

.. include:: pkgutil_extend_path.py
    :literal:
    :start-after: #end_pymotw_header

..
    When this test program is run directly from the command line, the
    :mod:`not_shared` module is not found.  

このテストプログラムをコマンドラインから直接実行すると、 :mod:`not_shared` モジュールが見つかりません。

.. note::

  .. The full filesystem paths in these examples have been shortened to
     emphasize the parts that change.

  この記事のサンプルのファイルシステム上のフルパスは、変更された部分を強調するために短縮しています。

::

	$ python pkgutil_extend_path.py

	demopkg1.__path__ before:
	['.../PyMOTW/pkgutil/demopkg1']
	
	demopkg1.__path__ after:
	['.../PyMOTW/pkgutil/demopkg1']
	
	demopkg1           : .../PyMOTW/pkgutil/demopkg1/__init__.py
	demopkg1.shared    : .../PyMOTW/pkgutil/demopkg1/shared.py
	demopkg1.not_shared: Not found (No module named not_shared)

..
    However, if the ``extension`` directory is added to the
    :data:`PYTHONPATH` and the program is run again, different results are
    produced.

但し、この ``extension`` ディレクトリを :data:`PYTHONPATH` に追加して、同じプログラムを再実行すると違う結果になります。

::

    $ export PYTHONPATH=extension
    $ python pkgutil_extend_path.py
    demopkg1.__path__ before:
    ['.../PyMOTW/pkgutil/demopkg1']

    demopkg1.__path__ after:
    ['.../PyMOTW/pkgutil/demopkg1',
     '.../PyMOTW/pkgutil/extension/demopkg1']

    demopkg1           : .../PyMOTW/pkgutil/demopkg1/__init__.pyc
    demopkg1.shared    : .../PyMOTW/pkgutil/demopkg1/shared.pyc
    demopkg1.not_shared: .../PyMOTW/pkgutil/extension/demopkg1/not_shared.py

..
    The version of :mod:`demopkg1` inside the ``extension`` directory has
    been added to the search path, so the :mod:`not_shared` module is
    found there.

``extension`` ディレクトリ内の :mod:`demopkg1` が検索パスへ追加されたので、 :mod:`not_shared` モジュールがそこで見つかります。

..
    Extending the path in this manner is useful for combining
    platform-specific versions of packages with common packages,
    especially if the platform-specific versions include C extension
    modules.

この方法でパスを拡張することは、共通パッケージとプラットフォーム固有のモジュールを組み合わせるのに都合が良く、特に C 言語の拡張モジュールを含むプラットフォーム固有のモジュールに便利です。

..
    Development Versions of Packages
    --------------------------------

パッケージの開発バージョン
--------------------------

..
    While develop enhancements to a project, it is common to need to test
    changes to an installed package. Replacing the installed copy with a
    development version may be a bad idea, since it is not necessarily
    correct and other tools on the system are likely to depend on the
    installed package. 

あるプロジェクトで拡張機能を開発する一方で、インストール済みパッケージへの変更をテストしなければならないことがよくあります。インストール済みのパッケージを開発バージョンと置き換えることは、悪い考えかもしれません。それは必ずしも正しいとは言えなくて、システム上のその他のツールがインストール済みパッケージに依存している可能性があるからです。

..
    A completely separate copy of the package could be configured in a
    development environment using `virtualenv`_, but for small
    modifications the overhead of setting up a virtual environment with
    all of the dependencies may be excessive.

完全に独立したパッケージのコピーをもつ開発環境は `virtualenv`_ で設定できますが、些細な変更のために全ての依存関係をもつ仮想環境を構築するのは、やり過ぎかもしれません。

..
    Another option is to use :mod:`pkgutil` to modify the module search
    path for modules that belong to the package under development. In this
    case, however, the path must be reversed so development version
    overrides the installed version.

別の方法としては、開発環境でパッケージがもつモジュールの検索パスを変更するのに :mod:`pkgutil` を使用することです。このケースでは、但し、そのパスは置き換えなければならないので、開発バージョンはインストール済みバージョンを上書きします。

..
    Given a package :mod:`demopkg2` like this:

任意のパッケージ :mod:`demopkg2` は次のファイルを含みます。

::

    $ find demopkg2 -name '*.py'
    demopkg2/__init__.py
    demopkg2/overloaded.py

..
    With the function under development located in
    ``demopkg2/overloaded.py``. The installed version contains

``demopkg2/overloaded.py`` に置かれた開発中の関数と一緒に、インストール済みバージョンは、

.. include:: demopkg2/overloaded.py
    :literal:
    :start-after: #end_pymotw_header

..
    and ``demopkg2/__init__.py`` contains

と ``demopkg2/__init__.py`` 


.. include:: demopkg2/__init__.py
    :literal:
    :start-after: #end_pymotw_header

を含みます。

..
    :func:`reverse` is used to ensure that any directories added to the
    search path by :mod:`pkgutil` are scanned for imports *before* the
    default location.

:func:`reverse` は、 :mod:`pkgutil` が検索パスへ任意のディレクトリを追加するのを保証するために使用され、デフォルトの位置よりも *先に* インポートのために調べられます。

..
    This program imports :mod:`demopkg2.overloaded` and calls :func:`func`:

このプログラムは、 :mod:`demopkg2.overloaded` をインポートして :func:`func` を呼び出します。

.. include:: pkgutil_devel.py
    :literal:
    :start-after: #end_pymotw_header

..
    Running it without any special path treatment produces output from the
    installed version of :func:`func`.

特別なパス設定を行わずに、そのテストプログラムを実行すると、インストール済みの :func:`func` を呼び出して表示します。

::

    $ python pkgutil_devel.py
    demopkg2           : .../PyMOTW/pkgutil/demopkg2/__init__.py
    demopkg2.overloaded: .../PyMOTW/pkgutil/demopkg2/overloaded.py

..
    A development directory containing

開発ディレクトリは、次のファイルを含みます。

::

    $ find develop -name '*.py'
    develop/demopkg2/__init__.py
    develop/demopkg2/overloaded.py

..
    and a modified version of :mod:`overloaded`

そして :mod:`overloaded` の変更されたバージョンは次になります。

.. include:: develop/demopkg2/overloaded.py
    :literal:
    :start-after: #end_pymotw_header

..
    will be loaded when the test program is run with the ``develop``
    directory in the search path.

テストプログラムが検索パスの ``develop`` ディレクトリで実行されるときに読み込まれます。

::

    $ export PYTHONPATH=develop 
    $ python pkgutil_devel.py

    demopkg2           : .../PyMOTW/pkgutil/demopkg2/__init__.pyc
    demopkg2.overloaded: .../PyMOTW/pkgutil/develop/demopkg2/overloaded.pyc

..
    Managing Paths with PKG Files
    -----------------------------

PKG ファイルでパスを管理する
----------------------------

..
    The first example above illustrated how to extend the search path
    using extra directories included in the :data:`PYTHONPATH`. It is also
    possible to add to the search path using ``*.pkg`` files containing
    directory names. PKG files are similar to the PTH files used by the
    :mod:`site` module. They can contain directory names, one per line, to
    be added to the search path for the package.

前節の最初のサンプルは、 :data:`PYTHONPATH` にディレクトリを追加して、検索パスを拡張する方法を説明しました。その他にディレクトリ名を含む ``*.pkg`` ファイルを利用して検索パスを追加することもできます。PKG ファイルは、 :mod:`site` モジュールが利用する PTH ファイルとよく似ています。これらのファイルは、パッケージの検索パスを追加するために、1行につき1ディレクトリ名を含みます。

..
    Another way to structure the platform-specific portions of the
    application from the first example is to use a separate directory for
    each operating system, and include a ``.pkg`` file to extend the
    search path.

最初のサンプルからアプリケーションのプラットフォーム固有の部分を構成する別の方法は、各オペレーティングシステム用に別ディレクトリを使用して、検索パスを拡張する ``.pkg`` ファイルを含めます。

..
    This example uses the same :mod:`demopkg1` files, and also includes
    the following files:

このサンプルでは、同じ :mod:`demopkg1` ファイルを使用して、次のファイルも含めます。

::

    $ find os_* -type f
    os_one/demopkg1/__init__.py
    os_one/demopkg1/not_shared.py
    os_one/demopkg1.pkg
    os_two/demopkg1/__init__.py
    os_two/demopkg1/not_shared.py
    os_two/demopkg1.pkg

..
    The PKG files are named ``demopkg1.pkg`` to match the package
    being extended.  They both contain::

PKG ファイルは、拡張されるパッケージ名と一致するように ``demopkg1.pkg`` というファイル名にします。両方とも次の内容を含みます。

::

    demopkg

..
    This demo program shows the version of the module being imported:

このデモプログラムは、インポートされたモジュールのバージョンを表示します。

.. include:: pkgutil_os_specific.py
    :literal:
    :start-after: #end_pymotw_header

..
    A simple run script can be used to switch between the two packages:

シンプルな実行スクリプトを利用して、2つのパッケージ間を切り替えます。

.. include:: with_os.sh
    :literal:
    :start-after: #end_pymotw_header

..
    And when run with ``"one"`` or ``"two"`` as the arguments, the path is
    adjusted appropriately:

引数に ``"one"`` か ``"two"`` を渡して実行すると、そのパスが適切に設定されます。

::

    $ ./with_os.sh one
    PYTHONPATH=os_one

    demopkg1.__path__ before:
    ['.../PyMOTW/pkgutil/demopkg1']

    demopkg1.__path__ after:
    ['.../PyMOTW/pkgutil/demopkg1',
     '.../PyMOTW/pkgutil/os_one/demopkg1',
     'demopkg']

    demopkg1           : .../PyMOTW/pkgutil/demopkg1/__init__.pyc
    demopkg1.shared    : .../PyMOTW/pkgutil/demopkg1/shared.pyc
    demopkg1.not_shared: .../PyMOTW/pkgutil/os_one/demopkg1/not_shared.pyc

::

    $ ./with_os.sh two
    PYTHONPATH=os_two

    demopkg1.__path__ before:
    ['.../PyMOTW/pkgutil/demopkg1']

    demopkg1.__path__ after:
    ['.../PyMOTW/pkgutil/demopkg1',
     '.../PyMOTW/pkgutil/os_two/demopkg1',
     'demopkg']

    demopkg1           : .../PyMOTW/pkgutil/demopkg1/__init__.pyc
    demopkg1.shared    : .../PyMOTW/pkgutil/demopkg1/shared.pyc
    demopkg1.not_shared: .../PyMOTW/pkgutil/os_two/demopkg1/not_shared.pyc

..
    PKG files can appear anywhere in the normal search path, so a
    single PKG file in the current working directory could also be
    used to include a development tree.

PKG ファイルは、通常の検索パスの任意の場所に置けます。カレントのワークディレクトリにある PKG ファイルは、開発ツリーを含めるためにも使用できます。

..
    Nested Packages
    ---------------

ネストされたパッケージ
----------------------

..
    For nested packages, it is only necessary to modify the path of the top-level
    package. For example, with this directory structure

ネストされたパッケージのために、トップレベルパッケージのパスを変更する必要があります。例えば、次のディレクトリ構造では、

::

    $ find nested -name '*.py'
    nested/__init__.py
    nested/second/__init__.py
    nested/second/deep.py
    nested/shallow.py

..
    Where ``nested/__init__.py`` contains

ここで ``nested/__init__.py`` は次のようになります。

.. include:: nested/__init__.py
    :literal:
    :start-after: #end_pymotw_header

..
    and a development tree like

そして、開発ツリーは次のようになります。

::

    $ find develop/nested -name '*.py'
    develop/nested/__init__.py
    develop/nested/second/__init__.py
    develop/nested/second/deep.py
    develop/nested/shallow.py

..
    Both the :mod:`shallow` and :mod:`deep` modules contain a simple
    function to print out a message indicating whether or not they come
    from the installed or development version.

:mod:`shallow` と :mod:`deep` の両モジュールは、そのモジュールがインストール済みバージョンか、開発バージョンかを表すメッセージを出力するシンプルな関数を提供します。

..
    This test program exercises the new packages.

このテストプログラムは、新しいパッケージを実行します。

.. include:: pkgutil_nested.py
    :literal:
    :start-after: #end_pymotw_header

..
    When ``pkgutil_nested.py`` is run without any path manipulation, the
    installed version of both modules are used.

パス操作を行わずに ``pkgutil_nested.py`` が実行されると、両モジュールのインストール済みバージョンが使用されます。

::

    $ python pkgutil_nested.py
    nested.shallow: .../PyMOTW/pkgutil/nested/shallow.pyc
    This func() comes from the installed version of nested.shallow

    nested.second.deep: .../PyMOTW/pkgutil/nested/second/deep.pyc
    This func() comes from the installed version of nested.second.deep

..
    When the ``develop`` directory is added to the path, the development
    version of both functions override the installed versions.

``develop`` ディレクトリがその検索パスに追加されると、開発バージョンの両関数がインストール済みバージョンを上書きします。

::

    $ PYTHONPATH=develop python pkgutil_nested.py 
    nested.shallow: .../PyMOTW/pkgutil/develop/nested/shallow.pyc
    This func() comes from the development version of nested.shallow

    nested.second.deep: .../PyMOTW/pkgutil/develop/nested/second/deep.pyc
    This func() comes from the development version of nested.second.deep

..
    Package Data
    ============

パッケージのデータ
==================

..
    In addition to code, Python packages can contain data files such as
    templates, default configuration files, images, and other supporting
    files used by the code in the package.  The :func:`get_data` function
    gives access to the data in the files in a format-agnostic way, so it
    does not matter if the package is distributed as an EGG, part of a
    frozen binary, or regular files on the filesystem.

コードに加えて、Python パッケージは、テンプレート、デフォルト設定ファイル、画像ファイル、パッケージのコードで使用するその他のファイルといった、データファイルを含められます。 :func:`get_data` 関数は、フォーマットに依存せず、ファイルのデータへのアクセスを提供します。そのため、パッケージが EGG ファイル、バイナリの一部、もしくはファイルシステム上の通常ファイルで配布されるかどうかといったことは問題になりません。

..
    With a package :mod:`pkgwithdata` containing a ``templates`` directory

パッケージ :mod:`pkgwithdata` は ``templates`` ディレクトリを含みます。

::

    $ find pkgwithdata -type f
    
    pkgwithdata/__init__.py
    pkgwithdata/templates/base.html

..
    and ``pkgwithdata/templates/base.html`` containing

そして ``pkgwithdata/templates/base.html`` も含みます。

.. literalinclude:: pkgwithdata/templates/base.html

..
    This program uses :func:`get_data` to retrieve the template contents
    and print them out.

このプログラムは、テンプレートのコンテンツを取り出すために :func:`get_data` を利用して、その内容を表示します。

.. include:: pkgutil_get_data.py
   :literal:
   :start-after: #end_pymotw_header

..
    The arguments to :func:`get_data` are the dotted name of the package,
    and a filename relative to the top of the package.  The return value
    is a byte sequence, so it is encoded as UTF-8 before being printed.

:func:`get_data` の引数は、パッケージのドット名で、パッケージのトップから相対的なファイル名になります。返り値はバイトシーケンスなので、表示する前に UTF-8 でエンコードします。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'pkgutil_get_data.py'))
.. }}}
.. {{{end}}}

..
    :func:`get_data` is distribution format-agnostic because it uses the
    import hooks defined in :pep:`302` to access the package contents.
    Any loader that provides the hooks can be used, including the ZIP
    archive importer in :mod:`zipfile`.

:func:`get_data` は、フォーマット非依存な配布形式です。というのは、パッケージのコンテンツへアクセスするのに :pep:`302` で定義されたインポートフックを使用するからです。インポートフックを提供する任意のローダは、 :mod:`zipfile` の ZIP アーカイブインポータを含めて使用できます。

.. include:: pkgutil_get_data_zip.py
   :literal:
   :start-after: #end_pymotw_header

..
    This example creates a ZIP archive with a copy of the
    :mod:`pkgwithdata` package, including a renamed version of the
    template file.  It then adds the ZIP archive to the import path before
    using :mod:`pkgutil` to load the template and print it.

このサンプルは、テンプレートファイルの名前を変更したファイルを含め、 :mod:`pkgwithdata` パッケージのコピーと一緒に ZIP アーカイブを作成します。それから、テンプレートを読み込むために :mod:`pkgutil` の使用前にインポートパスへ ZIP アーカイブを追加して、そのテンプレートの内容を表示します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'pkgutil_get_data_zip.py'))
.. }}}
.. {{{end}}}


.. seealso::

    `pkgutil <http://docs.python.org/lib/module-pkgutil.html>`_
        .. Standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント

    `virtualenv`_
        .. Ian Bicking's virtual environment script.

        Ian Bicking の仮想環境スクリプト

    :mod:`distutils`
        .. Packaging tools from Python standard library.

        標準ライブラリのパッケージングツール

    `Distribute`_
        .. Next-generation packaging tools.

        次世代パッケージングツール

    :pep:`302`
        .. Import Hooks

        インポートフック

    :mod:`zipfile`
        .. Create importable ZIP archives.

        インポートできる ZIP アーカイブを作成

    :mod:`zipimport`
        .. Importer for packages in ZIP archives.

        ZIP アーカイブからパッケージをインポート

.. _virtualenv: http://pypi.python.org/pypi/virtualenv

.. _Distribute: http://packages.python.org/distribute/
