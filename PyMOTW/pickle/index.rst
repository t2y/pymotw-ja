================================
pickle and cPickle
================================
.. module:: pickle
    :synopsis: Python object serialization

.. module:: cPickle
    :synopsis: Python object serialization

:Module: pickle and cPickle
:Purpose: Python object serialization
:Python Version: pickle at least 1.4, cPickle 1.5

Description
===========

The pickle module implements an algorithm for turning an arbitrary Python
object into a series of bytes ("serializing" the object). The byte stream can
then be transmitted or stored, and later reconstructed to create a new object
with the same characteristics.

The cPickle module implements the same algorithm, in C instead of Python. It
is many times faster than the Python implementation, but does not allow the
user to subclass from Pickle. If subclassing is not important for your use,
you probably want to use cPickle.

Warning: The documentation for pickle makes clear that it offers no security
guarantees. Be careful if you use pickle for inter-process communication or
data storage and do not trust data you cannot verify as secure.

Example
=======

This first example of pickle encodes a data structure as a string, then prints
the string to the console.

::

    try:
       import cPickle as pickle
    except:
       import pickle
    import pprint

We first try to import cPickle, giving an alias of "pickle". If that import
fails for any reason, we fall back to the native Python implementation in the
pickle module. This gives us the faster implementation, if it is available,
and the portable implementation otherwise.

Next we define a data structure made up of entirely native types. Instances of
any class can be pickled, as will be illustrated in a later example. I chose
native data types to start to keep the example simple.

::

    data = [ { 'a':'A', 'b':2, 'c':3.0 } ]
    print 'DATA:',
    pprint.pprint(data)


And now we use pickle.dumps() to create a string representation of the value
of data.

::

    data_string = pickle.dumps(data)
    print 'PICKLE:', data_string

By default, the pickle will use only ASCII characters. A more efficient binary
format is also available, but I will be sticking with the ASCII version for
these examples.

