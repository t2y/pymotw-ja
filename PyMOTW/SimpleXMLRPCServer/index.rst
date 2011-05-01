..
    ===================================================
    SimpleXMLRPCServer -- Implements an XML-RPC server.
    ===================================================

==============================================
SimpleXMLRPCServer -- XML-RPC サーバを実装する
==============================================

..
    :synopsis: Implements an XML-RPC server.

.. module:: SimpleXMLRPCServer
    :synopsis: XML-RPC サーバを実装する

..
    :Purpose: Implements an XML-RPC server.
    :Available In: 2.2 and later

:目的: XML-RPC サーバを実装する
:利用できるバージョン: 2.2 以上

..
    The :mod:`SimpleXMLRPCServer` module contains classes for creating
    your own cross-platform, language-independent server using the XML-RPC
    protocol. Client libraries exist for many other languages, making
    XML-RPC an easy choice for building RPC-style services.

:mod:`SimpleXMLRPCServer` モジュールは XML-RPC プロトコルを使用してクロスプラットホーム、言語非依存なサーバを作成するためのクラスを提供します。多くのクライアントライブラリが多言語で存在するので RPC スタイルのサービスを構築するために XML-RPC を選択することは簡単な方法です。

..
    All of the examples provided here include a client module as well to
    interact with the demonstration server. If you want to download the code and
    run the examples, you will want to use 2 separate shell windows, one for the
    server and one for the client.

.. note::

    本稿で紹介する全てのサンプルはデモサーバとやり取りするクライアントモジュールを含めて提供します。もし、そのコードをダウンロードしてサンプルプログラムを実行したいなら、2つのシェルウィンドウを起動して、1つはサーバ、もう1つはクライアントにすると良いでしょう。

..
    A Simple Server
    ===============

シンプルサーバ
==============

..
    This simple server example exposes a single function that takes the
    name of a directory and returns the contents. The first step is to
    create the :class:`SimpleXMLRPCServer` instance and tell it where to
    listen for incoming requests ('localhost' port 9000 in this
    case). Then we define a function to be part of the service, and
    register the function so the server knows how to call it. The final
    step is to put the server into an infinite loop receiving and
    responding to requests.

このシンプルサーバのサンプルはディレクトリ名を受け取ってコンテンツを返す1つの関数を提供します。先ず :class:`SimpleXMLRPCServer` インスタンスを作成して、入力となるリクエスト(このケースでは 'localhost' の9000番ポート)を受信するサーバ/ポートを指定します。それから、そのサービスの一部となる関数を定義して、サーバへその関数の呼び出し方法を知らせるために登録を行います。最後にリクエストを受信するためにそのサーバを無限ループで実行してレスポンスを返します。

.. include:: SimpleXMLRPCServer_function.py
    :literal:
    :start-after: #end_pymotw_header

..
    The server can be accessed at the URL http://localhost:9000 using
    :mod:`xmlrpclib`.  This client code illustrates how to call the
    :func:`list_contents()` service from Python.

サーバは :mod:`xmlrpclib` を使用して http://localhost:9000 の URL にアクセスされます。このクライアントコードは Python から :func:`list_contents()` サービスを呼び出す方法を紹介します。

.. include:: SimpleXMLRPCServer_function_client.py
    :literal:
    :start-after: #end_pymotw_header

..
    Notice that we simply connect the :class:`ServerProxy` to the server
    using its base URL, and then call methods directly on the proxy. Each
    method invoked on the proxy is translated into a request to the
    server. The arguments are formatted using XML, and then POSTed to the
    server. The server unpacks the XML and figures out what function to
    call based on the method name invoked from the client. The arguments
    are passed to the function, and the return value is translated back to
    XML to be returned to the client.

そのベース URL を使用してサーバに対する :class:`ServerProxy` へ単純に接続して、プロキシで直接メソッドを呼び出していることに注意してください。プロキシで実行される各メソッドはサーバへのリクエストに変換されます。その引数は XML でフォーマットされてサーバへ POST されます。サーバはその XML をアンパックして、クライアントから実行されたメソッド名からどの関数を呼び出すかを見つけ出します。その引数は関数へ渡されて、その返り値は XML に変換されてクライアントへ返されます。

..
    Starting the server gives::

サーバを起動します。

::

    $ python SimpleXMLRPCServer_function.py 
    Use Control-C to exit

..
    Running the client in a second window shows the contents of my
    ``/tmp`` directory::

別のウィンドウでクライアントを実行すると ``/tmp`` ディレクトリの中身を表示します。

