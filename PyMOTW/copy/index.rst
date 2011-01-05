..
   =========================
   copy -- Duplicate objects
   =========================

============================
copy -- オブジェクトのコピー
============================

.. module:: copy
    :synopsis: オブジェクトを浅い動作や深い動作を使いコピーをする関数の提供

..
   :Purpose: Provides functions for duplicating objects using shallow or deep copy semantics.
   :Python Version: 1.4

:目的: オブジェクトを浅い動作や深い動作を使いコピーをする関数の提供
:Python バージョン: 1.4


..
   The copy module includes 2 functions, copy() and deepcopy(), for duplicating
   existing objects.

copy モジュールは存在するオブジェクトのコピーのために、 copy() と deepcopy() の 2 つの関数を含んでいます。

..
   Shallow Copies
   ==============

浅いコピー
==========

..
   The shallow copy created by copy() is a new container populated with
   references to the contents of the original object. For example, a new list is
   constructed and the elements of the original list are appended to it.

copy() 関数によって作られる浅いコピーは、元のオブジェクトの内容への参照を含んだ新しいコンテイナとなっています。例えば、新しいリストが作られ、そして元のリストの要素がそこに加えられます。

.. include:: copy_shallow.py
    :literal:
    :start-after: #end_pymotw_header

..
   For a shallow copy, the MyClass instance is not duplicated so the reference in
   the dup list is to the same object that is in the l list.

浅いコピーでは、 MyClass インスタンスは複製されません。なので、 dup リストに含まれた参照は、 l リストに含まれたものとなっています。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'copy_shallow.py'))
.. }}}
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

deepcopy() 関数を使って作られた深いコピーは、元のオブジェクトの内容のコピーを含んだ新しいコンテイナとなっています。例えば、新しいリストが作られ、そして元のリストの要素がコピーされます。そして、コピーされた後のものが作られた新しいリストに加えられます。

..
   By replacing the call to copy() with deepcopy(), the difference becomes
   apparent.

先程の例において、 copy() 関数の呼び出しを deepcopy() に置き換えることによって、違いは明らかになります。

::

    dup = copy.deepcopy(l)

..
   Notice that the first element of the list is no longer the same object
   reference, but the two objects still evaluate as being equal.

リストの最初の要素がもはや同じオブジェクトへの参照でないことに注意してください。しかしながら、 2 つのオブジェクトは未だ等しい物として評価されます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'copy_deep.py'))
.. }}}
.. {{{end}}}


..
   Controlling Copy Behavior
   =========================

コピーの挙動の制御
==================

..
   It is possible to control how copies are made using the __copy__ and
   __deepcopy__ hooks.

__copy__ と __deepcopy__ を使うことで、どのようにコピーがなされるかを制御することが可能となっています。

..
   * __copy__() is called without any arguments and should return a shallow copy
     of the object.

* __copy__() は引数なしで呼び出され、オブジェクトの浅いコピーを返すべきとなっています。

..
   * __deepcopy__() is called with a memo dictionary, and should return a
     deep copy of the object. Any member attributes that need to be
     deep-copied should be passed to copy.deepcopy(), along with the memo
     dictionary, to control for recursion (see below).

* __deepcopy__() は小さなメモのようなディクショナリと共に呼び出され、オブジェクトの深いコピーを返すべきとなっています。再帰のコントロールの為に、深いコピーをされるべき属性はすべてメモのようなディクショナリと共に copy.deepcopy() に渡されるべきとなっています。(以下参照)

..
   This example illustrates how the methods are called:

以下の例はどのようにメソッドが呼び出されるかを示しています。

.. include:: copy_hooks.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'copy_hooks.py'))
.. }}}
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

再帰のかかったデータ構造を複製する問題を避けるために、 ``deepcopy()`` 関数は既にコピーされたオブジェクトを追うために、ディクショナリを使用します。このディクショナリは ``__deepcopy__()`` メソッドに渡されることにより、そこで同様に使用されます。

..
   This example shows how an interconnected data structure such as a Digraph
   might assist with protecting against recursion by implementing a
   ``__deepcopy__()`` method. This particular example is just for illustration
   purposes, since the default implementation of ``deepcopy()`` already handles the
   recursion cases correctly.

以下の例は ``__deepcopy__()`` メソッドを実装することにより、どのようにして有向グラフのような相互に連結されたデータ構造が再帰に対しての保護を助けるかどうかを示しています。デフォルトでの ``deepcopy()`` の実装自体が再帰の場合を正しく対処するため、この例は示すだけのものとなっています。

.. include:: copy_recursion.py
    :literal:
    :start-after: #end_pymotw_header

..
   First, some basic directed graph methods: A graph can be initialized with a
   name and a list of existing nodes to which it is connected. The
   addConnection() method is used to set up bi-directional connections. It is
   also used by the deepcopy operator.

まず初めに、基本的な有向グラフのメソッドについて見てみましょう。まずグラフはグラフの名前とグラフが連結されている、存在する節のリストと共に初期化されます。 addConnection() メソッドは双方向の連結を作るために使われます。これはまた deepcopy 演算子によっても使用されます。

..
   The ``__deepcopy__()`` method prints messages to show how it is called, and
   manages the memo dictionary contents as needed. Instead of copying the
   connection list wholesale, it creates a new list and appends copies of the
   individual connections to it. That ensures that the memo dictionary is updated
   as each new node is duplicated, and avoids recursion issues or extra copies of
   nodes. As before, it returns the copied object when it is done.

``__deepcopy__()`` メソッドは、どのようにして呼び出されるかを示すためにメッセージを表示し、必要ならばメモのようなディクショナリを管理します。連結のリストすべてをコピーする代わりに、新しいリストを作成し、個々の連結のコピーをそこに加えます。それぞれの節が複製されるたびにメモのようなディクショナリが更新されているか確かにし、再帰問題や、節の余分なコピーを避けます。前と同じように、終了時にはコピーされたオブジェクトを返します。

..
   Next we can set up a graph with a nodes *root*, *a*, and *b*. The
   graph looks like:

次に、 *root*, *a*, *b* の節でできたグラフを用意します。グラフは次のようなものです。

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

グラフにはいくつかのループがありますが、ディクショナリを使って再帰に対処することで走査する際にスタックオーバーフローエラーが起こるのを避けることができます。 *root* の節がコピーされた時は以下のようになります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'copy_recursion.py'))
.. }}}
.. {{{end}}}

..
   The second time the *root* node is encountered, while the *a* node is
   being copied, ``__deepcopy__`` detects the recursion and re-uses the
   existing value from the memo dictionary instead of creating a new
   object.

*root* の節が 2 回目に出てきたとき、 *a* の節はコピーされているので、 ``__deepcopy__`` は再帰を検知し、新しいオブジェクトを作成する代わりに、ディクショナリから存在する値を再利用する。

.. seealso::

    `copy <http://docs.python.org/library/copy.html>`_
        このモジュールの基本ドキュメンテーション
