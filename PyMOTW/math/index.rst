..
    ================================
     math -- Mathematical functions
    ================================

==========================
 math -- 数学に関する関数
==========================

..
    :synopsis: Mathematical functions

.. module:: math
    :synopsis: 数学に関する関数

..
    :Purpose: Provides functions for specialized mathematical operations.
    :Available In: 1.4

:目的: 数学に関する演算に特化した機能を提供する
:利用できるバージョン: 1.4

..
    The :mod:`math` module implements many of the IEEE functions that would
    normally be found in the native platform C libraries for complex
    mathematical operations using floating point values, including
    logarithms and trigonometric operations.

:mod:`math` モジュールは、浮動小数点数、対数、三角法の演算を含む複雑な数学の演算のために、C 言語のネイティブライブラリで標準的に提供されている多くの IEEE 関数を実装します。

..
    Special Constants
    =================

特別な定数
==========

..
    Many math operations depend on special constants.  :mod:`math`
    includes values for π (pi) and e.

多くの数学の演算は、特別な定数に依存します。 :mod:`math` は π (パイ) や e の値を提供します。

.. include:: math_constants.py
   :literal:
   :start-after: #end_pymotw_header

..
    Both values are limited in precision only by the platform's floating
    point C library.

両方の定数の値の精度は、プラットフォームの浮動小数点数の C 言語ライブラリにのみ制限されます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'math_constants.py'))
.. }}}

::

	$ python math_constants.py
	
	π: 3.141592653589793115997963468544
	e: 2.718281828459045090795598298428

.. {{{end}}}

..
    Testing for Exceptional Values
    ==============================

例外値のテスト
==============

..
    Floating point calculations can result in two types of exceptional
    values.  ``INF`` ("infinity") appears when the *double* used to hold a
    floating point value overflows from a value with a large absolute
    value.

浮動小数点数の計算は、2つの例外値を導くことがあります。 ``INF`` ("無限大") は、 浮動小数点数の *double* 型のある値から巨大な絶対値をもつ値にオーバーフローするときに現れます。

.. include:: math_isinf.py
   :literal:
   :start-after: #end_pymotw_header

..
    When the exponent in this example grows large enough, the square of
    *x* no longer fits inside a *double*, and the value is recorded as
    infinite.

このサンプルの指数は、 *x* の2乗が *double* 型の範囲内に収まらないほど巨大な値になると、その値は無限大として記録されます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'math_isinf.py'))
.. }}}

::

	$ python math_isinf.py
	
	 e   x       x**2    isinf 
	---  ------  ------  ------
	  0  1.0     1.0     False 
	 20  1e+20   1e+40   False 
	 40  1e+40   1e+80   False 
	 60  1e+60   1e+120  False 
	 80  1e+80   1e+160  False 
	100  1e+100  1e+200  False 
	120  1e+120  1e+240  False 
	140  1e+140  1e+280  False 
	160  1e+160  inf     True  
	180  1e+180  inf     True  
	200  1e+200  inf     True  

.. {{{end}}}

..
    Not all floating point overflows result in ``INF`` values, however.
    Calculating an exponent with floating point values, in particular,
    raises :ref:`OverflowError <exceptions-OverflowError>` instead of
    preserving the ``INF`` result.

しかし、全ての浮動小数点数の値がオーバーフローすると ``INF`` の値になるというわけではありません。特に浮動小数点数の指数計算を行うと ``INF`` を保持するのではなく :ref:`OverflowError <exceptions-OverflowError>` を発生させます。

.. include:: math_overflow.py
   :literal:
   :start-after: #end_pymotw_header

..
    This discrepancy is caused by an implementation difference in the
    library used by C Python.

この不一致は、CPython が使用するライブラリの実装の違いが原因です。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'math_overflow.py'))
.. }}}

::

	$ python math_overflow.py
	
	x    = 1e+200
	x*x  = inf
	x**2 = (34, 'Result too large')

.. {{{end}}}

..
    Division operations using infinite values are undefined.  The result
    of dividing a number by infinity is ``NaN`` ("not a number").

無限大の値を使用する除算は未定義です。ある数を無限大で割ると ``NaN`` ("数字ではない") になります。

.. include:: math_isnan.py
   :literal:
   :start-after: #end_pymotw_header

..
    ``NaN`` does not compare as equal to any value, even itself, so to
    check for ``NaN`` you must use :func:`isnan`.

``NaN`` は、自分自身との比較も含め、どんな値と比較しても等しくないので、 ``NaN`` を調べるには :func:`isnan` を使用しなければなりません。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'math_isnan.py'))
.. }}}

