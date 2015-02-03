..
    ======================================================
    trace -- Follow Python statements as they are executed
    ======================================================

=================================================
trace -- 実行された通りに Python コードを追跡する
=================================================

..
    :synopsis: Follow Python statements as they are executed.

.. module:: trace
    :synopsis: 実行された通りに Python コードを追跡する

..
    :Purpose: Monitor which statements and functions are executed as a program runs to produce coverage and call-graph information.
    :Available In: 2.3 and later

:目的: カバレッジやコールグラフ情報を生成するためにプログラムが実行された通りにコードや関数の動きを監視する
:利用できるバージョン: 2.3 以上

..
    The :mod:`trace` module helps you understand the way your program
    runs.  You can trace the statements executed, produce coverage
    reports, and investigate the relationships between functions that call
    each other.

:mod:`trace` モジュールはプログラムがどういった順番に実行されるかを理解し易くします。実行されたコードをトレースしたり、カバレッジレポートを生成したり、関数間の呼び出し関係を調査したりできます。

..
    Command Line Interface
    ======================

コマンドラインインタフェース
============================

..
    It is easy use :mod:`trace` directly from the command line.  Given the
    following Python scripts as input:

コマンドラインから直接 :mod:`trace` を使用するのが簡単です。入力として次の Python スクリプトを使用します。

.. include:: trace_example/main.py
    :literal:
    :start-after: #end_pymotw_header

.. include:: trace_example/recurse.py
    :literal:
    :start-after: #end_pymotw_header

..
    Tracing Execution
    -----------------

トレース実行
------------

..
    We can see which statements are being executed as the program runs
    using the :option:`--trace` option.

:option:`--trace` オプションを使用してプログラム内のどのコードが実行されるかが分かります。

.. {{{cog
.. cog.out(run_script(cog.inFile, '-m trace --trace trace_example/main.py'))
.. }}}

::

	$ python -m trace --trace trace_example/main.py
	
	 --- modulename: main, funcname: <module>
	main.py(7): """
	main.py(12): from recurse import recurse
	 --- modulename: recurse, funcname: <module>
	recurse.py(7): """
	recurse.py(12): def recurse(level):
	recurse.py(18): def not_called():
	main.py(14): def main():
	main.py(19): if __name__ == '__main__':
	main.py(20):     main()
	 --- modulename: main, funcname: main
	main.py(15):     print 'This is the main program.'
	This is the main program.
	main.py(16):     recurse(2)
	 --- modulename: recurse, funcname: recurse
	recurse.py(13):     print 'recurse(%s)' % level
	recurse(2)
	recurse.py(14):     if level:
	recurse.py(15):         recurse(level-1)
	 --- modulename: recurse, funcname: recurse
	recurse.py(13):     print 'recurse(%s)' % level
	recurse(1)
	recurse.py(14):     if level:
	recurse.py(15):         recurse(level-1)
	 --- modulename: recurse, funcname: recurse
	recurse.py(13):     print 'recurse(%s)' % level
	recurse(0)
	recurse.py(14):     if level:
	recurse.py(16):     return
	recurse.py(16):     return
	recurse.py(16):     return
	main.py(17):     return
	 --- modulename: trace, funcname: _unsettrace
	trace.py(80):         sys.settrace(None)

.. {{{end}}}

..
    The first part of the output shows some setup operations performed by
    :mod:`trace`.  The rest of the output shows the entry into each
    function, including the module where the function is located, and then
    the lines of the source file as they are executed.  You can see that
    :func:`recurse()` is entered three times, as you would expect from the
    way it is called in :func:`main()`.

この出力の最初の部分は :mod:`trace` が実行したセットアップ処理です。残りの出力は、関数が定義されているモジュールとその関数へのエントリ、実行されたソースファイルの行番号です。 :func:`main()` で呼び出されて期待した通りに :func:`recurse()` は3回呼び出されることが分かります。

..
    Code Coverage
    -------------

コードカバレッジ
----------------

..
    Running :mod:`trace` from the command line with the :option:`--count`
    option will produce code coverage report information, so you can see
    which lines are run and which are skipped.  Since your program is
    usually made up of multiple files, a separate coverage report is
    produced for each.  By default the coverage report files are written
    to the same directory as the module, named after the module but with a
    ``.cover`` extension instead of ``.py``.

コマンドラインから :mod:`trace` に :option:`--count` オプションを与えるとコードカバレッジレポートを生成します。ソースコードのどの行が実行されて、どの行がスキップされたかが分かります。プログラムは通常、複数のソースファイルで構成されるので、分割されたカバレッジレポートがそれぞれに生成されます。デフォルトでは、カバレッジレポートファイルはモジュールと同じディレクトリに ``.py`` ではなく ``.cover`` という拡張子でモジュールと同じ名前で書き込まれます。

.. {{{cog
.. cog.out(run_script(cog.inFile, '-m trace --count trace_example/main.py'))
.. }}}

::

	$ python -m trace --count trace_example/main.py
	
	This is the main program.
	recurse(2)
	recurse(1)
	recurse(0)

.. {{{end}}}

..
    And two output files, ``trace_example/main.cover``:

2つのファイルが出力されます。 ``trace_example/main.cover`` と

.. include:: trace_example/main.cover
    :literal:
    :start-after: #end_pymotw_header

``trace_example/recurse.cover`` です。

.. include:: trace_example/recurse.cover
    :literal:
    :start-after: #end_pymotw_header

.. note:: 

    .. Although the line ``def recurse(level):`` has a count of ``1``,
       that does not mean the function was only run once.  It means the
       function *definition* was only executed once.

    ``def recurse(level):`` 行の件数は ``1`` ですが、この関数が1度だけ呼び出されたという意味ではありません。これは関数の *定義* が1度だけ行われたことを表します。

..
    It is also possible to run the program several times, perhaps with
    different options, to save the coverage data and produce a combined
    report.

おそらくは違うオプションでカバレッジデータを保存するためにプログラムを数回実行して、それらを組み合わせたレポートも生成できます。

.. {{{cog
.. (path(cog.inFile).parent / 'coverdir1').rmtree()
.. (path(cog.inFile).parent / 'coverdir1').mkdir()
.. cog.out(run_script(cog.inFile, '-m trace --coverdir coverdir1 --count --file coverdir1/coverage_report.dat trace_example/main.py'))
.. cog.out(run_script(cog.inFile, '-m trace --coverdir coverdir1 --count --file coverdir1/coverage_report.dat trace_example/main.py', include_prefix=False))
.. cog.out(run_script(cog.inFile, '-m trace --coverdir coverdir1 --count --file coverdir1/coverage_report.dat trace_example/main.py', include_prefix=False))
.. }}}

::

	$ python -m trace --coverdir coverdir1 --count --file coverdir1/coverage\
	_report.dat trace_example/main.py
	
	Skipping counts file 'coverdir1/coverage_report.dat': [Errno 2] No such file or directory: 'coverdir1/coverage_report.dat'
	This is the main program.
	recurse(2)
	recurse(1)
	recurse(0)

	$ python -m trace --coverdir coverdir1 --count --file coverdir1/coverage\
	_report.dat trace_example/main.py
	
	This is the main program.
	recurse(2)
	recurse(1)
	recurse(0)

	$ python -m trace --coverdir coverdir1 --count --file coverdir1/coverage\
	_report.dat trace_example/main.py
	
	This is the main program.
	recurse(2)
	recurse(1)
	recurse(0)

.. {{{end}}}

..
    Once the coverage information is recorded to the ``.cover`` files, you
    can produce reports with the :option:`--report` option.

カバレッジ情報が ``.cover`` ファイルに記録されたら :option:`--report` オプションでレポートを生成できます。

.. {{{cog
.. cog.out(run_script(cog.inFile, '-m trace --coverdir coverdir1 --report --summary --missing --file coverdir1/coverage_report.dat trace_example/main.py'))
.. }}}

::

	$ python -m trace --coverdir coverdir1 --report --summary --missing --fi\
	le coverdir1/coverage_report.dat trace_example/main.py
	
	lines   cov%   module   (path)
	  515     0%   trace   (/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/trace.py)
	    8   100%   trace_example.main   (trace_example/main.py)
	    8    87%   trace_example.recurse   (trace_example/recurse.py)

.. {{{end}}}

..
    Since the program ran three times, the coverage report shows values
    three times higher than the first report.  The :option:`--summary`
    option adds the percent covered information to the output above.  The
    ``recurse`` module is only 87% covered.  A quick look at the cover
    file for recurse shows that the body of ``not_called()`` is indeed
    never run, indicated by the ``>>>>>>`` prefix.

3回プログラムを実行したので、カバレッジレポートは最初のレポートよりも3倍多くなります。 :option:`--summary` オプションは上述したレポートのカバレッジ情報のパーセンテージを追加します。 ``recurse`` モジュールは 87% だけ実行されました。recurse の cover ファイルをざっと見てみると ``not_called()`` 関数が実行されていないことが ``>>>>>>`` の接頭辞で表されています。

.. include:: coverdir1/trace_example.recurse.cover
    :literal:
    :start-after: #end_pymotw_header

..
    Calling Relationships
    ---------------------

呼び出し関係
------------

..
    In addition to coverage information, :mod:`trace` will collect and
    report on the relationships between functions that call each other.

カバレッジ情報に加えて :mod:`trace` が関数間の呼び出し関係を集めてレポートを生成します。

..
    For a simple list of the functions called, use :option:`--listfuncs`:

関数呼び出しのシンプルなリストは :option:`--listfuncs` オプションを使用してください。

.. {{{cog
.. cog.out(run_script(cog.inFile, '-m trace --listfuncs trace_example/main.py'))
.. }}}

::

	$ python -m trace --listfuncs trace_example/main.py
	
	This is the main program.
	recurse(2)
	recurse(1)
	recurse(0)
	
	functions called:
	filename: /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/trace.py, modulename: trace, funcname: _unsettrace
	filename: trace_example/main.py, modulename: main, funcname: <module>
	filename: trace_example/main.py, modulename: main, funcname: main
	filename: trace_example/recurse.py, modulename: recurse, funcname: <module>
	filename: trace_example/recurse.py, modulename: recurse, funcname: recurse

.. {{{end}}}

..
    For more details about who is doing the calling, use
    :option:`--trackcalls`.

どの関数から呼び出したかの詳細については :option:`--trackcalls` オプションを使用してください。

.. {{{cog
.. cog.out(run_script(cog.inFile, '-m trace --listfuncs --trackcalls trace_example/main.py'))
.. }}}

::

	$ python -m trace --listfuncs --trackcalls trace_example/main.py
	
	This is the main program.
	recurse(2)
	recurse(1)
	recurse(0)
	
	calling relationships:
	
	*** /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/trace.py ***
	    trace.Trace.runctx -> trace._unsettrace
	  --> trace_example/main.py
	    trace.Trace.runctx -> main.<module>
	
	*** trace_example/main.py ***
	    main.<module> -> main.main
	  --> trace_example/recurse.py
	    main.<module> -> recurse.<module>
	    main.main -> recurse.recurse
	
	*** trace_example/recurse.py ***
	    recurse.recurse -> recurse.recurse

.. {{{end}}}

..
    Programming Interface
    =====================

プログラミングインタフェース
============================

..
    For a little more control over the trace interface, you can invoke it
    from within your program using a :class:`Trace` object.
    :class:`Trace` lets you set up fixtures and other dependencies before
    running a single function or execing a Python command to be traced.

trace のインタフェース上でもう少し制御するためにプログラム内で :class:`Trace` オブジェクトを使用して実行できます。 :class:`Trace` クラスは1つの関数を実行する、もしくはトレースする Python コマンドを実行する前にフィクスチャとその他の依存関係を設定します。

.. include:: trace_run.py
    :literal:
    :start-after: #end_pymotw_header

..
    Since the example only traces into the :func:`recurse()` function, no
    information from ``main.py`` is included in the output.

:func:`recurse()` 関数の内部のみをトレースするサンプルなので ``main.py`` からの情報が出力結果には含まれません。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'trace_run.py'))
.. }}}

::

	$ python trace_run.py
	
	 --- modulename: trace_run, funcname: <module>
	<string>(1):   --- modulename: recurse, funcname: recurse
	recurse.py(13):     print 'recurse(%s)' % level
	recurse(2)
	recurse.py(14):     if level:
	recurse.py(15):         recurse(level-1)
	 --- modulename: recurse, funcname: recurse
	recurse.py(13):     print 'recurse(%s)' % level
	recurse(1)
	recurse.py(14):     if level:
	recurse.py(15):         recurse(level-1)
	 --- modulename: recurse, funcname: recurse
	recurse.py(13):     print 'recurse(%s)' % level
	recurse(0)
	recurse.py(14):     if level:
	recurse.py(16):     return
	recurse.py(16):     return
	recurse.py(16):     return

.. {{{end}}}

..
    That same output could have been produced with the :func:`runfunc()`
    method, too.  :func:`runfunc()` accepts arbitrary positional and
    keyword arguments, which are passed to the function when it is called
    by the tracer.

これと同じ出力は :func:`runfunc()` メソッドでも生成されます。 :func:`runfunc()` はトレーサが呼び出されるときに関数へ渡す任意の位置引数とキーワード引数を取ります。

.. include:: trace_runfunc.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'trace_runfunc.py'))
.. }}}

::

	$ python trace_runfunc.py
	
	 --- modulename: recurse, funcname: recurse
	recurse.py(13):     print 'recurse(%s)' % level
	recurse(2)
	recurse.py(14):     if level:
	recurse.py(15):         recurse(level-1)
	 --- modulename: recurse, funcname: recurse
	recurse.py(13):     print 'recurse(%s)' % level
	recurse(1)
	recurse.py(14):     if level:
	recurse.py(15):         recurse(level-1)
	 --- modulename: recurse, funcname: recurse
	recurse.py(13):     print 'recurse(%s)' % level
	recurse(0)
	recurse.py(14):     if level:
	recurse.py(16):     return
	recurse.py(16):     return
	recurse.py(16):     return

