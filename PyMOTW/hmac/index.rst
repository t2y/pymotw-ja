..
    =============================================================
    hmac -- Cryptographic signature and verification of messages.
    =============================================================

========================================
hmac -- 暗号化シグネチャとメッセージ検証
========================================

..
    :synopsis: Cryptographic signature and verification of messages.

.. module:: hmac
    :synopsis: 暗号化シグネチャとメッセージ検証

..
    :Purpose: 
        The hmac module implements keyed-hashing for message authentication, as
        described in :rfc:`2104`.
    :Available In: 2.2

:目的: :rfc:`2104` で提案されたメッセージ認証の鍵付きハッシュを提供する
:利用できるバージョン: 2.2

..
    The HMAC algorithm can be used to verify the integrity of information
    passed between applications or stored in a potentially vulnerable
    location. The basic idea is to generate a cryptographic hash of the
    actual data combined with a shared secret key. The resulting hash can
    then be used to check the transmitted or stored message to determine a
    level of trust, without transmitting the secret key.

HMAC アルゴリズムは、潜在的に脆弱性のあるところで格納されるデータ、もしくはアプリケーション間で受け渡しする情報の整合性検証に使用されます。基本的な考え方は、共有秘密鍵を組み合わせた実際のデータの暗号化ハッシュを生成することです。それにより生成されたハッシュは、秘密鍵を転送することなく、信頼性を決定する格納メッセージや通信そのものをチェックするために使用されます。

..
    Disclaimer: I'm not a security expert. For the full details on HMAC,
    check out :rfc:`2104`.

免責事項: 私はセキュリティの専門家ではありません。HMAC の詳細は :rfc:`2104` を調べてください。

..
    Example
    =======

サンプル
========

..
    Creating the hash is not complex. Here's a simple example which uses
    the default MD5 hash algorithm:

ハッシュを作成するのは難しくありません。デフォルトの MD5 ハッシュアルゴリズムを使用する簡単なサンプルは次になります。

.. include:: hmac_simple.py
    :literal:
    :start-after: #end_pymotw_header

..
    When run, the code reads its source file and computes an HMAC
    signature for it:

実行すると、このスクリプトはソースファイルを読み込み HMAC シグネチャを算出します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'hmac_simple.py'))
.. }}}

::

	$ python hmac_simple.py
	
	4bcb287e284f8c21e87e14ba2dc40b16

.. {{{end}}}

.. note::

   .. If I haven't changed the file by the time I release the example
      source for this week, the copy you download should produce the same
      hash.

   今週サンプルソースをリリースするときに変更がなければ、ダウンロードしたサンプルソースも同じハッシュ値を生成します。

..
    SHA vs. MD5
    ===========

SHA と MD5
==========

..
    Although the default cryptographic algorithm for :mod:`hmac` is MD5,
    that is not the most secure method to use. MD5 hashes have some
    weaknesses, such as collisions (where two different messages produce
    the same hash). The SHA-1 algorithm is considered to be stronger, and
    should be used instead.

:mod:`hmac` のデフォルトの暗号化アルゴリズムは MD5 ですが、MD5 は最もセキュアなメソッドではありません。MD5 ハッシュは、衝突(2つの異なるメッセージが同じハッシュを生成する)といった脆弱性があります。SHA-1 アルゴリズムはより強力と考えられており、こちらを使用すべきです。

.. include:: hmac_sha.py
    :literal:
    :start-after: #end_pymotw_header

..
    ``hmac.new()`` takes 3 arguments. The first is the secret key, which
    should be shared between the two endpoints which are communicating so
    both ends can use the same value. The second value is an initial
    message. If the message content that needs to be authenticated is
    small, such as a timestamp or HTTP POST, the entire body of the
    message can be passed to ``new()`` instead of using the update()
    method. The last argument is the digest module to be used. The default
    is ``hashlib.md5``. The previous example substitutes ``hashlib.sha1``.

:func:`hmac.new` は3つの引数を取ります。1番目の引数は、同じ値で通信する両方の終端で共有される秘密鍵です。2番目の引数は、初期化メッセージです。認証が必要なメッセージの本文が、タイムスタンプや HTTP POST といった小さなデータの場合、全てのメッセージ本文は :func:`update` ではなく :func:`new` へ渡されます。3番目の引数は、使用するダイジェストモジュールです。デフォルトは :func:`hashlib.md5` です。このサンプルは :func:`hashlib.sha1` に置き換えています。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'hmac_sha.py'))
.. }}}

::

	$ python hmac_sha.py
	
	69b26d1731a0a5f0fc7a92fc6c540823ec210759

.. {{{end}}}

..
    Binary Digests
    ==============

