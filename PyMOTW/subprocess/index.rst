==============================================================
subprocess -- Spawn and communicate with additional processes.
==============================================================

.. module:: subprocess
    :synopsis: Spawn and communicate with additional processes.

:Purpose: Spawn and communicate with additional processes.
:Python Version: New in 2.4

The :mod:`subprocess` module provides a consistent interface to
creating and working with additional processes. It offers a
higher-level interface than some of the other available modules, and
is intended to replace functions such as :func:`os.system`,
:func:`os.spawn*`, :func:`os.popen*`, :func:`popen2.*` and
:func:`commands.*`. To make it easier to compare subprocess with those
other modules, the examples here re-create those used for
:mod:`os` and :mod:`popen`.

The :mod:`subprocess` module defines one class, :class:`Popen` and a
few wrapper functions which use that class. The constructor for
:class:`Popen` takes several arguments to make it easier to set up the
new process, and then communicate with it via pipes. I will
concentrate on example code here; for a complete description of the
arguments, refer to section 17.1.1 of the library documentation.

.. note::

    The API is roughly the same, but the underlying implementation is
    slightly different between Unix and Windows. All of the examples
    shown here were tested on Mac OS X. Your mileage on a non-Unix OS
    will vary.

Running External Command
========================

To run an external command without interacting with it, such as one
would do with :ref:`os.system() <os-system>`, Use the :func:`call()`
function.

.. include:: subprocess_os_system.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'subprocess_os_system.py'))
.. }}}

::

	$ python subprocess_os_system.py
	__init__.py
	index.rst
	interaction.py
	repeater.py
	signal_child.py
	signal_parent.py
	subprocess_os_system.py
	subprocess_pipes.py
	subprocess_popen2.py
	subprocess_popen3.py
	subprocess_popen4.py
	subprocess_popen_read.py
	subprocess_popen_write.py
	subprocess_shell_variables.py
	subprocess_signal_parent_shell.py
	subprocess_signal_setsid.py

.. {{{end}}}

When *shell* is set to ``True``, shell variables in the command
string are expanded:

.. include:: subprocess_shell_variables.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'subprocess_shell_variables.py'))
.. }}}

::

	$ python subprocess_shell_variables.py
	Desktop
	Documents
	Download
	MailAttach
	Music
	Pictures
	Public
	Templates
	Videos
	bin
	dev
	kanri
	pkgs
	rpmbuild
	tmp
	work

.. {{{end}}}

Working with Pipes
==================

By passing different arguments for *stdin*, *stdout*, and *stderr* it
is possible to mimic the variations of :func:`os.popen()`.

popen
-----

Reading from the output of a pipe:

.. include:: subprocess_popen_read.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, '-u subprocess_popen_read.py'))
.. }}}

::

	$ python -u subprocess_popen_read.py
	
	read:
		stdout: '\n'

.. {{{end}}}


Writing to the input of a pipe:

.. include:: subprocess_popen_write.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, '-u subprocess_popen_write.py'))
.. }}}

::

	$ python -u subprocess_popen_write.py
	
	write:
		stdin: to stdin

.. {{{end}}}

popen2
------

Reading and writing, as with popen2:

.. include:: subprocess_popen2.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, '-u subprocess_popen2.py'))
.. }}}

::

	$ python -u subprocess_popen2.py
	
	popen2:
		pass through: 'through stdin to stdout'

.. {{{end}}}

popen3
------

Separate streams for stdout and stderr, as with popen3:

.. include:: subprocess_popen3.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, '-u subprocess_popen3.py'))
.. }}}

::

	$ python -u subprocess_popen3.py
	
	popen3:
		pass through: 'through stdin to stdout'
		stderr: ';to stderr\n'

.. {{{end}}}

popen4
------

Merged stdout and stderr, as with popen4:

.. include:: subprocess_popen4.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, '-u subprocess_popen4.py'))
.. }}}

::

	$ python -u subprocess_popen4.py
	
	popen4:
		combined output: 'through stdin to stdout\n;to stderr\n'

.. {{{end}}}

Connecting Segments of a Pipe
=============================

By creating separate Popen instances and chaining their inputs and outputs
together, you can create your own pipeline of commands just as with the
Unix shell.

.. include:: subprocess_pipes.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, '-u subprocess_pipes.py'))
.. }}}

::

	$ python -u subprocess_pipes.py
	Included files:
		subprocess_os_system.py
		subprocess_shell_variables.py
		subprocess_popen_read.py
		subprocess_popen_write.py
		subprocess_popen2.py
		subprocess_popen3.py
		subprocess_popen4.py
		subprocess_pipes.py
		repeater.py
		interaction.py
		signal_child.py
		signal_parent.py
		subprocess_signal_parent_shell.py
		subprocess_signal_setsid.py

.. {{{end}}}



Interacting with Another Command
================================

All of the above examples assume a limited amount of interaction. The
:func:`communicate()` method reads all of the output and waits for
child process to exit before returning. It is also possible to write
to and read from the individual pipe handles used by the
:class:`Popen` instance. A simple echo program that reads from
standard input and writes to standard output illustrates this:

.. include:: repeater.py
    :literal:
    :start-after: #end_pymotw_header

Make note of the fact that ``repeater.py`` writes to stderr when it
starts and stops. That information can be used to show the lifetime of
the child process. 

