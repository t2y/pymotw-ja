.. _article-text-processing:

##################
テキスト処理ツール
##################

..
    #####################
    Text Processing Tools
    #####################

..
    The string class is the most obvious text processing tool available to Python programmers, but there are plenty of other tools in the standard library to make text manipulation simpler.  

文字列クラスは、Python プログラマに最も分かり易いテキスト処理ツールですが、テキストをシンプルに処理するツールが標準ライブラリにはたくさんあります。

..
    string module
    =============

string モジュール
=================

..
    Old-style code will use functions from the :mod:`string` module, instead of methods of string objects.  There is an equivalent method for each function from the module, and use of the functions is deprecated for new code.  

旧スタイルのコードは、文字列オブジェクトのメソッドではなく、 :mod:`string` モジュールの関数で使用できます。 :mod:`string` モジュールに等価な関数はありますが、今はそういった関数は非推奨です。

..
    Newer code may use a ``string.Template`` as a simple way to parameterize strings beyond the features of the string or unicode classes.  While not as feature-rich as templates defined by many of the web frameworks or extension modules available on PyPI, ``string.Template`` is a good middle ground for user-modifiable templates where dynamic values need to be inserted into otherwise static text.

今は string や unicode クラスの機能以上に文字列をパラメータ化するシンプルな方法として ``string.Template`` を使用すると良いです。多くの web フレームワークで定義されるテンプレートや PyPI で利用可能な拡張モジュールと比較すると機能が十分ではないものの、 ``string.Template`` は動的な値を静的なテキストに挿入するユーザ定義テンプレートとして優れた中間層です。

..
    Text Input
    ==========

テキスト入力
============

..
    Reading from a file is easy enough, but if you're writing a line-by-line filter the :mod:`fileinput` module is even easier.  The fileinput API calls for you to iterate over the ``input()`` generator, processing each line as it is yielded.  The generator handles parsing command line arguments for file names, or falling back to reading directly from ``sys.stdin``.  The result is a flexible tool your users can run directly on a file or as part of a pipeline.

ファイルからの読み込みはとても簡単ですが、行単位のフィルタを書いているなら :mod:`fileinput` モジュールを使用するとさらに簡単です。 :mod:`fileinput` の API は、行単位で処理する :func:`input` が返すオブジェクトをイテレートします。そのオブジェクトはファイル名のためにコマンドライン引数を解析して扱うか、もしくは :func:`sys.stdin` から直接読み込みます。その出力はファイルやパイプラインの一部として直接実行可能な柔軟性のあるツールです。

..
    Text Output
    ===========

テキスト出力
============

..
    The :mod:`textwrap` module includes tools for formatting text from paragraphs by limiting the width of output, adding indentation, and inserting line breaks to wrap lines consistently.

:mod:`textwrap` モジュールは、インデントを追加したり、他の行と同じ位置で改行を挿入するといった出力幅を制限することでパラグラフの整形を行うツールを提供します。

..
    Comparing Values
    ================

テキストを比較する
==================

..
    The standard library includes two modules related to comparing text values beyond the built-in equality and sort comparison supported by string objects.  :mod:`re` provides a complete regular expression library, implemented largely in C for performance.  Regular expressions are well-suited for finding substrings within a larger data set, comparing strings against a pattern (rather than another fixed string), and mild parsing.  

標準ライブラリには、string オブジェクトでサポートされる組み込みの等号やソートによる比較より高機能なテキストの比較に関連するモジュールが2つあります。 :mod:`re` モジュールは、パフォーマンスのためにほとんど C 言語で実装された完全な正規表現ライブラリを提供します。正規表現は、大きなデータセットから部分文字列を見つけたり、(特定文字列というよりも)パターンに対して文字列を比較したり、ちょっとした構文解析に適しています。

..
    :mod:`difflib`, on the other hand, shows you the actual differences between sequences of text in terms of the parts added, removed, or changed.  The output of the comparison functions in :mod:`difflib` can be used to provide more detailed feedback to user about where changes occur in two inputs, how a document has changed over time, etc.

一方、 :mod:`difflib` モジュールは、テキストの部分文字列において追加、削除、変更された差異を表示します。 :mod:`difflib` モジュールの比較関数の出力は、時間とともにどのようにドキュメントが変更されたか等、2つの入力テキストで生じた変更に関して詳細なフィードバックをユーザへ提供します。
