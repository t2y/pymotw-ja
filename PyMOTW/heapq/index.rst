============
heapq
============
.. module:: heapq
    :synopsis: In-place heap sort algorithm

:Module: heapq
:Purpose: In-place heap sort algorithm
:Python Version: New in 2.3 with additions in 2.5
:Abstract:

    The heapq implements a min-heap sort algorithm suitable for use with
    Python's lists.


Description
===========

A heap is a tree-like data structure where the child nodes have a sort-order
relationship with the parents. Binary heaps can be represented using a list or
array organized so that the children of element N are at positions 2*N+1 and
2*N+2 (for zero-based indexes). This feature makes it possible to rearrange
heaps in place, so it is not necessary to reallocate as much memory when
adding or removing items.

A max-heap ensures that the parent is larger than or equal to both of its
children. A min-heap requires that the parent be less than or equal to its
children. Python's heapq module implements a min-heap.

Creating a Heap
===============

There are 2 basic ways to create a heap, heappush() and heapify().

Using heappush(), the heap sort order of the elements is maintained as new
items are added from a data source.

::

    import heapq
    from heapq_showtree import show_tree
    from heapq_heapdata import data

    heap = []
    print 'random :', data
    print

    for n in data:
        print 'add %3d:' % n
        heapq.heappush(heap, n)
        show_tree(heap)


::

    $ python heapq_heappush.py
    random : [19, 9, 4, 10, 11, 8, 2]

    add  19:

                     19                 
    ------------------------------------

    add   9:

                     9                  
            19        
    ------------------------------------

    add   4:

                     4                  
            19                9         
    ------------------------------------

    add  10:

                     4                  
            10                9         
        19   
    ------------------------------------

    add  11:

                     4                  
            10                9         
        19       11   
    ------------------------------------

    add   8:

                     4                  
            10                8         
        19       11       9    
    ------------------------------------

    add   2:

                     2                  
            10                4         
        19       11       9        8    
    ------------------------------------


If the data is already in memory, it is more efficient to use heapify() to
rearrange the items of the list in place.

::

    import heapq
    from heapq_showtree import show_tree
    from heapq_heapdata import data

    print 'random    :', data
    heapq.heapify(data)
    print 'heapified :'
    show_tree(data)

::

    $ python heapq_heapify.py
    random    : [19, 9, 4, 10, 11, 8, 2]
    heapified :

                     2                  
            9                 4         
        10       11       8        19   
    ------------------------------------


Accessing Contents of a Heap
============================

Once the heap is organized correctly, use heappop() to remove the element with
the lowest value. In this example, adapted from the stdlib documentation,
heapify() and heappop() are used to sort a list of numbers.

::

    import heapq
    from heapq_showtree import show_tree
    from heapq_heapdata import data

    print 'random    :', data
    heapq.heapify(data)
    print 'heapified :'
    show_tree(data)
    print

    inorder = []
    while data:
        smallest = heapq.heappop(data)
        print 'pop    %3d:' % smallest
        show_tree(data)
        inorder.append(smallest)
    print 'inorder   :', inorder


::

    $ python heapq_heappop.py
    random    : [19, 9, 4, 10, 11, 8, 2]
    heapified :

                     2                  
            9                 4         
        10       11       8        19   
    ------------------------------------


    pop      2:

                     4                  
            9                 8         
        10       11       19   
    ------------------------------------

    pop      4:

                     8                  
            9                 19        
        10       11   
    ------------------------------------

    pop      8:

                     9                  
            10                19        
        11   
    ------------------------------------

    pop      9:

                     10                 
            11                19        
    ------------------------------------

    pop     10:

                     11                 
            19        
    ------------------------------------

    pop     11:

                     19                 
    ------------------------------------

    pop     19:

    ------------------------------------

    inorder   : [2, 4, 8, 9, 10, 11, 19]


To remove existing elements and replace them with new values in a single
operation, use heapreplace().

::

    import heapq
    from heapq_showtree import show_tree
    from heapq_heapdata import data

    heapq.heapify(data)
    print 'start:'
    show_tree(data)

    for n in [0, 7, 13, 9, 5]:
        smallest = heapq.heapreplace(data, n)
        print 'replace %2d with %2d:' % (smallest, n)
        show_tree(data)


This technique lets you maintain a fixed size heap, such as a queue of jobs
ordered by priority.

::

    $ python heapq_heapreplace.py
    start:

                     2                  
            9                 4         
        10       11       8        19   
    ------------------------------------

    replace  2 with  0:

                     0                  
            9                 4         
        10       11       8        19   
    ------------------------------------

    replace  0 with  7:

                     4                  
            9                 7         
        10       11       8        19   
    ------------------------------------

    replace  4 with 13:

                     7                  
            9                 8         
        10       11       13       19   
    ------------------------------------

    replace  7 with  9:

                     8                  
            9                 9         
        10       11       13       19   
    ------------------------------------

    replace  8 with  5:

                     5                  
            9                 9         
        10       11       13       19   
    ------------------------------------


Data Extremes
=============

heapq also includes 2 functions to examine an iterable to find a range of the
largest or smallest values it contains. Using nlargest() and nsmallest() are
really only efficient for relatively small values of n > 1, but can still come
in handy in a few cases.

::

    import heapq
    from heapq_heapdata import data

    print 'all       :', data
    print '3 largest :', heapq.nlargest(3, data)
    print 'from sort :', list(reversed(sorted(data)[-3:]))
    print '3 smallest:', heapq.nsmallest(3, data)
    print 'from sort :', sorted(data)[:3]


    $ python heapq_extremes.py
    all       : [19, 9, 4, 10, 11, 8, 2]
    3 largest : [19, 11, 10]
    from sort : [19, 11, 10]
    3 smallest: [2, 4, 8]
    from sort : [2, 4, 8]
