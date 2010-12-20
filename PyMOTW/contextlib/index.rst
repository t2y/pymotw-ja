..
    =======================================
    contextlib -- Context manager utilities
    =======================================

==================================================
contextlib -- コンテキストマネージャユーティリティ
==================================================

..
    :synopsis: Utilities for creating and working with context managers.

.. module:: contextlib
    :synopsis: コンテキストマネージャの操作ユーティリティ

..
    :Purpose: Utilities for creating and working with context managers.
    :Python Version: 2.5 and later

:目的: コンテキストマネージャを作成して操作するためのユーティリティ
:Python バージョン: 2.5

..
    The :mod:`contextlib` module contains utilities for working with
    context managers and the :command:`with` statement.

:mod:`contextlib` モジュールはコンテキストマネージャと :command:`with` 文を連携させるユーティリティを提供します。

.. note:: 
    ..
        Context managers are tied to the :command:`with` statement. Since
        :command:`with` is officially part of Python 2.6, you have to import it
        from :mod:`__future__` before using contextlib in Python 2.5.

    コンテキストマネージャは ``with`` 文と関係があります。 :command:`with` 文は Python 2.6 から公式対応になるので Python 2.5 で contextlib を使用するには from :mod:`__future__` からインポートする必要があります。

..
    Context Manager API
    ===================

コンテキストマネージャ API
==========================

..
    A *context manager* is responsible for a resource within a code block,
    possibly creating it when the block is entered and then cleaning it up
    after the block is exited.  For example, files support the context
    manager API to make it easy to ensure they are closed after all
    reading or writing is done.

*コンテキストマネージャ* はコードブロック内のリソース管理に責任を持ちます。それはブロックに入るときにそのリソースが生成されて、ブロックから出るときにクリーンアップするような場合です。例えば、コンテキストマネージャの API をサポートするファイルは、そのファイルが全て読み込み、または書き込みされた後でクローズされることを保証するのが簡単になります。

.. include:: contextlib_file.py
   :literal:
   :start-after: #end_pymotw_header

..
    A context manager is enabled by the :command:`with` statement, and the
    API involves two methods.  The :func:`__enter__` method is run when
    execution flow enters the code block inside the :command:`with`.  It
    returns an object to be used within the context.  When execution flow
    leaves the :command:`with` block, the :func:`__exit__` method of the
    context manager is called to clean up any resources being used.

コンテキストマネージャは :command:`with` 文により利用可能となり、その API は2つのメソッドを実行します。 :func:`__enter__` メソッドは実行フローが :command:`with` 内部のコードブロックに入るときに実行されます。そしてコンテキスト内で使用されるオブジェクトを返します。実行フローが :command:`with` ブロックを出るときにコンテキストマネージャの :func:`__exit__` メソッドが使用されたリソースをクリーンアップするために呼ばれます。

.. include:: contextlib_api.py
   :literal:
   :start-after: #end_pymotw_header

..
    Combining a context manager and the :command:`with` statement is a
    more compact way of writing a ``try:finally`` block, since the context
    manager's :func:`__exit__` method is always called, even if an
    exception is raised.

コンテキストマネージャと :command:`with` 文を組み合わせることは ``try:finally`` ブロックをよりも小さなコーディングで済みます。それはエラーが発生したとしても、コンテキストマネージャの :func:`__exit__` メソッドは常に呼び出されるからです。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'contextlib_api.py'))
.. }}}
.. {{{end}}}

..
    :func:`__enter__` can return any object to be associated with a name
    specified in the :command:`as` clause of the :command:`with`
    statement.  In this example, the :class:`Context` returns an object
    that uses the open context.

:func:`__enter__` は :command:`with` 文の :command:`as` で指定された名前に関連付けられるオブジェクトを返します。このサンプルでは、 :class:`Context` はオープンされたコンテキストを使用するオブジェクトを返します。

.. include:: contextlib_api_other_object.py
   :literal:
   :start-after: #end_pymotw_header

..
    It can be a little confusing, but the value associated with the
    variable :data:`c` is the object returned by :func:`__enter__` and
    *not* the :class:`Context` instance created in the :command:`with`
    statement.

少し混乱するかもしれませんが、変数 :data:`c` に関連付けられた値は :func:`__enter__` が返すオブジェクトで :command:`with` 文で作成された :class:`Context` インスタンスでは *ありません* 。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'contextlib_api_other_object.py'))
.. }}}
.. {{{end}}}

..
    The :func:`__exit__` method receives arguments containing details of
    any exception raised in the :command:`with` block.  

:func:`__exit__` メソッドは :command:`with` ブロック内で発生した例外の詳細を引数により受け取ります。

.. include:: contextlib_api_error.py
   :literal:
   :start-after: #end_pymotw_header

..
    If the context manager can handle the exception, :func:`__exit__`
    should return a true value to indicate that the exception does not
    need to be propagated.  Returning false causes the exception to be
    re-raised after :func:`__exit__` returns.

コンテキストマネージャが例外を扱う場合、その例外を伝搬する必要がないなら :func:`__exit__` は True を返します。False を返すことは :func:`__exit__` が返された後でその例外を再発生させることになります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'contextlib_api_error.py', ignore_error=True))
.. }}}
.. {{{end}}}

..
    From Generator to Context Manager
    =================================

ジェネレータからコンテキストマネージャへ
========================================

..
    Creating context managers the traditional way, by writing a class with
    :func:`__enter__()` and :func:`__exit__()` methods, is not
    difficult. But sometimes it is more overhead than you need just to
    manage a trivial bit of context. In those sorts of situations, you can
    use the :func:`contextmanager()` decorator to convert a generator
    function into a context manager.

