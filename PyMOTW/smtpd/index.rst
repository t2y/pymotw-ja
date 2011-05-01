..
    ============================
    smtpd -- Sample SMTP Servers
    ============================

=============================
smtpd -- サンプル SMTP サーバ
=============================

..
    :synopsis: Includes classes for implementing SMTP servers.

.. module:: smtpd
    :synopsis: SMTP サーバを実装するクラスを提供する

..
    :Purpose: Includes classes for implementing SMTP servers.
    :Available In: 2.1 and later

:目的: SMTP サーバを実装するクラスを提供する
:利用できるバージョン: 2.1 以上

..
    The :mod:`smtpd` module includes classes for building simple mail
    transport protocol servers.  It is the server-side of the protocol
    used by :mod:`smtplib`.

:mod:`smtpd` モジュールは SMTP (簡易メール転送プロトコル) サーバを構築するためのクラスを提供します。それは :mod:`smtplib` が使用するプロトコルのサーバ側のプログラムです。

..
    SMTPServer
    ==========

SMTP サーバ
===========

..
    The base class for all of the provided example servers is
    :class:`SMTPServer`.  It handles communicating with the client,
    receiving the data, and provides a convenient hook to override to
    handle the message once it is fully available.

:class:`SMTPServer` は全てのサンプルサーバのベースクラスになります。それはクライアントとの通信を制御してデータを受信します。そして、データを完全に受信すると、そのメッセージ操作をオーバライドする便利なフックを提供します。

..
    The constructor arguments are the local address to listen for
    connections and the remote address for proxying.  The method
    :func:`process_message()` is provided as a hook to be overridden by
    your derived class.  It is called when the message is completely
    received, and given these arguments:

コンストラクタの引数はクライアントからの接続を listen するローカルアドレスとプロキシのリモートアドレスです。 :func:`process_message()` メソッドは派生したサブクラスでオーバーライドされるフックとして提供されます。そのメソッドはメッセージを完全に受信したときに呼び出されて、次の引数を受け取ります。

peer

  .. The client's address, a tuple containing IP and incoming port.

  クライアントのアドレス、IP アドレスと入力ポート番号のタプルです。

mailfrom

  .. The "from" information out of the message envelope, given to the
     server by the client when the message is delivered.  This does not
     necessarily match the ``From`` header in all cases.

  メッセージエンベロープから取り出された "from" の情報です。メッセージが配信されるときにクライアントからサーバへ渡されます。この情報は必ずしもメールヘッダの ``From`` と一致するというわけではありません。

rcpttos

  .. The list of recipients from the message envelope.  Again, this does
     not always match the ``To`` header, especially if someone is blind
     carbon copied.

  メッセージエンベロープの受取人のリストです。繰り返しますが、この情報も必ずしもメールヘッダの ``To`` と一致するわけではありません。例えば BCC の場合が一致しません。

data

  .. The full :rfc:`2822` message body.

  :rfc:`2822` 完全準拠のメッセージ本文です。

..
    Since the default implementation of :func:`process_message()` raises
    :ref:`NotImplementedError <exceptions-NotImplementedError>`, to
    demonstrate using :class:`SMTPServer` we need to create a subclass and
    provide a useful implementation.  This first example defines a server
    that prints information about the messages it receives.

:func:`process_message()` のデフォルト実装は :ref:`NotImplementedError <exceptions-NotImplementedError>` を発生させるので、 :class:`SMTPServer` を使用して実行するには、サブクラスとそのメソッドの実装を作成する必要があります。最初のサンプルは受信したメッセージに関する情報を表示するサーバです。

.. include:: smtpd_custom.py
    :literal:
    :start-after: #end_pymotw_header

..
    :class:`SMTPServer` uses :mod:`asyncore`, so to run the server we call
    ``asyncore.loop()``.

:class:`SMTPServer` は :mod:`asyncore` を使用するので、そのサーバを実行するために ``asyncore.loop()`` を呼び出します。

..
    Now, we need a client to send data.  By adapting one of the examples
    from the :mod:`smtplib` page, we can set up a client to send data to
    our test server running locally on port 1025.

ここでデータを送信するクライアントが必要です。 :mod:`smtplib` ページから適応するサンプルを使用して、ローカルホストの 1025 番ポートで実行したテストサーバへデータを送信するクライアントを設定します。

.. include:: smtpd_senddata.py
    :literal:
    :start-after: #end_pymotw_header

..
    Now if we run ``smtpd_custom.py`` in one terminal, and
    ``smtpd_senddata.py`` in another, we should see:

あるターミナルで ``smtpd_custom.py`` を、別のターミナルで ``smtpd_senddata.py`` を実行すると次のようになります。

::

    $ python smtpd_senddata.py 
    send: 'ehlo farnsworth.local\r\n'
    reply: '502 Error: command "EHLO" not implemented\r\n'
    reply: retcode (502); Msg: Error: command "EHLO" not implemented
    send: 'helo farnsworth.local\r\n'
    reply: '250 farnsworth.local\r\n'
    reply: retcode (250); Msg: farnsworth.local
    send: 'mail FROM:<author@example.com>\r\n'
    reply: '250 Ok\r\n'
    reply: retcode (250); Msg: Ok
    send: 'rcpt TO:<recipient@example.com>\r\n'
    reply: '250 Ok\r\n'
    reply: retcode (250); Msg: Ok
    send: 'data\r\n'
    reply: '354 End data with <CR><LF>.<CR><LF>\r\n'
    reply: retcode (354); Msg: End data with <CR><LF>.<CR><LF>
    data: (354, 'End data with <CR><LF>.<CR><LF>')
    send: 'Content-Type: text/plain; charset="us-ascii"\r\nMIME-Version: 1.0\r\nContent-Transfer-Encoding: 7bit\r\nTo: Recipient <recipient@example.com>\r\nFrom: Author <author@example.com>\r\nSubject: Simple test message\r\n\r\nThis is the body of the message.\r\n.\r\n'
    reply: '250 Ok\r\n'
    reply: retcode (250); Msg: Ok
    data: (250, 'Ok')
    send: 'quit\r\n'
    reply: '221 Bye\r\n'
    reply: retcode (221); Msg: Bye

