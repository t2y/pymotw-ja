.. _sys-interpreter:

====================
Interpreter Settings
====================

:mod:`sys` contains attributes and functions for accessing
compile-time or runtime configuration settings for the interpreter.

.. _sys-build-time-info:

Build-time Version Information
==============================

The version used to build the C interpreter is available in a few
forms.  :const:`sys.version` is a human-readable string that usually
includes the full version number as well as information about the
build date, compiler, and platform.  :const:`sys.hexversion` is easier
to use for checking the interpreter version since it is a simple
integer.  When formatted using :func:`hex`, it is clear that parts of
:const:`sys.hexversion` come from the version information also visible
in the more readable :const:`sys.version_info` (a 5-part tuple
representing just the version number).  

More specific information about the source that went into the build
can be found in the :const:`sys.subversion` tuple, which includes the
actual branch and subversion revision that was checked out and built.
The separate C API version used by the current interpreter is saved in
:const:`sys.api_version`.

.. include:: sys_version_values.py
    :literal:
    :start-after: #end_pymotw_header

All of the values depend on the actual interpreter used to run the
sample program, of course.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sys_version_values.py', interpreter='python2.6', break_lines_at=70))
.. cog.out(run_script(cog.inFile, 'sys_version_values.py', interpreter='python2.7', include_prefix=False, break_lines_at=70))
.. }}}

::

	$ python2.6 sys_version_values.py
	
	Version info:
	
	sys.version      = '2.6.8 (unknown, Aug 31 2012, 07:19:38) \n[GCC 4.2.
	1 (Based on Apple Inc. build 5658) (LLVM build 2336.1.00)]'
	sys.version_info = (2, 6, 8, 'final', 0)
	sys.hexversion   = 0x20608f0
	sys.subversion   = ('CPython', '', '')
	sys.api_version  = 1013

	$ python2.7 sys_version_values.py
	
	Version info:
	
	sys.version      = '2.7.2 (v2.7.2:8527427914a2, Jun 11 2011, 15:22:34)
	 \n[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)]'
	sys.version_info = sys.version_info(major=2, minor=7, micro=2, release
	level='final', serial=0)
	sys.hexversion   = 0x20702f0
	sys.subversion   = ('CPython', '', '')
	sys.api_version  = 1013

.. {{{end}}}

The operating system platform used to build the interpreter is saved
as :const:`sys.platform`.

.. include:: sys_platform.py
    :literal:
    :start-after: #end_pymotw_header

For most Unix systems, the value comes from combining the output of
``uname -s`` with the first part of the version in ``uname -r``. For
other operating systems there is a `hard-coded table of values
<http://docs.python.org/library/sys.html#sys.platform>`_.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sys_platform.py'))
.. }}}

::

	$ python sys_platform.py
	
	This interpreter was built for: darwin

.. {{{end}}}

.. _sys-prefix:

Install Location
================

The path to the actual interpreter program is available in
:const:`sys.executable` on all systems for which having a path to the
interpreter makes sense.  This can be useful for ensuring that the
*correct* interpreter is being used, and also gives clues about paths
that might be set based on the interpreter location.

:const:`sys.prefix` refers to the parent directory of the interpreter
installation.  It usually includes ``bin`` and ``lib`` directories for
executables and installed modules, respectively.

.. include:: sys_locations.py
    :literal:
    :start-after: #end_pymotw_header

.. note:: 

  This example output was produced on a Mac running a framework build
  installed from python.org.  Other versions may produce different
  path information, even on a Mac.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sys_locations.py'))
.. }}}

::

	$ python sys_locations.py
	
	Interpreter executable: /Users/dhellmann/Envs/pymotw/bin/python
	Installation prefix   : /Users/dhellmann/Envs/pymotw/bin/..

.. {{{end}}}


Command Line Options
====================

The CPython interpreter accepts several command line options to
control its behavior.

.. {{{cog
.. cog.out(run_script(cog.inFile, '-h'))
.. }}}

::

	$ python -h
	
	usage: python [option] ... [-c cmd | -m mod | file | -] [arg] ...
	Options and arguments (and corresponding environment variables):
	-B     : don't write .py[co] files on import; also PYTHONDONTWRITEBYTECODE=x
	-c cmd : program passed in as string (terminates option list)
	-d     : debug output from parser; also PYTHONDEBUG=x
	-E     : ignore PYTHON* environment variables (such as PYTHONPATH)
	-h     : print this help message and exit (also --help)
	-i     : inspect interactively after running script; forces a prompt even
	         if stdin does not appear to be a terminal; also PYTHONINSPECT=x
	-m mod : run library module as a script (terminates option list)
	-O     : optimize generated bytecode slightly; also PYTHONOPTIMIZE=x
	-OO    : remove doc-strings in addition to the -O optimizations
	-Q arg : division options: -Qold (default), -Qwarn, -Qwarnall, -Qnew
	-s     : don't add user site directory to sys.path; also PYTHONNOUSERSITE
	-S     : don't imply 'import site' on initialization
	-t     : issue warnings about inconsistent tab usage (-tt: issue errors)
	-u     : unbuffered binary stdout and stderr; also PYTHONUNBUFFERED=x
	         see man page for details on internal buffering relating to '-u'
	-v     : verbose (trace import statements); also PYTHONVERBOSE=x
	         can be supplied multiple times to increase verbosity
	-V     : print the Python version number and exit (also --version)
	-W arg : warning control; arg is action:message:category:module:lineno
	         also PYTHONWARNINGS=arg
	-x     : skip first line of source, allowing use of non-Unix forms of #!cmd
	-3     : warn about Python 3.x incompatibilities that 2to3 cannot trivially fix
	file   : program read from script file
	-      : program read from stdin (default; interactive mode if a tty)
	arg ...: arguments passed to program in sys.argv[1:]
	
	Other environment variables:
	PYTHONSTARTUP: file executed on interactive startup (no default)
	PYTHONPATH   : ':'-separated list of directories prefixed to the
	               default module search path.  The result is sys.path.
	PYTHONHOME   : alternate <prefix> directory (or <prefix>:<exec_prefix>).
	               The default module search path uses <prefix>/pythonX.X.
	PYTHONCASEOK : ignore case in 'import' statements (Windows).
	PYTHONIOENCODING: Encoding[:errors] used for stdin/stdout/stderr.

