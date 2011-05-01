..
    =========================================================================
    profile, cProfile, and pstats -- Performance analysis of Python programs.
    =========================================================================

==================================================================
profile, cProfile, pstats -- Python プログラムのパフォーマンス解析
==================================================================

..
    :synopsis: Performance analysis of Python programs.

.. module:: profile
    :synopsis: Python プログラムのパフォーマンス解析

..
    :synopsis: Performance analysis of Python programs.

.. module:: cProfile
    :synopsis: Python プログラムのパフォーマンス解析

..
    :Purpose: Performance analysis of Python programs.
    :Available In: 1.4 and later, these examples are for Python 2.5

:目的: Python プログラムのパフォーマンス解析
:利用できるバージョン: 1.4 以上、このサンプルは Python 2.5 向け

..
    The :mod:`profile` and :mod:`cProfile` modules provide APIs for
    collecting and analyzing statistics about how Python source consumes
    processor resources.

:mod:`profile` と :mod:`cProfile` モジュールは、Python プログラムがどのぐらいプロセッサのリソースを消費するかの統計を収集分析する API を提供します。

run()
=====

..
    The most basic starting point in the profile module is ``run()``.  It
    takes a string statement as argument, and creates a report of the time
    spent executing different lines of code while running the statement.

:mod:`profile` モジュールの最も基本的な開始ポイントは :func:`run` です。それは引数として文字列のコードを受け取り、文字列のコードの実行時に実際のコードの実行に要した時間のレポートを作成します。

.. include:: profile_fibonacci_raw.py
   :literal:
   :start-after: #end_pymotw_header

..
    This recursive version of a fibonacci sequence calculator
    [#fibonacci]_ is especially useful for demonstrating the profile
    because we can improve the performance so much.  The standard report
    format shows a summary and then details for each function executed.

このフィボナッチ数列計算の再帰バージョン [#fibonacci]_ は、大幅なパフォーマンス改善ができるのでプロファイルのデモをするのに特に便利です。標準のレポートフォーマットは、全体パフォーマンスの要約と実行したそれぞれの関数の詳細を表示します。

::

    $ python profile_fibonacci_raw.py
    RAW
    ================================================================================
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
    
             57356 function calls (66 primitive calls) in 0.746 CPU seconds
    
       Ordered by: standard name
    
       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
           21    0.000    0.000    0.000    0.000 :0(append)
           20    0.000    0.000    0.000    0.000 :0(extend)
            1    0.001    0.001    0.001    0.001 :0(setprofile)
            1    0.000    0.000    0.744    0.744 <string>:1(<module>)
            1    0.000    0.000    0.746    0.746 profile:0(print fib_seq(20); print)
            0    0.000             0.000          profile:0(profiler)
     57291/21    0.743    0.000    0.743    0.035 profile_fibonacci_raw.py:13(fib)
         21/1    0.001    0.000    0.744    0.744 profile_fibonacci_raw.py:22(fib_seq)

..
    As you can see, it takes 57356 separate function calls and 3/4 of a
    second to run.  Since there are only 66 *primitive* calls, we know
    that the vast majority of those 57k calls were recursive.  The details
    about where time was spent are broken out by function in the listing
    showing the number of calls, total time spent in the function, time
    per call (tottime/ncalls), cumulative time spent in a function, and
    the ratio of cumulative time to primitive calls.

ご覧の通り、これは 57356 回の関数呼び出しと実行に 3/4 秒かかります。 *プリミティブ* な呼び出しは 66 回のみなので、57000 回の大半の呼び出しは再帰的に呼び出されたと分かります。処理に関する詳細は、関数毎に呼び出しの数(ncalls)、関数の実行に要した合計時間(tottime)、1回の呼び出し毎の時間(percall: tottime/ncalls)、1つの関数に要した累積時間(cumtime)、プリミティブな呼び出しの累積時間の割合(percall)に分類されます。

..
    Not surprisingly, most of the time here is spent calling ``fib()``
    repeatedly.  We can add a memoize decorator [#memoize]_ to reduce the
    number of recursive calls and have a big impact on the performance of
    this function.

当然のことながら、この処理の大半の時間は何回も :func:`fib` の呼び出しにかかっています。再帰呼び出しの回数を減らすために memoize デコレータ [#memoize]_ を追加すると、この関数のパフォーマンスに大きな影響があります。

.. include:: profile_fibonacci_memoized.py
    :literal:
    :start-after: #end_pymotw_header

..
    By remembering the Fibonacci value at each level we can avoid most of
    the recursion and drop down to 145 calls that only take 0.003 seconds.
    Also notice that the ncalls count for ``fib()`` shows that it *never*
    recurses.

再帰呼び出しの各レベルでフィボナッチ数を覚えておくことで、ほとんどの再帰呼び出しを行わずに 145 回に減らして、ほんの 0.003 秒になります。さらに :func:`fib` の ncalls 回数を見ると、その関数が *決して* 再帰呼び出しされないことに注目してください。

::

    $ python profile_fibonacci_memoized.py
    MEMOIZED
    ================================================================================
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
    
             145 function calls (87 primitive calls) in 0.003 CPU seconds
    
       Ordered by: standard name
    
       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
           21    0.000    0.000    0.000    0.000 :0(append)
           20    0.000    0.000    0.000    0.000 :0(extend)
            1    0.001    0.001    0.001    0.001 :0(setprofile)
            1    0.000    0.000    0.002    0.002 <string>:1(<module>)
            1    0.000    0.000    0.003    0.003 profile:0(print fib_seq(20); print)
            0    0.000             0.000          profile:0(profiler)
        59/21    0.001    0.000    0.001    0.000 profile_fibonacci_memoized.py:19(__call__)
           21    0.000    0.000    0.001    0.000 profile_fibonacci_memoized.py:26(fib)
         21/1    0.001    0.000    0.002    0.002 profile_fibonacci_memoized.py:36(fib_seq)

runctx()
========

..
    Sometimes, instead of constructing a complex expression for ``run()``,
    it is easier to build a simple expression and pass it parameters
    through a context, using ``runctx()``.

場合によっては :func:`run` に複雑な式を渡すのではなく、シンプルな式を作成して :func:`runctx` からコンテキストを通してパラメータを渡すと簡単です。

.. include:: profile_runctx.py
    :literal:
    :start-after: #end_pymotw_header

..
    In this example, the value of "n" is passed through the local variable
    context instead of being embedded directly in the statement passed to
    ``runctx()``.

このサンプルでは、"n" の値は :func:`runctx` へ渡すコードに直接含まれるのではなく、ローカル変数のコンテキストを通して渡されます。

::

    $ python profile_runctx.py
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]

             145 function calls (87 primitive calls) in 0.003 CPU seconds

       Ordered by: standard name

       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
           21    0.000    0.000    0.000    0.000 :0(append)
           20    0.000    0.000    0.000    0.000 :0(extend)
            1    0.001    0.001    0.001    0.001 :0(setprofile)
            1    0.000    0.000    0.002    0.002 <string>:1(<module>)
            1    0.000    0.000    0.003    0.003 profile:0(print fib_seq(n); print)
            0    0.000             0.000          profile:0(profiler)
        59/21    0.001    0.000    0.001    0.000 profile_fibonacci_memoized.py:19(__call__)
           21    0.000    0.000    0.001    0.000 profile_fibonacci_memoized.py:26(fib)
         21/1    0.001    0.000    0.002    0.002 profile_fibonacci_memoized.py:36(fib_seq)

..
    pstats: Saving and Working With Statistics
    ==========================================

pstats: 統計を保存して扱う
==========================

..
    :synopsis: Manipulate and analyze profile statistics.

.. module:: pstats
    :synopsis: profile の統計を分析して扱う

..
    The standard report created by the :mod:`profile` functions is not
    very flexible.  If it doesn't meet your needs, you can produce your
    own reports by saving the raw profiling data from ``run()`` and
    ``runctx()`` and processing it separately with the **Stats** class
    from :mod:`pstats`.

:mod:`profile` 関数が作成する標準レポートはあまり柔軟ではありません。もし標準レポートが要望にあわないなら、 :func:`run` と :func:`runctx` が生成した raw プロファイルデータを保存して、 :mod:`pstats` から **Stats** クラスで個別に処理することで独自レポートを作成できます。

..
    For example, to run several iterations of the same test and combine
    the results, you could do something like this:

例えば、同じテストを何回か繰り返し実行して、その実行結果を組み合わせるのは次のようになります。

.. include:: profile_stats.py
    :literal:
    :start-after: #end_pymotw_header

..
    The output report is sorted in descending order of cumulative time
    spent in the function and the directory names are removed from the
    printed filenames to conserve horizontal space.

その実行結果のレポートは、その関数に要した累積時間の降順にソートされます。そして、表示上の横幅を節約するためにファイル名からディレクトリ名を削除します。

::

    $ python profile_stats.py
    0 [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
    1 [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
    2 [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
    3 [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
    4 [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
    Sun Aug 31 11:29:36 2008    profile_stats_0.stats
    Sun Aug 31 11:29:36 2008    profile_stats_1.stats
    Sun Aug 31 11:29:36 2008    profile_stats_2.stats
    Sun Aug 31 11:29:36 2008    profile_stats_3.stats
    Sun Aug 31 11:29:36 2008    profile_stats_4.stats
    
             489 function calls (351 primitive calls) in 0.008 CPU seconds
    
       Ordered by: cumulative time
    
       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
            5    0.000    0.000    0.007    0.001 <string>:1(<module>)
        105/5    0.004    0.000    0.007    0.001 profile_fibonacci_memoized.py:36(fib_seq)
            1    0.000    0.000    0.003    0.003 profile:0(print 0, fib_seq(20))
      143/105    0.001    0.000    0.002    0.000 profile_fibonacci_memoized.py:19(__call__)
            1    0.000    0.000    0.001    0.001 profile:0(print 4, fib_seq(20))
            1    0.000    0.000    0.001    0.001 profile:0(print 1, fib_seq(20))
            1    0.000    0.000    0.001    0.001 profile:0(print 2, fib_seq(20))
            1    0.000    0.000    0.001    0.001 profile:0(print 3, fib_seq(20))
           21    0.000    0.000    0.001    0.000 profile_fibonacci_memoized.py:26(fib)
          100    0.001    0.000    0.001    0.000 :0(extend)
          105    0.001    0.000    0.001    0.000 :0(append)
            5    0.001    0.000    0.001    0.000 :0(setprofile)
            0    0.000             0.000          profile:0(profiler)

..
    Limiting Report Contents
    ========================

レポートコンテンツを制限する
============================

..
    Since we are studying the performance of ``fib()`` and ``fib_seq()``,
    we can also restrict the output report to only include those functions
    using a regular expression to match the ``filename:lineno(function)``
    values we want.

いまは :func:`fib` と :func:`fib_seq` のパフォーマンスを調べているので、 ``filename:lineno(function)`` にマッチする正規表現を使用してそういった関数のみを含めるように結果レポートを制限できます。

.. include:: profile_stats_restricted.py
    :literal:
    :start-after: #end_pymotw_header

..
    The regular expression includes a literal left paren (``(``) to match
    against the function name portion of the location value.

この正規表現は関数名の部分にマッチするようにリテラルの左括弧 (``(``) を含めます。

::

    $ python profile_stats_restricted.py
    Sun Aug 31 11:29:36 2008    profile_stats_0.stats
    Sun Aug 31 11:29:36 2008    profile_stats_1.stats
    Sun Aug 31 11:29:36 2008    profile_stats_2.stats
    Sun Aug 31 11:29:36 2008    profile_stats_3.stats
    Sun Aug 31 11:29:36 2008    profile_stats_4.stats
    
             489 function calls (351 primitive calls) in 0.008 CPU seconds
    
       Ordered by: cumulative time
       List reduced from 13 to 2 due to restriction <'\\(fib'>
    
       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        105/5    0.004    0.000    0.007    0.001 profile_fibonacci_memoized.py:36(fib_seq)
           21    0.000    0.000    0.001    0.000 profile_fibonacci_memoized.py:26(fib)
    
..    
    Caller / Callee Graphs
    ======================

呼び出し / 呼び出される関数のグループ
=====================================

..
    **Stats** also includes methods for printing the callers and callees
    of functions.

さらに **Stats** は、関数の呼び出し側と呼び出される側を表示するメソッドを提供します。

.. include:: profile_stats_callers.py
    :literal:
    :start-after: #end_pymotw_header

..
    The arguments to ``print_callers()`` and ``print_callees()`` work the
    same as the restriction arguments to ``print_stats()``.  The output
    shows the caller, callee, and cumulative time.

:func:`print_callers` と :func:`print_callees` への引数は :func:`print_stats` の引数と同様に正規表現で出力を制限できます。その結果レポートは呼び出し側と呼び出される側の累積時間を表示します。

::

    $ python profile_stats_callers.py
    INCOMING CALLERS:
       Ordered by: cumulative time
       List reduced from 13 to 2 due to restriction <'\\(fib'>
    
    Function                                   was called by...
    profile_fibonacci_memoized.py:36(fib_seq)  <- <string>:1(<module>)(5)    0.007
                                                  profile_fibonacci_memoized.py:36(fib_seq)(100)    0.007
    profile_fibonacci_memoized.py:26(fib)      <- profile_fibonacci_memoized.py:19(__call__)(21)    0.002
    
    
    OUTGOING CALLEES:
       Ordered by: cumulative time
       List reduced from 13 to 2 due to restriction <'\\(fib'>
    
    Function                                   called...
    profile_fibonacci_memoized.py:36(fib_seq)  -> :0(append)(105)    0.001
                                                  :0(extend)(100)    0.001
                                                  profile_fibonacci_memoized.py:19(__call__)(105)    0.002
                                                  profile_fibonacci_memoized.py:36(fib_seq)(100)    0.007
    profile_fibonacci_memoized.py:26(fib)      -> profile_fibonacci_memoized.py:19(__call__)(38)    0.002


.. seealso::

    `profile and cProfile <http://docs.python.org/lib/module-profile.html>`_
        .. Standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント

    `pstats <http://docs.python.org/lib/profile-stats.html>`_
        .. Standard library documentation for pstats.

        pstats の標準ライブラリドキュメント

    `Gprof2Dot <http://code.google.com/p/jrfonseca/wiki/Gprof2Dot>`_
        .. Visualization tool for profile output data.

        プロファイル出力データの視覚化ツール

    .. [#fibonacci] *Fibonacci numbers (Python) - LiteratePrograms* via http://en.literateprograms.org/Fibonacci_numbers_(Python)

    .. [#memoize] *Python Decorators: Syntactic Sugar | avinash.vora* from http://avinashv.net/2008/04/python-decorators-syntactic-sugar/
