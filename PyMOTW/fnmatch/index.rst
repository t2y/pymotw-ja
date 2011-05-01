..
    ==============================================================
    fnmatch -- Compare filenames against Unix-style glob patterns.
    ==============================================================

======================================================
fnmatch -- Unix の glob パターンに対応したファイ名比較
======================================================

.. module:: fnmatch
    :synopsis: Unix の glob パターンに対応したファイ名比較

..
    :Purpose: Handle Unix-style filename comparison with the fnmatch module.
    :Available In: 1.4 and later.

:目的: fnmatch モジュールで Unix のファイル名比較を扱う
:利用できるバージョン: 1.4 以上

..
    The fnmatch module is used to compare filenames against glob-style patterns
    such as used by Unix shells.

fnmatch モジュールは Unix シェルで使用されるような glob パターンに対応したファイル名を比較するために使用されます。

..
    Simple Matching
    ===============

単純なマッチング
================

..
    ``fnmatch()`` compares a single filename against a pattern and returns
    a boolean indicating whether or not they match. The comparison is
    case-sensitive when the operating system uses a case-sensitive
    filesystem.

``fnmatch()`` はあるパターンに対応したファイル名を比較して、マッチしたかどうかを表すブーリアン値を返します。オペレーティングシステムが大文字小文字を区別するファイルシステムな場合、そのマッチングは大文字小文字を区別します。

.. include:: fnmatch_fnmatch.py
    :literal:
    :start-after: #end_pymotw_header

..
    In this example, the pattern matches all files starting with 'fnmatch_' and
    ending in '.py'.

このサンプルのパターンは 'fnmatch\_' で始まり '.py' で終わる全てのファイルにマッチします。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'fnmatch_fnmatch.py'))
.. }}}
.. {{{end}}}

..
    To force a case-sensitive comparison, regardless of the filesystem and
    operating system settings, use ``fnmatchcase()``.

オペレーティングシステムやそのファイルシステムの設定に関係なく、大文字小文字の個別を強制するには ``fnmatchcase()`` を使用してください。

.. include:: fnmatch_fnmatchcase.py
    :literal:
    :start-after: #end_pymotw_header

..
    Since my laptop uses a case-sensitive filesystem, no files match the modified
    pattern.

私のラップトップは大文字小文字を区別するファイルシステムなので、大文字に修正したパターンにマッチするファイルはありません。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'fnmatch_fnmatchcase.py'))
.. }}}
.. {{{end}}}

..
    Filtering
    =========

フィルタリング
==============

..
    To test a sequence of filenames, you can use ``filter()``. It returns
    a list of the names that match the pattern argument.

ファイル名のシーケンスをテストするために ``filter()`` を使用することができます。 ``filter()`` はその pattern の引数にマッチする名前のリストを返します。

.. include:: fnmatch_filter.py
    :literal:
    :start-after: #end_pymotw_header

..
    In this example, ``filter()`` returns the list of names of the example
    source files associated with this post.

このサンプルでは ``filter()`` は本稿で紹介しているサンプルソースファイル名のリストを返します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'fnmatch_filter.py'))
.. }}}
.. {{{end}}}

..
    Translating Patterns
    ====================

変換パターン
============

..
    Internally, fnmatch converts the glob pattern to a regular expression
    and uses the :mod:`re` module to compare the name and pattern. The
    ``translate()`` function is the public API for converting glob patterns to
    regular expressions.

内部的に fnmatch は名前とパターンを比較するために :mod:`re` モジュールで glob パターンから正規表現へ変換します。 ``translate()`` 関数は glob パターンから正規表現へ変換するためのパブリック API です

.. include:: fnmatch_translate.py
    :literal:
    :start-after: #end_pymotw_header

..
    Notice that some of the characters are escaped to make a valid expression.

幾つかの文字は有効な正規表現にするためにエスケープされることに注意してください。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'fnmatch_translate.py'))
.. }}}
.. {{{end}}}

..
    `fnmatch <http://docs.python.org/library/fnmatch.html>`_
        The standard library documentation for this module.
    :mod:`glob`
        The glob module combines :mod:`fnmatch` matching with
        ``os.listdir()`` to produce lists of files and directories
        matching patterns.
    :ref:`article-file-access`
        More modules for working with files.

.. seealso::

    `fnmatch <http://docs.python.org/library/fnmatch.html>`_
        本モジュールの標準ライブラリドキュメント

    :mod:`glob`
        glob モジュールはパターンにマッチするファイルやディレクトリのリストを生成するために ``os.listdir()`` と :mod:`fnmatch` を組み合わせます。

    :ref:`article-file-access`
        ファイルと共に使用するその他のモジュール
