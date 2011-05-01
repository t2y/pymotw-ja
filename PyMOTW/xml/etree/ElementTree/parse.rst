.. _xml.etree.ElementTree.parsing:

============================
 XML ドキュメントを解析する
============================

..
    =======================
     Parsing XML Documents
    =======================

..
    Parsed XML documents are represented in memory by :class:`ElementTree`
    and :class:`Element` objects connected into a tree structure based on
    the way the nodes in the XML document are nested.

解析された XML ドキュメントは、XML ドキュメントのノードをネストさせる方法に基づいてツリー構造に関連付けた :class:`ElementTree` と :class:`Element` オブジェクトによってインメモリで表されます。

..
    Parsing an Entire Document
    ==========================

ドキュメント全体を解析する
==========================

..
    Parsing an entire document with :func:`parse()` returns an
    :class:`ElementTree` instance.  The tree knows about all of the data
    in the input document, and the nodes of the tree can be searched or
    manipulated in place.  While this flexibility can make working with
    the parsed document a little easier, it typically takes more memory
    than an event-based parsing approach since the entire document must be
    loaded at one time.

ドキュメント全体を :func:`parse()` で解析すると :class:`ElementTree` インスタンスが返されます。このツリーは入力ドキュメントの全てのデータを解釈して、ツリーのノードは適切な位置で検索や操作ができます。この柔軟性は解析されたドキュメントをちょっと扱うには簡単ですが、ドキュメント全体を一度に読み込む必要があるので、イベントベースの解析方法よりも普通はより多くのメモリを使用します。

..
    The memory footprint of small, simple documents such as this list of
    podcasts represented as an OPML_ outline is not significant:

OPML_ アウトラインとして表されるポッドキャストのリストをサンプルに、シンプルなドキュメントでは、メモリ使用量は少なくて重要ではありません。

.. literalinclude:: podcasts.opml
   :language: xml

..
    To parse the file, pass an open file handle to :func:`parse()`.

ファイルを解析するには、オープンしたファイルハンドラを :func:`parse()` へ渡します。

.. include:: ElementTree_parse_opml.py
   :literal:
   :start-after: #end_pymotw_header

..
    It will read the data, parse the XML, and return an
    :class:`ElementTree` object.

これはデータを読み込み、XML を解析して、 :class:`ElementTree` オブジェクトを返します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ElementTree_parse_opml.py'))
.. }}}
.. {{{end}}}

..
    Traversing the Parsed Tree
    ==========================

解析されたツリーを横断する
==========================

..
    To visit all of the children in order, use :func:`iter` to create a
    generator that iterates over the :class:`ElementTree` instance.

順番に全ての子を参照するには、 :class:`ElementTree` インスタンスを繰り返し処理するジェネレータを生成する :func:`iter` を使用してください。

.. include:: ElementTree_dump_opml.py
   :literal:
   :start-after: #end_pymotw_header

..
    This example prints the entire tree, one tag at a time.

このサンプルはツリー全体と1つのタグを一緒に表示します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ElementTree_dump_opml.py'))
.. }}}
.. {{{end}}}

..
    To print only the groups of names and feed URLs for the podcasts,
    leaving out of all of the data in the header section by iterating over
    only the ``outline`` nodes and print the *text* and *xmlUrl*
    attributes.

podcast の名前のグループとフィード URL のみを表示するには、ヘッダセクションにある全てのデータを取り除き、 ``outline`` ノードのみを対象にして *text* と *xmlUrl* 属性を表示します。

.. include:: ElementTree_show_feed_urls.py
   :literal:
   :start-after: #end_pymotw_header

..
    The ``'outline'`` argument to :func:`iter` means processing is limited
    to only nodes with the tag ``'outline'``.

:func:`iter` へ渡す ``'outline'`` という引数は、 ``'outline'`` タグをもつノードのみに処理を絞り込みます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ElementTree_show_feed_urls.py'))
.. }}}
.. {{{end}}}

..
    Finding Nodes in a Document
    ===========================

ドキュメントのノードを見つける
==============================

..
    Walking the entire tree like this searching for relevant nodes can be
    error prone.  The example above had to look at each outline node to
    determine if it was a group (nodes with only a :attr:`text` attribute)
    or podcast (with both :attr:`text` and :attr:`xmlUrl`).  To produce a
    simple list of the podcast feed URLs, without names or groups, for a
    podcast downloader application, the logic could be simplified using
    :func:`findall()` to look for nodes with more descriptive search
    characteristics.

