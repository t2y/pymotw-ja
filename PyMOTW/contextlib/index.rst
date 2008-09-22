=================
contextlib
=================
.. module:: contextlib
    :synopsis: Utilities for creating and working with context managers.

:Module: contextlib
:Purpose: Utilities for creating and working with context managers.
:Python Version: 2.5
:Abstract:

    The contextlib module contains utilities for working with context managers
    and the with statement.

Description
===========

Context managers are tied to the with statement. Since with is officially part
of Python 2.6, you have to import it from __future__ before using contextlib
in Python 2.5.

From Generator to Context Manager
=================================

Creating context managers the traditional way, by writing a class with
__enter__() and __exit__() methods, is not difficult. But sometimes it is more
overhead than you need just to manage a trivial bit of context. In those sorts
of situations, you can use the contextmanager() decorator to convert a
generator function into a context manager.

The generator should initialize the context, yield exactly one time, then
clean up the context. The value yielded, if any, is bound to the variable in
the as clause of the with statement. Exceptions from within the with block are
re-raised inside the generator, so you can handle them there.

::

    from __future__ import with_statement

    import contextlib

    @contextlib.contextmanager
    def make_context():
        print '  entering'
        try:
            yield {}
        except RuntimeError, err:
            print '  ERROR:', err
        finally:
            print '  exiting'

    print 'Normal:'
    with make_context() as value:
        print '  inside with statement:', value

    print
    print 'Handled error:'
    with make_context() as value:
        raise RuntimeError('showing example of handling an error')

    print
    print 'Unhandled error:'
    with make_context() as value:
        raise ValueError('this exception is not handled')

::

    $ python contextlib_contextmanager.py
    Normal:
      entering
      inside with statement: {}
      exiting

    Handled error:
      entering
      ERROR: showing example of handling an error
      exiting

    Unhandled error:
      entering
      exiting
    Traceback (most recent call last):
      File "/Users/dhellmann/Documents/PyMOTW/in_progress/contextlib/contextlib_contextmanager.py", line 38, in <module>
        raise ValueError('this exception is not handled')
    ValueError: this exception is not handled


Nesting Contexts
================

At times it is necessary to manage multiple contexts simultaneously (such as
when copying data between input and output file handles, for example). It is,
of course, possible to nest with statements one inside another. If the outer
contexts do not need their own separate block, though, this adds to the
indention level without giving any real benefit. By using contextlib.nested(),
you can nest the contexts and use a single with statement.

::

    from __future__ import with_statement

    import contextlib

    @contextlib.contextmanager
    def make_context(name):
        print 'entering:', name
        yield name
        print 'exiting :', name

    with contextlib.nested(make_context('A'), make_context('B'), make_context('C')) as (A, B, C):
        print 'inside with statement:', A, B, C

Notice that the contexts are exited in the reverse order in which they are
entered.

::

    $ python contextlib_nested.py
    entering: A
    entering: B
    entering: C
    inside with statement: A B C
    exiting : C
    exiting : B
    exiting : A


Closing Open Handles
====================

The file() class supports the context manager API directly, but some other
objects that represent open handles do not. The example given in the standard
library documentation for contextlib is the object returned from
urllib.urlopen(), and you may have legacy classes in your own code as well. If
you want to ensure that a handle is closed, use contextlib.closing() to create
a context manager for it.

::

    from __future__ import with_statement

    import contextlib

    class Door(object):
        def __init__(self):
            print '  __init__()'
        def close(self):
            print '  close()'

    print 'Normal Example:'
    with contextlib.closing(Door()) as door:
        print '  inside with statement'

    print
    print 'Error handling example:'
    try:
        with contextlib.closing(Door()) as door:
            print '  raising from inside with statement'
            raise RuntimeError('error message')
    except Exception, err:
        print '  Had an error:', err

The handle is closed whether there is an error in the with block or not.

::

    $ python contextlib_closing.py
    Normal Example:
      __init__()
      inside with statement
      close()

    Error handling example:
      __init__()
      raising from inside with statement
      close()
      Had an error: error message
