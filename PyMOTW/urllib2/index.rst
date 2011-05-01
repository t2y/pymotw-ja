..
    ====================================
    urllib2 -- Library for opening URLs.
    ====================================

=======================================
urllib2 -- URL をオープンするライブラリ
=======================================

..
    :synopsis: Library for opening URLs.

.. module:: urllib2
    :synopsis: URL をオープンするライブラリ

..
    :Purpose: A library for opening URLs that can be extended by defining custom protocol handlers.
    :Available In: 2.1

:目的: カスタムプロトコルハンドラを定義して拡張できる URL をオープンするライブラリ
:利用できるバージョン: 2.1

..
    The :mod:`urllib2` module provides an updated API for using internet
    resources identified by URLs.  It is designed to be extended by
    individual applications to support new protocols or add variations to
    existing protocols (such as handling HTTP basic authentication).

:mod:`urllib2` モジュールは、URL で識別するインターネットリソースのために拡張された API です。個別のアプリケーションで新たなプロトコルをサポートしたり、(HTTP ベーシック認証を処理するといった)既存のプロトコルに修正を加えたりして拡張することを意図して設計されています。

HTTP GET
========

.. note::

    .. The test server for these examples is in BaseHTTPServer_GET.py, from the
       PyMOTW examples for :mod:`BaseHTTPServer`. Start the server in one
       terminal window, then run these examples in another.

    この記事のサンプルのテストサーバは :mod:`BaseHTTPServer` モジュールのサンプルにある BaseHTTPServer_GET.py です。ターミナルでサーバを起動して、それとは別のターミナルでこの記事のサンプルを実行してください。

..
    As with :mod:`urllib`, an HTTP GET operation is the simplest use of
    :mod:`urllib2`. Pass the URL to :func:`urlopen()` to get a "file-like"
    handle to the remote data.

:mod:`urllib` と同様に HTTP GET の操作は :mod:`urllib2` の最も簡単な使用法です。リモートのデータを処理する "ファイルのような" オブジェクトを取得するために :func:`urlopen()` へ URL を渡してください。

.. include:: urllib2_urlopen.py
    :literal:
    :start-after: #end_pymotw_header

..
    The example server accepts the incoming values and formats a plain
    text response to send back. The return value from :func:`urlopen()`
    gives access to the headers from the HTTP server through the
    :func:`info()` method, and the data for the remote resource via
    methods like :func:`read()` and :func:`readlines()`.

このサンプルサーバは、入力データを受け取って、プレーンテキストでレスポンスを返します。 :func:`urlopen()` からの返り値に対して、 :func:`info()` を通して HTTP サーバからのヘッダへ、 :func:`read()` や :func:`readlines()` といったメソッドを通してリモートリソースのデータへのアクセスします。

::

    $ python urllib2_urlopen.py
    RESPONSE: <addinfourl at 11940488 whose fp = <socket._fileobject object at 0xb573f0>>
    URL     : http://localhost:8080/
    DATE    : Sun, 19 Jul 2009 14:01:31 GMT
    HEADERS :
    ---------
    Server: BaseHTTP/0.3 Python/2.6.2
    Date: Sun, 19 Jul 2009 14:01:31 GMT
    
    LENGTH  : 349
    DATA    :
    ---------
    CLIENT VALUES:
    client_address=('127.0.0.1', 55836) (localhost)
    command=GET
    path=/
    real path=/
    query=
    request_version=HTTP/1.1
    
    SERVER VALUES:
    server_version=BaseHTTP/0.3
    sys_version=Python/2.6.2
    protocol_version=HTTP/1.0
    
    HEADERS RECEIVED:
    accept-encoding=identity
    connection=close
    host=localhost:8080
    user-agent=Python-urllib/2.6
    
..
    The file-like object returned by :func:`urlopen()` is iterable:

:func:`urlopen()` が返すファイルのようなオブジェクトは繰り返し処理できます。

.. include:: urllib2_urlopen_iterator.py
    :literal:
    :start-after: #end_pymotw_header

..
    This example strips the trailing newlines and carriage returns before
    printing the output.

このサンプルは、出力を表示する前にその文字列の改行コードを取り除いています。

::

    $ python urllib2_urlopen_iterator.py
    CLIENT VALUES:
    client_address=('127.0.0.1', 55840) (localhost)
    command=GET
    path=/
    real path=/
    query=
    request_version=HTTP/1.1
    
    SERVER VALUES:
    server_version=BaseHTTP/0.3
    sys_version=Python/2.6.2
    protocol_version=HTTP/1.0
    
    HEADERS RECEIVED:
    accept-encoding=identity
    connection=close
    host=localhost:8080
    user-agent=Python-urllib/2.6

