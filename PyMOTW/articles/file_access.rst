.. _article-file-access:

################
ファイルアクセス
################

..
    ###########
    File Access
    ###########

..
    Python's standard library includes a large range of tools for working with files, filenames, and file contents.

Python の標準ライブラリは、ファイル、ファイル名、ファイル内容を扱う様々なツールを提供します。

..
    Filenames
    =========

ファイル名
==========

..
    The first step in working with files is to get the name of the file so you can operate on it.  Python represents filenames as simple strings, but provides tools for building them from standard, platform-independent, components in :mod:`os.path`.  List the contents of a directory with ``listdir()`` from :mod:`os`, or use :mod:`glob` to build a list of filenames from a pattern.  Finer grained filtering of filenames is possible with :mod:`fnmatch`.  

ファイルを扱う最初のステップは対象ファイルのファイル名を取得することです。Python はファイル名をシンプルな文字列で表現しますが、標準、プラットフォーム独自、 :mod:`os.path` のコンテンツからファイル名を取得するツールを提供します。 :mod:`os` の :func:`listdir` でディレクトリの内容を表示するか、ファイル名のリストをパターンから取得する :mod:`glob`  を使用してください。 :mod:`fnmatch` を使用すると細かな粒度でファイル名のフィルタリングができます。

..
    Meta-data
    =========

メタデータ
==========

..
    Once you know the name of the file, you may want to check other characteristics such as permissions or the file size using ``os.stat()`` and the constants in :mod:`stat`.

ファイル名が分かったら :func:`os.stat` と :mod:`stat` の定数を使用してファイルサイズやパーミッションといったその他の特性をチェックしても良いです。

..
    Reading Files
    =============

ファイルを読み込む
==================

..
    If you're writing a filter application that processes text input line-by-line, :mod:`fileinput` provides an easy framework to get started.  The fileinput API calls for you to iterate over the ``input()`` generator, processing each line as it is yielded.  The generator handles parsing command line arguments for file names, or falling back to reading directly from ``sys.stdin``.  The result is a flexible tool your users can run directly on a file or as part of a pipeline.

行単位でテキスト入力を処理するフィルタアプリケーションを開発しているなら :mod:`fileinput` が簡単なフレームワークを提供します。 :mod:`fileinput` の API は、行単位で処理する :func:`input` が返すオブジェクトをイテレートします。そのオブジェクトはファイル名のためにコマンドライン引数を解析して扱うか、もしくは :func:`sys.stdin` から直接読み込みます。その出力はファイルやパイプラインの一部として直接実行可能な柔軟性のあるツールです。

..
    If your app needs random access to files, :mod:`linecache` makes it easy to read lines by their line number.  The contents of the file are maintained in a cache, so be careful of memory consumption.

アプリケーションがファイルへランダムアクセスするなら :mod:`linecache` を使用すると行番号を指定して簡単にその行を読み込めます。ファイルのコンテンツはキャッシュに保持されるのでメモリの消費量に注意してください。

..
    Temporary Files
    ===============

一時ファイル
============

..
    For cases where you need to create scratch files to hold data temporarily, or before moving it to a permanent location, :mod:`tempfile` will be very useful.  It provides classes to create temporary files and directories safely and securely.  Names are guaranteed not to collide, and include random components so they are not easily guessable.

適切な保存場所へ移動する前や一時的にデータを保持するために空っぽのファイルを作成する必要がある場合は :mod:`tempfile` がとても便利です。それは一時ファイルやディレクトリを確実且つセキュアに作成するクラスを提供します。ファイル名は衝突しないことが保証されていて、簡単に推測できないようにランダムな文字列になります。

..
    Files and Directories
    =====================

ファイルとディレクトリ
======================

..
    Frequently you need to work on a file as a whole, without worrying about what is in it.  The :mod:`shutil` module includes high-level file operations such as copying files and directories, setting permissions, etc.

ファイルの中身ではなく、ファイルそのものを扱いたいこともよくあります。 :mod:`shutil` モジュールは、ファイルやディレクトリのコピー、パーミッションの設定といった高レベルのファイル操作を提供します。
