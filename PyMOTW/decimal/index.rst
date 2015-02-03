..
    ========================================
    decimal -- Fixed and floating point math
    ========================================

=====================================
decimal -- 固定小数点数と浮動小数点数
=====================================

..
    :synopsis: Fixed and floating point math

.. module:: decimal
    :synopsis: 固定小数点数と浮動小数点数

..
    :Purpose: Decimal arithmetic using fixed and floating point numbers
    :Available In: 2.4 and later

:目的: 固定小数点数と浮動小数点数を扱う10進数の計算
:利用できるバージョン: 2.4 以上

..
    The :mod:`decimal` module implements fixed and floating point
    arithmetic using the model familiar to most people, rather than the
    IEEE floating point version implemented by most computer hardware.  A
    Decimal instance can represent any number exactly, round up or down,
    and apply a limit to the number of significant digits.

:mod:`decimal` モジュールは、コンピュータのハードウェアが実装した IEEE の浮動小数点数より、人間にとって分かりやすいモデルの固定小数点数と浮動小数点数を実装します。Decimal インスタンスは、任意の数を正確に表したり、端数の切り上げや切り下げ、有効桁数の制限を設けます。

Decimal
=======

..
    Decimal values are represented as instances of the :class:`Decimal`
    class.  The constructor takes as argument an integer, or a string.
    Floating point numbers must be converted to a string before being used
    to create a :class:`Decimal`, letting the caller explicitly deal with
    the number of digits for values that cannot be expressed exactly using
    hardware floating point representations.

Decimal の値は :class:`Decimal` クラスのインスタンスとして表されます。コンストラクタの引数は整数か文字列を受け取ります。 :class:`Decimal` で浮動小数点数を表すには、その引数を文字列に変換しなければなりません。そして :class:`Decimal` は、ハードウェアの浮動小数点数では正確に表せない桁の値を呼び出し側で明示的に指定できます。

.. include:: decimal_create.py
    :literal:
    :start-after: #end_pymotw_header

..
    Notice that the floating point value of ``0.1`` is not represented as
    an exact value, so the representation as a float is different from the
    Decimal value.

``0.1`` という値の浮動小数点数は、厳密な値の表現ではないので、その浮動小数表現は Decimal の値とは違うことに注意してください。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'decimal_create.py'))
.. }}}

::

	$ python decimal_create.py
	
	Input                Output              
	-------------------- --------------------
	5                    5                   
	3.14                 3.14                
	0.1                  0.1                 

.. {{{end}}}

..
    Less conveniently, Decimals can also be created from tuples containing
    a sign flag (``0`` for positive, ``1`` for negative), a tuple of
    digits, and an integer exponent.

あまり使い勝手が良くないですが、Decimal は符号のフラグ (``0`` は正, ``1`` は負)、それぞれの桁の値を表すタプル、整数の指数の3つの値をもつタプルからも作成されます。

.. include:: decimal_tuple.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'decimal_tuple.py'))
.. }}}

::

	$ python decimal_tuple.py
	
	Input  : (1, (1, 1), -2)
	Decimal: -0.11

.. {{{end}}}

..
    Arithmetic
    ==========

計算
====

..
    Decimal overloads the simple arithmetic operators so once you have a
    value you can manipulate it in much the same way as the built-in
    numeric types.

Decimal は、単純な算術演算子をオーバーロードするので、ある値が与えられたときに組み込みの数値型とほぼ同じようにその値を計算します。

.. include:: decimal_operators.py
    :literal:
    :start-after: #end_pymotw_header

..
    Decimal operators also accept integer arguments, but floating point
    values must be converted to Decimal instances.

また Decimal の演算子は整数を受け取って計算できますが、浮動小数の場合は Decimal インスタンスに変換する必要があります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'decimal_operators.py'))
.. }}}

::

	$ python decimal_operators.py
	
	a     = 5.1
	b     = 3.14
	c     = 4
	d     = 3.14
	
	a + b = 8.24
	a - b = 1.96
	a * b = 16.014
	a / b = 1.624203821656050955414012739
	
	a + c = 9.1
	a - c = 1.1
	a * c = 20.4
	a / c = 1.275
	
	a + d = unsupported operand type(s) for +: 'Decimal' and 'float'

.. {{{end}}}

..
    Logarithms
    ==========

対数
====

