..
    ============================
    abc -- Abstract Base Classes
    ============================

=====================
abc -- 抽象基底クラス
=====================

..
    :synopsis: Abstract Base Classes

.. module:: abc
    :synopsis: 抽象基底クラス

..
    :Purpose: Define and use abstract base classes for API checks in your code.
    :Python Version: 2.6

:目的: コードをチェックする API のために抽象基底クラスの使用、定義する
:Python バージョン: 2.6

..
    Why use Abstract Base Classes?
    ==============================

なぜ抽象基底クラスを使用するのか？
==================================

..
    Abstract base classes are a form of interface checking more strict
    than individual ``hasattr()`` checks for particular methods.  By
    defining an abstract base class, you can define a common API for a set
    of subclasses.  This capability is especially useful in situations
    where a third-party is going to provide implementations, such as with
    plugins to an application, but can also aid you when working on a
    large team or with a large code-base where keeping all classes in your
    head at the same time is difficult or not possible.

抽象基底クラス(ABC)は特定メソッドをチェックする個別の ``hasattr()`` よりも厳密なチェックのためのインタフェースです。抽象基底クラスを定義することでサブクラスセットのための共通 API を定義することができます。この機能はアプリケーションに対するプラグインのような、サードパーティが実装を提供する状況でかなり便利です。さらに、同時に頭の中で全クラスを把握することが難しい、もしくは不可能な、大規模なチーム又はコードベースで開発することもできます。

..
    How ABCs Work
    =============

どのように ABC を用いて開発するか
=================================

..
    :mod:`abc` works by marking methods of the base class as abstract, and
    then registering concrete classes as implementations of the abstract
    base.  If your code requires a particular API, you can use
    ``issubclass()`` or ``isinstance()`` to check an object against the
    abstract class.

:mod:`abc` は抽象的な基底クラスのメソッドをマークしてから、抽象基底クラスの実装として具象クラスを登録します。コードが特定 API を要求するなら、抽象クラスに対するオブジェクトをチェックするために ``issubclass()`` か ``isinstance()`` を使用することができます。

..
    Let's start by defining an abstract base class to represent the API of
    a set of plugins for saving and loading data.

データの保存や読み込みのためのプラグインセットの API を表すために抽象基底クラスを定義してみましょう。

.. include:: abc_base.py
    :literal:
    :start-after: #end_pymotw_header

..
    Registering a Concrete Class
    ============================

具象クラスを登録する
====================

..
    There are two ways to indicate that a concrete class implements an
    abstract: register the class with the abc or subclass directly from
    the abc.

そのクラスを ABC で登録するか、ABC から直接サブクラス化するかといった抽象的なモノを実装する具象クラスを指し示す方法が2つあります。

.. include:: abc_register.py
    :literal:
    :start-after: #end_pymotw_header

..
    In this example the ``RegisteredImplementation`` is not derived from
    ``PluginBase``, but is registered as implementing the ``PluginBase``
    API.

この例の ``RegisteredImplementation`` は ``PluginBase`` から派生しませんが ``PluginBase`` API の実装として登録されます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'abc_register.py'))
.. }}}
.. {{{end}}}

..
    Implementation Through Subclassing
    ==================================

サブクラス化による実装
======================

..
    By subclassing directly from the base, we can avoid the need to
    register the class explicitly.

その基底クラスから直接サブクラス化することで明示的にその具象クラスを登録する必要はありません。

.. include:: abc_subclass.py
    :literal:
    :start-after: #end_pymotw_header

..
    In this case the normal Python class management is used to recognize
    ``SubclassImplementation`` as implementing the abstract ``PluginBase``.

このケースでは、通常の Python のクラス管理が抽象クラス ``PluginBase`` を実装する ``SubclassImplementation`` を認識します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'abc_subclass.py'))
.. }}}
.. {{{end}}}

..
    A side-effect of using direct subclassing is it is possible to find
    all of the implementations of your plugin by asking the base class for
    the list of known classes derived from it (this is not an abc feature,
    all classes can do this).

