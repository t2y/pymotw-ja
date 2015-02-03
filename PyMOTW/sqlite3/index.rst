..
    ========================================
     sqlite3 -- Embedded Relational Database
    =========================================

====================================
 sqlite3 -- 組み込み関係データベース
====================================

..
    :synopsis: Embedded relational database

.. module:: sqlite3
    :synopsis: 組み込み関係データベース

..
    :Purpose: Implements an embedded relational database with SQL support.
    :Available In: 2.5 and later

:目的: SQL をサポートした組み込み関係データベースを実装する
:利用できるバージョン: 2.5 以上

..
    The :mod:`sqlite3` module provides a DB-API 2.0 compliant interface to
    the SQLite_ relational database.  SQLite is an in-process database,
    designed to be embedded in applications, instead of using a separate
    database server program such as MySQL, PostgreSQL, or Oracle.  SQLite
    is fast, rigorously tested, and flexible, making it suitable for
    prototyping and production deployment for some applications.

:mod:`sqlite3` モジュールは SQLite_ 関係データベースに対する DB-API 2.0 準拠のインタフェースを提供します。SQLite はアプリケーション内に組み込むように設計された、インプロセスデータベースであり、MySQL, PostgreSQL や Oracle のような独立したサーバプログラムではありません。SQLite は高速且つ柔軟で徹底的にテストされており、プロトタイピングのみならず、アプリケーションによっては本番環境にも使用できます。

..
    Creating a Database
    ===================

データベースを作成する
======================

..
    An SQLite database is stored as a single file on the filesystem.  The
    library manages access to the file, including locking it to prevent
    corruption when multiple writers use it.  The database is created the
    first time the file is accessed, but the application is responsible
    for managing the table definitions, or *schema*, within the database.

SQLite データベースはファイルシステム上の1つのファイルに格納されます。ライブラリはそのファイルへのアクセスを管理し、複数のプログラムがそのファイルへ書き込むときにデータが破損しないようにロックします。そのファイルへの初回アクセス時にデータベースが作成されますが、アプリケーションはデータベース内のテーブル定義もしくは *スキーマ* を管理する責任があります。

..
    This example looks for the database file before opening it with
    :func:`connect` so it knows when to create the schema for new
    databases.

このサンプルは :func:`connect` でデータベースファイルをオープンする前にデータベースファイルの存在を調べるので、新しいデータベースのスキーマを作成するかどうかが分かります。

.. include:: sqlite3_createdb.py
   :literal:
   :start-after: #end_pymotw_header

..
    Running the script twice shows that it creates the empty file if it
    does not exist.

このスクリプトを２回実行すると、そのデータベースファイルが存在しなければ空のファイルを作成することが分かります。

.. {{{cog
.. (cog.inFile.dirname() / 'todo.db').unlink()
.. cog.out(run_script(cog.inFile, 'ls *.db', interpreter='', ignore_error=True))
.. cog.out(run_script(cog.inFile, 'sqlite3_createdb.py', include_prefix=False))
.. cog.out(run_script(cog.inFile, 'ls *.db', interpreter='', include_prefix=False))
.. cog.out(run_script(cog.inFile, 'sqlite3_createdb.py', include_prefix=False))
.. }}}

::

	$ ls *.db
	
	ls: *.db: No such file or directory

	$ python sqlite3_createdb.py
	
	Need to create schema

	$ ls *.db
	
	todo.db

	$ python sqlite3_createdb.py
	
	Database exists, assume schema does, too.

.. {{{end}}}

..
    After creating the new database file, the next step is to create the
    schema to define the tables within the database.  The remaining
    examples in this section all use the same database schema with tables
    for managing tasks.  The tables are:

新しいデータベースファイルを作成した後、その次のステップはデータベース内のテーブルを定義するスキーマを作成します。このセクションのこの後の全サンプルは、タスク管理テーブルを持つ同じデータベーススキーマを使用します。テーブルは次の通りです。

..
    **project**
      ===========  ====  ===========
      Column       Type  Description
      ===========  ====  ===========
      name         text  Project name
      description  text  Long project description
      deadline     date  Due date for the entire project
      ===========  ====  ===========

**project**

  ===========  ====  ===========
  列           型    説明
  ===========  ====  ===========
  name         text  プロジェクト名
  description  text  プロジェクトの説明
  deadline     date  プロジェクト全体の期限
  ===========  ====  ===========

..
    **task**
      ===============  =======  ===========
      Column           Type     Description
      ===============  =======  ===========
      id               number   Unique task identifier
      priority         integer  Numerical priority, lower is more important
      details          text     Full task details
      status           text     Task status (one of 'new', 'pending', 'done', or 'canceled').
      deadline         date     Due date for this task
      completed_on     date     When the task was completed.
      project          text     The name of the project for this task.
      ===============  =======  ===========

**task**

  ===============  =======  ===========
  列               型       説明
  ===============  =======  ===========
  id               number   ユニークなタスク識別子
  priority         integer  優先度の数値、低いほど優先度が高い
  details          text     タスクの詳細
  status           text     タスクの状況 ('new', 'pending', 'done' 又は 'canceled' のどれか)
  deadline         date     タスクの期限
  completed_on     date     タスクの完了を表す
  project          text     タスクのプロジェクト名
  ===============  =======  ===========

..
    The *data definition language* (DDL) statements to create the tables
    are:

テーブルを作成する *データ定義言語* (DDL) 文は次の通りです。

.. literalinclude:: todo_schema.sql
   :language: sql

..
    The :func:`executescript` method of the :class:`Connection` can be
    used to run the DDL instructions to create the schema.

:class:`Connection` クラスの :func:`executescript` メソッドはそのスキーマを作成する DDL 命令を実行するために使用されます。

.. include:: sqlite3_create_schema.py
   :literal:
   :start-after: #end_pymotw_header

..
    After the tables are created, a few :command:`insert` statements
    create a sample project and related tasks.  The :command:`sqlite3`
    command line program can be used to examine the contents of the
    database.

そのテーブルを作成した後、数個の :command:`insert` 文がサンプルプロジェクトと関連タスクを作成します。 :command:`sqlite3` コマンドラインプログラムをデータベースのコンテンツを調べるために使用します。

.. {{{cog
.. (cog.inFile.dirname() / 'todo.db').unlink()
.. cog.out(run_script(cog.inFile, 'sqlite3_create_schema.py'))
.. cog.out(run_script(cog.inFile, "sqlite3 todo.db 'select * from task'", 
..         interpreter=None, include_prefix=False))
.. }}}

::

	$ python sqlite3_create_schema.py
	
	Creating schema
	Inserting initial data

	$ sqlite3 todo.db 'select * from task'
	
	1|1|write about select|done|2010-10-03||pymotw
	2|1|write about random|waiting|2010-10-10||pymotw
	3|1|write about sqlite3|active|2010-10-17||pymotw

.. {{{end}}}

..
    Retrieving Data
    ===============

データを取り出す
================

..
    To retrieve the values saved in the :data:`task` table from within a
    Python program, create a :class:`Cursor` from a database connection
    using the :func:`cursor` method.  A cursor produces a consistent view
    of the data, and is the primary means of interacting with a
    transactional database system like SQLite.

Python プログラムから :data:`task` テーブルに保存された値を取り出すには :func:`cursor` メソッドでデータベースコネクションから :class:`Cursor` を作成します。カーソルはデータの一貫したビューを生成して、SQLite のようなトランザクションデータベースシステムで対話的にやり取りする基本的な方法です。

.. include:: sqlite3_select_tasks.py
   :literal:
   :start-after: #end_pymotw_header

..
    Querying is a two step process.  First, run the query with the
    cursor's :func:`execute` method to tell the database engine what data
    to collect.  Then, use :func:`fetchall` to retrieve the results.  The
    return value is a sequence of tuples containing the values for the
    columns included in the :command:`select` clause of the query.

