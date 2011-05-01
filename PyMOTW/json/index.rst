..
    =============================================
    json -- JavaScript Object Notation Serializer
    =============================================

===============================================
json -- JavaScript Object Notation シリアライザ
===============================================

..
    :synopsis: JavaScript Object Notation Serializer

.. module:: json
    :synopsis: JavaScript Object Notation シリアライザ

..
    :Purpose: Encode Python objects as JSON strings, and decode JSON strings into Python objects.
    :Available In: 2.6

:目的: Python オブジェクトを JSON 文字列へエンコード、JSON 文字列を Python オブジェクトへデコードする
:利用できるバージョン: 2.6

..
    The :mod:`json` module provides an API similar to :mod:`pickle` for
    converting in-memory Python objects to a serialized representation
    known as `JavaScript Object Notation`_ (JSON).  Unlike pickle, JSON
    has the benefit of having implementations in many languages
    (especially JavaScript), making it suitable for inter-application
    communication.  JSON is probably most widely used for communicating
    between the web server and client in an AJAX application, but is not
    limited to that problem domain.

:mod:`json` モジュールはインメモリの Python オブジェクトを `JavaScript Object Notation`_ (JSON) というシリアライズされたフォーマットへ変換する :mod:`pickle` に似た API を提供します。pickle と違うのは、JSON はアプリケーション間通信に適応するように多くの言語(特に JavaScript)で実装されている利点があります。JSON は AJAX アプリケーションにおける web サーバとクライアント間の通信でおそらく最もよく利用されていますが、その課題領域のみに制限されているわけではありません。

..
    Encoding and Decoding Simple Data Types
    =======================================

シンプルなデータ型をエンコード、デコードする
============================================

..
    The encoder understands Python's native types by default (string,
    unicode, int, float, list, tuple, dict).

エンコーダはデフォルトで Python のネイティブのデータ型(string, unicode, int, float, list, tuple, dict)を理解します。

.. include:: json_simple_types.py
    :literal:
    :start-after: #end_pymotw_header

..
    Values are encoded in a manner very similar to Python's ``repr()``
    output.

値は Python の ``repr()`` の出力とよく似た値にエンコードされます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'json_simple_types.py'))
.. }}}
.. {{{end}}}

..
    Encoding, then re-decoding may not give exactly the same type of
    object.

エンコードした後に再度デコードすると、厳密には同じ型のオブジェクトを取得できないこともあります。

.. include:: json_simple_types_decode.py
    :literal:
    :start-after: #end_pymotw_header

..
    In particular, strings are converted to unicode and tuples become
    lists.

特に、文字列はユニコードへ、タプルは JSON リストへ変換されます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'json_simple_types_decode.py'))
.. }}}
.. {{{end}}}

..
    Human-consumable vs. Compact Output
    ===================================

人間が読み易い 対 コンパクトアウトプット
========================================

..
    Another benefit of JSON over pickle is that the results are
    human-readable.  The ``dumps()`` function accepts several arguments to
    make the output even nicer.  For example, ``sort_keys`` tells the
    encoder to output the keys of a dictionary in sorted, instead of
    random, order.

pickle より優れている JSON の他の利点はその出力結果を人間が読み易いことです。 ``dumps()`` 関数はその出力を読み易くするために複数の引数を受け取ります。例えば、 ``sort_keys`` はランダムな順序ではなく、ディクショナリのキーをソートして出力するようにエンコーダへ伝えます。

.. include:: json_sort_keys.py
    :literal:
    :start-after: #end_pymotw_header

..
    Sorting makes it easier to scan the results by eye, and also makes it
    possible to compare JSON output in tests.

ソートすることで、その出力結果を目視で確認するのに便利です。さらにテストのときに JSON の出力を比較するのも簡単です。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'json_sort_keys.py'))
.. }}}
.. {{{end}}}

..
    For highly-nested data structures, you will want to specify a value
    for ``indent``, so the output is formatted nicely as well.

深くネストされたデータ構造の出力を分かり易くするために ``indent`` に値を指定したくなるでしょう。

.. include:: json_indent.py
    :literal:
    :start-after: #end_pymotw_header

..
    When indent is a non-negative integer, the output more closely
    resembles that of :mod:`pprint`, with leading spaces for each level of
    the data structure matching the indent level.

インデントが正の数の場合、データ構造の各レベルに対応するインデントレベルにスペースを入れて :mod:`pprint` によく似た出力になります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'json_indent.py'))
.. }}}
.. {{{end}}}

..
    Verbose output like this increases the number of bytes needed to
    transmit the same amount of data, however, so it isn't the sort of
    thing you necessarily want to use in a production environment.  In
    fact, you may want to adjust the settings for separating data in the
    encoded output to make it even more compact than the default.

同じデータ量を送信する必要ある冗長な出力には、サンプルのようにバイト数が増加しますが、本番環境で意図したようにソートされるとは限りません。実際、デフォルト設定よりもっとコンパクトになるようにエンコードしたとしても、エンコードされた出力のデータを分割するために設定を調整したくなるかもしれません。

.. include:: json_compact_encoding.py
    :literal:
    :start-after: #end_pymotw_header

..
    The ``separators`` argument to ``dumps()`` should be a tuple
    containing the strings to separate items in a list and keys from
    values in a dictionary.  The default is ``(', ', ': ')``. By removing
    the whitespace, we can produce a more compact output.

``dumps()`` への ``separators`` 引数はディクショナリの値からリストやキーのアイテムを分離するためにその文字列を含むタプルにします。デフォルトは ``(', ', ': ')`` です。スペースを削除することでもっとコンパクトな出力になります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'json_compact_encoding.py'))
.. }}}
.. {{{end}}}

..
    Encoding Dictionaries
    =====================

ディクショナリをエンコードする
==============================

..
    The JSON format expects the keys to a dictionary to be strings.  If
    you have other types as keys in your dictionary, trying to encode the
    object will produce a :ref:`ValueError <exceptions-ValueError>`.  One way
    to work around that limitation is to skip over non-string keys using
    the ``skipkeys`` argument:

JSON フォーマットはディクショナリのキーが文字列であることを前提とします。ディクショナリのキーに他のデータ型を使用している場合、そのオブジェクトをエンコードしようとすると :ref:`ValueError <exceptions-ValueError>` が発生します。その制限を回避する1つのワークアラウンドは ``skipkeys`` 引数を使用して非文字列のキーを読み飛ばすことです。

.. include:: json_skipkeys.py
    :literal:
    :start-after: #end_pymotw_header

..
    Rather than raising an exception, the non-string key is simply
    ignored.

例外を発生させずに非文字列のキーは単純に無視されます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'json_skipkeys.py'))
.. }}}
.. {{{end}}}

..
    Working with Your Own Types
    ===========================

独自のデータ型で使用する
========================

..
    All of the examples so far have used Pythons built-in types because
    those are supported by :mod:`json` natively.  It isn't uncommon, of
    course, to have your own types that you want to be able to encode as
    well.  There are two ways to do that.

これまでの全てのサンプルは Python の組み込みデータ型がネイティブに :mod:`json` でサポートされているので、そういった組み込みデータ型を使用していました。Python のデータ型と同様にエンコードできるようにしたい独自のデータ型を定義することは珍しいことではありません。そのために2つの方法があります。

..
    First, we'll need a class to encode:

先ずエンコードするためのクラスが必要になります。

.. include:: json_myobj.py
    :literal:
    :start-after: #end_pymotw_header

..
    The simple way of encoding a ``MyObj`` instance is to define a
    function to convert an unknown type to a known type.  You don't have
    to do the encoding yourself, just convert one object to another.

``MyObj`` インスタンスをエンコードする簡単な方法は不明なデータ型をよく知られたデータ型へ変換する関数を定義することです。自分自身でエンコードする必要はありません。ただ1つのオブジェクトを他のオブジェクトへ変換するのみです。

.. include:: json_dump_default.py
    :literal:
    :start-after: #end_pymotw_header

..
    In ``convert_to_builtin_type()``, instances of classes not recognized
    by :mod:`json` are converted to dictionaries with enough information
    to re-create the object if a program has access to the Python modules
    necessary.

``convert_to_builtin_type()`` の関数内で、あるプログラムが Python モジュールへアクセスする必要がある場合、 :mod:`json` が認識しないクラスのインスタンスはそのオブジェクトを再作成するために十分な情報を持つディクショナリへ変換されます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'json_dump_default.py'))
.. }}}
.. {{{end}}}

..
    To decode the results and create a ``MyObj`` instance, we need to tie
    in to the decoder so we can import the class from the module and
    create the instance.  For that, we use the ``object_hook`` argument to
    ``loads()``.

