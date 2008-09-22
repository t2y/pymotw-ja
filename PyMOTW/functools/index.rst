================
functools
================
.. module:: functools
    :synopsis: Tools for making decorators and other function wrappers.

:Module: functools
:Purpose: Tools for making decorators and other function wrappers.
:Python Version: new in 2.5
:Abstract:

    The functools module includes tools for wrapping functions and other
    callable objects.

Description
===========

The primary tool supplied by the functools module is the class partial, which
can be used to "wrap" a callable with default arguments. The resulting object
is itself callable and can be treated as though it is the original function.
It takes all of the same arguments as the original callable and can be invoked
with extra positional or named arguments as well.

partial
=======

This example shows two simple partial objects for the function myfunc().
Notice that show_details() prints the func, args, and keywords attributes of
the partial object.

::

    import functools

    def myfunc(a, b=2):
        """Docstring for myfunc()."""
        print '\tcalled myfunc with:', (a, b)
        return

    def show_details(name, f, is_partial=False):
        """Show details of a callable object."""
        print '%s:' % name
        print '\tobject:', f
        if not is_partial:
            print '\t__name__:', f.__name__
        print '\t__doc__', repr(f.__doc__)
        if is_partial:
            print '\tfunc:', f.func
            print '\targs:', f.args
            print '\tkeywords:', f.keywords
        return

    show_details('myfunc', myfunc)
    myfunc('a', 3)
    print

    p1 = functools.partial(myfunc, b=4)
    show_details('partial with named default', p1, True)
    p1('default a')
    p1('override b', b=5)
    print

    p2 = functools.partial(myfunc, 'default a', b=99)
    show_details('partial with defaults', p2, True)
    p2()
    p2(b='override b')
    print

    print 'Insufficient arguments:'
    p1()


At the end of the example, the first partial created is invoked without
passing a value for a, causing an exception.

::

    $ python functools_partial.py
    myfunc:
        object: <function myfunc at 0x7cbf0>
        __name__: myfunc
        __doc__ 'Docstring for myfunc().'
        called myfunc with: ('a', 3)

    partial with named default:
        object: <functools.partial object at 0x74ea0>
        __doc__ 'partial(func, *args, **keywords) - new function with partial application\n\tof the given arguments and keywords.\n'
        func: <function myfunc at 0x7cbf0>
        args: ()
        keywords: {'b': 4}
        called myfunc with: ('default a', 4)
        called myfunc with: ('override b', 5)

    partial with defaults:
        object: <functools.partial object at 0x74ed0>
        __doc__ 'partial(func, *args, **keywords) - new function with partial application\n\tof the given arguments and keywords.\n'
        func: <function myfunc at 0x7cbf0>
        args: ('default a',)
        keywords: {'b': 99}
        called myfunc with: ('default a', 99)
        called myfunc with: ('default a', 'override b')

    Insufficient arguments:
    Traceback (most recent call last):
      File "/Users/dhellmann/Documents/PyMOTW/in_progress/functools/functools_partial.py", line 48, in <module>
        p1()
    TypeError: myfunc() takes at least 1 non-keyword argument (0 given)


update_wrapper
==============

As illustrated in the previous example, the partial object does not have a
__name__ or __doc__ attributes by default. Losing those attributes for
decorated functions makes them more difficult to debug. By using
update_wrapper, you can copy or add attributes from the original function to
the partial object.

::

    import functools

    def myfunc(a, b=2):
        """Docstring for myfunc()."""
        print '\tcalled myfunc with:', (a, b)
        return

    def show_details(name, f):
        """Show details of a callable object."""
        print '%s:' % name
        print '\tobject:', f
        print '\t__name__:', 
        try:
            print f.__name__
        except AttributeError:
            print '(no __name__)'
        print '\t__doc__', repr(f.__doc__)
        print
        return

    show_details('myfunc', myfunc)

    p1 = functools.partial(myfunc, b=4)
    show_details('raw wrapper', p1)

    print 'Updating wrapper:'
    print '\tassign:', functools.WRAPPER_ASSIGNMENTS
    print '\tupdate:', functools.WRAPPER_UPDATES
    print

    functools.update_wrapper(p1, myfunc)
    show_details('updated wrapper', p1)

The attributes added to the wrapper are defined in
functools.WRAPPER_ASSIGNMENTS, while functools.WRAPPER_UPDATES lists values to
be modified.

::

    $ python functools_update_wrapper.py
    myfunc:
        object: <function myfunc at 0x7cb30>
        __name__: myfunc
        __doc__ 'Docstring for myfunc().'

    raw wrapper:
        object: <functools.partial object at 0x74f30>
        __name__: (no __name__)
        __doc__ 'partial(func, *args, **keywords) - new function with partial application\n\tof the given arguments and keywords.\n'

    Updating wrapper:
        assign: ('__module__', '__name__', '__doc__')
        update: ('__dict__',)

    updated wrapper:
        object: <functools.partial object at 0x74f30>
        __name__: myfunc
        __doc__ 'Docstring for myfunc().'

Methods and Other Callables
===========================

