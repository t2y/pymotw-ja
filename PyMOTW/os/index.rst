============================================================
os -- Portable access to operating system specific features.
============================================================

.. module:: os
    :synopsis: Portable access to operating system specific features.

:Purpose: Portable access to operating system specific features.
:Python Version: 1.4 (or earlier)

The :mod:`os` module provides a wrapper for platform specific modules
such as :mod:`posix`, :mod:`nt`, and :mod:`mac`. The API for functions
available on all platform should be the same, so using the os module
offers some measure of portability. Not all functions are available on
all platforms, however. Many of the process management functions
described in this summary are not available for Windows.

The Python documentation for the os module is subtitled "Miscellaneous
operating system interfaces". The module includes mostly functions for
creating and managing running processes or filesystem content (files
and directories), with a few other random bits of functionality thrown
in besides.

.. note::

    Some of the example code below will only work on Unix-like
    operating systems.

Process Owner
=============

The first set of functions to cover are used for determining and
changing the process owner ids. These are mostly useful to authors of
daemons or special system programs which need to change permission
level rather than running as ``root``. I won't try to explain all of
the intricate details of Unix security, process owners, etc. in this
brief post. See the References list below for more details.

Let's start with a script to show the real and effective user and
group information for a process, and then change the effective
values. This is similar to what a daemon would need to do when it
starts as root during a system boot, to lower the privilege level and
run as a different user. If you download the examples to try them out,
you should change the ``TEST_GID`` and ``TEST_UID`` values to match
your user.

.. include:: os_process_user_example.py
    :literal:
    :start-after: #end_pymotw_header

When run as myself (527, 501) on OS X, I see this output:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'os_process_user_example.py'))
.. }}}

::

	$ python os_process_user_example.py
	BEFORE CHANGE:
	Effective User  : 500
	Effective Group : 500
	Actual User     : 500 morimoto
	Actual Group    : 500
	Actual Groups   : [10, 500]
	
	ERROR: Could not change effective group.  Re-run as root.
	ERROR: Could not change effective user.  Re-run as root.

.. {{{end}}}

Notice that the values do not change. Since I am not running as root,
processes I start cannot change their effective owner values. If I do try to
set the effective user id or group id to anything other than my own, an
OSError is raised.

Now let's look at what happens when we run the same script using
``sudo`` to start out with root privileges:

.. Don't use cog here because sudo sometimes asks for a password.

::

	$ sudo python os_process_user_example.py
	BEFORE CHANGE:
	Effective User  : 0
	Effective Group : 0
	Actual User	 : 0 dhellmann
	Actual Group	: 0
	Actual Groups   : [0, 1, 2, 8, 29, 3, 9, 4, 5, 80, 20]
	
	CHANGED GROUP:
	Effective User  : 0
	Effective Group : 501
	Actual User	 : 0 dhellmann
	Actual Group	: 0
	Actual Groups   : [501, 1, 2, 8, 29, 3, 9, 4, 5, 80, 20]
	
	CHANGE USER:
	Effective User  : 527
	Effective Group : 501
	Actual User	 : 0 dhellmann
	Actual Group	: 0
	Actual Groups   : [501, 1, 2, 8, 29, 3, 9, 4, 5, 80, 20]
	

In this case, since we start as root, we can change the effective user and
group for the process. Once we change the effective UID, the process is
limited to the permissions of that user. Since non-root users cannot change
their effective group, we need to change the group first then the user.

Besides finding and changing the process owner, there are functions for
determining the current and parent process id, finding and changing the
process group and session ids, as well as finding the controlling terminal id.
These can be useful for sending signals between processes or for complex
applications such as writing your own command line shell.

Process Environment
===================

Another feature of the operating system exposed to your program though
the os module is the environment. Variables set in the environment are
visible as strings that can be read through ``os.environ`` or
:func:`os.getenv()`. Environment variables are commonly used for
configuration values such as search paths, file locations, and debug
flags. Let's look at an example of retrieving an environment variable,
and passing a value through to a child process.

.. include:: os_environ_example.py
    :literal:
    :start-after: #end_pymotw_header


The ``os.environ`` object follows the standard Python mapping API for
retrieving and setting values. Changes to ``os.environ`` are exported
for child processes.

.. {{{cog
.. cog.out(run_script(cog.inFile, '-u os_environ_example.py'))
.. }}}

::

	$ python -u os_environ_example.py
	Initial value: None
	Child process:
	
	
	Changed value: THIS VALUE WAS CHANGED
	Child process:
	THIS VALUE WAS CHANGED
	
	Removed value: None
	Child process:
	

.. {{{end}}}


Process Working Directory
=========================

The notion of the "current working directory" for a process is a
concept from operating systems with hierarchical filesystems.  This is
the directory on the filesystem the process uses as the starting
location when files are accessed with relative paths.

.. include:: os_cwd_example.py
    :literal:
    :start-after: #end_pymotw_header

Note the use of ``os.curdir`` and ``os.pardir`` to refer to the
current and parent directories in a portable manner. The output should
not be surprising:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'os_cwd_example.py'))
.. }}}

::

	$ python os_cwd_example.py
	Starting: /home/morimoto/work/translate/02_pymotw/pymotw-ja/PyMOTW/os
	['os_directories.py', 'os_spawn_example.py', 'os_popen4.py', 'os_popen.py', 'os_popen2_seq.py', 'os_popen3.py', 'os_access.py', 'os_stat_chmod_example.txt', 'os_process_user_example.py', 'os_process_id_example.py', 'os_system_shell.py', 'os_exec_example.py', 'os_popen2.py', '__init__.py', 'os_stat.py', 'index.rst', 'os_environ_example.py', 'os_waitpid_example.py', 'os_kill_example.py', 'os_walk.py', 'os_stat_chmod.py', 'os_system_background.py', 'os_cwd_example.py', 'os_wait_example.py', 'os_system_example.py', 'os_fork_example.py', 'os_symlinks.py']
	Moving up one: ..
	After move: /home/morimoto/work/translate/02_pymotw/pymotw-ja/PyMOTW
	['mail.png', 'unittest', 'locale', 'datetime', 'decimal', 'warnings', 'pyclbr', 'urlparse', 'asynchat', 'hmac', 'internet_data.rst', 'shlex', 'optparse', 'threading', 'traceback', 'sys', 'cmd', 'struct', 'uuid', 'numeric.rst', 'robotparser', 'profilers.rst', 'operator', 'Queue', 'heapq', 'BaseHTTPServer', 'mhlib', 'rlcompleter', 'calendar', 'StringIO', 'plistlib', 'hashlib', 'shelve', 'feed.png', 'shutil', 'ipc.rst', 'zipfile', 'internet_protocols.rst', 'linecache', 'optional_os.rst', 'abc', 'base64', 'gzip', 'tabnanny', 'whichdb', 'file_formats.rst', 'cryptographic.rst', 'xml', 'miscelaneous.rst', 'profile', 'signal', 'grp', 'subprocess', 'csv', 'SocketServer', 'fractions', 'anydbm', 'pipes', 'inspect', 'builtins.rst', 'copyright.rst', 'logging', 'pickle', 'weakref', 'pdf_contents.rst', '__init__.py', '__init__.pyc', 'difflib', 'generic_os.rst', 'pkgutil', 'runtime_services.rst', 'glob', 'smtpd', 'site', 'getpass', 'imp', 'compileall', 'pydoc', 'sched', 'unix.rst', 'file_access.rst', 'ConfigParser', 'xmlrpclib', 'language.rst', 'bisect', 'about.rst', 'mmap', 'urllib', 'pprint', 'collections', 'dev_tools.rst', 'gettext', 'dircache', 'cc-by-nc-sa.png', 'data_types.rst', 'markup.rst', 'fnmatch', 'SimpleXMLRPCServer', 'readline', 'importing.rst', 'time', 'fileinput', 'dumbdbm', 'Cookie', 'array', 'tempfile', 'articles', 'bz2', 'gdbm', 'exceptions', 'contextlib', 'history.rst', 'smtplib', 'tarfile', 'string_services.rst', 'dis', 'compression.rst', 'webbrowser', 'multiprocessing', 'dbm', 'contents.rst', 'pwd', 'itertools', 'urllib2', 'os', 'platform', 'EasyDialogs', 'zipimport', 'gc', 'ospath', 'asyncore', 'timeit', 'resource', 'atexit', 'json', 'i18n.rst', 'filecmp', 'cgitb', 'copy', 'frameworks.rst', 'textwrap', 'getopt', 'string', 'persistence.rst', 'commands', 'dbhash', 'mailbox', 'functools', 'imaplib', 'trace', 'zlib']