::

	$ python math_isnan.py
	
	x = inf
	isnan(x) = False
	y = x / x = nan
	y == nan = False
	isnan(y) = True

.. {{{end}}}

..
    Converting to Integers
    ======================

整数への変換
============

..
    The :mod:`math` module includes three functions for converting
    floating point values to whole numbers.  Each takes a different
    approach, and will be useful in different circumstances.

:mod:`math` モジュールは、浮動小数点数の値から整数に変換する3つの関数を提供します。それぞれが別のアプローチを取り、様々な状況で役に立ちます。

..
    The simplest is :func:`trunc`, which truncates the digits following
    the decimal, leaving only the significant digits making up the whole
    number portion of the value.  :func:`floor` converts its input to the
    largest preceding integer, and :func:`ceil` (ceiling) produces the
    largest integer following sequentially after the input value.

最も簡単なのは :func:`trunc` で、ある値の整数部分の桁のみを残して、その小数部分の桁を切り捨てます。 :func:`floor` は入力値以下の最も大きな整数に変換し、 :func:`ceil` (天井値) は入力値以上の最も大きな整数を生成します。

.. include:: math_integers.py
   :literal:
   :start-after: #end_pymotw_header

..
    :func:`trunc` is equivalent to converting to :class:`int` directly.

:func:`trunc` は、直接 :class:`int` に変換するのと等価です。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'math_integers.py'))
.. }}}

::

	$ python math_integers.py
	
	  i     int   trunk  floor  ceil 
	-----  -----  -----  -----  -----
	 -1.5   -1.0   -1.0   -2.0   -1.0
	 -0.8    0.0    0.0   -1.0   -0.0
	 -0.5    0.0    0.0   -1.0   -0.0
	 -0.2    0.0    0.0   -1.0   -0.0
	  0.0    0.0    0.0    0.0    0.0
	  0.2    0.0    0.0    0.0    1.0
	  0.5    0.0    0.0    0.0    1.0
	  0.8    0.0    0.0    0.0    1.0
	  1.0    1.0    1.0    1.0    1.0

.. {{{end}}}

..
    Alternate Representations
    =========================

代替の表現
==========

..
    :func:`modf` takes a single floating point number and returns a tuple
    containing the fractional and whole number parts of the input value.

:func:`modf` は、1つの浮動小数点数を受け取り、その入力値から小数部と整数部に分けたタプルを返します。

.. include:: math_modf.py
   :literal:
   :start-after: #end_pymotw_header

..
    Both numbers in the return value are floats.

返り値のタプルに含まれる両方の値は float 型です。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'math_modf.py'))
.. }}}

::

	$ python math_modf.py
	
	0/2 = (0.0, 0.0)
	1/2 = (0.5, 0.0)
	2/2 = (0.0, 1.0)
	3/2 = (0.5, 1.0)
	4/2 = (0.0, 2.0)
	5/2 = (0.5, 2.0)

.. {{{end}}}

..
    :func:`frexp` returns the mantissa and exponent of a floating point
    number, and can be used to create a more portable representation of
    the value.

:func:`frexp` は、浮動小数点数の仮数と指数を返し、引数の値のより移植性の高い表現を作成するのに使用されます。

.. include:: math_frexp.py
   :literal:
   :start-after: #end_pymotw_header

..
    :func:`frexp` uses the formula ``x = m * 2**e``, and returns the
    values *m* and *e*.

:func:`frexp` は、数式 ``x = m * 2**e`` を導く *m* と *e* の値を返します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'math_frexp.py'))
.. }}}

::

	$ python math_frexp.py
	
	   x        m        e   
	-------  -------  -------
	   0.10     0.80       -3
	   0.50     0.50        0
	   4.00     0.50        3

.. {{{end}}}

..
    :func:`ldexp` is the inverse of :func:`frexp`.  

:func:`ldexp` は :func:`frexp` の逆の計算をします。

.. include:: math_ldexp.py
   :literal:
   :start-after: #end_pymotw_header

..
    Using the same formula as :func:`frexp`, :func:`ldexp` takes the
    mantissa and exponent values as arguments and returns a floating point
    number.

:func:`frexp` と同じ数式を用いて、 :func:`ldexp` は、仮数と指数の値を引数として受け取り、浮動小数点数の値を返します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'math_ldexp.py'))
.. }}}

::

	$ python math_ldexp.py
	
	   m        e        x   
	-------  -------  -------
	   0.80       -3     0.10
	   0.50        0     0.50
	   0.50        3     4.00

