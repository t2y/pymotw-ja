..
    =============================================
    xml.etree.ElementTree -- XML Manipulation API
    =============================================

=====================================
xml.etree.ElementTree -- XML 操作 API
=====================================

..
    :synopsis: XML Manipulation API

.. module:: xml.etree.ElementTree
    :synopsis: XML 操作 API

..
    :Purpose: Generate and parse XML documents
    :Python Version: 2.5 and later

:目的: XML ドキュメントの生成と解析
:Python バージョン: 2.5 以上

..
    The ElementTree library was contributed to the standard library by
    Fredrick Lundh.  It includes tools for parsing XML using event-based
    and document-based APIs, searching parsed documents with XPath
    expressions, and creating new or modifying existing documents.

ElementTree ライブラリは、Fredrick Lundh によって標準ライブラリに寄贈されました。このライブラリは、イベントやドキュメントベースの API で XML を解析する、XPath 式でドキュメントを検索する、新たなドキュメントを作成したり既存のドキュメントを変更したするといったツールを提供します。

.. note::

  .. All of the examples in this section use the Python implementation of
     ElementTree for simplicity, but there is also a C implementation in
     :mod:`xml.etree.cElementTree`.

  この記事の全てのサンプルは、シンプルさ故に ElementTree の Python 実装を使用しますが、 :mod:`xml.etree.cElementTree` の C 実装もあります。

.. toctree::

   parse
   create


.. seealso::

    `xml.etree.ElementTree <http://docs.python.org/library/xml.etree.elementtree.html>`_
        .. The standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント

    `ElementTree Overview <http://effbot.org/zone/element-index.htm>`_
        .. Fredrick Lundh's original documentation and links to the
           development versions of the ElementTree library.

        Fredrick Lundh の ElementTree ライブラリ開発バージョンのオリジナルのドキュメント


    `Process XML in Python with ElementTree <http://www.ibm.com/developerworks/library/x-matters28/>`_
        .. IBM DeveloperWorks article by David Mertz.

        David Mertz の IBM DeveloperWorks の記事

    `lxml.etree <http://codespeak.net/lxml/>`_
        .. A separate implementation of the ElementTree API based on libxml2 with more complete XPath support.

        もっと複雑な XPath をサポートした libxml2 ベースの ElementTree API の他の実装
