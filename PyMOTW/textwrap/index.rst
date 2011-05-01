..
    ======================================
    textwrap -- Formatting text paragraphs
    ======================================

======================================
textwrap -- 段落内のテキストを整形する
======================================

..
    :synopsis: Formatting text by adjusting where line breaks occur in a paragraph.

.. module:: textwrap
    :synopsis: 段落内のテキストの改行位置を調整して整形する

..
    :Purpose: Formatting text by adjusting where line breaks occur in a paragraph.
    :Available In: 2.5

:目的: 段落内のテキストの改行位置を調整して整形する
:利用できるバージョン: 2.5

..
    The :mod:`textwrap` module can be used to format text for output in
    situations where pretty-printing is desired. It offers programmatic
    functionality similar to the paragraph wrapping or filling features
    found in many text editors.

:mod:`textwrap` モジュールは、人間が見易いように表示したいときにテキストを整形するのに使用されます。多くのテキストエディタにある、段落内のテキストの折り返しや詰め込みといった機能がプログラミングできます。

..
    Example Data
    ============

サンプルデータ
==============

..
    The examples below use ``textwrap_example.py``, which contains a
    string ``sample_text``:

サンプルプログラムは、以下の ``textwrap_example.py`` で ``sample_text`` を使用します。

.. include:: textwrap_example.py
    :literal:
    :start-after: #end_pymotw_header

..
    Filling Paragraphs
    ==================

段落の詰め込み
==============

..
    The :func:`fill()` convenience function takes text as input and
    produces formatted text as output. Let's see what it does with the
    sample_text provided.

:func:`fill()` は便利な関数でテキストを入力として受け取り、整形されたテキストを出力します。sample_text を渡して、その整形処理がどのように行われるかを見てみましょう。

.. include:: textwrap_fill.py
    :literal:
    :start-after: #end_pymotw_header

..
    The results are something less than what we want:

実行結果は望むものとはちょっと違うようです。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'textwrap_fill.py'))
.. }}}
.. {{{end}}}


..
    Removing Existing Indentation
    =============================

既存インデントの削除
====================

..
    Notice the embedded tabs and extra spaces mixed into the middle of the
    output. It looks pretty rough. We can do better if we start by
    removing any common whitespace prefix from all of the lines in the
    sample text. This allows us to use docstrings or embedded multi-line
    strings straight from our Python code while removing the formatting of
    the code itself. The sample string has an artificial indent level
    introduced for illustrating this feature.

埋め込まれたタブと余分なスペースが実行結果の出力に混在していることに注目してください。それはあまりにも見辛いものです。サンプルテキストの全行から接頭辞のスペースを削除すればもっと良くなります。これは Python のコードそのもののフォーマットを削除する一方で、そのコードから直接的に埋め込まれた複数行の文字列や docstring が使用できます。サンプルの文字列は、この機能を分かり易く説明するためにわざわざインデントしています。

.. include:: textwrap_dedent.py
    :literal:
    :start-after: #end_pymotw_header

..
    The results are starting to look better:

実行結果はずっと見易くなります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'textwrap_dedent.py'))
.. }}}
.. {{{end}}}

..
    Since "dedent" is the opposite of "indent", the result is a block of
    text with the common initial whitespace from each line removed. If one
    line is already indented more than another, some of the whitespace
    will not be removed.

"dedent" の対義語は "indent" なので、その実行結果はテキストの段落から各行の最初にあるスペースが削除されています。ある行が他の行よりもインデントされていると、いくつかのスペースは削除されません。

::

     One tab.
     Two tabs.
    One tab.

は次のようになります。

::

    One tab.
    Two tabs.
    One tab.


..
    Combining Dedent and Fill
    =========================

インデント除去と詰め込みの組み合わせ
====================================

..
    Next, let's see what happens if we take the dedented text and pass it
    through :func:`fill()` with a few different *width* values.

次にインデントが除去されたテキストを受け取り *width* の値を変更して :func:`fill()` へ渡すとどうなるかを見てみましょう。

.. include:: textwrap_fill_width.py
    :literal:
    :start-after: #end_pymotw_header

..
    This gives several sets of output in the specified widths:

出力幅をいろいろ指定した出力は次のようになります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'textwrap_fill_width.py'))
.. }}}
.. {{{end}}}


..
    Hanging Indents
    ===============

インデントのぶら下げ
====================

..
    Besides the width of the output, you can control the indent of the
    first line independently of subsequent lines.

出力幅の他にも、最初の行に続くそれ以降の行のインデントを制御できます。

.. include:: textwrap_hanging_indent.py
    :literal:
    :start-after: #end_pymotw_header

..
    This makes it relatively easy to produce a hanging indent, where the
    first line is indented less than the other lines.

これは最初の行がその他の行よりもインデントが少ないので、比較的、インデントのぶら下げを生成し易いです。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'textwrap_hanging_indent.py'))
.. }}}
.. {{{end}}}

..
    The indent values can include non-whitespace characters, too, so the
    hanging indent can be prefixed with ``*`` to produce bullet points,
    etc. That came in handy when I converted my old zwiki content so I
    could import it into trac. I used the StructuredText package from Zope
    to parse the zwiki data, then created a formatter to produce trac's
    wiki markup as output. Using :mod:`textwrap`, I was able to format the
    output pages so almost no manual tweaking was needed after the
    conversion.

インデントの値にはスペース以外の文字も含められます。そのため、インデントのぶら下げは箇条書き等を生成するために ``*`` を接頭辞にすることもできます。それは古い zwiki の内容を変換するときにそのまま Trac へインポートできるのでかなり重宝します。私は zwiki のデータの解析に Zope の StructuredText パッケージを使用して、Trac の wiki マークアップになるようにフォーマッタを作成しました。 :mod:`textwrap` を使用すると変換後に手作業での微調整がほとんど必要なかったので、その出力ページを整形することができました。

.. seealso::

    `textwrap <http://docs.python.org/lib/module-textwrap.html>`_
        .. Standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント

    :ref:`article-text-processing`
        .. More tools for working with text.

        テキストを処理するその他のツール
