##############################################################
shelve -- Persistent storage of arbitrary Python objects
##############################################################

.. module:: shelve
    :synopsis: The shelve module implements persistent storage for arbitrary Python objects which can be pickled, using a dictionary-like API.

:Module: shelve
:Purpose: The shelve module implements persistent storage for arbitrary Python objects which can be pickled, using a dictionary-like API.
:Python Version: 1.4

The shelve module can be used as a simple persistent storage option for Python
objects when a relational database is overkill. The shelf is accessed by keys,
just as with a dictionary. The values are pickled and written to a database
created and managed by :mod:`anydbm`.

====================
Creating a new Shelf
====================

The simplest way to use shelve is via the DbfilenameShelf class. It uses
anydbm to store the data. You can use the class directly, or simply call
shelve.open():

::

    import shelve

    s = shelve.open('test_shelf.db')
    try:
        s['key1'] = { 'int': 10, 'float':9.5, 'string':'Sample data' }
    finally:
        s.close()

To access the data again, open the shelf and use it like a dictionary:

::

    s = shelve.open('test_shelf.db')
    try:
        existing = s['key1']
    finally:
        s.close()

    print existing

If you run both sample scripts, you should see:

::

    $ python shelve_create.py
    $ python shelve_existing.py 
    {'int': 10, 'float': 9.5, 'string': 'Sample data'}

The dbm module does not support multiple applications writing to the same
database at the same time. If you know your client will not be modifying the
shelf, you can tell shelve to open the database read-only.

::

    s = shelve.open('test_shelf.db', flag='r')
    try:
        existing = s['key1']
    finally:
        s.close()

    print existing

If your program tries to modify the database while it is opened read-only, an
access error exception is generated. The exception type depends on the
database module selected by anydbm when the database was created.

==========
Write-back
==========

Shelves do not track modifications to volatile objects, by default. That means
if you change the contents of an item stored in the shelf, you must update the
shelf explicitly by storing the item again.

::

    s = shelve.open('test_shelf.db')
    try:
        print s['key1']
        s['key1']['new_value'] = 'this was not here before'
    finally:
        s.close()

    s = shelve.open('test_shelf.db', writeback=True)
    try:
        print s['key1']
    finally:
        s.close()

In this example, the dictionary at 'key1' is not stored again, so when the
shelf is re-opened, the changes have not been preserved.

::

    $ python shelve_create.py
    $ python shelve_withoutwriteback.py
    {'int': 10, 'float': 9.5, 'string': 'Sample data'}
    {'int': 10, 'float': 9.5, 'string': 'Sample data'}

To automatically catch changes to volatile objects stored in the shelf, open
the shelf with writeback enabled. The writeback flag causes the shelf to
remember all of the objects retrieved from the database using an in-memory
cache. Each cache object is also written back to the database when the shelf
is closed. 

::

    s = shelve.open('test_shelf.db', writeback=True)
    try:
        print s['key1']
        s['key1']['new_value'] = 'this was not here before'
        print s['key1']
    finally:
        s.close()

    s = shelve.open('test_shelf.db', writeback=True)
    try:
        print s['key1']
    finally:
        s.close()


Although it reduces the chance of programmer error, and can make object
persistence more transparent, using writeback mode may not be desirable in
every situation. The cache consumes extra memory while the shelf is open, and
pausing to write every cached object back to the database when it is closed
can take extra time. Since there is no way to tell if the cached objects have
been modified, they are all written back. If your application reads data more
than it writes, writeback will add more overhead than you might want.

::

    $ python shelve_create.py
    $ python shelve_writeback.py
    {'int': 10, 'float': 9.5, 'string': 'Sample data'}
    {'int': 10, 'new_value': 'this was not here before', 'float': 9.5, 'string': 'Sample data'}
    {'int': 10, 'new_value': 'this was not here before', 'float': 9.5, 'string': 'Sample data'}


====================
Specific Shelf Types
====================

The examples above all use the default shelf implementation. Using
shelve.open() instead of one of the shelf implementations directly is a common
usage pattern, especially if you do not care what type of database is used to
store the data. There are times, however, when you do care. In those
situations, you may want to use DbfilenameShelf or BsdDbShelf directly, or
even subclass Shelf for a custom solution.

==========
References
==========

See also :mod:`anydbm`

Standard library documentation: `shelve <http://docs.python.org/lib/module-shelve.html>`_

`feedcache <http://www.doughellmann.com/projects/feedcache/>` uses shelve as a default storage option.

`shove <http://pypi.python.org/pypi/shove/>` implements a similar API with more backend formats.