.. {{{end}}}


Pipes
=====

The :mod:`os` module provides several functions for managing the I/O
of child processes using *pipes*. The functions all work essentially
the same way, but return different file handles depending on the type
of input or output desired. For the most part, these functions are
made obsolete by the :mod:`subprocess` module (added in Python 2.4),
but there is a good chance you will encounter them if you are
maintaining legacy code.

The most commonly used pipe function is :func:`popen()`. It creates a
new process running the command given and attaches a single stream to
the input or output of that process, depending on the mode
argument. While :func:`popen` functions work on Windows, some of these
examples assume some sort of Unix-like shell. The descriptions of the
streams also assume Unix-like terminology:

* stdin - The "standard input" stream for a process (file descriptor 0) is
  readable by the process. This is usually where terminal input goes.

* stdout - The "standard output" stream for a process (file descriptor
  1) is writable by the process, and is used for displaying regular
  output to the user.

* stderr - The "standard error" stream for a process (file descriptor 2) is
  writable by the process, and is used for conveying error messages.

.. include:: os_popen.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, '-u os_popen.py'))
.. }}}

::

	$ python -u os_popen.py
	popen, read:
		stdout: 'to stdout\n'
	
	popen, write:
		stdin: to stdin

.. {{{end}}}

The caller can only read from or write to the streams associated with
the child process, which limits the usefulness. The other
:func:`popen` variants provide additional streams so it is possible to
work with stdin, stdout, and stderr as needed.

For example, :func:`popen2()` returns a write-only stream attached to
stdin of the child process, and a read-only stream attached to its
stdout.

.. include:: os_popen2.py
    :literal:
    :start-after: #end_pymotw_header


This simplistic example illustrates bi-directional communication. The
value written to stdin is read by ``cat`` (because of the ``'-'``
argument), then written back to stdout. Obviously a more complicated
process could pass other types of messages back and forth through the
pipe; even serialized objects.

.. {{{cog
.. cog.out(run_script(cog.inFile, '-u os_popen2.py'))
.. }}}

::

	$ python -u os_popen2.py
	popen2:
		pass through: 'through stdin to stdout'

.. {{{end}}}

In most cases, it is desirable to have access to both stdout and
stderr. The stdout stream is used for message passing and the stderr
stream is used for errors, so reading from it separately reduces the
complexity for parsing any error messages. The :func:`popen3()`
function returns 3 open streams tied to stdin, stdout, and stderr of
the new process.

.. include:: os_popen3.py
    :literal:
    :start-after: #end_pymotw_header

Notice that we have to read from and close both stdout and stderr
*separately*. There are some related to flow control and sequencing
when dealing with I/O for multiple processes. The I/O is buffered, and
if the caller expects to be able to read all of the data from a stream
then the child process must close that stream to indicate the
end-of-file. For more information on these issues, refer to the `Flow
Control Issues
<http://docs.python.org/library/popen2.html#popen2-flow-control>`__
section of the Python library documentation.

.. {{{cog
.. cog.out(run_script(cog.inFile, '-u os_popen3.py'))
.. }}}

::

	$ python -u os_popen3.py
	popen3:
		pass through: 'through stdin to stdout'
		stderr: ';to stderr\n'

.. {{{end}}}

And finally, :func:`popen4()` returns 2 streams, stdin and a merged
stdout/stderr.  This is useful when the results of the command need to
be logged, but not parsed directly.

.. include:: os_popen4.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, '-u os_popen4.py'))
.. }}}

::

	$ python -u os_popen4.py
	popen4:
		combined output: 'through stdin to stdout;to stderr\n'

.. {{{end}}}

Besides accepting a single string command to be given to the shell for
parsing, :func:`popen2()`, :func:`popen3()`, and :func:`popen4()` also
accept a sequence of strings (command, followed by arguments). In this
case, the arguments are not processed by the shell.

.. include:: os_popen2_seq.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, '-u os_popen2_seq.py'))
.. }}}

::

	$ python -u os_popen2_seq.py
	popen2, cmd as sequence:
		pass through: 'through stdin to stdout'

.. {{{end}}}


File Descriptors
================

:mod:`os` includes the standard set of functions for working with
low-level *file descriptors* (integers representing open files owned
by the current process). This is a lower-level API than is provided by
:class:`file` objects. I am going to skip over describing them here,
since it is generally easier to work directly with :class:`file`
objects. Refer to the library documentation for details if you do need
to use file descriptors.

Filesystem Permissions
======================

The function :func:`os.access()` can be used to test the access rights a
process has for a file.

.. include:: os_access.py
    :literal:
    :start-after: #end_pymotw_header

Your results will vary depending on how you install the example code, but it
should look something like this:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'os_access.py'))
.. }}}

::

	$ python os_access.py
	Testing: os_access.py
	Exists: True
	Readable: True
	Writable: True
	Executable: False

.. {{{end}}}


The library documentation for :func:`os.access()` includes two special
warnings. First, there isn't much sense in calling :func:`os.access()`
to test whether a file can be opened before actually calling
:func:`open()` on it. There is a small, but real, window of time
between the two calls during which the permissions on the file could
change. The other warning applies mostly to networked filesystems that
extend the POSIX permission semantics. Some filesystem types may
respond to the POSIX call that a process has permission to access a
file, then report a failure when the attempt is made using
:func:`open()` for some reason not tested via the POSIX call. All in
all, it is better to call :func:`open()` with the required mode and
catch the :ref:`IOError <exceptions-IOError>` raised if there is a
problem.

More detailed information about the file can be accessed using
:func:`os.stat()` or :func:`os.lstat()` (if you want the status of
something that might be a symbolic link).

.. include:: os_stat.py
    :literal:
    :start-after: #end_pymotw_header

Once again, your results will vary depending on how the example code
was installed. Try passing different filenames on the command line to
``os_stat.py``.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'os_stat.py'))
.. }}}

::

	$ python os_stat.py
	os.stat(os_stat.py):
		Size: 1516
		Permissions: 0100664
		Owner: 500
		Device: 2053
		Last modified: Mon Jul 12 18:49:33 2010

.. {{{end}}}


On Unix-like systems, file permissions can be changed using
:func:`os.chmod()`, passing the mode as an integer. Mode values can be
constructed using constants defined in the :mod:`stat` module. Here is
an example which toggles the user's execute permission bit:

.. include:: os_stat_chmod.py
    :literal:
    :start-after: #end_pymotw_header


