..
    =================================================
    pickle and cPickle -- Python object serialization
    =================================================

============================================================
pickle と cPickle -- Python オブジェクトシリアライゼーション
============================================================

..
    :synopsis: Python object serialization

.. module:: pickle
    :synopsis: Python オブジェクトシリアライゼーション

..
    :synopsis: Python object serialization

.. module:: cPickle
    :synopsis: Python オブジェクトシリアライゼーション

..
    :Purpose: Python object serialization
    :Python Version: pickle at least 1.4, cPickle 1.5

:目的: Python オブジェクトシリアライゼーション
:Python バージョン: pickle は 1.4, cPickle は 1.5

..
    The :mod:`pickle` module implements an algorithm for turning an
    arbitrary Python object into a series of bytes.  This process is also
    called *serializing*" the object. The byte stream representing the
    object can then be transmitted or stored, and later reconstructed to
    create a new object with the same characteristics.

:mod:`pickle` モジュールは任意の Python オブジェクトをバイトデータに変換するアルゴリズムを実装します。この処理もまたオブジェクトの *シリアライズ* と呼ばれます。バイトストリームは転送または格納されて、後で同じ特性を持つ新たなオブジェクトを作成して再構築されるオブジェクトを表します。

..
    The :mod:`cPickle` module implements the same algorithm, in C instead
    of Python. It is many times faster than the Python implementation, but
    does not allow the user to subclass from Pickle. If subclassing is not
    important for your use, you probably want to use cPickle.

:mod:`cPickle` モジュールは同じアルゴリズムを Python ではなく C 言語で実装します。それは Python の実装よりも何倍か速いですが、ユーザは Pickle からサブクラス化することができません。サブクラス化が重要ではない用途なら、おそらく cPickle を使いたくなるでしょう。

.. warning::

    .. The documentation for pickle makes clear that it offers no security
       guarantees. Be careful if you use pickle for inter-process communication or
       data storage.  Do not trust data you cannot verify as secure.
     
    pickle のドキュメントにはセキュリティの保証がないことが明確に記載されています。プロセス間通信、もしくはデータストレージに pickle を使用する場合に注意してください。セキュアだと証明できないデータを信頼してはいけません。

..
    Importing
    =========

インポート
==========

..
    It is common to first try to import cPickle, giving an alias of
    "pickle". If that import fails for any reason, you can then fall back
    on the native Python implementation in the pickle module. This gives
    you the faster implementation, if it is available, and the portable
    implementation otherwise.

最初に cPickle をインポートしようとして "pickle" のエイリアスにするのが一般的です。何らかの理由でインポートに失敗したら、それからネイティブ Python 実装である pickle モジュールをインポートします。このインポートは利用可能ならより速い実装を、そうでないなら移植性の高い実装を提供するものです。

::

    try:
       import cPickle as pickle
    except:
       import pickle

..
    Encoding and Decoding Data in Strings
    =====================================

文字列のエンコーディングとデコーディングデータ
==============================================

..
    This first example encodes a data structure as a string, then prints
    the string to the console. It uses a data structure made up of
    entirely native types. Instances of any class can be pickled, as will
    be illustrated in a later example.  Use ``pickle.dumps()`` to create a
    string representation of the value of the object.

最初のサンプルは文字としてのデータ構造をエンコードします。それからコンソールに文字列を表示します。それは完全にネイティブ型で構成されたデータ構造を使用します。pickle されたクラスのインスタンスは、この後のサンプルで説明します。オブジェクトの値を文字列で表すために ``pickle.dumps()`` を使用してください。

.. include:: pickle_string.py
    :literal:
    :start-after: #end_pymotw_header

..
    By default, the pickle will contain only ASCII characters. A more
    efficient binary format is also available, but all of the examples
    here use the ASCII output because it is easier to understand in print.

デフォルトでは、pickle は ASCII 文字のみを含みます。もっと効率的なバイナリフォーマットも利用できますが、ここでのサンプルは表示された内容が理解し易いので ASCII 出力のみを扱います。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'pickle_string.py'))
.. }}}
.. {{{end}}}

..
    Once the data is serialized, you can write it to a file, socket, pipe, etc.
    Then later you can read the file and unpickle the data to construct a new
    object with the same values.

データがシリアライズされるとき、ファイル、ソケット、パイプ等に書き込むことができます。この後でファイルを読み込んで同じ値で新たなオブジェクトを構築するためにデータを unpickle します。

.. include:: pickle_unpickle.py
    :literal:
    :start-after: #end_pymotw_header

..
    As you see, the newly constructed object is the equal to but not the same
    object as the original. No surprise there.

ご覧の通り、新たに構築されたオブジェクトは等価ですが、オリジナルと同じオブジェクトではありません。そこは納得できますね。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'pickle_unpickle.py'))
.. }}}
.. {{{end}}}

..
    Working with Streams
    ====================

ストリームと連携する
====================

..
    In addition to ``dumps()`` and ``loads()``, pickle provides a couple
    of convenience functions for working with file-like streams. It is
    possible to write multiple objects to a stream, and then read them
    from the stream without knowing in advance how many objects are
    written or how big they are.

``dumps()`` や ``loads()`` に加えて、pickle はファイルのようなストリームと連携する便利な関数を提供します。それはストリームに対して複数のオブジェクトを書き込むことができます。そして、書き込んだデータがどんなに巨大でも、先に何回書き込まれたかを知らなくてもストリームからそのデータを読み込めます。

.. include:: pickle_stream.py
    :literal:
    :start-after: #end_pymotw_header

..
    The example simulates streams using StringIO buffers, so we have to
    play a little trickery to establish the readable stream. A simple
    database format could use pickles to store objects, too, though
    :mod:`shelve` would be easier to work with.

このサンプルは StringIO バッファを使用してストリームを模倣します。読み込み可能なストリームを作成するには少しトリッキーなことを行う必要があるからです。シンプルなデータベースフォーマットは pickle を使用してオブジェクトを格納することもできますが、 :mod:`shelve` はもっと簡単に連携することができます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'pickle_stream.py'))
.. }}}
.. {{{end}}}

..
    Besides storing data, pickles are very handy for inter-process
    communication. For example, using ``os.fork()`` and ``os.pipe()``, one
    can establish worker processes that read job instructions from one
    pipe and write the results to another pipe. The core code for managing
    the worker pool and sending jobs in and receiving responses can be
    reused, since the job and response objects don't have to be of a
    particular class. If you are using pipes or sockets, do not forget to
    flush after dumping each object, to push the data through the
    connection to the other end.  See :mod:`multiprocessing` if you don't
    want to write your own worker pool manager.

データを格納することに加えて、pickle はプロセス間通信にとても扱い易いです。例えば、 ``os.fork()`` や ``os.pipe()`` を使用して、あるパイプからジョブ命令を読み込み、別のパイプへ結果を書き込むワーカープロセスを作成します。ワーカープールを管理してジョブを送信したり結果を受信したりするコア部分は再利用されます。それはジョブとレスポンスオブジェクトが特定のクラスである必要がないからです。もしパイプやソケットを使用しているなら、他端とのコネクションを経由してデータをプッシュするために、それぞれのオブジェクトをダンプした後でフラッシュするのを忘れないでください。独自のワーカープールマネージャを書きたくないなら :mod:`multiprocessing` を参照してください。

..
    Problems Reconstructing Objects
    ===============================

オブジェクトを再構築するときの問題
==================================

..
    When working with your own classes, you must ensure that the class being
    pickled appears in the namespace of the process reading the pickle. Only the
    data for the instance is pickled, not the class definition. The class name is
    used to find the constructor to create the new object when unpickling. Take
    this example, which writes instances of a class to a file:

独自クラスと連携するとき、その pickle を読み込むプロセスの名前空間に pickle 化されたクラスが現れることを保証しなければなりません。そのインスタンスのためのデータのみが pickle 化されます、それはクラス定義ではありません。クラス名は unpickle されるときに新しいオブジェクトを作成するコンストラクタを見つけるために使用されます。ファイルへクラスのインスタンスを書き込むサンプルを見てください

.. include:: pickle_dump_to_file_1.py
    :literal:
    :start-after: #end_pymotw_header

..
    When run, the script creates a file based on the name given as
    argument on the command line:

実行すると、そのスクリプトはコマンドラインで引数として与えた名前でファイルを作成します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'pickle_dump_to_file_1.py test.dat'))
.. }}}
.. {{{end}}}

..
    A simplistic attempt to load the resulting pickled objects fails:

実行結果の pickle 化されたオブジェクトを読み込もうとすると失敗します。

.. include:: pickle_load_from_file_1.py
    :literal:
    :start-after: #end_pymotw_header

..
    This version fails because there is no SimpleObject class available:

このサンプルは SimpleObject クラスが定義されてないので失敗します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'pickle_load_from_file_1.py test.dat', ignore_error=True))
.. }}}
.. {{{end}}}

..
    The corrected version, which imports SimpleObject from the original
    script, succeeds.

正しいサンプルはオリジナルのスクリプトから SimpleObject をインポートすると成功します。

..
    Add:

次を追加します。

::

    from pickle_dump_to_file_1 import SimpleObject

..
    to the end of the import list, then re-run the script:

インポートリストの最後に追加してから、そのスクリプトを再実行します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'pickle_load_from_file_2.py test.dat'))
.. }}}
.. {{{end}}}

..
    There are some special considerations when pickling data types with
    values that cannot be pickled (sockets, file handles, database
    connections, etc.). Classes that use values which cannot be pickled
    can define ``__getstate__()`` and ``__setstate__()`` to return a
    subset of the state of the instance to be pickled. New-style classes
    can also define ``__getnewargs__()``, which should return arguments to
    be passed to the class memory allocator (``C.__new__()``).  Use of
    these features is covered in more detail in the standard library
    documentation.

pickle 化できない値を持つデータ型(ソケット、ファイルハンドラ、データベースコネクション等)を pickle 化するときは特に注意することがあります。pickle 化できない値を使用するクラスはpickle 化されるインスタンスの状態のサブセットを返す ``__getstate__()`` や ``__setstate__()`` を定義します。さらに新スタイルクラスはクラスメモリアロケータ(``C.__new__()``)へ渡される引数を返す ``__getnewargs__()`` も定義します。こういった機能を利用するには、標準ライブラリドキュメントに詳細が説明されています。

..
    Circular References
    ===================

循環参照
========

..
    The pickle protocol automatically handles circular references between
    objects, so you don't need to do anything special with complex data
    structures.  Consider the digraph:

pickle プロトコルは自動的にオブジェクト間の循環参照を扱います。そのため、複雑なデータ構造でも特別に何かをする必要はありません。ダイグラフを考えてみましょう。

.. digraph:: pickle_example

   "root";
   "root" -> "a";
   "root" -> "b";
   "a" -> "b";
   "b" -> "a";
   "b" -> "c";
   "a" -> "a";

..
    Even though the graph includes several cycles, the correct structure
    can be pickled and then reloaded.

グラフは複数のサイクルを含みますが、正しい構造で pickle 化されて再読み込みされます。

.. include:: pickle_cycle.py
    :literal:
    :start-after: #end_pymotw_header

..
    The reloaded nodes are not the same object, but the relationship
    between the nodes is maintained and only one copy of the object with
    multiple reference is reloaded. Both of these statements can be
    verified by examining the ``id()`` values for the nodes before and
    after being passed through pickle.

再読み込みされたノードは同じオブジェクトではありませんが、そのノード間の関係は保持されていて、複数の参照先を持つオブジェクトのコピーが1つだけ再読み込みされます。いま説明した内容は pickle を経由する前後でノードの ``id()`` 値を調べることで検証することができます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'pickle_cycle.py'))
.. }}}
.. {{{end}}}


.. seealso::

    `pickle <http://docs.python.org/lib/module-pickle.html>`_
        .. Standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント

    :mod:`shelve`
        .. The shelve module.
        
        shelve モジュール

    `Pickle: An interesting stack language. <http://peadrop.com/blog/2007/06/18/pickle-an-interesting-stack-language/>`__
        .. by Alexandre Vassalotti

        Alexandre Vassalotti による説明

    :ref:`article-data-persistence`
