..
    =================================================
    readline -- Interface to the GNU readline library
    =================================================

===================================================
readline -- GNU readline ライブラリのインタフェース
===================================================

..
    :synopsis: Interface to the GNU readline library

.. module:: readline
    :synopsis: GNU readline ライブラリのインタフェース

..
    :Purpose: Provides an interface to the GNU readline library for interacting with the user at a command prompt.
    :Available In: 1.4 and later

:目的: コマンドプロンプトでユーザと対話的にやり取りするための GNU readline ライブラリのインタフェースを提供する
:利用できるバージョン: 1.4 以上

..
    The :mod:`readline` module can be used to enhance interactive command
    line programs to make them easier to use.  It is primarily used to
    provide command line text completion, or "tab completion".

:mod:`readline` モジュールは、簡単に対話的なコマンドラインプログラムを拡張するために使用できます。主にコマンドラインのテキスト補完、または "タブ補完" に使用されます。

.. note::

    .. Because :mod:`readline` interacts with the console content,
       printing debug messages makes it difficult to see what it
       happening in the sample code versus what readline is doing for
       free.  The examples below use the :mod:`logging` module to write
       debug information to a separate file.  The log output is shown
       with each example.

    :mod:`readline` はコンソールコンテンツを対話的にやり取りするので、デバッグメッセージを表示すると readline が普通に動作しているのと比べて、サンプルコードで何が起こっているかが分かり難くなります。次のサンプルでは、デバッグ情報を別ファイルへ書き込むのに :mod:`logging` を使用します。ログ出力はサンプルごとに表示します。

..
    Configuring
    ===========

設定
====

..
    There are two ways to configure the underlying readline library, using
    a configuration file or the ``parse_and_bind()`` function.
    Configuration options include the keybinding to invoke completion,
    editing modes (vi or emacs), and many other values.  Refer to the `GNU
    readline library documentation
    <http://tiswww.case.edu/php/chet/readline/readline.html#SEC10>`_ for
    details.

readline ライブラリを有効にする設定方法は、設定ファイルか :func:`parse_and_bind()` 関数を使用するかの2通りあります。設定オプションは、補完処理を実行するキーバインド、編集モード(vi や emacs)、他にも多くのオプションがあります。詳細は `GNU readline ライブラリドキュメント <http://tiswww.case.edu/php/chet/readline/readline.html#SEC10>`_ を参照してください。

..
    The easiest way to enable tab-completion is through a call to
    ``parse_and_bind()``.  Other options can be set at the same time.
    This example changes the editing controls to use "vi" mode instead of
    the default of "emacs".  To edit the current input line, press ``ESC``
    then use normal vi navigation keys such as ``j``, ``k``, ``l``, and
    ``h``.

タブ補完を有効にする最も簡単な方法は、 :func:`parse_and_bind()` を呼び出すことです。その他のオプションも同時に設定できます。このサンプルは、編集制御をデフォルトの "emacs" ではなく "vi" モードに変更します。カレントの入力行を編集するには、 ``ESC`` を押してから ``j``, ``k``, ``l``, ``h`` といった通常の vi ナビゲーションキーを使用します。

.. include:: readline_parse_and_bind.py
    :literal:
    :start-after: #end_pymotw_header

..
    The same configuration can be stored as instructions in a file read by
    the library with a single call.  If ``myreadline.rc`` contains:

同じ設定は、ライブラリが1回の呼び出しでファイルを読み込んで設定できます。もし ``myreadline.rc`` が、

.. include:: myreadline.rc
    :literal:

..
    the file can be read with ``read_init_file()``:

を含む場合、 :func:`read_init_file()` で読み込みます。

.. include:: readline_read_init_file.py
    :literal:
    :start-after: #end_pymotw_header

..
    Completing Text
    ===============

テキストを補完する
==================

