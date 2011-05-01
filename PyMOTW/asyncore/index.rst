..
    ====================================
    asyncore -- Asynchronous I/O handler
    ====================================

===============================
asyncore -- 非同期 I/O ハンドラ
===============================

..
    :synopsis: Asynchronous I/O handler

.. module:: asyncore
    :synopsis: 非同期 I/O ハンドラ

..
    :Purpose: Asynchronous I/O handler
    :Available In: 1.5.2 and later

:目的: 非同期 I/O ハンドラ
:利用できるバージョン: 1.5.2 以上

..
    The asyncore module includes tools for working with I/O objects such as sockets so they can be managed asynchronously (instead of, for example, using threads).  The main class provided is :class:`dispatcher`, a wrapper around a socket that provides hooks for handling events like connecting, reading, and writing when invoked from the main loop function, :func:`loop`.

:mod:`asyncore` モジュールは、(例えば、スレッドを使用せずに)非同期で制御できるように、ソケットのような非同期 I/O オブジェクトを扱うツールを提供します。主なクラスは :class:`dispatcher` です。そのクラスは :func:`loop` のようなメインループ関数から実行されるコネクション接続や読み書きといったイベントを操作するフックを提供するソケット周りのラッパーです。

..
    Clients
    =======

クライアント
============

..
    To create an asyncore-based client, subclass :class:`dispatcher` and provide implementations for creating the socket, reading, and writing.  Let's examine this HTTP client, based on the one from the standard library documentation.

asyncore ベースのクライアントを作成するには :class:`dispatcher` のサブクラスで、ソケットの作成、読み書きの実装を提供します。標準ライブラリドキュメントで紹介されている、この HTTP クライアントを検証してみましょう。

.. include:: asyncore_http_client.py
    :literal:
    :start-after: #end_pymotw_header

..
    First, the socket is created in ``__init__()`` using the base class method ``create_socket()``.  Alternative implementations of the method may be provided, but in this case we want a TCP/IP socket so the base class version is sufficient.

まずソケットはベースクラスのメソッド :func:`create_socket` を使用して :func:`__init__` で作成されます。このメソッドの代替実装もあるでしょうが、このケースでは TCP/IP ソケットが必要なのでベースクラスのメソッドで十分です。

..
    The ``handle_connect()`` hook is present simply to illustrate when it is called.  Other types of clients that need to do some sort of hand-shaking or protocol negotiation should do the work in ``handle_connect()``.

:func:`handle_connect` のフックは、この処理が呼び出されたことが単純に分かるために実装しています。何らかのハンドシェイクか、プロトコルネゴシエーションをする必要があるクライアントの場合は :func:`handle_connect` で処理を実装します。

..
    ``handle_close()`` is similarly presented for the purposes of showing when the method is called.  The base class version closes the socket correctly, so if you don't need to do extra cleanup on close you can leave the method out.

同様に :func:`handle_close` もこのメソッドが呼び出されたときにそのことを表示する目的で実装しています。ベースクラスバージョンは正常にソケットをクローズするので、クローズ時に追加のクリーンアップ処理をする必要がないなら、このメソッドを取り除けます。

..
    The asyncore loop uses ``writable()`` and its sibling method ``readable()`` to decide what actions to take with each dispatcher.  Actual use of poll() or select() on the sockets or file descriptors managed by each dispatcher is handled inside the :mod:`asyncore` code, so you don't need to do that yourself.  Simply indicate whether the dispatcher cares at all about reading or writing.  In the case of this HTTP client, ``writable()`` returns True as long as there is data from the request to send to the server.  ``readable()`` always returns True because we want to read all of the data.

asyncore ループは、それぞれのディスパッチャがどのような処理をするかを決めるために :func:`writable` とその兄弟メソッドの :func:`readable` を使用します。実際には、それぞれのディスパッチャが管理するソケットかファイルディスクリプタ上で :func:`poll` か :func:`select` を使用して :mod:`asyncore` コードの内部で操作されます。そのため、自分でそういった処理を行う必要はありません。ディスパッチャに読み込みか、書き込みかを単純に指示してください。この HTTP クライアントのケースでは、 :func:`writable` はサーバへ送られるリクエストにデータが存在する限り、True を返します。 :func:`readable` は、全てのデータを読み込むので常に True を返します。

