.. _article-data-structures:

####################
インメモリデータ構造
####################

..
    #########################
    In-Memory Data Structures
    #########################

..
    Python includes several standard programming data structures as `built-in types <http://docs.python.org/library/stdtypes.html>`_ (list, tuple, dictionary, and set).  Most applications won't need any other structures, but when they do the standard library delivers.

Python は標準的なプログラミングのデータ構造を `組み込み型 <http://docs.python.org/library/stdtypes.html>`_  (リスト、タプル、ディクショナリ、集合) として提供します。ほとんどのアプリケーションではそれ以上のデータ構造は必要ないですが、必要になったとき標準ライブラリが提供してくれます。

..
    array
    =====

配列
====

..
    For large amounts of data, it may be more efficient to use an :mod:`array` instead of a ``list``.  Since the array is limited to a single data type, it can use a more compact memory representation than a general purpose list.  As an added benefit, arrays can be manipulated using many of the same methods as a list, so it may be possible to replaces lists with arrays in to your application without a lot of other changes.

大量データの用途には ``list`` ではなく :mod:`array` を使用した方が効率が良くなるかもしれません。array は1つのデータ型のみに制限されるので、汎用目的のリストよりもメモリ表現が小さくなります。この利点に加えて、array はリストとほとんど同じメソッドで操作できます。そのため、アプリケーションに大きな変更なく、リストから array に置き換えられる可能性があります。

..
    Sorting
    =======

ソート
======

..
    If you need to maintain a sorted list as you add and remove values, check out :mod:`heapq`.  By using the functions in :mod:`heapq` to add or remove items from a list, you can maintain the sort order of the list with low overhead.  

値を追加したり削除したりするときにソートされたリストを保持する必要があるときは :mod:`heapq` を調べてみてください。リストから要素を追加したり、削除したりするのに :mod:`heapq` の関数を使用することで、低いオーバーヘッドでリストの順番を保持できます。

..
    Another option for building sorted lists or arrays is :mod:`bisect`.  bisect uses a binary search to find the insertion point for new items, and is an alternative to repeatedly sorting a list that changes frequently.

ソートされたリストや array を作成する別の選択肢として :mod:`bisect` があります。 :mod:`bisect` は、新しい要素の挿入位置を2分探索で探すことで、変更する毎にリストのソートを繰り返すことの代替方法になります。

..
    Queue
    =====

キュー
======

..
    Although the built-in list can simulate a queue using the ``insert()`` and ``pop()`` methods, it isn't thread-safe.  For true ordered communication between threads you should use a :mod:`Queue`.  :mod:`multiprocessing` includes a version of a Queue that works between processes, making it easier to port between the modules.

組み込み型のリストは ``insert()`` と ``pop()`` メソッドでキューを模倣できますが、それはスレッドセーフではありません。スレッド間で本当の実行順序を保持するために :mod:`Queue` を使用してください。 :mod:`multiprocessing` は、モジュール間で簡単にやり取りできるようにプロセス間で動作するキューを提供します。

..
    collections
    ===========

コレクション
============

..
    :mod:`collections` includes implementations of several data structures that extend those found in other modules.  For example, Deque is a double-ended queue, and allows you to add or remove items from either end.  The ``defaultdict`` is a dictionary that responds with a default value if a key is missing.  And ``namedtuple`` extends the normal tuple to give each member item an attribute name in addition to a numerical index.

:mod:`collections` はその他のモジュールで見られる拡張データ構造の実装を提供します。例えば、Deque はどちらかの端からも要素を追加したり削除したりできる両端キューです。 ``defaultdict`` は、キーが存在しないときにデフォルト値を返すディクショナリです。 ``namedtuple`` は、数値インデックスに加えて属性名で要素のメンバーへアクセスできるようにタプルを拡張したものです。

..
    Decoding Data
    =============

データのデコード
================

..
    If you are working with data from another application, perhaps coming from a binary file or stream of data, you will find :mod:`struct` useful for decoding the data into Python's native types for easier manipulation.

別のアプリケーションとデータを連携する場合、バイナリファイルまたはデータストリームで入力されるかもしれません。 :mod:`struct` は、Python のネイティブ型にデータをデコードすることで簡単に操作させる便利なモジュールです。

..
    Custom Variations
    =================

カスタムデータ型
================

..
    And finally, if the available types don't give you what you need, you may want to subclass one of the native types and customize it.  You can also start from scratch by using the abstract base classes defined in :mod:`collections`.

最後に、目的にあう型がなかった場合、カスタマイズするためにネイティブ型の1つをサブクラス化して定義すると良いかもしれません。また :mod:`collections` で定義されている抽象ベースクラスで一から定義することもできます。