.. {{{end}}}

..
    Positive and Negative Signs
    ===========================

正負の符号
==========

..
    The absolute value of number is its value without a sign.  Use
    :func:`fabs` to calculate the absolute value of a floating point
    number.

数値の絶対値は符号をもたない値です。浮動小数点数の絶対値を計算するには :func:`fabs` を使用してください。

.. include:: math_fabs.py
   :literal:
   :start-after: #end_pymotw_header

..
    In practical terms, the absolute value of a :class:`float` is
    represented as a positive value.

実際には :class:`float` 型の絶対値は正の値として表現されます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'math_fabs.py'))
.. }}}

::

	$ python math_fabs.py
	
	1.1
	0.0
	0.0
	1.1

.. {{{end}}}

..
    To determine the sign of a value, either to give a set of values the
    same sign or simply for comparison, use :func:`copysign` to set the
    sign of a known good value.

ある値の符号を決めるには、与えられた値セットが同じ符号をもつ、またはシンプルに比較する目的であるなら、既知の値から符号をセットするために :func:`copysign` を使用してください。

.. include:: math_copysign.py
   :literal:
   :start-after: #end_pymotw_header

..
    An extra function like :func:`copysign` is needed because comparing
    NaN and -NaN directly with other values does not work.

:func:`copysign` のような拡張関数は、NaN と -NaN を他の値と直接的に比較すると正しく処理されないので必要です。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'math_copysign.py'))
.. }}}

::

	$ python math_copysign.py
	
	
	  f      s     < 0    > 0    = 0 
	-----  -----  -----  -----  -----
	 -1.0     -1  True   False  False
	  0.0      1  False  False  True 
	  1.0      1  False  True   False
	 -inf     -1  True   False  False
	  inf      1  False  True   False
	  nan     -1  False  False  False
	  nan      1  False  False  False

.. {{{end}}}

..
    Commonly Used Calculations
    ==========================

一般的によく使う計算
====================

..
    Representing precise values in binary floating point memory is
    challenging.  Some values cannot be represented exactly, and the more
    often a value is manipulated through repeated calculations, the more
    likely a representation error will be introduced.  :mod:`math`
    includes a function for computing the sum of a series of floating
    point numbers using an efficient algorithm that minimize such errors.

バイナリの浮動小数点数メモリに正確な値を表現することが挑戦されています。いくつかの値は、正確に表現することはできません。そして、繰り返しの計算を通して多くの値が操作され、表現エラーが発生する可能性が高くなります。 :mod:`math` は、そういったエラーを最小限に抑えるように効率化されたアルゴリズムを使用して、一連の浮動小数点数の和を計算する関数を提供します。

.. include:: math_fsum.py
   :literal:
   :start-after: #end_pymotw_header

..
    Given a sequence of ten values each equal to ``0.1``, the expected
    value for the sum of the sequence is ``1.0``.  Since ``0.1`` cannot be
    represented exactly as a floating point value, however, errors are
    introduced into the sum unless it is calculated with :func:`fsum`.

あるシーケンスの10個の値がそれぞれ ``0.1`` のとき、そのシーケンスの合計値は ``1.0`` になると予想されます。 ``0.1`` は浮動小数点数の値として正確な表現ではないので、 :func:`fsum` で計算しない限り、その和はエラーになります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'math_fsum.py'))
.. }}}

::

	$ python math_fsum.py
	
	Input values: [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
	sum()       : 0.99999999999999988898
	for-loop    : 0.99999999999999988898
	math.fsum() : 1.00000000000000000000

.. {{{end}}}

..
    :func:`factorial` is commonly used to calculate the number of
    permutations and combinations of a series of objects.  The factorial
    of a positive integer *n*, expressed ``n!``, is defined recursively as
    ``(n-1)! * n`` and stops with ``0! == 1``.

:func:`factorial` は、一般的に一連のオブジェクトの順列や組み合わせの数を計算するのに使用されます。正の整数 *n* の階乗は、 ``n!`` で表され、 ``(n-1)! * n`` として再帰的に定義されて ``0! == 1`` で止まります。

.. include:: math_factorial.py
   :literal:
   :start-after: #end_pymotw_header

..
    :func:`factorial` only works with whole numbers, but does accept
    :class:`float` arguments as long as they can be converted to an
    integer without losing value.

:func:`factorial` は整数でのみ動作しますが、値を失わずに整数に変換されるのであれば :class:`float` の引数を受け取ります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'math_factorial.py'))
.. }}}

