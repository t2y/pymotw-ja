..
    ===========================
    gettext -- Message Catalogs
    ===========================

=============================
gettext -- メッセージカタログ
=============================

..
    :synopsis: Message Catalogs

.. module:: gettext
    :synopsis: メッセージカタログ

..
    :Purpose: Message catalog API for internationalization.
    :Available In: 2.1.3 and later

:目的: 国際化(Internationalization)のためのメッセージカタログ API
:利用できるバージョン: 2.1.3 以上

..
    The :mod:`gettext` module provides a pure-Python implementation
    compatible with the `GNU gettext`_ library for message translation and
    catalog management.  The tools available with the Python source
    distribution enable you to extract messages from your source, build a
    message catalog containing translations, and use that message catalog
    to print an appropriate message for the user at runtime.

:mod:`gettext` モジュールは `GNU gettext`_ ライブラリ互換なメッセージ翻訳とカタログ管理のためにピュア Python の実装を提供します。Python のソースと一緒に配布可能なツールは、ソースからメッセージを展開して、翻訳を含んだメッセージカタログを構築し、実行時にそのメッセージカタログを使用してユーザへ適切なメッセージを表示します。

..
    Message catalogs can be used to provide internationalized interfaces
    for your program, showing messages in a language appropriate to the
    user.  They can also be used for other message customizations,
    including "skinning" an interface for different wrappers or partners.

メッセージカタログは、ユーザへ適切な言語のメッセージを表示するために、プログラムの国際化インタフェースを提供するために使用されます。さらに違うラッパーやパートナーのインタフェースの "スキン" を含めた、その他のカスタマイズされたメッセージを使用することもできます。

.. note::

    .. Although the standard library documentation says everything you
       need is included with Python, I found that ``pygettext.py``
       refused to extract messages wrapped in the ``ungettext`` call,
       even when I used what seemed to be the appropriate command line
       options. I ended up installing the `GNU gettext`_ tools from
       source and using ``xgettext`` instead.

    標準ライブラリドキュメントでは、必要なものは全て Python で提供されているとありますが、おそらく適切なコマンドラインオプションを使用しても ``pygettext.py`` は ``ungettext`` 呼び出しでラップされたメッセージの展開が拒否されることを私は発見しました。最終的に私は `GNU gettext`_ ツールをソースからインストールして代わりに ``xgettext`` を使用しました。

..
    Translation Workflow Overview
    =============================

翻訳ワークフロー概要
====================

..
    The process for setting up and using translations includes five steps:

設定と翻訳を使用する工程は5つの手順になります。

.. 1. Mark up literal strings in your code that contain messages to translate.

1. 翻訳したいメッセージを含むコード内のリテラル文字列をマークアップする。

   .. Start by identifying the messages within your program source that
      need to be translated, and marking the literal strings so the
      extraction program can find them.

   翻訳する必要があるプログラムソース内のメッセージを識別することで始まります。そして、展開プログラムがそういったメッセージを見つけられるようにリテラル文字列をマークします。

.. 2. Extract the messages.

2. メッセージを展開する。

   .. After you have identified the translatable strings in your program
      source, use ``xgettext`` to pull the strings out and create a
      ``.pot`` file, or translation template. The template is a text file
      with copies of all of the strings you identified and placeholders
      for their translations.

   プログラムソース内の翻訳可能な文字列を識別した後で、その翻訳可能な文字列を抜き出すために ``xgettext`` を使用して ``.pot`` ファイルか、翻訳テンプレートを作成します。そのテンプレートは全ての識別した文字列や翻訳のためのプレースフォルダのコピーとなるテキストファイルです。

.. 3. Translate the messages.

3. メッセージを翻訳する。

   .. Give a copy of the ``.pot`` file to the translator, changing the
      extension to ``.po``. The ``.po`` file is an editable source file
      used as input for the compilation step. The translator should
      update the header text in the file and provide translations for all
      of the strings.

   翻訳者へ ``.pot`` ファイルのコピーを渡して、拡張子を ``.po`` に変更します。 ``.po`` ファイルはコンパイル時の入力として使用する編集可能なソースファイルです。翻訳者はファイル内のヘッダテキストを更新して全ての文字列の翻訳を提供します。

