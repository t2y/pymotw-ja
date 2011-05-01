..
    ================================
    webbrowser -- Displays web pages
    ================================

==================================
webbrowser -- web ページを表示する
==================================

..
    :synopsis: Displays web pages

.. module:: webbrowser
    :synopsis: web ページを表示する

..
    :Purpose: Use the `webbrowser` module to display web pages to your users.
    :Available In: 2.1.3 and later

:目的: ユーザへ web ページを表示するのに `webbrowser` モジュールを使用する
:利用できるバージョン: 2.1.3 以上

..
    The :mod:`webbrowser` module includes functions to open URLs in interactive
    browser applications. The module includes a registry of available
    browsers, in case multiple options are available on the system. It can
    also be controlled with the ``BROWSER`` environment variable.

:mod:`webbrowser` モジュールはインタラクティブなブラウザアプリケーションで URL を開く機能を提供します。このモジュールは、利用可能なブラウザを登録して、システム上で複数のオプションを利用できます。さらに ``BROWSER`` 環境変数で管理することもできます。

..
    Simple Example
    ==============

簡単なサンプル
==============

..
    To open a page in the browser, use the :func:`open()` function.

ブラウザでページを開くには :func:`open()` 関数を使用してください。

.. include:: webbrowser_open.py
    :literal:
    :start-after: #end_pymotw_header

..
    The URL is opened in a browser window, and that window is raised to
    the top of the window stack. The documentation says that an existing
    window will be reused, if possible, but the actual behavior may depend
    on your browser's settings. Using Firefox on my Mac, a new window was
    always created.

ブラウザが指定した URL を開いて、その画面がウィンドウスタックのトップに表示されます。標準ライブラリドキュメントにはできるだけ既存のウィンドウを再利用すると記載されていますが、実際には、ブラウザ設定に依存する可能性があります。私の Mac 上で Firefox を使用すると、毎回、新しいウィンドウが作成されます。

..
    Windows vs. Tabs
    ================

ウィンドウとタブ
================

..
    If you always want a new window used, use :func:`open_new()`.

必ず新しいウィンドウを開きたいなら :func:`open_new()` を使用してください。

.. include:: webbrowser_open_new.py
    :literal:
    :start-after: #end_pymotw_header

..
    If you would rather create a new tab, use :func:`open_new_tab()` instead.

新しいタブを作成したいなら、代わりに :func:`open_new_tab()` を使用してください。

..
    Using a specific browser
    ========================

特殊なブラウザを使用する
========================

..
    If for some reason your application needs to use a specific browser,
    you can access the set of registered browser controllers using the
    :func:`get()` function. The browser controller has methods to
    :func:`open()`, :func:`open_new()`, and :func:`open_new_tab()`. This
    example forces the use of the lynx browser:

何らかの理由でアプリケーションが特殊なブラウザを使用する必要があるなら、 :func:`get()` を使用して登録済みのブラウザコントローラへアクセスできます。ブラウザコントローラは :func:`open()`, :func:`open_new()`, :func:`open_new_tab()` というメソッドがあります。このサンプルは強制的に lynx ブラウザを使用します。

.. include:: webbrowser_get.py
    :literal:
    :start-after: #end_pymotw_header

..
    Refer to the module documentation for a list of available browser
    types.

利用可能なブラウザの種類については標準ライブラリドキュメントを参照してください。

..
    ``BROWSER`` variable
    ====================

``BROWSER`` 変数
================

..
    Users can control the module from outside your application by setting
    the environment variable ``BROWSER`` to the browser names or commands
    to try. The value should consist of a series of browser names
    separated by ``os.pathsep``. If the name includes ``%s``, the name is
    interpreted as a literal command and executed directly with the ``%s``
    replaced by the URL. Otherwise, the name is passed to :func:`get()` to
    obtain a controller object from the registry.

ユーザは、ブラウザ名かコマンドを環境変数 ``BROWSER`` を設定することでアプリケーションの外部からこのモジュールを管理できます。その値は :func:`os.pathsep` で分割される一連のブラウザ名で構成されます。もし ``%s`` という名前を含むなら、その名前はリテラルコマンドとして解釈されて、URL によって置き換えられる ``%s`` で直接的に実行されます。それ以外の場合は、その名前が :func:`get()` へ渡されて、レジストラからコントローラオブジェクトを取り出します。

..
    For example, this command opens the web page in lynx, assuming it is
    available, no matter what other browsers are registered.

例えば、このコマンドは lynx が利用可能であることを前提として lynx で web ページをオープンします。
他のブラウザが登録されていても問題はありません。

::

    $ BROWSER=lynx python webbrowser_open.py 

..
    If none of the names in ``BROWSER`` work, :mod:`webbrowser` falls back
    to its default behavior.

``BROWSER`` 変数に値がセットされていない場合 :mod:`webbrowser` はデフォルトの動作になります。

..
    Command Line Interface
    ======================

コマンドラインインタフェース
============================

..
    All of the features of the :mod:`webbrowser` module are available via
    the command line as well as from within your Python program.

:mod:`webbrowser` モジュールの全ての機能は Python プログラム内から扱うのと同様にコマンドラインからも利用できます。

::

    $ python -m webbrowser   
    Usage: /Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5/webbrowser.py [-n | -t] url
        -n: open new window
        -t: open new tab


.. seealso::

    `webbrowser <http://docs.python.org/lib/module-webbrowser.html>`_
        .. Standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント
