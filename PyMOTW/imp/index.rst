..
    ============================================
    imp -- Interface to module import mechanism.
    ============================================

=======================================================
imp -- モジュールのインポート構造に対するインタフェース
=======================================================

..
    :synopsis: Interface to module import mechanism.

.. module:: imp
    :synopsis: モジュールのインポート構造に対するインタフェース

..
    :Purpose: 
        The imp module exposes the implementation of Python's import statement.
    :Available In: At least 2.2.1

:目的: imp モジュールは Python の import 文の実装を公開する
:利用できるバージョン: 2.2.1 以上

..
    The imp module includes functions that expose part of the underlying
    implementation of Python's import mechanism for loading code in packages and
    modules. It is one access point to importing modules dynamically, and useful
    in some cases where you don't know the name of the module you need to import
    when you write your code (e.g., for plugins or extensions to an application).

imp モジュールにはパッケージやモジュールでコードを読み込む Python のインポート構造における下位実装を公開する機能があります。それは動的にインポートしたモジュールへの1つのアクセスポイントです。そして、コード(例えば、アプリケーションのプラグイン、又は拡張機能)を書くときにインポートする必要のあるモジュール名を知らないときに役立ちます。

..
    Example Package
    ===============

example パッケージ
==================

..
    The examples below use a package called "example" with ``__init__.py``:

次のサンプルは ``__init__.py`` で "example" というパッケージを使用します。

.. include:: example/__init__.py
    :literal:
    :start-after: #end_pymotw_header

..
    and module called submodule containing:

そして、submodule というモジュールも含みます。

.. include:: example/submodule.py
    :literal:
    :start-after: #end_pymotw_header

..
    Watch for the text from the print statements in the sample output when
    the package or module are imported.

パッケージ又はモジュールがインポートされたときに出力する print 文のテキストに注目してください。

..
    Module Types
    ============

モジュールタイプ
================

..
    Python supports several styles of modules. Each requires its own handling when
    opening the module and adding it to the namespace. Some of the supported types
    and those parameters can be listed by the ``get_suffixes()`` function.

Python はモジュールの複数のスタイルをサポートします。モジュールをオープンして名前空間へそのモジュールを追加するときに、モジュールタイプそれぞれの要素独自の操作を必要とします。サポートされているタイプとそのパラメータは ``get_suffixes()`` 関数で表示することができます。

.. include:: imp_get_suffixes.py
    :literal:
    :start-after: #end_pymotw_header

..
    ``get_suffixes()`` returns a sequence of tuples containing the file
    extension, mode to use for opening the file, and a type code from a
    constant defined in the module. This table is incomplete, because some
    of the importable module or package types do not correspond to single
    files.

``get_suffixes()`` はファイル拡張子、ファイルを開くために使用するモード、そしてモジュールで定義された定数のタイプコードを含むタプルのリストを返します。このテーブルは不完全です。というのは、インポート可能なモジュール又はパッケージのタイプは1つのファイルに対応しないからです。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'imp_get_suffixes.py'))
.. }}}
.. {{{end}}}

..
    Finding Modules
    ===============

モジュールを見つける
====================

..
    The first step to loading a module is finding it. ``find_module()``
    scans the import search path looking for a package or module with the
    given name. It returns an open file handle (if appropriate for the
    type), filename where the module was found, and "description" (a tuple
    such as those returned by ``get_suffixes()``).

モジュールを読み込むための最初のステップはそのモジュールを見つけることです。 ``find_module()`` はインポートされた検索パスを精査して、与えられた名前からパッケージ又はモジュールを探します。 ``find_module()`` は(そのタイプが適切なら)ファイルハンドラ、モジュールを見つけたファイル名、そして "description"( ``get_suffixes()`` が返すタプル) を返します。

.. include:: imp_find_module.py
    :literal:
    :start-after: #end_pymotw_header

..
    ``find_module()`` does not pay attention to dotted package names
    ("example.submodule"), so the caller has to take care to pass the
    correct path for any nested modules. That means that when importing
    the submodule from the package, you need to give a path that points to
    the package directory for ``find_module()`` to locate the module
    you're looking for.

``find_module()`` はドットを含むパッケージ名("example.submodule")には注意しません。そのため、呼び出し側はネストされたモジュールの正しいパスを渡すことに注意する必要があります。パッケージからサブモジュールをインポートする場合、探しているモジュールを配置するために ``find_module()`` にパッケージのディレクトリパスを渡す必要があります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'imp_find_module.py'))
.. }}}
.. {{{end}}}

..
    If ``find_module()`` cannot locate the module, it raises an
    :ref:`ImportError <exceptions-ImportError>`.

もし ``find_module()`` がそのモジュールを配置できなかったら :ref:`ImportError <exceptions-ImportError>` を発生させます。

.. include:: imp_find_module_error.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'imp_find_module_error.py'))
.. }}}
.. {{{end}}}

..
    Loading Modules
    ===============

モジュールを読み込む
====================

..
    Once you have found the module, use ``load_module()`` to actually
    import it.  ``load_module()`` takes the full dotted path module name
    and the values returned by ``find_module()`` (the open file handle,
    filename, and description tuple).

モジュールを見つけたら、実際にそのモジュールをインポートするために ``load_module()`` を使用してください。 ``load_module()`` は完全にドットで区切られたパスのモジュール名と ``find_module()`` が返す値(ファイルハンドラ、ファイル名、説明のタプル)を引数に取ります。

.. include:: imp_load_module.py
    :literal:
    :start-after: #end_pymotw_header

..
    ``load_module()`` creates a new module object with the name given,
    loads the code for it, and adds it to :ref:`sys.modules
    <sys-modules>`.

``load_module()`` は与えられた名前でモジュールのコードを読み込んで新たなモジュールオブジェクトを作成します。そして :ref:`sys.modules <sys-modules>` にモジュールを追加します。

.. Do not use cog for this example because the path changes.

::

	$ python imp_load_module.py
	Importing example package
	Package: <module 'example' from '/Users/dhellmann/Documents/PyMOTW/trunk/PyMOTW/imp/example/__init__.py'>
	Importing submodule
	Sub-module: <module 'example.module' from '/Users/dhellmann/Documents/PyMOTW/trunk/PyMOTW/imp/example/submodule.py'>

..
    If you call ``load_module()`` for a module which has already been
    imported, the effect is like calling ``reload()`` on the existing
    module object.

既にインポートされているモジュールに対して ``load_module()`` を呼び出すと、既存のモジュールオブジェクトに ``reload()`` を呼び出すような結果になります。

.. include:: imp_load_module_reload.py
    :literal:
    :start-after: #end_pymotw_header

..
    Instead of a creating a new module, the contents of the existing
    module are simply replaced.

新たなモジュールを作成する代わりに、既存モジュールのコンテンツを単純に置き換えます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'imp_load_module_reload.py'))
.. }}}
.. {{{end}}}

..
    `imp <http://docs.python.org/library/imp.html>`_
        The standard library documentation for this module.
    :ref:`sys-imports`
        Import hooks, the module search path, and other related machinery.
    :mod:`inspect`
        Load information from a module programmatically.
    :pep:`302`
        New import hooks.
    :pep:`369`
        Post import hooks.

.. seealso::

    `imp <http://docs.python.org/library/imp.html>`_
        本モジュールの標準ライブラリドキュメント
        
    :ref:`sys-imports`
        インポートフック、モジュールのパス検索、その他の関連する仕組み

    :mod:`inspect`
        モジュールプログラムから情報を読み込む

    :pep:`302`
        新たなインポートフック

    :pep:`369`
        インポートフックの投稿