関連するノードをこのように探してツリー全体を横断するとエラーが発生し易くなります。前節のサンプルは、それぞれの ``outline`` ノードでグループ(:attr:`text` 属性のみをもつノード)かどうかを決めるために調べなければなりませんでした。podcast のダウンローダアプリケーション向けに名前やグループをもたない podcast フィード URL のシンプルなリストを作成するには、そのロジックはもっと分かり易い検索特性でノードを探すために :func:`findall()` を使用すると簡単になります。

..
    As a first pass at converting the above example, we can construct an
    XPath_ argument to look for all outline nodes.

前節の変換サンプルの1番目の引数として、全ての ``outline`` ノードを探す XPath_ の引数を渡します。

.. include:: ElementTree_find_feeds_by_tag.py
   :literal:
   :start-after: #end_pymotw_header

..
    The logic in this version is not substantially different than the
    version using :func:`getiterator()`.  It still has to check for the
    presence of the URL, except that it does not print the group name when
    the URL is not found.

このサンプルのロジックは、本質的には :func:`getiterator()` を使用するサンプルと同じです。URL が見つからなかったときにグループ名を表示しないことを除けば、それでも URL の存在を確認する必要があります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ElementTree_find_feeds_by_tag.py'))
.. }}}
.. {{{end}}}

..
    Another version can take advantage of the fact that the outline nodes
    are only nested two levels deep.  Changing the search path to
    ``.//outline/outline`` mean the loop will process only the second
    level of outline nodes.

別のサンプルとして、 ``outline`` ノードが深さ2でネストされている構造を利用できます。検索パスを ``.//outline/outline`` に変更すると、そのループ処理が ``outline`` ノードの深さ2のレベルのみを処理します。

.. include:: ElementTree_find_feeds_by_structure.py
   :literal:
   :start-after: #end_pymotw_header

..
    All of those outline nodes nested two levels deep in the input are
    expected to have the *xmlURL* attribute refering to the podcast feed,
    so the loop can skip checking for for the attribute before using it.

入力である深さ2でネストされたこれらの全ての ``outline`` ノードは、podcast フィードを参照する *xmlURL* 属性をもっていると予想されるので、このサンプルのループ処理は *xmlURL* 属性の確認処理を省けます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ElementTree_find_feeds_by_structure.py'))
.. }}}
.. {{{end}}}

..
    This version is limited to the existing structure, though, so if the
    outline nodes are ever rearranged into a deeper tree it will stop
    working.

このサンプルは存在するデータ構造を絞り込んでいますが、もしこの ``outline`` ノードがさらに深いツリーで再配置される場合は処理が停止します。

..
    Parsed Node Attributes
    ======================

解析されたノード属性
====================

..
    The items returned by :func:`findall()` and :func:`iter()` are
    :class:`Element` objects, each representing a node in the XML parse
    tree.  Each :class:`Element` has attributes for accessing data pulled
    out of the XML.  This can be illustrated with a somewhat more
    contrived example input file, ``data.xml``:

:func:`findall()` と :func:`iter()` が返す要素は :class:`Element` オブジェクトです。XML 構文解析ツリーのノードで表されます。それぞれの :class:`Element` は、XML から引き出したデータへアクセスする属性をもちます。これはやや不自然なサンプル入力ファイル ``data.xml`` で説明できます。

.. literalinclude:: data.xml
   :language: xml
   :linenos:

..
    The "attributes" of a node are available in the :attr:`attrib`
    property, which acts like a dictionary.

ノードの "属性" はディクショナリのように動作する :attr:`attrib` プロパティを利用できます。

.. include:: ElementTree_node_attributes.py
   :literal:
   :start-after: #end_pymotw_header

..
    The node on line five of the input file has two attributes,
    :attr:`name` and :attr:`foo`.

入力ファイル ``data.xml`` の5行目のノードは2つの属性 :attr:`name` と :attr:`foo` をもちます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ElementTree_node_attributes.py'))
.. }}}
.. {{{end}}}

..
    The text content of the nodes is available, along with the "tail" text
    that comes after the end of a close tag.

ノードのテキストコンテンツは、終了タグの後ろに続く "tail" のテキストと一緒に利用できます。

.. include:: ElementTree_node_text.py
   :literal:
   :start-after: #end_pymotw_header

..
    The ``child`` node on line three contains embedded text, and the node
    on line four has text with a tail (including any whitespace).

3行目の ``child`` ノードテキストが埋め込まれています。そして、4行目のノードは(全てのスペースを含む) "tail" のテキストがあります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ElementTree_node_text.py'))
.. }}}
.. {{{end}}}

..
    XML entity references embedded in the document are conveniently
    converted to the appropriate characters before values are returned.

