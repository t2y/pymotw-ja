..
    =================================================================
    rlcompleter -- Adds tab-completion to the interactive interpreter
    =================================================================

=================================================================
rlcompleter -- インタラクティブインタープリタへタブ補完を追加する
=================================================================

..
    :synopsis: Adds tab-completion to the interactive interpreter

.. module:: rlcompleter
    :synopsis: インタラクティブインタープリタへタブ補完を追加する

..
    :Purpose: Adds tab-completion to the interactive interpreter
    :Available In: 1.5 and later

:目的: インタラクティブインタープリタへタブ補完を追加する
:利用できるバージョン: 1.5 以上

..
    :mod:`rlcompleter` adds tab-completion for Python symbols to the
    interactive interpreter.  Importing the module causes it to configure
    a completer function for :mod:`readline`.  The only other step
    required is to configure the tab key to trigger the completer.  All of
    this can be done in a `PYTHONSTARTUP
    <http://docs.python.org/using/cmdline.html#envvar-PYTHONSTARTUP>`_
    file so that it runs each time the interactive interpreter starts.

:mod:`rlcompleter` はインタラクティブインタープリタに Python シンボルのタブ補完を追加します。そのモジュールをインポートすることで :mod:`readline` に補完関数を設定します。唯一の必要な別ステップは補完のトリガーとしてタブキーを設定することです。
インタラクティブインタープリタが起動したときに毎回実行されるように、この設定は `PYTHONSTARTUP <http://docs.python.org/using/cmdline.html#envvar-PYTHONSTARTUP>`_ ファイルで行うことができます。

..
    For example, create a file ``~/.pythonrc`` containing:

例えば ``~/.pythonrc`` ファイルを作成してそれに保存します。

.. include:: rlcompleter_pythonstartup.py
    :literal:
    :start-after: #end_pymotw_header

..
    Then set ``PYTHONSTARTUP`` to ``"~/.pythonrc"``.  When you start the
    interactive interpreter, tab completion for names from the contents of
    modules or attributes of objects is activated.

それから ``"~/.pythonrc"`` に対して ``PYTHONSTARTUP`` をセットします。インタラクティブインタープリタを起動するとき、モジュールのコンテンツからの名前やオブジェクトの属性の名前のタブ補完が有効になります。

.. seealso::

    `rlcompleter <http://docs.python.org/library/rlcompleter.html>`_
        .. The standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント

    :mod:`readline`
        .. The readline module.

        readline モジュール