クエリの実行は2つのステップで行われます。最初にカーソルの :func:`execute` メソッドを実行して、どんなデータを取得するかをデータベースエンジンに伝えます。それから、その結果を取り出すために :func:`fetchall` を使用します。返り値はクエリの :command:`select` 句に記述された列の値を含むタプルのシーケンスです。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sqlite3_select_tasks.py'))
.. }}}

::

	$ python sqlite3_select_tasks.py
	
	 1 {1} write about select   [done    ] (2010-10-03)
	 2 {1} write about random   [waiting ] (2010-10-10)
	 3 {1} write about sqlite3  [active  ] (2010-10-17)

.. {{{end}}}

..
    The results can be retrieved one at a time with :func:`fetchone`, or
    in fixed-size batches with :func:`fetchmany`.

その結果は :func:`fetchone` で一度に1つだけ取り出したり、 :func:`fetchmany` で固定サイズ分まとめて取り出すこともできます。

.. include:: sqlite3_select_variations.py
   :literal:
   :start-after: #end_pymotw_header

..
    The value passed to :func:`fetchmany` is the maximum number of items
    to return.  If fewer items are available, the sequence returned will
    be smaller than the maximum value.

:func:`fetchmany` へ渡された値は返す要素の最大数です。もし指定した最大数よりも要素が少ないなら、その最大数よりも小さいシーケンスが返されます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sqlite3_select_variations.py'))
.. }}}

::

	$ python sqlite3_select_variations.py
	
	Project details for Python Module of the Week (pymotw) due 2010-11-01
	
	Next 5 tasks:
	 1 {1} write about select        [done    ] (2010-10-03)
	 2 {1} write about random        [waiting ] (2010-10-10)
	 3 {1} write about sqlite3       [active  ] (2010-10-17)

.. {{{end}}}

..
    Query Metadata
    --------------

クエリメタデータ
----------------

..
    The DB-API 2.0 specification says that after :func:`execute` has been
    called, the :class:`Cursor` should set its :attr:`description`
    attribute to hold information about the data that will be returned by
    the fetch methods.  The API specification say that the description
    value is a sequence of tuples containing the column name, type,
    display size, internal size, precision, scale, and a flag that says
    whether null values are accepted.

DB-API 2.0 の仕様では :func:`execute` が呼び出された後、 :class:`Cursor` はその :attr:`description` 属性をセットして、fetch メソッドが返すデータに関する情報を保持します。API の仕様では、その description の値は列名、型、表示サイズ、内部サイズ、精度、スケールや NULL 値を許容するかどうかのフラグを含むタプルのシーケンスになります。

.. include:: sqlite3_cursor_description.py
   :literal:
   :start-after: #end_pymotw_header

..
    Because :mod:`sqlite3` does not enforce type or size constraints on
    data inserted into a database, only the column name value is filled
    in.

:mod:`sqlite3` はデータベースへ追加するデータの型やサイズの制約を強制しないので、列名のみがセットされます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sqlite3_cursor_description.py'))
.. }}}

::

	$ python sqlite3_cursor_description.py
	
	Task table has these columns:
	('id', None, None, None, None, None, None)
	('priority', None, None, None, None, None, None)
	('details', None, None, None, None, None, None)
	('status', None, None, None, None, None, None)
	('deadline', None, None, None, None, None, None)
	('completed_on', None, None, None, None, None, None)
	('project', None, None, None, None, None, None)

.. {{{end}}}

..
    Row Objects
    -----------

行オブジェクト
--------------

..
    By default, the values returned by the fetch methods as "rows" from
    the database are tuples.  The caller is responsible for knowing the
    order of the columns in the query and extracting individual values
    from the tuple.  When the number of values in a query grows, or the
    code working with the data is spread out in a library, it is usually
    easier to work with an object and access the column values using their
    column names, since that way the number and order of the tuple
    elements can change over time as the query is edited, and code
    depending on the query results is less likely to break.

デフォルトでは、データベースから "行" として fetch メソッドが返す値はタプルです。呼び出し側はクエリ内の列の順番を覚えておいて、タプルから対応する個々の値を展開する責任があります。あるクエリの値の数が増加する、もしくはそのデータと連携するコードがライブラリに展開されるとき、1つのオブジェクトに列名でその列の値にアクセスすると簡単です。その理由は、そのタプルの要素の順番と数はクエリが修正されると変更され、クエリの結果に依存するコードが壊れにくくなるからです。

..
    :class:`Connection` objects have a :data:`row_factory` property that
    allows the calling code to control the type of object created to
    represent each row in the query result set.  :mod:`sqlite3` also
    includes a :class:`Row` class intended to be used as a row factory.
    :class:`Row` instances can be accessed by column index and name.

:class:`Connection` オブジェクトは :data:`row_factory` プロパティを持ち、クエリの結果セットの各行を表すのに作成されたオブジェクトの型を制御します。さらに :mod:`sqlite3` は1行のファクトリとして使用することを目的とした :class:`Row` クラスもあります。 :class:`Row` インスタンスは列のインデックスや名前でアクセスできます。

.. include:: sqlite3_row_factory.py
   :literal:
   :start-after: #end_pymotw_header

..
    This version of the ``sqlite3_select_variations.py`` example has been
    re-written using :class:`Row` instances instead of tuples.  The
    project row is still printed by accessing the column values through
    position, but the :command:`print` statement for tasks uses keyword
    lookup instead, so it does not matter that the order of the columns in
    the query has been changed.

この ``sqlite3_select_variations.py`` のサンプルは、タプルの代わりに :class:`Row` インスタンスを使用して書き直しています。project テーブルの行はクエリの列名の位置でその値へアクセスして表示しますが、task テーブルの行を表示する :command:`print` 文はその代わりにキーワードを使用します。そのため、クエリの列の順番が変更されても問題にはなりません。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sqlite3_row_factory.py'))
.. }}}

::

	$ python sqlite3_row_factory.py
	
	Project details for Python Module of the Week (pymotw) due 2010-11-01
	
	Next 5 tasks:
	 1 {1} write about select        [done    ] (2010-10-03)
	 2 {1} write about random        [waiting ] (2010-10-10)
	 3 {1} write about sqlite3       [active  ] (2010-10-17)

.. {{{end}}}

..
    Using Variables with Queries
    ============================

クエリで変数を使用する
======================

..
    Using queries defined as literal strings embedded in a program is
    inflexible.  For example, when another project is added to the
    database the query to show the top five tasks should be updated to
    work with either project.  One way to add more flexibility is to build
    an SQL statement with the desired query by combining values in Python.
    However, building a query string in this way is dangerous, and should
    be avoided.  Failing to correctly escape special characters in the
    variable parts of the query can result in SQL parsing errors, or
    worse, a class of security vulnerabilities known as *SQL-injection
    attacks*.

プログラム内に組み込まれた文字列リテラルで定義されたクエリを使用することは柔軟性に欠けます。例えば、別のプロジェクトをデータベースに追加するとき、トップ5のタスクを表示するクエリを実行するにはどちらか一方のプロジェクトを更新すべきです。より柔軟性を確保するための1つの方法は、Python の変数を組み合わせて設計したクエリで SQL 文を構築することです。しかし、この方法を使用して文字列でクエリを構築することは危険なので止めた方が良いです。クエリで扱う変数の特殊文字のエスケープ処理を正しく行わないと、SQL の構文解析エラーか、もっと悪い *SQL インジェクション攻撃* として知られるセキュリティ上の脆弱性を引き起こします。

