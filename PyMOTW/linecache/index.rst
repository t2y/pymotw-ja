========================================
linecache -- Read text files efficiently
========================================

.. module:: linecache
    :synopsis: Retrieve lines of text from files or imported python modules, holding a cache of the results to make reading many lines from the same file more efficient.

:Purpose: Retrieve lines of text from files or imported python modules, holding a cache of the results to make reading many lines from the same file more efficient.
:Python Version: 1.4

The linecache module is used extensively throughout the Python standard
library when dealing with Python source files. The implementation of the cache
simply holds the contents of files, parsed into separate lines, in a
dictionary in memory. The API returns the requested line(s) by indexing into a
list. The time savings is from (repeatedly) reading the file and parsing lines
to find the one desired. This is especially useful when looking for multiple
lines from the same file, such as when producing a traceback for an error
report.

Test Data
=========

We will use some text produced by the Lorem Ipsum generator as sample input.

.. include:: linecache_data.py
    :literal:
    :start-after: #end_pymotw_header

Reading Specific Lines
======================

Reading the 5th line from the file is a simple one-liner.
Notice that the line numbers in the linecache module start with 1, but if we
split the string ourselves we start indexing the array from 0. We also need to
strip the trailing newline from the value returned from the cache.

.. include:: linecache_getline.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'linecache_getline.py'))
.. }}}
.. {{{end}}}

Handling Blank Lines
====================

Next let's see what happens if the line we want is empty:

.. include:: linecache_empty_line.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'linecache_empty_line.py'))
.. }}}
.. {{{end}}}

Error Handling
==============

If the requested line number falls out of the range of valid lines in the
file, linecache returns an empty string. 

.. include:: linecache_out_of_range.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'linecache_out_of_range.py'))
.. }}}
.. {{{end}}}


The module never raises an exception, even if the file does not exist:

.. include:: linecache_missing_file.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'linecache_missing_file.py'))
.. }}}
.. {{{end}}}

Python Source
=============

Since the linecache module is used so heavily when producing tracebacks, one
of the key features is the ability to find Python source modules in sys.path
by specifying the base name of the module. The cache population code in
linecache searches sys.path for the module if it cannot find the file
directly.

.. include:: linecache_path_search.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'linecache_path_search.py'))
.. }}}
.. {{{end}}}
    
.. seealso::

    `linecache <http://docs.python.org/library/linecache.html>`_
        The standard library documentation for this module.

    http://www.ipsum.com/
        Lorem Ipsum generator.
