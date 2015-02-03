..
    ===============================================
    mailbox -- Access and manipulate email archives
    ===============================================

===========================================
mailbox -- メールアーカイブのアクセスと操作
===========================================

..
    :synopsis: Access and manipulate email archives.

.. module:: mailbox
    :synopsis: メールアーカイブのアクセスと操作

..
    :Purpose: Work with email messages in various local file formats.
    :Available In: 1.4 and later

:目的: 様々なローカルファイルフォーマットのメールを扱う
:利用できるバージョン: 1.4 以上

..
    The :mod:`mailbox` module defines a common API for accessing email
    messages stored in local disk formats, including:

:mod:`mailbox` モジュールはローカルファイルフォーマットに格納されたメールのメッセージにアクセスする共通 API を定義します。

- Maildir
- mbox
- MH
- Babyl
- MMDF

..
    There are base classes for :class:`Mailbox` and :class:`Message`, and
    each mailbox format includes a corresponding pair of subclasses to
    implement the details for that format.

:class:`Mailbox` と :class:`Message` という2つのベースクラスがあります。各メールボックスのフォーマットは、そのフォーマットの詳細を実装した対応するサブクラスのペアを含みます。

mbox
====

..
    The mbox format is the simplest to illustrate in documentation, since
    it is entirely plain text.  Each mailbox is stored as a single file,
    with all of the messages concatenated together.  Each time a line
    starting with "From " (``From`` followed by a single space) is
    encountered it is treated as the beginning of a new message.  Any time
    those characters appear at the beginning of a line in the message
    body, they are escaped by prefixing the line with "``>``".

mbox フォーマットは全てプレーンテキストなので文章で説明することが最も簡単です。各メールボックスは全てのメッセージを連結した1つのファイルとして格納されます。"From " (``From`` の後にスペースが1個続く) で始まる行に遭遇すると、新たなメッセージの始まりとして扱われます。メッセージ本文の行頭に "From " が現れたときその行の接頭辞として "``>``" でエスケープします。

..
    Creating an mbox mailbox
    ------------------------

mbox メールボックスを作成する
-----------------------------

..
    Instantiate the ``email.mbox`` class by passing the filename to the
    constructor.  If the file does not exist, it is created when you add
    messages to it using ``add()``.

``email.mbox`` クラスのコンストラクタにファイル名を渡してインスタンス化してください。もしそのファイルが存在しなかったら ``add()`` を使用してそのメールボックスにメッセージを追加するときにメールボックスが作成されます。

.. include:: mailbox_mbox_create.py
    :literal:
    :start-after: #end_pymotw_header

..
    The result of this script is a new mailbox file with 2 email messages.

このスクリプトの実行結果は2つのメッセージを持つ新たなメールボックスが作成されます。

.. {{{cog
.. from paver.path import path
.. (path(cog.inFile).dirname() / 'example.mbox').unlink()
.. cog.out(run_script(cog.inFile, 'mailbox_mbox_create.py'))
.. }}}

::

	$ python mailbox_mbox_create.py
	
	From MAILER-DAEMON Thu Feb 21 11:35:54 2013
	From: Author <author@example.com>
	To: Recipient <recipient@example.com>
	Subject: Sample message 1
	
	This is the body.
	>From (should be escaped).
	There are 3 lines.
	
	From MAILER-DAEMON Thu Feb 21 11:35:54 2013
	From: Author <author@example.com>
	To: Recipient <recipient@example.com>
	Subject: Sample message 2
	
	This is the second body.
	

.. {{{end}}}

..
    Reading an mbox Mailbox
    -----------------------

mbox メールボックスを読み込む    
-----------------------------

..
    To read an existing mailbox, open it and treat the mbox object like a
    dictionary.  They keys are arbitrary values defined by the mailbox
    instance and are not necessary meaningful other than as internal
    identifiers for message objects.

既存のメールボックスを読むには、そのメールボックスをオープンして辞書のように mbox オブジェクトを扱います。メッセージオブジェクトはメールボックスインスタンスが定義した任意の値をキーに取りますが、そのオブジェクトの内部的な識別子として以外に意味はありません。

.. include:: mailbox_mbox_read.py
    :literal:
    :start-after: #end_pymotw_header

..
    You can iterate over the open mailbox but notice that, unlike with
    dictionaries, the default iterator for a mailbox works on the *values*
    instead of the *keys*.

オープンしたメールボックスは繰り返し処理することができますが、辞書とは違い、メールボックスのデフォルトイテレータは *キー* の代わりに *値* で動作します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'mailbox_mbox_read.py'))
.. }}}

::

	$ python mailbox_mbox_read.py
	
	Sample message 1
	Sample message 2

.. {{{end}}}

..
    Removing Messages from an mbox Mailbox
    --------------------------------------

mbox メールボックスからメッセージを削除する
-------------------------------------------

