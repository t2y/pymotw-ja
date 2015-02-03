=============
 OrderedDict
=============

..
    An :class:`OrderedDict` is a dictionary subclass that remembers the
    order in which its contents are added.  

:class:`OrderedDict` はそのコンテンツが追加された順番を覚えているディクショナリのサブクラスです。

.. include:: collections_ordereddict_iter.py
   :literal:
   :start-after: #end_pymotw_header

..
    A regular :class:`dict` does not track the insertion order, and
    iterating over it produces the values in an arbitrary order.  In an
    :class:`OrderedDict`, by contrast, the order the items are inserted is
    remembered and used when creating an iterator.

通常の :class:`dict` は追加した順番を記録せず、繰り返し処理を行うと任意の順番でその値を生成します。それと比較して :class:`OrderedDict` は追加された要素の順番を覚えていて、イテレータを作成するときに使用されます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'collections_ordereddict_iter.py'))
.. }}}

::

	$ python collections_ordereddict_iter.py
	
	Regular dictionary:
	a A
	c C
	b B
	e E
	d D
	
	OrderedDict:
	a A
	b B
	c C
	d D
	e E

.. {{{end}}}

..
    Equality
    ========

等価判定
========

..
    A regular :class:`dict` looks at its contents when testing for
    equality.  An :class:`OrderedDict` also considers the order the items
    were added.

通常の :class:`dict` は等価であるかを検査するときにそのコンテンツを調べます。 :class:`OrderedDict` は追加された要素の順番も考慮します。

.. include:: collections_ordereddict_equality.py
   :literal:
   :start-after: #end_pymotw_header

..
    In this case, since the two ordered dictionaries are created from
    values in a different order, they are considered to be different.

このケースでは、2つの順序付きディクショナリは違う順番の値から作成されるので、その2つは違うものと見なされます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'collections_ordereddict_equality.py'))
.. }}}

::

	$ python collections_ordereddict_equality.py
	
	dict       : True
	OrderedDict: False

.. {{{end}}}