.. 4. "Compile" the message catalog from the translation.

4. 翻訳されたファイルからメッセージカタログを "コンパイル" する。

   .. When the translator gives you back the completed ``.po`` file,
      compile the text file to the binary catalog format using
      ``msgfmt``. The binary format is used by the runtime catalog lookup
      code.

   翻訳者が全て翻訳した ``.po`` ファイルを返してきたら、 ``msgfmt`` を使用してその ``.po`` ファイルをバイナリのカタログフォーマットにコンパイルします。バイナリフォーマットは実行時のカタログ検査コードにより使用されます。

.. 5. Load and activate the appropriate message catalog at runtime.

5. 実行時に適切なメッセージカタログをアクティブ化して読み込む。

   .. The final step is to add a few lines to your application to
      configure and load the message catalog and install the translation
      function. There are a couple of ways to do that, with associated
      trade-offs, and each is covered below.

   最後の手順はアプリケーション設定のために数行追加して、メッセージカタログを読み込み、翻訳機能をインストールします。それを行うにはトレードオフの関係にある2つの方法があります。この後でそれぞれの方法を説明します。

..
    Let's go through those steps in a little more detail, starting with
    the modifications you need to make to your code.

もう少し詳細に触れながらこれらの手順を通してやってみましょう。コードに対して行う必要がある変更から始ます。

..
    Creating Message Catalogs from Source Code
    ==========================================

ソースコードからメッセージカタログを作成する
============================================

..
    :mod:`gettext` works by finding literal strings embedded in your
    program in a database of translations, and pulling out the appropriate
    translated string.  There are several variations of the functions for
    accessing the catalog, depending on whether you are working with
    Unicode strings or not.  The usual pattern is to bind the lookup
    function you want to use to the name ``_`` so that your code is not
    cluttered with lots of calls to functions with longer names.

:mod:`gettext` はプログラム内に組み込まれた翻訳データベースのリテラル文字列を見つけることにより動作します。そして、適切な翻訳文字列を抜き出します。カタログへのアクセスやユニコード文字列を扱うかどうかで複数の関数があります。通常のパターンは、長い名前で何度も関数呼び出しを行ってコードの可読性が落ちないように、使用したい検査関数を ``_`` という名前に束縛することです。

..
    The message extraction program, ``xgettext``, looks for messages
    embedded in calls to the catalog lookup functions.  It understands
    different source languages, and uses an appropriate parser for each.
    If you use aliases for the lookup functions or need to add extra
    functions, you can give ``xgettext`` the names of additional symbols
    to consider when extracting messages.

メッセージ展開プログラム ``xgettext`` はカタログ検査関数の呼び出しに組み込まれたメッセージを調べます。そのプログラムは違うソース言語を理解して、それぞれのために適切なパーサを使用します。もし検査関数のエイリアスを使用する、または拡張関数を追加する必要があるなら、メッセージを展開するときに追加のシンボル名を考慮するように ``xgettext`` へ与えることができます。

..
    Here's a simple script with a single message ready to be translated:

ここに1つのメッセージの翻訳準備が整った簡単なスクリプトがあります。

.. include:: gettext_example.py
    :literal:
    :start-after: #end_pymotw_header

..
    In this case I am using the Unicode version of the lookup function,
    ``ugettext()``.  The text ``"This message is in the script."`` is the
    message to be substituted from the catalog.  I've enabled fallback
    mode, so if we run the script without a message catalog, the in-lined
    message is printed:

このケースでは、検査関数のユニコード文字列バージョン ``ugettext()`` を使用しています。 ``"This message is in the script."`` というテキストはそのカタログから置き換えられるメッセージです。フォールバックモードを有効にしたので、メッセージカタログ無しでこのスクリプトを実行すると、インラインメッセージを表示します。

.. {{{cog
.. sh('rm -f PyMOTW/gettext/locale/en_US/LC_MESSAGES/gettext_example.mo')
.. cog.out(run_script(cog.inFile, 'gettext_example.py'))
.. }}}
.. {{{end}}}

..
    The next step is to extract the message(s) and create the ``.pot``
    file, using ``pygettext.py``.

次の手順は ``pygettext.py`` でメッセージを展開して ``.pot`` ファイルを作成します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'xgettext -d gettext_example -o gettext_example.pot gettext_example.py', interpreter=None))
.. }}}
.. {{{end}}}

..
    The output file produced looks like:

その出力ファイルは次のようになります。

.. include:: gettext_example.pot
    :literal:

..
    Message catalogs are installed into directories organized by *domain*
    and *language*.  The domain is usually a unique value like your
    application name.  In this case, I used ``gettext_example``.  The
    language value is provided by the user's environment at runtime,
    through one of the environment variables ``LANGUAGE``, ``LC_ALL``,
    ``LC_MESSAGES``, or ``LANG``, depending on their configuration and
    platform.  My language is set to ``en_US`` so that's what I'll be
    using in all of the examples below.

メッセージカタログは *ドメイン* や *言語* で構成されたディレクトリ内へインストールされます。ドメインは通常アプリケーションの名前のようなユニークな値です。このケースでは ``gettext_example`` を使用しました。言語の値は実行時にユーザ環境から、その設定やプラットホームに依存する ``LANGUAGE``, ``LC_ALL``, ``LC_MESSAGES`` または ``LANG`` といった環境変数の1つを通して提供されます。私の言語は ``en_US`` にセットされているので、この後のサンプルは全てその設定を使用します。

..
    Now that we have the template, the next step is to create the required
    directory structure and copy the template in to the right spot.  I'm
    going to use the ``locale`` directory inside the PyMOTW source tree as
    the root of my message catalog directory, but you would typically want
    to use a directory accessible system-wide.  The full path to the
    catalog input source is
    ``$localedir/$language/LC_MESSAGES/$domain.po``, and the actual
    catalog has the filename extension ``.mo``.

いまテンプレートができました。次の手順は必要なディレクトリ階層を作成して、正しい場所へテンプレートをコピーします。ここではメッセージカタログディレクトリのルートとして PyMOTW ソースツリー内部の ``locale`` ディレクトリを使用します。しかし、通常はシステム全体からアクセスできるディレクトリを使いたくなるでしょう。そのカタログの入力ソースのフルパスは ``$localedir/$language/LC_MESSAGES/$domain.po`` です。そして、実際のカタログのファイル名の拡張子は ``.mo`` です。

..
    For my configuration, I need to copy ``gettext_example.pot`` to
    ``locale/en_US/LC_MESSAGES/gettext_example.po`` and edit it to change
    the values in the header and add my alternate messages.  The result
    looks like:

私の設定では ``gettext_example.pot`` を ``locale/en_US/LC_MESSAGES/gettext_example.po`` にコピーする必要があります。そして、そのコピーしたファイルを編集してヘッダの値を変更し、置き換えるメッセージを追加します。その結果は次のようになります。

.. include:: locale/en_US/LC_MESSAGES/gettext_example.po
    :literal:

..
    The catalog is built from the ``.po`` file using ``msgformat``:

そのカタログは ``msgformat`` を使用して ``.po`` ファイルから作成されます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'cd locale/en_US/LC_MESSAGES/; msgfmt -o gettext_example.mo gettext_example.po', interpreter=None))
.. }}}
.. {{{end}}}

..
    And now when we run the script, the message from the catalog is
    printed instead of the in-line string:

さて、スクリプトを実行すると、インラインの文字列ではなくカタログからのメッセージが表示されます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'gettext_example.py'))
.. }}}
.. {{{end}}}

..
    Finding Message Catalogs at Runtime
    ===================================