::

    $ python pickle_string.py
    DATA:[{'a': 'A', 'b': 2, 'c': 3.0}]
    PICKLE: (lp1
    (dp2
    S'a'
    S'A'
    sS'c'
    F3
    sS'b'
    I2
    sa.

Once the data is serialized, you can write it to a file, socket, pipe, etc.
Then later you can read the file and unpickle the data to construct a new
object with the same values.

::

    data1 = [ { 'a':'A', 'b':2, 'c':3.0 } ]
    print 'BEFORE:',
    pprint.pprint(data1)

    data1_string = pickle.dumps(data1)

    data2 = pickle.loads(data1_string)
    print 'AFTER:',
    pprint.pprint(data2)

    print 'SAME?:', (data1 is data2)
    print 'EQUAL?:', (data1 == data2)

As you see, the newly constructed object is the equal to but not the same
object as the original. No surprise there.

::

    $ python pickle_unpickle.py
    BEFORE:[{'a': 'A', 'b': 2, 'c': 3.0}]
    AFTER:[{'a': 'A', 'b': 2, 'c': 3.0}]
    SAME?: False
    EQUAL?: True

In addition to dumps() and loads(), pickle provides a couple of convenience
functions for working with file-like streams. It is possible to write multiple
objects to a stream, and then read them from the stream without knowing in
advance how many objects are written or how big they are.

::

    try:
       import cPickle as pickle
    except:
       import pickle
    import pprint
    from StringIO import StringIO

    class SimpleObject(object):

       def __init__(self, name):
           self.name = name
           l = list(name)
           l.reverse()
           self.name_backwards = ''.join(l)
           return

    data = []
    data.append(SimpleObject('pickle'))
    data.append(SimpleObject('cPickle'))
    data.append(SimpleObject('last'))

    # Simulate a file with StringIO
    out_s = StringIO()

    # Write to the stream
    for o in data:
       print 'WRITING: %s (%s)' % (o.name, o.name_backwards)
       pickle.dump(o, out_s)
       out_s.flush()

    # Set up a read-able stream
    in_s = StringIO(out_s.getvalue())

    # Read the data
    while True:
       try:
           o = pickle.load(in_s)
       except EOFError:
           break
       else:
           print 'READ: %s (%s)' % (o.name, o.name_backwards)


The example simulates streams using StringIO buffers, so we have to play a
little trickery to establish the readable stream. A simple database format
might use pickles to store objects, too, though using the shelve module might
be easier to work with.

::

    $ python pickle_stream.py
    WRITING: pickle (elkcip)
    WRITING: cPickle (elkciPc)
    WRITING: last (tsal)
    READ: pickle (elkcip)
    READ: cPickle (elkciPc)
    READ: last (tsal)

In addition to storing data, pickles are very handy for inter-process
communication. For example, using os.fork() and os.pipe(), one can establish
worker processes which read job instructions from one pipe and write the
results to another pipe. The core code for managing the worker pool and
sending jobs in and receiving responses can be reused, since the job and
response objects don't have to be of a particular class. If you are using
pipes or sockets, do not forget to flush after dumping each object, to push
the data through the connection to the other end.

When working with your own classes, you must ensure that the class being
pickled appears in the namespace of the process reading the pickle. Only the
data for the instance is pickled, not the class definition. The class name is
used to find the constructor to create the new object when unpickling. Take
this example, which writes instances of a class to a file:

::

    try:
       import cPickle as pickle
    except:
       import pickle
    import sys

    class SimpleObject(object):

       def __init__(self, name):
           self.name = name
           l = list(name)
           l.reverse()
           self.name_backwards = ''.join(l)
           return

    if __name__ == '__main__':
       data = []
       data.append(SimpleObject('pickle'))
       data.append(SimpleObject('cPickle'))
       data.append(SimpleObject('last'))

       try:
           filename = sys.argv[1]
       except IndexError:
           raise RuntimeError('Please specify a filename as an argument to %s' % sys.argv[0])

       out_s = open(filename, 'wb')
       try:
           # Write to the stream
           for o in data:
               print 'WRITING: %s (%s)' % (o.name, o.name_backwards)
               pickle.dump(o, out_s)
       finally:
           out_s.close()

When I run the script, it will create a file I name as an argument on the
command line:

::

    $ python pickle_dump_to_file_1.py test.dat
    WRITING: pickle (elkcip)
    WRITING: cPickle (elkciPc)
    WRITING: last (tsal)

A simplistic attempt to load the resulting pickled objects might look like:

::

    try:
       import cPickle as pickle
    except:
       import pickle
    import pprint
    from StringIO import StringIO
    import sys

    try:
       filename = sys.argv[1]
    except IndexError:
       raise RuntimeError('Please specify a filename as an argument to %s' % sys.argv[0])

    in_s = open(filename, 'rb')
    try:
       # Read the data
       while True:
           try:
               o = pickle.load(in_s)
           except EOFError:
               break
           else:
               print 'READ: %s (%s)' % (o.name, o.name_backwards)
    finally:
       in_s.close()

This version fails because there is no SimpleObject class available:

::

    $ python pickle_load_from_file_1.py test.dat
    Traceback (most recent call last):
     File "pickle_load_from_file_1.py", line 52, in 
       o = pickle.load(in_s)
    AttributeError: 'module' object has no attribute 'SimpleObject'

A corrected version, which imports SimpleObject from the script which dumps
the data, succeeds.

Add:

::

    from pickle_dump_to_file_1 import SimpleObject

to the end of the import list, then run the script:

::

    $ python pickle_load_from_file_2.py test.dat
    READ: pickle (elkcip)
    READ: cPickle (elkciPc)
    READ: last (tsal)

There are some special considerations when pickling data types with values
that cannot be pickled (sockets, file handles, database connections, etc.).
Classes which use values which cannot be pickled can define __getstate__() and
__setstate__() to return a subset of the state of the instance to be pickled.
New-style classes can also define __getnewargs__(), which should return
arguments to be passed to the class memory allocator (C.__new__()). Use of
these features is covered in more detail in the standard library
documentation.