The script assumes you have the permissions necessary to modify the
mode of the file to begin with:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'os_stat_chmod.py'))
.. }}}

::

	$ python os_stat_chmod.py
	Adding execute permission

.. {{{end}}}

.. _os-directories:

Directories
===========

There are several functions for working with directories on the filesystem,
including creating, listing contents, and removing them.

.. include:: os_directories.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'os_directories.py'))
.. }}}

::

	$ python os_directories.py
	Creating os_directories_example
	Creating os_directories_example/example.txt
	Listing os_directories_example
	['example.txt']
	Cleaning up

.. {{{end}}}


There are two sets of functions for creating and deleting
directories. When creating a new directory with :func:`os.mkdir()`,
all of the parent directories must already exist. When removing a
directory with :func:`os.rmdir()`, only the leaf directory (the last
part of the path) is actually removed. In contrast,
:func:`os.makedirs()` and :func:`os.removedirs()` operate on all of
the nodes in the path.  :func:`os.makedirs()` will create any parts of
the path which do not exist, and :func:`os.removedirs()` will remove
all of the parent directories (assuming it can).

Symbolic Links
==============

For platforms and filesystems which support them, there are functions
for working with symlinks.

.. include:: os_symlinks.py
    :literal:
    :start-after: #end_pymotw_header


Although :mod:`os` includes :func:`os.tempnam()` for creating
temporary filenames, it is not as secure as the :mod:`tempfile` module
and produces a :ref:`RuntimeWarning <exceptions-RuntimeWarning>`
message when it is used. In general it is better to use
:mod:`tempfile`, as in this example.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'os_symlinks.py'))
.. }}}

::

	$ python os_symlinks.py
	Creating link /tmp/tmp6T1GX9 -> os_symlinks.py
	Permissions: 0120777
	Points to: os_symlinks.py

.. {{{end}}}


Walking a Directory Tree
========================

The function :func:`os.walk()` traverses a directory recursively and
for each directory generates a tuple containing the directory path,
any immediate sub-directories of that path, and the names of any files
in that directory.  This example shows a simplistic recursive
directory listing.

.. include:: os_walk.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'os_walk.py'))
.. }}}

::

	$ python os_walk.py
	
	/tmp
		.ICE-unix/
		.X0-lock
		.X11-unix/
		.esd-500/
		3659_02-0115.txt
		4AO3EV.tmp
		75HYEV.tmp
		Excel2007BinaryFileFormat(xlsb)Specification.pdf
		bkup.log
		dhklf008.tgz
		dirs-0KTOFV
		dirs-28UUFV
		dirs-5CSDFV
		dirs-62HUEV
		dirs-6JBKFV
		dirs-73MBEV
		dirs-7P7RDV
		dirs-AKCMFV
		dirs-AMF9EV
		dirs-CARSFV
		dirs-EVQGFV
		dirs-G3YFFV
		dirs-G7OHEV
		dirs-IANEFV
		dirs-IVZ7DV
		dirs-J8SREV
		dirs-JVGAFV
		dirs-K4SMEV
		dirs-KM7ZFV
		dirs-LN8MEV
		dirs-M2R8EV
		dirs-M9OHEV
		dirs-NP95DV
		dirs-ORRHDV
		dirs-QOCVEV
		dirs-RO2GEV
		dirs-S0TWEV
		dirs-U53HDV
		dirs-VHBRDV
		dirs-YPW1DV
		dirs-ZFHPEV
		django.po
		djangojs.po
		dmfxlibmlver3.doc
		dmfxlibver3.doc
		example.db
		hosts
		kde-morimoto/
		keyring-NNmbf2/
		keyring-qoDG37/
		ksocket-morimoto/
		nsmail-1.asc
		nsmail-2.asc
		orbit-morimoto/
		plugtmp-1/
		plugtmp/
		pulse-uXTDCdjuejPW/
		pymotw_import_example.shelve
		scim-helper-manager-socket-morimoto
		scim-panel-socket:0-morimoto
		scim-socket-frontend-morimoto
		sphinx-err-1j4tOo.log
		sphinx-err-2emfzd.log
		sphinx-err-2vIYM7.log
		sphinx-err-68_vWW.log
		sphinx-err-7bn26G.log
		sphinx-err-9YxfTg.log
		sphinx-err-AkPXqU.log
		sphinx-err-B6nIVr.log
		sphinx-err-BhIGyy.log
		sphinx-err-CHBG5d.log
		sphinx-err-DbJGW6.log
		sphinx-err-E4rP0z.log
		sphinx-err-FpjRCb.log
		sphinx-err-GX7aTs.log
		sphinx-err-Mat86d.log
		sphinx-err-O5B2V_.log
		sphinx-err-R78Fqn.log
		sphinx-err-Rlu__E.log
		sphinx-err-UJhDOd.log
		sphinx-err-VRQ2FL.log
		sphinx-err-_W2ccO.log
		sphinx-err-aTHJDM.log
		sphinx-err-bOdk1X.log
		sphinx-err-dOVkWv.log
		sphinx-err-dZIo1p.log
		sphinx-err-dg4xGX.log
		sphinx-err-fD9qaA.log
		sphinx-err-gEqdhj.log
		sphinx-err-gLHw0q.log
		sphinx-err-h4zdqz.log
		sphinx-err-i9n7cC.log
		sphinx-err-jHZNpP.log
		sphinx-err-jg9ZEJ.log
		sphinx-err-jj3ld1.log
		sphinx-err-ke6Yfj.log
		sphinx-err-l2jixV.log
		sphinx-err-mECiSc.log
		sphinx-err-o9Q6G4.log
		sphinx-err-rxOeos.log
		sphinx-err-tACpKT.log
		sphinx-err-u1Da67.log
		ssh-NHRlfb2285/
		ssh-zRKFQQ2189/
		trace_example.recurse.cover
		tracker-morimoto/
		virtual-morimoto.26mNh3/
		virtual-morimoto.FWbKZy/
		virtual-morimoto.NUY9DD/
		virtual-morimoto.NfSC6x/
		virtual-morimoto.RDLY7B/
		virtual-morimoto.vPtnVs/
		vmware-temp/
	
	/tmp/virtual-morimoto.FWbKZy
	
	/tmp/pulse-uXTDCdjuejPW
		native
		pid
	
	/tmp/virtual-morimoto.NUY9DD
	
	/tmp/.ICE-unix
		2189
	
	/tmp/virtual-morimoto.NfSC6x
	
	/tmp/tracker-morimoto
		Attachments/
		cache.db
		morimoto_tracker_lock
	
	/tmp/tracker-morimoto/Attachments
	
	/tmp/virtual-morimoto.26mNh3
	
	/tmp/plugtmp-1
	
	/tmp/ssh-zRKFQQ2189
		agent.2189
	
	/tmp/keyring-NNmbf2
		socket
		socket.pkcs11
		socket.ssh
	
	/tmp/vmware-temp
		vmware-root/
	
	/tmp/keyring-qoDG37
		socket
		socket.pkcs11
		socket.ssh
	
	/tmp/.X11-unix
		X0
	
	/tmp/plugtmp
	
	/tmp/orbit-morimoto
		bonobo-activation-register-d21c58466e94adb1be8470194c44e2d9.lock
		bonobo-activation-server-d21c58466e94adb1be8470194c44e2d9-ior
		linc-194e-0-56d294e97c613
		linc-700d-0-2ff90f92a6423
		linc-88b-0-3f1bd51b782d8
		linc-88d-0-5c6a3cb3f1fe
		linc-8bc-0-e5cbc58e4d6
		linc-8be-0-537db2987ad5f
		linc-8fa-0-432f5a6780ff
		linc-907-0-6d7bf08ea2e6f
		linc-908-0-231ea7d55663d
		linc-90a-0-4405393733f30
		linc-90c-0-35a9515b435ce
		linc-90e-0-26c10e9933a5e
		linc-90f-0-30b9d7ca6098f
		linc-917-0-2d7c39cf46778
		linc-91d-0-b5247be79cb8
		linc-938-0-2f4cfb6a1ad2
		linc-939-0-45d9b60e86700
		linc-944-0-8b8597db7ec6
		linc-946-0-1a31ed0b85b2c
		linc-950-0-7299709ba851
		linc-9da-0-13aa6968b6991
		linc-a13-0-7fc1535310719
	
	/tmp/ksocket-morimoto
		kdeinit4__0
		klauncherMT3558.slave-socket
	
	/tmp/kde-morimoto
	
	/tmp/ssh-NHRlfb2285
		agent.2285
	
	/tmp/.esd-500
		socket
	
	/tmp/virtual-morimoto.RDLY7B
	
	/tmp/virtual-morimoto.vPtnVs

