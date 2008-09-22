==============
hashlib
==============
.. module:: hashlib
    :synopsis: Cryptographic hashes and message digests

:Module: hashlib
:Purpose: Cryptographic hashes and message digests
:Python Version: 2.5
:Abstract:

    Generate cryptographically secure hashes with hashlib.

Description
===========

The hashlib module deprecates the separate md5 and sha modules and makes their
API consistent. To work with a specific hash algorithm, use the appropriate
constructor function to create a hash object. Then you can use the same API to
interact with the hash no matter what algorithm is being used.

Since hashlib is "backed" by OpenSSL, all of of the algorithms provided by
that library should be available, including::

    md5()
    sha1()
    sha224()
    sha256()
    sha384()
    sha512()

MD5 Example
===========

To calculate the MD5 digest for a block of data (here an ASCII string), create
the hash, add the data, and compute the digest. 

::

    import hashlib

    from hashlib_data import lorem

    h = hashlib.md5()
    h.update(lorem)
    print h.hexdigest()

This example uses the hexdigest() method instead of digest() because the
output is formatted to be printed. If a binary digest value is acceptable, you
can use digest().

::

    $ python hashlib_md5.py
    c3abe541f361b1bfbbcfecbf53aad1fb

SHA1 Example
============

A SHA1 digest for the same data would be calculated in much the same way::

    import hashlib

    from hashlib_data import lorem

    h = hashlib.sha1()
    h.update(lorem)
    print h.hexdigest()

Of course, the digest value is different because of the different algorithm.

::

    $ python hashlib_sha1.py
    ac2a96a4237886637d5352d606d7a7b6d7ad2f29


new()
=====

Sometimes it is more convenient to refer to the algorithm by name in a string
rather than by using the constructor function directly. It is useful, for
example, to be able to store the hash type in a configuration file. In those
cases, use the new() function directly to create a new hash calculator.

::

    import hashlib
    import sys


    try:
        hash_name = sys.argv[1]
    except IndexError:
        print 'Specify the hash name as the first argument.'
    else:
        try:
            data = sys.argv[2]
        except IndexError:    
            from hashlib_data import lorem as data
        
        h = hashlib.new(hash_name)
        h.update(data)
        print h.hexdigest()

When run with a variety of arguments:

::

    $ python hashlib_new.py sha1
    ac2a96a4237886637d5352d606d7a7b6d7ad2f29
    $ python hashlib_new.py sha256
    88b7404fc192fcdb9bb1dba1ad118aa1ccd580e9faa110d12b4d63988cf20332
    $ python hashlib_new.py sha512
    f58c6935ef9d5a94d296207ee4a7d9bba411539d8677482b7e9d60e4b7137f68d25f9747cab62fe752ec5ed1e5b2fa4cdbc8c9203267f995a5d17e4408dccdb4
    $ python hashlib_new.py md5   
    c3abe541f361b1bfbbcfecbf53aad1fb

Calling update() more than once:

The update() method of the hash calculators can be called repeatedly. Each
time, the digest is updated based on the additional text fed in. This can be
much more efficient than reading an entire file into memory, for example.

::

    import hashlib

    from hashlib_data import lorem

    h = hashlib.md5()
    h.update(lorem)
    all_at_once = h.hexdigest()

    def chunkize(size, text):
        "Return parts of the text in size-based increments."
        start = 0
        while start < len(text):
            chunk = text[start:start+size]
            yield chunk
            start += size
        return

    h = hashlib.md5()
    for chunk in chunkize(64, lorem):
        h.update(chunk)
    line_by_line = h.hexdigest()

    print 'All at once :', all_at_once
    print 'Line by line:', line_by_line
    print 'Same        :', (all_at_once == line_by_line)

This example is a little contrived because it works with such a small amount
of text, but it illustrates how you could incrementally update a digest as
data is read or otherwise produced.

::

    $ python hashlib_update.py
    All at once : c3abe541f361b1bfbbcfecbf53aad1fb
    Line by line: c3abe541f361b1bfbbcfecbf53aad1fb
    Same        : True