::

	$ python math_factorial.py
	
	 0       1
	 1       1
	 2       2
	 3       6
	 4      24
	 5     120
	Error computing factorial(6.1): factorial() only accepts integral values

.. {{{end}}}

..
    :func:`gamma` is like :func:`factorial`, except it works with real
    numbers and the value is shifted down one (gamma is equal to ``(n -
    1)!``).

:func:`gamma` も実数で動作する点を除けば、 :func:`factorial` と同じように動作しますが、その値は1つシフトダウンされます (ガンマは ``(n - 1)!`` と等価です) 。

.. include:: math_gamma.py
   :literal:
   :start-after: #end_pymotw_header

..
    Since zero causes the start value to be negative, it is not allowed.

ゼロは初期値が負の値から始まるので計算できません。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'math_gamma.py'))
.. }}}

::

	$ python math_gamma.py
	
	Error computing gamma(0): math domain error
	1.1    0.95
	2.2    1.10
	3.3    2.68
	4.4   10.14
	5.5   52.34
	6.6  344.70

.. {{{end}}}

..
    :func:`lgamma` returns the natural logarithm of the absolute value of
    Gamma for the input value.

:func:`lgamma` は、入力値のためにガンマの絶対値の自然対数を返します。

.. include:: math_lgamma.py
   :literal:
   :start-after: #end_pymotw_header

..
    Using :func:`lgamma` retains more precision than calculating the
    logarithm separately using the results of :func:`gamma`.

:func:`lgamma` を使用した方が、 :func:`gamma` の結果を使用して別々にその対数を計算するよりも高い精度を保持します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'math_lgamma.py'))
.. }}}

::

	$ python math_lgamma.py
	
	Error computing lgamma(0): math domain error
	1.1  -0.04987244125984036103  -0.04987244125983997245
	2.2  0.09694746679063825923  0.09694746679063866168
	3.3  0.98709857789473387513  0.98709857789473409717
	4.4  2.31610349142485727469  2.31610349142485727469
	5.5  3.95781396761871651080  3.95781396761871606671
	6.6  5.84268005527463252236  5.84268005527463252236

.. {{{end}}}

..
    The modulo operator (``%``) computes the remainder of a division
    expression (i.e., ``5 % 2 = 1``).  The operator built into the
    language works well with integers but, as with so many other floating
    point operations, intermediate calculations cause representational
    issues that result in a loss of data.  :func:`fmod` provides a more
    accurate implementation for floating point values.

モジュロ演算子 (``%``) は、除算の余りを計算します (例えば ``5 % 2 = 1`` ) 。この演算子は整数でうまく計算するように言語内に組み込まれていますが、その他の多くの浮動小数点数の計算と同様に、中間の計算で結果的にデータを失ってしまう表現の問題を引き起こします。 :func:`fmod` は、浮動小数点数のためにより正確な計算の実装を提供します。

.. include:: math_fmod.py
   :literal:
   :start-after: #end_pymotw_header

..
    A potentially more frequent source of confusion is the fact that the
    algorithm used by :mod:`fmod` for computing modulo is also different
    from that used by ``%``, so the sign of the result is different.
    mixed-sign inputs.

潜在的によく混乱するのは、モジュロ演算のために :mod:`fmod` が使用するアルゴリズムが ``%`` が使用するのと違っているという事実です。そのため、その結果の符号は違います。符号が混在した入力値を与えます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'math_fmod.py'))
.. }}}

::

	$ python math_fmod.py
	
	 x     y      %    fmod 
	----  ----  -----  -----
	 5.0   2.0   1.00   1.00
	 5.0  -2.0  -1.00   1.00
	-5.0   2.0   1.00  -1.00

.. {{{end}}}

..
    Exponents and Logarithms
    ========================

指数と対数
==========

..
    Exponential growth curves appear in economics, physics, and other
    sciences.  Python has a built-in exponentiation operator ("``**``"),
    but :func:`pow` can be useful when you need to pass a callable
    function as an argument.

指数関数的な曲線は、経済学、物理学、その他の科学の分野においても見られます。Python は組み込みのべき乗演算子 ("``**``") がありますが、呼び出し可能な関数に引数として渡す必要があるときは :func:`pow` が便利です。

.. include:: math_pow.py
   :literal:
   :start-after: #end_pymotw_header

..
    Raising ``1`` to any power always returns ``1.0``, as does raising any
    value to a power of ``0.0``.  Most operations on the not-a-number
    value ``nan`` return ``nan``.  If the exponent is less than ``1``,
    :func:`pow` computes a root.