..
    The proper way to use dynamic values with queries is through *host
    variables* passed to :func:`execute` along with the SQL instruction.
    A placeholder value in the SQL is replaced with the value of the host
    variable when the statement is executed.  Using host variables instead
    of inserting arbitrary values into the SQL before it is parsed avoids
    injection attacks because there is no chance that the untrusted values
    will affect how the SQL is parsed.  SQLite supports two forms for
    queries with placeholders, positional and named.

クエリで動的な値を使用する適切な方法は、SQL 命令に従い :func:`execute` へ渡す *ホスト変数* を経由することです。SQL のプレースホルダ値はその SQL 文の実行時にホスト変数の値で置き換えられます。SQL 内に任意の値を追加する代わりに、SQL が構文解析される前でホスト変数を使用することはインジェクション攻撃を避けます。その理由は信頼できない値が SQL 文の構文解析で影響を与える可能性がないからです。SQLite はプレースホルダを用いる2つのクエリ形態、位置と名前をサポートします。

..
    Positional Parameters
    ---------------------

位置パラメータ
--------------

..
    A question mark (``?``) denotes a positional argument, passed to
    :func:`execute` as a member of a tuple.

クエスチョンマーク (``?``) は位置引数を表します。それはタプルの要素として :func:`execute` に渡されます。

.. include:: sqlite3_argument_positional.py
   :literal:
   :start-after: #end_pymotw_header

..
    The command line argument is passed safely to the query as a
    positional argument, and there is no chance for bad data to corrupt
    the database.

コマンドライン引数は位置引数として安全にクエリへ渡されて、データベースを汚染するデータにはなりません。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sqlite3_argument_positional.py pymotw'))
.. }}}

::

	$ python sqlite3_argument_positional.py pymotw
	
	 1 {1} write about select   [done    ] (2010-10-03)
	 2 {1} write about random   [waiting ] (2010-10-10)
	 3 {1} write about sqlite3  [active  ] (2010-10-17)

.. {{{end}}}

..
    Named Parameters
    ----------------

名前付きパラメータ
------------------

..
    Use named parameters for more complex queries with a lot of parameters
    or where some parameters are repeated multiple times within the query.
    Named parameters are prefixed with a colon, like ``:param_name``.

多くのパラメータを持つ、または複数のパラメータがクエリ内で何回か繰り返される複雑なクエリには名前付きパラメータを使用してください。名前付きパラメータは ``:param_name`` のようにコロンを接頭辞に取ります。

.. include:: sqlite3_argument_named.py
   :literal:
   :start-after: #end_pymotw_header

..
    Neither positional nor named parameters need to be quoted or escaped,
    since they are given special treatment by the query parser.

位置パラメータも名前付きパラメータも、クエリパーサにより特別な処理が行われるのでクォートやエスケープ処理が必要ありません。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sqlite3_argument_named.py pymotw'))
.. }}}

::

	$ python sqlite3_argument_named.py pymotw
	
	 1 {1} write about select        [done    ] (2010-10-03)
	 2 {1} write about random        [waiting ] (2010-10-10)
	 3 {1} write about sqlite3       [active  ] (2010-10-17)

.. {{{end}}}

..
    Query parameters can be used with :command:`select`,
    :command:`insert`, and :command:`update` statements.  They can appear
    in any part of the query where a literal value is legal.

クエリパラメータは :command:`select`, :command:`insert` や :command:`update` 文で使用できます。クエリパラメータはリテラル値が正しく処理されるクエリ内のどこでも使用できます。

.. include:: sqlite3_argument_update.py
   :literal:
   :start-after: #end_pymotw_header

..
    This :command:`update` statement uses two named parameters.  The
    :data:`id` value is used to find the right row to modify, and the
    :data:`status` value is written to the table.

この :command:`update` 文は2つの名前付きパラメータを使用します。 :data:`id` 値は変更する行を見つけるために使用され :data:`status` 値がテーブルに書き込まれます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sqlite3_argument_update.py 2 done', trailing_newlines=False))
.. cog.out(run_script(cog.inFile, 'sqlite3_argument_named.py pymotw', include_prefix=False))
.. }}}

::

	$ python sqlite3_argument_update.py 2 done
	$ python sqlite3_argument_named.py pymotw
	
	 1 {1} write about select        [done    ] (2010-10-03)
	 2 {1} write about random        [done    ] (2010-10-10)
	 3 {1} write about sqlite3       [active  ] (2010-10-17)

.. {{{end}}}

..
    Bulk Loading
    ------------

バルクロード
------------

..
    To apply the same SQL instruction to a lot of data use
    :func:`executemany`.  This is useful for loading data, since it avoids
    looping over the inputs in Python and lets the underlying library
    apply loop optimizations.  This example program reads a list of tasks
    from a comma-separated value file using the :mod:`csv` module and
    loads them into the database.

大量データに対して同じ SQL 命令を適用するには :func:`executemany` を使用します。Python で入力のループを行わず低レイヤのライブラリでループを最適化するので、これはデータを読み込むのに便利です。このサンプルプログラムは :mod:`csv` モジュールを用いて、カンマで区切られた値を持つファイルからタスクのリストを読み込みます。そして、データベースへその読み込んだ値をロードします。

.. include:: sqlite3_load_csv.py
   :literal:
   :start-after: #end_pymotw_header

..
    The sample data file ``tasks.csv`` contains:

サンプルのデータファイル ``tasks.csv`` は次のデータを含みます。

.. literalinclude:: tasks.csv

..
    Running the program produces:

プログラムを実行すると次のようになります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sqlite3_load_csv.py tasks.csv', trailing_newlines=False))
.. cog.out(run_script(cog.inFile, 'sqlite3_argument_named.py pymotw', include_prefix=False))
.. }}}

::

	$ python sqlite3_load_csv.py tasks.csv
	$ python sqlite3_argument_named.py pymotw
	
	 4 {2} finish reviewing markup   [active  ] (2010-10-02)
	 6 {1} subtitle                  [active  ] (2010-10-03)
	 1 {1} write about select        [done    ] (2010-10-03)
	 5 {2} revise chapter intros     [active  ] (2010-10-03)
	 2 {1} write about random        [done    ] (2010-10-10)
	 3 {1} write about sqlite3       [active  ] (2010-10-17)

.. {{{end}}}

..
    Column Types
    ============

列の型
======

..
    SQLite has native support for integer, floating point, and text
    columns.  Data of these types is converted automatically by
    :mod:`sqlite3` from Python's representation to a value that can be
    stored in the database, and back again, as needed.  Integer values are
    loaded from the database into :class:`int` or :class:`long` variables,
    depending on the size of the value.  Text is saved and retrieved as
    :class:`unicode`, unless the :class:`Connection` :attr:`text_factory`
    has been changed.

SQLite は整数、浮動小数点やテキストの列をネイティブにサポートします。これらの型のデータは Python における表現からデータベースへ格納できる値へ :mod:`sqlite3` により 自動的に変換されます。また必要に応じて元に戻せます。整数値はその値のサイズによりデータベースから :class:`int` か :class:`long` 変数へ読み込まれます。
テキストは :class:`Connection` の :attr:`text_factory` 属性に変更していない限り :class:`unicode` として取り出されて保存されます。

..
    Although SQLite only supports a few data types internally,
    :mod:`sqlite3` includes facilities for defining custom types to allow
    a Python application to store any type of data in a column.
    Conversion for types beyond those supported by default is enabled in
    the database connection using the :data:`detect_types` flag.  Use
    :const:`PARSE_DECLTYPES` is the column was declared using the desired
    type when the table was defined.

SQLite は内部的には少しのデータ型のみをサポートしますが、 :mod:`sqlite3` には、どんなデータでも列に格納するために Python アプリケーションがカスタム型を定義できます。デフォルトでサポートされていない型の変換は、 :data:`detect_types` フラグを使用したデータベースコネクションで有効です。 :const:`PARSE_DECLTYPES` を使用すると、そのテーブルが定義されたときにカスタム型で定義された列になります。