The next interaction example uses the stdin and stdout file handles
owned by the :class:`Popen` instance in different ways. In the first
example, a sequence of 10 numbers are written to stdin of the process,
and after each write the next line of output is read back. In the
second example, the same 10 numbers are written but the output is read
all at once using :func:`communicate()`.

.. include:: interaction.py
    :literal:
    :start-after: #end_pymotw_header


Notice where the ``"repeater.py: exiting"`` lines fall in the output
for each loop:

.. {{{cog
.. cog.out(run_script(cog.inFile, '-u interaction.py'))
.. }}}

::

	$ python -u interaction.py
	One line at a time:
	repeater.py: starting
	0
	1
	2
	3
	4
	5
	6
	7
	8
	9
	repeater.py: exiting
	
	
	All output at once:
	repeater.py: starting
	repeater.py: exiting
	0
	1
	2
	3
	4
	5
	6
	7
	8
	9
	

.. {{{end}}}


Signaling Between Processes
===========================

The :mod:`os` examples include a demonstration of :ref:`signaling
between processes using os.fork() and os.kill()
<creating-processes-with-os-fork>`. Since each :class:`Popen` instance
provides a *pid* attribute with the process id of the child process,
it is possible to do something similar with :mod:`subprocess`. For
example, using this script for the child process to be executed by the
parent process:

.. include:: signal_child.py
    :literal:
    :start-after: #end_pymotw_header

and this parent process:

.. include:: signal_parent.py
    :literal:
    :start-after: #end_pymotw_header

the output will look something like:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'signal_parent.py'))
.. }}}

::

	$ python signal_parent.py
	PARENT: Pausing before sending signal...
	CHILD 5744: Setting up signal handler
	CHILD 5744: Pausing to wait for signal
	PARENT: Signaling child
	CHILD 5744: Received USR1

.. {{{end}}}

.. _subprocess-process-groups:

Process Groups / Sessions
-------------------------

Because of the way the process tree works under Unix, if the process
created by :mod:`Popen` spawns sub-processes, those children will not
receive any signals sent to the parent.  That means, for example, it
will be difficult to cause them to terminate by sending ``SIGINT`` or
``SIGTERM``.

.. include:: subprocess_signal_parent_shell.py
    :literal:
    :start-after: #end_pymotw_header

Notice that the pid used to send the signal is different from the pid
of the child of the shell script waiting for the signal because in
this example, there are three separate processes interacting:

1. ``subprocess_signal_parent_shell.py``
2. a Unix shell process running the script created by the main python
   program
3. ``signal_child.py``

.. {{{cog
.. cog.out(run_script(cog.inFile, 'subprocess_signal_parent_shell.py'))
.. }}}

::

	$ python subprocess_signal_parent_shell.py
	PARENT: Pausing before sending signal to child 5747...
	Shell script in process 5747
	+ python signal_child.py
	CHILD 5748: Setting up signal handler
	CHILD 5748: Pausing to wait for signal
	PARENT: Signaling child 5747
	CHILD 5748: Never received signal

.. {{{end}}}

The solution to this problem is to use a *process group* to associate
the children so they can be signaled together.  The process group is
created with ``os.setsid()``, setting the "session id" to the process
id of the current process.  All child processes inherit the session
id, and since we only want it set in the shell created by
:class:`Popen` and its descendants we don't call it in the parent
process.  Instead, we pass it to Popen as the *preexec_fn* argument so
it is run after the ``fork()`` inside the new process, before it calls
``exec()``.

.. include:: subprocess_signal_setsid.py
    :literal:
    :start-after: #end_pymotw_header

To signal the entire process group, we use ``os.killpg()`` with the
pid value from our :class:`Popen` instance.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'subprocess_signal_setsid.py'))
.. }}}

::

	$ python subprocess_signal_setsid.py
	PARENT: Pausing before sending signal to child 5751...
	Shell script in process 5751
	+ python signal_child.py
	CHILD 5752: Setting up signal handler
	CHILD 5752: Pausing to wait for signal
	PARENT: Signaling process group 5751
	CHILD 5752: Received USR1

.. {{{end}}}


Conclusions
===========

As you can see, :mod:`subprocess` can be much easier to work with than
fork, exec, and pipes on their own. It provides all of the
functionality of the other modules and functions it replaces, and
more. The API is consistent for all uses and many of the extra steps
of overhead needed (such as closing extra file descriptors, ensuring
the pipes are closed, etc.) are "built in" instead of being handled by
your code separately.


.. seealso::

    `subprocess <http://docs.python.org/lib/module-subprocess.html>`_
        Standard library documentation for this module.

    :mod:`os`
        Although many are deprecated, the functions for working with processes
        found in the os module are still widely used in existing code.

    `UNIX SIgnals and Process Groups <http://www.frostbytes.com/~jimf/papers/signals/signals.html>`_
        A good description of UNIX signaling and how process groups work.


    `Advanced Programming in the UNIX(R) Environment <http://www.amazon.com/Programming-Environment-Addison-Wesley-Professional-Computing/dp/0201433079/ref=pd_bbs_3/002-2842372-4768037?ie=UTF8&s=books&amp;qid=1182098757&sr=8-3>`_
        Covers working with multiple processes, such as handling signals, closing duplicated
        file descriptors, etc.

    :mod:`pipes`
        Unix shell command pipeline templates in the standard library.