..
    Encoding Arguments
    ------------------

エンコード引数
--------------

..
    Arguments can be passed to the server by encoding them with
    :ref:`urllib.urlencode() <urllib-urlencode>` and appending them to the
    URL.

:ref:`urllib.urlencode() <urllib-urlencode>` で引数をエンコードして URL に追加することでサーバへ引数が渡せます。

.. include:: urllib2_http_get_args.py
    :literal:
    :start-after: #end_pymotw_header

..
    The list of client values returned in the example output contains the
    encoded query arguments.

CLIENT VALUES のリストにエンコードされたクエリ引数が含まれています。

::

    $ python urllib2_http_get_args.py
    Encoded: q=query+string&foo=bar
    CLIENT VALUES:
    client_address=('127.0.0.1', 55849) (localhost)
    command=GET
    path=/?q=query+string&foo=bar
    real path=/
    query=q=query+string&foo=bar
    request_version=HTTP/1.1
    
    SERVER VALUES:
    server_version=BaseHTTP/0.3
    sys_version=Python/2.6.2
    protocol_version=HTTP/1.0
    
    HEADERS RECEIVED:
    accept-encoding=identity
    connection=close
    host=localhost:8080
    user-agent=Python-urllib/2.6


HTTP POST
=========

.. note::

    .. The test server for these examples is in BaseHTTPServer_POST.py, from the
       PyMOTW examples for the :mod:`BaseHTTPServer`. Start the server in one
       terminal window, then run these examples in another.

    この記事のサンプルのテストサーバは :mod:`BaseHTTPServer` モジュールのサンプルにある BaseHTTPServer_POST.py です。ターミナルでサーバを起動して、それとは別のターミナルでこの記事のサンプルを実行してください。

..
    To POST form-encoded data to the remote server, instead of using GET,
    pass the encoded query arguments as data to :func:`urlopen()`.

GET ではなく、リモートサーバへフォームでエンコードされたデータを POST するには、エンコードされたクエリ引数を :func:`urlopen()` へのデータとして渡してください。

.. include:: urllib2_urlopen_post.py
    :literal:
    :start-after: #end_pymotw_header

..
    The server can decode the form data and access the individual values
    by name.

このサーバはフォームデータをデコードして名前で個々のデータにアクセスできます。

::

    $ python urllib2_urlopen_post.py
    Client: ('127.0.0.1', 55943)
    User-agent: Python-urllib/2.6
    Path: /
    Form data:
    	q=query string
    	foo=bar

..
    Working with Requests Directly
    ==============================

リクエストを直接処理する
========================

..
    :func:`urlopen()` is a convenience function that hides some of the
    details of how the request is made and handled for you. For more
    precise control, you may want to instantiate and use a
    :class:`Request` object directly.

:func:`urlopen()` は、リクエストがどうやって作られて処理されているかの詳細を隠蔽してくれる便利な関数です。より詳細な制御をするには :class:`Request` オブジェクトを直接インスタンス化して使用すると良いです。

..
    Adding Outgoing Headers
    -----------------------

外部向けのヘッダを追加する
--------------------------

..
    As the examples above illustrate, the default *User-agent* header
    value is made up of the constant ``Python-urllib``, followed by the
    Python interpreter version. If you are creating an application that
    will access other people's web resources, it is courteous to include
    real user agent information in your requests, so they can identify the
    source of the hits more easily. Using a custom agent also allows them
    to control crawlers using a ``robots.txt`` file (see
    :mod:`robotparser`).

前説で説明したサンプルのように、デフォルトの *User-agent* ヘッダの値は、定数 ``Python-urllib`` に続く Python インタープリタのバージョンで構成されます。他人が管理している web リソースへアクセスするアプリケーションを開発しているなら、簡単にアクセス元が分かるのでリクエスト情報の中に本当のユーザエージェント情報を含めるのがお作法です。カスタムエージェントを使用すると ``robots.txt`` ファイルでクローラを制御することもできます(:mod:`robotparser` を参照)。

.. include:: urllib2_request_header.py
    :literal:
    :start-after: #end_pymotw_header

..
    After creating a :class:`Request` object, use :func:`add_header()` to
    set the user agent value before opening the request.  The last line of
    the output shows our custom value.