::

    $ python SimpleXMLRPCServer_function_client.py 
    ['.s.PGSQL.5432', '.s.PGSQL.5432.lock', '.X0-lock', '.X11-unix', 'ccc_exclude.1mkahl', 
    'ccc_exclude.BKG3gb', 'ccc_exclude.M5jrgo', 'ccc_exclude.SPecwL', 'com.hp.launchport', 'emacs527',
    'hsperfdata_dhellmann', 'launch-8hGHUp', 'launch-RQnlcc', 'launch-trsdly', 'launchd-242.T5UzTy', 
    'var_backups']

..
    and after the request is finished, log output appears in the server
    window

そのリクエストに対する処理が完了した後でサーバのウィンドウにログが出力されます。

::

    $ python SimpleXMLRPCServer_function.py 
    Use Control-C to exit
    DEBUG:root:list_contents(/tmp)
    localhost - - [29/Jun/2008 09:32:07] "POST /RPC2 HTTP/1.0" 200 -

..
    The first line of output is from the ``logging.debug()`` call inside
    :func:`list_contents()`. The second line is from the server logging
    the request because *logRequests* is ``True``.

ログ出力の最初の行は :func:`list_contents()` の内部で ``logging.debug()`` を呼び出して出力されます。2番目の行は *logRequests* が ``True`` なのでサーバのログが出力されます。

..
    Alternate Names
    ===============

関数の別名
==========

..
    Sometimes the function names you use inside your modules or libraries
    are not the names you want to use in your external API. You might need
    to load a platform-specific implementation, build the service API
    dynamically based on a configuration file, or replace real functions
    with stubs for testing. If you want to register a function with an
    alternate name, pass the name as the second argument to
    :func:`register_function()`, like this:

あなたのモジュール又はライブラリの内部で使用している関数名を外部 API で使用したくないときがあります。例えば、設定ファイルから動的にそのサービス API を構築して、プラットホームに特化した実装を読み込んだり、実際の関数をテスト用のスタブに置き換えたりする必要がある場合もあります。もし別の名前で関数を登録したいなら、次のように :func:`register_function()` の2番目の引数にその名前を渡してください。

.. include:: SimpleXMLRPCServer_alternate_name.py
    :literal:
    :start-after: #end_pymotw_header

..
    The client should now use the name ``dir()`` instead of
    ``list_contents()``:

今、クライアントは ``list_contents()`` の代わりに ``dir()`` という名前を使用します。

.. include:: SimpleXMLRPCServer_alternate_name_client.py
    :literal:
    :start-after: #end_pymotw_header

..
    Calling ``list_contents()`` results in an error, since the server no
    longer has a handler registered by that name.

サーバには ``list_contents()`` という名前でハンドラが登録されていないので ``list_contents()`` を呼び出すとエラーになります。

::

    $ python SimpleXMLRPCServer_alternate_name_client.py
    dir(): ['.s.PGSQL.5432', '.s.PGSQL.5432.lock', '.X0-lock', '.X11-unix', 'ccc_exclude.1mkahl', 'ccc_exclude.BKG3gb', 'ccc_exclude.M5jrgo', 'ccc_exclude.SPecwL', 'com.hp.launchport', 'emacs527', 'hsperfdata_dhellmann', 'launch-8hGHUp', 'launch-RQnlcc', 'launch-trsdly', 'launchd-242.T5UzTy', 'temp_textmate.V6YKzm', 'var_backups']
    list_contents():
    Traceback (most recent call last):
      File "/Users/dhellmann/Documents/PyMOTW/in_progress/SimpleXMLRPCServer/SimpleXMLRPCServer_alternate_name_client.py", line 15, in <module>
        print 'list_contents():', proxy.list_contents('/tmp')
      File "/Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5/xmlrpclib.py", line 1147, in __call__
        return self.__send(self.__name, args)
      File "/Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5/xmlrpclib.py", line 1437, in __request
        verbose=self.__verbose
      File "/Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5/xmlrpclib.py", line 1201, in request
        return self._parse_response(h.getfile(), sock)
      File "/Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5/xmlrpclib.py", line 1340, in _parse_response
        return u.close()
      File "/Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5/xmlrpclib.py", line 787, in close
        raise Fault(**self._stack[0])
    xmlrpclib.Fault: <Fault 1: '<type \'exceptions.Exception\'>:method "list_contents" is not supported'>

..
    Dotted Names
    ============

ドット名
========

