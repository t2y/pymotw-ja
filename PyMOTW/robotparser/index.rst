..
    =============================================
    robotparser -- Internet spider access control
    =============================================

=====================================================
robotparser -- インターネットスパイダーのアクセス制御
=====================================================

..
    :synopsis: Internet spider access control

.. module:: robotparser
    :synopsis: インターネットスパイダーのアクセス制御

..
    :Purpose: Parse robots.txt file used to control Internet spiders
    :Available In: 2.1.3 and later

:目的: インターネットスパイダーを制御する robots.txt ファイルを解析する
:利用できるバージョン: 2.1.3 以上

..
    :mod:`robotparser` implements a parser for the ``robots.txt`` file format, including a simple function for checking if a given user agent can access a resource.  It is intended for use in well-behaved spiders or other crawler applications that need to either be throttled or otherwise restricted.

:mod:`robotparser` は、あるユーザエージェントがリソースへアクセスできるかどうかをチェックするシンプルな仕組みを含む ``robots.txt`` ファイルフォーマットのパーサを実装します。それはスパイダー、もしくは他のクローラーアプリケーションの動作を調整したり、制限したりする必要があることを想定しています。

.. note::

    .. The :mod:`robotparser` module has been renamed :mod:`urllib.robotparser` in Python 3.0.
       Existing code using :mod:`robotparser` can be updated using 2to3.

    :mod:`robotparser` モジュールは Python 3.0 で :mod:`urllib.robotparser` に変更されました。 :mod:`robotparser` を使用する既存のコードは 2to3 で変更されます。

robots.txt
==========

..
    The ``robots.txt`` file format is a simple text-based access control system for computer programs that automatically access web resources ("spiders", "crawlers", etc.).  The file is made up of records that specify the user agent identifier for the program followed by a list of URLs (or URL prefixes) the agent may not access.  

``robots.txt`` ファイルフォーマットは、web を自動徘徊してリソースへアクセスするプログラム("スパイダー" や "クローラー" 等)向けのシンプルなテキストベースのアクセス制御システムです。そのファイルは、ユーザエージェントがアクセスする必要のない URL リスト(または URL の接頭辞)をそういったプログラム向けに提供し、ユーザエージェントの識別子を指定するレコードで構成されます。

..
    This is the ``robots.txt`` file for ``http://www.doughellmann.com/``:

これは ``http://www.doughellmann.com/`` の ``robots.txt`` ファイルです。

.. include:: robots.txt
    :literal:

..
    It prevents access to some of the expensive parts of my site that would overload the server if a search engine tried to index them.  For a more complete set of examples, refer to `The Web Robots Page`_.

検索エンジンが私のサイトの重いページをインデクシングしようとすると、サーバが高負荷になるので、そういったページへのアクセスを制限しています。もっと詳細なサンプルとしては `The Web Robots Page`_ を参照してください。

..
    Simple Example
    ==============

シンプルなサンプル
==================

..
    Using the data above, a simple crawler can test whether it is allowed to download a page using the ``RobotFileParser``'s ``can_fetch()`` method.

前節のデータを使用して、シンプルなクローラが ``RobotFileParser`` の ``can_fetch()`` メソッドでページをダウンロードできるかどうかテストします。

.. include:: robotparser_simple.py
    :literal:
    :start-after: #end_pymotw_header

..
    The URL argument to ``can_fetch()`` can be a path relative to the root of the site, or full URL.

``can_fetch()`` への URL 引数はそのサイトのルートへの相対パスか、完全な URL で指定します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'robotparser_simple.py'))
.. }}}

::

	$ python robotparser_simple.py
	
	  True : /
	  True : http://www.doughellmann.com/
	
	  True : /PyMOTW/
	  True : http://www.doughellmann.com/PyMOTW/
	
	  True : /admin/
	  True : http://www.doughellmann.com/admin/
	
	 False : /downloads/PyMOTW-1.92.tar.gz
	 False : http://www.doughellmann.com/downloads/PyMOTW-1.92.tar.gz
	

.. {{{end}}}


..
    Long-lived Spiders
    ==================

長時間処理するスパイダー
========================

..
    An application that takes a long time to process the resources it downloads or that is throttled to pause between downloads may want to check for new ``robots.txt`` files periodically based on the age of the content it has downloaded already.  The age is not managed automatically, but there are convenience methods to make tracking it easier.

リソースをダウンロードする処理に長時間かかる、もしくはダウンロード中に一時停止するように調整されたアプリケーションは、既にダウンロード済みのコンテンツの age ヘッダに基づいて定期的に新しい ``robots.txt`` ファイルをチェックすると良いです。この age の時間は自動的に制御されませんが、簡単にその時間を記録する便利なメソッドがあります。

.. include:: robotparser_longlived.py
    :literal:
    :start-after: #end_pymotw_header

..
    This extreme example downloads a new ``robots.txt`` file if the one it has is more than 1 second old.

この極端なサンプルは、1秒後に新たな ``robots.txt`` ファイルをダウンロードします。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'robotparser_longlived.py'))
.. }}}

::

	$ python robotparser_longlived.py
	
	
	age: 0
	  True : /
	
	age: 1
	  True : /PyMOTW/
	
	age: 2 re-reading robots.txt
	 False : /admin/
	
	age: 1
	 False : /downloads/PyMOTW-1.92.tar.gz

.. {{{end}}}

..
    A "nicer" version of the long-lived application might request the modification time for the file before downloading the entire thing.  On the other hand, ``robots.txt`` files are usually fairly small, so it isn't that much more expensive to just grab the entire document again.

長時間処理するアプリケーションの "もっと良い" 実装は、そのファイルをダウンロードする前にファイル更新時刻をリクエストします。ただ、普通は ``robots.txt`` ファイルのサイズはかなり小さいので、再読み込みしてもそう大きな負荷にはなりません。

.. seealso::

    `robotparser <http://docs.python.org/library/robotparser.html>`_
        .. The standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント

    `The Web Robots Page`_
        .. Description of robots.txt format.

        robots.txt のフォーマット説明

.. _The Web Robots Page: http://www.robotstxt.org/orig.html