:class:`Request` オブジェクトの作成後、そのリクエストをオープンする前にユーザエージェントの値をセットするには :func:`add_header()` を使用してください。この結果出力の最後の行はカスタム値を表示します。

::

    $ python urllib2_request_header.py
    CLIENT VALUES:
    client_address=('127.0.0.1', 55876) (localhost)
    command=GET
    path=/
    real path=/
    query=
    request_version=HTTP/1.1
    
    SERVER VALUES:
    server_version=BaseHTTP/0.3
    sys_version=Python/2.6.2
    protocol_version=HTTP/1.0
    
    HEADERS RECEIVED:
    accept-encoding=identity
    connection=close
    host=localhost:8080
    user-agent=PyMOTW (http://www.doughellmann.com/PyMOTW/)

..
    Posting Form Data
    -----------------

フォームデータを POST する
--------------------------

..
    You can set the outgoing data on the :class:`Request` to post it to
    the server.

サーバへデータを POST する :class:`Request` にそのデータをセットできます。

.. include:: urllib2_request_post.py
    :literal:
    :start-after: #end_pymotw_header

..
    The HTTP method used by the :class:`Request` changes from GET to POST
    automatically after the data is added.

:class:`Request` が使用する HTTP メソッドは、自動的にデータが追加された後で GET から POST へ変更します。

::

    $ python urllib2_request_post.py
    Request method before data: GET
    Request method after data : POST
    
    OUTGOING DATA:
    q=query+string&foo=bar
    
    SERVER RESPONSE:
    Client: ('127.0.0.1', 56044)
    User-agent: PyMOTW (http://www.doughellmann.com/PyMOTW/)
    Path: /
    Form data:
    	q=query string
    	foo=bar
    
.. note::

    .. Although the method is :func:`add_data()`, its effect is *not*
       cumulative.  Each call replaces the previous data.

    :func:`add_data()` というメソッド名ですが、この処理はデータを追加 *しません* 。呼び出す毎にその前のデータは置き換えられます。

..
    Uploading Files
    ---------------

ファイルをアップロードする
--------------------------

..
    Encoding files for upload requires a little more work than simple forms.  A complete MIME
    message needs to be constructed in the body of the request, so that the server can
    distinguish incoming form fields from uploaded files.

アップロード用にファイルをエンコードすることは、シンプルなフォームよりも一手間あります。サーバがアップロードファイルからフォームフィールドを判別できるように、リクエスト本文に完全な MIME メッセージを作成する必要があります。

.. include:: urllib2_upload_files.py
    :literal:
    :start-after: #end_pymotw_header

..
    The :class:`MultiPartForm` class can represent an arbitrary form as a
    multi-part MIME message with attached files.

:class:`MultiPartForm` クラスは、添付ファイルのマルチパート MIME メッセージのように任意のフォームを表せます。

::

    $ python urllib2_upload_files.py
    
    OUTGOING DATA:
    --192.168.1.17.527.30074.1248020372.206.1
    Content-Disposition: form-data; name="firstname"
    
    Doug
    --192.168.1.17.527.30074.1248020372.206.1
    Content-Disposition: form-data; name="lastname"
    
    Hellmann
    --192.168.1.17.527.30074.1248020372.206.1
    Content-Disposition: file; name="biography"; filename="bio.txt"
    Content-Type: text/plain
    
    Python developer and blogger.
    --192.168.1.17.527.30074.1248020372.206.1--
    
    
    SERVER RESPONSE:
    Client: ('127.0.0.1', 57126)
    User-agent: PyMOTW (http://www.doughellmann.com/PyMOTW/)
    Path: /
    Form data:
    	lastname=Hellmann
    	Uploaded biography as "bio.txt" (29 bytes)
    	firstname=Doug
    

..
    Custom Protocol Handlers
    ========================

カスタムプロトコルハンドラ
==========================

..
    :mod:`urllib2` has built-in support for HTTP(S), FTP, and local file
    access. If you need to add support for other URL types, you can
    register your own protocol handler to be invoked as needed. For
    example, if you want to support URLs pointing to arbitrary files on
    remote NFS servers, without requiring your users to mount the path
    manually, would create a class derived from :class:`BaseHandler` and
    with a method :func:`nfs_open()`.

:mod:`urllib2` は HTTP(S)、FTP、ローカルファイルへのアクセスを組み込み機能でサポートします。その他の URL タイプをサポートする必要があるなら、必要に応じて実行される独自のプロトコルハンドラを登録できます。例えば、リモートの NFS サーバ上に対して、ユーザへ手動でパスをマウントさせずに任意のファイルを参照する URL をサポートしたいなら、 :class:`BaseHandler` から派生したクラスと :func:`nfs_open()` メソッドを作成できます。

..
    The protocol :func:`open()` method takes a single argument, the
    :class:`Request` instance, and it should return an object with a
    :func:`read()` method that can be used to read the data, an
    :func:`info()` method to return the response headers, and
    :func:`geturl()` to return the actual URL of the file being read. A
    simple way to achieve that is to create an instance of
    :class:`urllib.addurlinfo`, passing the headers, URL, and open file
    handle in to the constructor.

プロトコルの :func:`open()` メソッドは :class:`Request` インスタンスの引数を1つだけ受け取ります。 :class:`Request` インスタンスは、データを読み込むのに使用される :func:`read()` メソッド、レスポンスヘッダを返す :func:`info()` メソッド、読み込まれたファイルの実際の URL を返す :func:`geturl()` メソッドを持つオブジェクトを返します。これを実装する簡単な方法の1つは、ヘッダ、URL、オープンファイルハンドラをコンストラクタへ渡して :class:`urllib.addurlinfo` のインスタンスを作成することです。

.. include:: urllib2_nfs_handler.py
    :literal:
    :start-after: #end_pymotw_header

..
    The :class:`FauxNFSHandler` and :class:`NFSFile` classes print
    messages to illustrate where a real implementation would add mount and
    unmount calls. Since this is just a simulation,
    :class:`FauxNFSHandler` is primed with the name of a temporary
    directory where it should look for all of its files.

:class:`FauxNFSHandler` と :class:`NFSFile` クラスは、実際の実装がどこで mount と unmound を呼び出すかを理解するためにメッセージ出力します。このサンプルはただのシミュレーションなので、 :class:`FauxNFSHandler` に一時ディレクトリの場所を教えて、そこにあるファイルを探します。

::

    $ python urllib2_nfs_handler.py
    
    FauxNFSHandler simulating mount:
      Remote path: /path/to/the
      Server     : remote_server
      Local path : /var/folders/9R/9R1t+tR02Raxzk+F71Q50U+++Uw/-Tmp-/tmppv5Efn
      File name  : file.txt
    
    READ CONTENTS: Contents of file.txt
    URL          : nfs://remote_server/path/to/the/file.txt
    HEADERS:
      Content-length  = 20
      Content-type    = text/plain
    
    NFSFile:
      unmounting /var/folders/9R/9R1t+tR02Raxzk+F71Q50U+++Uw/-Tmp-/tmppv5Efn
      when file.txt is closed


.. seealso::

    `urllib2 <http://docs.python.org/library/urllib2.html>`_
        .. The standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント

    :mod:`urllib`
        .. Original URL handling library.

        URL 操作のオリジナルのライブラリ

    :mod:`urlparse`
        .. Work with the URL string itself.

        URL 文字列を処理する

    `urllib2 -- The Missing Manual <http://www.voidspace.org.uk/python/articles/urllib2.shtml>`_
        .. Michael Foord's write-up on using urllib2.

        Michael Foord の urllib2 の記事
    
    `Upload Scripts <http://www.voidspace.org.uk/python/cgi.shtml#upload>`_
        .. Example scripts from Michael Foord that illustrate how to upload a file
           using HTTP and then receive the data on the server.

        HTTP でファイルをアップロードしてサーバ上でデータを受け取る方法を説明する Michael Foord のサンプルスクリプト

    `HTTP client to POST using multipart/form-data <http://code.activestate.com/recipes/146306/>`_
        .. Python cookbook recipe showing how to encode and post data, including files,
           over HTTP.

        HTTP でエンコード、ファイルを含めたデータの POST を行う Python クックブックのレシピ

    `Form content types <http://www.w3.org/TR/REC-html40/interact/forms.html#h-17.13.4>`_
        .. W3C specification for posting files or large amounts of data via HTTP forms.

        HTTP フォームでファイルや巨大なデータを解析する W3C の仕様

    :mod:`mimetypes`
        .. Map filenames to mimetype.

        ファイル名と MIME タイプをマップする
    
    :mod:`mimetools`
        .. Tools for parsing MIME messages.

        MIME メッセージを解析するツール
