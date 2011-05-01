..
    ===================================
    cgitb -- Detailed traceback reports
    ===================================

=====================================
cgitb -- 詳細なトレースバックレポート
=====================================

..
    :synopsis: Mis-named module that provides extended traceback information.

.. module:: cgitb
    :synopsis: 拡張トレースバック情報を提供する名前がよくないモジュール

..
    :Purpose: cgitb provides more detailed traceback information than :mod:`traceback`.
    :Available In: 2.2 and later

:目的: cgitb は :mod:`traceback` よりも詳細なトレースバック情報を提供する
:利用できるバージョン: 2.2 以上

..
    :mod:`cgitb` was originally designed for showing errors and debugging
    information in web applications.  It was later updated to include
    plain-text output as well, but unfortunately wasn't renamed.  This has
    led to obscurity and the module is not used as often as it should be.
    Nonetheless, :mod:`cgitb` is a valuable debugging tool in the standard
    library.

もともと :mod:`cgitb` は、web アプリケーションのエラーとデバッグ情報の表示を目的に設計されていました。後になってプレーンテキストの出力も同様に含めるように拡張されましたが、残念ながら名前は変更されませんでした。この名前は分かり難いので、このモジュールはあまり使われていません。そうとは言え :mod:`cgitb` は標準ライブラリの優れたデバッグツールです。

..
    Standard Traceback Dumps
    ========================

標準トレースバックの出力
========================

..
    Python's default exception handling behavior is to print a *traceback*
    to standard error with the call stack leading up to the error
    position.  This basic output frequently contains enough information to
    understand the cause of the exception and permit a fix.

Python のデフォルトの例外処理の動作は、エラーが発生した箇所へ至るコールスタックと *トレースバック* を標準エラー出力に表示します。この基本的な出力は、例外が発生した原因を理解して、その不具合を修正するのに十分な情報を提供します。

.. include:: cgitb_basic_traceback.py
   :literal:
   :start-after: #end_pymotw_header

..
    The above sample program has a subtle error in :func:`func3()`.

上述したサンプルプログラムは :func:`func3()` に分かり難いエラーがあります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'cgitb_basic_traceback.py', ignore_error=True))
.. }}}
.. {{{end}}}

..
    Enabling Detailed Tracebacks
    ============================

詳細なトレースバックを有効にする
================================

..
    While the basic traceback includes enough information for us to spot
    the error, enabling cgitb replaces ``sys.excepthook`` with a function
    that gives extended tracebacks with even more detail.

標準のトレースバックはエラーが発生した箇所を見つけるのに十分な情報を提供しますが、 :mod:`cgitb` を有効にすると ``sys.excepthook`` をさらに詳細なトレースバック情報を出力するように拡張した関数に置き換えてくれます。

.. include:: cgitb_extended_traceback.py
   :literal:
   :start-after: #end_pymotw_header

..
    As you can see below, the error report is much more extensive.  Each
    frame of the stack is listed, along with:

ご覧のように、このエラーレポートはかなり広範囲に及びます。スタックの各フレームが次の内容にそって表示されます。

..
    * the full path to the source file, instead of just the base name
    * the values of the arguments to each function in the stack
    * a few lines of source context from around the line in the error path
    * the values of variables in the expression causing the error

* ファイル名だけではなく、ソースファイルのフルパスを表示する
* スタックの各関数への引数の値を表示する
* エラーパス周辺のソースコンテキストを数行表示する
* エラーを発生させた式の変数の値を表示する

.. {{{cog
.. cog.out(run_script(cog.inFile, 'cgitb_extended_traceback.py', ignore_error=True))
.. }}}
.. {{{end}}}

..
    The end of the output also includes the full details of the exception
    object (in case it has attributes other than ``message`` that would be
    useful for debugging) and the original form of a traceback dump.

この出力の最後の方に、(``message`` 以外のデバッグに役立つ属性を持つ場合は)例外オブジェクトの全ての詳細とオリジナルのトレースバック出力も含みます。

..
    Local Variables in Tracebacks
    =============================

トレースバックのローカル変数
============================

..
    Having access to the variables involved in the error stack can help
    find a logical error that occurs somewhere higher in the stack than
    the line where the actual exception is generated.

エラースタックで実行された変数へアクセスできることは、実際に例外が発生した行よりもスタックの高いところで起こる論理的なエラーを見つけるのに役立ちます。

.. include:: cgitb_local_vars.py
   :literal:
   :start-after: #end_pymotw_header

..
    In the case of this code with a :ref:`ZeroDivisionError
    <exceptions-ZeroDivisionError>`, we can see that the problem is
    introduced in the computation of the value of ``c`` in ``func1()``,
    rather than where the value is used in ``func2()``.

:ref:`ZeroDivisionError <exceptions-ZeroDivisionError>` を発生させるこのサンプルコードでは、 ``func2()`` で使用される値の計算よりも ``func1()`` で ``c`` の値の計算でこの問題が発生することが分かります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'cgitb_local_vars.py', ignore_error=True))
.. }}}
.. {{{end}}}

..
    The code in :mod:`cgitb` that examines the variables used in the stack
    frame leading to the error is smart enough to evaluate object
    attributes to display them, too.

エラーを引き起こすスタックフレームで使用される変数を調べる :mod:`cgitb` のコードは、オブジェクトの属性を評価して表示するのにも十分実用できます。

.. include:: cgitb_with_classes.py
   :literal:
   :start-after: #end_pymotw_header

..
    Here we see that ``self.a`` and ``self.b`` are involved in the
    error-prone code.

