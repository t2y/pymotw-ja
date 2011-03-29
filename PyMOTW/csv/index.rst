..
    ==================================
    csv -- Comma-separated value files
    ==================================

=============================
csv -- カンマ区切りのファイル
=============================

..
    :synopsis: Read and write comma separated value files.

.. module:: csv
    :synopsis: カンマ区切りのファイルを読み書きする

..
    :Purpose: Read and write comma separated value files.
    :Python Version: 2.3 and later

:目的: カンマ区切りのファイルを読み書きする
:Python バージョン: 2.3 以上

..
    The :mod:`csv` module is useful for working with data exported from
    spreadsheets and databases into text files formatted with fields and
    records, commonly referred to as *comma-separated value* (CSV) format
    because commas are often used to separate the fields in a record.

:mod:`csv` モジュールは、スプレッドシートやデータベースからデータをエクスポートして、一般的に *カンマ区切り* (CSV) フォーマットと言う、フィールド(列)とレコード(行)のテキストファイルを処理するのに便利です。カンマは1つのレコードを複数のフィールドに分割するために使用されます。

.. note::

  .. The Python 2.5 version of :mod:`csv` does not support Unicode
     data. There are also "issues with ASCII NUL characters". Using UTF-8
     or printable ASCII is recommended.

  Python 2.5 の :mod:`csv` モジュールでは Unicode データをサポートしません。"ASCII NUL 文字の問題" もあります。UTF-8 か表示可能な ASCII 文字のみ使用することをお奨めします。

..
    Reading
    =======

読み込み処理
============

..
    Use :func:`reader` to create a an object for reading data from a CSV
    file.  The reader can be used as an iterator to process the rows of
    the file in order. For example:

CSV ファイルからデータを読み込んでオブジェクトを作成するには :func:`reader` を使用してください。reader は、ファイルを1行ずつ読み込んで処理するイテレータとして使用されます。例えば、次のようになります。

.. include:: csv_reader.py
    :literal:
    :start-after: #end_pymotw_header

..
    The first argument to :func:`reader` is the source of text lines. In
    this case, it is a file, but any iterable is accepted (:mod:`StringIO`
    instances, lists, etc.).  Other optional arguments can be given to
    control how the input data is parsed.

:func:`reader` の1番目の引数は、テキスト行のソースを渡します。このサンプルはファイルを渡していますが、繰り返し処理可能なオブジェクト(:mod:`StringIO` インスタンス、リスト等)であれば何でも構いません。その他のオプション引数は、入力データの解析方法を管理するために渡されます。

..
    This example file was exported from NeoOffice_.

これは NeoOffice_ からエクスポートされたサンプルファイルです。

.. include:: testdata.csv
    :literal:

..
    As it is read, each row of the input data is parsed and converted to a
    list of strings.

1行ずつ読み込みながら、入力データのそれぞれの行は解析されて文字列のリストへ変換されます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'csv_reader.py testdata.csv'))
.. }}}
.. {{{end}}}

..
    The parser handles line breaks embedded within strings in a row, which
    is why a "row" is not always the same as a "line" of input from the
    file.

パーサは1行の文字列内に組み込まれた改行を扱います。"レコードの行" は、ファイルから入力された "ファイルの行" と必ずしも同じではありません。

.. include:: testlinebreak.csv
    :literal:

..
    Values with line breaks in the input retain the internal line breaks
    when returned by the parser.

改行を含む値の入力は、パーサが返すときに内部に改行を含むように保持します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'csv_reader.py testlinebreak.csv'))
.. }}}
.. {{{end}}}

..
    Writing
    =======

書き込み処理
============

..
    Writing CSV files is just as easy as reading them. Use :func:`writer`
    to create an object for writing, then iterate over the rows, using
    :func:`writerow` to print them.

CSV ファイルの書き込みは、その読み込みと同じぐらい簡単です。 :func:`writer` で書き込むためにオブジェクトを作成してから、 :func:`writerow` を使用してその行を繰り返し処理します。

.. include:: csv_writer.py
    :literal:
    :start-after: #end_pymotw_header

..
    The output does not look exactly like the exported data used in the reader
    example:

その結果出力は、reader サンプルのエクスポートされたデータと厳密には同じではありません。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'csv_writer.py testout.csv'))
.. }}}
.. {{{end}}}

..
    The default quoting behavior is different for the writer, so the string column
    is not quoted. That is easy to change by adding a quoting argument to quote
    non-numeric values:

デフォルトのクォート処理は writer によって違うので、文字列カラムはクォートされません。数値以外の値をクォートするには ``quoting`` 引数を追加することで簡単に変更できます。

::

    writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)

