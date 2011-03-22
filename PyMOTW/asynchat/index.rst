..
    =========================================
    asynchat -- Asynchronous protocol handler
    =========================================

====================================
asynchat -- 非同期プロトコルハンドラ
====================================

..
    :synopsis: Asynchronous protocol handler

.. module:: asynchat
    :synopsis: 非同期プロトコルハンドラ

..
    :Purpose: Asynchronous network communication protocol handler
    :Python Version: 1.5.2 and later

:目的: 非同期ネットワーク通信プロトコルハンドラ
:Python バージョン: 1.5.2 以上

..
    The :mod:`asynchat` module builds on :mod:`asyncore` to make it easier
    to implement protocols based on passing messages back and forth
    between server and client. The :class:`async_chat` class is an
    :class:`asyncore.dispatcher` subclass that receives data and looks for
    a message terminator. Your subclass only needs to specify what to do
    when data comes in and how to respond once the terminator is
    found. Outgoing data is queued for transmission via FIFO objects
    managed by :class:`async_chat`.

:mod:`asynchat` モジュールは :mod:`asyncore` 上で構築されるサーバクライアント間でメッセージのやり取りに基づいたプロトコルを簡単に実装します。 :class:`async_chat` クラスは、データを受け取り、メッセージターミネイタを探す :class:`asyncore.dispatcher` のサブクラスです。そのサブクラスは、データを受け取ったときに何をするかと、ターミネイタを見つけたときにどう応答するかの2つのみ指定する必要があります。送信するデータは :class:`async_chat` が管理する FIFO オブジェクトを経由して転送キューに追加されます。

..
    Message Terminators
    ===================

メッセージターミネイタ
======================

..
    Incoming messages are broken up based on *terminators*, controlled for
    each instance via :func:`set_terminator()`. There are three possible
    configurations:

受け取ったメッセージは *ターミネイタ* に基づいて分割されて、 :func:`set_terminator()` を通してそれぞれのインスタンスで管理されます。設定方法は3つあります。

..
    1. If a string argument is passed to :func:`set_terminator()`, the
       message is considered complete when that string appears in the
       input data.

1. :func:`set_terminator()` に文字列の引数が渡された場合、入力データにその文字列が現れたときにメッセージが完了したと見なされます。

..
    2. If a numeric argument is passed, the message is considered complete
       when that many bytes have been read.

2. 数値の引数が渡された場合、そのバイト数を読み込んだときにメッセージが完了したと見なされます。

..
    3. If ``None`` is passed, message termination is not managed by
       :class:`async_chat`.

3. ``None`` が渡された場合、 :class:`async_chat` はメッセージの完了を管理しません。

..
    The :class:`EchoServer` example below uses both a simple string
    terminator and a message length terminator, depending on the context
    of the incoming data. The HTTP request handler example in the standard
    library documentation offers another example of how to change the
    terminator based on the context to differentiate between HTTP headers
    and the HTTP POST request body.

次の :class:`EchoServer` サンプルは、入力データのコンテキストに依存するシンプルな文字列ターミネイタとメッセージ長ターミネイタの2つを使用します。標準ライブラリドキュメントにある HTTP リクエストハンドラのサンプルは、HTTP ヘッダと HTTP POST リクエストの本文の間で異なるコンテキストに基づいてターミネイタを変更する方法を紹介します。

..
    Server and Handler
    ==================

サーバとハンドラ
================

..
    To make it easier to understand how :mod:`asynchat` is different from
    :mod:`asyncore`, the examples here duplicate the functionality of the
    :class:`EchoServer` example from the :mod:`asyncore` discussion. The
    same pieces are needed: a server object to accept connections, handler
    objects to deal with communication with each client, and client
    objects to initiate the conversation.

:mod:`asynchat` と :mod:`asyncore` の違いを簡単に説明するために、 :mod:`asyncore` の記事から同じ :class:`EchoServer` サンプルを紹介します。サーバオブジェクトはコネクションを受け付ける、ハンドラオブジェクトはそれぞれのクライアントとの通信を扱う、クライアントオブジェクトは通信を開始するといった同じ役割を担います。

..
    The :class:`EchoServer` needed to work with :mod:`asynchat` is
    essentially the same as the one created for the :mod:`asyncore`
    example, with fewer :mod:`logging` calls because they are less
    interesting this time around:

:mod:`asynchat` で動作する :class:`EchoServer` は、今回はあまり関係ない :mod:`logging` の呼び出す回数を少なくして、 :mod:`asyncore` のサンプルと同様に同じオブジェクトを作成します。

.. include:: asynchat_echo_server.py
    :literal:
    :start-after: #end_pymotw_header