.. include:: sqlite3_date_types.py
   :literal:
   :start-after: #end_pymotw_header

..
    :mod:`sqlite3` provides converters for date and timestamp columns,
    using :class:`date` and :class:`datetime` from the :mod:`datetime`
    module to represent the values in Python.  Both date-related
    converters are enabled automatically when type-detection is turned on.

:mod:`sqlite3` は :mod:`datetime` モジュールから :class:`date` と :class:`datetime` を使用して、Python で日付やタイムスタンプの列を扱うための変換機能を提供します。両方の日付に関する変換機能は型検出が有効なときに自動的に有効になります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sqlite3_date_types.py'))
.. }}}

::

	$ python sqlite3_date_types.py
	
	Without type detection:
	  column: id
	    value : 1
	    type  : <type 'int'>
	  column: details
	    value : write about select
	    type  : <type 'unicode'>
	  column: deadline
	    value : 2010-10-03
	    type  : <type 'unicode'>
	
	With type detection:
	  column: id
	    value : 1
	    type  : <type 'int'>
	  column: details
	    value : write about select
	    type  : <type 'unicode'>
	  column: deadline
	    value : 2010-10-03
	    type  : <type 'datetime.date'>

.. {{{end}}}

..
    Custom Types
    ------------

カスタム型
----------

..
    Two functions need to be registered to define a new type.  The
    *adapter* takes the Python object as input and returns a byte string
    that can be stored in the database.  The *converter* receives the
    string from the database and returns a Python object.  Use
    :func:`register_adapter` to define an adapter function, and
    :func:`register_converter` for a converter function.

新しい型を定義するために2つの関数を登録する必要があります。 *アダプタ* は入力として Python オブジェクトを受け取り、データベースに格納されるバイト列を返します。 *コンバータ* はデータベースから文字列を受け取り、Python オブジェクトを返します。アダプタ関数を定義するには :func:`register_adapter` を、コンバータ関数には :func:`register_converter` を使用してください。

.. include:: sqlite3_custom_type.py
   :literal:
   :start-after: #end_pymotw_header

..
    This example uses :mod:`pickle` to save an object to a string that can
    be stored in the database.  This technique is useful for storing
    arbitrary objects, but does not allow querying based on object
    attributes.  A real *object-relational mapper* such as SQLAlchemy
    that stores attribute values in their own columns will be more useful
    for large amounts of data.

このサンプルは、あるオブジェクトをデータベースに格納する文字列として保存するために :mod:`pickle` を使用します。このテクニックは任意のオブジェクトを格納するのに便利ですが、
オブジェクト属性をベースにしてクエリすることができません。独自の型に属性値を格納する SQLAlchemy のような、実際の *オブジェクト関係マッパー* は大量データを扱うのにもっと便利でしょう。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sqlite3_custom_type.py', break_lines_at=70))
.. }}}

::

	$ python sqlite3_custom_type.py
	
	adapter_func(MyObj('this is a value to save'))
	
	adapter_func(MyObj(42))
	
	converter_func("ccopy_reg\n_reconstructor\np1\n(c__main__\nMyObj\np2\n
	c__builtin__\nobject\np3\nNtRp4\n(dp5\nS'arg'\np6\nS'this is a value t
	o save'\np7\nsb.")
	
	converter_func("ccopy_reg\n_reconstructor\np1\n(c__main__\nMyObj\np2\n
	c__builtin__\nobject\np3\nNtRp4\n(dp5\nS'arg'\np6\nI42\nsb.")
	
	Retrieved 1 MyObj('this is a value to save') <class '__main__.MyObj'>
	
	Retrieved 2 MyObj(42) <class '__main__.MyObj'>
	

.. {{{end}}}

..
    Deriving Types from Column Names
    --------------------------------

列名から型を派生する
--------------------

..
    There are two sources for types information about the data for a
    query.  The original table declaration can be used to identify the
    type of a real column, as shown above.  A type specifier can also be
    included in the :command:`select` clause of the query itself using the
    form ``as "name [type]"``.

クエリのそのデータに関する型情報のために2つの情報源があります。オリジナルのテーブル定義は、この前のセクションで紹介したように本当の列の型を識別するために使用されます。さらに型識別子は ``as "name [type]"`` の形でクエリ内の :command:`select` 句に含めることもできます。

.. include:: sqlite3_custom_type_column.py
   :literal:
   :start-after: #end_pymotw_header

..
    Use the :data:`detect_types` flag :const:`PARSE_COLNAMES` when type is
    part of the query instead of the original table definition.

オリジナルのテーブル定義の代わりにクエリの一部に型があるときは :data:`detect_types` フラグに :const:`PARSE_COLNAMES` を使用してください。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sqlite3_custom_type_column.py', break_lines_at=70))
.. }}}

::

	$ python sqlite3_custom_type_column.py
	
	adapter_func(MyObj('this is a value to save'))
	
	adapter_func(MyObj(42))
	
	converter_func("ccopy_reg\n_reconstructor\np1\n(c__main__\nMyObj\np2\n
	c__builtin__\nobject\np3\nNtRp4\n(dp5\nS'arg'\np6\nS'this is a value t
	o save'\np7\nsb.")
	
	converter_func("ccopy_reg\n_reconstructor\np1\n(c__main__\nMyObj\np2\n
	c__builtin__\nobject\np3\nNtRp4\n(dp5\nS'arg'\np6\nI42\nsb.")
	
	Retrieved 1 MyObj('this is a value to save') <class '__main__.MyObj'>
	
	Retrieved 2 MyObj(42) <class '__main__.MyObj'>
	

.. {{{end}}}

..
    Transactions
    ============

トランザクション
================

..
    One of the key features of relational databases is the use of
    *transactions* to maintain a consistent internal state.  With
    transactions enabled, several changes can be made through one
    connection without effecting any other users until the results are
    *committed* and flushed to the actual database.  

関係データベースの重要な機能の1つは *トランザクション* であり、一貫した内部状態を保持するために使用します。トランザクションを有効にすることで1つのコネクションを通した複数の変更に対して、その結果が *コミット* されて実際にデータベースへ書き込まれるまで他のユーザへ影響を与えずに行うことができます。

..
    Preserving Changes
    ------------------

変更を保存する
--------------

..
    Changes to the database, either through :command:`insert` or
    :command:`update` statements, need to be saved by explicitly calling
    :func:`commit`.  This requirement gives an application an opportinity
    to make several related changes together, and have them stored
    *atomically* instead of incrementally, and avoids a situation where
    partial updates are seen by different clients connecting to the
    database.

:command:`insert` か :command:`update` 文のどちらかでデータベースを変更するとき、明示的に :func:`commit` を呼び出して保存する必要があります。この要求はアプリケーションに対して同時に関連する複数の変更を行う機会を与えます。そして、インクリメンタルではなく *原始的* に複数の変更を保存して、データベースへ複数のクライアントが接続することによる部分的な更新が行われないようにします。

..
    The effect of calling :func:`commit` can be seen with a program that
    uses several connections to the database.  A new row is inserted with
    the first connection, and then two attempts are made to read it back
    using separate connections.

:func:`commit` を呼び出す効果はデータベースへ複数のコネクションを持つプログラムを見ると分かり易いです。最初のコネクションで新たな行を追加した後、別のコネクションを使用してその行を読み込もうと2回行います。

.. include:: sqlite3_transaction_commit.py
   :literal:
   :start-after: #end_pymotw_header

..
    When :func:`show_projects` is called before :data:`conn1` has been
    committed, the results depend on which connection is used.  Since the
    change was made through :data:`conn1`, it sees the altered data.
    However, :data:`conn2` does not.  After committing, the new connection
    :data:`conn3` sees the inserted row.

:data:`conn1` がコミットされる前に :func:`show_projects` が呼び出されると、その結果はどちらのコネクションが使用されるかに依ります。その変更は :data:`conn1` を通して行われたので、その変更されたデータが確認されます。しかし :data:`conn2` はそうではありません。コミットした後で、新たなコネクション :data:`conn3` ではその追加された行が確認されます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sqlite3_transaction_commit.py'))
.. }}}

::

	$ python sqlite3_transaction_commit.py
	
	Before changes:
	   pymotw
	
	After changes in conn1:
	   pymotw
	   virtualenvwrapper
	
	Before commit:
	   pymotw
	
	After commit:
	   pymotw
	   virtualenvwrapper

.. {{{end}}}

..
    Discarding Changes
    ------------------

変更を放棄する
--------------

..
    Uncommitted changes can also be discarded entirely using
    :func:`rollback`.  The :func:`commit` and :func:`rollback` methods are
    usually called from different parts of the same ``try:except`` block,
    with errors triggering a rollback.

また、コミットされていない変更は :func:`rollback` で完全に放棄することもできます。 :func:`commit` と :func:`rollback` メソッドは、普通は同じ ``try:except`` ブロックの違う部分から呼び出されます。つまり、エラーはロールバックのトリガーとなります。

.. include:: sqlite3_transaction_rollback.py
   :literal:
   :start-after: #end_pymotw_header

..
    After calling :func:`rollback`, the changes to the database are no
    longer present.

:func:`rollback` を呼び出した後はデータベースに対する変更はありません。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sqlite3_transaction_rollback.py'))
.. }}}