実行時にメッセージカタログを見つける
====================================

..
    As described above, the *locale directory* containing the message
    catalogs is organized based on the language with catalogs named for
    the *domain* of the program.  Different operating systems define their
    own default value, but :mod:`gettext` does not know all of these
    defaults.  Iut uses a default locale directory of ``sys.prefix +
    '/share/locale'``, but most of the time it is safer for you to always
    explicitly give a ``localedir`` value than to depend on this default
    being valid.

前のセクションで説明したように、メッセージカタログを含む *ロケールディレクトリ* は、プログラムの *ドメイン* 向けに名付けられたカタログと共に言語に基づいて構成されます。オペレーティングシステムによって違う独自のデフォルト値を定義しますが、 :mod:`gettext` はそういった全てのデフォルト値が分かりません。それはデフォルトのロケールディレクトリ ``sys.prefix + '/share/locale'`` を使用しますが、ほとんどの場合、このデフォルトが有効かどうかに依存するよりも明示的に ``localedir`` の値を必ず指定する方が安全です。

..
    The language portion of the path is taken from one of several
    environment variables that can be used to configure localization
    features (``LANGUAGE``, ``LC_ALL``, ``LC_MESSAGES``, and ``LANG``).
    The first variable found to be set is used.  Multiple languages can be
    selected by separating the values with a colon (``:``).  We can
    illustrate how that works by creating a second message catalog and
    running a few experiments.

そのパスの言語の一部は地域化の機能(``LANGUAGE``, ``LC_ALL``, ``LC_MESSAGES`` や ``LANG``)を設定するために使用される複数の環境変数の1つから取得されます。最初の変数がセットされていれば、その値が使用されます。複数の言語はコロン (``:``) で区切られることにより選択できます。2番目のメッセージカタログを作成して少し実験することで、複数の言語を扱う方法を解説します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'cd locale/en_CA/LC_MESSAGES/; msgfmt -o gettext_example.mo gettext_example.po', trailing_newlines=False, interpreter=None))
.. cog.out(run_script(cog.inFile, 'gettext_find.py', include_prefix=False, trailing_newlines=False))
.. cog.out(run_script(cog.inFile, 'LANGUAGE=en_CA python gettext_find.py', interpreter=None, include_prefix=False, trailing_newlines=False))
.. cog.out(run_script(cog.inFile, 'LANGUAGE=en_CA:en_US python gettext_find.py', interpreter=None, include_prefix=False, trailing_newlines=False))
.. cog.out(run_script(cog.inFile, 'LANGUAGE=en_US:en_CA python gettext_find.py', interpreter=None, include_prefix=False))
.. }}}
.. {{{end}}}

..
    Although ``find()`` shows the complete list of catalogs, only the
    first one in the sequence is actually loaded for message lookups.

``find()`` は完全なカタログのリストを表示しますが、そのシーケンスの1番目のカタログのみが実際にメッセージを検査するために読み込まれます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'gettext_example.py', trailing_newlines=False))
.. cog.out(run_script(cog.inFile, 'LANGUAGE=en_CA python gettext_example.py', interpreter=None, include_prefix=False, trailing_newlines=False))
.. cog.out(run_script(cog.inFile, 'LANGUAGE=en_CA:en_US python gettext_example.py', interpreter=None, include_prefix=False, trailing_newlines=False))
.. cog.out(run_script(cog.inFile, 'LANGUAGE=en_US:en_CA python gettext_example.py', interpreter=None, include_prefix=False))
.. }}}
.. {{{end}}}

..
    Plural Values
    =============

複数形の値
==========

..
    While simple message substitution will handle most of your translation
    needs, :mod:`gettext` treats pluralization as a special case.
    Depending on the language, the difference between the singular and
    plural forms of a message may vary only by the ending of a single
    word, or the entire sentence structure may be different.  There may
    also be `different forms depending on the level of plurality
    <http://www.gnu.org/software/gettext/manual/gettext.html#Plural-forms>`_.
    To make managing plurals easier (and possible), there is a separate
    set of functions for asking for the plural form of a message.