..
    Individual functions can be registered with names that are not
    normally legal for Python identifiers. For example, you can include
    '.' in your names to separate the namespace in the service. This
    example extends our "directory" service to add "create" and "remove"
    calls. All of the functions are registered using the prefix "``dir.``"
    so that the same server can provide other services using a different
    prefix. One other difference in this example is that some of the
    functions return ``None``, so we have to tell the server to translate
    the ``None`` values to a nil value (see `XML-RPC Extensions`_).

個々の関数は Python の識別子のために通常は適切ではない名前で登録することができます。例えば、そのサービスの名前空間を分割するために名前に '.' を含めることができます。この例では "ディレクトリ" サービスに "create" と "remove" の関数呼び出しを追加して拡張します。同一サーバ上で違う接頭辞で他のサービスを提供できるように、全ての関数を "``dir.``" を接頭辞にして登録します。この例では他にも関数によって ``None`` を返しています。そのため ``None`` の値から nil の値へ変換するためにサーバへ教える必要があります( `XML-RPC Extensions`_ を参照)。

.. include:: SimpleXMLRPCServer_dotted_name.py
    :literal:
    :start-after: #end_pymotw_header

..
    To call the service functions in the client, simply refer to them with the
    dotted name, like so:

クライアントからそのサービスの関数を呼び出すために単純にドット名で参照してください。

.. include:: SimpleXMLRPCServer_dotted_name_client.py
    :literal:
    :start-after: #end_pymotw_header