任意の数を ``0.0`` 乗するのと同様に、 ``1`` を任意の数でべき乗しても ``1.0`` を返します。数字ではない値 ``nan`` について、ほとんどの演算は ``nan`` を返します。 ``1`` よりも小さい指数なら :func:`pow` はルート(√)を計算します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'math_pow.py'))
.. }}}

::

	$ python math_pow.py
	
	  2.0 ** 3.000 =  8.000
	  2.1 ** 3.200 = 10.742
	  1.0 ** 5.000 =  1.000
	  2.0 ** 0.000 =  1.000
	  2.0 **   nan =    nan
	  9.0 ** 0.500 =  3.000
	 27.0 ** 0.333 =  3.000

.. {{{end}}}

..
    Since square roots (exponent of ``1/2``) are used so frequently, there
    is a separate function for computing them.

よく使う平方根 (``1/2`` の指数) を計算するには別の関数があります。

.. include:: math_sqrt.py
   :literal:
   :start-after: #end_pymotw_header

..
    Computing the square roots of negative numbers requires *complex
    numbers*, which are not handled by :mod:`math`.  Any attempt to
    calculate a square root of a negative value results in a
    :ref:`ValueError <exceptions-ValueError>`.

負の数の平方根を計算するには、 :mod:`math` では処理できない *複素数* を必要とします。負の数の平方根を計算しようとすると :ref:`ValueError <exceptions-ValueError>` が発生します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'math_sqrt.py'))
.. }}}

::

	$ python math_sqrt.py
	
	3.0
	1.73205080757
	Cannot compute sqrt(-1): math domain error

.. {{{end}}}

..
    The logarithm function finds *y* where ``x = b ** y``.  By default,
    :func:`log` computes the natural logarithm (the base is *e*).  If a
    second argument is provided, that value is used as the base.

対数関数は ``x = b ** y`` という式の *y* を導きます。デフォルトでは、 :func:`log` は自然対数 (底は *e*) を計算します。第2引数が指定された場合、その値は底として利用されます。

.. include:: math_log.py
   :literal:
   :start-after: #end_pymotw_header

..
    Logarithms where *x* is less than one yield negative results.

*x* が1より小さい対数は、負の数を導きます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'math_log.py'))
.. }}}

::

	$ python math_log.py
	
	2.07944154168
	3.0
	-1.0

.. {{{end}}}

..
    There are two variations of :func:`log`.  Given floating point
    representation and rounding errors the computed value produced by
    ``log(x, b)`` has limited accuracy, especially for some bases.
    :func:`log10` computes ``log(x, 10)``, using a more accurate algorithm
    than :func:`log`.

:func:`log` には2つの関数があります。浮動小数点表現と丸め誤差の値を ``log(x, b)`` に渡して生成された値は、特に底の精度が制限されます。 :func:`log10` は、 :func:`log` より正確なアルゴリズムを用いて ``log(x, 10)`` を計算します。

.. include:: math_log10.py
   :literal:
   :start-after: #end_pymotw_header

..
    The lines in the output with trailing ``*`` highlight the inaccurate
    values.

``*`` が最後に付けられた出力結果の行は間違った値です。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'math_log10.py'))
.. }}}

::

	$ python math_log10.py
	
	i        x              accurate             inaccurate       mismatch
	--  ------------  --------------------  --------------------  --------
	 0           1.0  0.000000000000000000  0.000000000000000000       
	 1          10.0  1.000000000000000000  1.000000000000000000       
	 2         100.0  2.000000000000000000  2.000000000000000000       
	 3        1000.0  3.000000000000000000  2.999999999999999556    *  
	 4       10000.0  4.000000000000000000  4.000000000000000000       
	 5      100000.0  5.000000000000000000  5.000000000000000000       
	 6     1000000.0  6.000000000000000000  5.999999999999999112    *  
	 7    10000000.0  7.000000000000000000  7.000000000000000000       
	 8   100000000.0  8.000000000000000000  8.000000000000000000       
	 9  1000000000.0  9.000000000000000000  8.999999999999998224    *  

.. {{{end}}}

..
    :func:`log1p` calculates the Newton-Mercator series (the natural
    logarithm of ``1+x``).

:func:`log1p` は、ニュートンメルカトル級数 (``1+x`` の自然対数) を計算します。

.. include:: math_log1p.py
   :literal:
   :start-after: #end_pymotw_header

..
    :func:`log1p` is more accurate for values of *x* very close to zero
    because it uses an algorithm that compensates for round-off errors
    from the initial addition.

:func:`log1p` は、ゼロにとても近い *x* の、より正確な値を計算します。それは初期値からの丸め誤差を補償するアルゴリズムを使用するからです。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'math_log1p.py'))
.. }}}

