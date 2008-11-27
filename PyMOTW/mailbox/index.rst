===============================================
mailbox -- Access and manipulate email archives
===============================================

.. module:: mailbox
    :synopsis: Access and manipulate email archives.

:Purpose: Work with email messages in various local file formats.
:Python Version: 1.4 and later

The :mod:`mailbox` module defines a common API for accessing email messages stored in local disk formats, including:

- Maildir
- mbox
- MH
- Babyl
- MMDF

There are base classes for :class:`Mailbox` and :class:`Message`, and each mailbox format includes a corresponding pair of subclasses to implement the details for that format.

mbox
====

The mbox format is the simplest to illustrate in documentation, since it is entirely plain text.  Each mailbox is stored as a single file, with all of the messages concatenated together.  Each time a line starting with "From " (``From`` followed by a single space) is encountered it is treated as the beginning of a new message.  Any time those characters appear at the beginning of a line in the message body, they are escaped by prefixing the line with ">".

Creating an mbox mailbox
------------------------

Instantiate the ``email.mbox`` class by passing the filename to the constructor.  If the file does not exist, it is created when you add messages to it using ``add()``.

.. include:: mailbox_mbox_create.py
    :literal:
    :start-after: #end_pymotw_header

The result of this script is a new mailbox file with 2 email messages.

::

    $ python mailbox_mbox_create.py
    From MAILER-DAEMON Fri Sep 26 19:43:32 2008
    From: Author <author@example.com>
    To: Recipient <recipient@example.com>
    Subject: Sample message 1

    This is the body.
    >From (should be escaped).
    There are 3 lines.

    From MAILER-DAEMON Fri Sep 26 19:43:32 2008
    From: Author <author@example.com>
    To: Recipient <recipient@example.com>
    Subject: Sample message 2

    This is the second body.

Reading an mbox Mailbox
-----------------------

To read an existing mailbox, open it and treat the mbox object like a dictionary.  They keys are arbitrary values defined by the mailbox instance and are not necessary meaningful other than as internal identifiers for message objects.

.. include:: mailbox_mbox_read.py
    :literal:
    :start-after: #end_pymotw_header

You can iterate over the open mailbox but notice that, unlike with dictionaries, the default iterator for a mailbox works on the *values* instead of the *keys*.

::

    $ python mailbox_mbox_read.py
    Sample message 1
    Sample message 2

Removing Messages from an mbox Mailbox
--------------------------------------

To remove an existing message from an mbox file, use its key with ``remove()`` or use ``del``.

.. include:: mailbox_mbox_remove.py
    :literal:
    :start-after: #end_pymotw_header

Notice the use of ``lock()`` and ``unlock()`` to prevent issues from simultaneous access to the file, and ``flush()`` to force the changes to be written to disk.

::

    $ python mailbox_mbox_remove.py
    From MAILER-DAEMON Fri Sep 26 19:55:51 2008
    From: Author <author@example.com>
    To: Recipient <recipient@example.com>
    Subject: Sample message 1

    This is the body.
    >From (should be escaped).
    There are 3 lines.

Maildir
=======

The Maildir format was created to eliminate the problem of concurrent modification to an mbox file.  Instead of using a single file, each mailbox is a directory and each message is contained in its own file.  This also allows mailboxes to be nested, and so the API for a Maildir mailbox is extended with methods to work with sub-folders.

Creating a Maildir Mailbox
--------------------------

The only real difference between using a Maildir and mbox is that to instantiate the ``email.Maildir`` object we need to pass the directory containing the mailbox to the constructor.  As before, if it does not exist, the mailbox is created when you add messages to it using ``add()``.

.. include:: mailbox_maildir_create.py
    :literal:
    :start-after: #end_pymotw_header

Since we have added messages to the mailbox, they go to the "new" subdirectory.  Once they are "read" a client could move them to the "cur" subdirectory.

.. warning::
    Although it is safe to write to the same maildir from multiple processes, ``add()`` is not thread-safe, so make sure you use a semaphore or other locking device to prevent simultaneous modifications to the mailbox from multiple threads of the same process.