..
    And now the strings are quoted:

これで文字列はクォートされます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'csv_writer_quoted.py testout_quoted.csv'))
.. }}}
.. {{{end}}}

.. _csv-quoting:

クォート処理
------------

..
    Quoting
    -------

..
    There are four different quoting options, defined as constants in the csv
    module.

:mod:`csv` モジュールで定数として定義された4種類の ``quoting`` オプションがあります。

..
    QUOTE_ALL
      Quote everything, regardless of type.

QUOTE_ALL
  型に関係なく全てをクォートする

..
    QUOTE_MINIMAL
      Quote fields with special characters (anything that would confuse a parser
      configured with the same dialect and options). This is the default

QUOTE_MINIMAL
  (同じ dialect やオプションで設定されたパーサを混乱させる任意の)特別文字をもつフィールドをクォートする、デフォルトのオプション

..
    QUOTE_NONNUMERIC
      Quote all fields that are not integers or floats. When used with the reader,
      input fields that are not quoted are converted to floats.

QUOTE_NONNUMERIC
  整数や浮動小数ではない全てのフィールドをクォートする、reader で使用するとクォートされない入力フィールドは浮動小数に変換される

..
    QUOTE_NONE
      Do not quote anything on output. When used with the reader, quote characters
      are included in the field values (normally, they are treated as delimiters and
      stripped).

QUOTE_NONE
  何もクォートしない、reader で使用すると引用符はフィールドの値に含まれる(通常は、デリミタのように扱われて取り除かれる)

..
    Dialects
    ========

Dialect 処理
============

..
    There is no well-defined standard for comma-separated value files, so
    the parser needs to be flexible.  This flexibility means there are
    many parameters to control how :mod:`csv` parses or writes data.
    Rather than passing each of these parameters to the reader and writer
    separately, they are grouped together conveniently into a *dialect*
    object. 

カンマ区切りファイルには広く使用されている標準規格がないので、パーサは柔軟に処理する必要があります。この柔軟性のために :mod:`csv` モジュールがデータを解析する、もしくは書き込む方法を管理するパラメータがたくさんあります。しかし、reader や writer へこういったパラメータの1つずつ指定するというよりも、便利な *dialect* オブジェクトに複数のパラメータがグループ化されています。

..
    Dialect classes can be registered by name, so that callers of the csv
    module do not need to know the parameter settings in advance.  The
    complete list of registered dialects can be retrieved with
    :func:`list_dialects`.

dialect クラスは名前で登録されるので、 :mod:`csv` モジュールの呼び出し側は事前にパラメータ設定を知っている必要はありません。登録済みの dialect クラスの全リストは :func:`list_dialects` 関数で取り出せます。

.. include:: csv_list_dialects.py
   :literal:
   :start-after: #end_pymotw_header

..
    The standard library includes two dialects: ``excel``, and
    ``excel-tabs``. The ``excel`` dialect is for working with data in the
    default export format for Microsoft Excel, and also works with
    OpenOffice or NeoOffice.

標準ライブラリは ``excel`` と ``excel-tabs`` の2つの dialect を提供します。 ``excel`` dialect は、Microsoft Excel のデフォルトエクスポートフォーマットであり、OpenOffice や NeoOffice でも使用します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'csv_list_dialects.py'))
.. }}}
.. {{{end}}}

..
    Creating a Dialect
    ------------------

Dialect を作成する
------------------

..
    Suppose instead of using commas to delimit fields, the input file uses
    ``|``, like this:


次のようにフィールドの区切り文字をカンマではなく ``|`` を使用します。

.. include:: testdata.pipes
    :literal:

..
    A new dialect can be registered using the appropriate delimiter:

新しい dialect に ``delimiter`` を指定して登録できます。

.. include:: csv_dialect.py
    :literal:
    :start-after: #end_pymotw_header

..
    and the file can be read just as with the comma-delimited file:

このファイルは、カンマ区切りのファイルのように読み込まれます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'csv_dialect.py'))
.. }}}
.. {{{end}}}

..
    Dialect Parameters
    ------------------

Dialect パラメータ
------------------

..
    A dialect specifies all of the tokens used when parsing or writing a
    data file.  Every aspect of the file format can be specified, from the
    way columns are delimited to the character used to escape a token.

dialect 特性は、データファイルを解析したり、書き込むときに全てのトークンで使用されます。カラムがトークンのエスケープに使用される文字を区切る方法から、全てのファイルフォーマットの特徴が指定できます。