ドキュメントに埋め込まれた XML エンティティ参照は、便利なことに値が返される前に適切な文字に変換されます。

.. include:: ElementTree_entity_references.py
   :literal:
   :start-after: #end_pymotw_header

..
    The automatic conversion mean the implementation detail of
    representing certain characters in an XML document can be ignored.

自動変換は XML ドキュメントの特定文字を表す実装の詳細が無視されることを意味します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ElementTree_entity_references.py'))
.. }}}
.. {{{end}}}

..
    Watching Events While Parsing
    =============================

解析中にイベントを監視する
==========================

..
    The other API useful for processing XML documents is event-based.  The
    parser generates ``start`` events for opening tags and ``end`` events
    for closing tags.  Data can be extracted from the document during the
    parsing phase by iterating over the event stream, which is convenient
    if it is not necessary to manipulate the entire document afterwards
    and there is no need to hold the entire parsed document in memory.

その他の API は、XML ドキュメントをイベントベースで処理するときに便利です。パーサは、タグをオープンするために ``start`` イベントを、タグをクローズするために ``end`` イベントを生成します。データは、イベントストリームを繰り返し処理する解析フェーズでそのドキュメントから展開されます。これはその後でドキュメント全体を扱う必要がない場合に便利です。そして、解析されたドキュメント全体をメモリに保持する必要がありません。

..
    :func:`iterparse()` returns an iterable that produces tuples
    containing the name of the event and the node triggering the event.
    Events can be one of:

:func:`iterparse()` は、イベントの名前とイベントをトリガーにするノードを含むタプルを生成するイテレータを返します。イベントは次のいずれかを指定できます。

..
    ``start``
      A new tag has been encountered.  The closing angle bracket of the
      tag was processed, but not the contents.
    ``end``
      The closing angle bracket of a closing tag has been processed.  All
      of the children were already processed.
    ``start-ns``
      Start a namespace declaration.
    ``end-ns``
      End a namespace declaration.

``start``
  新しいタグが検出されます。タグの閉じ括弧は処理済みですが、コンテンツではありません。
``end``
  終了タグの閉じ括弧が処理されます。全ての子は既に処理済みです。
``start-ns``
  名前空間の定義を開始します。
``end-ns``
  名前空間の定義を終了します。

.. include:: ElementTree_show_all_events.py
   :literal:
   :start-after: #end_pymotw_header

..
    By default, only ``end`` events are generated.  To see other events,
    pass the list of desired event names to :func:`iterparse()`, as in
    this example:

デフォルトでは ``end`` イベントのみが生成されます。他のイベントを参照するには、このサンプルのように必要なイベント名のリストを :func:`iterparse()` へ渡してください。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ElementTree_show_all_events.py'))
.. }}}
.. {{{end}}}

..
    The event-style of processing is more natural for some operations,
    such as converting XML input to some other format.  This technique can
    be used to convert list of podcasts from the earlier examples from an
    XML file to a CSV file, so they can be loaded into a spreadsheet or
    database application.

イベントスタイルの処理は、XML の入力から他のフォーマットに変換するといったより自然な操作です。このテクニックは、前節のサンプルで podcast のリストを XML ファイルから CSV ファイルに変換するために使用できます。変換された CSV ファイルはスプレッドシートやデータベースアプリケーションで読み込めます。

.. include:: ElementTree_write_podcast_csv.py
   :literal:
   :start-after: #end_pymotw_header

..
    This conversion program does not need to hold the entire parsed input
    file in memory, and processing each node as it is encountered in the
    input is more efficient.

この変換プログラムは、解析された入力ファイル全体をメモリに保持する必要がありません。入力ファイルからそれぞれのノードで検出されたときに処理するので効率が良くなります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ElementTree_write_podcast_csv.py'))
.. }}}
.. {{{end}}}

..
    Creating a Custom Tree Builder
    ==============================

カスタムツリービルダーを作成する
================================

..
    A potentially more efficient means of handling parse events is to
    replace the standard tree builder behavior with a custom version.  The
    :class:`ElementTree` parser uses an :class:`XMLTreeBuilder` to process
    the XML and call methods on a target class to save the results.  The
    usual output is an :class:`ElementTree` instance created by the
    default :class:`TreeBuilder` class.  Replacing :class:`TreeBuilder`
    with another class allows it to receive the events before the
    :class:`Element` nodes are instantiated, saving that portion of the
    overhead.