::

	$ python sqlite3_transaction_rollback.py
	
	Before changes:
	   pymotw
	   virtualenvwrapper
	
	After delete:
	   pymotw
	ERROR: simulated error
	
	After rollback:
	   pymotw
	   virtualenvwrapper

.. {{{end}}}

..
    Isolation Levels
    ----------------

分離レベル
----------

..
    :mod:`sqlite3` supports three locking modes, called *isolation
    levels*, that control the locks used to prevent incompatible changes
    between connections.  The isolation level is set by passing a string
    as the *isolation_level* argument when a connection is opened, so
    different connections can use different values.

:mod:`sqlite3` は *分離レベル(isolation levels)* と呼ばれる3つのロックモードをサポートします。それはコネクション間で非互換な変更を行わないように使用されるロックを制御します。分離レベルはコネクションがオープンされるときに *isolation_level* 引数として文字列を渡すことでセットします。そのため、コネクションが違えば違う値を使用できます。

..
    This program demonstrates the effect of different isolation levels on
    the order of events in threads using separate connections to the same
    database.  Four threads are created.  Two threads write changes to the
    database by updating existing rows.  The other two threads attempt to
    read all of the rows from the ``task`` table.

このプログラムは同じデータベースに対して独立したコネクションを使用するスレッドのイベントの順番で違う分離レベルの効果を説明します。4つのスレッドが作成されます。2つのスレッドは既存の行を更新することでデータベースに変更を書き込みます。他の2つのスレッドは ``task`` テーブルから全ての行を読み込もうとします。

.. include:: sqlite3_isolation_levels.py
   :literal:
   :start-after: #end_pymotw_header

..
    The threads are synchronized using a :class:`Event` from the
    :mod:`threading` module.  The :func:`writer` function connects and
    make changes to the database, but does not commit before the event
    fires.  The :func:`reader` function connects, then waits to query the
    database until after the synchronization event occurs.

そのスレッドは :mod:`threading` モジュールの :class:`Event` を使用して同期します。 :func:`writer` 関数は接続して、データベースに変更を書き込みますが、そのイベントが発生する前にはコミットしません。 :func:`reader` 関数は接続してから、同期イベントの発生後までデータベースにクエリするのを待ちます。

..
    Deferred
    ~~~~~~~~

遅延(Deferred)
~~~~~~~~~~~~~~

..
    The default isolation level is ``DEFERRED``.  Using deferred mode
    locks the database, but only once a change is begun.  All of the
    previous examples use deferred mode.

デフォルトの分離レベルは ``DEFERRED`` です。遅延モードを使用するとデータベースをロックしますが、1度に1つの変更のみが開始されます。これまでの全てのサンプルは遅延モードを使用します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sqlite3_isolation_levels.py DEFERRED'))
.. }}}

::

	$ python sqlite3_isolation_levels.py DEFERRED
	
	2013-02-21 06:36:58,573 (Reader 1  ) waiting to synchronize
	2013-02-21 06:36:58,573 (Reader 2  ) waiting to synchronize
	2013-02-21 06:36:58,573 (Writer 1  ) connecting
	2013-02-21 06:36:58,574 (Writer 2  ) connecting
	2013-02-21 06:36:58,574 (Writer 1  ) connected
	2013-02-21 06:36:58,574 (Writer 2  ) connected
	2013-02-21 06:36:58,574 (Writer 1  ) changes made
	2013-02-21 06:36:58,575 (Writer 1  ) waiting to synchronize
	2013-02-21 06:36:59,574 (MainThread) setting ready
	2013-02-21 06:36:59,575 (Writer 1  ) PAUSING
	2013-02-21 06:36:59,575 (Reader 2  ) wait over
	2013-02-21 06:36:59,575 (Reader 1  ) wait over
	2013-02-21 06:36:59,576 (Reader 2  ) SELECT EXECUTED
	2013-02-21 06:36:59,576 (Reader 1  ) SELECT EXECUTED
	2013-02-21 06:36:59,577 (Reader 2  ) results fetched
	2013-02-21 06:36:59,577 (Reader 1  ) results fetched
	2013-02-21 06:37:00,579 (Writer 1  ) CHANGES COMMITTED
	2013-02-21 06:37:00,625 (Writer 2  ) changes made
	2013-02-21 06:37:00,626 (Writer 2  ) waiting to synchronize
	2013-02-21 06:37:00,626 (Writer 2  ) PAUSING
	2013-02-21 06:37:01,629 (Writer 2  ) CHANGES COMMITTED

.. {{{end}}}

..
    Immediate
    ~~~~~~~~~

即時(Immediate)
~~~~~~~~~~~~~~~

..
    Immediate mode locks the database as soon as a change starts and
    prevents other cursors from making changes until the transaction is
    committed.  It is suitable for a database with complicated writes but
    more readers than writers, since the readers are not blocked while the
    transaction is ongoing.

即時モードは変更が開始されるとすぐにデータベースをロックして、そのトランザクションがコミットされるまで他のカーソルから変更できないようにします。それは書き込みよりも読み込みの方が多いが、複雑な書き込みを行うデータベースには適しています。読み込みはトランザクションが進行中でもブロックされないからです。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sqlite3_isolation_levels.py IMMEDIATE'))
.. }}}

::

	$ python sqlite3_isolation_levels.py IMMEDIATE
	
	2013-02-21 06:37:01,668 (Reader 2  ) waiting to synchronize
	2013-02-21 06:37:01,668 (Reader 1  ) waiting to synchronize
	2013-02-21 06:37:01,669 (Writer 1  ) connecting
	2013-02-21 06:37:01,669 (Writer 2  ) connecting
	2013-02-21 06:37:01,669 (Writer 1  ) connected
	2013-02-21 06:37:01,669 (Writer 2  ) connected
	2013-02-21 06:37:01,670 (Writer 1  ) changes made
	2013-02-21 06:37:01,670 (Writer 1  ) waiting to synchronize
	2013-02-21 06:37:02,670 (MainThread) setting ready
	2013-02-21 06:37:02,671 (Writer 1  ) PAUSING
	2013-02-21 06:37:02,671 (Reader 2  ) wait over
	2013-02-21 06:37:02,671 (Reader 1  ) wait over
	2013-02-21 06:37:02,672 (Reader 2  ) SELECT EXECUTED
	2013-02-21 06:37:02,672 (Reader 1  ) SELECT EXECUTED
	2013-02-21 06:37:02,673 (Reader 2  ) results fetched
	2013-02-21 06:37:02,673 (Reader 1  ) results fetched
	2013-02-21 06:37:03,675 (Writer 1  ) CHANGES COMMITTED
	2013-02-21 06:37:03,724 (Writer 2  ) changes made
	2013-02-21 06:37:03,724 (Writer 2  ) waiting to synchronize
	2013-02-21 06:37:03,725 (Writer 2  ) PAUSING
	2013-02-21 06:37:04,729 (Writer 2  ) CHANGES COMMITTED

