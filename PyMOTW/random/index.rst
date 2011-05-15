..
    ===========================================
     random -- Pseudorandom number generators
    ===========================================

==========================
 random -- 疑似乱数の生成
==========================

..
    :synopsis: Pseudorandom number generators

.. module:: random
    :synopsis: 疑似乱数の生成

..
    :Purpose: Implements several types of pseudorandom number generators.
    :Available In: 1.4 and later

:目的: 数種類の疑似乱数ジェネレータを提供する
:利用できるバージョン: 1.4 以上

..
    The :mod:`random` module provides a fast pseudorandom number generator
    based on the *Mersenne Twister* algorithm.  Originally developed to
    produce inputs for Monte Carlo simulations, Mersenne Twister generates
    numbers with nearly uniform distribution and a large period, making it
    suited for a wide range of applications.

:mod:`random` モジュールは、 *Mersenne Twister* アルゴリズムに基づく高速な擬似乱数ジェネレータを提供します。もともとはモンテカルロシミュレーションの入力値を生成するために開発された Mersenne Twister は、周期が長く、広範囲なアプリケーションに適した連続一様分布の数値を生成します。

..
    Generating Random Numbers
    =========================

乱数の生成
==========

..
    The :func:`random` function returns the next random floating point
    value from the generated sequence.  All of the return values fall
    within the range ``0 <= n < 1.0``.

:func:`random` 関数は、生成されたシーケンスから次のランダムな浮動小数点数の値を返します。返り値の範囲は ``0 <= n < 1.0`` になります。

.. include:: random_random.py
   :literal:
   :start-after: #end_pymotw_header

..
    Running the program repeatedly produces different sequences of
    numbers.

このプログラムを繰り返し実行すると、別の数値のシーケンスを生成します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'random_random.py'))
.. cog.out(run_script(cog.inFile, 'random_random.py', include_prefix=False))
.. }}}
.. {{{end}}}

..
    To generate numbers in a specific numerical range, use :func:`uniform`
    instead.  

特定の範囲内の数値を生成するには :func:`uniform` を使用してください。

.. include:: random_uniform.py
   :literal:
   :start-after: #end_pymotw_header

..
    Pass minimum and maximum values, and :func:`uniform` adjusts the
    return values from :func:`random` using the formula ``min + (max -
    min) * random()``.

:func:`uniform` に最小値と最大値を渡すと、 :func:`random` からの返り値を ``min + (max - min) * random()`` の数式で計算します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'random_uniform.py'))
.. }}}
.. {{{end}}}

..
    Seeding
    =======

シード (種)
===========

..
    :func:`random` produces different values each time it is called, and
    has a very large period before it repeats any numbers.  This is useful
    for producing unique values or variations, but there are times when
    having the same dataset available to be processed in different ways is
    useful.  One technique is to use a program to generate random values
    and save them to be processed by a separate step.  That may not be
    practical for large amounts of data, though, so :mod:`random` includes
    the :func:`seed` function for initializing the pseudorandom generator
    so that it produces an expected set of values.

:func:`random` は呼び出される毎に違う値を生成し、任意の数が繰り返されるのにかなり長い周期があります。これは一意な値、またはそれに近い値を生成するには便利ですが、別の方法で処理するのに同じデータセットを利用できると便利なときもあります。1つのテクニックとしては、乱数を生成して、別の方法で処理されるように保存するプログラムを利用することです。しかし、このテクニックは巨大なデータに関しては実用的ではないかもしれません。そのため、 :mod:`random` は、予想される値セットを生成するために、疑似乱数ジェネレータを初期化する :func:`seed` を提供します。

.. include:: random_seed.py
   :literal:
   :start-after: #end_pymotw_header

..
    The seed value controls the first value produced by the formula used
    to produce pseudorandom numbers, and since the formula is
    deterministic it also sets the full sequence produced after the seed
    is changed.  The argument to :func:`seed` can be any hashable object.
    The default is to use a platform-specific source of randomness, if one
    is available.  Otherwise the current time is used.

シードの値は、擬似乱数を生成するために使用される数式によって生成された最初の値を制御します。その数式は決定性なので、シードが変更された後で生成された完全なシーケンスもセットします。 :func:`seed` の引数は、ハッシュ化できる任意のオブジェクトです。デフォルトでは、プラットフォーム固有な乱数のソースが利用できるのなら、それを使用します。それ以外の場合は現在時刻が使用されます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'random_seed.py'))
.. cog.out(run_script(cog.inFile, 'random_seed.py', include_prefix=False))
.. }}}
.. {{{end}}}

..
    Saving State
    ============

状態を保存する
==============

..
    Another technique useful for controlling the number sequence is to
    save the internal state of the generator between test runs.  Restoring
    the previous state before continuing reduces the likelyhood of
    repeating values or sequences of values from the earlier input.  The
    :func:`getstate` function returns data that can be used to
    re-initialize the random number generator later with :func:`setstate`.

数値のシーケンスを制御するのに便利なもう1つのテクニックは、テスト実行間の乱数ジェネレータの内部状態を保存することです。処理を継続する前にその前の状態を復元することで、初期の入力値からの数値、または数値のシーケンスが繰り返される可能性が低くなります。 :func:`getstate` 関数は、次の実行時に :func:`setstate` で乱数ジェネレータを再初期化するデータを返します。

.. include:: random_state.py
   :literal:
   :start-after: #end_pymotw_header

..
    The data returned by :func:`getstate` is an implementation detail, so
    this example saves the data to a file with :mod:`pickle` but otherwise
    treats it as a black box.  If the file exists when the program starts,
    it loads the old state and continues.  Each run produces a few numbers
    before and after saving the state, to show that restoring the state
    causes the generator to produce the same values again.

:func:`getstate` が返すデータは実装の詳細なので、このサンプルは :mod:`pickle` で変換してファイルにそのデータを保存します。それ以外の場合は、そのデータをブラックボックスとして扱います。プログラムの開始時にそのデータを保存したファイルが存在するなら、以前の古い状態を読み込んで処理を継続します。その状態を保存する前後でそれぞれ数回実行することで、状態を復元させるとその乱数ジェネレータは同じ値を生成することが分かります。

.. {{{cog
.. (path(cog.inFile).dirname() / 'state.dat').unlink()
.. cog.out(run_script(cog.inFile, 'random_state.py'))
.. cog.out(run_script(cog.inFile, 'random_state.py', include_prefix=False))
.. }}}
.. {{{end}}}

..
    Random Integers
    ===============

ランダムな整数
==============

..
    :func:`random` generates floating point numbers.  It is possible to
    convert the results to integers, but using :func:`randint` to generate
    integers directly is more convenient.

:func:`random` は、浮動小数点数の数値を生成します。その結果を整数に変換するのも可能ですが、 :func:`randint` 関数を直接使用する方がもっと便利です。

.. include:: random_randint.py
   :literal:
   :start-after: #end_pymotw_header

..
    The arguments to :func:`randint` are the ends of the inclusive range
    for the values.  The numbers can be positive or negative, but the
    first value should be less than the second.

:func:`randint` の引数は、値が取りうる範囲の両端の値です。その引数は、正負どちらの数も受け取れますが、第一引数は第二引数より小さい必要があります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'random_randint.py'))
.. }}}
.. {{{end}}}

..
    :func:`randrange` is a more general form of selecting values from a
    range.  

:func:`randrange` は、ある範囲から数値を選択する汎用的な関数です。

.. include:: random_randrange.py
   :literal:
   :start-after: #end_pymotw_header

..
    :func:`randrange` supports a *step* argument, in addition to start and
    stop values, so it is fully equivalent to selecting a random value
    from ``range(start, stop, step)``.  It is more efficient, because the
    range is not actually constructed.

:func:`randrange` は、start と stop の引数に加えて *step* 引数もサポートします。そのため、 ``range(start, stop, step)`` から乱数を選択しているのと完全に等価です。この範囲は、実際には構築されないので、かなり効率的です。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'random_randrange.py'))
.. }}}
.. {{{end}}}

..
    Picking Random Items
    ====================

ランダムな要素を選ぶ
====================

..
    One common use for random number generators is to select a random item
    from a sequence of enumerated values, even if those values are not
    numbers.  :mod:`random` includes the :func:`choice` function for
    making a random selection from a sequence.  This example simulates
    flipping a coin 10,000 times to count how many times it comes up heads
    and how many times tails.

