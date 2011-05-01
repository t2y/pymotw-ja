..
    =======================================
    pydoc -- Online help for Python modules
    =======================================

============================================
pydoc -- Python モジュールのオンラインヘルプ
============================================

..
    :synopsis: Online help for Python modules

.. module:: pydoc
    :synopsis: Python モジュールのオンラインヘルプ

..
    :Purpose: Generates help for Python modules and classes from the code.
    :Available In: 2.1 and later

:目的: コードから Python モジュールやクラスのヘルプを生成する
:利用できるバージョン: 2.1 以上

..
    The :mod:`pydoc` module imports a Python module and uses the contents
    to generate help text at runtime. The output includes docstrings for
    any objects that have them, and all of the documentable contents of
    the module are described.

:mod:`pydoc` モジュールは Python モジュールをインポートし、実行時にヘルプを生成してそのコンテンツを利用します。任意のオブジェクトの docstrings 出力とモジュールの全ドキュメントコンテンツが記述されます。

..
    Plain Text Help
    ===============

テキストヘルプ
==============

..
    Running::

実行方法::

    $ pydoc atexit

..
    Produces plaintext help on the console, using your pager if one is
    configured.

コンソール上にテキストヘルプを生成します。設定すればページャも使用できます。

..
    HTML Help
    =========

HTML ヘルプ
===========

..
    You can also cause :mod:`pydoc` to generate HTML output, either
    writing a static file to a local directory or starting a web server to
    browse documentation online.

さらに :mod:`pydoc` は HTML 出力も生成できます。ローカルディレクトリの静的ファイルへ書き込むか、オンラインドキュメントをブラウズするために web サーバを起動するかを選べます。

::

    $ pydoc -w atexit

..
    Creates ``atexit.html`` in the current directory.

カレントディレクトリに ``atexit.html`` を作成します。

::

    $ pydoc -p 5000

..
    Starts a web server listening at http://localhost:5000/. The server
    generates documentation as you browse through the available modules.

http://localhost:5000/ で web サーバを起動します。このサーバは利用可能なモジュールをブラウズできるようにドキュメントを生成します。

..
    Interactive Help
    ================

インタラクティブヘルプ
======================

..
    pydoc also adds a function ``help()`` to the ``__builtins__`` so you
    can access the same information from the Python interpreter prompt.

さらに pydoc は ``__builtins__`` に ``help()`` 関数を追加するので、Python インタープリタプロンプトから同じ情報にアクセスできます。

::

    $ python
    Python 2.6.2 (r262:71600, Apr 16 2009, 09:17:39) 
    [GCC 4.0.1 (Apple Computer, Inc. build 5250)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> help('atexit')
    Help on module atexit:

    NAME
        atexit

    FILE
        /Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/atexit.py
    ...

.. seealso::

    `pydoc <http://docs.python.org/library/pydoc.html>`_
        .. The standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント

    :ref:`motw-cli`
        .. Accessing the Module of the Week articles from the command line.

        コマンドラインから PyMOTW の記事へアクセスする

    :ref:`motw-interactive`
        .. Accessing the Module of the Week articles from the interactive interpreter.

        Python インタラクティブインタープリタから PyMOTW の記事へアクセスする