.. {{{end}}}

..
    Exclusive
    ~~~~~~~~~

排他(Exclusive)
~~~~~~~~~~~~~~~

..
    Exclusive mode locks the database to all readers and writers.  Its use
    should be limited in situations where database performance is
    important, since each exclusive connection blocks all other users.

排他モードは全ての読み込みと書き込みに対してデータベースをロックします。それぞれの排他コネクションが他の全てのユーザをブロックするので、データベースのパフォーマンスが重要な状況に限定して使用すべきです。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sqlite3_isolation_levels.py EXCLUSIVE'))
.. }}}

::

	$ python sqlite3_isolation_levels.py EXCLUSIVE
	
	2013-02-21 06:37:04,769 (Reader 2  ) waiting to synchronize
	2013-02-21 06:37:04,769 (Writer 1  ) connecting
	2013-02-21 06:37:04,768 (Reader 1  ) waiting to synchronize
	2013-02-21 06:37:04,769 (Writer 2  ) connecting
	2013-02-21 06:37:04,769 (Writer 1  ) connected
	2013-02-21 06:37:04,769 (Writer 2  ) connected
	2013-02-21 06:37:04,771 (Writer 1  ) changes made
	2013-02-21 06:37:04,771 (Writer 1  ) waiting to synchronize
	2013-02-21 06:37:05,770 (MainThread) setting ready
	2013-02-21 06:37:05,771 (Reader 1  ) wait over
	2013-02-21 06:37:05,771 (Reader 2  ) wait over
	2013-02-21 06:37:05,771 (Writer 1  ) PAUSING
	2013-02-21 06:37:06,775 (Writer 1  ) CHANGES COMMITTED
	2013-02-21 06:37:06,816 (Reader 2  ) SELECT EXECUTED
	2013-02-21 06:37:06,816 (Reader 1  ) SELECT EXECUTED
	2013-02-21 06:37:06,817 (Reader 2  ) results fetched
	2013-02-21 06:37:06,817 (Reader 1  ) results fetched
	2013-02-21 06:37:06,819 (Writer 2  ) changes made
	2013-02-21 06:37:06,819 (Writer 2  ) waiting to synchronize
	2013-02-21 06:37:06,819 (Writer 2  ) PAUSING
	2013-02-21 06:37:07,822 (Writer 2  ) CHANGES COMMITTED

.. {{{end}}}

..
    Because the first writer has started making changes, the readers and
    second writer block until it commits.  The :func:`sleep` call
    introduces an artificial delay in the writer thread to highlight the
    fact that the other connections are blocking.

最初の writer が変更を開始するので、その reader と2番目の writer は最初の writer がコミットされるまでブロックします。 :func:`sleep` 呼び出しは writer スレッドで人工的な遅延を発生させて、他のコネクションがブロックされているという現象を目立たせます。

..
    Autocommit
    ~~~~~~~~~~

自動コミット
~~~~~~~~~~~~

..
    The *isolation_level* parameter for the connection can also be set to
    ``None`` to enable autocommit mode.  With autocommit enabled, each
    :func:`execute` call is committed immediately when the statement
    finishes.  Autocommit mode is suited for short transactions, such as
    those that insert a small amount of data into a single table.  The
    database is locked for as little time as possible, so there is less
    chance of contention between threads.

コネクションの *isolation_level* パラメータは自動コミットモードを有効にする ``None`` をセットすることもできます。自動コミットが有効になると、それぞれの :func:`execute` 呼び出しは終了時に即コミットされます。自動コミットモードは、1つのテーブルに小さなデータを追加するような短いトランザクションに適しています。スレッド間で衝突する機会が少ないので、データベースはできるだけ短い時間ロックされます。

.. include:: sqlite3_autocommit.py
   :literal:
   :start-after: #end_pymotw_header

..
    The explicit call to :func:`commit` has been removed, but otherwise
    ``sqlite3_autocommit.py`` is the same as
    ``sqlite3_isolation_levels.py``.  The output is different, however,
    since both writer threads finish their work before either reader
    starts querying.

:func:`commit` の明示的な呼び出しを除去している点を除けば ``sqlite3_autocommit.py`` は ``sqlite3_isolation_levels.py`` と同じです。しかし、どちらの reader もクエリを開始する前に両方の writer スレッドの処理が終了するので出力は違っています。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sqlite3_autocommit.py'))
.. }}}

::

	$ python sqlite3_autocommit.py
	
	2013-02-21 06:37:07,878 (Reader 1  ) waiting to synchronize
	2013-02-21 06:37:07,878 (Reader 2  ) waiting to synchronize
	2013-02-21 06:37:07,878 (Writer 1  ) connecting
	2013-02-21 06:37:07,878 (Writer 2  ) connecting
	2013-02-21 06:37:07,878 (Writer 1  ) connected
	2013-02-21 06:37:07,879 (Writer 2  ) connected
	2013-02-21 06:37:07,880 (Writer 2  ) changes made
	2013-02-21 06:37:07,880 (Writer 2  ) waiting to synchronize
	2013-02-21 06:37:07,881 (Writer 1  ) changes made
	2013-02-21 06:37:07,881 (Writer 1  ) waiting to synchronize
	2013-02-21 06:37:08,879 (MainThread) setting ready
	2013-02-21 06:37:08,880 (Writer 1  ) PAUSING
	2013-02-21 06:37:08,880 (Writer 2  ) PAUSING
	2013-02-21 06:37:08,880 (Reader 1  ) wait over
	2013-02-21 06:37:08,881 (Reader 2  ) wait over
	2013-02-21 06:37:08,882 (Reader 2  ) SELECT EXECUTED
	2013-02-21 06:37:08,882 (Reader 1  ) SELECT EXECUTED
	2013-02-21 06:37:08,882 (Reader 2  ) results fetched
	2013-02-21 06:37:08,882 (Reader 1  ) results fetched

.. {{{end}}}

..
    User-defined Behaviors
    ======================

ユーザ定義の振る舞い
====================

..
    :mod:`sqlite3` supports several extension mechanisms, with support for
    extending the database features with functions and classes implemented
    in Python.

:mod:`sqlite3` は Python で実装された関数やクラスでデータベースの機能拡張と複数の拡張の仕組みをサポートします。

..
    Using Python Functions in SQL
    -----------------------------

SQL で Python 関数を使用する
----------------------------

..
    SQL syntax supports calling functions with during queries, either in
    the column list or :command:`where` clause of the :command:`select`
    statement.  This feature makes it possible to process data before
    returning it from the query, and can be used to convert between
    different formats, perform calculations that would be clumsy in pure
    SQL, and reuse application code.

SQL 構文はその列のリストか :command:`select` 文の :command:`where` 句のどちらかで、クエリ中の関数呼び出しをサポートします。この機能は SQL にクエリから処理したデータを返す前にそのデータを処理することを可能にします。そして、違うフォーマット間の変換に使用できて、純粋な SQL では体裁の悪い演算を行い、アプリケーションのコードを再利用します。

.. include:: sqlite3_create_function.py
   :literal:
   :start-after: #end_pymotw_header