乱数ジェネレータの一般的な用途の1つは、数字でなくても、列挙型のシーケンスからランダムな要素を選択することです。 :mod:`random` は、シーケンスからランダムに選択する :func:`choice` 関数を提供します。このサンプルは、10,000 回コインを投げて、何回、表 (head) と裏 (tail) が出たかを数えるシミュレーションです。

.. include:: random_choice.py
   :literal:
   :start-after: #end_pymotw_header

..
    There are only two outcomes allowed, so rather than use numbers and
    convert them the words "heads" and "tails" are used with
    :func:`choice`.  The results are tabulated in a dictionary using the
    outcome names as keys.

返り値は2つだけなので、数値を使用するよりも、 :func:`choice` を用いて "heads" と "tails" という単語を数値に変換します。この結果は、outcomes ディクショナリのキーの名前を使用してカウントされます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'random_choice.py'))
.. }}}
.. {{{end}}}

..
    Permutations
    ============

順列
====

..
    A simulation of a card game needs to mix up the deck of cards and then
    "deal" them to the players, without using the same card more than
    once.  Using :func:`choice` could result in the same card being dealt
    twice, so instead the deck can be mixed up with :func:`shuffle` and
    then individual cards removed as they are dealt.

カードゲームのシミュレーションは、カードのデッキを必ず混ぜ合わせてから、同じカードを2回使用しないようにプレイヤーへカードを "配ります" 。 :func:`choice` を使用すると、同じカードを2回配ってしまいます。そのため、代わりにデッキを :func:`shuffle` で混ぜ合わせてから、カードを配るときにそのカードを削除します。

.. include:: random_shuffle.py
   :literal:
   :start-after: #end_pymotw_header

..
    The cards are represented as tuples with the face value and a letter
    indicating the suit.  The dealt "hands" are created by adding one card
    at a time to each of four lists, and removing it from the deck so it
    cannot be dealt again.

カードは数とそのスート (マーク) を指す文字を含むタプルとして表現されます。配られた "手札" は、デッキから同じカードが2回配られないように削除すると同時に、それぞれ4種類のリストへ追加することで作成されます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'random_shuffle.py'))
.. }}}
.. {{{end}}}

..
    Many simulations need random samples from a population of input
    values.  The :func:`sample` function generates samples without
    repeating values and without modifying the input sequence.  This
    example prints a random sample of words from the system dictionary.

多くのシミュレーションは、入力値の母集団からのランダム・サンプルを必要とします。 :func:`sample` 関数は、入力値のシーケンスを変更せず、取り出した値を繰り返さずにサンプル値を生成します。このサンプルは、システム辞書から単語のランダム・サンプルを表示します。

.. include:: random_sample.py
   :literal:
   :start-after: #end_pymotw_header

..
    The algorithm for producing the result set takes into account the
    sizes of the input and the sample requested to produce the result as
    efficiently as possible.

結果セットを生成するためのアルゴリズムは、その入力値のサイズを考慮して、できるだけ効率的に結果を生成するようにサンプル値を指定しました。

::

	$ python random_sample.py

	pleasureman
	consequency
	docibility
	youdendrift
	Ituraean

	$ python random_sample.py

	jigamaree
	readingdom
	sporidium
	pansylike
	foraminiferan

..
    Multiple Simultaneous Generators
    ================================

同時に複数生成する
==================

..
    In addition to module-level functions, :mod:`random` includes a
    :class:`Random` class to manage the internal state for several random
    number generators.  All of the functions described above are available
    as methods of the :class:`Random` instances, and each instance can be
    initialized and used separately, without interfering with the values
    returned by other instances.

モジュールレベルの関数に加え、 :mod:`random` は、複数の乱数ジェネレータのために内部状態を管理する :class:`Random` クラスも提供します。これまでに説明した全ての関数は、 :class:`Random` インスタンスのメソッドとして利用できます。そして、それぞれのインスタンスは、他のインスタンスが返す値に影響を受けずに個別に初期化して使用できます。

.. include:: random_random_class.py
   :literal:
   :start-after: #end_pymotw_header

..
    On a system with good native random value seeding, the instances start
    out in unique states.  However, if there is no good platform random
    value generator, the instances are likely to have been seeded with the
    current time, and therefore produce the same values.