その出力結果をデコードして ``MyObj`` インスタンスを作成するには、そのモジュールからクラスをインポートして、そのクラスのインスタンスを作成できるようにデコーダへ関連付ける必要があります。そのため ``loads()`` への ``object_hook`` 引数を使用します。

..
    The ``object_hook`` is called for each dictionary decoded from the
    incoming data stream, giving us a chance to convert the dictionary to
    another type of object.  The hook function should return the object it
    wants the calling application to receive instead of the dictionary.

``object_hook`` は入ってくるデータストリームからデコードされるディクショナリ毎に呼び出されます。つまり、そのディクショナリから他のオブジェクトのデータ型へ変換する機会を提供してくれます。そのフック関数はそのディクショナリの代わりに受け取るための呼び出しアプリケーションを要求するオブジェクトを返すべきです。

.. include:: json_load_object_hook.py
    :literal:
    :start-after: #end_pymotw_header

..
    Since :mod:`json` converts string values to unicode objects, we need
    to re-encode them as ASCII strings before using them as keyword
    arguments to the class constructor.

:mod:`json` は文字列の値から unicode オブジェクトへ変換されます。そのため、そのクラスのコンストラクタへのキーワード引数として使用される前に、unicode オブジェクトを ASCII 文字列として再エンコードする必要があります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'json_load_object_hook.py'))
.. }}}
.. {{{end}}}

..
    Similar hooks are available for the built-in types integers
    (``parse_int``), floating point numbers (``parse_float``), and
    constants (``parse_constant``).

よく似たフック関数が組み込み型の整数(``parse_int``), 浮動小数点数(``parse_float``) と定数 (``parse_constant``) のために使用できます。

..
    Encoder and Decoder Classes
    ===========================

クラスのエンコーダとデコーダ
============================

..
    Besides the convenience functions we have already examined, the
    :mod:`json` module provides classes for encoding and decoding.  When
    using the classes directly, you have access to extra APIs and can
    create subclasses to customize their behavior.

既に説明した便利な関数に加えて、 :mod:`json` モジュールはエンコーディングとデコーディングのクラスを提供します。そのクラスを直接使用する場合、拡張 API へアクセスして、それらのクラスの振る舞いをカスタマイズするサブクラスを作成できます。

..
    The JSONEncoder provides an iterable interface for producing "chunks"
    of encoded data, making it easier for you to write to files or network
    sockets without having to represent an entire data structure in
    memory.

JSONEncoder はエンコードデータの "チャンク" を生成するために繰り返し利用できるインタフェースを提供します。そして、メモリ内にある完全なデータ構造を再構成せずに簡単にネットワークソケット又はファイルへの書き込みます。

.. include:: json_encoder_iterable.py
    :literal:
    :start-after: #end_pymotw_header

..
    As you can see, the output is generated in logical units, rather than
    being based on any size value.

ご覧の通り、その出力はサイズの値をベースにしたモノというよりはむしろ論理的なユニット単位で生成されます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'json_encoder_iterable.py'))
.. }}}
.. {{{end}}}

..
    The ``encode()`` method is basically equivalent to
    ``''.join(encoder.iterencode())``, with some extra error checking up
    front.

``encode()`` メソッドは ``''.join(encoder.iterencode())`` と基本的には等価です。そして、フロント側でその他のエラーを調べます。

..
    To encode arbitrary objects, we can override the ``default()`` method
    with an implementation similar to what we used above in
    ``convert_to_builtin_type()``.

任意のオブジェクトをエンコードするために、上述した ``convert_to_builtin_type()`` の方法と同様の実装で ``default()`` メソッドをオーバーライドできます。

.. include:: json_encoder_default.py
    :literal:
    :start-after: #end_pymotw_header

..
    The output is the same as the previous implementation.

その出力は以前の実装した内容と同じです。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'json_encoder_default.py'))
.. }}}
.. {{{end}}}

..
    Decoding text, then converting the dictionary into an object takes a
    little more work to set up than our previous implementation, but not
    much.

テキストをデコードした後、そのディクショナリをオブジェクトへ変換するには、以前の実装より少しだけ作業が必要ですが、大したことはありません。

.. include:: json_decoder_object_hook.py
    :literal:
    :start-after: #end_pymotw_header

..
    And the output is the same as the earlier example.

その出力は以前の例と同じです。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'json_decoder_object_hook.py'))
.. }}}
.. {{{end}}}