..
    Each time through the loop when ``writable()`` responds positively, ``handle_write()`` is invoked.  In this version, the HTTP request string that was built in ``__init__()`` is sent to the server and the write buffer is reduced by the amount successfully sent.

そのループを通して確実に :func:`writable` が応答するときに :func:`handle_write` が実行されます。このバージョンでは、 :func:`__init__` で作成された HTTP リクエストの文字列はサーバへ送られて、正常に送られることで書き込みバッファが減少します。

..
    Similarly, when ``readable()`` responds positively and there is data to read, ``handle_read()`` is invoked.

同様に :func:`readable` が確実に応答するときは読み込むデータがあり :func:`handle_read` が実行されます。

..
    The example below the ``__main__`` test configures logging for debugging then creates two clients to download two separate web pages.  Creating the clients registers them in a "map" kept internally by asyncore.  The downloading occurs as the loop iterates over the clients.  When the client reads 0 bytes from a socket that seems readable, the condition is interpreted as a closed connection and ``handle_close()`` is called.

サンプルの :func:`__main__` は、デバッグ用のロギング設定をテストしてから、2つの web ページをダウンロードする2つのクライアントを作成します。クライアントを作成するには、内部的に asyncore が管理する "map" にこれらのクライアントを登録します。ダウンロード処理はクライアントを繰り返し処理するループとして作成します。クライアントが読み込み用のソケットから 0 バイト読み込むときに、コネクションがクローズされたと解釈されて :func:`handle_close` が呼び出されます。

..
    One example of how this client app may run is:

このクライアントがどのように実行されるかの1つの例です

.. {{{cog
.. cog.out(run_script(cog.inFile, 'asyncore_http_client.py'))
.. }}}
.. {{{end}}}

..
    Servers
    =======

サーバ
======

..
    The example below illustrates using asyncore on the server by re-implementing the EchoServer from the :mod:`SocketServer` examples.  There are three classes: ``EchoServer`` receives incoming connections from clients and creates ``EchoHandler`` instances to deal with each.  The ``EchoClient`` is an asyncore dispatcher similar to the HttpClient defined above.

次のサンプルは、 :mod:`SocketServer` のサンプルから EchoServer を再実装することで、サーバでの asyncore の使用方法を説明します。3つのクラスがあります。 ``EchoServer`` はクライアントからコネクションを受け取り、それぞれのコネクションを扱う ``EchoHandler`` インスタンスを作成します。 ``EchoClient`` は、前説で紹介した HTTP クライアントと同様の asyncore のディスパッチャです。

.. include:: asyncore_echo_server.py
    :literal:
    :start-after: #end_pymotw_header

..
    The EchoServer and EchoHandler are defined in separate classes because they do different things.  When EchoServer accepts a connection, a new socket is established.  Rather than try to dispatch to individual clients within EchoServer, an EchoHandler is created to take advantage of the socket map maintained by asyncore.

EchoServer と EchoHandler は、違う処理を行うので別々のクラスで定義されます。EchoServer がコネクションを受け付けると、新たなソケットが作成されます。EchoServer 内部から個々のクライアントへディスパッチしようと試みるというよりも、asyncore が管理するソケットマップを活用して EchoHandler が作成されます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'asyncore_echo_server.py'))
.. }}}
.. {{{end}}}

..
    In this example the server, handler, and client objects are all being maintained in the same socket map by asyncore in a single process. To separate the server from the client, simply instantiate them from separate scripts and run ``asyncore.loop()`` in both. When a dispatcher is closed, it is removed from the map maintained by asyncore and the loop exits when the map is empty.

