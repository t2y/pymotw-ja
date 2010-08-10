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
    :Purpose:
        The contextlib module contains utilities for working with context managers
        and the ``with`` statement.
    :Python Version: 2.5

:目的: contextlib モジュールは ``with`` 文とコンテキストマネージャの操作ユーティリティを提供する
:Python バージョン: 2.5


.. note:: 
    ..
        Context managers are tied to the ``with`` statement. Since
        ``with`` is officially part of Python 2.6, you have to import it
        from :mod:`__future__` before using contextlib in Python 2.5.

    コンテキストマネージャは ``with`` 文と関係があります。 ``with`` 文は Python 2.6 から公式対応になるので Python 2.5 で contextlib を使用するには from :mod:`__future__` からインポートする必要があります。

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
    example). It is possible to nest with statements one inside
    another. If the outer contexts do not need their own separate block,
    though, this adds to the indention level without giving any real
    benefit. By using :func:`nested()`, you can nest the contexts and use
    a single ``with`` statement.

時々、複数のコンテキストを同時に管理する必要があります(例えば、入出力のファイルハンドラ間でデータをコピーするときです)。そういったときに複数のコンテンツ間で with 文をネストすることができます。もし外側のコンテキストが独立したブロックである必要性がない場合、そうとは言えこの例は実際には何の利点もありませんが、そのインデントレベルを追加します。 :func:`nested()` を使用することで、これらのコンテキストをネストして1つの ``with`` 文で使用することができます。

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
    Closing Open Handles
    ====================

オープンハンドラをクローズする
==============================

..
    The :class:`file()` class supports the context manager API directly,
    but some other objects that represent open handles do not. The example
    given in the standard library documentation for :mod:`contextlib` is
    the object returned from :func:`urllib.urlopen()`, and you may have
    legacy classes in your own code as well. If you want to ensure that a
    handle is closed, use :func:`closing()` to create a context manager
    for it.

:class:`file()` クラスはコンテキストマネージャの API を直接サポートしますが、オープンハンドラを表す他のオブジェクトによってはサポートしないものもあります。 :mod:`contextlib` の標準ライブラリドキュメントで説明されている例では :func:`urllib.urlopen()` から返されるオブジェクトがサポートしないものに該当します。同様にあなたのコードにもレガシーなクラスがあるかもしれません。もしハンドラが必ずクローズされることを保証したいなら、クローズのためのコンテキストマネージャを作成するために :func:`closing()` を使用してください。

.. include:: contextlib_closing.py
    :literal:
    :start-after: #end_pymotw_header

..
    The handle is closed whether there is an error in the with block or not.

with ブロック内でエラーが発生するか否かに関わらずハンドラがクローズされます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'contextlib_closing.py'))
.. }}}
.. {{{end}}}

.. seealso::

    `contextlib <http://docs.python.org/library/contextlib.html>`_
        .. The standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント

    :pep:`343`
        .. The ``with`` statement.

        ``with`` 文