..
    As an example of how to build command line completion, we can look at
    a program that has a built-in set of possible commands and uses
    tab-completion when the user is entering instructions.

コマンドライン補完を構築する方法の1つとして、あるプログラムの実行可能な組み込みのコマンドセットを調べられます。ユーザーがその命令を入力するとタブ補完を使用します。

.. include:: readline_completer.py
    :literal:
    :start-after: #end_pymotw_header

..
    The ``input_loop()`` function simply reads one line after another
    until the input value is ``"stop"``.  A more sophisticated program
    could actually parse the input line and run the command.

:func:`input_loop()` 関数は、入力された値が ``"stop"`` になるまで単純に一行読み込みます。より洗練されたプログラムは、実際に入力行を解析してコマンドを実行します。

..
    The ``SimpleCompleter`` class keeps a list of "options" that are
    candidates for auto-completion.  The ``complete()`` method for an
    instance is designed to be registered with :mod:`readline` as the
    source of completions.  The arguments are a "text" string to complete
    and a "state" value, indicating how many times the function has been
    called with the same text.  The function is called repeatedly with the
    state incremented each time.  It should return a string if there is a
    candidate for that state value or ``None`` if there are no more
    candidates.  The implementation of ``complete()`` here looks for a set
    of matches when state is ``0``, and then returns all of the candidate
    matches one at a time on subsequent calls.

``SimpleCompleter`` クラスは、自動補完の候補となる "options" のリストを保持します。インスタンスの :func:`complete()` メソッドは、補完ソースとして :mod:`readline` に登録されるように設計されています。その引数は、補完する "text" 文字列と、同じテキストで何回 :func:`complete()` が呼び出されたかを示す "state" の値です。この関数は呼び出される毎に "state" を追加します。"state" の値の候補がある場合は文字列を、候補がない場合は ``None`` を返します。この :func:`complete()` の実装は、"state" が ``0`` のときの ``matches`` を調べてから、その後の処理でマッチする全ての候補を返します。

..
    When run, the initial output looks something like this:

実行すると、最初の出力は次のようになります。

::

    $ python readline_completer.py 
    Prompt ("stop" to quit): 

..
    If you press ``TAB`` twice, a list of options are printed.

``TAB`` を2回押すと、オプションのリストが表示されます。

::

    $ python readline_completer.py 
    Prompt ("stop" to quit): 
    list   print  start  stop
    Prompt ("stop" to quit): 

..
    The log file shows that ``complete()`` was called with two separate
    sequences of state values.

ログファイルには、 :func:`complete()` が state 値をもつ2つの別々のシーケンスで呼び出されたことが出力されます。

::

    $ tail -f /tmp/completer.log
    DEBUG:root:(empty input) matches: ['list', 'print', 'start', 'stop']
    DEBUG:root:complete('', 0) => 'list'
    DEBUG:root:complete('', 1) => 'print'
    DEBUG:root:complete('', 2) => 'start'
    DEBUG:root:complete('', 3) => 'stop'
    DEBUG:root:complete('', 4) => None
    DEBUG:root:(empty input) matches: ['list', 'print', 'start', 'stop']
    DEBUG:root:complete('', 0) => 'list'
    DEBUG:root:complete('', 1) => 'print'
    DEBUG:root:complete('', 2) => 'start'
    DEBUG:root:complete('', 3) => 'stop'
    DEBUG:root:complete('', 4) => None

..
    The first sequence is from the first TAB key-press.  The completion
    algorithm asks for all candidates but does not expand the empty input
    line.  Then on the second TAB, the list of candidates is recalculated
    so it can be printed for the user.

1回目の TAB キー入力で最初のシーケンスが出力されます。この補完アルゴリズムは、全ての候補を問い合わせますが、空の入力行は展開しません。それから2回目の TAB で、候補のリストが再計算されてユーザへ表示されます。

..
    If next we type "``l``" and press TAB again, the screen shows:

もし次に "``l``" を入力して TAB を再入力すると、画面は次のようになります。

::

    Prompt ("stop" to quit): list

..
    and the log reflects the different arguments to ``complete()``:

ログには ``complete()`` へ別の引数が出力されます。

::

    DEBUG:root:'l' matches: ['list']
    DEBUG:root:complete('l', 0) => 'list'
    DEBUG:root:complete('l', 1) => None

..
    Pressing RETURN now causes ``raw_input()`` to return the value, and
    the ``while`` loop cycles.

RETURN キーを押すと、 :func:`raw_input()` で入力した値を返して ``while`` ループ処理が繰り返されます。

::

    Dispatch list
    Prompt ("stop" to quit):

..
    There are two possible completions for a command beginning with
    "``s``".  Typing "``s``", then pressing TAB finds that "``start``" and
    "``stop``" are candidates, but only partially completes the text on
    the screen by adding a "``t``".

"``s``" で始まるコマンドの補完候補が2つあります。"``s``" を入力した後で TAB キーを押すと、 "``start``" と "``stop``" が候補として見つかりますが、画面上では "``t``" のみを追加してテキスト補完が完了します。

..
    The log file shows:

ログファイルには次のように出力されます。

::

    DEBUG:root:'s' matches: ['start', 'stop']
    DEBUG:root:complete('s', 0) => 'start'
    DEBUG:root:complete('s', 1) => 'stop'
    DEBUG:root:complete('s', 2) => None

..
    and the screen:

そして、画面は次のように出力されます。

::

    Prompt ("stop" to quit): st


.. warning::

    .. If your completer function raises an exception, it is ignored
       silently and :mod:`readline` assumes there are no matching
       completions.

    補完関数が例外を発生させる場合、 :mod:`readline` は補完対象がなかったと仮定してその例外を無視します。

..
    Accessing the Completion Buffer
    ===============================

補完バッファへアクセスする
==========================

..
    The completion algorithm above is simplistic because it only looks the
    text argument passed to the function, but does not use any more of
    readline's internal state.  It is also possible to use :mod:`readline`
    functions to manipulate the text of the input buffer.

前節の補完アルゴリズムは単純なもので、関数に渡されたテキスト引数を調べるのみですが、readline 内部の状態を特に使用しません。入力バッファのテキストを扱うために :mod:`readline` の関数も使用できます。

.. include:: readline_buffer.py
    :literal:
    :start-after: #end_pymotw_header

..
    In this example, commands with sub-options are are being completed.
    The ``complete()`` method needs to look at the position of the
    completion within the input buffer to determine whether it is part of
    the first word or a later word.  If the target is the first word, the
    keys of the options dictionary are used as candidates.  If it is not
    the first word, then the first word is used to find candidates from
    the options dictionary.

このサンプルでは、サブオプションをもつコマンドが補完されます。 :func:`complete()` メソッドは、最初の単語、または後続の単語の一部かどうかを判断するために入力バッファ内の補完位置を探す必要があります。その対象が最初の単語なら、 ``options`` ディクショナリのキーが候補として使用されます。もし最初の単語はない場合、その後でその単語が ``options`` ディクショナリから候補を見つけるのに使用されます。

..
    There are three top-level commands, two of which have subcommands:

2つのサブコマンドをもつ3つのトップレベルのコマンドがあります。

- list

  - files
  - directories

- print

  - byname
  - bysize

- stop

..
    Following the same sequence of actions as before, pressing TAB twice
    gives us the three top-level commands:

前節同様に同じシーケンスで、TAB キーを押すと3つのトップレベルのコマンドが表示されます。

::

    $ python readline_buffer.py 
    Prompt ("stop" to quit): 
    list   print  stop   
    Prompt ("stop" to quit):

..
    and in the log:

ログです。

