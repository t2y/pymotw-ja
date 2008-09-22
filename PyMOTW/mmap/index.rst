===========
mmap
===========
.. module:: mmap
    :synopsis: Memory-map files instead of reading the contents directly.

:Module: mmap
:Purpose: Memory-map files instead of reading the contents directly.
:Python Version: 2.1 and later
:Abstract:

    Map files directly to memory using mmap.

Description
===========

Use the mmap() function to create a memory-mapped file. There are differences
in the arguments and behaviors for mmap() between Unix and Windows, which are
not discussed below. For more details, refer to the library documentation.

The first argument is a fileno, either from the fileno() method of a file
object or from os.open(). Since you have opened the file before calling
mmap(), you are responsible for closing it.

The second argument to mmap() is a size in bytes for the portion of the file
to map. If the value is 0, the entire file is mapped. You cannot create a
zero-length mapping under Windows. If the size is larger than the current size
of the file, the file is extended.

An optional keyword argument, access, is supported by both platforms. Use
ACCESS_READ for read-only access, ACCESS_WRITE for write-through (assignments
to the memory go directly to the file), or ACCESS_COPY for copy-on-write
(assignments to memory are not written to the file).

File and String API
===================

Memory-mapped files can be treated as mutable strings or file-like objects,
depending on your need. A mapped file supports the expected file API methods,
such as close(), flush(), read(), readline(), seek(), tell(), and write(). It
also supports the string API, with features such as slicing and methods like
find().

Sample Data
===========

All of the examples use the text file lorem.txt, containing a bit of Lorem
Ipsum. For reference, the text of the file is::

    Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Donec
    egestas, enim et consectetuer ullamcorper, lectus ligula rutrum leo, a
    elementum elit tortor eu quam. Duis tincidunt nisi ut ante. Nulla
    facilisi. Sed tristique eros eu libero. Pellentesque vel arcu. Vivamus
    purus orci, iaculis ac, suscipit sit amet, pulvinar eu,
    lacus. Praesent placerat tortor sed nisl. Nunc blandit diam egestas
    dui. Pellentesque habitant morbi tristique senectus et netus et
    malesuada fames ac turpis egestas. Aliquam viverra fringilla
    leo. Nulla feugiat augue eleifend nulla. Vivamus mauris. Vivamus sed
    mauris in nibh placerat egestas. Suspendisse potenti. Mauris massa. Ut
    eget velit auctor tortor blandit sollicitudin. Suspendisse imperdiet
    justo.

Reading
=======

To map a file for read-only access, make sure to pass access=mmap.ACCESS_READ:

::

    import mmap

    f = open('lorem.txt', 'r')
    try:
        m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
        try:
            print 'First 10 bytes via read :', m.read(10)
            print 'First 10 bytes via slice:', m[:10]
            print '2nd   10 bytes via read :', m.read(10)
        finally:
            m.close()
    finally:
        f.close()

In this example, even though the call to read() advances the file pointer, the
slice operation still gives us the same first 10 bytes because the file
pointer is reset. The file pointer tracks the last access, so after using the
slice operation to give us the first 10 bytes for the second time, calling
read gives the next 10 bytes in the file.

::

    $ python mmap_read.py
    First 10 bytes via read : Lorem ipsu
    First 10 bytes via slice: Lorem ipsu
    2nd   10 bytes via read : m dolor si

Writing
=======

If you need to write to the memory mapped file, start by opening it for
reading and appending (not with 'w', but 'r+') before mapping it. Then use any
of the API method which change the data (write(), assignment to a slice,
etc.).

Here's an example using the default access mode of ACCESS_WRITE and assigning
to a slice to modify part of a line in place::

    import mmap
    import shutil

    # Copy the example file
    shutil.copyfile('lorem.txt', 'lorem_copy.txt')

    word = 'consectetuer'
    reversed = word[::-1]
    print 'Looking for    :', word
    print 'Replacing with :', reversed

    f = open('lorem_copy.txt', 'r+')
    try:
        m = mmap.mmap(f.fileno(), 0)
        try:
            print 'Before:', m.readline().rstrip()
            m.seek(0) # rewind

            loc = m.find(word)
            m[loc:loc+len(word)] = reversed
            m.flush()

            m.seek(0) # rewind
            print 'After :', m.readline().rstrip()
        finally:
            m.close()
    finally:
        f.close()

As you can see here, the word shown in bold is replaced in the middle of the
first line::

    $ python mmap_write_slice.py
    Looking for    : consectetuer
    Replacing with : reutetcesnoc
    Before: Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Donec
    After : Lorem ipsum dolor sit amet, reutetcesnoc adipiscing elit. Donec

ACCESS_COPY Mode
================

Using the ACCESS_COPY mode does not write changes to the file on disk. 

::

    f = open('lorem_copy.txt', 'r+')
    try:
        m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_COPY)
        try:
            print 'Memory Before:', m.readline().rstrip()
            print 'File Before  :', f.readline().rstrip()
            print

            m.seek(0) # rewind
            loc = m.find(word)
            m[loc:loc+len(word)] = reversed

            m.seek(0) # rewind
            print 'Memory After :', m.readline().rstrip()

            f.seek(0)
            print 'File After   :', f.readline().rstrip()

        finally:
            m.close()
    finally:
        f.close()

Note, in this example, that it was necessary to rewind the file handle
separately from the mmap handle.

::

    $ python mmap_write_copy.py 
    Memory Before: Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Donec
    File Before  : Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Donec

    Memory After : Lorem ipsum dolor sit amet, reutetcesnoc adipiscing elit. Donec
    File After   : Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Donec

Regular Expressions
===================

Since a memory mapped file can act like a string, you can use it with other
modules that operate on strings, such as regular expressions. This example
finds all of the sentences with "nulla" in them.

::

    import mmap
    import re

    pattern = re.compile(r'(\.\W+)?([^.]?nulla[^.]*?\.)',
                         re.DOTALL | re.IGNORECASE | re.MULTILINE)

    f = open('lorem.txt', 'r')
    try:
        m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
        try:
            for match in pattern.findall(m):
                print match[1].replace('\n', ' ')
        finally:
            m.close()
    finally:
        f.close()

Since the pattern includes two groups, the return value from findall() is a
sequence of tuples. The print statement pulls out the sentence match and
replaces newlines with spaces so the result prints on a single line.

::

    $ python mmap_regex.py
    Nulla facilisi.
    Nulla feugiat augue eleifend nulla.