..
    and

と

::

    $ python smtpd_custom.py 
    Receiving message from: ('127.0.0.1', 58541)
    Message addressed from: author@example.com
    Message addressed to  : ['recipient@example.com']
    Message length        : 229

..
    The port number for the incoming message will vary each time.  Notice
    that the *rcpttos* argument is a list of values and *mailfrom* is a
    single string.

入力メッセージのポート番号は毎回変わります。 *rcpttos* 引数は値のリストで *mailfrom* は文字列であることに注意してください。

.. note::

    .. To stop the server, press ``Ctrl-C``.

    サーバを停止するには ``Ctrl-C`` を入力してください。


DebuggingServer
===============

..
    The example above shows the arguments to :func:`process_message()`,
    but :mod:`smtpd` also includes a server specifically designed for more
    complete debugging, called :class:`DebuggingServer`.  It prints the
    entire incoming message to stdout and then stops processing (it does
    not proxy the message to a real mail server).

上述したサンプルは :func:`process_message()` に渡された引数を表示しますが :mod:`smtpd` は :class:`DebuggingServer` という、さらに完璧なデバッグのために特別に設計されたサーバも提供します。それは入力メッセージを標準出力へ全て表示してから処理を停止します(実際のメールサーバへプロキシのようにメッセージは送信しません)。

.. include:: smtpd_debug.py
    :literal:
    :start-after: #end_pymotw_header

..
    Using the ``smtpd_senddata.py`` client program from above, the output
    of the :class:`DebuggingServer` is:

先ほど使用した ``smtpd_senddata.py`` クライアントプログラムを使用すると :class:`DebuggingServer` の出力は次のようになります。

::

    $ python smtpd_debug.py
    ---------- MESSAGE FOLLOWS ----------
    Content-Type: text/plain; charset="us-ascii"
    MIME-Version: 1.0
    Content-Transfer-Encoding: 7bit
    To: Recipient <recipient@example.com>
    From: Author <author@example.com>
    Subject: Simple test message
    X-Peer: 127.0.0.1

    This is the body of the message.
    ------------ END MESSAGE ------------

PureProxy
=========

..
    The :class:`PureProxy` class implements a straightforward proxy
    server.  Incoming messages are forwarded upstream to the server given
    as argument to the constructor.

:class:`PureProxy` クラスは真っ直ぐで単純なプロキシサーバを実装します。入力メッセージはコンストラクタの引数として渡された上流のサーバへ転送されます。

.. warning::

    .. The stdlib docs say, "running this has a good chance to make you
       into an open relay, so please be careful."

    標準ライブラリドキュメントには "このプログラムの実行はオープンリレーについて理解する良い機会なので慎重に行ってください" とあります。

..
    Setting up the proxy server is just as easy as the debug server:

プロキシサーバの設定はまさにデバッグサーバと同じぐらい簡単です。

.. include:: smtpd_proxy.py
    :literal:
    :start-after: #end_pymotw_header

..
    It prints no output, though, so to verify that it is working we need
    to look at the mail server logs.

このサンプルは何も出力しないのでプロキシサーバが動作しているかを調べるためにメールサーバのログを見る必要があります。

::

    Oct 19 19:16:34 homer sendmail[6785]: m9JNGXJb006785: from=<author@example.com>, size=248, class=0, nrcpts=1, msgid=<200810192316.m9JNGXJb006785@homer.example.com>, proto=ESMTP, daemon=MTA, relay=[192.168.1.17]


MailmanProxy
============

..
    :mod:`smtpd` also includes a special proxy that acts as a front-end
    for Mailman_.  If the local Mailman configuration recognizes the
    address, it is handled directly.  Otherwise the message is delivered
    to the proxy.

さらに :mod:`smtpd` は Mailman_ のフロントエンドとして動作する特別なプロキシを提供します。それはローカルの Mailman 設定がそのアドレスを認識する場合、直接的に操作されます。一方、そのメッセージはプロキシへ配送されます。

.. seealso::

    `smtpd <http://docs.python.org/lib/module-smtpd.html>`_
        .. Standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント

    :mod:`smtplib`
        .. Provides a client interface.

        クライアントインタフェースを提供する

    :mod:`email`
        .. Parses email messages.

        メールメッセージを構文解析する

    :mod:`asyncore`
        .. Base module for writing asynchronous servers.

        非同期サーバを実装するベースモジュール

    :rfc:`2822`
        .. Defines the email message format.

        メールメッセージフォーマットを定義する

    `GNU Mailman mailing list software <http://www.gnu.org/software/mailman/index.html>`_
        .. An excellent example of Python software that works with email messages.

        メールを扱う Python ソフトウェアの優れたサンプル

.. _Mailman: http://www.gnu.org/software/mailman/index.html