::

	$ python math_log1p.py
	
	x       : 1e-25
	1 + x   : 1.0
	log(1+x): 0.0
	log1p(x): 1e-25

.. {{{end}}}

..
    :func:`exp` computes the exponential function (``e**x``).  

:func:`exp` は指数関数を計算します (``e**x``) 。

.. include:: math_exp.py
   :literal:
   :start-after: #end_pymotw_header

..
    As with other special-case functions, it uses an algorithm that
    produces more accurate results than the general-purpose equivalent
    ``math.pow(math.e, x)``.

その他の特殊な関数と同様に、汎用目的で等価な ``math.pow(math.e, x)`` よりも正確な値を計算するアルゴリズムを使用します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'math_exp.py'))
.. }}}

::

	$ python math_exp.py
	
	7.38905609893064951876
	7.38905609893064951876
	7.38905609893065040694

.. {{{end}}}

..
    :func:`expm1` is the inverse of :func:`log1p`, and calculates ``e**x -
    1``.

:func:`expm1` は :func:`log1p` の逆にあたる ``e**x - 1`` を計算します。

.. include:: math_expm1.py
   :literal:
   :start-after: #end_pymotw_header

..
    As with :func:`log1p`, small values of *x* lose precision when the
    subtraction is performed separately.

:func:`log1p` と同様に *x* の小さな値は、その引き算が別々に計算されるときに精度が失われます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'math_expm1.py'))
.. }}}

::

	$ python math_expm1.py
	
	1e-25
	0.0
	1e-25

.. {{{end}}}

..
    Angles
    ======

角度
====

..
    Although degrees are more commonly used in everyday discussions of
    angles, radians are the standard unit of angular measure in science
    and math.  A radian is the angle created by two lines intersecting at
    the center of a circle, with their ends on the circumference of the
    circle spaced one radius apart.  

日常の議論では、度の方が角度よりも一般的に使用されますが、ラジアンは科学と数学の世界で角度を測定する標準単位です。ラジアンは、円周上の半径と同じ長さをもつ範囲において円の中心で交差する2つの線で作成された角度です。

..
    The circumference is calculated as ``2πr``, so there is a relationship
    between radians and π, a value that shows up frequently in
    trigonometric calculations.  That relationship leads to radians being
    used in trigonometry and calculus, because they result in more compact
    formulas.

円周は ``2πr`` として計算されるので、ラジアンとパイ (π) は関連があり、それは三角法の計算でよく示される値です。その関連はもっと小さな公式になるので三角法と計算で使用されるラジアンを導きます。

..
    To convert from degrees to radians, use :func:`radians`.

度からラジアンへ変換するには :func:`radians` を使用してください。

.. include:: math_radians.py
   :literal:
   :start-after: #end_pymotw_header

..
    The formula for the conversion is ``rad = deg * π / 180``.

変換の公式は ``rad = deg * π / 180`` です。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'math_radians.py'))
.. }}}

::

	$ python math_radians.py
	
	Degrees  Radians  Expected
	-------  -------  -------
	      0     0.00     0.00
	     30     0.52     0.52
	     45     0.79     0.79
	     60     1.05     1.05
	     90     1.57     1.57
	    180     3.14     3.14
	    270     4.71     4.71
	    360     6.28     6.28

.. {{{end}}}

..
    To convert from radians to degrees, use :func:`degrees`.

ラジアンから度へ変換するには :func:`degrees` を使用してください。

.. include:: math_degrees.py
   :literal:
   :start-after: #end_pymotw_header

..
    The formula is ``deg = rad * 180 / π``.

公式は ``deg = rad * 180 / π`` です。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'math_degrees.py'))
.. }}}

::

	$ python math_degrees.py
	
	Radians   Degrees   Expected
	--------  --------  --------
	    0.00      0.00      0.00
	    0.52     30.00     30.00
	    0.79     45.00     45.00
	    1.05     60.00     60.00
	    1.57     90.00     90.00
	    3.14    180.00    180.00
	    4.71    270.00    270.00
	    6.28    360.00    360.00

.. {{{end}}}

..
    Trigonometry
    ============

三角法
======

..
    Trigonometric functions relate angles in a triangle to the lengths of
    its sides.  They show up in formulas with periodic properties such as
    harmonics, circular motion, or when dealing with angles.

三角関数は、その辺の長さに対する三角形の角度に関連しています。調和や円運動か、角度を扱うときといった周期的性質をもつ公式で示されます。