..
    Beyond basic arithmetic, Decimal includes methods to find the base 10
    and natural logarithms.

基本的な計算に加えて、自然対数や10を底とする常用対数を調べるメソッドも提供します。

.. include:: decimal_log.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'decimal_log.py'))
.. }}}

::

	$ python decimal_log.py
	
	d     : 100
	log10 : 2
	ln    : 4.605170185988091368035982909

.. {{{end}}}

..
    Special Values
    ==============

特殊な値
========

..
    In addition to the expected numerical values, :class:`Decimal` can
    represent several special values, including positive and negative
    values for infinity, "not a number", and zero.

期待される数値表現に加えて、 :class:`Decimal` は、正負の無限大、"数値ではない"、ゼロを含む特殊な値を表現できます。

.. include:: decimal_special.py
    :literal:
    :start-after: #end_pymotw_header

..
    Adding to infinite values returns another infinite value.  Comparing
    for equality with NaN always returns False and comparing for
    inequality always returns true.  Comparing for sort order against NaN
    is undefined and results in an error.

無限大に値を加算すると、別の無限大の値を返します。NaN と等式で比較すると必ず False を返し、不等式で比較すると必ず True を返します。NaN に対してソートの比較を行うと、未定義のエラーが発生します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'decimal_special.py'))
.. }}}

::

	$ python decimal_special.py
	
	Infinity -Infinity
	NaN -NaN
	0 -0
	
	Infinity + 1: Infinity
	-Infinity + 1: -Infinity
	False
	True

.. {{{end}}}

..
    Context
    =======

コンテキスト
============

..
    So far all of the examples have used the default behaviors of the
    decimal module. It is possible to override settings such as the
    precision maintained, how rounding is performed, error handling,
    etc. All of these settings are maintained via a *context*.  Contexts
    can be applied for all Decimal instances in a thread or locally within
    a small code region.

これまでの全てのサンプルは、 :mod:`decimal` モジュールのデフォルトの処理を使用してきました。保持される精度、丸め、エラー処理といった設定は上書きできます。こういった全ての設定は *コンテキスト* 経由で行われます。コンテキストは、ローカルの小さなコード内か、スレッド内の全ての Decimal インスタンスに適用されます。

..
    Current Context
    ---------------

カレントコンテキスト
--------------------

..
    To retrieve the current global context, use ``getcontext()``.

カレントのグローバルコンテキストを取り出すには ``getcontext()`` を使用してください。

.. include:: decimal_getcontext.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'decimal_getcontext.py'))
.. }}}

::

	$ python decimal_getcontext.py
	
	Context(prec=28, rounding=ROUND_HALF_EVEN, Emin=-999999999, Emax=999999999, capitals=1, flags=[], traps=[DivisionByZero, Overflow, InvalidOperation])

.. {{{end}}}

..
    Precision
    ---------

精度
----

..
    The *prec* attribute of the context controls the precision maintained
    for new values created as a result of arithmetic.  Literal values are
    maintained as described.

コンテキストの *prec* 属性は、計算の結果として生成される新たな値が保持する精度を制御します。リテラル値は前節で説明したように保持されます。

.. include:: decimal_precision.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'decimal_precision.py'))
.. }}}

::

	$ python decimal_precision.py
	
	0 : 0.123456 0
	1 : 0.123456 0.1
	2 : 0.123456 0.12
	3 : 0.123456 0.123

.. {{{end}}}

..
    Rounding
    --------

丸め
----

..
    There are several options for rounding to keep values within the
    desired precision.

必要な精度の範囲内に値が収まるように丸めのオプションがあります。

ROUND_CEILING
  .. Always round upwards towards infinity.

  常に正の無限大へ切り上げて丸める

ROUND_DOWN
  .. Always round toward zero.

  常にゼロ方向に丸める

ROUND_FLOOR
  .. Always round down towards negative infinity.

  常に負の無限大へ丸める

ROUND_HALF_DOWN
  .. Rounds away from zero if the last significant digit is greater than
     or equal to 5, otherwise toward zero.

  最後の桁を五捨六入して丸める

ROUND_HALF_EVEN
  .. Like ROUND_HALF_DOWN except that if the value is 5 then the
     preceding digit is examined.  Even values cause the result to be
     rounded down and odd digits cause the result to be rounded up.

  ROUND_HALF_DOWN と同じように処理されますが、最後の桁の値が 5 の場合、精度の桁を調べて、偶数なら切り捨て、奇数なら切り上げる

