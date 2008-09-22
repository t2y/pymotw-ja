===============
operator
===============
.. module:: operator
    :synopsis: Functional interface to built-in operators.

:Module: operator
:Purpose: Functional interface to built-in operators.
:Python Version: 1.4 and later
:Abstract:

    The operator module contains functions that perform the same operations as
    man of the built-in operators.

Description
===========

Functional programming using iterators occasionally requires you to create
small functions for simple expressions. Sometimes these can be expressed as
lambda functions. But for some operations, you don't need to define your own
function at all. The operator module defines functions that correspond to
built-in operations for arithmetic, and comparison as well as sequence and
dictionary operations.

Logical Operations
==================

There are logical operations for determining the boolean equivalent for a
value, negating that to create the opposite boolean value, and comparing
objects to see if they are identical.

::

    from operator import *

    a = -1
    b = 5

    print 'a =', a
    print 'b =', b

    print 'not_(a):', not_(a)
    print 'truth(a):', truth(a)
    print 'is_(a, b):', is_(a,b)
    print 'is_not(a, b):', is_not(a,b)

::

    $ python operator_boolean.py
    a = -1
    b = 5
    not_(a): False
    truth(a): True
    is_(a, b): False
    is_not(a, b): True


Comparison Operators
====================

All of the rich comparison operators are supported::

    from operator import *

    a = 1
    b = 5.0

    print 'a =', a
    print 'b =', b
    for func in (lt, le, eq, ne, ge, gt):
        print '%s(a, b):' % func.__name__, func(a, b)

::

    $ python operator_comparisons.py
    a = 1
    b = 5.0
    lt(a, b): True
    le(a, b): True
    eq(a, b): False
    ne(a, b): True
    ge(a, b): False
    gt(a, b): False


Arithmetic Operators
====================

The arithmetic operators for manipulating numerical values are also supported.

::

    from operator import *

    a = -1
    b = 5.0
    c = 2
    d = 6

    print 'a =', a
    print 'b =', b
    print 'c =', c
    print 'd =', d

    print '\nPositive/Negative:'
    print 'abs(a):', abs(a)
    print 'neg(a):', neg(a)
    print 'neg(b):', neg(b)
    print 'pos(a):', pos(a)
    print 'pos(b):', pos(b)

    print '\nArithmetic:'
    print 'add(a, b):', add(a, b)
    print 'div(a, b):', div(a, b)
    print 'div(d, c):', div(d, c)
    print 'floordiv(a, b):', floordiv(a, b)
    print 'floordiv(d, c):', floordiv(d, c)
    print 'mod(a, b):', mod(a, b)
    print 'mul(a, b):', mul(a, b)
    print 'pow(c, d):', pow(c, d)
    print 'sub(b, a):', sub(b, a)
    print 'truediv(a, b):', truediv(a, b)
    print 'truediv(d, c):', truediv(d, c)

    print '\nBitwise:'
    print 'and_(c, d):', and_(c, d)
    print 'invert(c):', invert(c)
    print 'lshift(c, d):', lshift(c, d)
    print 'or_(c, d):', or_(c, d)
    print 'rshift(d, c):', rshift(d, c)
    print 'xor(c, d):', xor(c, d)


Notice the two division operators: floordiv (pre-3.0 integer division) and
truediv (floating point division).

::

    $ python operator_math.py
    a = -1
    b = 5.0
    c = 2
    d = 6

    Positive/Negative:
    abs(a): 1
    neg(a): 1
    neg(b): -5.0
    pos(a): -1
    pos(b): 5.0

    Arithmetic:
    add(a, b): 4.0
    div(a, b): -0.2
    div(d, c): 3
    floordiv(a, b): -1.0
    floordiv(d, c): 3
    mod(a, b): 4.0
    mul(a, b): -5.0
    pow(c, d): 64
    sub(b, a): 6.0
    truediv(a, b): -0.2
    truediv(d, c): 3.0

    Bitwise:
    and_(c, d): 2
    invert(c): -3
    lshift(c, d): 128
    or_(c, d): 6
    rshift(d, c): 1
    xor(c, d): 4


Sequence Operators
==================

The operators for working with sequences can be divided into roughly 4 groups
for building up sequences, searching, working with items, and removing items
from sequences.

::

    from operator import *

    a = [ 1, 2, 3 ]
    b = [ 'a', 'b', 'c' ]

    print 'a =', a
    print 'b =', b

    print '\nConstructive:'
    print 'concat(a, b):', concat(a, b)
    print 'repeat(a, 3):', repeat(a, 3)

    print '\nSearching:'
    print 'contains(a, 1):', contains(a, 1)
    print 'contains(b, "d"):', contains(b, "d")
    print 'countOf(a, 1):', countOf(a, 1)
    print 'countOf(b, "d"):', countOf(b, "d")
    print 'indexOf(a, 5):', indexOf(a, 1)

    print '\nAccess Items:'
    print 'getitem(b, 1):', getitem(b, 1)
    print 'getslice(a, 1, 3)', getslice(a, 1, 3)
    print 'setitem(b, 1, "d"):', setitem(b, 1, "d"), ',after b =', b
    print 'setslice(a, 1, 3, [4, 5]):', setslice(a, 1, 3, [4, 5]), ', after a =', a

    print '\nDestructive:'
    print 'delitem(b, 1):', delitem(b, 1), ',after b =', b
    print 'delslice(a, 1, 3):', delslice(a, 1, 3), ', after a =', a