構文解析のイベントを処理する潜在的にもっと効率の良い方法は、標準のツリービルダーをカスタムして置き換えることです。 :class:`ElementTree` パーサーは XML を処理するのに :class:`XMLTreeBuilder` を使用して、その結果を保存するために対象クラスのメソッドを呼び出します。通常の出力は、デフォルトの :class:`TreeBuilder` クラスが作成する :class:`ElementTree` インスタンスです。 :class:`TreeBuilder` を別のクラスに置き換えることで、オーバーヘッドを省いて、 :class:`Element` ノードがインスタンス化される前にイベントを受け取れます。

..
    The XML-to-CSV converter from the previous section can be translated
    to a tree builder.

前のセクションの XML-to-CSV コンバータはツリービルダーに変換できます。

.. include:: ElementTree_podcast_csv_treebuilder.py
   :literal:
   :start-after: #end_pymotw_header

..
    :class:`PodcastListToCSV` implements the :class:`TreeBuilder`
    protocol.  Each time a new XML tag is encountered, :func:`start()` is
    called with the tag name and attributes.  When a closing tag is seen
    :func:`end()` is called with the name.  In between, :func:`data()` is
    called when a node has content (the tree builder is expected to keep
    up with the "current" node).  When all of the input is processed,
    :func:`close()` is called.  It can return a value, which will be
    returned to the user of the :class:`XMLTreeBuilder`.

:class:`PodcastListToCSV` は :class:`TreeBuilder` プロトコルを実装します。新たな XML タグが検出されると、タグ名と属性をもつ :func:`start()` が呼び出されます。終了タグが現れるときにその名前で :func:`end()` が呼ばれます。その間、ノードがコンテンツをもつときに :func:`data()` が呼ばれます(ツリービルダーが "カレント" ノードを保持すると予想される)。全ての入力が処理されると :func:`close()` が呼ばれます。この処理は :class:`XMLTreeBuilder` のユーザへ返される値を返します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ElementTree_podcast_csv_treebuilder.py'))
.. }}}
.. {{{end}}}


..
    Parsing Strings
    ===============

文字列を解析する
================

..
    To work with smaller bits of XML text, especially string literals as
    might be embedded in the source of a program, use :func:`XML()` and
    the string containing the XML to be parsed as the only argument.

小さな XML テキスト、特にプログラムのソースに埋め込まれる可能性がある文字列リテラルを扱うには、 :func:`XML()` と1つの引数として解析される XML に含まれる文字列を使用してください。

.. include:: ElementTree_XML.py
   :literal:
   :start-after: #end_pymotw_header

..
    Notice that unlike with :func:`parse()`, the return value is an
    :class:`Element` instance instead of an :class:`ElementTree`.  An
    :class:`Element` supports the iterator protocol directly, so there is
    no need to call :func:`getiterator`.

:func:`parse()` とは違って、返り値は :class:`ElementTree` ではなく :class:`Element` インスタンスになることに注意してください。 :class:`Element` は直接イテレータプロトコルをサポートするので :func:`getiterator` を呼び出す必要はありません。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ElementTree_XML.py'))
.. }}}
.. {{{end}}}

..
    For structured XML that uses the :attr:`id` attribute to identify
    unique nodes of interest, :func:`XMLID()` is a convenient way to
    access the parse results.

目的のユニークなノードを識別する :attr:`id` 属性をもつ構造化された XML 向けに、解析結果に対してアクセスするには :func:`XMLID()` が便利な方法です。

.. include:: ElementTree_XMLID.py
   :literal:
   :start-after: #end_pymotw_header

..
    :func:`XMLID()` returns the parsed tree as an :class:`Element` object,
    along with a dictionary mapping the :attr:`id` attribute strings to
    the individual nodes in the tree.

:func:`XMLID()` は、 :class:`Element` オブジェクトとして解析されたツリーを返します。それと一緒に :attr:`id` 属性の文字列をツリーの個別ノードにマッピングするディクショナリも返します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ElementTree_XMLID.py'))
.. }}}
.. {{{end}}}


.. seealso::

   Outline Processor Markup Language, OPML_
       .. Dave Winer's OPML specification and documentation.

       Dave Winer の OPML 仕様とドキュメント

   XML Path Language, XPath_
       .. A syntax for identifying parts of an XML document.

       XML ドキュメントの一部を識別するための構文

   `XPath Support in ElementTree <http://effbot.org/zone/element-xpath.htm>`_
       .. Part of Fredrick Lundh's original documentation for ElementTree.

       Fredrick Lundh の ElementTree のオリジナルドキュメントの一部

   :mod:`csv`
       .. Read and write comma-separated-value files

       カンマ区切りのファイルを読み書きする

.. _OPML: http://www.opml.org/

.. _XPath: http://www.w3.org/TR/xpath/
