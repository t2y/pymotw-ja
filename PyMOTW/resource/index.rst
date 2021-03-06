..
    ======================================
    resource -- System resource management
    ======================================

================================
resource -- システムリソース管理
================================

..
    :synopsis: System resource management

.. module:: resource
    :synopsis: システムリソース管理

..
    :Purpose: Manage the system resource limits for a Unix program.
    :Available In: 1.5.2

:目的: Unix プログラムのシステムリソースリミットを管理する
:利用できるバージョン: 1.5.2

..
    The functions in :mod:`resource` probe the current system resources
    consumed by a process, and place limits on them to control how much
    load a program can impose on a system.

:mod:`resource` モジュールの関数は、プロセスが消費する現在のシステムリソースを調べて、プログラムがシステム上でどのぐらいの負荷を与えるかを制御するためにリミットを設けます。

..
    Current Usage
    =============

現在の使用状況
==============

..
    Use :func:`getrusage()` to probe the resources used by the current
    process and/or its children.  The return value is a data structure
    containing several resource metrics based on the current state of the
    system.

カレントプロセスやその子プロセスが使用するリソースを調べるには :func:`getrusage()` を使用してください。返り値は現在のシステムの状態に基づく複数のリソース値を含むデータです。

.. note::  

  .. Not all of the resource values gathered are displayed here.  Refer
     to the `stdlib docs
     <http://docs.python.org/library/resource.html#resource.getrusage>`_
     for a more complete list.

  この記事では全てのリソース値を紹介しません。完全なリストは `標準ライブラリドキュメント <http://docs.python.org/library/resource.html#resource.getrusage>`_ を参照してください。

.. include:: resource_getrusage.py
    :literal:
    :start-after: #end_pymotw_header

..
    Because the test program is extremely simple, it does not use very
    many resources:

テストプログラムはとても単純なので、あまりリソースを消費しません。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'resource_getrusage.py'))
.. }}}

::

	$ python resource_getrusage.py
	
	User time                 (ru_utime  ) = 0.010192
	System time               (ru_stime  ) = 0.005743
	Max. Resident Set Size    (ru_maxrss ) = 3891200
	Shared Memory Size        (ru_ixrss  ) = 0
	Unshared Memory Size      (ru_idrss  ) = 0
	Stack Size                (ru_isrss  ) = 0
	Block inputs              (ru_inblock) = 0
	Block outputs             (ru_oublock) = 0

.. {{{end}}}

..
    Resource Limits
    ===============

リソースリミット
================

..
    Separate from the current actual usage, it is possible to check the
    *limits* imposed on the application, and then change them.

現在の実際の使用状況とは別に、アプリケーションに与えられた *リミット* を調べて変更できます。

.. include:: resource_getrlimit.py
    :literal:
    :start-after: #end_pymotw_header

..
    The return value for each limit is a tuple containing the *soft* limit
    imposed by the current configuration and the *hard* limit imposed by
    the operating system.

それぞれのリミットの返り値は、現在の設定の *ソフト* リミットとオペレーティングシステムの *ハード* リミットを含むタプルです。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'resource_getrlimit.py'))
.. }}}

::

	$ python resource_getrlimit.py
	
	Maximum core file size            (RLIMIT_CORE    ) :                    0  9223372036854775807
	Maximum CPU time                  (RLIMIT_CPU     ) :  9223372036854775807  9223372036854775807
	Maximum file size                 (RLIMIT_FSIZE   ) :  9223372036854775807  9223372036854775807
	Maximum heap size                 (RLIMIT_DATA    ) :  9223372036854775807  9223372036854775807
	Maximum stack size                (RLIMIT_STACK   ) :              8388608             67104768
	Maximum resident set size         (RLIMIT_RSS     ) :  9223372036854775807  9223372036854775807
	Maximum number of processes       (RLIMIT_NPROC   ) :                  709                 1064
	Maximum number of open files      (RLIMIT_NOFILE  ) :                 2560  9223372036854775807
	Maximum lockable memory address   (RLIMIT_MEMLOCK ) :  9223372036854775807  9223372036854775807

.. {{{end}}}

..
    The limits can be changed with :func:`setrlimit()`.  For example, to
    control the number of files a process can open the :const:`RLIMIT_NOFILE`
    value can be set to use a smaller soft limit value.

そのリミットは :func:`setrlimit()` で変更できます。例えば、1つのプロセスがオープンできるファイル数を制御するために :const:`RLIMIT_NOFILE` をより小さなソフトリミットを使用するように変更できます。

.. include:: resource_setrlimit_nofile.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'resource_setrlimit_nofile.py'))
.. }}}

::

	$ python resource_setrlimit_nofile.py
	
	Soft limit starts as  : 2560
	Soft limit changed to : 4
	random has fd = 3
	[Errno 24] Too many open files: '/dev/null'

.. {{{end}}}

..
    It can also be useful to limit the amount of CPU time a process should
    consume, to avoid eating up too much time.  When the process runs past
    the allotted amount of time, it it sent a :const:`SIGXCPU` signal.

それは1つのプロセスが消費する CPU 時間に対して、多くの時間を費やさないように制限するのにも便利です。そのプロセスが割り当てられた CPU 時間を実行したときに :const:`SIGXCPU` シグナルを送信します。

.. include:: resource_setrlimit_cpu.py
    :literal:
    :start-after: #end_pymotw_header

..
    Normally the signal handler should flush all open files and close
    them, but in this case it just prints a message and exits.

普通はシグナルハンドラがオープンされた全てのファイルをフラッシュしてからクローズします。しかし、このサンプルはただメッセージを表示して終了します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'resource_setrlimit_cpu.py', ignore_error=True))
.. }}}

::

	$ python resource_setrlimit_cpu.py
	
	Soft limit starts as  : 9223372036854775807
	Soft limit changed to : 1
	
	Starting: Thu Feb 21 06:36:32 2013
	EXPIRED : Thu Feb 21 06:36:33 2013
	(time ran out)

.. {{{end}}}


.. seealso::

    `resource <http://docs.python.org/library/resource.html>`_
        .. The standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント

    :mod:`signal`
        .. For details on registering signal handlers.

        シグナルハンドラ登録の詳細
