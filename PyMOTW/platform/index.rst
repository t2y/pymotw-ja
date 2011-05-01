..
    ===============================================
     platform -- Access system version information
    ===============================================

====================================================
 platform -- システムのバージョン情報にアクセスする
====================================================

..
    :synopsis: Access system hardware, OS, and interpreter version information.

.. module:: platform
    :synopsis: システムのハードウェア、OS、インタープリタバージョン情報にアクセスする

..
    :Purpose: Probe the underlying platform's hardware, operating system, and interpreter version information.
    :Available In: 2.3 and later

:目的: システムのハードウェア、OS、インタープリタバージョン情報にアクセスする
:利用できるバージョン: 2.3 以上

..
    Although Python is often used as a cross-platform language, it is
    occasionally necessary to know what sort of system a program is
    running on. Build tools need that information, but an application
    might also know that some of the libraries or external commands it
    uses have different interfaces on different operating systems. For
    example, a tool to manage the network configuration of an operating
    system can define a portable representation of network interfaces,
    aliases, IP addresses, etc. But once it actually needs to edit the
    configuration files, it must know more about the host so it can use
    the correct operating system configuration commands and files.  The
    :mod:`platform` module includes the tools for learning about the
    interpreter, operating system, and hardware platform where a program
    is running.

Python は、クロスプラットフォームな言語としてよく使用されていますが、プログラムが実行されているシステムの情報を知りたいときがあります。ビルドツールはその情報を必要とし、アプリケーションも同様にそれぞれのオペレーティングシステムで別のインタフェースをもつライブラリや外部コマンドがあります。例えば、オペレーティングシステムのネットワーク設定を管理するツールは、ネットワークインタフェース、エイリアス、IPアドレス等の移植性の高い表現を定義できます。しかし、実際に設定ファイルを編集する必要がある場合、正しいオペレーティングシステムの設定コマンドとファイルを使用できるように、そのホストの詳細について知っておかなければなりません。 :mod:`platform` モジュールは、プログラムを実行しているインタープリタ、オペレーティングシステム、ハードウェアプラットフォームについて知るためのツールを提供します。

.. note::

    .. The example output below was generated on a MacBook Pro3,1 running
       OS X 10.6.4, a VMware Fusion VM running CentOS 5.5, and a Dell PC
       running Microsoft Windows 2008.  Python was installed on the OS X
       and Windows systems using the pre-compiled installer from
       python.org.  The Linux system is running an interpreter built from
       source locally.

    この記事のサンプル出力は、MacBook Pro3.1 の OS X 10.6.4、VMware Fusion VM の CentOS 5.5、Dell PC の Microsoft Windows 2008 で実行したものです。Python は python.org にあるコンパイル済みのインストーラを使用して OS X と Windodws にインストールしました。Linux は、ソースからローカルでビルドしたインタープリタを実行しています。

..
    Interpreter
    ===========

インタープリタ
==============

..
    There are four functions for getting information about the current
    Python interpreter. :func:`python_version` and
    :func:`python_version_tuple` return different forms of the interpreter
    version with major, minor, and patchlevel components.
    :func:`python_compiler` reports on the compiler used to build the
    interpreter. And :func:`python_build` gives a version string for the
    build of the interpreter.

使用している Python インタープリタに関する情報を取得する関数が4つあります。 :func:`python_version` と :func:`python_version_tuple` は、メジャー、マイナー、パッチレベルのコンポーネントをもつインタープリタのバージョンを別の形式で返します。 :func:`python_compiler` は、インタープリタをビルドするために使用したコンパイラを返します。 :func:`python_build` は、インタープリタのビルド番号の文字列を返します。

.. include:: platform_python.py
    :literal:
    :start-after: #end_pymotw_header


OS X:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'platform_python.py'))
.. }}}
.. {{{end}}}

Linux::

    $ python platform_python.py 
    Version      : 2.7.0
    Version tuple: ('2', '7', '0')
    Compiler     : GCC 4.1.2 20080704 (Red Hat 4.1.2-46)
    Build        : ('r27', 'Aug 20 2010 11:37:51')

Windows::

    C:> python.exe platform_python.py
    Version      : 2.7.0
    Version tuple: ['2', '7', '0']
    Compiler     : MSC v.1500 64 bit (AMD64)
    Build        : ('r27:82525', 'Jul  4 2010 07:43:08')

..
    Platform
    ========

プラットフォーム
================

..
    :func:`platform` returns string containing a general purpose platform
    identifier.  The function accepts two optional boolean arguments. If
    *aliased* is True, the names in the return value are converted from a
    formal name to their more common form. When *terse* is true, returns a
    minimal value with some parts dropped.