直接サブクラス化することの副作用は、抽象クラスから派生したクラスリストの基底クラスを調べることでプラグインの全ての実装を見つけられることです(これは ABC の機能ではなく、全てのクラスがこのように動作します)。

.. include:: abc_find_subclasses.py
    :literal:
    :start-after: #end_pymotw_header

..
    Notice that even though ``abc_register`` is imported,
    ``RegisteredImplementation`` is not among the list of subclasses
    because it is not actually derived from the base.

``abc_register`` がインポートされたとしても、実際にはその基底クラスから派生していないので ``RegisteredImplementation`` がサブクラスのリストに存在しないことに気付いてください。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'abc_find_subclasses.py'))
.. }}}
.. {{{end}}}

..
    Dr. André Roberge `has described
    <http://us.pycon.org/2009/conference/schedule/event/47/>`_ using this
    capability to discover plugins by importing all of the modules in a
    directory dynamically and then looking at the subclass list to find
    the implementation classes.

Dr. André Roberge は動的にディレクトリ内の全モジュールをインポートしてから実装クラスを見つけるためにサブクラスリストを探することで、プラグインを発見するためにこの機能を使用することを `説明しました <http://us.pycon.org/2009/conference/schedule/event/47/>`_ 。

..
    Incomplete Implementations
    --------------------------

不完全な実装
------------

..
    Another benefit of subclassing directly from your abstract base class
    is that the subclass cannot be instantiated unless it fully implements
    the abstract portion of the API.  This can keep half-baked
    implementations from triggering unexpected errors at runtime.

抽象基底クラスから直接サブクラス化することの他の利点は API の抽象的な部分を完全に実装しない限りサブクラスはインスタンス化されないということです。これは中途半端な実装で実行時に予測されないエラーを発生させないようにします。

.. include:: abc_incomplete.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'abc_incomplete.py', ignore_error=True))
.. }}}
.. {{{end}}}

..
    Concrete Methods in ABCs
    ========================

ABC の具象メソッド
==================

..
    Although a concrete class must provide an implementation of an
    abstract methods, the abstract base class can also provide an
    implementation that can be invoked via ``super()``.  This lets you
    re-use common logic by placing it in the base class, but force
    subclasses to provide an overriding method with (potentially) custom
    logic.

具象クラスは抽象メソッドの実装を提供しなければならないですが、抽象基底クラスが ``super()`` を通して実行される実装を提供することもできます。これは基底クラスに抽象メソッドの実装を配置することで共通ロジックを再利用させますが、(潜在的に)カスタムロジックでオーバーライドされたメソッドを提供することをサブクラスに強制します。

.. include:: abc_concrete_method.py
    :literal:
    :start-after: #end_pymotw_header

..
    Since ``ABCWithConcreteImplementation`` is an abstract base class, it
    isn't possible to instantiate it to use it directly.  Subclasses
    *must* provide an override for ``retrieve_values()``, and in this case
    the concrete class messages the data before returning it at all.

``ABCWithConcreteImplementation`` は抽象基底クラスなので、そのクラスを直接インスタンス化することはできません。サブクラスは ``retrieve_values()`` をオーバーライドして *提供しなければなりません* 。そして、このケースでは具象クラスが入力データを返す前にメッセージを表示します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'abc_concrete_method.py'))
.. }}}
.. {{{end}}}

.. _abc-abstract-properties:

..
    Abstract Properties
    ===================

抽象プロパティ
==============

..
    If your API specification includes attributes in addition to methods,
    you can require the attributes in concrete classes by defining them
    with ``@abstractproperty``.

API 仕様がメソッドに加えて属性を含むなら ``@abstractproperty`` で、そのようなメソッドを定義することで具象クラスに属性を要求することができます。

.. include:: abc_abstractproperty.py
    :literal:
    :start-after: #end_pymotw_header

..
    The ``Base`` class in the example cannot be instantiated because it
    has only an abstract version of the property getter method.

このサンプルの ``Base`` クラスは抽象プロパティのゲッタメソッドしか持たないのでインスタンス化できません。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'abc_abstractproperty.py'))
.. }}}
.. {{{end}}}

..
    You can also define abstract read/write properties.

抽象的な read/write プロパティを定義することもできます。