ROUND_HALF_UP
  .. Like ROUND_HALF_DOWN except if the last significant digit is 5 the
     value is rounded away from zero.

  ROUND_HALF_DOWN と同じように処理されますが、最後の桁を四捨五入する

ROUND_UP
  .. Round away from zero.

  ゼロから遠い値に丸める

ROUND_05UP
  .. Round away from zero if the last digit is ``0`` or ``5``, otherwise
     towards zero.

  最後の桁が ``0`` か ``5`` ならゼロから遠い値へ、それ以外はゼロに丸める

.. include:: decimal_rounding.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'decimal_rounding.py'))
.. }}}

::

	$ python decimal_rounding.py
	
	POSITIVES:
	
	                      1/8 (1)    1/8 (2)    1/8 (3)  
	                     ---------- ---------- ----------
	ROUND_CEILING        0.2        0.13       0.125     
	ROUND_DOWN           0.1        0.12       0.125     
	ROUND_FLOOR          0.1        0.12       0.125     
	ROUND_HALF_DOWN      0.1        0.12       0.125     
	ROUND_HALF_EVEN      0.1        0.12       0.125     
	ROUND_HALF_UP        0.1        0.13       0.125     
	ROUND_UP             0.2        0.13       0.125     
	ROUND_05UP           0.1        0.12       0.125     
	
	NEGATIVES:
	                      -1/8 (1)   -1/8 (2)   -1/8 (3) 
	                     ---------- ---------- ----------
	ROUND_CEILING        -0.1       -0.12      -0.125    
	ROUND_DOWN           -0.1       -0.12      -0.125    
	ROUND_FLOOR          -0.2       -0.13      -0.125    
	ROUND_HALF_DOWN      -0.1       -0.12      -0.125    
	ROUND_HALF_EVEN      -0.1       -0.12      -0.125    
	ROUND_HALF_UP        -0.1       -0.13      -0.125    
	ROUND_UP             -0.2       -0.13      -0.125    
	ROUND_05UP           -0.1       -0.12      -0.125    

.. {{{end}}}

..
    Local Context
    -------------

ローカルコンテキスト
--------------------

..
    Using Python 2.5 or later you can also apply the context to a subset
    of your code using the ``with`` statement and a context manager.

Python 2.5 以上を使用することで、さらに ``with`` 文とコンテキストマネージャでコードのサブセットに対してコンテキストを適用することもできます。

.. include:: decimal_context_manager.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'decimal_context_manager.py'))
.. }}}

::

	$ python decimal_context_manager.py
	
	Local precision: 2
	3.14 / 3 = 1.0
	
	Default precision: 28
	3.14 / 3 = 1.046666666666666666666666667

.. {{{end}}}

..
    Per-Instance Context
    --------------------

インスタンスごとのコンテキスト
------------------------------

..
    Contexts can be used to construct Decimal instances, applying the precision and rounding arguments to the conversion from the input type.  This lets your application select the precision of constant values separately from the precision of user data.

コンテキストは、精度の適用して入力の型から引数を丸めるように変換しながら、Decimal インスタンス作成するのに使用できます。これによりアプリケーションは、ユーザデータの精度から定数の値の精度を分離して選択できます。

.. include:: decimal_instance_context.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'decimal_instance_context.py'))
.. }}}

::

	$ python decimal_instance_context.py
	
	PI: 3.14
	RESULT: 6.3114

.. {{{end}}}

..
    Threads
    -------

スレッド
--------

..
    The "global" context is actually thread-local, so each thread can potentially be configured using different values.

"グローバル" コンテキストは、実際にはスレッドローカルなので、それぞれのスレッドは潜在的に違う値を設定できます。

.. include:: decimal_thread_context.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'decimal_thread_context.py'))
.. }}}

::

	$ python decimal_thread_context.py
	
	1 	4
	2 	3.9
	3 	3.87
	4 	3.875
	5 	3.8748

.. {{{end}}}


.. seealso::

    `decimal <http://docs.python.org/library/decimal.html>`_
        .. The standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント

    `Wikipedia: Floating Point <http://en.wikipedia.org/wiki/Floating_point>`_
        .. Article on floating point representations and arithmetic.

        浮動小数点数表現と数値に関する記事
