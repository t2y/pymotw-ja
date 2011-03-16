.. _article-data-persistence:

####################
データの永続化と変換
####################
..
    #############################
    Data Persistence and Exchange
    #############################

..
    Python provides several modules for storing data.  There are basically two aspects to persistence: converting the in-memory object back and forth into a format for saving it, and working with the storage of the converted data.

Python はデータを保存するための複数のモジュールを提供します。基本的に永続化は2つの様相があります。1つはインメモリオブジェクトを変換して保存用フォーマットにする、もう1つは変換されたデータのストレージと連携することです。

..
    ===================
    Serializing Objects
    ===================

==============================
オブジェクトをシリアライズする
==============================

..
    Python includes two modules capable of converting objects into a transmittable or storable format (*serializing*): :mod:`pickle` and :mod:`json`.  It is most common to use :mod:`pickle`, since there is a fast C implementation and it is integrated with some of the other standard library modules that actually store the serialized data, such as :mod:`shelve`.  Web-based applications may want to examine :mod:`json`, however, since it integrates better with some of the existing web service storage applications.

Python は、通信可能または保存可能なフォーマットにオブジェクトを変換 (*シリアライズ*) できる2つのモジュール :mod:`pickle` と :mod:`json` を提供します。最も一般的なのは :mod:`pickle` です。というのは、高速な C 言語実装があり、 :mod:`shelve` のように他の標準ライブラリで実際にデータをシリアライズして保存するのに利用されているからです。web ベースのアプリケーションは、既存の web サービスのストレージアプリケーションと連携するのに適した :mod:`json` を調べると良いです。

..
    ==========================
    Storing Serialized Objects
    ==========================

========================================
シリアライズされたオブジェクトを保存する
========================================

..
    Once the in-memory object is converted to a storable format, the next step is to decide how to store the data.  A simple flat-file with serialized objects written one after the other works for data that does not need to be indexed in any way.  But Python includes a collection of modules for storing key-value pairs in a simple database using one of the DBM format variants.

インメモリオブジェクトを保存可能なフォーマットに変換したら、次はそのデータを保存する方法を決めます。後続の処理においてインデクシングする必要がないデータなら、シリアライズされたオブジェクトを単純にファイルへ書き込みます。しかし、Python は DBM フォーマットの一種としてキーバリューを保存するシンプルなデータベースのために複数のモジュールを提供します。

..
    The simplest interface to take advantage of the DBM format is provided by :mod:`shelve`.  Simply open the shelve file, and access it through a dictionary-like API.  Objects saved to the shelve are automatically pickled and saved without any extra work on your part.  

:mod:`shelve` は DBM フォーマットを活用する最もシンプルなインタフェースです。shelve ファイルを単純にオープンして、ディクショナリのような API でアクセスします。shelve ファイルに保存するオブジェクトは自動的に pickle 化されて、特に意識する必要はありません。

..
    One drawback of shelve is that with the default interface you can't guarantee which DBM format will be used.  That won't matter if your application doesn't need to share the database files between hosts with different libraries, but if that is needed you can use one of the classes in the module to ensure a specific format is selected (:ref:`shelve-shelf-types`).

shelve の欠点の1つは、デフォルトのインタフェースでどの DBM フォーマットを使用するかを指定できないことです。そのことは、アプリケーションが異なるライブラリ間や複数ホスト間でデータベースファイルを共有する必要がない場合は大した問題ではあありません。しかし、そうした必要性がある場合、モジュールのクラスの1つを選択して特定のフォーマットを指定できます(:ref:`shelve-shelf-types`)。

..
    If you're going to be passing a lot of data around via JSON anyway, using :mod:`json` and :mod:`anydbm` can provide another persistence mechanism.  Since the DBM database keys and values must be strings, however, the objects won't be automatically re-created when you access the value in the database.

もし JSON 経由で大量データを渡す必要があるなら :mod:`json` と :mod:`anydbm` を使用して別の永続化の仕組みを提供します。DBM データベースのキーと値は文字列でなければならないので、データベースの値にアクセスするときにそのオブジェクトが自動的に再作成されることはありません。

..
    ====================
    Relational Databases
    ====================

================
関係データベース
================

..
    The excellent :mod:`sqlite3` in-process relational database is available with most Python distributions.  It stores its database in memory or in a local file, and all access is from within the same process, so there is no network lag.  The compact nature of :mod:`sqlite3` makes it especially well suited for embedding in desktop applications or development versions of web apps.

:mod:`sqlite3` という優れたインプロセス関係データベースがほとんどの Python 環境で利用できます。それはメモリまたはローカルファイルにデータベースを保存します。そして、全てのアクセスが同一プロセス内から行われるのでネットワークの遅延がありません。小型軽量な特徴をもつ :mod:`sqlite3` は特にデスクトップアプリケーションの組み込み用途や web アプリケーションの開発バージョンに適しています。

..
    All access to the database is through the Python DBI 2.0 API, by default, as no object relational mapper (ORM) is included.  The most popular general purpose ORM is `SQLAlchemy <http://www.sqlalchemy.org/>`_, but others such as Django's native ORM layer also support SQLite.  SQLAlchemy is easy to install and set up, but if your objects aren't very complicated and you are worried about overhead, you may want to use the DBI interface directly.

データベースへの全てのアクセスは Python DBI 2.0 API を経由して行われます。デフォルトでは、オブジェクト関係マッパ(ORM)は提供されません。

最も汎用的で人気のある ORM は `SQLAlchemy <http://www.sqlalchemy.org/>`_ です。しかし、Django のネイティブ ORM もまた SQLite をサポートします。SQLAlchemy のインストールと設定は簡単ですが、対象アプリケーションのオブジェクトがあまり複雑ではない、もしくはそのオーバーヘッドが気になるなら、直接 DBI インタフェースを使用した方が良いかもしれません。

..
    ======================================
    Data Exchange Through Standard Formats
    ======================================

================================
標準フォーマット経由のデータ変換
================================

..
    Although not usually considered a true persistence format :mod:`csv`, or comma-separated-value, files can be an effective way to migrate data between applications.  Most spreadsheet programs and databases support both export and import using CSV, so dumping data to a CSV file is frequently the simplest way to move data out of your application and into an analysis tool.

:mod:`csv` やカンマで分割される値は、本来、永続化目的には考えられていませんが、アプリケーション間でデータを移行するときにそういったファイルの方が効率的です。ほとんどのスプレッドシートプログラムやデータベースは CSV によるインポート/エクスポート機能をサポートします。そのため、CSV ファイルに出力するのは、アプリケーションや解析ツールにデータを移行する最も簡単な方法です。
