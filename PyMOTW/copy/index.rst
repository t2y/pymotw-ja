..
   =========================
   copy -- Duplicate objects
   =========================

============================
copy -- オブジェクトのコピー
============================

..
    :synopsis: Provides functions for duplicating objects using shallow or deep copy semantics.

.. module:: copy
    :synopsis: 浅いコピー(shallow copy)や深いコピー(deep copy)でオブジェクトをコピーする関数を提供する

..
    :Purpose: Provides functions for duplicating objects using shallow or deep copy semantics.
    :Available In: 1.4

:目的: 浅いコピー(shallow copy)や深いコピー(deep copy)でオブジェクトをコピーする関数を提供する
:利用できるバージョン: 1.4

..
   The copy module includes 2 functions, copy() and deepcopy(), for duplicating
   existing objects.

copy モジュールは既存のオブジェクトをコピーする copy() と deepcopy() の2つの関数を提供します。

..
   Shallow Copies
   ==============

浅いコピー
==========

..
   The shallow copy created by copy() is a new container populated with
   references to the contents of the original object. For example, a new list is
   constructed and the elements of the original list are appended to it.

copy() 関数が作成する浅いコピーは、元のオブジェクトのコンテンツへの参照をもつコンテナです。例えば、新しいリストが作られて、元のリストの要素がそのリストへ加えられます。

.. include:: copy_shallow.py
    :literal:
    :start-after: #end_pymotw_header

..
   For a shallow copy, the MyClass instance is not duplicated so the reference in
   the dup list is to the same object that is in the l list.

浅いコピーでは、MyClass のインスタンスはコピーされません。そのため、dup リストのオブジェクトの参照先は l リストのオブジェクトと同じです。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'copy_shallow.py'))
.. }}}

::

	$ python copy_shallow.py
	
	l  : [<__main__.MyClass instance at 0x100467d88>]
	dup: [<__main__.MyClass instance at 0x100467d88>]
	dup is l: False
	dup == l: True
	dup[0] is l[0]: True
	dup[0] == l[0]: True

.. {{{end}}}


..
   Deep Copies
   ===========

深いコピー
==========

..
   The deep copy created by deepcopy() is a new container populated with copies
   of the contents of the original object. For example, a new list is constructed
   and the elements of the original list are copied, then the copies are appended
   to the new list.

deepcopy() 関数が作成する深いコピーは、元のオブジェクトのコンテンツのコピーをもつ新しいコンテナです。例えば、新しいリストが作られて、元のリストの要素がコピーされます。それからコピーされた要素が新しいリストへ加えられます。

..
   By replacing the call to copy() with deepcopy(), the difference becomes
   apparent.

先程の例において、copy() 関数の呼び出しを deepcopy() に置き換えることにより、その違いは明らかになります。

::

    dup = copy.deepcopy(l)

..
   Notice that the first element of the list is no longer the same object
   reference, but the two objects still evaluate as being equal.

リストの最初の要素がもはや同じオブジェクトへの参照でないことに注意してください。しかし、2つのオブジェクトはそれでも等しいと評価されます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'copy_deep.py'))
.. }}}

::

	$ python copy_deep.py
	
	l  : [<__main__.MyClass instance at 0x100467d88>]
	dup: [<__main__.MyClass instance at 0x100467dd0>]
	dup is l: False
	dup == l: True
	dup[0] is l[0]: False
	dup[0] == l[0]: True

.. {{{end}}}


..
   Controlling Copy Behavior
   =========================

コピーの振る舞いの制御
======================

..
   It is possible to control how copies are made using the __copy__ and
   __deepcopy__ hooks.

__copy__ と __deepcopy__ フックを使用して、コピーする方法を制御することができます。

..
   * __copy__() is called without any arguments and should return a shallow copy
     of the object.

* __copy__() は引数なしで呼び出され、オブジェクトの浅いコピーを返します。

..
   * __deepcopy__() is called with a memo dictionary, and should return a
     deep copy of the object. Any member attributes that need to be
     deep-copied should be passed to copy.deepcopy(), along with the memo
     dictionary, to control for recursion (see below).

* __deepcopy__() はメモディクショナリと共に呼び出され、オブジェクトの深いコピーを返します。深いコピーが行われる全てのメンバ属性は、再起を制御するためにメモディクショナリと共に copy.deepcopy() へ渡されます。(以下を参照)

..
   This example illustrates how the methods are called:

以下の例はどのようにメソッドが呼び出されるかを示しています。

.. include:: copy_hooks.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'copy_hooks.py'))
.. }}}

::

	$ python copy_hooks.py
	
	__copy__()
	__deepcopy__({})

.. {{{end}}}


..
   Recursion in Deep Copy
   ======================

深いコピーにおける再帰
======================

..
   To avoid problems with duplicating recursive data structures, ``deepcopy()`` uses
   a dictionary to track objects that have already been copied. This dictionary
   is passed to the ``__deepcopy__()`` method so it can be used there as well.

再帰的なデータ構造のコピーによる問題を避けるために ``deepcopy()`` 関数は既にコピーされたオブジェクトを保持するディクショナリを使用します。このディクショナリは ``__deepcopy__()`` メソッドに渡されるので、そこでも同様に使用されます。

..
   This example shows how an interconnected data structure such as a Digraph
   might assist with protecting against recursion by implementing a
   ``__deepcopy__()`` method. This particular example is just for illustration
   purposes, since the default implementation of ``deepcopy()`` already handles the
   recursion cases correctly.

この例は ``__deepcopy__()`` メソッドを実装することにより、有向グラフのような相互に連結されたデータ構造が再起に対して保護し易くする方法を説明します。デフォルトの ``deepcopy()`` 実装が再起のデータ構造を正しく扱うので、この例はただ説明目的だけのものです。

.. include:: copy_recursion.py
    :literal:
    :start-after: #end_pymotw_header

..
   First, some basic directed graph methods: A graph can be initialized with a
   name and a list of existing nodes to which it is connected. The
   addConnection() method is used to set up bi-directional connections. It is
   also used by the deepcopy operator.

まず初めに、基本的な有向グラフのメソッドについて見てみましょう。グラフは名前とそのグラフが連結される既存のノードリストで初期化されます。addConnection() メソッドは双方向に連結するために使われます。またそれは deepcopy 演算子により使用されます。

..
   The ``__deepcopy__()`` method prints messages to show how it is called, and
   manages the memo dictionary contents as needed. Instead of copying the
   connection list wholesale, it creates a new list and appends copies of the
   individual connections to it. That ensures that the memo dictionary is updated
   as each new node is duplicated, and avoids recursion issues or extra copies of
   nodes. As before, it returns the copied object when it is done.

``__deepcopy__()`` メソッドは、どのようにして呼び出されるかを示すためにメッセージを表示して、必要に応じてメモディクショナリを管理します。連結のリスト全てをコピーせずに、新しいリストを作成し、個々の連結のコピーをそこに加えます。それぞれのノードがコピーされると、メモディクショナリが更新されることを保証します。そして、再帰の問題やノードの追加コピーを避けます。前のセクションで説明したように、終了時にコピーされたオブジェクトを返します。

..
   Next we can set up a graph with a nodes *root*, *a*, and *b*. The
   graph looks like:

次に *root*, *a*, *b* のノードをもつグラフを用意します。グラフは次のようなものです。

.. digraph:: copy_example

   "root";
   "a" -> "root";
   "b" -> "root";
   "b" -> "a";
   "root" -> "a";
   "root" -> "b";

..
   There are several cycles in the graph, but by handling the recursion
   with the memo dictionary we can avoid having the traversal cause a
   stack overflow error.  When the *root* node is copied, we see:

グラフ内の参照先が循環しますが、メモディクショナリでその再帰処理を扱うことでスタックオーバーフローエラーを発生させないようにします。 *root* ノードがコピーされるときは以下のようになります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'copy_recursion.py'))
.. }}}

::

	$ python copy_recursion.py
	
	
	<Graph(root) id=4299639696>
	{   }
	  COPYING TO <Graph(root) id=4299640056>
	
	<Graph(a) id=4299639768>
	{   <Graph(root) id=4299639696>: <Graph(root) id=4299640056>,
	    4298517936: ['root'],
	    4299576592: 'root'}
	  COPYING TO <Graph(a) id=4299640128>
	
	<Graph(root) id=4299639696>
	  ALREADY COPIED TO <Graph(root) id=4299640056>
	
	<Graph(b) id=4299639840>
	{   <Graph(root) id=4299639696>: <Graph(root) id=4299640056>,
	    <Graph(a) id=4299639768>: <Graph(a) id=4299640128>,
	    4297844216: 'a',
	    4298517936: [   'root',
	                    'a',
	                    <Graph(root) id=4299639696>,
	                    <Graph(a) id=4299639768>],
	    4299576592: 'root',
	    4299639696: <Graph(root) id=4299640056>,
	    4299639768: <Graph(a) id=4299640128>}
	  COPYING TO <Graph(b) id=4299640632>

.. {{{end}}}

..
   The second time the *root* node is encountered, while the *a* node is
   being copied, ``__deepcopy__`` detects the recursion and re-uses the
   existing value from the memo dictionary instead of creating a new
   object.

*root* ノードが2回目に出てきたとき *a* ノードはコピーされているので、 ``__deepcopy__`` は再帰を検知し、新しいオブジェクトを作成せずにメモディクショナリから既存の値を再利用します。

.. seealso::

    `copy <http://docs.python.org/library/copy.html>`_
        .. The standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント
