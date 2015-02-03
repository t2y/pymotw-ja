.. _xml.etree.ElementTree.creating:

============================
 XML ドキュメントを作成する
============================

..
    ========================
     Creating XML Documents
    ========================

..
    In addition to its parsing capabilities, :mod:`xml.etree.ElementTree`
    also supports creating well-formed XML documents from :class:`Element`
    objects constructed in an application.  The :class:`Element` class
    used when a document is parsed also knows how to generate a serialized
    form of its contents, which can then be written to a file or other
    data stream.

XML の構文解析に加えて、 :mod:`xml.etree.ElementTree` はアプリケーションで組み立てた :class:`Element` オブジェクトから一般的な XML ドキュメントを作成する機能も提供します。ドキュメントを解析するときに使用した :class:`Element` クラスは、そのコンテンツのシリアライズされたフォームの作成方法も知っていて、ファイルまたは他のデータストリームへ書き込みできます。

..
    Building Element Nodes
    ======================

要素のノードを組み立てる
========================

..
    There are three helper functions useful for creating a hierarchy of
    :class:`Element` nodes.  :func:`Element()` creates a standard node,
    :func:`SubElement()` attaches a new node to a parent, and
    :func:`Comment()` creates a node that serializes using XML's comment
    syntax.

:class:`Element` ノードの階層構造を作成するのに便利なヘルパー関数が3つあります。 :func:`Element()` は標準的なノードを作成します。 :func:`SubElement()` は親に新たなノードを追加します。 :func:`Comment()` は XML のコメント構文を使用してシリアライズするノードを作成します。

.. include:: ElementTree_create.py
   :literal:
   :start-after: #end_pymotw_header

..
    The output contains only the XML nodes in the tree, not the XML declaration
    with version and encoding.

この出力はツリーの XML ノードのみを含み、バージョンとエンコーディングをもつ XML の定義ではありません。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ElementTree_create.py', break_lines_at=68))
.. }}}

::

	$ python ElementTree_create.py
	
	<top><!--Generated for PyMOTW--><child>This child contains text.</ch
	ild><child_with_tail>This child has regular text.</child_with_tail>A
	nd "tail" text.<child_with_entity_ref>This &amp; that</child_with_en
	tity_ref></top>

.. {{{end}}}

..
    The ``&`` character in the text of ``child_with_entity_ref`` is
    converted to the entity reference ``&amp;`` automatically.

``child_with_entity_ref`` テキストの ``&`` という文字は、自動的に ``&amp;`` というエンティティ参照に変換されます。

..
    Pretty-Printing XML
    ===================

人が読み易い XML
================

..
    :class:`ElementTree` makes no effort to "pretty print" the output
    produced by :func:`tostring()`, since adding extra whitespace changes
    the contents of the document.  To make the output easier to follow for
    human readers, the rest of the examples below will use `a tip I found
    online
    <http://renesd.blogspot.com/2007/05/pretty-print-xml-with-python.html>`_
    and re-parse the XML with :mod:`xml.dom.minidom` then use its
    :func:`toprettyxml()` method.

:class:`ElementTree` は、余分なスペースを追加することでドキュメントのコンテンツを変更するので、 :func:`tostring()` が生成する出力を "pretty print" する機能がありません。人が読み易い出力を作成するには、 `私がインターネット上で見つけた tip <http://renesd.blogspot.com/2007/05/pretty-print-xml-with-python.html>`_ と :mod:`xml.dom.minidom` で XML を再解析した後で :func:`toprettyxml()` メソッドを使用します。

.. include:: ElementTree_pretty.py
   :literal:
   :start-after: #end_pymotw_header

..
    The updated example now looks like:

変更したサンプルは次のようになります。

.. include:: ElementTree_create_pretty.py
   :literal:
   :start-after: #end_pymotw_header

..
    and the output is easier to read:

この出力は以前の出力よりも読み易くなっています。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ElementTree_create_pretty.py'))
.. }}}

::

	$ python ElementTree_create_pretty.py
	
	<?xml version="1.0" ?>
	<top>
	  <!--Generated for PyMOTW-->
	  <child>
	    This child contains text.
	  </child>
	  <child_with_tail>
	    This child has regular text.
	  </child_with_tail>
	  And &quot;tail&quot; text.
	  <child_with_entity_ref>
	    This &amp; that
	  </child_with_entity_ref>
	</top>
	