..
    To remove an existing message from an mbox file, use its key with
    ``remove()`` or use ``del``.

mbox ファイルから既存メッセージを削除するには ``remove()`` メソッドにそのキーを渡すか ``del`` を使用してください。

.. include:: mailbox_mbox_remove.py
    :literal:
    :start-after: #end_pymotw_header

..
    Notice the use of ``lock()`` and ``unlock()`` to prevent issues from
    simultaneous access to the file, and ``flush()`` to force the changes
    to be written to disk.

メールボックスのファイルに対する同時アクセス問題を防ぐために ``lock()`` や ``unlock()`` を使用していることに注意してください。そして、強制的にその変更内容をディスクへ書き込むために ``flush()`` します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'mailbox_mbox_remove.py'))
.. }}}

::

	$ python mailbox_mbox_remove.py
	
	Removing: 1
	From MAILER-DAEMON Thu Feb 21 11:35:54 2013
	From: Author <author@example.com>
	To: Recipient <recipient@example.com>
	Subject: Sample message 1
	
	This is the body.
	>From (should be escaped).
	There are 3 lines.
	

.. {{{end}}}

Maildir
=======

..
    The Maildir format was created to eliminate the problem of concurrent
    modification to an mbox file.  Instead of using a single file, the
    mailbox is organized as directory where each message is contained in
    its own file.  This also allows mailboxes to be nested, and so the API
    for a Maildir mailbox is extended with methods to work with
    sub-folders.

1つの mbox ファイルの同時アクセスによる変更の問題を解決するために Maildir フォーマットが作成されました。1つのファイルを使用するのではなく、メールボックスをディレクトリとして構成して各メッセージをそのディレクトリ内に保存します。また Maildir メールボックスの API はサブフォルダでも動作するようにメソッドが拡張されているのでネストされたメールボックスも扱うことができます。

..
    Creating a Maildir Mailbox
    --------------------------

Maildir メールボックスを作成する
--------------------------------

..
    The only real difference between using a Maildir and mbox is that to
    instantiate the ``email.Maildir`` object we need to pass the directory
    containing the mailbox to the constructor.  As before, if it does not
    exist, the mailbox is created when you add messages to it using
    ``add()``.

Maildir と mbox の使用における実際の違いは ``email.Maildir`` オブジェクトをインスタンス化するためにコンストラクタへメールボックスを含むディレクトリを渡す必要がある点のみになります。mbox のセクションで説明した通り、もしディレクトリが存在しなかったら ``add()`` を使用してメッセージを追加したときにメールボックスが作成されます。

.. include:: mailbox_maildir_create.py
    :literal:
    :start-after: #end_pymotw_header

..
    Since we have added messages to the mailbox, they go to the "new"
    subdirectory.  Once they are "read" a client could move them to the
    "cur" subdirectory.

メールボックスへメッセージを追加すると "new" サブディレクトリにそのメッセージが追加されます。メールクライアントがそのメッセージを "読み込む" と "cur" サブディレクトリへ移動されます。

.. warning::
    .. Although it is safe to write to the same maildir from multiple
       processes, ``add()`` is not thread-safe, so make sure you use a
       semaphore or other locking device to prevent simultaneous
       modifications to the mailbox from multiple threads of the same
       process.

    複数プロセスから同じ Maildir へ書き込むことは安全ですが ``add()`` はスレッドセーフではありません。そのため、同一プロセスの複数スレッドからメールボックスへ同時アクセスによる変更を防ぐためにセマフォ又はロックの仕組みを使用するようにしてください。

.. {{{cog
.. from paver.path import path
.. (path(cog.inFile).dirname() / 'Example').rmtree()
.. cog.out(run_script(cog.inFile, 'mailbox_maildir_create.py'))
.. }}}

::

	$ python mailbox_maildir_create.py
	
	Example
		Directories: ['cur', 'new', 'tmp']
	Example/cur
		Directories: []
	Example/new
		Directories: []
	
	*** Example/new/1361446554.M933748P13757Q1.hubert.local
	From: Author <author@example.com>
	To: Recipient <recipient@example.com>
	Subject: Sample message 1
	
	This is the body.
	From (will not be escaped).
	There are 3 lines.
	
	********************
	
	*** Example/new/1361446554.M963206P13757Q2.hubert.local
	From: Author <author@example.com>
	To: Recipient <recipient@example.com>
	Subject: Sample message 2
	
	This is the second body.
	
	********************
	Example/tmp
		Directories: []

.. {{{end}}}

..
    Reading a Maildir Mailbox
    -------------------------

Maildir メールボックスを読み込む
--------------------------------

..
    Reading from an existing Maildir mailbox works just like with mbox.

やはり mbox と同じように既存の Maildir メールボックスから読み込んでください。

.. include:: mailbox_maildir_read.py
    :literal:
    :start-after: #end_pymotw_header

..
    Notice that the messages are not guaranteed to be read in any
    particular order.