単純なメッセージの置き換えが翻訳の要求の大半を扱う一方、 :mod:`gettext` は特別なケースとして複数形を扱います。言語によって、メッセージの単数形と複数形との違いは1つの単語の最後が変化するか、全体の文の構造が違うかに分かれます。さらに `複数形のレベルにより違う形 <http://www.gnu.org/software/gettext/manual/gettext.html#Plural-forms>`_ になるかもしれません。(できるだけ)簡単に複数形を管理するために、メッセージの複数形を尋ねるように分離された関数セットがあります。

.. include:: gettext_plural.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'xgettext -L Python -d gettext_plural -o gettext_plural.pot gettext_plural.py', interpreter=None))
.. }}}
.. {{{end}}}

..
    Since there are alternate forms to be translated, the replacements are
    listed in an array.  Using an array allows translations for languages
    with multiple plural forms (Polish, `for example
    <http://www.gnu.org/software/gettext/manual/gettext.html#Plural-forms>`_,
    has different forms indicating the relative quantity).

翻訳されて置き換えられるので、その置き換えられる文字列は1つの配列にリストされます。配列を使用することで、複数形による言語を翻訳ができるようになります(`例えば <http://www.gnu.org/software/gettext/manual/gettext.html#Plural-forms>`_ ポーランド語は相対量で違う形になります)。

.. include:: gettext_plural.pot
    :literal:

..
    In addition to filling in the translation strings, you will also need
    to describe the way plurals are formed so the library knows how to
    index into the array for any given count value.  The line
    ``"Plural-Forms: nplurals=INTEGER; plural=EXPRESSION;\n"`` includes
    two values to replace manually.  ``nplurals`` is an integer indicating
    the size of the array (the number of translations used) and ``plural``
    is a C language expression for converting the incoming quantity to an
    index in the array when looking up the translation.  The literal
    string ``n`` is replaced with the quantity passed to ``ungettext()``.

翻訳文字列を書き込んでいくことに加えて、そのライブラリは与えられた数値で配列内にインデックス化する方法を知っているので、複数形の翻訳文字列も記入する必要があります。 ``"Plural-Forms: nplurals=INTEGER; plural=EXPRESSION;\n"`` という行は手動で置き換える2つの値を含みます。 ``nplurals`` は配列のサイズを指す整数(使用される翻訳文字列の数)で、 ``plural`` はその翻訳を検査するときに配列のインデックスに対する入力値を変換するための C 言語拡張です。リテラル文字列 ``n`` は ``ungettext()`` へ渡された値で置き換えられます。

..
    For example, English includes two plural forms.  A quantity of ``0``
    is treated as plural ("0 bananas").  The Plural-Forms entry should
    look like::

例えば、英語は2つの複数形があります。 ``0`` は複数形として扱われます("0 bananas")。複数形のエントリは次のようになります。

::

    Plural-Forms: nplurals=2; plural=n != 1;

..
    The singular translation would then go in position 0, and the plural
    translation in position 1.

単数形の翻訳は0のインデックスで複数形の翻訳は1のインデックスになります。

.. include:: locale/en_US/LC_MESSAGES/gettext_plural.po
    :literal:

..
    If we run the test script a few times after the catalog is compiled,
    you can see how different values of N are converted to indexes for the
    translation strings.

そのカタログをコンパイルした後で数回テストスクリプトを実行すると、N の値の違いで翻訳文字列のインデックスに対して変換されることが分かります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'cd locale/en_US/LC_MESSAGES/; msgfmt -o gettext_plural.mo gettext_plural.po', trailing_newlines=False, interpreter=None))
.. cog.out(run_script(cog.inFile, 'gettext_plural.py 0', include_prefix=False, trailing_newlines=False))
.. cog.out(run_script(cog.inFile, 'gettext_plural.py 1', include_prefix=False, trailing_newlines=False))
.. cog.out(run_script(cog.inFile, 'gettext_plural.py 2', include_prefix=False))
.. }}}
.. {{{end}}}