.. {{{end}}}

..
    In addition to the extra whitespace for formatting, the
    :mod:`xml.dom.minidom` pretty-printer also adds an XML declaration to
    the output.

:mod:`xml.dom.minidom` の pretty-printer は、フォーマット時に余分なスペースに加えて XML 定義もこの出力に追加します。

..
    Setting Element Properties
    ==========================

要素のプロパティを設定する
==========================

..
    The previous example created nodes with tags and text content, but did
    not set any attributes of the nodes.  Many of the examples from
    :ref:`xml.etree.ElementTree.parsing` worked with an OPML_ file listing
    podcasts and their feeds.  The ``outline`` nodes in the tree used
    attributes for the group names and podcast properties.
    :class:`ElementTree` can be used to construct a similar XML file from
    a CSV input file, setting all of the element attributes as the tree is
    constructed.

前節のサンプルはタグとテキストのコンテンツをもつノードを作成しましたが、ノードへ任意の属性を設定しませんでした。 :ref:`xml.etree.ElementTree.parsing` にあるサンプルの多くは、podcast を表示する OPML_ ファイルとそのフィードを処理します。ツリーの ``outline`` ノードは、グループ名と podcast のプロパティの属性に使用されます。 :class:`ElementTree` は、CSV ファイルから同様の XML ファイルを組み立てられます。それはツリーを構築するときに全ての要素の属性を設定します。

.. include:: ElementTree_csv_to_xml.py
   :literal:
   :start-after: #end_pymotw_header

..
    The attribute values can be configured one at a time with
    :func:`set()` (as with the ``root`` node), or all at once by passing a
    dictionary to the node factory (as with each group and podcast node).

属性値は (``root`` ノードのように) :func:`set()` で1つずつか、(それぞれのグループと podcast ノードのように)ノードファクトリへディクショナリを渡すことでまとめて設定できます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ElementTree_csv_to_xml.py', break_lines_at=68))
.. }}}

::

	$ python ElementTree_csv_to_xml.py
	
	<?xml version="1.0" ?>
	<opml version="1.0">
	  <!--Generated by ElementTree_csv_to_xml.py for PyMOTW-->
	  <head>
	    <title>
	      My Podcasts
	    </title>
	    <dateCreated>
	      2013-02-21 06:38:01.494066
	    </dateCreated>
	    <dateModified>
	      2013-02-21 06:38:01.494066
	    </dateModified>
	  </head>
	  <body>
	    <outline text="Science and Tech">
	      <outline htmlUrl="http://www.publicradio.org/columns/futureten
	se/" text="APM: Future Tense" xmlUrl="http://www.publicradio.org/col
	umns/futuretense/podcast.xml"/>
	    </outline>
	    <outline text="Science and Tech">
	      <outline htmlUrl="http://www.uh.edu/engines/engines.htm" text=
	"Engines Of Our Ingenuity Podcast" xmlUrl="http://www.npr.org/rss/po
	dcast.php?id=510030"/>
	    </outline>
	    <outline text="Science and Tech">
	      <outline htmlUrl="http://www.nyas.org/WhatWeDo/SciencetheCity.
	aspx" text="Science &amp; the City" xmlUrl="http://www.nyas.org/Podc
	asts/Atom.axd"/>
	    </outline>
	    <outline text="Books and Fiction">
	      <outline htmlUrl="http://www.podiobooks.com/blog" text="Podiob
	ooker" xmlUrl="http://feeds.feedburner.com/podiobooks"/>
	    </outline>
	    <outline text="Books and Fiction">
	      <outline htmlUrl="http://web.me.com/normsherman/Site/Podcast/P
	odcast.html" text="The Drabblecast" xmlUrl="http://web.me.com/normsh
	erman/Site/Podcast/rss.xml"/>
	    </outline>
	    <outline text="Books and Fiction">
	      <outline htmlUrl="http://www.tor.com/" text="tor.com / categor
	y / tordotstories" xmlUrl="http://www.tor.com/rss/category/TorDotSto
	ries"/>
	    </outline>
	    <outline text="Computers and Programming">
	      <outline htmlUrl="http://twit.tv/mbw" text="MacBreak Weekly" x
	mlUrl="http://leo.am/podcasts/mbw"/>
	    </outline>
	    <outline text="Computers and Programming">
	      <outline htmlUrl="http://twit.tv" text="FLOSS Weekly" xmlUrl="
	http://leo.am/podcasts/floss"/>
	    </outline>
	    <outline text="Computers and Programming">
	      <outline htmlUrl="http://www.coreint.org/" text="Core Intuitio
	n" xmlUrl="http://www.coreint.org/podcast.xml"/>
	    </outline>
	    <outline text="Python">
	      <outline htmlUrl="http://advocacy.python.org/podcasts/" text="
	PyCon Podcast" xmlUrl="http://advocacy.python.org/podcasts/pycon.rss
	"/>
	    </outline>
	    <outline text="Python">
	      <outline htmlUrl="http://advocacy.python.org/podcasts/" text="
	A Little Bit of Python" xmlUrl="http://advocacy.python.org/podcasts/
	littlebit.rss"/>
	    </outline>
	    <outline text="Python">
	      <outline htmlUrl="" text="Django Dose Everything Feed" xmlUrl=
	"http://djangodose.com/everything/feed/"/>
	    </outline>
	    <outline text="Miscelaneous">
	      <outline htmlUrl="http://www.castsampler.com/users/dhellmann/"
	 text="dhellmann's CastSampler Feed" xmlUrl="http://www.castsampler.
	com/cast/feed/rss/dhellmann/"/>
	    </outline>
	  </body>
	</opml>
	

.. {{{end}}}

..
    Building Trees from Lists of Nodes
    ==================================

ノードのリストからツリーを構築する
==================================

..
    Multiple children can be added to an :class:`Element` instance with
    the :func:`extend` method.  The argument to :func:`extend` is any
    iterable, including a :class:`list` or another :class:`Element`
    instance.

複数の子は :func:`extend` メソッドをもつ :class:`Element` インスタンスへ追加できます。 :func:`extend` への引数は、 :class:`list` または別の :class:`Element` インスタンスを含む任意のイテレータです。

.. include:: ElementTree_extend.py
   :literal:
   :start-after: #end_pymotw_header

..
    When a :class:`list` is given, the nodes in the list are added
    directly to the new parent.

:class:`list` が渡されたとき、そのリストにあるノードは直接的に新たな親へ追加されます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ElementTree_extend.py'))
.. }}}

::

	$ python ElementTree_extend.py
	
	<?xml version="1.0" ?>
	<top>
	  <child num="0"/>
	  <child num="1"/>
	  <child num="2"/>
	</top>
	

.. {{{end}}}

..
    When another :class:`Element` instance is given, the children of that
    node are added to the new parent.

別の :class:`Element` インスタンスが渡されたとき、そのノードの子は新たな親へ追加されます。

.. include:: ElementTree_extend_node.py
   :literal:
   :start-after: #end_pymotw_header

..
    In this case, the node with tag ``root`` created by parsing the XML
    string has three children, which are added to the ``parent`` node.
    The ``root`` node is not part of the output tree.

この場合、3つの子をもつ XML 文字列を解析することで ``root`` タグをもつノードが作成されて ``parent`` ノードに追加されます。 ``root`` ノードは、出力ツリーにはありません。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ElementTree_extend_node.py'))
.. }}}

::

	$ python ElementTree_extend_node.py
	
	<?xml version="1.0" ?>
	<top>
	  <parent>
	    <child num="0"/>
	    <child num="1"/>
	    <child num="2"/>
	  </parent>
	</top>
	

.. {{{end}}}

..
    It is important to understand that :func:`extend` does not modify any
    existing parent-child relationships with the nodes.  If the values
    passed to extend exist somewhere in the tree already, they will still
    be there, and will be repeated in the output.

:func:`extend` は全ての既存ノードの親子関係を変更しないということを理解することが重要です。その値が既にツリーにある既存の部分を拡張するために渡される場合、そこにも存在して、繰り返して出力されます。

.. include:: ElementTree_extend_node_copy.py
   :literal:
   :start-after: #end_pymotw_header

..
    Setting the :attr:`id` attribute of these children to the Python
    unique object identifier exposes the fact that the same node objects
    appear in the output tree more than once.

Python のユニークなオブジェクト識別子へそういった子の :attr:`id` 属性を設定することは、その出力に同じノードオブジェクトが複数回現れることになります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ElementTree_extend_node_copy.py'))
.. }}}

::

	$ python ElementTree_extend_node_copy.py
	
	A:
	<?xml version="1.0" ?>
	<top>
	  <parent id="A">
	    <child id="4300110224" num="0"/>
	    <child id="4300110288" num="1"/>
	    <child id="4300110480" num="2"/>
	  </parent>
	  <parent id="B"/>
	</top>
	
	
	B:
	<?xml version="1.0" ?>
	<top>
	  <parent id="A">
	    <child id="4300110224" num="0"/>
	    <child id="4300110288" num="1"/>
	    <child id="4300110480" num="2"/>
	  </parent>
	  <parent id="B">
	    <child id="4300110224" num="0"/>
	    <child id="4300110288" num="1"/>
	    <child id="4300110480" num="2"/>
	  </parent>
	</top>
	
	

.. {{{end}}}

..
    Serializing XML to a Stream
    ===========================

ストリームへ XML をシリアライズする
===================================

..
    :func:`tostring()` is implemented to write to an in-memory file-like
    object and then return a string representing the entire element tree.
    When working with large amounts of data, it will take less memory and
    make more efficient use of the I/O libraries to write directly to a
    file handle using the :func:`write()` method of :class:`ElementTree`.

:func:`tostring()` は、ファイルのようなインメモリオブジェクトに書き込み、要素ツリー全体を表す文字列を返すように実装されています。巨大なデータを処理するときは、メモリの消費を少なくして、 :class:`ElementTree` の :func:`write()` メソッドでファイルハンドラへ直接書き込むために I/O ライブラリを効率良く使用します。

.. include:: ElementTree_write.py
   :literal:
   :start-after: #end_pymotw_header

..
    The example uses :ref:`sys.stdout <sys-input-output>` to write to the
    console, but it could also write to an open file or socket.

このサンプルは、コンソールへ書き込むために :ref:`sys.stdout <sys-input-output>` を使用しますが、オープンされたファイルまたはソケットにも書き込めます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ElementTree_write.py', break_lines_at=68))
.. }}}

::

	$ python ElementTree_write.py
	
	<top><!--Generated for PyMOTW--><child>This child contains text.</ch
	ild><child_with_tail>This child has regular text.</child_with_tail>A
	nd "tail" text.<child_with_entity_ref>This &amp; that</child_with_en
	tity_ref><empty_child /></top>

.. {{{end}}}

..
    The last node in the tree contains no text or sub-nodes, so it is
    written as an empty tag, ``<empty_child />``.  :func:`write` takes a
    *method* argument to control the handling for empty nodes.  

ツリーの最後のノードは、テキストまたはサブノードを含まないので、空のタグ ``<empty_child />`` として書き込まれます。 :func:`write` は、空のノード処理を制御するために *method* 引数を受け取ります。

.. include:: ElementTree_write_method.py
   :literal:
   :start-after: #end_pymotw_header

..
    Three methods are supported:

3つのメソッドがサポートされています。

..
    ``xml``
      The default method, produces ``<empty_child />``.
    ``html``
      Produce the tag pair, as is required in HTML documents
      (``<empty_child></empty_child>``).
    ``text``
      Prints only the text of nodes, and skips empty tags entirely.

``xml``
  デフォルトメソッドで ``<empty_child />`` を生成する。
``html``
  HTML で要求されるようなタグのペアを生成する(``<empty_child></empty_child>``)。
``text``
  ノードのテキストのみを表示して、空のタグを完全に読み飛ばす。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ElementTree_write_method.py'))
.. }}}

::

	$ python ElementTree_write_method.py
	
	xml
	<top><child>This child contains text.</child><empty_child /></top>
	
	html
	<top><child>This child contains text.</child><empty_child></empty_child></top>
	
	text
	This child contains text.
	

.. {{{end}}}



.. seealso::

   Outline Processor Markup Language, OPML_
       .. Dave Winer's OPML specification and documentation.

       Dave Winer の OPML 仕様とドキュメント

.. _OPML: http://www.opml.org/