..
    Working with Streams and Files
    ==============================

ストリームとファイルで使用する
==============================

..
    In all of the examples so far, we have assumed that we could (and
    should) hold the encoded version of the entire data structure in
    memory at one time.  With large data structures it may be preferable
    to write the encoding directly to a file-like object.  The convenience
    functions ``load()`` and ``dump()`` accept references to a file-like
    object to use for reading or writing.

これまでの全ての例では、メモリ内に完全なデータ構造が構成されているときにエンコードデータを対象として扱える(扱うべき)ということを前提としていました。巨大なデータ構造、例えばファイルのようなオブジェクトへ直接的にそのエンコードデータを書き込む方が望ましいでしょう。そのための便利な関数 ``load()`` と ``dump()`` は、読み書き用途にファイルのようなオブジェクトへのリファレンスを受け取ることができます。

.. include:: json_dump_file.py
    :literal:
    :start-after: #end_pymotw_header

..
    A socket would work in much the same way as the normal file handle
    used here.

ソケットもほぼ同様の方法で普通のファイルハンドラとして動作するでしょう。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'json_dump_file.py'))
.. }}}
.. {{{end}}}

..
    Although it isn't optimized to read only part of the data at a time,
    the ``load()`` function still offers the benefit of encapsulating the
    logic of generating objects from stream input.

一度にデータの一部のみを読み込むように最適化されてはいませんが、 ``load()`` 関数は入力ストリームからオブジェクトを生成するカプセル化のロジックの利点も提供します。

.. include:: json_load_file.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'json_load_file.py'))
.. }}}
.. {{{end}}}


..
    Mixed Data Streams
    ==================

混在するデータストリーム
========================

..
    The JSONDecoder includes the ``raw_decode()`` method for decoding a
    data structure followed by more data, such as JSON data with trailing
    text.  The return value is the object created by decoding the input
    data, and an index into that data indicating where decoding left off.

JSONDecoder には終了文字のある JSON データのような、複数のデータで構成されたデータ構造をデコードするために ``raw_decode()`` メソッドがあります。その返り値は入力データをデコードすることで作成されるオブジェクトと、そのデータのデコードが終了した位置を指すインデックスです。

.. include:: json_mixed_data.py
    :literal:
    :start-after: #end_pymotw_header

..
    Unfortunately, this only works if the object appears at the beginning
    of the input.

不幸にも ``raw_decode()`` は終了文字のあるデータ構造のオブジェクトが入力データの最初に現れた場合しか動作しません。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'json_mixed_data.py'))
.. }}}
.. {{{end}}}

..
    `json <http://docs.python.org/library/json.html>`_
        The standard library documentation for this module.
    `JavaScript Object Notation`_
        JSON home, with documentation and implementations in other languages.
    http://code.google.com/p/simplejson/
        simplejson, from Bob Ippolito, et al, is the externally
        maintained development version of the json library included
        with Python 2.6 and Python 3.0. It maintains backwards
        compatibility with Python 2.4 and Python 2.5.
    `jsonpickle <http://code.google.com/p/jsonpickle/>`_
        jsonpickle allows for any Python object to be serialized into JSON. 
    :ref:`article-data-persistence`
        Other examples of storing data from Python programs.

.. seealso::

    `json <http://docs.python.org/library/json.html>`_
        .. The standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント

    `JavaScript Object Notation`_
        .. JSON home, with documentation and implementations in other languages.

        JSON のホームページでドキュメントや他言語の実装がある

    http://code.google.com/p/simplejson/
        .. simplejson, from Bob Ippolito, et al, is the externally
           maintained development version of the json library included
           with Python 2.6 and Python 3.0. It maintains backwards
           compatibility with Python 2.4 and Python 2.5.

        Bob Ippolito と他の人による simplejson は Python2.6 と Python 3.0 で提供された json ライブラリの開発バージョンとしてメンテナンスされている、Python 2.4 と 2.5 にも後方互換性があるようにメンテナンスされている

    `jsonpickle <http://code.google.com/p/jsonpickle/>`_
        .. jsonpickle allows for any Python object to be serialized into JSON. 

        jsonpickle は任意の Python オブジェクトを JSON にシリアライズする

    :ref:`article-data-persistence`
        .. Other examples of storing data from Python programs.

        Python プログラムからデータを格納するその他のサンプル

.. _JavaScript Object Notation: http://json.org/