バイナリダイジェスト
====================

..
    The first few examples used the ``hexdigest()`` method to produce
    printable digests. The hexdigest is is a different representation of
    the value calculated by the ``digest()`` method, which is a binary
    value that may include unprintable or non-ASCII characters, including
    NULs. Some web services (Google checkout, Amazon S3) use the
    ``base64`` encoded version of the binary digest instead of the
    hexdigest.

前説のサンプルは、表示可能なダイジェストを生成するために :func:`hexdigest` メソッドを使用します。hexdigest は :func:`digest` メソッドが算出する異なる値の表現です。それは NUL も含めた表示不可能な文字、または ASCII ではない文字を含む可能性のあるバイナリ値です。(Google chekckout や Amazon S3 といった) web サービスによっては、hexdigest ではなく、バイナリダイジェストを ``base64`` でエンコードしたものを使用します。

.. include:: hmac_base64.py
    :literal:
    :start-after: #end_pymotw_header

..
    The base64 encoded string ends in a newline, which frequently needs to be
    stripped off when embedding the string in HTTP headers or other
    formatting-sensitive contexts.

base64 エンコード文字列は改行文字で終わりを表します。HTTP ヘッダ、またはその他のフォーマットに注意が必要なコンテンツに base64 エンコード文字列を組み込むときは改行を取り除く必要があります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'hmac_base64.py'))
.. }}}

::

	$ python hmac_base64.py
	
	olW2DoXHGJEKGU0aE9fOwSVE/o4=
	

.. {{{end}}}

..
    Applications
    ============

アプリケーション
================

..
    HMAC authentication should be used for any public network service, and
    any time data is stored where security is important. For example, when
    sending data through a pipe or socket, that data should be signed and
    then the signature should be tested before the data is used. The
    extended example below is available in the ``hmac_pickle.py`` file as
    part of the PyMOTW source package.

HMAC 認証は、任意の公開ネットワークサービスでセキュリティが要求されるデータに使用すべきです。例えば、パイプやソケットを通してデータを送信するとき、そのデータを署名してから送信して、そのデータを使用する前にそのシグネチャを検証すべきです。次の拡張したサンプルは、PyMOTW ソースパッケージにある ``hmac_pickle.py`` ファイルで利用できます。

..
    First, let's establish a function to calculate a digest for a string,
    and a simple class to be instantiated and passed through a
    communication channel.

まず文字列のダイジェストを算出する関数を定義して、シンプルなクラスをインスタンス化して通信チャンネルを通して渡します。

::

    import hashlib
    import hmac
    try:
        import cPickle as pickle
    except:
        import pickle
    import pprint
    from StringIO import StringIO


    def make_digest(message):
        "Return a digest for the message."
        return hmac.new('secret-shared-key-goes-here', message, hashlib.sha1).hexdigest()


    class SimpleObject(object):
        "A very simple class to demonstrate checking digests before unpickling."
        def __init__(self, name):
            self.name = name
        def __str__(self):
            return self.name

..
    Next, create a :mod:`StringIO` buffer to represent the socket or
    pipe. We will using a naive, but easy to parse, format for the data
    stream. The digest and length of the data are written, followed by a
    new line. The serialized representation of the object, generated by
    :mod:`pickle`, follows. In a real system, we would not want to depend
    on a length value, since if the digest is wrong the length is probably
    wrong as well. Some sort of terminator sequence not likely to appear
    in the real data would be more appropriate.

次にソケットかパイプを模倣する :mod:`StringIO` バッファを作成します。普通に使用しますが、データストリームのフォーマットや解析は簡単です。ダイジェストとデータ長を書き込んだ後で改行します。 :mod:`pickle` で生成されたオブジェクトのシリアライズ表現は次の通りです。実際のシステムでは、ダイジェストが不正な場合はおそらくデータも不正になるので、データ長の値は不要かもしれません。より適切な現実のデータには、何らかの終了シーケンスが現れない可能性が高いです。

..
    For this example, we will write two objects to the stream. The first is
    written using the correct digest value. 

このサンプルでは、ストリームに2つのオブジェクトを書き込みます。1番目のオブジェクトは正しいダイジェスト値を使用して書き込みます。

::

    # StringIO で書き込みソケットかパイプを模倣する
    out_s = StringIO()

    # ストリームへ正常なオブジェクトを書き込む
    #  digest\nlength\npickle
    o = SimpleObject('digest matches')
    pickled_data = pickle.dumps(o)
    digest = make_digest(pickled_data)
    header = '%s %s' % (digest, len(pickled_data))
    print '\nWRITING:', header
    out_s.write(header + '\n')
    out_s.write(pickled_data)