::

    DEBUG:root:origline=''
    DEBUG:root:begin=0
    DEBUG:root:end=0
    DEBUG:root:being_completed=
    DEBUG:root:words=[]
    DEBUG:root:complete('', 0) => list
    DEBUG:root:complete('', 1) => print
    DEBUG:root:complete('', 2) => stop
    DEBUG:root:complete('', 3) => None
    DEBUG:root:origline=''
    DEBUG:root:begin=0
    DEBUG:root:end=0
    DEBUG:root:being_completed=
    DEBUG:root:words=[]
    DEBUG:root:complete('', 0) => list
    DEBUG:root:complete('', 1) => print
    DEBUG:root:complete('', 2) => stop
    DEBUG:root:complete('', 3) => None

..
    If the first word is ``"list "`` (with a space after the word), the
    candidates for completion are different:

最初の単語が ``"list "`` (単語の後ろにスペース) なら、その補完候補が違います。

::

    Prompt ("stop" to quit): list 
    directories  files

..
    The log shows that the text being completed is *not* the full line,
    but the portion after

ログには、テキスト ``being_completed`` は全行では *ありません* が、その一部は後にあります。

::

    DEBUG:root:origline='list '
    DEBUG:root:begin=5
    DEBUG:root:end=5
    DEBUG:root:being_completed=
    DEBUG:root:words=['list']
    DEBUG:root:candidates=['files', 'directories']
    DEBUG:root:complete('', 0) => files
    DEBUG:root:complete('', 1) => directories
    DEBUG:root:complete('', 2) => None
    DEBUG:root:origline='list '
    DEBUG:root:begin=5
    DEBUG:root:end=5
    DEBUG:root:being_completed=
    DEBUG:root:words=['list']
    DEBUG:root:candidates=['files', 'directories']
    DEBUG:root:complete('', 0) => files
    DEBUG:root:complete('', 1) => directories
    DEBUG:root:complete('', 2) => None

..
    Input History
    =============

入力履歴
========

..
    :mod:`readline` tracks the input history automatically.  There are two
    different sets of functions for working with the history.  The history
    for the current session can be accessed with
    ``get_current_history_length()`` and ``get_history_item()``.  That
    same history can be saved to a file to be reloaded later using
    ``write_history_file()`` and ``read_history_file()``.  By default the
    entire history is saved but the maximum length of the file can be set
    with ``set_history_length()``.  A length of -1 means no limit.

:mod:`readline` は自動的に入力履歴を記録します。履歴を扱う2つの関数セットがあります。カレントセッションの履歴は :func:`get_current_history_length()` と :func:`get_history_item()` でアクセスできます。それと同じ履歴は :func:`write_history_file()` と :func:`read_history_file()` で、後からも再読み込みできるファイルに保存できます。デフォルトでは、全ての履歴がファイルに保存されますが、ファイルの最大長は :func:`set_history_length()` でセットできます。 ``-1`` の長さを指定すると無制限になります。

.. include:: readline_history.py
    :literal:
    :start-after: #end_pymotw_header

..
    The **HistoryCompleter** remembers everything you type and uses those
    values when completing subsequent inputs.

**HistoryCompleter** は全ての入力を覚えていて、その後で入力を補完するときにそういった値を使用します。

::

    $ python readline_history.py 
    Max history file length: -1
    Startup history: []
    Prompt ("stop" to quit): foo
    Adding "foo" to the history
    Prompt ("stop" to quit): bar
    Adding "bar" to the history
    Prompt ("stop" to quit): blah
    Adding "blah" to the history
    Prompt ("stop" to quit): b
    bar   blah  
    Prompt ("stop" to quit): b
    Prompt ("stop" to quit): stop
    Final history: ['foo', 'bar', 'blah', 'stop']

..
    The log shows this output when the "``b``" is followed by two TABs.

"``b``" に続けて TAB 2回を入力するとき、ログは次のように出力されます。