ここでは ``self.a`` と ``self.b`` が、エラーの発生し易いコードで実行されます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'cgitb_with_classes.py', ignore_error=True))
.. }}}
.. {{{end}}}



..
    Adding More Context
    ===================

もっとコンテキストを追加する
============================

..
    Suppose your function includes a lot of inline comments, whitespace,
    or other code that makes it very long.  Having the default of 5 lines
    of context may not be enough help in that case, if the body of the
    function is pushed out of the code window displayed.  Using a larger
    context value when enabling cgitb gets around this.

たくさんのコメント、スペース、余分なコードがある長い関数があると仮定してください。その場合、デフォルトで表示される5行のコンテキストだと、ウィンドウに表示されるコードから関数の主要部分が押し出されて必要な情報がないかもしれません。 :mod:`cgitb` を利用するときに *context* に大きな値をセットすると、そういった問題に対応できます。

.. include:: cgitb_more_context.py
   :literal:
   :start-after: #end_pymotw_header

..
    You can pass *context* to :func:`enable()` to control the amount of
    code displayed for each line of the traceback.

トレースバックに表示されるコード量を制御するために *context* を :func:`enable()` に渡します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'cgitb_more_context.py 5', ignore_error=True))
.. }}}
.. {{{end}}}

..
    Increasing the value gets us enough of the function that we can spot
    the problem in the code, again.

値を増やして再度実行すると、コード内の問題を見つけるのに十分な関数の情報を取得できます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'cgitb_more_context.py 10', ignore_error=True))
.. }}}
.. {{{end}}}

..
    Exception Properties
    ====================

例外プロパティ
==============

..
    In addition to the local variables from each stack frame, :mod:`cgitb`
    shows all properties of the exception object.  If you have a custom
    exception type with extra properties, they are printed as part of the
    error report.

各スタックフレームのローカル変数に加えて、 :mod:`cgitb` は例外オブジェクトの全てのプロパティを表示します。拡張プロパティをもつカスタム例外を扱う場合、それはエラーレポートの一部に表示されます。

.. include:: cgitb_exception_properties.py
   :literal:
   :start-after: #end_pymotw_header

..
    In this example, the *bad_value* property is included along with the
    standard *message* and *args* values.

このサンプルでは、 *bad_value* プロパティが標準の *message* と *args* の間にあります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'cgitb_exception_properties.py', ignore_error=True))
.. }}}
.. {{{end}}}


..
    Logging Tracebacks
    ==================

トレースバックをロギングする
============================

..
    For many situations, printing the traceback details to standard error
    is the best resolution.  In a production system, however, logging the
    errors is even better.  :func:`enable()` includes an optional
    argument, *logdir*, to enable error logging.  When a directory name is
    provided, each exception is logged to its own file in the given
    directory.

よくある環境では、トレースバック情報の詳細は標準エラー出力に表示することが最も良い方法です。しかし、本番環境では、エラーをロギングする方がもっと良いです。 :func:`enable()` は、エラーロギングを有効にする *logdir* というオプション引数を取ります。ディレクトリ名を指定すると、それぞれの例外はそのディレクトリのログファイルにロギングされます。

.. include:: cgitb_log_exception.py
   :literal:
   :start-after: #end_pymotw_header

..
    Even though the error display is suppressed, a message is printed
    describing where to go to find the error log.

エラーの出力は抑制されますが、そのエラーメッセージはエラーログを探しに行くと見つけられます。


.. {{{cog
.. path('PyMOTW/cgitb/LOGS').rmtree()
.. sh('mkdir -p PyMOTW/cgitb/LOGS')
.. cog.out(run_script(cog.inFile, 'cgitb_log_exception.py', ignore_error=True))
.. cog.out(run_script(cog.inFile, 'ls LOGS', interpreter=None, include_prefix=False))
.. cog.out(run_script(cog.inFile, 'cat LOGS/*.txt', interpreter=None, include_prefix=False))
.. }}}
.. {{{end}}}


..
    HTML Output
    ===========

HTML 出力
=========

..
    Because :mod:`cgitb` was originally developed for handling exceptions
    in web apps, no discussion would be complete without an example of the
    HTML output it produces.

:mod:`cgitb` は、もともと web アプリケーションの例外を処理するために開発されていたので、HTML 出力のサンプルを紹介しないわけにはいきません。

.. include:: cgitb_html_output.py
   :literal:
   :start-after: #end_pymotw_header

..
    By leaving out the *format* argument (or specifying ``html``), the
    traceback format changes to HTML output.

*format* 引数を取り除く(または ``html`` を指定する)ことで、トレースバック情報の出力フォーマットを HTML に変更します。

.. image:: html_error.png


.. seealso::

    `cgitb <http://docs.python.org/library/cgitb.html>`_
        .. The standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント

    :mod:`traceback`
        .. Standard library module for working with tracebacks.

        トレースバック情報を扱う標準ライブラリ

    :mod:`inspect`
        .. The inspect module includes more functions for examining the
           stack.

        スタックを調べる関数を提供する inspect モジュール

    :mod:`sys`
        .. The sys module provides access to the current exception value
           and the ``excepthook`` handler invoked when an exception
           occurs.

        カレントの実行値と例外が発生したときに実行される ``excepthook`` ハンドラへのアクセスを提供する sys モジュール

    `Improved traceback module <http://thread.gmane.org/gmane.comp.python.devel/110326>`_
        .. Python-dev discussion of improvements to the traceback module
           and related enhancements other developers use locally.

        traceback モジュールの改善と開発者が普段行っている機能拡張に関する Python-dev の議論