.. include:: abc_abstractproperty_rw.py
    :literal:
    :start-after: #end_pymotw_header

..
    Notice that the concrete property must be defined the same way as the
    abstract property.  Trying to override a read/write property in
    ``PartialImplementation`` with one that is read-only does not work.

具象プロパティは抽象プロパティと同じ方法で定義されなければならないことに注意してください。 ``PartialImplementation`` の read/write プロパティを 'Read-only' でオーバーライドしようとしても動作しません。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'abc_abstractproperty_rw.py'))
.. }}}
.. {{{end}}}

..
    To use the decorator syntax does with read/write abstract properties,
    the methods to get and set the value should be named the same.

抽象的な read/write プロパティを扱うデコレータ構文を使用するために value を get/set するメソッドは同じ名前にすべきです。

.. include:: abc_abstractproperty_rw_deco.py
    :literal:
    :start-after: #end_pymotw_header

..
    Notice that both methods in the ``Base`` and ``Implementation``
    classes are named ``value()``, although they have different
    signatures.

``Base`` と ``Implementation`` クラスの2つのメソッドは引数は違いますが ``value()`` という名前で定義していることに注意してください。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'abc_abstractproperty_rw_deco.py'))
.. }}}
.. {{{end}}}

.. _abc-collection-types:

..
    Collection Types
    ================

コレクション型
==============

..
    The :mod:`collections` module defines several abstract base classes
    related to container (and containable) types.

:mod:`collections` モジュールはコンテナ(とコンテナにできる)型に関連する複数の抽象基底クラスを定義します。

- Container
- Sized

..
    Iterator and Sequence classes:

イテレータとシーケンスクラス:

- Iterable
- Iterator
- Sequence
- MutableSequence

..
    Unique values:

ユニークな値:

- Hashable
- Set
- MutableSet

..
    Mappings:

マッピング:

- Mapping
- MutableMapping
- MappingView
- KeysView
- ItemsView
- ValuesView

..
    Miscelaneous:

その他:

- Callable

..
    In addition to serving as detailed real-world examples of abstract
    base classes, Python's built-in types are automatically registered to
    these classes when you import :mod:`collections`. This means you can
    safely use ``isinstance()`` to check parameters in your code to ensure
    that they support the API you need.  The base classes can also be used
    to define your own collection types, since many of them provide
    concrete implementations of the internals and only need a few methods
    overridden.  Refer to the standard library docs for collections for
    more details.

抽象基底クラスの現実世界の詳細なサンプルとして提供することに加えて Python のビルトイン型は :mod:`collections` をインポートするとき、これらのクラスに対して自動的に登録されます。これは必要とする API をこれらのクラスがサポートすることを保証して、コードのパラメータをチェックするために ``isinstance()`` を安全に使用できることを意味します。さらに、これらのクラスの多くは内部の具象的な実装を提供してオーバーライドされた数個のメソッドのみを必要とするので、その基底クラスは独自のコレクション型を定義するために使用されます。詳細はコレクションモジュールの標準ライブラリドキュメントを参照してください。

.. seealso::

    `abc <http://docs.python.org/library/abc.html>`_
        .. The standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント

    :pep:`3119`
        .. Introducing Abstract Base Classes

        抽象基底クラスの紹介
    
    :mod:`collections`
        .. The collections module includes abstract base classes for several collection types.

        コレクション型のために抽象基底クラスを含むコレクションモジュール

    `collections <http://docs.python.org/library/collections.html>`_
        .. The standard library documentation for collections.

        コレクションモジュールの標準ライブラリドキュメント

    :pep:`3141`
        .. A Type Hierarchy for Numbers

        数値のデータ型の階層構造

    `Wikipedia: Strategy Pattern <http://en.wikipedia.org/wiki/Strategy_pattern>`_
        .. Description and examples of the strategy pattern.

        ストラテジパターンの例と説明

    `Plugins and monkeypatching <http://us.pycon.org/2009/conference/schedule/event/47/>`_
        .. PyCon 2009 presentation by Dr. André Roberge

        Dr. André Roberge による PyCon 2009 のプレゼンテーション