ネイティブな乱数のシードをもつシステムでは、そのインスタンスが一意な状態を保持して利用されます。しかし、プラットフォームに適切な乱数のシードがない場合、そのインスタンスは現在時刻でシードの値を生成しているので、同じ値を生成します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'random_random_class.py'))
.. }}}
.. {{{end}}}

..
    To ensure that the generators produce values from different parts of
    the random period, use :func:`jumpahead` to shift one of them away
    from its initial state.

乱数ジェネレータがランダムな周期の別の部分から値を生成するのを保証するには、その初期状態を変更する :func:`jumpahead` を使用してください。

.. include:: random_jumpahead.py
   :literal:
   :start-after: #end_pymotw_header

..
    The argument to :func:`jumpahead` should be a non-negative integer
    based the number of values needed from each generator.  The internal
    state of the generator is scrambled based on the input value, but not
    simply by incrementing it by the number of steps given.

:func:`jumpahead` の引数は、それぞれの乱数ジェネレータから必要な数値に基づく正の整数にします。乱数ジェネレータの内部状態は、その入力値に基づいて混ぜられますが、引数に渡された値から入力値を増加させるという単純なものではありません。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'random_jumpahead.py'))
.. }}}
.. {{{end}}}

SystemRandom
============

..
    Some operating systems provide a random number generator that has
    access to more sources of entropy that can be introduced into the
    generator.  :mod:`random` exposes this feature through the
    :class:`SystemRandom` class, which has the same API as :class:`Random`
    but uses :func:`os.urandom` to generate the values that form the basis
    of all of the other algorithms.

一部のオペレーティングシステムは、乱数ジェネレータ内部に導入されるエントロピーのより多くのソースにアクセスする乱数ジェネレータを提供します。 :mod:`random` は、 :class:`Random` と同じ API を持つ :class:`SystemRandom` クラスを通して、この機能を公開します。しかし、その他の全てアルゴリズムの基本となる値を生成するには :func:`os.urandom` を使用します。

.. include:: random_system_random.py
   :literal:
   :start-after: #end_pymotw_header

..
    Sequences produced by :class:`SystemRandom` are not reproducable
    because the randomness is coming from the system, rather than software
    state (in fact, :func:`seed` and :func:`setstate` have no effect at
    all).

:class:`SystemRandom` が生成するシーケンスを再現できない理由は、その乱数がソフトウェアの状態というよりもそのシステムからきているからです (実際に :func:`seed` と :func:`setstate` は全く影響を受けません) 。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'random_system_random.py'))
.. }}}
.. {{{end}}}

..
    Non-uniform Distributions
    =========================

不均一分布
==========

..
    While the uniform distribution of the values produced by
    :func:`random` is useful for a lot of purposes, other distributions
    more accurately model specific situations.  The :mod:`random` module
    includes functions to produce values in those distributions, too.
    They are listed here, but not covered in detail because their uses
    tend to be specialized and require more complex examples.

:func:`random` が生成する値の連続一様分布は多くの用途に便利ではあるものの、その他に特定の状況により正確なモデルもあります。 :mod:`random` モジュールは、そういった分布の値を生成する関数も提供します。ここで紹介しますが、その詳細については、より複雑なサンプルを必要とし、その用途が特化されたものなので説明しません。

..
    Normal
    ------

正規分布
--------

..
    The *normal* distribution is commonly used for non-uniform continuous
    values such as grades, heights, weights, etc.  The curve produced by
    the distribution has a distinctive shape which has lead to it being
    nicknamed a "bell curve."  :mod:`random` includes two functions for
    generating values with a normal distribution, :func:`normalvariate`
    and the slightly faster :func:`gauss` (the normal distribution is also
    called the Gaussian distribution).

*正規* 分布は、一般的に非一様な連続性をもつ成績、身長、体重といった値に使用されます。分布曲線は、独特の形状をもち、通称 "ベルカーブ" と呼ばれます。 :mod:`random` は、正規分布の値を生成する2つの関数 :func:`normalvariate` と わずかに高速な :func:`gauss` を提供します (正規分布はガウス分布とも呼ばれる) 。

..
    The related function, :func:`lognormvariate` produces pseudorandom
    values where the logarithm of the values is distributed normally.
    Log-normal distributions are useful for values that are the product of
    several random variables which do not interact.

関連する関数 :func:`lognormvariate` は、正規分布の値の対数で疑似乱数を生成します。対数正規分布は、お互いに影響しない複数の乱数を集めた値に便利です。

..
    Approximation
    -------------

近似
----

..
    The *triangular* distribution is used as an approximate distribution
    for small sample sizes.  The "curve" of a triangular distribution has
    low points at known minimum and maximum values, and a high point at
    and the mode, which is estimated based on a "most likely" outcome
    (reflected by the mode argument to :func:`triangular`).

*三角* 分布は、小さなサンプルサイズの近似分布として使用されます。三角分布の "曲線" は、最小値と最大値の低位置の座標、高位置の座標、そのモードをもちます。そのモードは "最も近い" 結果 (:func:`triangular` のモードの引数で反映される) に基づいて見積もられます。

..
    Exponential
    -----------

指数関数
--------

..
    :func:`expovariate` produces an exponential distribution useful for
    simulating arrival or interval time values for in homogeneous Poisson
    processes such as the rate of radioactive decay or requests coming
    into a web server.

:func:`expovariate` は、Web サーバへ到着するリクエストや放射線減衰率といったポアソン分布のために、到着するものや間隔の時間の値に便利です。

..
    The Pareto, or power law, distribution matches many observable
    phenomena and was popularized by Chris Anderon's book, *The Long
    Tail*.  The :func:`paretovariate` function is useful for simulating
    allocation of resources to individuals (wealth to people, demand for
    musicians, attention to blogs, etc.).

パレート、またはべき乗則の分布は多くの実際に目に見える現象と一致し、Chris Anderon の著書 *ロングテール* で広まりました。 :func:`paretovariate` 関数は、目に見えないリソース (人々の豊かさ、音楽家の需要、ブログへのこだわりなど) を割り当てるシミュレーションに便利です。

..
    Angular
    -------

角度
----

..
    The von Mises, or circular normal, distribution (produced by
    :func:`vonmisesvariate`) is used for computing probabilities of cyclic
    values such as angles, calendar days, and times.

(:func:`vonmisesvariate` で生成される) フォン・ミーゼス分布、または円周上の正規分布は、角度、カレンダーの日付、時間といった周期的な確率を計算するのに使用されます。

..
    Sizes
    -----

サイズ
------

..
    :func:`betavariate` generates values with the Beta distribution, which
    is commonly used in Bayesian statistics and applications such as task
    duration modeling.

:func:`betavariate` は、モデリング間のタスクといったアプリケーションや一般的にベイズ統計で利用されるベータ分布の値を生成します。

..
    The Gamma distribution produced by :func:`gammavariate` is used for
    modeling the sizes of things such as waiting times, rainfall, and
    computational errors.

:func:`gammavariate` が生成するガンマ分布は、待ち時間、降雨量、計算エラーといったサイズをモデリングするために使用されます。

..
    The Weibull distribution computed by :func:`weibullvariate` is used in
    failure analysis, industrial engineering, and weather forecasting.  It
    describes the distribution of sizes of particles or other discrete
    objects.

:func:`weibullvariate` が生成するワイブル分布は、不良解析、工業エンジニアリング、天気予報に使用されます。これは粒子または離散物体のサイズの分布を説明します。

.. seealso::

    `random <http://docs.python.org/library/random.html>`_
        .. The standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント

    Mersenne Twister: A 623-dimensionally equidistributed uniform pseudorandom number generator
        .. Article by M. Matsumoto and T. Nishimura from *ACM
           Transactions on Modeling and Computer Simulation* Vol. 8,
           No. 1, January pp.3-30 1998.

        松本眞氏と西村拓士氏の論文 *ACM Transactions on Modeling and Computer Simulation* Vol. 8, No. 1, January pp.3-30 1998

    `Wikipedia: Mersenne Twister <http://en.wikipedia.org/wiki/Mersenne_twister>`_
        .. Article about the pseudorandom generator algorithm used by Python.

        Python で利用できる疑似乱数生成に関する記事

    `Wikipedia: Uniform distribution <http://en.wikipedia.org/wiki/Uniform_distribution_(continuous)>`_
        .. Article about continuous uniform distributions in statistics.

        統計における連続一様分布に関する記事
