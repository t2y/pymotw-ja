..
    ===============================================
    plistlib -- Manipulate OS X property list files
    ===============================================

=====================================================
plistlib -- Mac OS X のプロパティリストファイルを扱う
=====================================================

..
    :synopsis: Manipulate OS X property list files

.. module:: plistlib
    :synopsis: Mac OS X のプロパティリストファイルを扱う

..
    :Purpose: Read and write OS X property list files
    :Python Version: 2.6

:目的: Mac OS X のプロパティリストファイルを読み書きする
:Python バージョン: 2.6

..
    :mod:`plistlib` provides an interface for working with property list
    files used under OS X.  plist files are typically XML, sometimes
    compressed.  They are used by the operating system and applications to
    store preferences or other configuration settings.  The contents are
    usually structured as a dictionary containing key value pairs of basic
    built-in types (unicode strings, integers, dates, etc.).  Values can
    also be nested data structures such as other dictionaries or lists.
    Binary data, or strings with control characters, can be encoded using
    the ``data`` type.

:mod:`plistlib` は、Mac OS X 環境で使用されるプロパティリストを扱うインタフェースを提供します。plist ファイルは、普通は XML ファイルですが、たまに圧縮されています。それは OS やアプリケーションが設定を保存するために使用します。そのコンテンツは、通常、基本的な組み込み型(ユニコード文字列、整数、日付等)のキーと値を含むディクショナリとして構成されます。また、その値は他のディクショナリやリストを含むネストしたデータ構造でも構いません。バイナリデータや制御文字を含む文字列は ``data`` 型でエンコードされます。

..
    Reading plist Files
    ===================

plist ファイルを読み込む
========================

..
    OS X applications such as iCal use plist files to store meta-data
    about objects they manage.  For example, iCal stores the definitions
    of all of your calendars as a series of plist files in the Library
    directory.  

iCal のような Mac OS X アプリケーションは、管理するオブジェクトについてのメタデータを保存するために plist ファイルを使用します。例えば、iCal はライブラリディクショナリに一連の plist ファイルとしてカレンダーの全ての定義を格納します。

.. literalinclude:: Info.plist
   :language: xml

..
    This sample script finds the calendar defintions, reads
    them, and prints the titles of any calendars being displayed by iCal
    (having the property ``Checked`` set to a true value).

このサンプルスクリプトは、plist ファイルを読み込んでからカレンダー定義を探して、iCal が表示する(``Checked`` プロパティが True にセットされている)任意のカレンダーのタイトルを表示します。

.. include:: plistlib_checked_calendars.py
   :literal:
   :start-after: #end_pymotw_header

..
    The type of the ``Checked`` property is defined by the plist file, so
    our script does not need to convert the string to an integer.

``Checked`` プロパティの型は plist ファイルによって定義されるので、このサンプルスクリプトが文字列から整数へ変換する必要はありません。

::

	$ python plistlib_checked_calendars.py
	Doug Hellmann
	Tasks
	Vacation Schedule
	EarthSeasons
	US Holidays
	Athens, GA Weather - By Weather Underground
	Birthdays
	Georgia Bulldogs Calendar (NCAA Football)
	Home
	Meetup: Django
	Meetup: Python

..
    Writing plist Files
    ===================

plist ファイルを書き込む
========================

..
    If you want to use plist files to save your own settings, use
    ``writePlist()`` to serialize the data and write it to the filesystem.

もし plist ファイルに独自の設定を保存したいなら、データをシリアライズしてファイルシステム上のファイルへ書き込むのに ``writePlist()`` を使用してください。

.. include:: plistlib_write_plist.py
   :literal:
   :start-after: #end_pymotw_header

..
    The first argument is the data structure to write out, and the second
    is an open file handle or the name of a file.

1番目の引数は書き込むデータ構造で、2番目の引数はオープンされたファイルハンドラか、ファイル名です。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'plistlib_write_plist.py'))
.. }}}
.. {{{end}}}

..
    Binary Property Data
    ====================

バイナリプロパティデータ
========================

..
    Serializing binary data or strings that may include control characters
    using a plist is not immune to the typical challenges for an XML
    format.  To work around the issues, plist files can store binary data
    in :mod:`base64` format if the object is wrapped with a ``Data``
    instance.

plist を使用して制御文字を含む可能性がある文字列やバイナリデータをシリアライズすることは、XML フォーマットの典型的な問題を回避しません。この問題のワークアラウンドとして、そのオブジェクトが ``Data`` インスタンスでラップされる場合、plist ファイルは :mod:`base64` フォーマットでバイナリデータを格納できます。

.. include:: plistlib_binary_write.py
   :literal:
   :start-after: #end_pymotw_header

..
    This example uses the ``writePlistToString()`` to create an in-memory
    string, instead of writing to a file.

このサンプルは、ファイルへ書き込むのではなく、インメモリ文字列を作成するために ``writePlistToString()`` を使用します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'plistlib_binary_write.py'))
.. }}}
.. {{{end}}}

..
    Binary data is automatically converted to a ``Data`` instance when
    read.

バイナリデータは、読み込み時に自動的に ``Data`` インスタンスに変換されます。

.. include:: plistlib_binary_read.py
   :literal:
   :start-after: #end_pymotw_header

..
    The ``data`` attribute of the object contains the decoded data.

このオブジェクトの ``data`` 属性はデコードされたデータを含みます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'plistlib_binary_read.py'))
.. }}}
.. {{{end}}}



.. seealso::

    `plistlib <http://docs.python.org/library/plistlib.html>`_
        .. The standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント

    `plist manual page <http://developer.apple.com/documentation/Darwin/Reference/ManPages/man5/plist.5.html>`_
        .. Documentation of the plist file format.

        plist ファイルフォーマットのドキュメント

    `Weather Underground <http://www.wunderground.com/>`_
        .. Free weather information, including ICS and RSS feeds.

        ICS や RSS フィードを提供するフリーの天気情報

    `Convert plist between XML and Binary formats <http://www.macosxhints.com/article.php?story=20050430105126392>`_
        .. Some plist files are stored in a binary format instead of XML
           because the binary format is faster to parse using Apple's
           libraries.  Python's plistlib module does not handle the
           binary format, so you may need to convert binary files to XML
           using ``plutil`` before reading them.

        plist ファイルによっては XML ではなくバイナリフォーマットに格納されます。それはバイナリフォーマットの方が Apple のライブラリを使用して解析するのが速いからです。Python の plistlib モジュールはバイナリフォーマットを扱わないので、バイナリファイルを読み込む前に ``plutil`` で XML ファイルに変換する必要があるかもしれません。


    `Using Python for System Administration <http://docs.google.com/present/view?id=0AW0cyKASCypUZGczODJ6YjdfMjRobW16dG5mNQ&hl=en>`_
        .. Presentation from Nigel Kersten and Chris Adams, including
           details of using PyObjC to load plists using the native Cocoa
           API, which transparently handles both the XML and binary
           formats.  See slice 27, especially.

        ネイティブの Cocoa API で plist をロードするために PyObjC 使用の詳細についての Nigel Kersten と Chris Adams の発表内容です。それは透過的に XML とバイナリフォーマットの両方を扱います。特に 27 ページ以降が参考になります。