::

    $ python mailbox_maildir_create.py
    Example
    	Directories: ['cur', 'new', 'tmp']
    Example/cur
    	Directories: []
    Example/new
    	Directories: []
    
    *** Example/new/1222461341.M456778P55802Q1.farnsworth.local
    From: Author <author@example.com>
    To: Recipient <recipient@example.com>
    Subject: Sample message 1
    
    This is the body.
    From (will not be escaped).
    There are 3 lines.
    
    ********************
    
    *** Example/new/1222461341.M461013P55802Q2.farnsworth.local
    From: Author <author@example.com>
    To: Recipient <recipient@example.com>
    Subject: Sample message 2
    
    This is the second body.
    
    ********************
    Example/tmp
    	Directories: []


Reading a Maildir Mailbox
-------------------------

Reading from an existing Maildir mailbox works just like with mbox.

.. include:: mailbox_maildir_read.py
    :literal:
    :start-after: #end_pymotw_header

Notice that the messages are not guaranteed to be read in any particular order.

::

    $ python mailbox_maildir_read.py
    Sample message 2
    Sample message 1


Removing Messages from a Maildir Mailbox
----------------------------------------

To remove an existing message from a Maildir mailbox, use its key with ``remove()`` or use ``del``.

.. include:: mailbox_maildir_remove.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python mailbox_maildir_remove.py
    Removing: 1222461409.M320082P55935Q2.farnsworth.local
    Example
        Directories: ['cur', 'new', 'tmp']
    Example/cur
        Directories: []
    Example/new
        Directories: []

    *** Example/new/1222461409.M315136P55935Q1.farnsworth.local
    From: Author <author@example.com>
    To: Recipient <recipient@example.com>
    Subject: Sample message 1

    This is the body.
    From (will not be escaped).
    There are 3 lines.

    ********************
    Example/tmp
        Directories: []


Maildir folders
---------------

Subdirectories or *folders* of a Maildir mailbox can be managed directly through the methods of the Maildir class.  Callers can list, retrieve, create, and remove sub-folders for a given mailbox.

.. include:: mailbox_maildir_folders.py
    :literal:
    :start-after: #end_pymotw_header

The directory name for the folder is constructed by prefixing the folder name with ``.``.

::

    Before: []
    Example
    Example/cur
    Example/new
    Example/new/1222461409.M315136P55935Q1.farnsworth.local
    Example/tmp

    ##############################

    subfolder created: ['subfolder']
    Example
    Example/.subfolder
    Example/.subfolder/cur
    Example/.subfolder/maildirfolder
    Example/.subfolder/new
    Example/.subfolder/tmp
    Example/cur
    Example/new
    Example/new/1222461409.M315136P55935Q1.farnsworth.local
    Example/tmp
    subfolder contents: []

    ##############################

    second_level created: ['second_level']
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
    Example/new/1222461409.M315136P55935Q1.farnsworth.local
    Example/tmp

    ##############################

    second_level removed: []
    Example
    Example/.subfolder
    Example/.subfolder/cur
    Example/.subfolder/maildirfolder
    Example/.subfolder/new
    Example/.subfolder/tmp
    Example/cur
    Example/new
    Example/new/1222461409.M315136P55935Q1.farnsworth.local
    Example/tmp


Other Formats
=============

MH is another multi-file mailbox format used by some mail handlers.  Babyl and MMDF are single-file formats with different message separators than mbox.  None seem to be as popular as mbox or Maildir.  The single-file formats support the same API as mbox, and MH includes the folder-related methods found in the Maildir class.

.. seealso::

    `mailbox <http://docs.python.org/library/mailbox.html>`_
        The standard library documentation for this module.

    mbox manpage from qmail
        http://www.qmail.org/man/man5/mbox.html

    maildir manpage from qmail
        http://www.qmail.org/man/man5/maildir.html

    :mod:`email`
        The email module.

    :mod:`mhlib`
        The mhlib module.