.. {{{end}}}

..
    Saving Result Data
    ------------------

結果データを保存する
--------------------

..
    Counts and coverage information can be recorded as well, just as with
    the command line interface.  The data must be saved explicitly, using
    the :class:`CoverageResults` instance from the :class:`Trace` object.

件数とカバレッジ情報はコマンドラインインタフェースと同様に記録されます。そのデータは :class:`Trace` オブジェクトの :class:`CoverageResults` インスタンスを使用して明示的に保存されなければなりません。

.. include:: trace_CoverageResults.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'trace_CoverageResults.py'))
.. cog.out(run_script(cog.inFile, 'find coverdir2', interpreter=None, include_prefix=False))
.. }}}

::

	$ python trace_CoverageResults.py
	
	recurse(2)
	recurse(1)
	recurse(0)

	$ find coverdir2
	
	coverdir2
	coverdir2/trace_example.recurse.cover

.. {{{end}}}

..
    And the contents of ``coverdir2/trace_example.recurse.cover``:

``coverdir2/trace_example.recurse.cover`` のコンテンツです。

.. include:: coverdir2/trace_example.recurse.cover
    :literal:

..
    To save the counts data for generating reports, use the *infile* and
    *outfile* argument to :class:`Trace`.

レポートを生成するための件数データを保存するために :class:`Trace` へ渡す *infile* と *outfile* 引数を使用してください。

.. include:: trace_report.py
    :literal:
    :start-after: #end_pymotw_header

..
    Pass a filename to *infile* to read previously stored data, and a
    filename to *outfile* to write new results after tracing.  If *infile*
    and *outfile* are the same, it has the effect of updating the file
    with cummulative data.

以前に保存されたデータを読み込むために *infile* へ、トレースした新たな結果を書き込むために *outfile* へファイル名を渡します。 *infile* と *outfile* が同じファイルなら、データを累積してファイルが更新されます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'trace_report.py'))
.. }}}

::

	$ python trace_report.py
	
	recurse(2)
	recurse(1)
	recurse(0)
	lines   cov%   module   (path)
	    8    50%   trace_example.recurse   (/Users/dhellmann/Documents/PyMOTW/src/PyMOTW/trace/trace_example/recurse.py)

.. {{{end}}}

..
    Trace Options
    -------------

Trace オプション
----------------

..
    The constructor for :class:`Trace` takes several optional parameters
    to control runtime behavior.

:class:`Trace` のコンストラクタは実行時の振る舞いを制御する複数のオプションパラメータを取ります。

..
    *count*
      Boolean.  Turns on line number counting.  Defaults to True.

*count*
  ブーリアン。行番号を数えるかを指定します。デフォルトは True です。

..
    *countfuncs*
      Boolean.  Turns on list of functions called during the run.
      Defaults to False.

*countfuncs*
  ブーリアン。実行して呼び出された関数の数を表示するかを指定します。デフォルトは False です。

..
    *countcallers*
      Boolean.  Turns on tracking for callers and callees.  Defaults to
      False.

*countcallers*
  ブーリアン。呼び出し側と呼び出される側を追跡するかを指定します。デフォルトは False です。

..
    *ignoremods*
      Sequence.  List of modules or packages to ignore when tracking
      coverage.  Defaults to an empty tuple.

*ignoremods*
  シーケンス。カバレッジを追跡するときに無視するモジュールやパッケージを指定します。デフォルトは空のタプルです。

..
    *ignoredirs*
      Sequence.  List of directories containing modules or packages to be
      ignored.  Defaults to an empty tuple.

*ignoredirs*
  シーケンス。無視するモジュールやパッケージを含むディレクトリを指定します。デフォルトは空のタプルです。

..
    *infile*
      Name of the file containing cached count values.  Defaults to None.

*infile*
  キャッシュされた件数を含む入力ファイル名です。デフォルトは None です。

..
    *outfile*
      Name of the file to use for storing cached count files.  Defaults to
      None, and data is not stored.

*outfile*
  件数をキャッシュするための出力ファイル名です。デフォルトは None で、データは保存されません。

.. seealso::

    `trace <http://docs.python.org/lib/module-trace.html>`_
        .. Standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント

    :ref:`sys-tracing`
        .. The :mod:`sys` module includes facilities for adding your own
           tracing function to the interpreter at run-time.

        :mod:`sys` モジュールは実行時にインタープリタに独自トレース関数を追加するための仕組みを提供します

    `coverage.py <http://nedbatchelder.com/code/modules/coverage.html>`_
        .. Ned Batchelder's coverage module.

        Ned Batchelder のカバレッジモジュール

    `figleaf <http://darcs.idyll.org/~t/projects/figleaf/doc/>`_
        .. Titus Brown's coverage app.

        Titus Brown のカバレッジアプリケーション