このサンプルのサーバ、ハンドラ、クライアントオブジェクトは、1つのプロセス内で asyncore が全て同じソケットマップで管理します。クライアントとサーバを分割するには、単純にスクリプトを分割して両方のスクリプトで :func:`asyncore.loop`` を実行してください。あるディスパッチャがクローズされると、asyncore が管理するマップから削除されて、そのマップが空っぽになったときにループが終了します。

..
    Working with Other Event Loops
    ==============================

その他のイベントループを扱う
============================

..
    It is sometimes necessary to integrate the asyncore event loop with an event loop from the parent application.  For example, a GUI application would not want the UI to block until all asynchronous transfers are handled -- that would defeat the purpose of making them asynchronous.  To make this sort of integration easy, ``asyncore.loop()`` accepts arguments to set a timeout and to limit the number of times the loop is run.  We can see their effect on the client by re-using HttpClient from the first example.

時々、親アプリケーションのイベントループから asyncore のイベントループを統合する必要があります。例えば、GUI アプリケーションは、全ての非同期通信の処理されるまで待つように UI をブロックしたくありません。ブロックしてしまうと、非同期に処理させる意味がありません。このような統合を簡単にするために、 :func:`asyncore.loop` の引数に timeout を設定して、そのループを実行する時間を制限します。

.. include:: asyncore_loop.py
    :literal:
    :start-after: #end_pymotw_header

..
    Here we see that the client is only asked to read or data once per call into ``asyncore.loop()``.  Instead of our own ``while`` loop, we could call ``asyncore.loop()`` like this from a GUI toolkit idle handler or other mechanism for doing a small amount of work when the UI is not busy with other event handlers.

このクライアントは :func:`asyncore.loop` 内で呼び出すごとにデータを読み込むかを訪ねます。その UI が他のイベントハンドラの処理を行っていないとき、小さな処理を行うには GUI ツールキットのアイドルハンドラかその他の仕組みから、独自の ``while`` ループではなく :func:`asyncore.loop` を呼び出せます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'asyncore_loop.py'))
.. }}}
.. {{{end}}}

..
    Working with Files
    ==================

ファイルを扱う
==============

..
    Normally you would want to use asyncore with sockets, but there are times when it is useful to read files asynchronously, too (to use files when testing network servers without requiring the network setup, or to read or write large data files in parts).  For these situations, asyncore provides the :class:`file_dispatcher` and :class:`file_wrapper` classes.

普通はソケットで asyncore を使用しますが、非同期にファイルを読み込めると便利なときもあります(ネットワーク設定せずにネットワークサービスをテストするときにファイルを使用する、もしくは巨大なデータファイルを読み書きする処理の一部等)。このような処理のために asyncore は :class:`file_dispatcher` と :class:`file_wrapper` クラスを提供します。

.. include:: asyncore_file_dispatcher.py
    :literal:
    :start-after: #end_pymotw_header

..
    This example was tested under Python 2.5.2, so I am using ``os.open()`` to get a file descriptor for the file.  For Python 2.6 and later, ``file_dispatcher`` automatically converts anything with a ``fileno()`` method to a file descriptor.

このサンプルは Python 2.5.2 でテストしたので、ファイルディスクリプタを取得するために ``os.open()`` を使用しました。Python 2.6 以上では ``file_dispatcher`` がファイルディスクリプタへの ``fileno()`` メソッドで自動的に変換されます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'asyncore_file_dispatcher.py'))
.. }}}
.. {{{end}}}


.. seealso::

    `asyncore <http://docs.python.org/library/asyncore.html>`_
        .. The standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント
    
    :mod:`asynchat`
        .. The asynchat module builds on asyncore to make it easier to create clients
           and servers communicate by passing messages back and forth using a set protocol.

        asyncore 上で構築されるサーバクライアント間でメッセージのやり取りに基づいたプロトコルを簡単に実装する asynchat モジュール

    :mod:`SocketServer`
        .. The SocketServer module article includes another example of the EchoServer with
           threading and forking variants.

        スレッドとフォークを使用して別の EchoServer のサンプルを提供する SocketServer モジュール