..
    and (assuming you don't have a ``/tmp/EXAMPLE`` file on your system)
    the output for the sample client script looks like::

そして(システム上に ``/tmp/EXAMPLE`` ファイルがない場合)、クライアントのサンプルスクリプトの出力は次のようになります。

::

    $ python SimpleXMLRPCServer_dotted_name_client.py
    BEFORE       : False
    CREATE       : None
    SHOULD EXIST : True
    REMOVE       : None
    AFTER        : False

..
    Arbitrary Names
    ===============

任意の名前
==========

..
    A less useful, but potentially interesting feature is the ability to register
    functions with names that are otherwise invalid attribute names. This example
    service registers a function with the name "``multiply args``".

利便性は低いですが、無効な属性名を登録する機能が潜在的におもしろいです。この例のサービスは "``multiply args``" という名前で関数を登録します。

.. include:: SimpleXMLRPCServer_arbitrary_name.py
    :literal:
    :start-after: #end_pymotw_header

..
    Since the registered name contains a space, we can't use dot notation
    to access it directly from the proxy. We can, however, use
    ``getattr()``.

登録された名前がスペースを含むので、プロキシからドット表記で直接その名前にアクセスすることはできません。 しかし ``getattr()`` を使用することでアクセスできます。

.. include:: SimpleXMLRPCServer_arbitrary_name_client.py
    :literal:
    :start-after: #end_pymotw_header

..
    You should avoid creating services with names like this, though.  This
    example is provided not necessarily because it is a good idea, but
    because you may encounter existing services with arbitrary names and
    need to be able to call them.

アクセスはできますが、このような名前でサービスを作成しないようにしてください。この例はそれが良いアイディアだと言うわけではなく、あなたが任意の名前を持つ既存のサービスに遭遇して無効な名前で呼び出す必要があるときの方法を提供します。

::

    $ python SimpleXMLRPCServer_arbitrary_name_client.py
    25

..
    Exposing Methods of Objects
    ===========================

オブジェクトのメソッドを公開する
================================

..
    The earlier sections talked about techniques for establishing APIs
    using good naming conventions and namespacing. Another way to
    incorporate namespacing into your API is to use instances of classes
    and expose their methods. We can recreate the first example using an
    instance with a single method.

前半のセクションでは優れた命名規則や名前空間を使用して API を開発するためのテクニックについて説明しました。API に名前空間を組み込む他の方法として、クラスのインスタンスを使用してそのメソッドを公開する方法があります。最初のサンプルを1つのメソッドを持つインスタンスで再作成することができます。

.. include:: SimpleXMLRPCServer_instance.py
    :literal:
    :start-after: #end_pymotw_header

..
    A client can call the method directly:

クライアントは直接そのメソッドを呼び出すことができます。

.. include:: SimpleXMLRPCServer_instance_client.py
    :literal:
    :start-after: #end_pymotw_header

..
    and receive output like::

受け取った出力は次のようになります。

::

    $ python SimpleXMLRPCServer_instance_client.py
    ['.s.PGSQL.5432', '.s.PGSQL.5432.lock', '.X0-lock', '.X11-unix', 'ccc_exclude.1mkahl', 
    'ccc_exclude.BKG3gb', 'ccc_exclude.M5jrgo', 'ccc_exclude.SPecwL', 'com.hp.launchport', 
    'emacs527', 'hsperfdata_dhellmann', 'launch-8hGHUp', 'launch-RQnlcc', 'launch-trsdly', 
    'launchd-242.T5UzTy', 'temp_textmate.XNiIdy', 'var_backups']

..
    We've lost the "``dir.``" prefix for the service, though, so let's
    define a class to let us set up a service tree that can be invoked
    from clients.

この方法はそのサービスから "``dir.``" の接頭辞をなくしましたが、そのためにクライアントから実行されるサービスツリーをセットアップするためのクラスを定義します。

.. include:: SimpleXMLRPCServer_instance_dotted_names.py
    :literal:
    :start-after: #end_pymotw_header

..
    By registering the instance of :class:`ServiceRoot` with
    *allow_dotted_names* enabled, we give the server permission to walk
    the tree of objects when a request comes in to find the named method
    using ``getattr()``.

*allow_dotted_names* を有効にした :class:`ServiceRoot` インスタンスを登録することで ``getattr()`` でその名前のメソッドを見つけるためのリクエストを受け取ったとき、そのオブジェクトのツリーを辿る権限をサーバへ与えます。

.. include:: SimpleXMLRPCServer_instance_dotted_names_client.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python SimpleXMLRPCServer_instance_dotted_names_client.py
    ['.s.PGSQL.5432', '.s.PGSQL.5432.lock', '.X0-lock', '.X11-unix', 'ccc_exclude.1mkahl', 'ccc_exclude.BKG3gb', 'ccc_exclude.M5jrgo', 'ccc_exclude.SPecwL', 'com.hp.launchport', 'emacs527', 'hsperfdata_dhellmann', 'launch-8hGHUp', 'launch-RQnlcc', 'launch-trsdly', 'launchd-242.T5UzTy', 'temp_textmate.adghkQ', 'var_backups']

..
    Dispatching Calls Yourself
    ==========================

呼び出しをディスパッチする
==========================

..
    By default, :func:`register_instance()` finds all callable attributes
    of the instance with names not starting with '``_``' and registers
    them with their name. If you want to be more careful about the exposed
    methods, you could provide your own dispatching logic. For example:

デフォルトでは :func:`register_instance()` は '``_``' で始まらない名前を持つインスタンスの全ての呼び出し可能な属性を見つけます。そして見つけた名前をサービスに登録します。もしメソッドの公開を慎重に行いたいなら、独自のディスパッチロジックを提供することができます。例えば、

.. include:: SimpleXMLRPCServer_instance_with_prefix.py
    :literal:
    :start-after: #end_pymotw_header

..
    The :func:`public()` method of :class:`MyService` is marked as exposed
    to the XML-RPC service while :func:`private()` is not. The
    :func:`_dispatch()` method is invoked when the client tries to access
    a function that is part of :class:`MyService`. It first enforces the
    use of a prefix ("``prefix.``" in this case, but you can use any
    string).  Then it requires the function to have an attribute called
    *exposed* with a true value. The exposed flag is set on a function
    using a decorator for convenience.

:class:`MyService` の :func:`public()` メソッドは XML-RPC サービスへ公開する関数として expose としてマークします。一方 :func:`private()` にはありません。クライアントが :class:`MyService` にある関数へアクセスしようとするとき :func:`_dispatch()` メソッドが実行されます。 :func:`_dispatch()` メソッドは接頭辞の使用を強制します(このケースでは "``prefix.``" ですが、他の文字列も使用することができます)。それから *exposed* という属性が True である関数を要求します。exposed フラグはデコレータでセットすると便利です。

..
    Here are a few sample client calls:

クライアントからの呼び出しは次のようになります。

.. include:: SimpleXMLRPCServer_instance_with_prefix_client.py
    :literal:
    :start-after: #end_pymotw_header

..
    and the resulting output, with the expected error messages trapped and
    reported::

結果の出力は予想した通りトラップしたエラーメッセージが表示されます。

::

    $ python SimpleXMLRPCServer_instance_with_prefix_client.py
    public(): This is public
    private(): ERROR: <Fault 1: '<type \'exceptions.Exception\'>:method "prefix.private" is not supported'>
    public() without prefix: ERROR: <Fault 1: '<type \'exceptions.Exception\'>:method "public" is not supported'>

..
    There are several other ways to override the dispatching mechanism, including
    subclassing directly from SimpleXMLRPCServer. Check out the docstrings in the
    module for more details.

SimpleXMLRPCServer から直接サブクラス化することも含めて、ディスパッチの仕組みをオーバーライドするために複数の方法があります。より詳細については SimpleXMLRPCServer の docstring を確認してください。

..
    Introspection API
    =================

イントロスペクション API
========================

..
    As with many network services, it is possible to query an XML-RPC
    server to ask it what methods it supports and learn how to use
    them. :class:`SimpleXMLRPCServer` includes a set of public methods for
    performing this introspection. By default they are turned off, but can
    be enabled with :func:`register_introspection_functions()`. You can
    add explicit support for :func:`system.listMethods()` and
    :func:`system.methodHelp()` by defining :func:`_listMethods()` and
    :func:`_methodHelp()` on your service class. For example,

多くのネットワークサービスと同様に、どんなメソッドがサポートされているかとその使用方法を尋ねるために XML-RPC サーバへクエリすることができます。 :class:`SimpleXMLRPCServer` はこのイントロスペクションを実行する公開メソッドのセットを提供します。デフォルトではその機能は無効になっていますが、 :func:`register_introspection_functions()` で有効にすることができます。サービスを行うクラスで :func:`_listMethods()` と :func:`_methodHelp()` を定義することで :func:`system.listMethods()` と :func:`system.methodHelp()` を明示的にサポートするように追加することができます。例えば、

.. include:: SimpleXMLRPCServer_introspection.py
    :literal:
    :start-after: #end_pymotw_header

..
    In this case, the convenience function :func:`list_public_methods()`
    scans an instance to return the names of callable attributes that do
    not start with '``_``'. You can redefine :func:`_listMethods()` to
    apply whatever rules you like.  Similarly, for this basic example
    :func:`_methodHelp()` returns the docstring of the function, but could
    be written to build a help string from another source.

このケースでは、便利な関数 :func:`list_public_methods()` が呼び出し可能な '``_``' で始まらない属性名を返すためにインスタンスを調べます。あなた好みにどんなルールでも :func:`_listMethods()` を再定義することで適用することができます。同様にこの基本サンプルの :func:`_methodHelp()` はその関数の docstring を返しますが、他のソースからのヘルプを返すようにはなっていません。

.. include:: SimpleXMLRPCServer_introspection_client.py
    :literal:
    :start-after: #end_pymotw_header

..
    Notice that the system methods are included in the results.

その system メソッドが実行結果に含まれることに注意してください。

::

    $ python SimpleXMLRPCServer_introspection_client.py
    ============================================================
    list
    ------------------------------------------------------------
    list(dir_name) => [<filenames>]

    Returns a list containing the contents of the named directory.

    ============================================================
    system.listMethods
    ------------------------------------------------------------
    system.listMethods() => ['add', 'subtract', 'multiple']

    Returns a list of the methods supported by the server.

    ============================================================
    system.methodHelp
    ------------------------------------------------------------
    system.methodHelp('add') => "Adds two integers together"

    Returns a string containing documentation for the specified method.

    ============================================================
    system.methodSignature
    ------------------------------------------------------------
    system.methodSignature('add') => [double, int, int]

    Returns a list describing the signature of the method. In the
    above example, the add method takes two integers as arguments
    and returns a double result.

    This server does NOT support system.methodSignature.

..
    `SimpleXMLRPCServer <http://docs.python.org/lib/module-SimpleXMLRPCServer.html>`_
        Standard library documentation for this module.
    `XML-RPC How To <http://www.tldp.org/HOWTO/XML-RPC-HOWTO/index.html>`_
        Describes how to use XML-RPC to implement clients and servers in 
        a variety of languages.
    `XML-RPC Extensions`_
        Specifies an extension to the XML-RPC protocol.
    :mod:`xmlrpclib`
        XML-RPC client library

.. _XML-RPC Extensions: http://ontosys.com/xml-rpc/extensions.php

.. seealso::

    `SimpleXMLRPCServer <http://docs.python.org/lib/module-SimpleXMLRPCServer.html>`_
        本モジュールの標準ライブラリドキュメント

    `XML-RPC 入門 <http://www.tldp.org/HOWTO/XML-RPC-HOWTO/index.html>`_
        様々な言語でクライアントとサーバを実装するために XML-RPC の使用方法を説明します

    `XML-RPC Extensions`_
        XML-RPC プロトコルの機能拡張に特化した内容です

    :mod:`xmlrpclib`
        XML-RPC クライアントライブラリ

.. _XML-RPC Extensions: http://ontosys.com/xml-rpc/extensions.php