..
    The second object is written to the stream with an invalid digest, produced by
    calculating the digest for some other data instead of the pickle.

2番目のオブジェクトは、pickle 化されたデータではなく、別のデータのダイジェストを算出して生成した不正なダイジェストでストリームへ書き込みます。

::

    # ストリームへ不正なオブジェクトを書き込む
    o = SimpleObject('digest does not match')
    pickled_data = pickle.dumps(o)
    digest = make_digest('not the pickled data at all')
    header = '%s %s' % (digest, len(pickled_data))
    print '\nWRITING:', header
    out_s.write(header + '\n')
    out_s.write(pickled_data)

    out_s.flush()

..
    Now that the data is in the :mod:`StringIO` buffer, we can read it
    back out again.  The first step is to read the line of data with the
    digest and data length.  Then the remaining data is read (using the
    length value). We could use ``pickle.load()`` to read directly from
    the stream, but that assumes a trusted data stream and we do not yet
    trust the data enough to unpickle it. Reading the pickle as a string
    collect the data from the stream, without actually unpickling the
    object.

いま、書き込んだデータは :mod:`StringIO` バッファにあり、そのデータを読み返します。まずはダイジェストとデータ長の行を読み込みます。それから、残りのデータを(データ長の値を利用して)読み込みます。ストリームから直接読み込むのに :func:`pickle.load` を使用できますが、その処理は信頼できるデータストリームを前提としているので、信頼できないデータに対してはまだ unpickle しません。文字列としての pickle を読み込むには、オブジェクトを実際に unpickle せずにストリームからデータを読み込みます。

::

    # StringIO で読み込みソケットかパイプを模倣する
    in_s = StringIO(out_s.getvalue())

    # データを読み込む
    while True:
        first_line = in_s.readline()
        if not first_line:
            break
        incoming_digest, incoming_length = first_line.split(' ')
        incoming_length = int(incoming_length)
        print '\nREAD:', incoming_digest, incoming_length
        incoming_pickled_data = in_s.read(incoming_length)

..
    Once we have the pickled data, we can recalculate the digest value and
    compare it against what we read. If the digests match, we know it is
    safe to trust the data and unpickle it.

pickle 化されたデータを見つけたら、読み込んだデータに対してダイジェスト値を再計算して比較します。算出したダイジェストが一致したら、読み込んだデータが信頼して良いデータだと分かるので、そのデータを unpickle します。

::

        actual_digest = make_digest(incoming_pickled_data)
        print 'ACTUAL:', actual_digest

        if incoming_digest != actual_digest:
            print 'WARNING: Data corruption'
        else:
            obj = pickle.loads(incoming_pickled_data)
            print 'OK:', obj

..
    The output shows that the first object is verified and the second is deemed
    "corrupted", as expected:

その実行結果は、1番目のオブジェクトは検証され、2番目のオブジェクトは期待した通り "Data corruption(データ破損)" と見なされます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'hmac_pickle.py'))
.. }}}

::

	$ python hmac_pickle.py
	
	
	WRITING: 387632cfa3d18cd19bdfe72b61ac395dfcdc87c9 124
	
	WRITING: b01b209e28d7e053408ebe23b90fe5c33bc6a0ec 131
	
	READ: 387632cfa3d18cd19bdfe72b61ac395dfcdc87c9 124
	ACTUAL: 387632cfa3d18cd19bdfe72b61ac395dfcdc87c9
	OK: digest matches
	
	READ: b01b209e28d7e053408ebe23b90fe5c33bc6a0ec 131
	ACTUAL: dec53ca1ad3f4b657dd81d514f17f735628b6828
	WARNING: Data corruption

.. {{{end}}}


.. seealso::

    `hmac <http://docs.python.org/library/hmac.html>`_
        .. The standard library documentation for this module.
    
        本モジュールの標準ライブラリドキュメント

    :rfc:`2104`
        .. HMAC: Keyed-Hashing for Message Authentication

        HMAC: メッセージ認証のキーハッシュ

    :mod:`hashlib`
        .. The :mod:`hashlib` module.

        :mod:`hashlib` モジュール

    :mod:`pickle`
        .. Serialization library.

        シリアライズライブラリ

    `WikiPedia: MD5 <http://en.wikipedia.org/wiki/MD5>`_
        .. Description of the MD5 hashing algorithm.

        MD5 ハッシュアルゴリズムの説明

    `Amazon S3 Web サービスの認証 <http://docs.amazonwebservices.com/AmazonS3/2006-03-01/index.html?S3_Authentication.html>`_
        .. Instructions for authenticating to S3 using HMAC-SHA1 signed credentials.

        HMAC-SHA1 署名で S3 の認証を行う方法