..
    Functions are exposed using the :func:`create_function` method of the
    :class:`Connection`.  The parameters are the name of the function (as
    it should be used from within SQL), the number of arguments the
    function takes, and the Python function to expose.

:class:`Connection` の :func:`create_function` メソッドで SQL から見えるように関数を公開します。そのパラメータは(SQL 内で使用される)関数の名前、関数が受け取る引数の数や公開する Python の関数です。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sqlite3_create_function.py'))
.. }}}

::

	$ python sqlite3_create_function.py
	
	Original values:
	(1, u'write about select')
	(2, u'write about random')
	(3, u'write about sqlite3')
	(4, u'finish reviewing markup')
	(5, u'revise chapter intros')
	(6, u'subtitle')
	
	Encrypting...
	Encrypting u'write about select'
	Encrypting u'write about random'
	Encrypting u'write about sqlite3'
	Encrypting u'finish reviewing markup'
	Encrypting u'revise chapter intros'
	Encrypting u'subtitle'
	
	Raw encrypted values:
	(1, u'jevgr nobhg fryrpg')
	(2, u'jevgr nobhg enaqbz')
	(3, u'jevgr nobhg fdyvgr3')
	(4, u'svavfu erivrjvat znexhc')
	(5, u'erivfr puncgre vagebf')
	(6, u'fhogvgyr')
	
	Decrypting in query...
	Decrypting u'jevgr nobhg fryrpg'
	Decrypting u'jevgr nobhg enaqbz'
	Decrypting u'jevgr nobhg fdyvgr3'
	Decrypting u'svavfu erivrjvat znexhc'
	Decrypting u'erivfr puncgre vagebf'
	Decrypting u'fhogvgyr'
	(1, u'write about select')
	(2, u'write about random')
	(3, u'write about sqlite3')
	(4, u'finish reviewing markup')
	(5, u'revise chapter intros')
	(6, u'subtitle')

.. {{{end}}}

..
    Custom Aggregation
    ------------------

カスタム集約
------------

..
    An aggregation function collects many pieces of individual data and
    summarizes it in some way.  Examples of built-in aggregation functions
    are :func:`avg` (average), :func:`min`, :func:`max`, and
    :func:`count`.

集約関数は多くの個々のデータを集めて、何らかの方法でそういったデータを集約します。組み込みの集約関数の例は :func:`avg` (平均), :func:`min`, :func:`max` や :func:`count` です。

..
    The API for aggregators used by :mod:`sqlite3` is defined in terms of
    a class with two methods.  The :func:`step` method is called once for
    each data value as the query is processed.  The :func:`finalize`
    method is called one time at the end of the query and should return
    the aggregate value.  This example implements an aggregator for the
    arithmetic *mode*.  It returns the value that appears most frequently
    in the input.

:mod:`sqlite3` が使用する集約の API は2つのメソッドを持つクラスで定義されます。 :func:`step` メソッドはそのクエリが処理されるときに、それぞれのデータの値につき呼び出されます。 :func:`finalize` メソッドはそのクエリの最後で1回呼び出されて集約された値を返します。このサンプルは算術的な *mode* の集約関数を実装します。その集約関数は入力に最も多く現れた値を返します。

.. include:: sqlite3_create_aggregate.py
   :literal:
   :start-after: #end_pymotw_header

..
    The aggregator class is registered with the :func:`create_aggregate`
    method of the :class:`Connection`.  The parameters are the name of the
    function (as it should be used from within SQL), the number of
    arguments the :func:`step` method takes, and the class to use.

:class:`Connection` の :func:`create_aggregate` メソッドで集約クラスを登録します。そのパラメータは(SQL 内で使用される)関数の名前、 :func:`step` が受け取る引数の数と使用するクラスです。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sqlite3_create_aggregate.py'))
.. }}}

::

	$ python sqlite3_create_aggregate.py
	
	step(u'2010-10-03')
	step(u'2010-10-10')
	step(u'2010-10-17')
	step(u'2010-10-02')
	step(u'2010-10-03')
	step(u'2010-10-03')
	finalize() -> u'2010-10-03' (3 times)
	mode(deadline) is: 2010-10-03

.. {{{end}}}

..
    Custom Sorting
    --------------

カスタムソート
--------------

..
    A *collation* is a comparison function used in the :command:`order by`
    section of an SQL query.  Custom collations can be used to compare
    data types that could not otherwise be sorted by SQLite internally.
    For example, a custom collation would be needed to sort the pickled
    objects saved in ``sqlite3_custom_type.py`` above.

*照合(collation)* は SQL クエリの :command:`order by` セクションで使用される比較関数です。カスタム照合は内部的に SQLite がソートできないデータ型を比較するために使用されます。例えば、カスタム照合はこの前のセクションで紹介した ``sqlite3_custom_type.py`` で保存した pickle 化されたオブジェクトをソートするために必要です。

.. include:: sqlite3_create_collation.py
   :literal:
   :start-after: #end_pymotw_header

..
    The arguments to the collation function are byte strings, so they must
    be unpickled and converted to :class:`MyObj` instances before the
    comparison can be performed.

照合関数の引数はバイト列なので、その引数は比較処理が行われる前に unpickle されて :class:`MyObj` インスタンスへ変換されます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sqlite3_create_collation.py'))
.. }}}

::

	$ python sqlite3_create_collation.py
	
	
	Querying:
	collation_func(MyObj(5), MyObj(4))
	collation_func(MyObj(4), MyObj(3))
	collation_func(MyObj(4), MyObj(2))
	collation_func(MyObj(3), MyObj(2))
	collation_func(MyObj(3), MyObj(1))
	collation_func(MyObj(2), MyObj(1))
	7 MyObj(1)
	
	6 MyObj(2)
	
	5 MyObj(3)
	
	4 MyObj(4)
	
	3 MyObj(5)
	

.. {{{end}}}

..
    Restricting Access to Data
    ==========================

データへのアクセスを制限する
============================

..
    Although SQLite does not have user access controls found in other,
    larger, relational databases, it does have a mechanism for limiting
    access to columns.  Each connection can install an *authorizer
    function* to grant or deny access to columns at runtime based on any
    desired criteria.  The authorizer function is invoked during the
    parsing of SQL statements, and is passed five arguments.  The first is
    an action code indicating the type of operation being performed
    (reading, writing, deleting, etc.).  The rest of the arguments depend
    on the action code.  For :const:`SQLITE_READ` operations, the
    arguments are the name of the table, the name of the column, the
    location in the SQL where the access is occuring (main query, trigger,
    etc.), and ``None``.  

SQLite は他の大規模な関係データベースで見られるユーザアクセス制御を行いませんが、列に対するアクセスを制限する仕組みを持っています。それぞれのコネクションは、要求される基準で実行時に列へのアクセスを許可する、または拒否するために *認証関数* をインストールすることができます。認証関数は SQL 文の構文解析を行うときに実行されて、5つの引数が渡されます。1つ目は実行される操作の種別(読み込み、書き込み、削除、その他)を示すアクションコードです。残りの引数はアクションコード次第で変わってきます。 :const:`SQLITE_READ` 操作では、その引数はテーブルの名前、列の名前、そのアクセスが発生する SQL の場所(メインクエリ、トリガー等)と ``None`` です。

.. include:: sqlite3_set_authorizer.py
   :literal:
   :start-after: #end_pymotw_header

..
    This example uses :const:`SQLITE_IGNORE` to cause the strings from the
    ``task.details`` column to be replaced with null values in the query
    results.  It also prevents all access to the ``task.priority`` column
    by returning :const:`SQLITE_DENY`, which in turn causes SQLite to
    raise an exception.

