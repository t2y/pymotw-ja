=============================================
json -- JavaScript Object Notation Serializer
=============================================

.. module:: json
    :synopsis: JavaScript Object Notation Serializer

..
    :Purpose: Encode Python objects as JSON strings, and decode JSON strings into Python objects.
    :Python Version: 2.6

:目的: Python オブジェクトを JSON 文字列へエンコード、JSON 文字列を Python オブジェクトへデコードする
:Python バージョン: 2.6

..
    The :mod:`json` module provides an API similar to :mod:`pickle` for
    converting in-memory Python objects to a serialized representation
    known as `JavaScript Object Notation`_ (JSON).  Unlike pickle, JSON
    has the benefit of having implementations in many languages
    (especially JavaScript), making it suitable for inter-application
    communication.  JSON is probably most widely used for communicating
    between the web server and client in an AJAX application, but is not
    limited to that problem domain.

:mod:`json` モジュールはインメモリ Python オブジェクトを `JavaScript Object Notation`_ (JSON) というシリアライズされたフォーマットへ変換するための :mod:`pickle` に似た API を提供します。pickle と違うのは、JSON はアプリケーション間通信に適応するために多くの言語(特に JavaScript)で実装されている利点があります。JSON は AJAX アプリケーションにおける web サーバとクライアント間通信でおそらくは最もよく利用されていますが、その領域の問題が制限されていません。

..
    Encoding and Decoding Simple Data Types
    =======================================

シンプルなデータ型をエンコード、デコードする
============================================

..
    The encoder understands Python's native types by default (string,
    unicode, int, float, list, tuple, dict).

そのエンコーダはデフォルトで Python のネイティブのデータ型(string, unicode, int, float, list, tuple, dict)を解釈します。

.. include:: json_simple_types.py
    :literal:
    :start-after: #end_pymotw_header

..
    Values are encoded in a manner very similar to Python's ``repr()``
    output.

値は、言わば、Python の ``repr()`` 出力とよく似た値にエンコードされます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'json_simple_types.py'))
.. }}}

::

	$ python json_simple_types.py
	DATA: [{'a': 'A', 'c': 3.0, 'b': (2, 4)}]
	JSON: [{"a": "A", "c": 3.0, "b": [2, 4]}]

.. {{{end}}}

..
    Encoding, then re-decoding may not give exactly the same type of
    object.

エンコードした後に再度デコードすると厳密には同じ型のオブジェクトを取得できない可能性があります。

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

::

	$ python json_simple_types_decode.py
	ENCODED: [{"a": "A", "c": 3.0, "b": [2, 4]}]
	DECODED: [{u'a': u'A', u'c': 3.0, u'b': [2, 4]}]
	ORIGINAL: <type 'tuple'>
	DECODED : <type 'list'>

.. {{{end}}}

..
    Human-consumable vs. Compact Output
    ===================================

Human-consumable vs. コンパクトアウトプット
===========================================

..
    Another benefit of JSON over pickle is that the results are
    human-readable.  The ``dumps()`` function accepts several arguments to
    make the output even nicer.  For example, ``sort_keys`` tells the
    encoder to output the keys of a dictionary in sorted, instead of
    random, order.

pickle より優れた JSON の他の利点はその結果(出力)を人間が読み易いことです。 ``dumps()`` 関数はその出力を読み易くするために複数の引数を受け取ります。例えば、 ``sort_keys`` はランダムな順序ではなく、ディクショナリのキーをソートして出力するようにエンコーダへ伝えます。

.. include:: json_sort_keys.py
    :literal:
    :start-after: #end_pymotw_header

..
    Sorting makes it easier to scan the results by eye, and also makes it
    possible to compare JSON output in tests.

ソートされていると、目視でその結果(出力)を確認するのに便利です。またテスト時に JSON の出力を比較するのが簡単になります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'json_sort_keys.py'))
.. }}}

::

	$ python json_sort_keys.py
	DATA: [{'a': 'A', 'c': 3.0, 'b': (2, 4)}]
	JSON: [{"a": "A", "c": 3.0, "b": [2, 4]}]
	SORT: [{"a": "A", "b": [2, 4], "c": 3.0}]
	UNSORTED MATCH: False
	SORTED MATCH  : True

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

::

	$ python json_indent.py
	DATA: [{'a': 'A', 'c': 3.0, 'b': (2, 4)}]
	NORMAL: [{"a": "A", "b": [2, 4], "c": 3.0}]
	INDENT: [
	  {
	    "a": "A", 
	    "b": [
	      2, 
	      4
	    ], 
	    "c": 3.0
	  }
	]

.. {{{end}}}

..
    Verbose output like this increases the number of bytes needed to
    transmit the same amount of data, however, so it isn't the sort of
    thing you necessarily want to use in a production environment.  In
    fact, you may want to adjust the settings for separating data in the
    encoded output to make it even more compact than the default.