::

    $ python operator_sequences.py
    a = [1, 2, 3]
    b = ['a', 'b', 'c']

    Constructive:
    concat(a, b): [1, 2, 3, 'a', 'b', 'c']
    repeat(a, 3): [1, 2, 3, 1, 2, 3, 1, 2, 3]

    Searching:
    contains(a, 1): True
    contains(b, "d"): False
    countOf(a, 1): 1
    countOf(b, "d"): 0
    indexOf(a, 5): 0

    Access Items:
    getitem(b, 1): b
    getslice(a, 1, 3) [2, 3]
    setitem(b, 1, "d"): None ,after b = ['a', 'd', 'c']
    setslice(a, 1, 3, [4, 5]): None , after a = [1, 4, 5]

    Destructive:
    delitem(b, 1): None ,after b = ['a', 'c']
    delslice(a, 1, 3): None , after a = [1]


In-place Operators
==================

In addition to the standard operators, many types of objects support
"in-place" modification through special operators such as +=. There are
equivalent functions for in-place modifications, too::

    from operator import *

    a = -1
    b = 5.0
    c = [ 1, 2, 3 ]
    d = [ 'a', 'b', 'c']
    print 'a =', a
    print 'b =', b
    print 'c =', c
    print 'd =', d

    print 'iadd(a, b):', iadd(a, b)
    a = iadd(a, b)
    print 'a = iadd(a, b) =>', a

    print 'iconcat(c, d):', iconcat(c, d)
    c = iconcat(c, d)
    print 'c = iconcat(c, d) =>', c


These examples only demonstrate a couple of the functions. Refer to the stdlib
documentation for complete details.

::

    $ python operator_inplace.py
    a = -1
    b = 5.0
    c = [1, 2, 3]
    d = ['a', 'b', 'c']
    iadd(a, b): 4.0
    a = iadd(a, b) => 4.0
    iconcat(c, d): [1, 2, 3, 'a', 'b', 'c']
    c = iconcat(c, d) => [1, 2, 3, 'a', 'b', 'c', 'a', 'b', 'c']


Attribute and Item "Getters"
============================

One of the most unusual features of the operator module is the notion of
"getters". These are callable objects constructed at runtime to retrieve
attributes of items from objects or sequences. Getters are especially useful
when working with iterators or generator sequences, where they are intended to
incur less overhead than a lambda or Python function.

Attribute getters work like lambda x, n='attrname': getattr(x, n)::

    from operator import *

    class MyObj(object):
        """example class for attrgetter"""
        def __init__(self, arg):
            super(MyObj, self).__init__()
            self.arg = arg
        def __repr__(self):
            return 'MyObj(%s)' % self.arg

    l = [ MyObj(i) for i in xrange(5) ]
    print l
    g = attrgetter('arg')
    vals = [ g(i) for i in l ]
    print vals

::

    $ python operator_attrgetter.py
    [MyObj(0), MyObj(1), MyObj(2), MyObj(3), MyObj(4)]
    [0, 1, 2, 3, 4]

While item getters work like lambda x, y=5: x[y]::

    from operator import *

    print 'Dictionaries:'
    l = [ dict(val=i) for i in xrange(5) ]
    print l
    g = itemgetter('val')
    vals = [ g(i) for i in l ]
    print vals

    print 'Tuples:'
    l = [ (i, i*2) for i in xrange(5) ]
    print l
    g = itemgetter(1)
    vals = [ g(i) for i in l ]
    print vals


Item getters work with mappings as well as sequences.

::

    $ python operator_itemgetter.py
    Dictionaries:
    [{'val': 0}, {'val': 1}, {'val': 2}, {'val': 3}, {'val': 4}]
    [0, 1, 2, 3, 4]
    Tuples:
    [(0, 0), (1, 2), (2, 4), (3, 6), (4, 8)]
    [0, 2, 4, 6, 8]


Working With Your Own Classes
=============================

The functions in the operator module work via the standard Python interfaces
for their operations, so they work with your classes as well as the builtin
types.

::

    from operator import *

    class MyObj(object):
        """Example for operator overloading"""
        def __init__(self, val):
            super(MyObj, self).__init__()
            self.val = val
            return
        def __str__(self):
            return 'MyObj(%s)' % self.val
        def __lt__(self, other):
            """compare for less-than"""
            print 'Testing %s < %s' % (self, other)
            return self.val < other.val
        def __add__(self, other):
            """add values"""
            print 'Adding %s + %s' % (self, other)
            return MyObj(self.val + other.val)

    a = MyObj(1)
    b = MyObj(2)

    print lt(a, b)
    print add(a, b)

::

    $ python operator_classes.py
    Testing MyObj(1) < MyObj(2)
    True
    Adding MyObj(1) + MyObj(2)
    MyObj(3)


Type Checking
=============

Besides the actual operators, there are functions for testing API compliance
for mapping, number, and sequence types. The tests are not perfect, since the
interfaces are not strictly defined, but they do give you some idea of what is
supported.

::

    from operator import *

    class NoType(object):
        """Supports none of the type APIs"""
        
    class MultiType(object):
        """Supports multiple type APIs"""
        def __len__(self):
            return 0
        def __getitem__(self, name):
            return 'mapping'
        def __int__(self):
            return 0

    o = NoType()
    t = MultiType()

    for func in (isMappingType, isNumberType, isSequenceType):
        print '%s(o):' % func.__name__, func(o)
        print '%s(t):' % func.__name__, func(t)

::

    $ python operator_typechecking.py
    isMappingType(o): False
    isMappingType(t): True
    isNumberType(o): False
    isNumberType(t): True
    isSequenceType(o): False
    isSequenceType(t): True

