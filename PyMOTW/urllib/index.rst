..
    ======================================================
    urllib -- simple interface for network resource access
    ======================================================

==========================================================
urllib -- ネットワークリソースへのシンプルなインタフェース
==========================================================

..
    :synopsis: Accessing remote resources that don't need authentication, cookies, etc.

.. module:: urllib
    :synopsis: 認証や cookie が必要ないリモートのリソースへアクセスする

..
    :Purpose: Accessing remote resources that don't need authentication, cookies, etc.
    :Available In: 1.4 and later

:目的: 認証や cookie が必要ないリモートのリソースへアクセスする
:利用できるバージョン: 1.4 以上

..
    The :mod:`urllib` module provides a simple interface for network
    resource access. Although :mod:`urllib` can be used with gopher and
    ftp, these examples all use http.

:mod:`urllib` モジュールは、ネットワークリソースへのシンプルなインタフェースを提供します。 :mod:`urllib` は gopher や ftp プロトコルでも使用できますが、この記事では http のサンプルのみを紹介します。

HTTP GET
========

.. note::

    .. The test server for these examples is in BaseHTTPServer_GET.py, from the
       PyMOTW examples for :mod:`BaseHTTPServer`. Start the server in one
       terminal window, then run these examples in another.

    この記事のサンプルのテストサーバは :mod:`BaseHTTPServer` モジュールのサンプルにある BaseHTTPServer_GET.py です。ターミナルでサーバを起動して、それとは別のターミナルでこの記事のサンプルを実行してください。

..
    An HTTP GET operation is the simplest use of urllib. Simply pass the
    URL to :func:`urlopen()` to get a "file-like" handle to the remote
    data.

HTTP GET の操作は :mod:`urllib` の最も簡単な使用法です。リモートデータに対する "ファイルのような" ハンドラを取得するために :func:`urlopen()` へ単純に URL を渡してください。

.. include:: urllib_urlopen.py
    :literal:
    :start-after: #end_pymotw_header

..
    The example server takes the incoming values and formats a plain text
    response to send back. The return value from :func:`urlopen()` gives
    access to the headers from the HTTP server through the :func:`info()`
    method, and the data for the remote resource via methods like
    :func:`read()` and :func:`readlines()`.

このサンプルサーバは、入力データを受け取って、プレーンテキストでレスポンスを返します。 :func:`urlopen()` からの返り値に対して、 :func:`info()` を通して HTTP サーバからのヘッダへ、 :func:`read()` や :func:`readlines()` といったメソッドを通してリモートリソースのデータへのアクセスします。

::

    $ python urllib_urlopen.py
    RESPONSE: <addinfourl at 10180248 whose fp = <socket._fileobject object at 0x935c30>>
    URL     : http://localhost:8080/
    DATE    : Sun, 30 Mar 2008 16:27:10 GMT
    HEADERS :
    ---------
    Server: BaseHTTP/0.3 Python/2.5.1
    Date: Sun, 30 Mar 2008 16:27:10 GMT

    LENGTH  : 221
    DATA    :
    ---------
    CLIENT VALUES:
    client_address=('127.0.0.1', 54354) (localhost)
    command=GET
    path=/
    real path=/
    query=
    request_version=HTTP/1.0

    SERVER VALUES:
    server_version=BaseHTTP/0.3
    sys_version=Python/2.5.1
    protocol_version=HTTP/1.0

..
    The file-like object is also iterable:

また、返り値のファイルのようなオブジェクトは繰り返し処理できます。

.. include:: urllib_urlopen_iterator.py
    :literal:
    :start-after: #end_pymotw_header

..
    Since the lines are returned with newlines and carriage returns intact, this
    example strips them before printing the output.

このサンプルの行は改行コード付きでそのまま返されるので、出力を表示する前にその改行コードを取り除いています。

::

    $ python urllib_urlopen_iterator.py
    CLIENT VALUES:
    client_address=('127.0.0.1', 54380) (localhost)
    command=GET
    path=/
    real path=/
    query=
    request_version=HTTP/1.0

    SERVER VALUES:
    server_version=BaseHTTP/0.3
    sys_version=Python/2.5.1
    protocol_version=HTTP/1.0

.. _urllib-urlencode:

..
    Encoding Arguments
    ==================

エンコード引数
==============

..
    Arguments can be passed to the server by encoding them and appending them to
    the URL.

引数をエンコードして URL に追加することでサーバへ引数が渡せます。

.. include:: urllib_urlencode.py
    :literal:
    :start-after: #end_pymotw_header

..
    Notice that the query, in the list of client values, contains the encoded
    query arguments.

CLIENT VALUES のリストに、エンコードされたクエリ引数を含まれていることに注目してください。