:func:`platform` は、汎用的なプラットフォームの識別子を含む文字列を返します。この関数は2つのオプション引数をブーリアン値で受け取ります。 *aliased* が True の場合、返り値の名前は公式名から一般名に変換されます。 *terse* が True の場合、一部が削除された短い名前が返されます。

.. include:: platform_platform.py
    :literal:
    :start-after: #end_pymotw_header

OS X:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'platform_platform.py'))
.. }}}
.. {{{end}}}

Linux::

    $ python platform_platform.py 
    Normal : Linux-2.6.18-194.3.1.el5-i686-with-redhat-5.5-Final
    Aliased: Linux-2.6.18-194.3.1.el5-i686-with-redhat-5.5-Final
    Terse  : Linux-2.6.18-194.3.1.el5-i686-with-glibc2.3

Windows::

    C:> python.exe platform_platform.py
    Normal : Windows-2008ServerR2-6.1.7600
    Aliased: Windows-2008ServerR2-6.1.7600
    Terse  : Windows-2008ServerR2
    
..
    Operating System and Hardware Info
    ==================================

オペレーティングシステムとハードウェアの情報
============================================

..
    More detailed information about the operating system and hardware the
    interpreter is running under can be retrieved as well. ``uname()``
    returns a tuple containing the system, node, release, version,
    machine, and processor values.  Individual values can be accessed
    through functions of the same names:

同様にインタープリタが実行されているオペレーティングシステムとハードウェアに関する詳細情報も取り出せます。 ``uname()`` はシステム、ノード、リリース、バージョン、マシン、プロセッサの値を含むタプルを返します。個々の値は、同じ名前の関数でアクセスできます。

..
    :func:`system`
      returns the operating system name
    :func:`node`
      returns the hostname of the server, not fully qualified
    :func:`release`
      returns the operating system release number
    :func:`version`
      returns the more detailed system version
    :func:`machine`
      gives a hardware-type identifier such as ``'i386'``
    :func:`processor`
      returns a real identifier for the processor, or the same value as
      machine() in many cases

:func:`system`
  オペレーティングシステム名を返す
:func:`node`
  完全修飾ではないサーバのホスト名を返す
:func:`release`
  オペレーティングシステムのリリース番号を返す
:func:`version`
  より詳細なシステムのバージョン番号を返す
:func:`machine`
  ``'i386'`` といったハードウェアタイプの識別子を返す
:func:`processor`
  プロセッサの実際の識別子か、ほとんどの場合は :func:`machine()` と同じ値を返す

.. include:: platform_os_info.py
    :literal:
    :start-after: #end_pymotw_header


OS X:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'platform_os_info.py'))
.. }}}
.. {{{end}}}

Linux::

    $ python platform_os_info.py 
    uname: ('Linux', 'hermes.hellfly.net', '2.6.18-194.3.1.el5', 
    '#1 SMP Thu May 13 13:09:10 EDT 2010', 'i686', 'i686')
    
    system   : Linux
    node     : hermes.hellfly.net
    release  : 2.6.18-194.3.1.el5
    version  : #1 SMP Thu May 13 13:09:10 EDT 2010
    machine  : i686
    processor: i686

Windows::

    C:> python.exe platform_os_info.py
    uname: ('Windows', 'dhellmann', '2008ServerR2', '6.1.7600', 'AMD64', 
    'Intel64 Family 6 Model 15 Stepping 11, GenuineIntel')

    system   : Windows
    node     : dhellmann
    release  : 2008ServerR2
    version  : 6.1.7600
    machine  : AMD64
    processor: Intel64 Family 6 Model 15 Stepping 11, GenuineIntel
    
..
    Executable Architecture
    =======================

実行可能なアーキテクチャ
========================

..
    Individual program architecture information can be probed using the
    :func:`architecture` function. The first argument is the path to an
    executable program (defaulting to ``sys.executable``, the Python
    interpreter). The return value is a tuple containing the bit
    architecture and the linkage format used.

個別のプログラムアーキテクチャの情報は :func:`architecture` 関数を使用して調べられます。最初の引数は、実行可能なプログラム(デフォルトは ``sys.executable`` の Python インタープリタ)へのパスです。返り値は、ビットアーキテクチャと使用されるリンケージフォーマットを含むタプルです。

.. include:: platform_architecture.py
    :literal:
    :start-after: #end_pymotw_header


OS X:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'platform_architecture.py'))
.. }}}
.. {{{end}}}

Linux::

    $ python platform_architecture.py 
    interpreter: ('32bit', 'ELF')
    /bin/ls    : ('32bit', 'ELF')

Windows::

    C:> python.exe platform_architecture.py
    interpreter  : ('64bit', 'WindowsPE')
    iexplore.exe : ('64bit', '')

.. seealso::

    `platform <http://docs.python.org/lib/module-platform.html>`_
        Standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント
