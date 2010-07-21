====================================
dircache -- Cache directory listings
====================================

.. module:: dircache
    :synopsis: Cache directory listings, updating when the modification time of a directory changes.

:Purpose: Cache directory listings, updating when the modification time of a directory changes.
:Python Version: 1.4 and later

Listing Directory Contents
==========================

The main function in the dircache API is listdir(), a wrapper around
os.listdir() that caches the results and returns the same list each
time it is called with the same path unless the modification date of
the named directory changes.

.. include:: dircache_listdir.py
    :literal:
    :start-after: #end_pymotw_header

It is important to recognize that the exact same list is returned each time,
so it should not be modified in place.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'dircache_listdir.py'))
.. }}}

::

	$ python dircache_listdir.py
	Contents : ['__init__.py', 'dircache_annotate.py', 'dircache_listdir.py', 'dircache_listdir_file_added.py', 'dircache_reset.py', 'index.rst']
	Identical: True
	Equal    : True

.. {{{end}}}

If the contents of the directory changes, it is rescanned.

.. include:: dircache_listdir_file_added.py
    :literal:
    :start-after: #end_pymotw_header

In this case the new file causes a new list to be constructed.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'dircache_listdir_file_added.py'))
.. }}}

::

	$ python dircache_listdir_file_added.py
	Identical : False
	Equal     : False
	Difference: ['pymotw_tmp.txt']

.. {{{end}}}

It is also possible to reset the entire cache, discarding its contents so that
each path will be rechecked.

.. include:: dircache_reset.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'dircache_reset.py'))
.. }}}

::

	$ python dircache_reset.py
	Identical : False
	Equal     : True
	Difference: []

.. {{{end}}}


Annotated Listings
==================

The other interesting function provided by the dircache module is annotate().
When called, annotate() modifies a list such as is returned by listdir(),
adding a '/' to the end of the names that represent directories. (Sorry
Windows users, although it uses os.path.join() to construct names to test, it
always appends a ``'/'``, not os.sep.)

.. include:: dircache_annotate.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'dircache_annotate.py'))
.. }}}

::

	$ python dircache_annotate.py
	                 ORIGINAL	                ANNOTATED
	-------------------------	-------------------------
	                      .hg	                     .hg/
	                .hgignore	                .hgignore
	                  .hgtags	                  .hgtags
	              LICENSE.txt	              LICENSE.txt
	              MANIFEST.in	              MANIFEST.in
	                   PyMOTW	                  PyMOTW/
	               README.txt	               README.txt
	                      bin	                     bin/
	                   module	                   module
	                     motw	                     motw
	              pavement.py	              pavement.py
	   sitemap_gen_config.xml	   sitemap_gen_config.xml
	                   sphinx	                  sphinx/
	                    utils	                   utils/

.. {{{end}}}

.. seealso::

    `dircache <http://docs.python.org/library/dircache.html>`_
        The standard library documentation for this module.