このサンプルは :const:`SQLITE_IGNORE` を使用して、クエリ結果の ``task.details`` 列の文字列を Null 値で置き換えます。さらに :const:`SQLITE_DENY` を返すことで ``task.priority`` 列への全てのアクセスを SQLite に例外を発生させることで拒否します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sqlite3_set_authorizer.py', ignore_error=True))
.. }}}

::

	$ python sqlite3_set_authorizer.py
	
	Using SQLITE_IGNORE to mask a column value:
	
	authorizer_func(21, None, None, None, None)
	requesting permission to run a select statement
	
	authorizer_func(20, task, id, main, None)
	requesting permission to access the column task.id from main
	
	authorizer_func(20, task, details, main, None)
	requesting permission to access the column task.details from main
	  ignoring details column
	
	authorizer_func(20, task, project, main, None)
	requesting permission to access the column task.project from main
	1 None
	2 None
	3 None
	4 None
	5 None
	6 None
	
	Using SQLITE_DENY to deny access to a column:
	
	authorizer_func(21, None, None, None, None)
	requesting permission to run a select statement
	
	authorizer_func(20, task, id, main, None)
	requesting permission to access the column task.id from main
	
	authorizer_func(20, task, priority, main, None)
	requesting permission to access the column task.priority from main
	  preventing access to priority column
	Traceback (most recent call last):
	  File "sqlite3_set_authorizer.py", line 47, in <module>
	    cursor.execute("select id, priority from task where project = 'pymotw'")
	sqlite3.DatabaseError: access to task.priority is prohibited

.. {{{end}}}

..
    The possible action codes are available as constants in
    :mod:`sqlite3`, with names prefixed ``SQLITE_``.  Each type of SQL
    statement can be flagged, and access to individual columns can be
    controlled as well.

アクションコードは :mod:`sqlite3` の ``SQLITE_`` の接頭辞を持つ定数が利用できると考えられます。SQL 文のそれぞれの種別はフラグで指定されて、同様に個々の列に対するアクセス制御が行われます。

.. Extension Modules
.. =================

.. .. Only works if the proper version of the sqlite library is available
.. .. during compilation

.. * full-text search
.. * loading from api
.. * loading from sql

..
    In-Memory Databases
    ===================

インメモリデータベース
======================

..
    SQLite supports managing an entire database in RAM, instead of relying
    on a disk file.  In-memory databases are useful for automated testing,
    where the database does not need to be preserved between test runs, or
    when experimenting with a schema or other database features.  To open
    an in-memory database, use the string ``':memory:'`` instead of a
    filename when creating the :class:`Connection`.

SQLite はディスク上のファイルに頼らずに RAM 上での完全なデータベース管理をサポートします。インメモリデータベースはデータベースをテスト間で保存する必要がない自動テスト、もしくはスキーマやその他のデータベース機能の検証を行うときに便利です。インメモリデータベースをオープンするには :class:`Connection` を作成するとき、ファイル名の代わりに ``':memory:'`` を使用してください。

.. include:: sqlite3_memory.py
   :literal:
   :start-after: #end_pymotw_header

..
    The second query attempt in this example fails with an error because
    the table does not exist.  Each connection creates a separate
    database, so changes made by a cursor in one do not effect other
    connections.

このサンプルの2番目のクエリはテーブルが存在しないのでエラーで失敗します。コネクション毎に独立したデータベースを作成するので、あるカーソルによる変更は他のコネクションに影響しません。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sqlite3_memory.py', ignore_error=True))
.. }}}

::

	$ python sqlite3_memory.py
	
	Creating schema
	Inserting initial data
	Looking for tasks...
	 1 {1} write about select        [done    ] (2010-10-03)
	 2 {1} write about random        [waiting ] (2010-10-10)
	 3 {1} write about sqlite3       [active  ] (2010-10-17)
	
	Looking for tasks in second connection...
	Traceback (most recent call last):
	  File "sqlite3_memory.py", line 54, in <module>
	    """)
	sqlite3.OperationalError: no such table: task

.. {{{end}}}

..
    Exporting the Contents of a Database
    ====================================

データベースのコンテンツをエクスポートする
==========================================

..
    The contents of an in-memory database can be saved using the
    :func:`iterdump` method of the :class:`Connection`.  The iterator
    returned by :func:`iterdump` produces a series of strings which
    together build SQL instructions to recreate the state of the database.

インメモリデータベースのコンテンツは :class:`Connection` の :func:`iterdump` メソッドを使用して保存されます。 :func:`iterdump` が返すイテレータはデータベースの状態を再作成する SQL 命令をまとめて構築する一連の文字列を生成します。

.. include:: sqlite3_iterdump.py
   :literal:
   :start-after: #end_pymotw_header

..
    :func:`iterdump` can also be used with databases saved to files, but
    it is most useful for preserving a database that would not otherwise
    be saved.

また :func:`iterdump` はファイルに保存されたデータベースで使用することもできますが、他の方法で保存されないデータベースを保存するために使用すると最も便利です。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sqlite3_iterdump.py'))
.. }}}

::

	$ python sqlite3_iterdump.py
	
	Creating schema
	Inserting initial data
	Dumping:
	BEGIN TRANSACTION;
	CREATE TABLE project (
	    name        text primary key,
	    description text,
	    deadline    date
	);
	INSERT INTO "project" VALUES('pymotw','Python Module of the Week','2010-11-01');
	CREATE TABLE task (
	    id           integer primary key autoincrement not null,
	    priority     integer default 1,
	    details      text,
	    status       text,
	    deadline     date,
	    completed_on date,
	    project      text not null references project(name)
	);
	INSERT INTO "task" VALUES(1,1,'write about select','done','2010-10-03',NULL,'pymotw');
	INSERT INTO "task" VALUES(2,1,'write about random','waiting','2010-10-10',NULL,'pymotw');
	INSERT INTO "task" VALUES(3,1,'write about sqlite3','active','2010-10-17',NULL,'pymotw');
	DELETE FROM sqlite_sequence;
	INSERT INTO "sqlite_sequence" VALUES('task',3);
	COMMIT;

.. {{{end}}}

..
    Threading and Connection Sharing
    ================================

スレッドとコネクションの共有
============================

..
    For historical reasons having to do with old versions of SQLite,
    :class:`Connection` objects cannot be shared between threads.  Each
    thread must create its own connection to the database.

歴史的な理由で SQLite の旧バージョンで行わなければならない :class:`Connection` オブジェクトはスレッド間で共有されません。それぞれのスレッドはデータベースへの独自のコネクションを作成しなければなりません。

.. include:: sqlite3_threading.py
   :literal:
   :start-after: #end_pymotw_header

..
    Attempts to share a connection between threads result in an exception.

スレッド間でコネクションを共有しようとすると例外が発生します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sqlite3_threading.py'))
.. }}}

::

	$ python sqlite3_threading.py
	
	Starting thread
	ERROR: SQLite objects created in a thread can only be used in that same thread.The object was created in thread id 140735199439200 and this is thread id 4315942912

.. {{{end}}}

.. seealso::

    `sqlite3 <http://docs.python.org/library/sqlite3.html>`_
        .. The standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント

    :pep:`249` -- DB API 2.0 Specificiation
        .. A standard interface for modules that provide access to
           relational databases.

        関係データベースへのアクセスを提供するモジュールの標準インタフェース

    `SQLite`_
        .. The official site of the SQLite library.

        SQLite ライブラリの公式サイト

    :mod:`shelve`
        .. Key-value store for saving arbitrary Python objects.

        任意の Python オブジェクトを保存するキーバリューストア

    `SQLAlchemy <http://sqlalchemy.org/>`_
        .. A popular object-relational mapper that supports SQLite among
           many other relational databases.

        SQLite やその他の多くの関係データベースをサポートする人気のあるオブジェクト関係マッパ

.. _SQLite: http://www.sqlite.org/
