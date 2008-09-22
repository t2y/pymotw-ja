================
linecache
================
.. module:: linecache
    :synopsis: Retrieve lines of text from files or imported python modules, holding a cache of the results to make reading many lines from the same file more efficient.

:Module: linecache
:Purpose: Retrieve lines of text from files or imported python modules, holding a cache of the results to make reading many lines from the same file more efficient.
:Python Version: 1.4

Description
===========

The linecache module is used extensively throughout the Python standard
library when dealing with Python source files. The implementation of the cache
simply holds the contents of files, parsed into separate lines, in a
dictionary in memory. The API returns the requested line(s) by indexing into a
list. The time savings is from (repeatedly) reading the file and parsing lines
to find the one desired. This is especially useful when looking for multiple
lines from the same file, such as when producing a traceback for an error
report.

Example
=======

::

    import linecache

    import os
    import tempfile

We will use some text produced by the Lorem Ipsum generator as sample input:

::

    lorem = '''Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
    Vivamus eget elit. In posuere mi non risus. Mauris id quam posuere

    lectus sollicitudin varius. Praesent at mi. Nunc eu velit. Sed augue
    massa, fermentum id, nonummy a, nonummy sit amet, ligula. Curabitur
    eros pede, egestas at, ultricies ac, pellentesque eu, tellus. 

    Sed sed odio sed mi luctus mollis. Integer et nulla ac augue convallis
    accumsan. Ut felis. Donec lectus sapien, elementum nec, condimentum ac,
    interdum non, tellus. Aenean viverra, mauris vehicula semper porttitor,
    ipsum odio consectetuer lorem, ac imperdiet eros odio a sapien. Nulla
    mauris tellus, aliquam non, egestas a, nonummy et, erat. Vivamus

    sagittis porttitor eros.'''

    # Create a temporary text file with some text in it
    fd, temp_file_name = tempfile.mkstemp()

    os.close(fd)
    f = open(temp_file_name, 'wt')

    try:
    f.write(lorem)
    finally:
    f.close()


And now that we have a temporary file to work with, let's get on to the
interesting bits. Reading the 5th line from the file is a simple one-liner.
Notice that the line numbers in the linecache module start with 1, but if we
split the string ourselves we start indexing the array from 0. We also need to
strip the trailing newline from the value returned from the cache.

::

    # Pick out the same line from source and cache.
    # (Notice that linecache counts from 1)
    print 'SOURCE: ', lorem.split('\n')[4]
    print 'CACHE : ', linecache.getline(temp_file_name, 5).rstrip()

Next let's see what happens if the line we want is empty:

::

    # Blank lines include the newline
    print '\nBLANK : "%s"' % linecache.getline(temp_file_name, 6)

If the requested line number falls out of the range of valid lines in the
file, linecache returns an empty string. 

::

    # The cache always returns a string, and uses
    # an empty string to indicate a line which does
    # not exist.
    not_there = linecache.getline(temp_file_name, 500)
    print '\nNOT THERE: "%s" includes %d characters' %  (not_there, len(not_there))


The module never raises an exception, even if the file does not exist::

    # Errors are even hidden if linecache cannot find the file
    no_such_file = linecache.getline('this_file_does_not_exist.txt', 1)
    print '\nNO FILE: ', no_such_file

Since the linecache module is used so heavily when producing tracebacks, one
of the key features is the ability to find Python source modules in sys.path
by specifying the base name of the module. The cache population code in
linecache searches sys.path for the module if it cannot find the file
directly.

::

    # Look for the linecache module, using
    # the built in sys.path search.
    module_line = linecache.getline('linecache.py', 3)
    print '\nMODULE : ', module_line

Example Output:

::

    SOURCE:  eros pede, egestas at, ultricies ac, pellentesque eu, tellus.
    CACHE :  eros pede, egestas at, ultricies ac, pellentesque eu, tellus.

    BLANK : "
    "

    NOT THERE: "" includes 0 characters

    NO FILE: 

    MODULE :  This is intended to read lines from modules imported -- hence if a filename