.. {{{end}}}

.. _os-system:

Running External Commands
=========================

.. warning::

    Many of these functions for working with processes have limited
    portability. For a more consistent way to work with processes in a
    platform independent manner, see the :mod:`subprocess` module
    instead.

The simplest way to run a separate command, without interacting with
it at all, is :func:`os.system()`. It takes a single string which is
the command line to be executed by a sub-process running a shell.

.. include:: os_system_example.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, '-u os_system_example.py'))
.. }}}

::

	$ python -u os_system_example.py
	合計 152
	-rw-rw-r-- 1 morimoto morimoto     0 2010-07-12 18:49 __init__.py
	-rw-rw-r-- 1 morimoto morimoto 50263 2010-07-21 18:52 index.rst
	-rw-rw-r-- 1 morimoto morimoto  1360 2010-07-12 18:49 os_access.py
	-rw-rw-r-- 1 morimoto morimoto  1347 2010-07-12 18:49 os_cwd_example.py
	-rw-rw-r-- 1 morimoto morimoto  1499 2010-07-12 18:49 os_directories.py
	-rw-rw-r-- 1 morimoto morimoto  1573 2010-07-12 18:49 os_environ_example.py
	-rw-rw-r-- 1 morimoto morimoto  1241 2010-07-12 18:49 os_exec_example.py
	-rw-rw-r-- 1 morimoto morimoto  1267 2010-07-12 18:49 os_fork_example.py
	-rw-rw-r-- 1 morimoto morimoto  1703 2010-07-12 18:49 os_kill_example.py
	-rw-rw-r-- 1 morimoto morimoto  1476 2010-07-12 18:49 os_popen.py
	-rw-rw-r-- 1 morimoto morimoto  1506 2010-07-12 18:49 os_popen2.py
	-rw-rw-r-- 1 morimoto morimoto  1528 2010-07-12 18:49 os_popen2_seq.py
	-rw-rw-r-- 1 morimoto morimoto  1658 2010-07-12 18:49 os_popen3.py
	-rw-rw-r-- 1 morimoto morimoto  1567 2010-07-12 18:49 os_popen4.py
	-rw-rw-r-- 1 morimoto morimoto  1395 2010-07-12 18:49 os_process_id_example.py
	-rw-rw-r-- 1 morimoto morimoto  1896 2010-07-12 18:49 os_process_user_example.py
	-rw-rw-r-- 1 morimoto morimoto  1206 2010-07-12 18:49 os_spawn_example.py
	-rw-rw-r-- 1 morimoto morimoto  1516 2010-07-12 18:49 os_stat.py
	-rw-rw-r-- 1 morimoto morimoto  1751 2010-07-12 18:49 os_stat_chmod.py
	-rwxrw-r-- 1 morimoto morimoto     8 2010-07-21 18:59 os_stat_chmod_example.txt
	-rw-rw-r-- 1 morimoto morimoto  1421 2010-07-12 18:49 os_symlinks.py
	-rw-rw-r-- 1 morimoto morimoto  1250 2010-07-12 18:49 os_system_background.py
	-rw-rw-r-- 1 morimoto morimoto  1191 2010-07-12 18:49 os_system_example.py
	-rw-rw-r-- 1 morimoto morimoto  1214 2010-07-12 18:49 os_system_shell.py
	-rw-rw-r-- 1 morimoto morimoto  1499 2010-07-12 18:49 os_wait_example.py
	-rw-rw-r-- 1 morimoto morimoto  1555 2010-07-12 18:49 os_waitpid_example.py
	-rw-rw-r-- 1 morimoto morimoto  1643 2010-07-12 18:49 os_walk.py

.. {{{end}}}


Since the command is passed directly to the shell for processing, it can even
include shell syntax such as globbing or environment variables:

.. include:: os_system_shell.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, '-u os_system_shell.py'))
.. }}}

::

	$ python -u os_system_shell.py
	drwxrwxr-x 2 morimoto morimoto 4096 2010-07-21 18:59 .

.. {{{end}}}


Unless you explicitly run the command in the background, the call to
:func:`os.system()` blocks until it is complete. Standard input,
output, and error from the child process are tied to the appropriate
streams owned by the caller by default, but can be redirected using
shell syntax.

.. include:: os_system_background.py
    :literal:
    :start-after: #end_pymotw_header


This is getting into shell trickery, though, and there are better ways to
accomplish the same thing.

.. {{{cog
.. cog.out(run_script(cog.inFile, '-u os_system_background.py'))
.. }}}

::

	$ python -u os_system_background.py
	Calling...
	2010年  7月 21日 水曜日 18:59:07 JST
	Sleeping...
	2010年  7月 21日 水曜日 18:59:10 JST

.. {{{end}}}

.. _creating-processes-with-os-fork:

Creating Processes with os.fork()
=================================

The POSIX functions :func:`fork()` and :func:`exec*()` (available
under Mac OS X, Linux, and other UNIX variants) are exposed via the
:mod:`os` module. Entire books have been written about reliably using
these functions, so check your library or bookstore for more details
than I will present here.

To create a new process as a clone of the current process, use
:func:`os.fork()`:

.. include:: os_fork_example.py
    :literal:
    :start-after: #end_pymotw_header

Your output will vary based on the state of your system each time you run the
example, but it should look something like:

.. {{{cog
.. cog.out(run_script(cog.inFile, '-u os_fork_example.py'))
.. }}}

::

	$ python -u os_fork_example.py
	I am the child
	Child process id: 6626

.. {{{end}}}

After the fork, you end up with two processes running the same
code. To tell which one you are in, check the return value of
:func:`fork()`. If it is ``0``, you are inside the child process. If
it is not ``0``, you are in the parent process and the return value is
the process id of the child process.

From the parent process, it is possible to send the child signals. This is a
bit more complicated to set up, and uses the :mod:`signal` module, so let's walk
through the code. First we can define a signal handler to be invoked when the
signal is received.

.. literalinclude:: os_kill_example.py
   :lines: 33-40

Then we fork, and in the parent pause a short amount of time before
sending a ``USR1`` signal using :func:`os.kill()`. The short pause
gives the child process time to set up the signal handler.

.. literalinclude:: os_kill_example.py
   :lines: 42-48

In the child, we set up the signal handler and go to sleep for a while to give
the parent time to send us the signal:

