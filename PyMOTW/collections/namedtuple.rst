.. _collections-namedtuple:

============
 namedtuple
============

..
    The standard :class:`tuple` uses numerical indexes to access its
    members.

標準の :class:`tuple` は要素にアクセスするために数値インデックスを使用します。

.. include:: collections_tuple.py
   :literal:
   :start-after: #end_pymotw_header

..
    This makes :class:`tuples` convenient containers for simple uses.

:class:`tuples` はシンプルな用途に便利なコンテナになります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'collections_tuple.py'))
.. }}}

::

	$ python collections_tuple.py
	
	Representation: ('Bob', 30, 'male')
	
	Field by index: Jane
	
	Fields by index:
	Bob is a 30 year old male
	Jane is a 29 year old female

.. {{{end}}}

..
    On the other hand, remembering which index should be used for each
    value can lead to errors, especially if the :class:`tuple` has a lot
    of fields and is constructed far from where it is used.  A
    :class:`namedtuple` assigns names, as well as the numerical index, to
    each member.

その一方で、それぞれの値に対応するインデックスがエラーを発生させることを覚えておいてください。特に :class:`tuple` が大量のフィールドを持ち、その値が使用される場所から離れて構築される場合です。数値インデックスと同様に :class:`namedtuple` はそれぞれの値に対応する名前を割り当てます。

..
    Defining
    ========

定義
====

..
    :class:`namedtuple` instances are just as memory efficient as regular
    tuples because they do not have per-instance dictionaries.  Each kind
    of :class:`namedtuple` is represented by its own class, created by
    using the :func:`namedtuple` factory function.  The arguments are the
    name of the new class and a string containing the names of the
    elements.

:class:`namedtuple` インスタンスは、インスタンス毎にディクショナリを持たないので通常のタプルのようにメモリ効率が良いです。 :class:`namedtuple` のそれぞれの種別はその独自クラスで表現され、 :func:`namedtuple` ファクトリ関数を使用して作成されます。その引数は新しいクラスの名前と要素の名前を含む文字列です。

.. include:: collections_namedtuple_person.py
    :literal:
    :start-after: #end_pymotw_header

..
    As the example illustrates, it is possible to access the fields of the
    :class:`namedtuple` by name using dotted notation (``obj.attr``) as
    well as using the positional indexes of standard tuples.

このサンプルは標準タプルの位置インデックスを使用するのと同様に、ドット表記(``obj.attr``)を使用する名前により :class:`namedtuple` フィールドへアクセスできることを説明します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'collections_namedtuple_person.py'))
.. }}}

::

	$ python collections_namedtuple_person.py
	
	Type of Person: <type 'type'>
	
	Representation: Person(name='Bob', age=30, gender='male')
	
	Field by name: Jane
	
	Fields by index:
	Bob is a 30 year old male
	Jane is a 29 year old female

.. {{{end}}}

..
    Invalid Field Names
    ===================

無効なフィールド名
==================

..
    As the field names are parsed, invalid values cause :ref:`ValueError
    <exceptions-ValueError>` exceptions.

フィールド名が解析されるときに無効な値だと :ref:`ValueError <exceptions-ValueError>` 例外が発生します。

.. include:: collections_namedtuple_bad_fields.py
   :literal:
   :start-after: #end_pymotw_header

..
    Names are invalid if they are repeated or conflict with Python
    keywords.

同じ名前を繰り返したときや Python のキーワードの名前は無効です。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'collections_namedtuple_bad_fields.py'))
.. }}}

::

	$ python collections_namedtuple_bad_fields.py
	
	Type names and field names cannot be a keyword: 'class'
	Encountered duplicate field name: 'age'

.. {{{end}}}

..
    In situations where a :class:`namedtuple` is being created based on
    values outside of the control of the programm (such as to represent
    the rows returned by a database query, where the schema is not known
    in advance), set the *rename* option to ``True`` so the fields are
    renamed.

:class:`namedtuple` がプログラム制御外の値に基づいて作成される状況(例えば、前もってスキーマが分からないデータベースのクエリにより返される行を表示する)においては、そのフィールドの名前を変更する *rename* オプションに ``True`` をセットしてください。

.. include:: collections_namedtuple_rename.py
   :literal:
   :start-after: #end_pymotw_header

..
    The field with name ``class`` becomes ``_1`` and the duplicate ``age``
    field is changed to ``_3``.

``class`` という名前のフィールドは ``_1`` になり、重複した ``age`` フィールドは ``_3`` に変更されます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'collections_namedtuple_rename.py'))
.. }}}

::

	$ python collections_namedtuple_rename.py
	
	('name', '_1', 'age', 'gender')
	('name', 'age', 'gender', '_3')

.. {{{end}}}
