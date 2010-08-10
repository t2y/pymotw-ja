..
    ============================================
    urlparse -- Split URL into component pieces.
    ============================================

======================================
urlparse -- URL を部分文字列に分割する
======================================

..
    :synopsis: Split URL into component pieces.

.. module:: urlparse
    :synopsis: URL を部分文字列に分割する

..
    :Purpose: Split URL into component pieces.
    :Python Version: since 1.4

:目的: URL を部分文字列に分割する
:Python バージョン: 1.4 以降

..
    The :mod:`urlparse` module provides functions for breaking URLs down
    into their component parts, as defined by the relevant RFCs.

:mod:`urlparse` モジュールは関連する RFC で定義されているように URL を部分文字列に分解するための機能を提供します。

..
    Parsing
    =======

解析する
========

..
    The return value from the :func:`urlparse()` function is an object
    which acts like a tuple with 6 elements.

:func:`urlparse()` 関数は6つの要素を持つタプルのように動作するオブジェクトを返します。

.. include:: urlparse_urlparse.py
    :literal:
    :start-after: #end_pymotw_header

..
    The parts of the URL available through the tuple interface are the scheme,
    network location, path, parameters, query, and fragment.

タプルのインタフェースを通して利用できる URL の部分文字列はスキーマ(scheme), ネットワークロケーション(netloc), パス(path), パラメータ(params), クエリ(query) と フラグメント(fragment) です。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'urlparse_urlparse.py'))
.. }}}
.. {{{end}}}

..
    Although the return value acts like a tuple, it is really based on a
    :ref:`namedtuple <collections-namedtuple>`, a subclass of tuple that
    supports accessing the parts of the URL via named attributes instead
    of indexes. That's especially useful if, like me, you can't remember
    the index order. In addition to being easier to use for the
    programmer, the attribute API also offers access to several values not
    available in the tuple API.

返される値はタプルのように動作しますが、実際は :ref:`namedtuple <collections-namedtuple>` に基づいています。タプルのサブクラスはインデックスの代わりに属性名を通して URL の部分文字列へアクセスすることをサポートします。プログラマが簡単に使用できるのに加えて、その属性 API はタプル API では利用できない複数の値へのアクセスも提供します。

.. include:: urlparse_urlparseattrs.py
    :literal:
    :start-after: #end_pymotw_header

..
    The *username* and *password* are available when present in the input
    URL and ``None`` when not. The *hostname* is the same value as
    *netloc*, in all lower case.  And the *port* is converted to an
    integer when present and ``None`` when not.

*username* と *password* は入力 URL に含まれるときに利用できて、含まれないときは ``None`` です。 *hostname* は *netloc* と同じ値で全て小文字です。 *port* は存在するときに整数値へ変換され、存在しないときは ``None`` です。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'urlparse_urlparseattrs.py'))
.. }}}
.. {{{end}}}

..
    The :func:`urlsplit()` function is an alternative to
    :func:`urlparse()`. It behaves a little different, because it does not
    split the parameters from the URL. This is useful for URLs following
    :rfc:`2396`, which supports parameters for each segment of the path.

:func:`urlsplit()` 関数は :func:`urlparse()` に対する代替方法です。その動作は URL からパラメータを分割しないので :func:`urlparse()` と少し違っています。これは :rfc:`2396` に従う、そのパスの各セグメントのパラメータをサポートする URL に便利です。

.. include:: urlparse_urlsplit.py
    :literal:
    :start-after: #end_pymotw_header

..
    Since the parameters are not split out, the tuple API will show 5
    elements instead of 6, and there is no *params* attribute.

パラメータが分割されないのでタプル API は *params* 属性のない、6つではなく5つの要素を返します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'urlparse_urlsplit.py'))
.. }}}
.. {{{end}}}

..
    To simply strip the fragment identifier from a URL, as you might need
    to do to find a base page name from a URL, use :func:`urldefrag()`.