同じデータ量を送信する必要性がある冗長な出力は、例のようにバイト数が増加しますが、本番環境で意図したようにソートされるとは限りません。実際、デフォルト設定よりもっとコンパクトになるようにエンコードされたその出力内にあるデータを分離するための設定を調整したくなるでしょう。

.. include:: json_compact_encoding.py
    :literal:
    :start-after: #end_pymotw_header

..
    The ``separators`` argument to ``dumps()`` should be a tuple
    containing the strings to separate items in a list and keys from
    values in a dictionary.  The default is ``(', ', ': ')``. By removing
    the whitespace, we can produce a more compact output.

``dumps()`` への ``separators`` 引数はディクショナリの値からリストやキーのアイテムを分離するためにその文字列を含むタプルにすべきです。デフォルトは ``(', ', ': ')`` です。スペースを削除することでもっとコンパクトな出力になります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'json_compact_encoding.py'))
.. }}}

::

	$ python json_compact_encoding.py
	DATA: [{'a': 'A', 'c': 3.0, 'b': (2, 4)}]
	repr(data)             : 35
	dumps(data)            : 35
	dumps(data, indent=2)  : 76
	dumps(data, separators): 29

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

JSON フォーマットはディクショナリのキーが文字列であることを前提とします。ディクショナリのキーに他のデータ型を使用していて、そのオブジェクトをエンコードしようとすると :ref:`ValueError <exceptions-ValueError>` が発生します。その制限を回避する1つのワークアラウンドは ``skipkeys`` 引数を使用して非文字列のキーを読み飛ばすことです。

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

::

	$ python json_skipkeys.py
	First attempt
	ERROR: key ('d',) is not a string
	
	Second attempt
	[{"a": "A", "c": 3.0, "b": [2, 4]}]

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

これまでの全ての例は Python のビルトインのデータ型がネイティブに :mod:`json` でサポートされているのでビルトインのデータ型を使用していました。Python のデータ型と同様にエンコードできるようにしたい独自のデータ型を持つことは珍しいことではありません。そのために2つの方法があります。

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

::

	$ python json_dump_default.py
	First attempt
	ERROR: <MyObj(instance value goes here)> is not JSON serializable
	
	With default
	default( <MyObj(instance value goes here)> )
	{"s": "instance value goes here", "__module__": "json_myobj", "__class__": "MyObj"}

.. {{{end}}}

..
    To decode the results and create a ``MyObj`` instance, we need to tie
    in to the decoder so we can import the class from the module and
    create the instance.  For that, we use the ``object_hook`` argument to
    ``loads()``.

その結果(出力)をデコードして ``MyObj`` インスタンスを作成するためには、そのモジュールからクラスをインポートして、そのクラスのインスタンスを作成できるようにデコーダへ結び付ける必要があります。そのため ``loads()`` への ``object_hook`` 引数を使用します。

..
    The ``object_hook`` is called for each dictionary decoded from the
    incoming data stream, giving us a chance to convert the dictionary to
    another type of object.  The hook function should return the object it
    wants the calling application to receive instead of the dictionary.

``object_hook`` は入ってくるデータストリームからデコードされる各ディクショナリのために呼び出されます。つまり、そのディクショナリから他のオブジェクトのデータ型へ変換する機会を提供してくれます。そのフック関数はそのディクショナリの代わりに受け取るための呼び出しアプリケーションを要求するオブジェクトを返すべきです。

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

::

	$ python json_load_object_hook.py
	MODULE: <module 'json_myobj' from '/home/morimoto/work/translate/02_pymotw/pymotw-ja/PyMOTW/json/json_myobj.pyc'>
	CLASS: <class 'json_myobj.MyObj'>
	INSTANCE ARGS: {'s': u'instance value goes here'}
	[<MyObj(instance value goes here)>]

.. {{{end}}}

..
    Similar hooks are available for the built-in types integers
    (``parse_int``), floating point numbers (``parse_float``), and
    constants (``parse_constant``).

よく似たフック関数がビルトイン型の整数(``parse_int``), 浮動小数点数(``parse_float``) と定数 (``parse_constant``) のために使用できます。

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

既に説明した便利な関数に加えて、 :mod:`json` モジュールはエンコーディングとデコーディングのためのクラスを提供します。そのクラスを直接使用する場合、拡張 API へアクセスして、それらのクラスの振る舞いをカスタマイズするサブクラスを作成することができます。

..
    The JSONEncoder provides an iterable interface for producing "chunks"
    of encoded data, making it easier for you to write to files or network
    sockets without having to represent an entire data structure in
    memory.