.. literalinclude:: os_kill_example.py
   :language: python
   :lines: 49-53

In a real app, you probably wouldn't need to (or want to) call
:func:`sleep()`.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'os_kill_example.py'))
.. }}}

::

	$ python os_kill_example.py
	Forking...
	PARENT: Pausing before sending signal...
	PARENT: Signaling 6629
	Forking...
	CHILD: Setting up signal handler
	CHILD: Pausing to wait for signal
	Received USR1 in process 6629

.. {{{end}}}


As you see, a simple way to handle separate behavior in the child
process is to check the return value of :func:`fork()` and branch. For
more complex behavior, you may want more code separation than a simple
branch. In other cases, you may have an existing program you have to
wrap. For both of these situations, you can use the :func:`os.exec*()`
series of functions to run another program. When you "exec" a program,
the code from that program replaces the code from your existing
process.

.. include:: os_exec_example.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'os_exec_example.py'))
.. }}}

::

	$ python os_exec_example.py
	合計 10396
	-rw-rw-r--  1 morimoto morimoto  142899 2010-07-21 12:56 3659_02-0115.txt
	-rw-------  1 morimoto morimoto    2419 2010-06-29 18:43 4AO3EV.tmp
	-rw-------  1 morimoto morimoto    2419 2010-06-29 12:19 75HYEV.tmp
	-rw-rw-r--  1 morimoto morimoto 4458794 2010-07-14 16:21 Excel2007BinaryFileFormat(xlsb)Specification.pdf
	-rw-rw-r--  1 morimoto morimoto     168 2010-07-21 17:52 bkup.log
	-rw-rw-r--  1 morimoto morimoto 3990400 2010-07-15 14:02 dhklf008.tgz
	-rw-------  1 morimoto morimoto       0 2010-07-06 08:53 dirs-0KTOFV
	-rw-------  1 morimoto morimoto       0 2010-07-06 08:50 dirs-28UUFV
	-rw-------  1 morimoto morimoto       0 2010-07-15 08:44 dirs-5CSDFV
	-rw-------  1 morimoto morimoto       0 2010-06-30 15:16 dirs-62HUEV
	-rw-------  1 morimoto morimoto       0 2010-07-16 08:56 dirs-6JBKFV
	-rw-------  1 morimoto morimoto       0 2010-06-16 08:41 dirs-73MBEV
	-rw-------  1 morimoto morimoto       0 2010-06-02 03:07 dirs-7P7RDV
	-rw-------  1 morimoto morimoto       0 2010-07-08 08:08 dirs-AKCMFV
	-rw-------  1 morimoto morimoto       0 2010-06-28 09:04 dirs-AMF9EV
	-rw-------  1 morimoto morimoto       0 2010-07-09 07:32 dirs-CARSFV
	-rw-------  1 morimoto morimoto       0 2010-07-11 11:59 dirs-EVQGFV
	-rw-------  1 morimoto morimoto       0 2010-07-13 08:38 dirs-G3YFFV
	-rw-------  1 morimoto morimoto       0 2010-06-18 08:53 dirs-G7OHEV
	-rw-------  1 morimoto morimoto       0 2010-07-14 08:55 dirs-IANEFV
	-rw-------  1 morimoto morimoto       0 2010-06-12 10:58 dirs-IVZ7DV
	-rw-------  1 morimoto morimoto       0 2010-07-01 08:48 dirs-J8SREV
	-rw-------  1 morimoto morimoto       0 2010-06-29 08:53 dirs-JVGAFV
	-rw-------  1 morimoto morimoto       0 2010-06-17 08:30 dirs-K4SMEV
	-rw-------  1 morimoto morimoto       0 2010-07-20 08:42 dirs-KM7ZFV
	-rw-------  1 morimoto morimoto       0 2010-06-21 08:39 dirs-LN8MEV
	-rw-------  1 morimoto morimoto       0 2010-07-02 08:59 dirs-M2R8EV
	-rw-------  1 morimoto morimoto       0 2010-06-15 08:30 dirs-M9OHEV
	-rw-------  1 morimoto morimoto       0 2010-06-22 08:15 dirs-NP95DV
	-rw-------  1 morimoto morimoto       0 2010-06-06 13:34 dirs-ORRHDV
	-rw-------  1 morimoto morimoto       0 2010-06-25 08:05 dirs-QOCVEV
	-rw-------  1 morimoto morimoto       0 2010-06-11 08:24 dirs-RO2GEV
	-rw-------  1 morimoto morimoto       0 2010-06-26 13:12 dirs-S0TWEV
	-rw-------  1 morimoto morimoto       0 2010-06-03 08:37 dirs-U53HDV
	-rw-------  1 morimoto morimoto       0 2010-05-31 09:13 dirs-VHBRDV
	-rw-------  1 morimoto morimoto       0 2010-06-14 08:33 dirs-YPW1DV
	-rw-------  1 morimoto morimoto       0 2010-06-23 08:33 dirs-ZFHPEV
	-rw-r--r--  1 morimoto morimoto   51739 2010-07-20 15:05 django.po
	-rw-r--r--  1 morimoto morimoto   18674 2010-07-15 19:29 djangojs.po
	-rw-r--r--  1 morimoto morimoto  848384 2010-04-16 09:42 dmfxlibmlver3.doc
	-rw-rw-r--  1 morimoto morimoto  826880 2010-06-16 12:50 dmfxlibver3.doc
	-rw-rw-r--  1 morimoto morimoto   12288 2010-07-21 18:58 example.db
	-rw-r--r--  1 morimoto morimoto     187 2010-02-04 06:51 hosts
	drwx------  2 morimoto morimoto    4096 2010-07-20 09:07 kde-morimoto
	drwx------  2 morimoto morimoto    4096 2010-07-20 08:42 keyring-NNmbf2
	drwx------  2 morimoto morimoto    4096 2009-09-14 08:15 keyring-qoDG37
	drwx------  2 morimoto morimoto    4096 2010-07-20 09:07 ksocket-morimoto
	-rw-------  1 morimoto morimoto    6462 2010-06-14 08:42 nsmail-1.asc
	-rw-------  1 morimoto morimoto    2498 2010-07-21 10:41 nsmail-2.asc
	drwx------  2 morimoto morimoto    4096 2010-07-21 18:59 orbit-morimoto
	drwx------  2 morimoto morimoto    4096 2010-07-21 15:59 plugtmp
	drwx------  2 morimoto morimoto    4096 2010-07-12 18:46 plugtmp-1
	drwx------. 2 morimoto morimoto    4096 2010-07-20 08:42 pulse-uXTDCdjuejPW
	-rw-rw-r--  1 morimoto morimoto   12288 2010-07-21 18:57 pymotw_import_example.shelve
	srw-------  1 morimoto morimoto       0 2010-07-20 08:42 scim-helper-manager-socket-morimoto
	srw-------  1 morimoto morimoto       0 2010-07-20 08:42 scim-panel-socket:0-morimoto
	srw-------  1 morimoto morimoto       0 2010-07-20 08:42 scim-socket-frontend-morimoto
	-rw-------  1 morimoto morimoto    1684 2010-07-21 18:32 sphinx-err-1j4tOo.log
	-rw-------  1 morimoto morimoto    1684 2010-07-21 17:29 sphinx-err-2emfzd.log
	-rw-------  1 morimoto morimoto    1305 2010-07-12 19:42 sphinx-err-2vIYM7.log
	-rw-------  1 morimoto morimoto     792 2010-07-15 09:54 sphinx-err-68_vWW.log
	-rw-------  1 morimoto morimoto    1684 2010-07-21 07:38 sphinx-err-7bn26G.log
	-rw-------  1 morimoto morimoto    1684 2010-07-15 20:37 sphinx-err-9YxfTg.log
	-rw-------  1 morimoto morimoto    1684 2010-07-15 09:57 sphinx-err-AkPXqU.log
	-rw-------  1 morimoto morimoto    1684 2010-07-21 09:37 sphinx-err-B6nIVr.log
	-rw-------  1 morimoto morimoto    1684 2010-07-15 10:10 sphinx-err-BhIGyy.log
	-rw-------  1 morimoto morimoto    1684 2010-07-15 21:00 sphinx-err-CHBG5d.log
	-rw-------  1 morimoto morimoto    1684 2010-07-20 18:30 sphinx-err-DbJGW6.log
	-rw-------  1 morimoto morimoto    1305 2010-07-12 19:45 sphinx-err-E4rP0z.log
	-rw-------  1 morimoto morimoto    1684 2010-07-21 08:20 sphinx-err-FpjRCb.log
	-rw-------  1 morimoto morimoto    1684 2010-07-21 09:37 sphinx-err-GX7aTs.log
	-rw-------  1 morimoto morimoto    1684 2010-07-20 18:06 sphinx-err-Mat86d.log
	-rw-------  1 morimoto morimoto    1684 2010-07-14 17:36 sphinx-err-O5B2V_.log
	-rw-------  1 morimoto morimoto    1684 2010-07-20 09:29 sphinx-err-R78Fqn.log
	-rw-------  1 morimoto morimoto    1375 2010-07-12 20:05 sphinx-err-Rlu__E.log
	-rw-------  1 morimoto morimoto    1684 2010-07-21 08:25 sphinx-err-UJhDOd.log
	-rw-------  1 morimoto morimoto    1684 2010-07-21 17:44 sphinx-err-VRQ2FL.log
	-rw-------  1 morimoto morimoto     792 2010-07-14 17:33 sphinx-err-_W2ccO.log
	-rw-------  1 morimoto morimoto    1684 2010-07-14 18:27 sphinx-err-aTHJDM.log
	-rw-------  1 morimoto morimoto    1684 2010-07-15 10:15 sphinx-err-bOdk1X.log
	-rw-------  1 morimoto morimoto    1684 2010-07-14 18:34 sphinx-err-dOVkWv.log
	-rw-------  1 morimoto morimoto    1684 2010-07-21 18:03 sphinx-err-dZIo1p.log
	-rw-------  1 morimoto morimoto     832 2010-07-14 17:33 sphinx-err-dg4xGX.log
	-rw-------  1 morimoto morimoto    1684 2010-07-14 17:43 sphinx-err-fD9qaA.log
	-rw-------  1 morimoto morimoto    1684 2010-07-14 17:34 sphinx-err-gEqdhj.log
	-rw-------  1 morimoto morimoto    1684 2010-07-15 20:55 sphinx-err-gLHw0q.log
	-rw-------  1 morimoto morimoto     832 2010-07-15 09:56 sphinx-err-h4zdqz.log
	-rw-------  1 morimoto morimoto    1684 2010-07-21 08:33 sphinx-err-i9n7cC.log
	-rw-------  1 morimoto morimoto    1684 2010-07-15 10:14 sphinx-err-jHZNpP.log
	-rw-------  1 morimoto morimoto    1684 2010-07-21 09:25 sphinx-err-jg9ZEJ.log
	-rw-------  1 morimoto morimoto     832 2010-07-12 19:41 sphinx-err-jj3ld1.log
	-rw-------  1 morimoto morimoto    1684 2010-07-21 09:27 sphinx-err-ke6Yfj.log
	-rw-------  1 morimoto morimoto    1684 2010-07-21 08:21 sphinx-err-l2jixV.log
	-rw-------  1 morimoto morimoto    1684 2010-07-16 10:19 sphinx-err-mECiSc.log
	-rw-------  1 morimoto morimoto    1684 2010-07-21 17:38 sphinx-err-o9Q6G4.log
	-rw-------  1 morimoto morimoto     792 2010-07-12 19:38 sphinx-err-rxOeos.log
	-rw-------  1 morimoto morimoto    1684 2010-07-16 10:28 sphinx-err-tACpKT.log
	-rw-------  1 morimoto morimoto    1684 2010-07-21 18:05 sphinx-err-u1Da67.log
	drwx------  2 morimoto morimoto    4096 2010-07-20 08:42 ssh-NHRlfb2285
	drwx------  2 morimoto morimoto    4096 2010-07-20 08:42 ssh-zRKFQQ2189
	-rw-rw-r--  1 morimoto morimoto     448 2010-07-21 18:50 trace_example.recurse.cover
	drwx------. 3 morimoto morimoto    4096 2010-07-20 09:08 tracker-morimoto
	drwx------  2 morimoto morimoto    4096 2010-07-14 08:56 virtual-morimoto.26mNh3
	drwx------  2 morimoto morimoto    4096 2010-07-11 11:59 virtual-morimoto.FWbKZy
	drwx------  2 morimoto morimoto    4096 2010-07-13 08:39 virtual-morimoto.NUY9DD
	drwx------  2 morimoto morimoto    4096 2010-07-20 08:42 virtual-morimoto.NfSC6x
	drwx------  2 morimoto morimoto    4096 2010-07-16 08:56 virtual-morimoto.RDLY7B
	drwx------  2 morimoto morimoto    4096 2010-07-15 08:44 virtual-morimoto.vPtnVs
	drwxrwxrwx  3 root     root        4096 2010-07-13 08:38 vmware-temp