.. note::

    .. All of the trigonometric functions in the standard library take
       angles expressed as radians.

    標準ライブラリの全ての三角関数は、ラジアンで表される角度を受け取ります。

..
    Given an angle in a right triangle, the *sine* is the ratio of the
    length of the side opposite the angle to the hypotenuse (``sin A =
    opposite/hypotenuse``).  The *cosine* is the ratio of the length of
    the adjacent side to the hypotenuse (``cos A = adjacent/hypotenuse``).
    And the *tangent* is the ratio of the opposite side to the adjacent
    side (``tan A = opposite/adjacent``).

直角三角形のある角度が与えられたとき、 *正弦 (sine)* は、斜辺に対する角の辺の長さの比です (``sin A = opposite/hypotenuse``) 。 *余弦 (cosine)* は、斜辺に隣接する辺の長さの比です (``cos A = adjacent/hypotenuse``) 。そして *正接 (tangent)* は、隣接する辺の反対側の辺の比です (``tan A = opposite/adjacent``) 。

.. include:: math_trig.py
   :literal:
   :start-after: #end_pymotw_header

..
    The tangent can also be defined as the ratio of the sine of the angle
    to its cosine, and since the cosine is 0 for π/2 and 3π/2 radians, the
    tangent is infinite.

正接 (tangent) は、その余弦 (cosine) に対する角の正弦 (sine) としても定義されます。そして、余弦 (cosine) は、π/2 や 3π/2 ラジアンに対して 0 なので、正接 (tangent) は無限大です。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'math_trig.py'))
.. }}}

::

	$ python math_trig.py
	
	Degrees  Radians  Sine     Cosine    Tangent
	-------  -------  -------  --------  -------
	   0.00     0.00     0.00     1.00     0.00
	  30.00     0.52     0.50     0.87     0.58
	  60.00     1.05     0.87     0.50     1.73
	  90.00     1.57     1.00     0.00      inf
	 120.00     2.09     0.87    -0.50    -1.73
	 150.00     2.62     0.50    -0.87    -0.58
	 180.00     3.14     0.00    -1.00    -0.00
	 210.00     3.67    -0.50    -0.87     0.58
	 240.00     4.19    -0.87    -0.50     1.73
	 270.00     4.71    -1.00    -0.00      inf
	 300.00     5.24    -0.87     0.50    -1.73
	 330.00     5.76    -0.50     0.87    -0.58
	 360.00     6.28    -0.00     1.00    -0.00

.. {{{end}}}

..
    Given a point (*x*, *y*), the length of the hypotenuse for the
    triangle between the points [(0, 0), (*x*, 0), (*x*, *y*)] is
    ``(x**2 + y**2) ** 1/2``, and can be computed with :func:`hypot`.

座標 (*x*, *y*) が与えられたとき、[(0, 0), (*x*, 0), (*x*, *y*)] の座標間にある三角形の斜辺の長さは、 ``(x**2 + y**2) ** 1/2`` です。これは :func:`hypot` でも計算できます。

.. include:: math_hypot.py
   :literal:
   :start-after: #end_pymotw_header

..
    Points on the circle always have hypotenuse == ``1``.

円になるのは、必ず hypotenuse == ``1`` になります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'math_hypot.py'))
.. }}}

::

	$ python math_hypot.py
	
	   X        Y     Hypotenuse
	-------  -------  ----------
	   1.00     1.00     1.41
	  -1.00    -1.00     1.41
	   1.41     1.41     2.00
	   3.00     4.00     5.00
	   0.71     0.71     1.00
	   0.50     0.87     1.00

.. {{{end}}}

..
    The same function can be used to find the distance between two points.

2つの座標間の距離を調べるために同じ関数が使用できます。

.. include:: math_distance_2_points.py
   :literal:
   :start-after: #end_pymotw_header

..
    Use the difference in the *x* and *y* values to move one endpoint to
    the origin, and then pass the results to :func:`hypot`.

原点から端点へ移動する *x* と *y* の距離を計算してから :func:`hypot` へその結果を渡してください。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'math_distance_2_points.py'))
.. }}}

::

	$ python math_distance_2_points.py
	
	   X1        Y1        X2        Y2     Distance
	--------  --------  --------  --------  --------
	    5.00      5.00      6.00      6.00      1.41
	   -6.00     -6.00     -5.00     -5.00      1.41
	    0.00      0.00      3.00      4.00      5.00
	   -1.00     -1.00      2.00      3.00      5.00

.. {{{end}}}

..
    :mod:`math` also defines inverse trigonometric functions.