メッセージは指定した特定の順番で読めないことに注意してください。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'mailbox_maildir_read.py'))
.. }}}

::

	$ python mailbox_maildir_read.py
	
	Sample message 2
	Sample message 1

.. {{{end}}}

..
    Removing Messages from a Maildir Mailbox
    ----------------------------------------

Maildir メールボックスからメッセージを削除する
----------------------------------------------

..
    To remove an existing message from a Maildir mailbox, use its key with
    ``remove()`` or use ``del``.

Maildir メールボックスから既存メッセージを削除するには ``remove()`` メソッドにそのキーを渡すか ``del`` を使用してください。

.. include:: mailbox_maildir_remove.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'mailbox_maildir_remove.py'))
.. }}}

::

	$ python mailbox_maildir_remove.py
	
	Removing: 1361446554.M963206P13757Q2.hubert.local
	Example
		Directories: ['cur', 'new', 'tmp']
	Example/cur
		Directories: []
	Example/new
		Directories: []
	
	*** Example/new/1361446554.M933748P13757Q1.hubert.local
	From: Author <author@example.com>
	To: Recipient <recipient@example.com>
	Subject: Sample message 1
	
	This is the body.
	From (will not be escaped).
	There are 3 lines.
	
	********************
	Example/tmp
		Directories: []

.. {{{end}}}

..
    Maildir folders
    ---------------

Maildir フォルダ
----------------

..
    Subdirectories or *folders* of a Maildir mailbox can be managed
    directly through the methods of the Maildir class.  Callers can list,
    retrieve, create, and remove sub-folders for a given mailbox.

Maildir メールボックスのサブディレクトリ又は *フォルダ* は Maildir クラスのメソッドを通して直接管理できます。メソッドを呼び出すと、所定のメールボックスのサブフォルダに対する一覧表示、取り出し、作成、削除ができます。

.. include:: mailbox_maildir_folders.py
    :literal:
    :start-after: #end_pymotw_header

..
    The directory name for the folder is constructed by prefixing the
    folder name with ``.``.

フォルダのディレクトリ名は ``.`` から始まるフォルダ名で構成されます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'mailbox_maildir_folders.py'))
.. }}}

::

	$ python mailbox_maildir_folders.py
	
	Example
	Example/cur
	Example/new
	Example/new/1361446554.M933748P13757Q1.hubert.local
	Example/tmp
	Example
	Example/.subfolder
	Example/.subfolder/cur
	Example/.subfolder/maildirfolder
	Example/.subfolder/new
	Example/.subfolder/tmp
	Example/cur
	Example/new
	Example/new/1361446554.M933748P13757Q1.hubert.local
	Example/tmp
	Example
	Example/.subfolder
	Example/.subfolder/.second_level
	Example/.subfolder/.second_level/cur
	Example/.subfolder/.second_level/maildirfolder
	Example/.subfolder/.second_level/new
	Example/.subfolder/.second_level/tmp
	Example/.subfolder/cur
	Example/.subfolder/maildirfolder
	Example/.subfolder/new
	Example/.subfolder/tmp
	Example/cur
	Example/new
	Example/new/1361446554.M933748P13757Q1.hubert.local
	Example/tmp
	Example
	Example/.subfolder
	Example/.subfolder/cur
	Example/.subfolder/maildirfolder
	Example/.subfolder/new
	Example/.subfolder/tmp
	Example/cur
	Example/new
	Example/new/1361446554.M933748P13757Q1.hubert.local
	Example/tmp
	Before: []
	
	##############################
	
	subfolder created: ['subfolder']
	subfolder contents: []
	
	##############################
	
	second_level created: ['second_level']
	
	##############################
	
	second_level removed: []

.. {{{end}}}

..
    Other Formats
    =============

その他のフォーマット
====================

..
    MH is another multi-file mailbox format used by some mail handlers.
    Babyl and MMDF are single-file formats with different message
    separators than mbox.  None seem to be as popular as mbox or Maildir.
    The single-file formats support the same API as mbox, and MH includes
    the folder-related methods found in the Maildir class.

MH は幾つかのメールハンドラで使用される複数ファイルの別のメールボックスフォーマットです。Babyl や MMDF は mbox とは違うメッセージセパレータを持つ1ファイルフォーマットです。こういったフォーマットは mbox や Maildir ほど一般的ではないと思います。Babyl や MMDF は mbox と同じ API を、MH は Maildir クラスにあるフォルダ関連のメソッドをサポートします。

.. seealso::

    `mailbox <http://docs.python.org/library/mailbox.html>`_
        .. The standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント

    mbox manpage from qmail
        http://www.qmail.org/man/man5/mbox.html

    maildir manpage from qmail
        http://www.qmail.org/man/man5/maildir.html

    :mod:`email`
        .. The email module.

        email モジュール

    :mod:`mhlib`
        .. The mhlib module.

        mhlib モジュール
