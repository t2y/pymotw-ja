..
    =========================================
    SocketServer -- Creating network servers.
    =========================================

==============================================
SocketServer -- ネットワークサービスを作成する
==============================================

..
    :synopsis: Creating network servers.

.. module:: SocketServer
    :synopsis: ネットワークサービスを作成する

..
    :Purpose: Creating network servers.
    :Python Version: 1.4

:目的: ネットワークサービスを作成する
:Python バージョン: 1.4

..
    The :mod:`SocketServer` module is a framework for creating network
    servers. It defines classes for handling synchronous network requests
    (the server request handler blocks until the request is completed)
    over TCP, UDP, Unix streams, and Unix datagrams. It also provides
    mix-in classes for easily converting servers to use a separate thread
    or process for each request, depending on what is most appropriate for
    your situation.

:mod:`SocketServer` モジュールはネットワークサービスを作成するフレームワークです。TCP, UDP, Unix ストリームや Unix データグラムで(受け取ったリクエストの処理が完了するまでサーバのリクエストハンドラがブロックする)同期ネットワークリクエストを扱うクラスを定義します。さらに状況に応じて、それぞれのリクエストにスレッドかプロセスを使うように簡単にサーバを移行する mix-in クラスも提供します。

..
    Responsibility for processing a request is split between a server
    class and a request handler class. The server deals with the
    communication issues (listing on a socket, accepting connections,
    etc.) and the request handler deals with the "protocol" issues
    (interpreting incoming data, processing it, sending data back to the
    client). This division of responsibility means that in many cases you
    can simply use one of the existing server classes without any
    modifications, and provide a request handler class for it to work with
    your protocol.

1つのリクエストを処理するレスポンス機能はサーバクラスとリクエストハンドラクラスに分割されます。サーバは通信関連の処理(ソケットを listen する、コネクションを accept する等)を扱います。リクエストハンドラは "プロトコル" 関連の処理(入力データを解釈して処理する、クライアントにデータを送り返す)を扱います。このレスポンス機能の分割により、多くのケースにおいて、何の変更もなく既存のサーバクラスの1つをシンプルに使用できて、独自プロトコルと連携するようにリクエストハンドラクラスを提供します。

..
    Server Types
    ============

サーバタイプ
============

..
    There are five different server classes defined in
    :mod:`SocketServer`.  :class:`BaseServer` defines the API, and is not
    really intended to be instantiated and used
    directly. :class:`TCPServer` uses TCP/IP sockets to
    communicate. :class:`UDPServer` uses datagram
    sockets. :class:`UnixStreamServer` and :class:`UnixDatagramServer` use
    Unix-domain sockets and are only available on Unix platforms.

:mod:`SocketServer` モジュールには5つのサーバクラスが定義されています。 :class:`BaseServer` は API を定義しますが、実際にインスタンス化して直接使うことはありません。 :class:`TCPServer` は通信のための TCP/IP ソケットを使用します。 :class:`UDPServer` はデータグラムソケットを使用します。 :class:`UnixStreamServer` と :class:`UnixDatagramServer` は Unix フラットフォームでのみ利用可能な Unix ドメインソケットを使用します。

..
    Server Objects
    ==============

サーバオブジェクト
==================

..
    To construct a server, pass it an address on which to listen for
    requests and a request handler *class* (not instance). The address
    format depends on the server type and the socket family used. Refer to
    the :mod:`socket` module documentation for details.

サーバを構築するには、リクエストを受け付けるアドレスとリクエストハンドラ *クラス* (インスタンスではない) を引数として渡してください。アドレスのフォーマットはサーバタイプと使用されるソケットファミリーに依存します。詳細は :mod:`socket` モジュールのドキュメントを参照してください。

..
    Once the server object is instantiated, use either
    :func:`handle_request()` or :func:`serve_forever()` to process
    requests. The :func:`serve_forever()` method simply calls
    :func:`handle_request()` in an infinite loop, so if you need to
    integrate the server with another event loop or use :func:`select()`
    to monitor several sockets for different servers, you could call
    :func:`handle_request()` on your own. See the example below for more
    detail.

サーバオブジェクトをインスタンス化すると、リクエストを処理するために :func:`handle_request()` か :func:`serve_forever()` のどちらか一方を使用します。 :func:`serve_forever()` メソッドは単純な無限ループで :func:`handle_request()` を呼び出します。そのため、複数サーバの複数ソケットを監視するために別のイベントループか :func:`select()` を使用してサーバを統合する必要があるなら、独自に :func:`handle_request()` を呼び出すことができます。詳細はこの後で紹介するサンプルを見てください。

..
    Implementing a Server
    =====================

サーバを実装する
================

..
    If you are creating a server, it is usually possible to re-use one of
    the existing classes and simply provide a custom request handler
    class. If that does not meet your needs, there are several methods of
    :class:`BaseServer` available to override in a subclass:

サーバを作成するなら通常は既存クラスの1つを再利用して、カスタムリクエストハンドラクラスを提供できます。もしも要望にあわないなら、 :class:`BaseServer` をサブクラス化して利用可能なメソッドをオーバーライドします。

..
    * ``verify_request(request, client_address)`` - Return True to process
      the request or False to ignore it. You could, for example, refuse
      requests from an IP range if you want to block certain clients from
      accessing the server.

* ``verify_request(request, client_address)`` - リクエストを処理すれば True を、無視すれば False を返します。例えば、サーバへのアクセスから特定のクライアントをブロックしたい場合、IP アドレスの範囲を指定してリクエストを拒否します。

..
    * ``process_request(request, client_address)`` - Typically just calls
      :func:`finish_request()` to actually do the work. It can also create
      a separate thread or process, as the mix-in classes do (see below).

* ``process_request(request, client_address)`` - 通常は実際の処理を行う :func:`finish_request()` を呼び出すだけです。mix-in クラスが行うように、スレッドかプロセスかを分割して作成することもできます。(後述)

..
    * ``finish_request(request, client_address)`` - Creates a request
      handler instance using the class given to the server's
      constructor. Calls :func:`handle()` on the request handler to
      process the request.

* ``finish_request(request, client_address)`` - 与えられたクラスからサーバのコンストラクタに対してリクエストハンドラインスタンスを作成します。リクエストを処理するにはリクエストハンドラで :func:`handle()` を呼び出してください。

..
    Request Handlers
    ================

リクエストハンドラ
==================

..
    Request handlers do most of the work of receiving incoming requests and
    deciding what action to take. The handler is responsible for implementing the
    "protocol" on top of the socket layer (for example, HTTP or XML-RPC). The
    request handler reads the request from the incoming data channel, processes
    it, and writes a response back out. There are 3 methods available to be
    over-ridden.

リクエストハンドラは大半の入力リクエストの受信処理を行い、どんなアクションを取るかを決定します。ハンドラはソケット層のトップ(例えば、HTTP や XML-RPC)で "プロトコル" を実装する責任を持ちます。リクエストハンドラは入力データチャンネルからリクエストを読み込み、その処理を行い、レスポンスを書き込みます。次の3つのメソッドが利用可能でオーバーライドされます。

..
    * ``setup()`` - Prepare the request handler for the request. In the
      :class:`StreamRequestHandler`, for example, the :func:`setup()`
      method creates file-like objects for reading from and writing to the
      socket.

* ``setup()`` - リクエストに対するリクエストハンドラを準備します。例えば、 :class:`StreamRequestHandler` では :func:`setup()` メソッドはソケットに対して読み書きするためにファイルのようなオブジェクトを作成します。

..
    * ``handle()`` - Do the real work for the request. Parse the incoming
      request, process the data, and send a response.

* ``handle()`` - リクエストに対して実際の処理を行います。入力リクエストを解析して、処理を行い、レスポンスを送ります。

..
    * ``finish()`` - Clean up anything created during :func:`setup()`.

* ``finish()`` - :func:`setup()` で作成したものをクリーンアップします。

..
    In many cases, you can simply provide a :func:`handle()` method.

多くのケースでは、シンプルに :func:`handle()` を提供します。

..
    Echo Example
    ============

Echo サンプル
=============

..
    Let's look at a simple server/request handler pair that accepts TCP
    connectcions and echos back any data sent by the client. The only
    method that actually needs to be provided in the sample code is
    :func:`EchoRequestHandler.handle()`, but all of the methods described
    above are overridden to insert :mod:`logging` calls so the output of
    the sample program illustrates the sequence of calls made.