..
    The :class:`EchoHandler` is based on ``asynchat.async_chat`` instead
    of the :class:`asyncore.dispatcher` this time around. It operates at a
    slightly higher level of abstraction, so reading and writing are
    handled automatically. The buffer needs to know four things:

このサンプルは :class:`asyncore.dispatcher` ではなく ``asynchat.async_chat`` をベースクラスとする :class:`EchoHandler` です。それはわずかに高レベルの抽象化を行って操作するので、読み書きは自動的に扱われます。そのバッファは次の4つを知っている必要があります。

..
    - what to do with incoming data (by overriding
      :func:`handle_incoming_data()`)
    - how to recognize the end of an incoming message (via
      :func:`set_terminator()`)
    - what to do when a complete message is received (in
      :func:`found_terminator()`)
    - what data to send (using :func:`push()`)

- (:func:`handle_incoming_data()` をオーバーライドすることで) 入力データで何をするか
- (:func:`set_terminator()` 経由の) 入力メッセージの終わりをどうやって認識するか
- (:func:`found_terminator()` で) メッセージが完了したときに何をするか
- (:func:`push()` を使用して) 何を送信するか 

..
    The example application has two operating modes. It is either waiting
    for a command of the form ``ECHO length\n``, or waiting for the data
    to be echoed. The mode is toggled back and forth by setting an
    instance variable *process_data* to the method to be invoked when the
    terminator is found and then changing the terminator as appropriate.

サンプルアプリケーションは2つの操作モードがあります。1つは ``ECHO length\n`` フォームのコマンドを待つか、もう1つは送り返されるデータを待つかです。このモードは、ターミネイタが見つかった後で必要に応じてターミネイタを変更するときに、実行されるメソッドに対するインスタンス変数 *process_data* の設定によって交互に変わります。

.. include:: asynchat_echo_handler.py
    :literal:
    :start-after: #end_pymotw_header

..
    Once the complete command is found, the handler switches to
    message-processing mode and waits for the complete set of text to be
    received. When all of the data is available, it is pushed onto the
    outgoing channel and set up the handler to be closed once the data is
    sent.

完了コマンドが見つかると、ハンドラはメッセージ処理モードを切り替えて、テキストセット全体を受信するのを待ちます。全てのデータを受信すると、送信チャンネルへ追加されて、そのデータを送信したら閉じるようにハンドラを設定します。

..
    Client
    ======

クライアント
============

..
    The client works in much the same way as the handler. As with the
    :mod:`asyncore` implementation, the message to be sent is an argument
    to the client's constructor. When the socket connection is
    established, :func:`handle_connect()` is called so the client can send
    the command and message data.

クライアントは、ほとんどハンドラと同様に動作します。 :mod:`asyncore` の実装と同様に、その送信メッセージはクライアントのコンストラクタへの引数です。ソケットのコネクションが確立されると、 :func:`handle_connect()` が呼び出されるので、クライアントはコマンドとメッセージデータを送れます。

..
    The command is pushed directly, but a special "producer" class is used
    for the message text. The producer is polled for chunks of data to
    send out over the network. When the producer returns an empty string,
    it is assumed to be empty and writing stops.

そのコマンドは直接追加されますが、メッセージテキストには特別な "producer" クラスを使用します。producer は、ネットワーク上で送信するためにデータのチャンクをポーリングします。producer が空文字を返すとき、それはデータがなくなり、停止を書き込んだと想定します。

..
    The client expects just the message data in response, so it sets an
    integer terminator and collects data in a list until the entire
    message has been received.

クライアントは、応答のメッセージデータをただ待ち続けるので、整数ターミネイタを設定して、メッセージ全体を受信するまでリストにデータを追加します。

.. include:: asynchat_echo_client.py
    :literal:
    :start-after: #end_pymotw_header

..
    Putting It All Together
    =======================

全てひとつにまとめる
====================

..
    The main program for this example sets up the client and server in the
    same :mod:`asyncore` main loop.

このサンプルのメインプログラムは、同じ :mod:`asyncore` メインループ内にクライアントとサーバを設定します。

.. include:: asynchat_echo_main.py
    :literal:
    :start-after: #end_pymotw_header

..
    Normally you would have them in separate processes, but this makes it
    easier to show the combined output.

普通は、独立したプロセスでクライアントやサーバを実行しますが、こうすることで簡単にログ出力を組み合わせて表示できます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'asynchat_echo_main.py'))
.. }}}
.. {{{end}}}


.. seealso::

    `asynchat <http://docs.python.org/library/asynchat.html>`_
        .. The standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント

    :mod:`asyncore`
        .. The asyncore module implements an lower-level asynchronous I/O
           event loop.

        低レベルの非同期 I/O イベントループを実装する asyncore モジュール