::

    $ python urllib_urlencode.py
    Encoded: q=query+string&foo=bar
    CLIENT VALUES:
    client_address=('127.0.0.1', 54415) (localhost)
    command=GET
    path=/?q=query+string&foo=bar
    real path=/
    query=q=query+string&foo=bar
    request_version=HTTP/1.0

    SERVER VALUES:
    server_version=BaseHTTP/0.3
    sys_version=Python/2.5.1
    protocol_version=HTTP/1.0

..
    To pass a sequence of values using separate occurrences of the
    variable in the query string, set *doseq* to True when calling
    :func:`urlencode()`.

クエリ文字列の変数を別々に指定してシーケンスを渡すには、 :func:`urlencode()` を呼び出すときに *doseq* 引数に True をセットしてください。

.. include:: urllib_urlencode_doseq.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python urllib_urlencode_doseq.py
    Single  : foo=%5B%27foo1%27%2C+%27foo2%27%5D
    Sequence: foo=foo1&foo=foo2

..
    To decode the query string, see the :class:`FieldStorage` class from
    the :mod:`cgi` module.

クエリ文字列をデコードするには、 :mod:`cgi` モジュールの :class:`FieldStorage` クラスを参照してください。

..
    Special characters within the query arguments that might cause parse
    problems with the URL on the server side are "quoted" when passed to
    :func:`urlencode()`. To quote them locally to make safe versions of
    the strings, you can use the :func:`quote()` or :func:`quote_plus()`
    functions directly.

サーバ上の URL 解析で問題を起こす可能性があるクエリ引数内の特殊文字は、 :func:`urlencode()` へ渡されるときに "クォート" されます。そういった特殊文字をローカルで安全にクォートするには :func:`quote()` や :func:`quote_plus()` 関数を直接、使用できます。

.. include:: urllib_quote.py
    :literal:
    :start-after: #end_pymotw_header

..
    Notice that :func:`quote_plus()` is more aggressive about the
    characters it replaces.

:func:`quote_plus()` は :func:`quote` より積極的に文字を置き換えることに注意してください。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'urllib_quote.py'))
.. }}}

::

	$ python urllib_quote.py
	
	urlencode() : url=http%3A%2F%2Flocalhost%3A8080%2F%7Edhellmann%2F
	quote()     : http%3A//localhost%3A8080/%7Edhellmann/
	quote_plus(): http%3A%2F%2Flocalhost%3A8080%2F%7Edhellmann%2F

.. {{{end}}}

..
    To reverse the quote operations, use :func:`unquote()` or
    :func:`unquote_plus()`, as appropriate.

アンクォートするには :func:`unquote()` や :func:`unquote_plus()` を適切に使用してください。

.. include:: urllib_unquote.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'urllib_unquote.py'))
.. }}}

::

	$ python urllib_unquote.py
	
	http://localhost:8080/~dhellmann/
	http://localhost:8080/~dhellmann/

.. {{{end}}}


HTTP POST
=========

.. note::

    .. The test server for these examples is in BaseHTTPServer_POST.py, from the
       PyMOTW examples for the :mod:`BaseHTTPServer`. Start the server in one
       terminal window, then run these examples in another.

    この記事のサンプルのテストサーバは :mod:`BaseHTTPServer` モジュールのサンプルにある BaseHTTPServer_POST.py です。ターミナルでサーバを起動して、それとは別のターミナルでこの記事のサンプルを実行してください。

..
    To POST data to the remote server, instead of using GET, pass the
    encoded query arguments as data to :func:`urlopen()` instead of
    appending them to the URL.

GET ではなく、リモートサーバへデータを POST するには、URL に対してエンコードされたクエリ引数を追加するのではなく、 :func:`urlopen()` へのデータとして渡してください。

.. include:: urllib_urlopen_post.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python urllib_urlopen_post.py
    Client: ('127.0.0.1', 54545)
    Path: /
    Form data:
        q=query string
        foo=bar

..
    You can send any byte-string as data, in case the server expects
    something other than url-encoded form arguments in the posted data.

データとして任意のバイト文字列を送信できます。このサーバのサンプルは POST されたデータにある URL エンコードされたフォーム引数以外のデータを待ちます。

..
    Paths vs. URLs
    ==============

パスと URL
==========

..
    Some operating systems use different values for separating the
    components of paths in local files than URLs. To make your code
    portable, you should use the functions :func:`pathname2url()` and
    :func:`url2pathname()` to convert back and forth. Since I am working
    on a Mac, I have to explicitly import the Windows versions of the
    functions. Using the versions of the functions exported by
    :mod:`urllib` gives you the correct defaults for your platform, so you
    do not need to do this.

オペレーティングシステムによっては、URL よりローカルファイルのパスのコンポーネント区切りに違う文字を使用します。コードの移植性を高めるために、変換したり戻したりするのに :func:`pathname2url()` や :func:`url2pathname()` といった関数を使用した方が良いです。私は Mac を使っているので、その関数の Windows 版を明示的にインポートする必要があります。 :mod:`urllib` がエクスポートする関数を使用すると、プラットフォームに適切なデフォルトが渡されるので、こんなことをする必要はありません。