.. {{{end}}}


There are many variations of :func:`exec*()`, depending on what form
you might have the arguments in, whether you want the path and
environment of the parent process to be copied to the child, etc. Have
a look at the library documentation to for complete details.

For all variations, the first argument is a path or filename and the remaining
arguments control how that program runs. They are either passed as command
line arguments or override the process "environment" (see os.environ and
os.getenv).

Waiting for a Child
===================

Suppose you are using multiple processes to work around the threading
limitations of Python and the Global Interpreter Lock. If you start
several processes to run separate tasks, you will want to wait for one
or more of them to finish before starting new ones, to avoid
overloading the server. There are a few different ways to do that
using :func:`wait()` and related functions.

If you don't care, or know, which child process might exit first
:func:`os.wait()` will return as soon as any exits:

.. include:: os_wait_example.py
    :literal:
    :start-after: #end_pymotw_header


Notice that the return value from :func:`os.wait()` is a tuple
containing the process id and exit status ("a 16-bit number, whose low
byte is the signal number that killed the process, and whose high byte
is the exit status").

.. {{{cog
.. cog.out(run_script(cog.inFile, 'os_wait_example.py'))
.. }}}

::

	$ python os_wait_example.py
	PARENT: Forking 0
	WORKER 0: Starting
	WORKER 0: Finishing
	PARENT: Forking 0
	PARENT: Forking 1
	WORKER 1: Starting
	WORKER 1: Finishing
	PARENT: Forking 0
	PARENT: Forking 1
	PARENT: Forking 2
	WORKER 2: Starting
	WORKER 2: Finishing
	PARENT: Forking 0
	PARENT: Forking 1
	PARENT: Forking 2
	PARENT: Waiting for 0
	PARENT: (6635, 0)
	PARENT: Waiting for 1
	PARENT: (6636, 256)
	PARENT: Waiting for 2
	PARENT: (6637, 512)

.. {{{end}}}

If you want a specific process, use :func:`os.waitpid()`.

.. include:: os_waitpid_example.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'os_waitpid_example.py'))
.. }}}