JSONEncoder はエンコードデータの "チャンク" を生成するために繰り返し利用可能なインタフェースを提供します。そして、メモリ内にある完全なデータ構造を再構成せずにネットワークソケット又はファイルへの書き込むを簡単にします。

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

::

	$ python json_encoder_iterable.py
	PART: [
	PART: {
	PART: "a"
	PART: : 
	PART: "A"
	PART: , 
	PART: "c"
	PART: : 
	PART: 3.0
	PART: , 
	PART: "b"
	PART: : 
	PART: [
	PART: 2
	PART: , 
	PART: 4
	PART: ]
	PART: }
	PART: ]

.. {{{end}}}

..
    The ``encode()`` method is basically equivalent to
    ``''.join(encoder.iterencode())``, with some extra error checking up
    front.

``encode()`` メソッドは ``''.join(encoder.iterencode())`` と基本的には等価です。そして、フロント側で追加のエラーを調べます。

..
    To encode arbitrary objects, we can override the ``default()`` method
    with an implementation similar to what we used above in
    ``convert_to_builtin_type()``.

任意のオブジェクトをエンコードするために、上述した ``convert_to_builtin_type()`` で使用した内容と同様の実装で ``default()`` メソッドをオーバーライドすることができます。

.. include:: json_encoder_default.py
    :literal:
    :start-after: #end_pymotw_header

..
    The output is the same as the previous implementation.

その出力は以前の実装した内容と同じです。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'json_encoder_default.py'))
.. }}}

::

	$ python json_encoder_default.py
	<MyObj(internal data)>
	default( <MyObj(internal data)> )
	{"s": "internal data", "__module__": "json_myobj", "__class__": "MyObj"}

.. {{{end}}}

..
    Decoding text, then converting the dictionary into an object takes a
    little more work to set up than our previous implementation, but not
    much.

テキストをデコードした後、そのディクショナリをオブジェクトへ変換するためには、以前の実装より少しだけ作業が必要になりますが、大したことはありません。

.. include:: json_decoder_object_hook.py
    :literal:
    :start-after: #end_pymotw_header

..
    And the output is the same as the earlier example.

その出力は以前の例と同じです。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'json_decoder_object_hook.py'))
.. }}}

::

	$ python json_decoder_object_hook.py
	MODULE: <module 'json_myobj' from '/home/morimoto/work/translate/02_pymotw/pymotw-ja/PyMOTW/json/json_myobj.pyc'>
	CLASS: <class 'json_myobj.MyObj'>
	INSTANCE ARGS: {'s': u'instance value goes here'}
	[<MyObj(instance value goes here)>]

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

これまでの全ての例では、メモリ内に完全なデータ構造が構成されているときにエンコードデータを対象として扱える(扱うべき)ということを前提としていました。巨大なデータ構造では、例えばファイルのようなオブジェクトへ直接的にそのエンコードデータを書き込む方が望ましいでしょう。そのための便利な関数 ``load()`` と ``dump()`` は、読み書き用途にファイルのようなオブジェクトへのリファレンスを受け取ることができます。

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

::

	$ python json_dump_file.py
	[{"a": "A", "c": 3.0, "b": [2, 4]}]

.. {{{end}}}

..
    Although it isn't optimized to read only part of the data at a time,
    the ``load()`` function still offers the benefit of encapsulating the
    logic of generating objects from stream input.

1度にデータの一部のみを読み込むようには最適化されてはいませんが、その ``load()`` 関数は入力ストリームからオブジェクトを生成するカプセル化ロジックの利点も提供します。

.. include:: json_load_file.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'json_load_file.py'))
.. }}}

::

	$ python json_load_file.py
	[{u'a': u'A', u'c': 3.0, u'b': [2, 4]}]

.. {{{end}}}


..
    Mixed Data Streams
    ==================

ミックスされたデータストリーム
==============================

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

::

	$ python json_mixed_data.py
	JSON first:
	Object              : [{u'a': u'A', u'c': 3.0, u'b': [2, 4]}]
	End of parsed input : 35
	Remaining text      : ' This text is not JSON.'
	
	JSON embedded:
	ERROR: No JSON object could be decoded

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
        本モジュールの標準ライブラリドキュメント

    `JavaScript Object Notation`_
        JSON のホームページでドキュメントや他言語の実装があります。

    http://code.google.com/p/simplejson/
        Bob Ippolito やその他の人による simplejson は Python2.6 と Python 3.0 に含まれる json ライブラリの開発バージョンが外部でメンテナンスされています。Python 2.4 と 2.5 にも後方互換性があります。

    `jsonpickle <http://code.google.com/p/jsonpickle/>`_
        jsonpickle は JSON にシリアライズされるどのような Python オブジェクトをも許容します。

    :ref:`article-data-persistence`
        Python プログラムからデータを格納するその他のサンプル

.. _JavaScript Object Notation: http://json.org/
