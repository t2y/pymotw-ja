=============
 OrderedDict
=============

An :class:`OrderedDict` is a dictionary subclass that remembers the
order in which its contents are added.  

.. include:: collections_ordereddict_iter.py
   :literal:
   :start-after: #end_pymotw_header

A regular :class:`dict` does not track the insertion order, and
iterating over it produces the values in an arbitrary order.  In an
:class:`OrderedDict`, by contrast, the order the items are inserted is
remembered and used when creating an iterator.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'collections_ordereddict_iter.py'))
.. }}}
.. {{{end}}}

Equality
========

A regular :class:`dict` looks at its contents when testing for
equality.  An :class:`OrderedDict` also considers the order the items
were added.

.. include:: collections_ordereddict_equality.py
   :literal:
   :start-after: #end_pymotw_header

In this case, since the two ordered dictionaries are created from
values in a different order, they are considered to be different.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'collections_ordereddict_equality.py'))
.. }}}
.. {{{end}}}

