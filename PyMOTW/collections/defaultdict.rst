=============
 defaultdict
=============

..
    The standard dictionary includes the method :func:`setdefault` for
    retrieving a value and establishing a default if the value does not
    exist. By contrast, :class:`defaultdict` lets the caller specify the
    default up front when the container is initialized.

標準のディクショナリは、ある値を取り出すときにその値が存在しなかったらデフォルト値を設定する :func:`setdefault` メソッドを提供します。それと比較して :class:`defaultdict` はそのコンテナが初期化されるときに呼び出し側に前もってデフォルト値を指定させます。

.. include:: collections_defaultdict.py
    :literal:
    :start-after: #end_pymotw_header

..
    This works well as long as it is appropriate for all keys to have the
    same default. It can be especially useful if the default is a type
    used for aggregating or accumulating values, such as a :class:`list`,
    :class:`set`, or even :class:`int`. The standard library documentation
    includes several examples of using :class:`defaultdict` this way.

これは同じデフォルト値を持つように全てのキーに適用するのであればうまく動作します。それはデフォルト値が集約か累積の数値に使用される型、例えば :class:`list`, :class:`set` または :class:`int` であっても、そういった場合に特に便利です。標準ライブラリのドキュメントにこの方法で :class:`defaultdict` を使用するサンプルがあります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'collections_defaultdict.py'))
.. }}}
.. {{{end}}}

.. seealso::

    `defaultdict examples <http://docs.python.org/lib/defaultdict-examples.html>`_
        .. Examples of using defaultdict from the standard library documentation.

        標準ライブラリドキュメントの defaultdict を使用するサンプル

    `James Tauber: Evolution of Default Dictionaries in Python <http://jtauber.com/blog/2008/02/27/evolution_of_default_dictionaries_in_python/>`_
        .. Discussion of how defaultdict relates to other means of initializing dictionaries.

        defaultdict がディクショナリの初期化にどう関連するかの別の視点による説明
