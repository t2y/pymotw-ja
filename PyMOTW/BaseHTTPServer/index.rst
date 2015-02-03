..
    ===========================================================
    BaseHTTPServer -- base classes for implementing web servers
    ===========================================================

==================================================
BaseHTTPServer -- web サーバを実装するベースクラス
==================================================

..
    :synopsis: Provides base classes for implementing web servers.

.. module:: BaseHTTPServer
    :synopsis: web サーバを実装するベースクラス

..
    :Purpose: BaseHTTPServer includes classes that can form the basis of a web server.
    :Available In: 1.4 and later

:目的: BaseHTTPServer は web サーバの基本的なクラスを提供する
:利用できるバージョン: 1.4 以上

..
    :mod:`BaseHTTPServer` uses classes from :mod:`SocketServer` to create
    base classes for making HTTP servers. :class:`HTTPServer` can be used
    directly, but the :class:`BaseHTTPRequestHandler` is intended to be
    extended to handle each protocol method (GET, POST, etc.).

:mod:`BaseHTTPServer` モジュールは、HTTP サーバを構築するベースクラスを作るために :mod:`SocketServer` モジュールのクラスを使用します。 :class:`HTTPServer` は直接的に使用できますが、 :class:`BaseHTTPRequestHandler` は各プロトコルメソッド(GET, POST 等)を扱うように拡張するためにあります。

HTTP GET
========

..
    To add support for an HTTP method in your request handler class,
    implement the method :func:`do_METHOD`, replacing *METHOD* with the
    name of the HTTP method. For example, :func:`do_GET`, :func:`do_POST`,
    etc. For consistency, the method takes no arguments. All of the
    parameters for the request are parsed by
    :class:`BaseHTTPRequestHandler` and stored as instance attributes of
    the request instance.

リクエストハンドラクラスの HTTP メソッドをサポートするために、引数を取らない :func:`do_METHOD` メソッドを実装してください。 *METHOD* の部分は実際の HTTP メソッドの名前に置き換えます。例えば、 :func:`do_GET`, :func:`do_POST` 等になります。一貫性をもたせるためにこれらのメソッドは引数を受け取りません。全てのリクエストのパラメータは :class:`BaseHTTPRequestHandler` へ渡されて、リクエストインスタンスの属性として保持されます。

..
    This example request handler illustrates how to return a response to the
    client and some of the local attributes which can be useful in building the
    response:

このサンプルのリクエストハンドラは、レスポンスを作成するために便利なローカル属性とクライアントへレスポンスを返す方法を説明します。

.. include:: BaseHTTPServer_GET.py
    :literal:
    :start-after: #end_pymotw_header

..
    The message text is assembled and then written to :attr:`wfile`, the
    file handle wrapping the response socket. Each response needs a
    response code, set via :func:`send_response`. If an error code is used
    (404, 501, etc.), an appropriate default error message is included in
    the header, or a message can be passed with the error code.

メッセージのテキストを組み立ててから、レスポンスのソケットをラップするファイルハンドラ :attr:`wfile` へ書き込みます。それぞれのレスポンスは、 :func:`send_response` を通してレスポンスコードをセットする必要があります。エラーコード(404, 501 等)を使用する場合、適切なデフォルトのエラーメッセージがヘッダに含まれるか、またはメッセージがエラーコードで渡されます。

..
    To run the request handler in a server, pass it to the constructor of
    HTTPServer, as in the ``__main__`` processing portion of the sample script.

サーバのリクエストハンドラを実行するには、サンプルスクリプトの ``__main__`` の処理に HTTPServer のコンストラクタへそのハンドラクラスを引数として渡します。

..
    Then start the server:

さぁ、サーバを起動しましょう。

::

    $ python BaseHTTPServer_GET.py 
    Starting server, use <Ctrl-C> to stop

..
    In a separate terminal, use :command:`curl` to access it:

別のターミナルでこのサーバへアクセスするために :command:`curl` コマンドを使用してください。

::

    $ curl -i http://localhost:8080/?foo=barHTTP/1.0 200 OK
    Server: BaseHTTP/0.3 Python/2.5.1
    Date: Sun, 09 Dec 2007 16:00:34 GMT

    CLIENT VALUES:
    client_address=('127.0.0.1', 51275) (localhost)
    command=GET
    path=/?foo=bar
    real path=/
    query=foo=bar
    request_version=HTTP/1.1

    SERVER VALUES:
    server_version=BaseHTTP/0.3
    sys_version=Python/2.5.1
    protocol_version=HTTP/1.0



HTTP POST
=========

..
    Supporting POST requests is a little more work, because the base class
    does not parse the form data for us. The :mod:`cgi` module provides
    the :class:`FieldStorage` class which knows how to parse the form, if
    it is given the correct inputs.

POST リクエストをサポートするにはもう少し大変です。それはベースクラスがフォームデータを解析しないからです。 :mod:`cgi` モジュールは、与えられた入力が正しいときにフォームの解析方法を知っている :class:`FieldStorage` クラスを提供します。

.. include:: BaseHTTPServer_POST.py
    :literal:
    :start-after: #end_pymotw_header

..
    :command:`curl` can include form data in the message it posts to the
    server. The last argument, ``-F datafile=@BaseHTTPServer_GET.py``,
    posts the contents of the file ``BaseHTTPServer_GET.py`` to illustrate
    reading file data from the form.

:command:`curl` コマンドでサーバへ POST するメッセージのフォームデータを作成します。最後の引数 ``-F datafile=@BaseHTTPServer_GET.py`` は、そのフォームからファイルデータを読み込むのを説明するために ``BaseHTTPServer_GET.py`` の内容を POST します。

::

    $ curl http://localhost:8080/ -F name=dhellmann -F foo=bar -F  datafile=@BaseHTTPServer_GET.py
    Client: ('127.0.0.1', 51128)
    Path: /
    Form data:
            name=dhellmann
            foo=bar
            Uploaded datafile (2222 bytes)

..
    Threading and Forking
    =====================

スレッドとフォーク
==================

..
    :class:`HTTPServer` is a simple subclass of
    :class:`SocketServer.TCPServer`, and does not use multiple threads or
    processes to handle requests. To add threading or forking, create a
    new class using the appropriate mix-in from :mod:`SocketServer`.

:class:`HTTPServer` は :class:`SocketServer.TCPServer` のシンプルなサブクラスです。それはリクエストを扱う複数スレッドや複数プロセスを使用しません。スレッドやプロセスをフォークして扱うには、 :mod:`SocketServer` からどちらかのクラスを mix-in して新たなクラスを作成してください。

.. include:: BaseHTTPServer_threads.py
    :literal:
    :start-after: #end_pymotw_header

..
    Each time a request comes in, a new thread or process is created to
    handle it:

リクエストを受け付けると、新たなスレッドかプロセスがそのリクエストを扱うのに作成されます。

::

    $ curl http://localhost:8080/
    Thread-1
    $ curl http://localhost:8080/
    Thread-2
    $ curl http://localhost:8080/
    Thread-3

..
    Swapping :class:`ForkingMixIn` for :class:`ThreadingMixIn` above would
    achieve similar results, using separate processes instead of threads.

..
    Handling Errors
    ===============

エラー制御
==========

..
    Error handling is made easy with :meth:`send_error()`. Simply pass the
    appropriate error code and an optional error message, and the entire
    response (with headers, status code, and body) is generated
    automatically.

エラー制御は :meth:`send_error()` で簡単に行えます。適切なエラーコードと追加のエラーメッセージを単純に渡すと、(ヘッダ、ステータスコード、本文をもつ)完全なレスポンスが自動的に生成されます。

.. include:: BaseHTTPServer_errors.py
    :literal:
    :start-after: #end_pymotw_header

..
    In this case, a 404 error is always returned.

このケースでは、404 エラーが必ず返されます。

::

    $ curl -i http://localhost:8080/
    HTTP/1.0 404 Not Found
    Server: BaseHTTP/0.3 Python/2.5.1
    Date: Sun, 09 Dec 2007 15:49:44 GMT
    Content-Type: text/html
    Connection: close

    <head>
    <title>Error response</title>
    </head>
    <body>
    <h1>Error response</h1>
    <p>Error code 404.
    <p>Message: Not Found.
    <p>Error code explanation: 404 = Nothing matches the given URI.
    </body>

..
    Setting Headers
    ===============

ハンドラ設定
============

..
    The :mod:`send_header` method adds header data to the HTTP response.
    It takes two arguments, the name of the header and the value.

:mod:`send_header` メソッドは HTTP レスポンスへのヘッダデータを追加します。その関数はヘッダ名とその値の2つの引数を取ります。

.. include:: BaseHTTPServer_send_header.py
   :literal:
   :start-after: #end_pymotw_header

..
    This example sets the ``Last-Modified`` header to the current
    timestamp formatted according to :rfc:`2822`.

このサンプルは :rfc:`2822` に準拠したカレントのタイムスタンプに ``Last-Modified`` ヘッダをセットします。

::

    $ curl -i http://localhost:8080/
    HTTP/1.0 200 OK
    Server: BaseHTTP/0.3 Python/2.7
    Date: Sun, 10 Oct 2010 13:58:32 GMT
    Last-Modified: Sun, 10 Oct 2010 13:58:32 -0000
    
    Response body


.. seealso::

    `BaseHTTPServer <http://docs.python.org/library/basehttpserver.html>`_
        .. The standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント

    :mod:`SocketServer`
        .. The SocketServer module provides the base class which handles
           the raw socket connection.

        raw ソケットコネクションを操作するベースクラスを提供する SocketServer モジュール
