======================================
pyclbr -- Python class browser support
======================================

.. module:: pyclbr
    :synopsis: Python class browser support

:Purpose: Implements an API suitable for use in a source code editor for making a class browser.
:Python Version: 1.4 and later

:mod:`pyclbr` can scan Python source to find classes and stand-alone functions.  The information about class, method, and function names and line numbers is gathered using :mod:`tokenize` *without* importing the code.

The examples below use this source file as input:

.. include:: pyclbr_example.py
    :literal:
    :start-after: #end_pymotw_header


Scanning for Classes
====================

There are two public functions exposed by :mod:`pyclbr`.  ``readmodule()`` takes the name of the module as argument returns a mapping of class names to ``Class`` objects containing the meta-data about the class source.

.. include:: pyclbr_readmodule.py
    :literal:
    :start-after: #end_pymotw_header

The meta-data for the class includes the file and line number where it is defined, as well as the names of super classes.  The methods of the class are saved as a mapping between method name and line number.  The output below shows the classes and methods listed in order based on their line number in the source file.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'pyclbr_readmodule.py'))
.. }}}
.. {{{end}}}


Scanning for Functions
======================

The other public function in :mod:`pyclbr` is ``readmodule_ex()``.  It does everything that ``readmodule()`` does, and adds functions to the result set.

.. include:: pyclbr_readmodule_ex.py
    :literal:
    :start-after: #end_pymotw_header

Each ``Function`` object has properties much like the ``Class`` object.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'pyclbr_readmodule_ex.py'))
.. }}}
.. {{{end}}}



.. seealso::

    `pyclbr <http://docs.python.org/library/pyclbr.html>`_
        The standard library documentation for this module.

    :mod:`inspect`
        The inspect module can discover more meta-data about classes and functions, but requires importing the code.

    :mod:`tokenize`
        The tokenize module parses Python source code into tokens.