.. include:: urllib_pathnames.py
    :literal:
    :start-after: #end_pymotw_header

..
    There are two Windows examples, with and without the drive letter at the
    prefix of the path.

パスの接頭辞にドライブ文字が付く、付かない場合の Windows サンプルが2つあります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'urllib_pathnames.py'))
.. }}}

::

	$ python urllib_pathnames.py
	
	== Default ==
	Original: /a/b/c
	URL     : /a/b/c
	Path    : /d/e/f
	
	== Windows, without drive letter ==
	Original: \a\b\c
	URL     : /a/b/c
	Path    : \d\e\f
	
	== Windows, with drive letter ==
	Original: C:\\a\b\c
	URL     : ///C:/a/b/c
	Path    : \d\e\f

.. {{{end}}}

..
    Simple Retrieval with Cache
    ===========================

キャッシュでシンプルに取り出す
==============================

..
    Retrieving data is a common operation, and :mod:`urllib` includes the
    :func:`urlretrieve()` function so you don't have to write your
    own. :func:`urlretrieve()` takes arguments for the URL, a temporary
    file to hold the data, a function to report on download progress, and
    data to pass if the URL refers to a form where data should be
    POSTed. If no filename is given, :func:`urlretrieve()` creates a
    temporary file. You can delete the file yourself, or treat the file as
    a cache and use :func:`urlcleanup()` to remove it.

データを取り出すのは一般的な操作です。 :mod:`urllib` には :func:`urlretrieve()` 関数があるので、独自にその処理を書く必要はありません。 :func:`urlretrieve()` は、URL、データを保持する一時ファイル、ダウンロード進捗をレポートする関数、引数の URL が POST されるフォームを参照するときに渡すデータといった引数を取ります。もしファイル名が渡されなければ、 :func:`urlretrieve()` は一時ファイルを作成します。その一時ファイルはキャッシュのように扱ったり、 :func:`urlcleanup()` を使用して削除できます。

..
    This example uses GET to retrieve some data from a web server:

このサンプルは web サーバからデータを取り出すために GET を使用します。

.. include:: urllib_urlretrieve.py
    :literal:
    :start-after: #end_pymotw_header

..
    Since the server does not return a ``Content-length`` header,
    :func:`urlretrieve()` does not know how big the data should be, and
    passes -1 as the *total_size* argument to :func:`reporthook()`.

このサーバは ``Content-length`` ヘッダを返さないので、 :func:`urlretrieve()` は返されるデータがどのぐらい大きいかが分かりません。そして :func:`reporthook()` の *total_size* 引数として -1 が渡されます。

::


    $ python urllib_urlretrieve.py
    Connection opened
    Read 1 blocks
    Read 2 blocks
    Read 3 blocks
    Read 4 blocks
    Read 5 blocks
    Read 6 blocks
    Read 7 blocks
    Read 8 blocks
    Read 9 blocks
    Read 10 blocks
    Read 11 blocks
    Read 12 blocks
    Read 13 blocks
    Read 14 blocks
    Read 15 blocks
    Read 16 blocks
    Read 17 blocks
    Read 18 blocks
    Read 19 blocks

    File: /var/folders/9R/9R1t+tR02Raxzk+F71Q50U+++Uw/-Tmp-/tmp3HRpZP
    Headers:
    Content-Type: text/html; charset=UTF-8
    Last-Modified: Tue, 25 Mar 2008 23:09:10 GMT
    Cache-Control: max-age=0 private
    ETag: "904b02e0-c7ff-47f6-9f35-cc6de5d2a2e5"
    Server: GFE/1.3
    Date: Sun, 30 Mar 2008 17:36:48 GMT
    Connection: Close

    File exists before cleanup: True
    File still exists: False


URLopener
=========

..
    :mod:`urllib` provides a :class:`URLopener` base class, and
    :class:`FancyURLopener` with default handling for the supported
    protocols. If you find yourself needing to change their behavior, you
    are probably better off looking at the :mod:`urllib2` module, added in
    Python 2.1.

:mod:`urllib` は :class:`URLopener` ベースクラスと、サポート済みプロトコルのデフォルト操作を行う :class:`FancyURLopener` を提供します。もしこういったクラスの処理を変更する必要が出てきたら、Python 2.1 で追加された :mod:`urllib2` モジュールに探してみる方が良いでしょう。

.. seealso::

    `urllib <http://docs.python.org/lib/module-urllib.html>`_
        .. Standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント

    :mod:`urllib2`
        .. Updated API for working with URL-based services.

        URL ベースのサービスを処理する API の拡張
    
    :mod:`urlparse`
        .. Parse URL values to access their components.

        URL コンポーネントにアクセスする URL 文字列を解析