さらに :mod:`math` は逆三角関数も定義します。

.. include:: math_inverse_trig.py
   :literal:
   :start-after: #end_pymotw_header

..
    ``1.57`` is roughly equal to ``π/2``, or 90 degrees, the angle at
    which the sine is 1 and the cosine is 0.

``1.57`` は、およそ ``π/2`` または90度です。それは正弦 (sine) が 1 且つ余弦 (cosine) が 0 の角度です。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'math_inverse_trig.py'))
.. }}}

::

	$ python math_inverse_trig.py
	
	arcsine(0.0)    =  0.00
	arccosine(0.0)  =  1.57
	arctangent(0.0) =  0.00
	
	arcsine(0.5)    =  0.52
	arccosine(0.5)  =  1.05
	arctangent(0.5) =  0.46
	
	arcsine(1.0)    =  1.57
	arccosine(1.0)  =  0.00
	arctangent(1.0) =  0.79
	

.. {{{end}}}

.. atan2

..
    Hyperbolic Functions
    ====================

双曲線関数
==========

..
    Hyperbolic functions appear in linear differential equations and are
    used when working with electromagnetic fields, fluid dynamics, special
    relativity, and other advanced physics and mathematics.

線形微分方程式に見られる双曲線関数は、電磁界、流体力学、特殊相対性理論、その他の高度な物理学と数学の世界で使用されます。

.. include:: math_hyperbolic.py
   :literal:
   :start-after: #end_pymotw_header

..
    Whereas the cosine and sine functions enscribe a circle, the
    hyperbolic cosine and hyperbolic sine form half of a hyperbola.

余弦 (cosine) と正弦 (sine) の関数は円を描くのに対して、双曲線余弦と双曲線正弦フォームは双曲線の半分です。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'math_hyperbolic.py'))
.. }}}

::

	$ python math_hyperbolic.py
	
	  X      sinh    cosh    tanh 
	------  ------  ------  ------
	0.0000  0.0000  1.0000  0.0000
	0.2000  0.2013  1.0201  0.1974
	0.4000  0.4108  1.0811  0.3799
	0.6000  0.6367  1.1855  0.5370
	0.8000  0.8881  1.3374  0.6640
	1.0000  1.1752  1.5431  0.7616

.. {{{end}}}

..
    Inverse hyperbolic functions :func:`acosh`, :func:`asinh`, and
    :func:`atanh` are also available.

逆双曲線関数 :func:`acosh`, :func:`asinh`, :func:`atanh` も利用できます。

..
    Special Functions
    =================

特殊関数
========

..
    The Gauss Error function is used in statistics.

統計では、ガウスエラー関数が使用されます。

.. include:: math_erf.py
   :literal:
   :start-after: #end_pymotw_header

..
    Notice that ``erf(-x) == -erf(x)``.

``erf(-x) == -erf(x)`` であることに注意してください。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'math_erf.py'))
.. }}}

::

	$ python math_erf.py
	
	  x    erf(x) 
	-----  -------
	-3.00  -1.0000
	-2.00  -0.9953
	-1.00  -0.8427
	-0.50  -0.5205
	-0.25  -0.2763
	 0.00   0.0000
	 0.25   0.2763
	 0.50   0.5205
	 1.00   0.8427
	 2.00   0.9953
	 3.00   1.0000

.. {{{end}}}

..
    The complimentary error function is ``1 - erf(x)``.

補足のエラー関数は ``1 - erf(x)`` です。

.. include:: math_erfc.py
   :literal:
   :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'math_erfc.py'))
.. }}}

::

	$ python math_erfc.py
	
	  x    erfc(x)
	-----  -------
	-3.00   2.0000
	-2.00   1.9953
	-1.00   1.8427
	-0.50   1.5205
	-0.25   1.2763
	 0.00   1.0000
	 0.25   0.7237
	 0.50   0.4795
	 1.00   0.1573
	 2.00   0.0047
	 3.00   0.0000

.. {{{end}}}


.. seealso::

    `math <http://docs.python.org/library/math.html>`_
        .. The standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント

    `IEEE floating point arithmetic in Python <http://www.johndcook.com/blog/2009/07/21/ieee-arithmetic-python/>`__
        .. Blog post by John Cook about how special values arise and are
           dealt with when doing math in Python.

        John Cook による Python で数学をするときに特殊な値の発生とその対処方法について書かれたブログの記事

    `SciPy <http://scipy.org/>`_
        .. Open source libraryes for scientific and mathematical
           calculations in Python.

        Python で科学技術計算や数学のためのオープンソースライブラリ
