.. _sys-limits:

============================
Memory Management and Limits
============================

:mod:`sys` includes several functions for understanding and controlling memory usage.

Reference Counts
================

Python helps you manage memory with garbage collection.  An object is automatically marked to be collected when its reference count drops to zero.  To examine the reference count of an existing object, use ``getrefcount()``.

.. include:: sys_getrefcount.py
    :literal:
    :start-after: #end_pymotw_header

Notice that the count is actually one higher than expected because there is a temporary reference to the object held by ``getrefcount()`` itself.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sys_getrefcount.py'))
.. }}}
.. {{{end}}}

.. seealso::

    :mod:`gc`
        Control the garbage collector via the functions exposed in :mod:`gc`.

Object Size
===========

Knowing how many references an object has may help you figure out where you have a cycle or a leak in your memory, but it isn't enough to determine what objects are consuming the *most* memory.  For that, you also need to know how big objects are.

.. include:: sys_getsizeof.py
    :literal:
    :start-after: #end_pymotw_header

The size is reported in bytes.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sys_getsizeof.py'))
.. }}}
.. {{{end}}}

The reported size for your own classes does not include the size of the attribute values.

.. include:: sys_getsizeof_object.py
    :literal:
    :start-after: #end_pymotw_header

This can give a false impression of the amount of memory being consumed.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sys_getsizeof_object.py'))
.. }}}
.. {{{end}}}


For a more complete estimate of the space used by a class, you can provide a ``__sizeof__()`` method to compute the value by aggregating the sizes of attributes of an object.

.. include:: sys_getsizeof_custom.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sys_getsizeof_custom.py'))
.. }}}
.. {{{end}}}

Recursion
=========

Allowing infinite recursion in a Python application may introduce a stack overflow in the interpreter itself, leading to a crash. To eliminate this situation, the interpreter lets you control the maximum recursion depth using ``setrecursionlimit()`` and ``getrecursionlimit()``.

.. include:: sys_recursionlimit.py
    :literal:
    :start-after: #end_pymotw_header

Once the recursion limit is reached, the interpreter raises a ``RuntimeError`` exception so your program has an opportunity to handle the situation.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sys_recursionlimit.py'))
.. }}}
.. {{{end}}}


Maximum Values
==============

Along with the runtime configurable values, :mod:`sys` includes variables defining the maximum values for types that vary from system to system.

.. include:: sys_maximums.py
    :literal:
    :start-after: #end_pymotw_header

``maxint`` is the largest representable regular integer.  ``maxsize`` is the maximum size of a list, dictionary, string, or other data structure dictated by the C interpreter's size type.  ``maxunicode`` is the largest integer Unicode point supported by the interpreter as currently configured.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sys_maximums.py'))
.. }}}
.. {{{end}}}

Floating Point Values
=====================

The structure ``float_info`` contains information about the floating point type representation used by the interpreter, based on the underlying system's float implementation.

.. include:: sys_float_info.py
    :literal:
    :start-after: #end_pymotw_header

.. note:: These values depend on the compiler and underlying system, so you may have different results.  These examples were produced on OS X 10.5.8.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sys_float_info.py'))
.. }}}
.. {{{end}}}

.. seealso::

    Your system's ``float.h`` contains more details about these settings.