..
    Application vs. Module Localization
    ===================================

アプリケーション対モジュールの地域化(Localization)
==================================================

..
    The scope of your translation effort defines how you install and use
    the :mod:`gettext` functions in your code.

翻訳の成果のスコープはコード内で :mod:`gettext` 関数をインストールして使用する方法を定義します。

..
    Application Localization
    ------------------------

アプリケーションの地域化(Localization)
--------------------------------------

..
    For application-wide translations, it would be acceptable to install a
    function like ``ungettext()`` globally using the ``__builtins__``
    namespace because you have control over the top-level of the
    application's code.

アプリケーション全体の翻訳のために、 ``__builtins__`` 名前空間をグローバルに使用して ``ungettext()`` のような関数をインストールするためにアクセスされます。その理由はアプリケーションのコードのトップレベルで制御するからです。

.. include:: gettext_app_builtin.py
    :literal:
    :start-after: #end_pymotw_header

..
    The ``install()`` function binds ``gettext()`` to the name ``_()`` in
    the ``__builtins__`` namespace.  It also adds ``ngettext()`` and other
    functions listed in *names*.  If *unicode* is true, the Unicode
    versions of the functions are used instead of the default ASCII
    versions.

``install()`` 関数は ``__builtins__`` 名前空間の ``_()`` という名前に ``gettext()`` を束縛します。さらに ``ngettext()`` や *names* にリストされたその他の関数も追加します。 *unicode* が True の場合、その関数のユニコード文字列バージョンがデフォルトの ASCII バージョンの代わりに使用されます。

..
    Module Localization
    -------------------

モジュールの地域化(Localization)
--------------------------------

..
    For a library, or individual module, modifying ``__builtins__`` is not
    a good idea because you don't know what conflicts you might introduce
    with an application global value.  You can import or re-bind the names
    of translation functions by hand at the top of your module.

ライブラリまたは個別のモジュールのために ``__builtins__`` を変更することは良い考えではありません。その理由は何が競合してアプリケーションのグローバルな値を生成するか分からないからです。モジュールの上部で手動で翻訳関数の名前を再束縛するか、インポートすることができます。

.. include:: gettext_module_global.py
    :literal:
    :start-after: #end_pymotw_header


.. seealso::

    `gettext <http://docs.python.org/library/gettext.html>`_
        .. The standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント

    :mod:`locale`
        .. Other localization tools.

        他の国際化ツール

    `GNU gettext`_
        .. The message catalog formats, API, etc. for this module are all
           based on the original gettext package from GNU.  The catalog
           file formats are compatible, and the command line scripts have
           similar options (if not identical).  The `GNU gettext manual
           <http://www.gnu.org/software/gettext/manual/gettext.html>`_
           has a detailed description of the file formats and describes
           GNU versions of the tools for working with them.

        メッセージカタログフォーマット、API 等があります。このモジュールの全ては GNU のオリジナル gettext パッケージに基づいています。カタログファイルフォーマットは互換性があり、コマンドラインスクリプトも(全く同じでない場合は)よく似たオプションを持ちます。 `GNU gettext マニュアル <http://www.gnu.org/software/gettext/manual/gettext.html>`_ にファイルフォーマットの詳細とカタログファイルを扱う GNU ツールの説明があります。

    `Internationalizing Python <http://www.python.org/workshops/1997-10/proceedings/loewis.html>`_
        .. A paper by Martin von Löwis about techniques for
           internationalization of Python applications.

        Martin von Löwis が Python アプリケーションの国際化のテクニックについて書いた論文です。

    `Django Internationalization <http://docs.djangoproject.com/en/dev/topics/i18n/>`_
        .. Another good source of information on using gettext, including
           real-life examples.

        実際のアプリケーションで gettext を使用するときの良い情報源です。

.. _GNU gettext: http://www.gnu.org/software/gettext/