URL からフラグメントの識別子を簡単に取り除くために、また URL からベースページの名前を取得するために :func:`urldefrag()` を使用する必要があるでしょう。

.. include:: urlparse_urldefrag.py
    :literal:
    :start-after: #end_pymotw_header

..
    The return value is a tuple containing the base URL and the fragment.

ベース URL とそのフラグメントを含むタプルが返されます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'urlparse_urldefrag.py'))
.. }}}
.. {{{end}}}

..
    Unparsing
    =========

再構築
======

..
    There are several ways to assemble a split URL back together into a
    single string. The parsed URL object has a :func:`geturl()` method.

分割された URL から1つの文字列へ戻す複数の方法があります。解析された URL オブジェクトは :func:`geturl()` メソッドを持ちます。

.. include:: urlparse_geturl.py
    :literal:
    :start-after: #end_pymotw_header

..
    :func:`geturl()` only works on the object returned by
    :func:`urlparse()` or :func:`urlsplit()`.

:func:`geturl()` は :func:`urlparse()` 又は :func:`urlsplit()` によって返されるオブジェクトでのみ動作します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'urlparse_geturl.py'))
.. }}}
.. {{{end}}}

..
    If you have a regular tuple of values, you can use
    :func:`urlunparse()` to combine them into a URL.

もし普通のタプルで取得したいなら、URL にそれらを結合するために :func:`urlunparse()` を使用できます。

.. include:: urlparse_urlunparse.py
    :literal:
    :start-after: #end_pymotw_header

..
    While the :class:`ParseResult` returned by :func:`urlparse()` can be
    used as a tuple, in this example I explicitly create a new tuple to
    show that :func:`urlunparse()` works with normal tuples, too.

:func:`urlparse()` が返す :class:`ParseResult` クラスはタプルのようには使用できません。この例では :func:`urlunparse()` が普通のタプルでも動作することを表すために明示的に新たなタプルを作成します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'urlparse_urlunparse.py'))
.. }}}
.. {{{end}}}

..
    If the input URL included superfluous parts, those may be dropped from the
    unparsed version of the URL.

入力 URL が余分な文字列を含むなら URL を再構築した文字列からその文字列が欠落します。

.. include:: urlparse_urlunparseextra.py
    :literal:
    :start-after: #end_pymotw_header

..
    In this case, the *parameters*, *query*, and *fragment* are all
    missing in the original URL. The new URL does not look the same as the
    original, but is equivalent according to the standard.

このケースでは *parameters*, *query* と *fragment* がオリジナルの URL から全て欠落します。新たな URL はオリジナルの URL と同じではありませんが、標準によると等価です。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'urlparse_urlunparseextra.py'))
.. }}}
.. {{{end}}}

..
    Joining
    =======

結合
====

..
    In addition to parsing URLs, :mod:`urlparse` includes
    :func:`urljoin()` for constructing absolute URLs from relative
    fragments.

URL を解析することに加えて :mod:`urlparse` には関連するフラグメントから相対 URL を構築する :func:`urljoin()` があります。

.. include:: urlparse_urljoin.py
    :literal:
    :start-after: #end_pymotw_header

..
    In the example, the relative portion of the path (``"../"``) is taken
    into account when the second URL is computed.

この例では、そのパスの相対部分(``"../"``)は 2番目の URL が算出されるときに考慮されます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'urlparse_urljoin.py'))
.. }}}
.. {{{end}}}

..
    `urlparse <http://docs.python.org/lib/module-urlparse.html>`_
        Standard library documentation for this module.
    :mod:`urllib`
        Retrieve the contents of a resource identified by a URL.
    :mod:`urllib2`
        Alternative API for accessing remote URLs.

.. seealso::

    `urlparse <http://docs.python.org/lib/module-urlparse.html>`_
        本モジュールの標準ライブラリドキュメント

    :mod:`urllib`
        URL で識別されるリソースからコンテンツを取り出す

    :mod:`urllib2`
        リモート URL アクセスの代替 API