::

	$ python os_waitpid_example.py
	PARENT: Forking 0
	WORKER 0: Starting
	WORKER 0: Finishing
	PARENT: Forking 0
	PARENT: Forking 1
	WORKER 1: Starting
	WORKER 1: Finishing
	PARENT: Forking 0
	PARENT: Forking 1
	PARENT: Forking 2
	WORKER 2: Starting
	WORKER 2: Finishing
	PARENT: Forking 0
	PARENT: Forking 1
	PARENT: Forking 2
	PARENT: Waiting for 6640
	PARENT: (6640, 0)
	PARENT: Waiting for 6641
	PARENT: (6641, 256)
	PARENT: Waiting for 6642
	PARENT: (6642, 512)

.. {{{end}}}

:func:`wait3()` and :func:`wait4()` work in a similar manner, but
return more detailed information about the child process with the pid,
exit status, and resource usage.

Spawn
=====

As a convenience, the :func:`spawn*()` family of functions handles the
:func:`fork()` and :func:`exec*()` calls for you in one statement:

.. include:: os_spawn_example.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'os_spawn_example.py'))
.. }}}

::

	$ python os_spawn_example.py
	合計 10396
	-rw-rw-r--  1 morimoto morimoto  142899 2010-07-21 12:56 3659_02-0115.txt
	-rw-------  1 morimoto morimoto    2419 2010-06-29 18:43 4AO3EV.tmp
	-rw-------  1 morimoto morimoto    2419 2010-06-29 12:19 75HYEV.tmp
	-rw-rw-r--  1 morimoto morimoto 4458794 2010-07-14 16:21 Excel2007BinaryFileFormat(xlsb)Specification.pdf
	-rw-rw-r--  1 morimoto morimoto     168 2010-07-21 17:52 bkup.log
	-rw-rw-r--  1 morimoto morimoto 3990400 2010-07-15 14:02 dhklf008.tgz
	-rw-------  1 morimoto morimoto       0 2010-07-06 08:53 dirs-0KTOFV
	-rw-------  1 morimoto morimoto       0 2010-07-06 08:50 dirs-28UUFV
	-rw-------  1 morimoto morimoto       0 2010-07-15 08:44 dirs-5CSDFV
	-rw-------  1 morimoto morimoto       0 2010-06-30 15:16 dirs-62HUEV
	-rw-------  1 morimoto morimoto       0 2010-07-16 08:56 dirs-6JBKFV
	-rw-------  1 morimoto morimoto       0 2010-06-16 08:41 dirs-73MBEV
	-rw-------  1 morimoto morimoto       0 2010-06-02 03:07 dirs-7P7RDV
	-rw-------  1 morimoto morimoto       0 2010-07-08 08:08 dirs-AKCMFV
	-rw-------  1 morimoto morimoto       0 2010-06-28 09:04 dirs-AMF9EV
	-rw-------  1 morimoto morimoto       0 2010-07-09 07:32 dirs-CARSFV
	-rw-------  1 morimoto morimoto       0 2010-07-11 11:59 dirs-EVQGFV
	-rw-------  1 morimoto morimoto       0 2010-07-13 08:38 dirs-G3YFFV
	-rw-------  1 morimoto morimoto       0 2010-06-18 08:53 dirs-G7OHEV
	-rw-------  1 morimoto morimoto       0 2010-07-14 08:55 dirs-IANEFV
	-rw-------  1 morimoto morimoto       0 2010-06-12 10:58 dirs-IVZ7DV
	-rw-------  1 morimoto morimoto       0 2010-07-01 08:48 dirs-J8SREV
	-rw-------  1 morimoto morimoto       0 2010-06-29 08:53 dirs-JVGAFV
	-rw-------  1 morimoto morimoto       0 2010-06-17 08:30 dirs-K4SMEV
	-rw-------  1 morimoto morimoto       0 2010-07-20 08:42 dirs-KM7ZFV
	-rw-------  1 morimoto morimoto       0 2010-06-21 08:39 dirs-LN8MEV
	-rw-------  1 morimoto morimoto       0 2010-07-02 08:59 dirs-M2R8EV
	-rw-------  1 morimoto morimoto       0 2010-06-15 08:30 dirs-M9OHEV
	-rw-------  1 morimoto morimoto       0 2010-06-22 08:15 dirs-NP95DV
	-rw-------  1 morimoto morimoto       0 2010-06-06 13:34 dirs-ORRHDV
	-rw-------  1 morimoto morimoto       0 2010-06-25 08:05 dirs-QOCVEV
	-rw-------  1 morimoto morimoto       0 2010-06-11 08:24 dirs-RO2GEV
	-rw-------  1 morimoto morimoto       0 2010-06-26 13:12 dirs-S0TWEV
	-rw-------  1 morimoto morimoto       0 2010-06-03 08:37 dirs-U53HDV
	-rw-------  1 morimoto morimoto       0 2010-05-31 09:13 dirs-VHBRDV
	-rw-------  1 morimoto morimoto       0 2010-06-14 08:33 dirs-YPW1DV
	-rw-------  1 morimoto morimoto       0 2010-06-23 08:33 dirs-ZFHPEV
	-rw-r--r--  1 morimoto morimoto   51739 2010-07-20 15:05 django.po
	-rw-r--r--  1 morimoto morimoto   18674 2010-07-15 19:29 djangojs.po
	-rw-r--r--  1 morimoto morimoto  848384 2010-04-16 09:42 dmfxlibmlver3.doc
	-rw-rw-r--  1 morimoto morimoto  826880 2010-06-16 12:50 dmfxlibver3.doc
	-rw-rw-r--  1 morimoto morimoto   12288 2010-07-21 18:58 example.db
	-rw-r--r--  1 morimoto morimoto     187 2010-02-04 06:51 hosts
	drwx------  2 morimoto morimoto    4096 2010-07-20 09:07 kde-morimoto
	drwx------  2 morimoto morimoto    4096 2010-07-20 08:42 keyring-NNmbf2
	drwx------  2 morimoto morimoto    4096 2009-09-14 08:15 keyring-qoDG37
	drwx------  2 morimoto morimoto    4096 2010-07-20 09:07 ksocket-morimoto
	-rw-------  1 morimoto morimoto    6462 2010-06-14 08:42 nsmail-1.asc
	-rw-------  1 morimoto morimoto    2498 2010-07-21 10:41 nsmail-2.asc
	drwx------  2 morimoto morimoto    4096 2010-07-21 18:59 orbit-morimoto
	drwx------  2 morimoto morimoto    4096 2010-07-21 15:59 plugtmp
	drwx------  2 morimoto morimoto    4096 2010-07-12 18:46 plugtmp-1
	drwx------. 2 morimoto morimoto    4096 2010-07-20 08:42 pulse-uXTDCdjuejPW
	-rw-rw-r--  1 morimoto morimoto   12288 2010-07-21 18:57 pymotw_import_example.shelve
	srw-------  1 morimoto morimoto       0 2010-07-20 08:42 scim-helper-manager-socket-morimoto
	srw-------  1 morimoto morimoto       0 2010-07-20 08:42 scim-panel-socket:0-morimoto
	srw-------  1 morimoto morimoto       0 2010-07-20 08:42 scim-socket-frontend-morimoto
	-rw-------  1 morimoto morimoto    1684 2010-07-21 18:32 sphinx-err-1j4tOo.log
	-rw-------  1 morimoto morimoto    1684 2010-07-21 17:29 sphinx-err-2emfzd.log
	-rw-------  1 morimoto morimoto    1305 2010-07-12 19:42 sphinx-err-2vIYM7.log
	-rw-------  1 morimoto morimoto     792 2010-07-15 09:54 sphinx-err-68_vWW.log
	-rw-------  1 morimoto morimoto    1684 2010-07-21 07:38 sphinx-err-7bn26G.log
	-rw-------  1 morimoto morimoto    1684 2010-07-15 20:37 sphinx-err-9YxfTg.log
	-rw-------  1 morimoto morimoto    1684 2010-07-15 09:57 sphinx-err-AkPXqU.log
	-rw-------  1 morimoto morimoto    1684 2010-07-21 09:37 sphinx-err-B6nIVr.log
	-rw-------  1 morimoto morimoto    1684 2010-07-15 10:10 sphinx-err-BhIGyy.log
	-rw-------  1 morimoto morimoto    1684 2010-07-15 21:00 sphinx-err-CHBG5d.log
	-rw-------  1 morimoto morimoto    1684 2010-07-20 18:30 sphinx-err-DbJGW6.log
	-rw-------  1 morimoto morimoto    1305 2010-07-12 19:45 sphinx-err-E4rP0z.log
	-rw-------  1 morimoto morimoto    1684 2010-07-21 08:20 sphinx-err-FpjRCb.log
	-rw-------  1 morimoto morimoto    1684 2010-07-21 09:37 sphinx-err-GX7aTs.log
	-rw-------  1 morimoto morimoto    1684 2010-07-20 18:06 sphinx-err-Mat86d.log
	-rw-------  1 morimoto morimoto    1684 2010-07-14 17:36 sphinx-err-O5B2V_.log
	-rw-------  1 morimoto morimoto    1684 2010-07-20 09:29 sphinx-err-R78Fqn.log
	-rw-------  1 morimoto morimoto    1375 2010-07-12 20:05 sphinx-err-Rlu__E.log
	-rw-------  1 morimoto morimoto    1684 2010-07-21 08:25 sphinx-err-UJhDOd.log
	-rw-------  1 morimoto morimoto    1684 2010-07-21 17:44 sphinx-err-VRQ2FL.log
	-rw-------  1 morimoto morimoto     792 2010-07-14 17:33 sphinx-err-_W2ccO.log
	-rw-------  1 morimoto morimoto    1684 2010-07-14 18:27 sphinx-err-aTHJDM.log
	-rw-------  1 morimoto morimoto    1684 2010-07-15 10:15 sphinx-err-bOdk1X.log
	-rw-------  1 morimoto morimoto    1684 2010-07-14 18:34 sphinx-err-dOVkWv.log
	-rw-------  1 morimoto morimoto    1684 2010-07-21 18:03 sphinx-err-dZIo1p.log
	-rw-------  1 morimoto morimoto     832 2010-07-14 17:33 sphinx-err-dg4xGX.log
	-rw-------  1 morimoto morimoto    1684 2010-07-14 17:43 sphinx-err-fD9qaA.log
	-rw-------  1 morimoto morimoto    1684 2010-07-14 17:34 sphinx-err-gEqdhj.log
	-rw-------  1 morimoto morimoto    1684 2010-07-15 20:55 sphinx-err-gLHw0q.log
	-rw-------  1 morimoto morimoto     832 2010-07-15 09:56 sphinx-err-h4zdqz.log
	-rw-------  1 morimoto morimoto    1684 2010-07-21 08:33 sphinx-err-i9n7cC.log
	-rw-------  1 morimoto morimoto    1684 2010-07-15 10:14 sphinx-err-jHZNpP.log
	-rw-------  1 morimoto morimoto    1684 2010-07-21 09:25 sphinx-err-jg9ZEJ.log
	-rw-------  1 morimoto morimoto     832 2010-07-12 19:41 sphinx-err-jj3ld1.log
	-rw-------  1 morimoto morimoto    1684 2010-07-21 09:27 sphinx-err-ke6Yfj.log
	-rw-------  1 morimoto morimoto    1684 2010-07-21 08:21 sphinx-err-l2jixV.log
	-rw-------  1 morimoto morimoto    1684 2010-07-16 10:19 sphinx-err-mECiSc.log
	-rw-------  1 morimoto morimoto    1684 2010-07-21 17:38 sphinx-err-o9Q6G4.log
	-rw-------  1 morimoto morimoto     792 2010-07-12 19:38 sphinx-err-rxOeos.log
	-rw-------  1 morimoto morimoto    1684 2010-07-16 10:28 sphinx-err-tACpKT.log
	-rw-------  1 morimoto morimoto    1684 2010-07-21 18:05 sphinx-err-u1Da67.log
	drwx------  2 morimoto morimoto    4096 2010-07-20 08:42 ssh-NHRlfb2285
	drwx------  2 morimoto morimoto    4096 2010-07-20 08:42 ssh-zRKFQQ2189
	-rw-rw-r--  1 morimoto morimoto     448 2010-07-21 18:50 trace_example.recurse.cover
	drwx------. 3 morimoto morimoto    4096 2010-07-20 09:08 tracker-morimoto
	drwx------  2 morimoto morimoto    4096 2010-07-14 08:56 virtual-morimoto.26mNh3
	drwx------  2 morimoto morimoto    4096 2010-07-11 11:59 virtual-morimoto.FWbKZy
	drwx------  2 morimoto morimoto    4096 2010-07-13 08:39 virtual-morimoto.NUY9DD
	drwx------  2 morimoto morimoto    4096 2010-07-20 08:42 virtual-morimoto.NfSC6x
	drwx------  2 morimoto morimoto    4096 2010-07-16 08:56 virtual-morimoto.RDLY7B
	drwx------  2 morimoto morimoto    4096 2010-07-15 08:44 virtual-morimoto.vPtnVs
	drwxrwxrwx  3 root     root        4096 2010-07-13 08:38 vmware-temp