..
    ================  ======================  =======
    Attribute         Default                 Meaning
    ================  ======================  =======
    delimiter         ``,``                   Field separator (one character)
    doublequote       True                    Flag controlling whether quotechar instances are doubled
    escapechar        None                    Character used to indicate an escape sequence
    lineterminator    ``\r\n``                String used by writer to terminate a line
    quotechar         ``"``                   String to surround fields containing special values (one character)
    quoting           :const:`QUOTE_MINIMAL`  Controls quoting behavior described above
    skipinitialspace  False                   Ignore whitespace after the field delimiter
    ================  ======================  =======

================  ======================  =======
属性              デフォルト              内容
================  ======================  =======
delimiter         ``,``                   フィールドセパレータ (一文字)
doublequote       True                    引用符インスタンスを2重にするかどうかの制御フラグ
escapechar        None                    エスケープシーケンスを表す文字
lineterminator    ``\r\n``                writer が使用する一行の終わりを表す文字列
quotechar         ``"``                   特別な値を含むフィールドを囲むための文字列(一文字)
quoting           :const:`QUOTE_MINIMAL`  前説で説明したクォート処理を制御する
skipinitialspace  False                   フィールド区切り文字の後のスペースを無視する
================  ======================  =======

.. include:: csv_dialect_variations.py
   :literal:
   :start-after: #end_pymotw_header

..
    This program shows how the same data appears in several different dialects.

このプログラムは、複数の dialect で同じデータがどう処理されるかを表示します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'csv_dialect_variations.py'))
.. }}}
.. {{{end}}}

..
    Automatically Detecting Dialects
    --------------------------------

自動的に Dialect を検出する
---------------------------

..
    The best way to configure a dialect for parsing an input file is to
    know the right settings in advance.  For data where the dialect
    parameters are unknown, the :class:`Sniffer` class can be used to make
    an educated guess.  The :func:`sniff` method takes a sample of the
    input data and an optional argument giving the possible delimiter
    characters.

入力ファイルを解析する dialect を設定する最も良い方法は、事前に適切な設定を知っておくことです。dialect パラメータが不明なデータのために、 :class:`Sniffer` クラスが目星を付けるために使用されます。 :func:`sniff` メソッドは入力データのサンプルと、可能性のあるデリミタ文字をオプション引数で受け取ります。

.. include:: csv_dialect_sniffer.py
   :literal:
   :start-after: #end_pymotw_header

..
    :func:`sniff` returns a :class:`Dialect` instance with the settings to
    be used for parsing the data.  The results are not always perfect, as
    demonstrated by the "escaped" dialect in the example.

:func:`sniff` は、データの解析に使用される設定をもつ :class:`Dialect` インスタンスを返します。その実行結果は、このサンプルの "escaped" dialect で紹介するように、必ずしも完全ではないかもしれません。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'csv_dialect_sniffer.py'))
.. }}}
.. {{{end}}}

..
    Using Field Names
    =================

フィールド名を使用する
======================

..
    In addition to working with sequences of data, the :mod:`csv` module
    includes classes for working with rows as dictionaries so that the
    fields can be named. The :class:`DictReader` and :class:`DictWriter`
    classes translate rows to dictionaries instead of lists. Keys for the
    dictionary can be passed in, or inferred from the first row in the
    input (when the row contains headers).

シーケンスデータの処理に加えて、 :mod:`csv` モジュールは、フィールドに名前を付けてディクショナリとして行を処理するクラスを提供します。 :class:`DictReader` と :class:`DictWriter` クラスは、行をリストではなくディクショナリとして変換します。ディクショナリのキーは引数で渡されるか、(ヘッダを含むときに)入力データの先頭行から推定されます。

.. include:: csv_dictreader.py
    :literal:
    :start-after: #end_pymotw_header

..
    The dictionary-based reader and writer are implemented as wrappers
    around the sequence-based classes, and use the same methods and
    arguments. The only difference in the reader API is that rows are
    returned as dictionaries instead of lists or tuples.

ディクショナリベースの reader や writer は、同じメソッドや引数を使用して、シーケンスベースのクラスのラッパーとして実装されます。reader API の唯一の違いは、その行がリストやタプルではなくディクショナリとして返されることです。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'csv_dictreader.py testdata.csv'))
.. }}}
.. {{{end}}}

..
    The :class:`DictWriter` must be given a list of field names so it
    knows how to order the columns in the output.

:class:`DictWriter` は、出力のカラムの順番通りにフィールド名のリストを渡さなければなりません。

.. include:: csv_dictwriter.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'csv_dictwriter.py testout.csv'))
.. }}}
.. {{{end}}}

.. seealso::

    `csv <http://docs.python.org/library/csv.html>`_
        .. The standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント

    :pep:`305`
        .. CSV File API

        CSV ファイル API

.. _NeoOffice: http://www.neooffice.org/