伝統的な手法であるコンテキストマネージャを作成することは難しいことではありません。コンテキストマネージャは :func:`__enter__()` と :func:`__exit__()` メソッドを持つクラスを書くことで作成できます。しかし、あなたが些細なコンテキストを管理したいだけならちょっと面倒になるときがあります。そういった状況では、ジェネレータの機能をコンテキストマネージャの中に転用して :func:`contextmanager()` デコレータを使用することができます。

..
    The generator should initialize the context, yield exactly one time, then
    clean up the context. The value yielded, if any, is bound to the variable in
    the as clause of the with statement. Exceptions from within the with block are
    re-raised inside the generator, so you can handle them there.

ジェネレータはコンテキストを初期化すべきで yield が1回呼び出されてからコンテキストをクリーンアップします。もし yield された値があれば with 文の as で指定された変数にセットされます。with ブロック内からの例外はその発生場所で扱えるようにジェネレータ内部で再発生させます。

.. include:: contextlib_contextmanager.py
    :literal:
    :start-after: #end_pymotw_header

..
    The generator should initialize the context, yield exactly one time,
    then clean up the context. The value yielded, if any, is bound to the
    variable in the :command:`as` clause of the :command:`with`
    statement. Exceptions from within the :command:`with` block are
    re-raised inside the generator, so they can be handled there.

ジェネレータはコンテキストを初期化し、厳密に一度だけ yield します。それからそのコンテキストをクリーンアップします。yield される値があるなら :command:`with` 文の :command:`as` の変数に束縛されます。 :command:`with` ブロック内の例外は、ジェネレータ内部で扱うことができるので再発生させます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'contextlib_contextmanager.py', ignore_error=True))
.. }}}
.. {{{end}}}

..
    Nesting Contexts
    ================

ネストされたコンテキスト
========================

..
    At times it is necessary to manage multiple contexts simultaneously
    (such as when copying data between input and output file handles, for
    example). It is possible to nest :command:`with` statements one inside
    another. If the outer contexts do not need their own separate block,
    though, this adds to the indention level without giving any real
    benefit. Using :func:`nested()` nests the contexts using a single
    :command:`with` statement.

時々、複数のコンテキストを同時に管理する必要があります(例えば、入出力のファイルハンドラ間でデータをコピーするときです)。そういったときに複数のコンテキスト間で with 文をネストすることができます。もし外側のコンテキストが独立したブロックである必要性がない場合、何の利点はなくてもインデントレベルを追加してしまいます。 :func:`nested()` を使用すると1つの :command:`with` 文でそういったコンテキストをネストします。

.. include:: contextlib_nested.py
    :literal:
    :start-after: #end_pymotw_header

..
    Notice that the contexts are exited in the reverse order in which they are
    entered.

entering したコンテキストとは逆の順番で exiting していることに注意してください。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'contextlib_nested.py'))
.. }}}
.. {{{end}}}

..
    In Python 2.7 and later, :func:`nested` is deprecated because the
    :command:`with` statement supports nesting directly.

Python 2.7 以上では、 :command:`with` 文が直接ネストすることをサポートしたことにより :func:`nested` は廃止予定です。

.. include:: contextlib_nested_with.py
   :literal:
   :start-after: #end_pymotw_header

..
    Each context manager and optional :command:`as` clause are separated
    by a comma (``,``).  The effect is similar to using :func:`nested`,
    but avoids some of the edge-cases around error handling that
    :func:`nested` could not implement correctly.

それぞれのコンテキストマネージャとオプションの :command:`as` はカンマ (``,``) で分割されます。その効果は :func:`nested` を使用するのと似ていますが、 :func:`nested` が正しく実装できないエラー処理関連の特別な状況を回避します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'contextlib_nested_with.py'))
.. }}}
.. {{{end}}}

..
    Closing Open Handles
    ====================

オープンハンドラをクローズする
==============================

..
    The :class:`file` class supports the context manager API directly, but
    some other objects that represent open handles do not. The example
    given in the standard library documentation for :mod:`contextlib` is
    the object returned from :func:`urllib.urlopen`.  There are other
    legacy classes that use a :func:`close` method but do not support the
    context manager API. To ensure that a handle is closed, use
    :func:`closing()` to create a context manager for it.

:class:`file()` クラスはコンテキストマネージャの API を直接サポートしますが、オープンハンドラを表す他のオブジェクトによってはサポートしないものもあります。 :mod:`contextlib` の標準ライブラリドキュメントで説明されている例では :func:`urllib.urlopen()` から返されるオブジェクトがサポートしないものに該当します。 :func:`close` メソッドを使用するレガシーなクラスが他にもありますが、コンテキストマネージャ API をサポートしません。ハンドラがクローズされることを保証するには、そういったコンテキストマネージャを作成するための :func:`closing()` を使用してください。

.. include:: contextlib_closing.py
    :literal:
    :start-after: #end_pymotw_header

..
    The handle is closed whether there is an error in the :command:`with`
    block or not.

:command:`with` ブロック内でエラーが発生するか否かに関わらずハンドラがクローズされます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'contextlib_closing.py'))
.. }}}
.. {{{end}}}

.. seealso::

    `contextlib <http://docs.python.org/library/contextlib.html>`_
        .. The standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント

    :pep:`343`
        .. The :command:`with` statement.

        :command:`with` 文

    `Context Manager Types <http://docs.python.org/library/stdtypes.html#typecontextmanager>`__
        .. Description of the context manager API from the standard library documentation.

        標準ライブラリドキュメントのコンテキストマネージャ API の説明

    `With Statement Context Managers <http://docs.python.org/reference/datamodel.html#context-managers>`__
        .. Description of the context manager API from the Python Reference Guide.

        Python リファレンスガイドのコンテキストマネージャ API の説明