.. {{{end}}}

Some of these are available for programs to check through
:const:`sys.flags`.

.. include:: sys_flags.py
    :literal:
    :start-after: #end_pymotw_header

Experiment with ``sys_flags.py`` to learn how the command line options
map to the flags settings.

.. {{{cog
.. cog.out(run_script(cog.inFile, '-3 -S -E sys_flags.py'))
.. }}}

::

	$ python -3 -S -E sys_flags.py
	
	Warning about Python 3.x incompatibilities
	Warning about division change
	Not importing "site"
	Ignoring environment
	Checking for mixed tabs and spaces

.. {{{end}}}


.. _sys-unicode-defaults:

Unicode Defaults
================

To get the name of the default Unicode encoding being used by the
interpreter, use :func:`getdefaultencoding`.  The value is set during
startup by :mod:`site`, which calls :func:`sys.setdefaultencoding` and
then removes it from the namespace in :mod:`sys` to avoid having it
called again.

The internal encoding default and the filesystem encoding may be
different for some operating systems, so there is a separate way to
retrieve the filesystem setting.  :func:`getfilesystemencoding`
returns an OS-specific (*not* filesystem-specific) value.

.. include:: sys_unicode.py
    :literal:
    :start-after: #end_pymotw_header

Rather than changing the global default encoding, most Unicode experts
recommend making an application explicitly Unicode-aware. This
provides two benefits: Different Unicode encodings for different data
sources can be handled more cleanly, and the number of assumptions
about encodings in the application code is reduced.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sys_unicode.py'))
.. }}}

::

	$ python sys_unicode.py
	
	Default encoding    : ascii
	Filesystem encoding : utf-8

.. {{{end}}}


Interactive Prompts
===================

The interactive interpreter uses two separate prompts for indicating
the default input level (:data:`ps1`) and the "continuation" of a
multi-line statement (:data:`ps2`).  The values are only used by the
interactive interpreter.

::

    >>> import sys
    >>> sys.ps1
    '>>> '
    >>> sys.ps2
    '... '
    >>>

Either or both prompt can be changed to a different string

::

    >>> sys.ps1 = '::: '
    ::: sys.ps2 = '~~~ '
    ::: for i in range(3):
    ~~~   print i
    ~~~ 
    0
    1
    2
    ::: 

Alternately, any object that can be converted to a string (via
``__str__``) can be used for the prompt.

.. include:: sys_ps1.py
    :literal:
    :start-after: #end_pymotw_header

The :class:`LineCounter` keeps track of how many times it has been
used, so the number in the prompt increases each time.

::

    $ python
    Python 2.6.2 (r262:71600, Apr 16 2009, 09:17:39)
    [GCC 4.0.1 (Apple Computer, Inc. build 5250)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from PyMOTW.sys.sys_ps1 import LineCounter
    >>> import sys
    >>> sys.ps1 = LineCounter()
    (  1)>
    (  2)>
    (  3)>

Display Hook
============

:data:`sys.displayhook` is invoked by the interactive interpreter each
time the user enters an expression.  The *result* of the expression is
passed as the only argument to the function.  

.. include:: sys_displayhook.py
    :literal:
    :start-after: #end_pymotw_header

The default value (saved in :data:`sys.__displayhook__`) prints the
result to stdout and saves it in :data:`__builtin__._` for easy
reference later.

::

    $ python 
    Python 2.6.2 (r262:71600, Apr 16 2009, 09:17:39) 
    [GCC 4.0.1 (Apple Computer, Inc. build 5250)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import PyMOTW.sys.sys_displayhook
    installing
    >>> 1+2

      Previous: <PyMOTW.sys.sys_displayhook.ExpressionCounter object at 0x9c5f90>
      New     : 3

    3
    (  1)> 'abc'

      Previous: 3
      New     : abc

    'abc'
    (  2)> 'abc'

      Previous: abc
      New     : abc

    'abc'
    (  2)> 'abc' * 3

      Previous: abc
      New     : abcabcabc

    'abcabcabc'
    (  3)>