.. {{{end}}}


.. seealso::

    `os <http://docs.python.org/lib/module-os.html>`_
        Standard library documentation for this module.

    :mod:`subprocess`
        The subprocess module supersedes os.popen().

    :mod:`multiprocessing` 
        The multiprocessing module makes working with extra processes
        easier than doing all of the work yourself.

    :mod:`tempfile`
        The tempfile module for working with temporary files.

    *Unix Manual Page Introduction*
        Includes definitions of real and effective ids, etc.
        
        http://www.scit.wlv.ac.uk/cgi-bin/mansec?2+intro

    *Speaking UNIX, Part 8.*
        Learn how UNIX multitasks.
        
        http://www.ibm.com/developerworks/aix/library/au-speakingunix8/index.html

    *Unix Concepts*
        For more discussion of stdin, stdout, and stderr.
        
        http://www.linuxhq.com/guides/LUG/node67.html

    *Delve into Unix Process Creation*
        Explains the life cycle of a UNIX process.
        
        http://www.ibm.com/developerworks/aix/library/au-unixprocess.html

    `Advanced Programming in the UNIX(R) Environment <http://www.amazon.com/Programming-Environment-Addison-Wesley-Professional-Computing/dp/0201433079/ref=pd_bbs_3/002-2842372-4768037?ie=UTF8&s=books&amp;qid=1182098757&sr=8-3>`_
        Covers working with multiple processes, such as handling signals, closing duplicated
        file descriptors, etc.

    :ref:`article-file-access`
