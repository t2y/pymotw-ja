..
    ===============================
    About Python Module of the Week
    ===============================

==================================
Python Module of the Week について
==================================

..
    PyMOTW is a series of blog posts written by `Doug Hellmann
    <http://www.doughellmann.com/>`_.  It was started as a way to build
    the habit of writing something on a regular basis.  The focus of the
    series is building a set of example code for the modules in the
    `Python <http://www.python.org/>`_ standard library.

PyMOTW は `Doug Hellmann <http://www.doughellmann.com/>`_ が執筆しているブログの連載です。当初は定期的に何かを書く習慣を身に着ける方法として始めました。この連載の主要な点は `Python <http://www.python.org/>`_ 標準ライブラリモジュールのサンプルコードを書くことです。

..
    See the project home page at http://www.doughellmann.com/PyMOTW/ for
    updates and the latest release.  Source code is available from
    http://bitbucket.org/dhellmann/pymotw/.

最新リリースや更新については、プロジェクトのホームページ(http://www.doughellmann.com/PyMOTW/ )を参照してください。ソースコードは http://bitbucket.org/dhellmann/pymotw/ から取得できます。

..
    Complete documentation for the standard library can be found on the
    Python web site at http://docs.python.org/library/.

標準ライブラリの完全なドキュメントは Python web サイト(http://docs.python.org/library/) で見つけることができます。

..
    Tools
    =====

ツール
======

..
    The source text for PyMOTW is `reStructuredText
    <http://docutils.sourceforge.net/>`_ and the HTML and PDF output are
    created using `Sphinx <http://sphinx.pocoo.org/>`_.

PyMOTW のソースは `reStructuredText <http://docutils.sourceforge.net/>`_ です。 `Sphinx <http://sphinx.pocoo.org/>`_ を利用して HTML と PDF ファイルを作成しています。

..
    Subscribe
    =========

フィード登録
============

..
    As new articles are written, they are posted to my blog
    (http://blog.doughellmann.com/).  Updates are available by RSS from
    http://feeds.doughellmann.com/PyMOTW and `email
    <http://feedburner.google.com/fb/a/mailverify?uri=PyMOTW&amp;loc=en_US>`_.

PyMOTW の新しい記事が私のブログ(http://blog.doughellmann.com/)に投稿されると、新しい記事になります。 http://feeds.doughellmann.com/PyMOTW から RSS や `メール <http://feedburner.google.com/fb/a/mailverify?uri=PyMOTW&amp;loc=en_US>`_ で更新情報を取得できます。

.. _motw-cli:

..
    The motw Command Line Interface
    ===============================

motw コマンドラインインタフェース
=================================

..
    PyMOTW includes a command line program, ``motw``, to make it even
    easier to access the examples while you are developing. Simply run
    ``motw module`` to open the local copy of the HTML text for the named
    module. There are also options to view the articles in different
    formats (see the ``-h`` output for details).

PyMOTW は開発中にサンプルコードへ簡単にアクセスできるようにコマンドラインプログラム ``motw`` が用意されています。単純に ``motw module`` と実行するとローカルにあるモジュールの HTML ファイルを表示します。またフォーマットを変更して記事を表示するオプションがあります(詳細は ``-h`` の出力を参照)。

..
    Usage: ``motw [options] <module_name>``

使用方法: ``motw [options] <module_name>``

..
    Options:
    -h, --help  show this help message and exit
    -t, --text  Print plain-text version of help to stdout
    -w, --web   Open HTML version of help from web
    --html      Open HTML version of help from installed file

オプション:

    -h, --help  ヘルプメッセージを表示する
    -t, --text  標準出力にヘルプのプレーンテキスト版を表示する
    -w, --web   ウェブからヘルプの HTML 版を開く
    --html      インストールされたファイルからヘルプの HTML 版を開く

.. _motw-interactive:

..
    Using PyMOTW with the Interactive Interpreter
    =============================================

PyMOTW をインタラクティブインタプリタで使用する
===============================================

..
    PyMOTW articles are at your fingertips while you're working with the
    Python interactive interpreter.  Importing ``PyMOTW`` adds the
    function ``motw()`` to the ``__builtins__`` namespace.  Run
    ``motw(module)`` to see the help for an imported module.  Enclose the
    name in quotes for a module that you haven't already imported.

PyMOTW の記事を Python インタラクティブインタプリタの実行中に見ることができます。 ``PyMOTW`` をインポートして ``motw()`` 関数を ``__builtins__`` 名前空間へ追加してください。そしてインポートされたモジュールのヘルプを見るために ``motw(module)`` を実行してください。見たいモジュールがインポートされていないときはモジュール名をクォートしてください。

::

    $ python
    Python 2.6.2 (r262:71600, Apr 16 2009, 09:17:39) 
    [GCC 4.0.1 (Apple Computer, Inc. build 5250)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import PyMOTW
    >>> motw('atexit')
    
    atexit -- Call functions when a program is closing down
    *******************************************************
    ...

.. _translations:

..
    Translations and Other Versions
    ===============================

翻訳や他のバージョン
====================

..
    `Chinese <http://www.vbarter.cn/pymotw/>`_
..
  Junjie Cai (蔡俊杰) and Yan Sheng (盛艳) have started a google code
  project called PyMOTWCN (http://code.google.com/p/pymotwcn/) and
  posted the completed translations at http://www.vbarter.cn/pymotw/.

`中国語 <http://www.vbarter.cn/pymotw/>`_

  Junjie Cai (蔡俊杰) と Yan Sheng (盛艳) は PyMOTWCN (http://code.google.com/p/pymotwcn/) という google code プロジェクトを始めました。 http://www.vbarter.cn/pymotw/ に完全な翻訳を投稿しています。

..
    `German <http://schoenian-online.de/pymotw.html>`_
..
  Ralf Schönian is translating PyMOTW into German, following an
  alphabetical order.  The results are available on his web site,
  http://schoenian-online.de/pymotw.html.  Ralf is an active member of
  the `pyCologne
  <http://wiki.python.de/User_Group_K%C3%B6ln?action=show&redirect=pyCologne>`_
  user group in Germany and author of pyVoc, the open source
  English/German vocabulary trainer (http://code.google.com/p/pyvoc/).

`ドイツ語 <http://schoenian-online.de/pymotw.html>`_

  Ralf Schönian はアルファベット順に PyMOTW をドイツ語に翻訳しています。その成果は彼の web サイト http://schoenian-online.de/pymotw.html で確認できます。Ralf はドイツの `pyCologne <http://wiki.python.de/User_Group_K%C3%B6ln?action=show&redirect=pyCologne>`_ ユーザグループのアクティブメンバーで、オープンソースの英語/ドイツ語のボキャブラリトレーナーである pyVoc (http://code.google.com/p/pyvoc/) の開発者です。

..
    `Italian <http://robyp.x10hosting.com/>`_
..
   Roberto Pauletto is working on an Italian translation at
   http://robyp.x10hosting.com/.  Roberto creates Windows applications
   with C# by day, and tinkers with Linux and Python at home.  He has
   recently moved to Python from Perl for all of his
   system-administration scripting.

`イタリア語 <http://robyp.x10hosting.com/>`_

  Roberto Pauletto が http://robyp.x10hosting.com/ でイタリア語翻訳をしています。Roberto は昼間は Windows アプリケーションを C# で開発していて、自宅では Linux と Python をいじくり回しています。彼は最近、開発した全てのシステム管理用スクリプトを Perl から Python へ移行しました。

..
    `Spanish <http://denklab.org/articles/category/pymotw/>`_
..
  `Ernesto Rico Schmidt <http://denklab.org/>`_ provides a Spanish
  translation that follows the English version posts. Ernesto is in
  Bolivia, and is translating these examples as a way to contribute to
  the members of the `Bolivian Free Software
  <http://www.softwarelibre.org.bo/>`_ community who use Python.  The
  full list of articles available in Spanish can be found at
  http://denklab.org/articles/category/pymotw/, and there is an `RSS
  feed <http://denklab.org/feeds/articles/category/pymotw/>`_.

`スペイン語 <http://denklab.org/articles/category/pymotw/>`_

  `Ernesto Rico Schmidt <http://denklab.org/>`_ は英語版の投稿を見ながらスペイン語翻訳を提供しています。Ernesto は Bolivia に住んでいて、Python を使用する `Bolivian Free Software <http://www.softwarelibre.org.bo/>`_ コミュニティメンバーへの貢献手段の1つの例として翻訳しています。スペイン語の記事の完全なリストは http://denklab.org/articles/category/pymotw/ で発見できます。 `RSS フィード <http://denklab.org/feeds/articles/category/pymotw/>`_ も提供されています。

..
    `Japanese <http://www.doughellmann.com/PyMOTW-ja/>`_
..
  `Tetsuya Morimoto <http://d.hatena.ne.jp/t2y-1979/>`_ is creating a
  Japanese translation. Tetsuya has used Python for 1.5 years. He has
  as experience at a Linux Distributor using Python with yum,
  anaconda, and rpm-tools while building RPM packages. Now, he uses it
  to make useful tools for himself, and is interested in application
  frameworks such as Django, mercurial and wxPython. Tetsuya is a
  member of `Python Japan User's Group <http://www.python.jp/Zope/>`_
  and `Python Code Reading
  <http://groups.google.co.jp/group/python-code-reading>`_. The home
  page for his translation is http://www.doughellmann.com/PyMOTW-ja/.

`日本語 <http://www.doughellmann.com/PyMOTW-ja/>`_

  `Tetsuya Morimoto <http://d.hatena.ne.jp/t2y-1979/>`_ は日本語翻訳をしています。Tetsuya は Python を 1.5 年程度使っています。彼は Linux ディストリビュータで働いていた頃 RPM パッケージのビルド等に yum, anaconda や rpm-tools で Python を使用していました。現在は自分用のツールを開発したりして Django, mercurial や wxPython 等のアプリケーションフレームワークに興味を持っています。Tetsuya は `Python Japan User's Group <http://www.python.jp/Zope/>`_ や `Python Code Reading <http://groups.google.co.jp/group/python-code-reading>`_ のメンバーです。日本語翻訳は http://www.doughellmann.com/PyMOTW-ja/ にあります。

..
    Compendiums
    -----------

抄録
----

..
    Gerard Flanagan is working on a "Python compendium" called `The Hazel
    Tree <http://www.thehazeltree.org/>`_.  He is converting a collection
    of old and new of Python-related reference material into
    reStructuredText and then building a single searchable repository from
    the results.  I am very pleased to have PyMOTW included with works
    from authors like Mark Pilgrim, Fredrik Lundh, Andrew Kuchling, and a
    growing list of others.

Gerard Flanagan は `The Hazel Tree <http://www.thehazeltree.org/>`_ という "Python 抄録" を作成しています。彼は Python に関連する新旧のリファレンス資料を reStructuredText へ変換しています。そして、その結果から1つの検索可能なリポジトリを構築します。私は Mark Pilgrim, Fredrik Lundh, Andrew Kuchling のような著者やさらに他の著者も増え続けるそのリストへ PyMOTW が追加されてとても嬉しいです。

..
    Other Contributors
    ==================

その他の貢献者
==============

..
    Thank you to John Benediktsson for the original HTML-to-reST
    conversion.

オリジナルの HTML から reST への変換を手伝ってくれた John Benediktsson に感謝します。

.. include:: copyright.rst
