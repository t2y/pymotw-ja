..
    =================================
    tabnanny -- Indentation validator
    =================================

================================
tabnanny -- インデントバリデータ
================================

..
    :synopsis: Scan Python source code looking for suspicious indentation.

.. module:: tabnanny
    :synopsis: Python のソースコードから不審なインデントを探して検査する

..
    :Purpose: Scan Python source code looking for suspicious indentation.
    :Available In: 2.1.3 and later

:目的: Python のソースコードから不審なインデントを探して検査する
:利用できるバージョン: 2.1.3 以上

..
    Consistent use of indentation is important in a langauge like Python,
    where white-space is significant.  The :mod:`tabnanny` module provides
    a scanner to report on "ambiguous" use of indentation.

Python のようなプログラミング言語では、スペースが重要な意味を持つので一貫したインデントを使用することが重要です。 :mod:`tabnanny` モジュールは "不明瞭な" インデントの使用を検出する機能を提供します。

..
    Running from the Command Line
    =============================

コマンドラインから実行する
==========================

..
    The simplest way to use :mod:`tabnanny` is to run it from the command
    line, passing the names of files to check.  If you pass directory
    names, the directories are scanned recursively to find `.py` files to
    check.

:mod:`tabnanny` を使用する最も簡単な方法は検査するファイル名を渡してコマンドラインから実行します。ディレクトリ名を渡せば、そのディレクトリに含まれる `.py` を再帰的に探して検査します。

..
    When I ran tabnanny across the PyMOTW source code, I found one old
    module with tabs instead of spaces::

PyMOTW のソースコードに対して tabnanny を実行したとき、スペースではなくタブでコーディングされた古いモジュールを発見しました。

::

    $ python -m tabnanny .
    ./PyMOTW/Queue/fetch_podcasts.py 78 "\t\tfor enclosure in entry.get('enclosures', []):\n"

..
    Sure enough, line 78 of `fetch_podcasts.py` had two tabs instead of 8
    spaces.  I didn't see this by looking at it in my editor because I
    have my tabstops set to 4 spaces, so visually there was no difference.

案の定 `fetch_podcasts.py` の78行目に8つのスペースではなく2つのタブがありました。私は tabstop を4スペースに設定していて見た目には違いがないので、エディタで見ているだけではこのことを見つけられませんでした。

::

        for enclosure in entry.get('enclosures', []):
            print 'Queuing:', enclosure['url']
            enclosure_queue.put(enclosure['url'])

..
    Correcting line 78 and running tabnanny again showed another error on
    line 79.  One last problem showed up on line 80.

78行目を修正してもう一度 tabnanny を実行すると79行目に別のエラーが出ました。最後にもう一度80行目にも問題がありました。

..
    If you want to scan files, but not see the details about the error,
    you can use the `-q` option to suppress all information except the
    filename.

ファイルを検査してもエラーの詳細を見たくないなら、ファイル名以外の情報を抑制する `-q` オプションを使用します。

::

    $ python -m tabnanny -q .
    ./PyMOTW/Queue/fetch_podcasts.py

..
    To see more information about the files being scanned, use the `-v` option.

検査対象ファイルのもっと詳細な情報を見るには `-v` オプションを使用してください。

::

    $ python -m tabnanny -v ./PyMOTW/Queue
    './PyMOTW/Queue': listing directory
    './PyMOTW/Queue/__init__.py': Clean bill of health.
    './PyMOTW/Queue/feedparser.py': Clean bill of health.
    './PyMOTW/Queue/fetch_podcasts.py': *** Line 78: trouble in tab city! ***
    offending line: "\t\tfor enclosure in entry.get('enclosures', []):\n"
    indent not greater e.g. at tab sizes 1, 2

..
    Using within Your Program
    =========================

プログラム内から使用する
========================

..
    As soon as I discovered the mistake in my Queue example, I decided I
    needed to add an automatic check to my PyMOTW build process.  I
    created a ``tabcheck`` task in my ``pavement.py`` build script so I
    could run `paver tabcheck` and scan the code I'm working on for
    PyMOTW.  This is possible because tabnanny exposes its `check()`
    function as a public API.

Queue のサンプルプログラムの間違いを見つけてすぐに私は PyMOTW のビルド処理に自動チェックを追加することに決めました。私は `paver tabcheck` を実行して PyMOTW のコードを検査できるのように PyMOTW の ``pavement.py`` ビルドスクリプトに ``tabcheck`` タスクを作成しました。これは tabnanny はパブリック API として `check()` 関数を提供するので実現できます。

..
    Here's an example of using tabnanny that doesn't require understanding
    Paver's task definition decorators.

ここに Paver のタスク定義を理解していなくても使える tabnanny のサンプルがあります。

.. include:: tabnanny_check.py
   :literal:
   :start-after: #end_pymotw_header

実行結果です。

::

	$ python tabnanny_check.py ../Queue
	'../Queue': listing directory
	'../Queue/__init__.py': Clean bill of health.
	'../Queue/feedparser.py': Clean bill of health.
	'../Queue/fetch_podcasts.py': *** Line 78: trouble in tab city! ***
	offending line: "\t\tfor enclosure in entry.get('enclosures', []):\n"
	indent not greater e.g. at tab sizes 1, 2

.. note:: 

  .. If you run these examples against the PyMOTW code it won't report
     the same errors, since I have fixed my code in this release.

  PyMOTW コードに対してこれらのサンプルプログラムを実行しても、今回のリリースで私がコードを修正したので同じエラーは検出されません。

.. seealso::

    `tabnanny <http://docs.python.org/library/tabnanny.html>`_
        .. The standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント

    :mod:`tokenize`
        .. Lexical scanner for Python source code.

        Python ソースコードの字句解析器
