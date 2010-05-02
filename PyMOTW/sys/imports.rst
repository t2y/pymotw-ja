.. _sys-imports:

===================
Modules and Imports
===================

Most Python programs end up as a combination of several modules with a
main application importing them. Whether you are using the features of
the standard library, or organizing your own code in separate files to
make it easier to maintain, understanding and managing the
dependencies for your program is an important aspect of
development. :mod:`sys` includes information about the modules
available to your application, either as built-ins or after being
imported.  It also defines hooks for overriding the standard import
behavior for special cases.

.. _sys-modules:

Imported Modules
================

``sys.modules`` is a dictionary mapping the names of imported modules to the module object holding the code.

.. include:: sys_modules.py
    :literal:
    :start-after: #end_pymotw_header

The contents of ``sys.modules`` change as new modules are imported.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sys_modules.py'))
.. }}}
.. {{{end}}}


Built-in Modules
================

The Python interpreter can be compiled with some C modules built right in, so you don't need to distribute them
as separate shared libraries. These modules don't appear in the list of imported modules managed in
``sys.modules`` because they weren't technically imported. The only way to find the available built-in modules is
through ``sys.builtin_module_names``.

.. include:: sys_builtins.py
    :literal:
    :start-after: #end_pymotw_header

.. note::

    Your results may vary, especially if you have built a custom version of the interpreter.
    This script was run using a copy of the interpreter installed from the standard python.org
    installer for the platform.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sys_builtins.py'))
.. }}}
.. {{{end}}}


.. seealso::

    `Build instructions <http://svn.python.org/view/python/trunk/README?view=markup>`_
        Instructions for building Python, from the README distributed with the source.

Import Path
===========

The search path for modules is managed as a Python list saved in ``sys.path``. The default contents of the path
include the directory of the script used to start the application and the current working directory.

.. include:: sys_path_show.py
    :literal:
    :start-after: #end_pymotw_header

As you can see here, the first directory in the search path is the home for the sample script itself. That is
followed by a series of platform-specific paths where compiled extension modules (written in C) might be
installed, and then the global ``site-packages`` directory is listed last.

::

	$ python sys_path_show.py
	/Users/dhellmann/Documents/PyMOTW/src/PyMOTW/sys
	/Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6
	/Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/plat-darwin
	/Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/lib-tk
	/Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/plat-mac
	/Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/plat-mac/lib-scriptpackages
	/Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/site-packages


The import search path list can be modified before starting the interpreter by setting the shell variable
``PYTHONPATH`` to a colon-separated list of directories.

::

	$ PYTHONPATH=/my/private/site-packages:/my/shared/site-packages python sys_path_show.py
	/Users/dhellmann/Documents/PyMOTW/src/PyMOTW/sys
	/my/private/site-packages
	/my/shared/site-packages
	/Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6
	/Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/plat-darwin
	/Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/lib-tk
	/Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/plat-mac
	/Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/plat-mac/lib-scriptpackages
	/Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/site-packages

A program can also modify its path by adding elements to ``sys.path`` directly.

.. include:: sys_path_modify.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sys_path_modify.py'))
.. }}}
.. {{{end}}}


Custom Importers
================

Modifying the search path lets you control how standard Python modules are found, but what if you need to import
code from somewhere other than the usual ``.py`` or ``.pyc`` files on the filesystem? :pep:`302` solves this
problem by introducing the idea of *import hooks* that let you trap an attempt to find a module on the search
path and take alternative measures to load the code from somewhere else or apply pre-processing to it.

Finders
-------

Custom importers are implemented in two separate phases. The *finder* is responsible for locating a module and
providing a *loader* to manage the actual import. Adding a custom module finder is as simple as appending a
factory to the ``sys.path_hooks`` list. On import, each part of the path is given to a finder until one claims
support (by not raising ImportError). That finder is then responsible for searching data storage represented by
its path entry for named modules.

.. include:: sys_path_hooks_noisy.py
    :literal:
    :start-after: #end_pymotw_header

This example illustrates how the finders are instantiated and queried. The NoisyImportFinder raises ImportError
when instantiated with a path entry that does not match its special trigger value, which is obviously not a real
path on the filesystem. This test prevents the NoisyImportFinder from breaking imports of real modules.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sys_path_hooks_noisy.py'))
.. }}}
.. {{{end}}}

Importing from a Shelve
-----------------------

When the finder locates a module, it is responsible for returning a *loader* capable of importing that module.
This example illustrates a custom importer that saves its module contents in a database created by :mod:`shelve`.

The first step is to create a script to populate the shelf with a package containing a sub-module and
sub-package.

.. include:: sys_shelve_importer_create.py
    :literal:
    :start-after: #end_pymotw_header

A real packaging script would read the contents from the filesystem, but using hard-coded values is sufficient
for a simple example like this.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sys_shelve_importer_create.py'))
.. }}}
.. {{{end}}}

Next, we need to provide finder and loader classes that know how to look in a shelf for the source of a module or
package:

.. include:: sys_shelve_importer.py
    :literal:
    :start-after: #end_pymotw_header

Now we can use ``ShelveFinder`` and ``ShelveLoader`` to import code from a shelf. For example, importing the
``package`` created above:

.. include:: sys_shelve_importer_package.py
    :literal:
    :start-after: #end_pymotw_header

The shelf is added to the import path the first time an import occurs after the path is modified. The finder
recognizes the shelf and returns a loader, which is used for all imports from that shelf. The initial
package-level import creates a new module object and then execs the source loaded from the shelf, using the new
module as the namespace so that names defined in the source are preserved as module-level attributes. 

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sys_shelve_importer_package.py'))
.. }}}
.. {{{end}}}

Packages
--------

The loading of other modules and sub-packages proceeds in the same way.

.. include:: sys_shelve_importer_module.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sys_shelve_importer_module.py'))
.. }}}
.. {{{end}}}

Reloading
---------

Reloading a module is handled slightly differently. Instead of creating a new module object, the existing module
is re-used.

.. include:: sys_shelve_importer_reload.py
    :literal:
    :start-after: #end_pymotw_header

By re-using the same object, existing references to the module are preserved even if class or function
definitions are modified by the reload.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sys_shelve_importer_reload.py'))
.. }}}
.. {{{end}}}

Import Errors
-------------

When a module cannot be imported, ``ImportError`` is raised.

.. include:: sys_shelve_importer_missing.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sys_shelve_importer_missing.py'))
.. }}}
.. {{{end}}}

Package Data
------------

In addition to defining the API loading executable Python code, :pep:`302` defines an optional API for retrieving
package data intended for distributing data files, documentation, and other non-code resources used by a package. By implementing ``get_data()``, a loader can allow calling applications to support retrieval of data associated with the package without considering how the package is actually installed (especially without assuming that the package is stored as files on a filesystem).

.. include:: sys_shelve_importer_get_data.py
    :literal:
    :start-after: #end_pymotw_header

``get_data()`` takes a path based on the module or package that owns the data, and returns the contents of the
resource "file" as a string, or raises IOError if the resource does not exist.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sys_shelve_importer_get_data.py', ignore_error=True))
.. }}}
.. {{{end}}}


Importer Cache
==============

Searching through all of the hooks each time a module is imported can become expensive. To save time,
``sys.path_importer_cache`` is maintained as a mapping between a path entry and the loader that can use the
value to find modules.

.. include:: sys_path_importer_cache.py
    :literal:
    :start-after: #end_pymotw_header

A cache value of ``None`` means to use the default filesystem loader. Each missing directory is associated with
an ``imp.NullImporter`` instance, since modules cannot be imported from directories that do not exist. In the
example output below, several ``zipimport.zipimporter`` instances are used to manage EGG files found on the path.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sys_path_importer_cache.py'))
.. }}}
.. {{{end}}}


Meta Path
=========

The ``sys.meta_path`` further extends the sources of potential imports by allowing a finder to be searched
*before* the regular ``sys.path`` is scanned. The API for a finder on the meta-path is the same as for a regular
path. The difference is that the meta-finder is not limited to a single entry in ``sys.path``, it can search
anywhere at all.

.. include:: sys_meta_path.py
    :literal:
    :start-after: #end_pymotw_header

Each finder on the meta-path is interrogated before ``sys.path`` is searched, so there is always an opportunity to have a central importer load modules without explicitly modifying ``sys.path``.  Once the module is "found", the loader API works in the same way as for regular loaders (although this example is truncated for simplicity).

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sys_meta_path.py'))
.. }}}
.. {{{end}}}



.. seealso::

    :pep:`302`
        Import Hooks

    :mod:`imp`
        The imp module provides tools used by importers.
        
    :mod:`zipimport`
        Implements importing Python modules from inside ZIP archives.
        
    `The Quick Guide to Python Eggs <http://peak.telecommunity.com/DevCenter/PythonEggs>`_
        PEAK documentation for working with EGGs.
    
    `Import this, that, and the other thing: custom importers <http://us.pycon.org/2010/conference/talks/?filter=core>`_
        Brett Cannon's PyCon 2010 presentation.
        
    `Python 3 stdlib module "importlib" <http://docs.python.org/py3k/library/importlib.html>`_
        Python 3.x includes abstract base classes that makes it easier to create custom importers.