::

    DEBUG:root:history: ['foo', 'bar', 'blah']
    DEBUG:root:matches: ['bar', 'blah']
    DEBUG:root:complete('b', 0) => 'bar'
    DEBUG:root:complete('b', 1) => 'blah'
    DEBUG:root:complete('b', 2) => None
    DEBUG:root:history: ['foo', 'bar', 'blah']
    DEBUG:root:matches: ['bar', 'blah']
    DEBUG:root:complete('b', 0) => 'bar'
    DEBUG:root:complete('b', 1) => 'blah'
    DEBUG:root:complete('b', 2) => None

..
    When the script is run the second time, all of the history is read
    from the file.

このスクリプトが2回目に実行されるとき、そのファイルから全ての履歴が読み込まれます。

::

    $ python readline_history.py 
    Max history file length: -1
    Startup history: ['foo', 'bar', 'blah', 'stop']
    Prompt ("stop" to quit): 

..
    There are functions for removing individual history items and clearing
    the entire history, as well.

同様に個々の履歴を削除したり、履歴を完全に消去する関数もあります。

..
    Hooks
    =====

フック
======

..
    There are several hooks available for triggering actions as part of
    the interaction sequence.  The *startup* hook is invoked immediately
    before printing the prompt, and the *pre-input* hook is run after the
    prompt, but before reading text from the user.

対話的シーケンスの一部としてのアクションをトリガーするのに利用できるフックがあります。 *startup* フックは、プロンプトを表示する直前に呼び出されます。 *pre-input* フックは、プロンプトを実行した後でユーザーからのテキスト入力の前に実行されます。

.. include:: readline_hooks.py
    :literal:
    :start-after: #end_pymotw_header

..
    Either hook is a potentially good place to use ``insert_text()`` to
    modify the input buffer.

どちらのフックも入力バッファを変更するために :func:`insert_text()` を使用するため潜在的に便利な位置です。

::

    $ python readline_hooks.py 
    Prompt ("stop" to quit): from startup_hook from pre_input_hook

..
    If the buffer is modified inside the pre-input hook, you need to call
    ``redisplay()`` to update the screen.

もしこのバッファが *pre-input* フック内部で変更されるなら、画面を更新するために :func:`redisplay()` を呼び出す必要があります。

.. seealso::

    `readline <http://docs.python.org/library/readline.html>`_
        .. The standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント

    `GNU readline <http://tiswww.case.edu/php/chet/readline/readline.html>`_
        .. Documentation for the GNU readline library.

        GNU readline ライブラリのドキュメント
        
    `readline init file format <http://tiswww.case.edu/php/chet/readline/readline.html#SEC10>`_
        .. The initialization and configuration file format.

        初期化と設定ファイルフォーマット
    
    `effbot: The readline module <http://sandbox.effbot.org/librarybook/readline.htm>`_
        .. Effbot's guide to the readline module.

        Effbot による readline モジュールのガイド

    `pyreadline <https://launchpad.net/pyreadline>`_
        .. pyreadline, developed as a Python-based replacement for readline to be
           used in `iPython <http://ipython.scipy.org/>`_.

        pyreadline は `iPython <http://ipython.scipy.org/>`_ で使用されていて readline に置き換わる Python ベースのライブラリとして開発されている

    :mod:`cmd`
        .. The :mod:`cmd` module uses :mod:`readline` extensively to implement  
           tab-completion in the command interface.  Some of the examples here
           were adapted from the code in :mod:`cmd`.

        :mod:`cmd` モジュールは、コマンドラインインタフェースでタブ補完を実装するために :mod:`readline` を広範囲で使用します。この記事のサンプルは :mod:`cmd` から編集しました。

    :mod:`rlcompleter`
        .. :mod:`rlcompleter` uses :mod:`readline` to add tab-completion to the interactive 
           Python interpreter.

        :mod:`rlcompleter` は Python インタープリタと対話的にタブ補完を追加するために :mod:`readline` を使用します。