TCP コネクションを受け付けて、クライアントから送られたデータをそのまま返すシンプルなサーバ/リクエストハンドラを見てみましょう。サンプルコードで実際に必要なメソッドは :func:`EchoRequestHandler.handle()` のみですが、サンプルプログラムの出力がどの順番で呼び出されるかを解説するために :mod:`logging` を追加するように、前節で説明した全てのメソッドをオーバーライドしています。

..
    The only thing left is to have simple program that creates the
    server, runs it in a thread, and connects to it to illustrate which
    methods are called as the data is echoed back.

あと残っている処理はサーバを作成して、1つのスレッド内で実行し、データがそのまま送り返されるようにどのメソッドが呼び出されるかを理解するためにそのサーバへ接続する、シンプルなプログラムです。

.. include:: SocketServer_echo.py
    :literal:
    :start-after: #end_pymotw_header

..
    The output for the program should look something like this:

このプログラムの出力は次のようになります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'SocketServer_echo.py'))
.. }}}
.. {{{end}}}

..
    The port number used will change each time you run it, as the kernel
    allocates an available port automatically. If you want the server to
    listen on a specific port each time you run it, provide that number in
    the address tuple instead of the ``0``.

使用されるポート番号は実行する度に変わります。カーネルが自動的に利用可能なポート番号を割り当てます。実行するときにサーバに特定のポート番号を指定したいなら、アドレスのタプルに ``0`` ではなく、その番号を指定してください。

..
    Here is a simpler version of the same thing, without the
    :mod:`logging`:

ここに :mod:`logging` を取り除いて同じことをするシンプルなバージョンがあります。

.. include:: SocketServer_echo_simple.py
    :literal:
    :start-after: #end_pymotw_header

..
    In this case, no special server class is required since the
    :mod:`TCPServer` handles all of the server requirements.

このケースでは :mod:`TCPServer` が全てのサーバへの要求を扱うので特別なサーバクラスは必要ありません。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'SocketServer_echo_simple.py'))
.. }}}
.. {{{end}}}

..
    Threading and Forking
    =====================

スレッドとフォーク
==================

..
    Adding threading or forking support to a server is as simple as
    including the appropriate mix-in in the class hierarchy for the
    server. The mix-in classes override :func:`process_request()` to start
    a new thread or process when a request is ready to be handled, and the
    work is done in the new child.

サーバに対してスレッドかフォークの機能を追加するには、サーバのクラス階層で適切な mix-in を含めることでシンプルに実現できます。mix-in クラスはリクエストを扱うときに新たなスレッドかプロセスを生成するために :func:`process_request()` をオーバーライドします。そして、生成されたスレッドかプロセスでその処理が行われます。

..
    For threads, use the :class:`ThreadingMixIn`:

スレッドで扱いたいなら :class:`ThreadingMixIn` を使用してください。

.. include:: SocketServer_threaded.py
    :literal:
    :start-after: #end_pymotw_header

..
    The response from the server includes the id of the thread where the
    request is handled:

サーバからのレスポンスにはリクエストを扱ったスレッドの ID を含みます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'SocketServer_threaded.py'))
.. }}}
.. {{{end}}}

..
    To use separate processes, use the :class:`ForkingMixIn`:

プロセスを分割したいなら :class:`ForkingMixIn` を使用してください。

.. include:: SocketServer_forking.py
    :literal:
    :start-after: #end_pymotw_header

..
    In this case, the process id of the child is included in the response
    from the server:

このケースでは、子プロセスのプロセス ID がサーバからのレスポンスに含められます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'SocketServer_forking.py'))
.. }}}
.. {{{end}}}


.. seealso::

    `SocketServer <http://docs.python.org/lib/module-SocketServer.html>`_
        .. Standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント

    :mod:`asyncore`
        .. Use asyncore to create asynchronous servers that do not block while processing a
           request.

        リクエスト処理中にブロッキングしない非同期サービスを作成するには asyncore を使用してください

    :mod:`SimpleXMLRPCServer`
        .. XML-RPC server built using :mod:`SocketServer`.

        :mod:`SocketServer` で構築する XML-RPC サーバ