Partials work with any callable object, including methods and instances.

::

    import functools

    class MyClass(object):
        """Demonstration class for functools"""
        
        def meth1(self, a, b=2):
            """Docstring for meth1()."""
            print '\tcalled meth1 with:', (self, a, b)
            return
        
        def meth2(self, c, d=5):
            """Docstring for meth2"""
            print '\tcalled meth2 with:', (self, c, d)
            return
        wrapped_meth2 = functools.partial(meth2, 'wrapped c')
        functools.update_wrapper(wrapped_meth2, meth2)
        
        def __call__(self, e, f=6):
            """Docstring for MyClass.__call__"""
            print '\tcalled object with:', (self, e, f)
            return

    def show_details(name, f):
        """Show details of a callable object."""
        print '%s:' % name
        print '\tobject:', f
        print '\t__name__:', 
        try:
            print f.__name__
        except AttributeError:
            print '(no __name__)'
        print '\t__doc__', repr(f.__doc__)
        return
        
    o = MyClass()

    show_details('meth1 straight', o.meth1)
    o.meth1('no default for a', b=3)
    print

    p1 = functools.partial(o.meth1, b=4)
    functools.update_wrapper(p1, o.meth1)
    show_details('meth1 wrapper', p1)
    p1('a goes here')
    print

    show_details('meth2', o.meth2)
    o.meth2('no default for c', d=6)
    print

    show_details('wrapped meth2', o.wrapped_meth2)
    o.wrapped_meth2('no default for c', d=6)
    print

    show_details('instance', o)
    o('no default for e')
    print

    p2 = functools.partial(o, f=7)
    show_details('instance wrapper', p2)
    p2('e goes here')


::

    $ python functools_method.py
    meth1 straight:
        object: <bound method MyClass.meth1 of <__main__.MyClass object at 0x7ecd0>>
        __name__: meth1
        __doc__ 'Docstring for meth1().'
        called meth1 with: (<__main__.MyClass object at 0x7ecd0>, 'no default for a', 3)

    meth1 wrapper:
        object: <functools.partial object at 0x81060>
        __name__: meth1
        __doc__ 'Docstring for meth1().'
        called meth1 with: (<__main__.MyClass object at 0x7ecd0>, 'a goes here', 4)

    meth2:
        object: <bound method MyClass.meth2 of <__main__.MyClass object at 0x7ecd0>>
        __name__: meth2
        __doc__ 'Docstring for meth2'
        called meth2 with: (<__main__.MyClass object at 0x7ecd0>, 'no default for c', 6)

    wrapped meth2:
        object: <functools.partial object at 0x74f90>
        __name__: meth2
        __doc__ 'Docstring for meth2'
        called meth2 with: ('wrapped c', 'no default for c', 6)

    instance:
        object: <__main__.MyClass object at 0x7ecd0>
        __name__: (no __name__)
        __doc__ 'Demonstration class for functools'
        called object with: (<__main__.MyClass object at 0x7ecd0>, 'no default for e', 6)

    instance wrapper:
        object: <functools.partial object at 0x81090>
        __name__: (no __name__)
        __doc__ 'partial(func, *args, **keywords) - new function with partial application\n\tof the given arguments and keywords.\n'
        called object with: (<__main__.MyClass object at 0x7ecd0>, 'e goes here', 7)

wraps
=====

As mentioned earlier, these capabilities are especially useful when used in
decorators, since the decorated function ends up with properties of the
original, "raw", function. functools provides a convenience function, wraps(),
to be used as a decorator itself and to apply update_wrapper() automatically.

::

    import functools

    def show_details(name, f):
        """Show details of a callable object."""
        print '%s:' % name
        print '\tobject:', f
        print '\t__name__:', 
        try:
            print f.__name__
        except AttributeError:
            print '(no __name__)'
        print '\t__doc__', repr(f.__doc__)
        print
        return

    def simple_decorator(f):
        @functools.wraps(f)
        def decorated(a='decorated defaults', b=1):
            print '\tdecorated:', (a, b)
            print '\t',
            f(a, b=b)
            return
        return decorated

    def myfunc(a, b=2):
        print '\tmyfunc:', (a,b)
        return

    show_details('myfunc', myfunc)
    myfunc('unwrapped, default b')
    myfunc('unwrapped, passing b', 3)
    print

    wrapped_myfunc = simple_decorator(myfunc)
    show_details('wrapped_myfunc', wrapped_myfunc)
    wrapped_myfunc()
    wrapped_myfunc('args to decorated', 4)


::

    $ python functools_wraps.py
    myfunc:
        object: <function myfunc at 0x7cc70>
        __name__: myfunc
        __doc__ None

        myfunc: ('unwrapped, default b', 2)
        myfunc: ('unwrapped, passing b', 3)

    wrapped_myfunc:
        object: <function myfunc at 0x7ccb0>
        __name__: myfunc
        __doc__ None

        decorated: ('decorated defaults', 1)
            myfunc: ('decorated defaults', 1)
        decorated: ('args to decorated', 4)
            myfunc: ('args to decorated', 4)
