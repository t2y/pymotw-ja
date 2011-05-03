..
    =============================
    fractions -- Rational Numbers
    =============================

===================
fractions -- 有理数
===================

..
    :synopsis: Implements a class for working with rational numbers.

.. module:: fractions
    :synopsis: 有理数を扱うクラスを提供する

..
    :Purpose: Implements a class for working with rational numbers.
    :Available In: 2.6 and later

:目的: 有理数を扱うクラスを提供する
:利用できるバージョン: 2.6 以上

..
    The Fraction class implements numerical operations for rational numbers based on the API defined by :class:`Rational` in :mod:`numbers`.

Fraction クラスは、 :mod:`numbers` モジュールの :class:`Rational` クラスで定義されている API に基づいた有理数の計算を実装します。

..
    Creating Fraction Instances
    ===========================

Fraction インスタンスを作成する
===============================

..
    As with :mod:`decimal`, new values can be created in several ways.  One easy way is to create them from separate numerator and denominator values:

:mod:`decimal` と同様に、複数の方法で新たな値が作成されます。簡単な方法の1つは、別々に与えた分子と分母の値から作成することです。

.. include:: fractions_create_integers.py
    :literal:
    :start-after: #end_pymotw_header

..
    The lowest common denominator is maintained as new values are computed.

新たな値として最小の共通分母を保持して計算されます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'fractions_create_integers.py'))
.. }}}
.. {{{end}}}

..
    Another way to create a Fraction is using a string representation of ``<numerator> / <denominator>``:

別の方法としては、 ``<分子> / <分母>`` の文字列表現で Fraction インスタンスを作成します。

.. include:: fractions_create_strings.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'fractions_create_strings.py'))
.. }}}
.. {{{end}}}

..
    Strings can also use the more usual decimal or floating point notation of ``[<digits>].[<digits>]``.

さらに、より一般的な10進数表現、または ``[<digits>].[<digits>]`` の浮動小数点表現を使用することもできます。

.. include:: fractions_create_strings_floats.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'fractions_create_strings_floats.py'))
.. }}}
.. {{{end}}}

..
    There are class methods for creating Fraction instances directly from other representations of rational values such as float or :mod:`decimal`.

float 型または :mod:`decimal` で表される有理数から直接、Fraction インスタンスを作成するクラスメソッドがあります。

.. include:: fractions_from_float.py
    :literal:
    :start-after: #end_pymotw_header

..
    Notice that for floating point values that cannot be expressed exactly the rational representation may yield unexpected results.

有理数では正確に表せない浮動小数の値は予想外の結果を算出する可能性があることに注意してください。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'fractions_from_float.py'))
.. }}}
.. {{{end}}}

..
    Using :mod:`decimal` representations of the values gives the expected results.

:mod:`decimal` で表した値を使用すると期待通りの結果になります。

.. include:: fractions_from_decimal.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'fractions_from_decimal.py'))
.. }}}
.. {{{end}}}

..
    Arithmetic
    ==========

計算
====

..
    Once the fractions are instantiated, they can be used in mathematical expressions as you would expect.

Fraction をインスタンス化すると、期待した通りに数学の式で使用できます。

.. include:: fractions_arithmetic.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'fractions_arithmetic.py'))
.. }}}
.. {{{end}}}

..
    Approximating Values
    ====================

近似値
======

..
    A useful feature of Fraction is the ability to convert a floating point number to an approximate rational value by limiting the size of the denominator.

Fraction の便利な機能は、分母の大きさを制限することで浮動小数の値から有理数の近似値に変換する機能です。

.. include:: fractions_limit_denominator.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'fractions_limit_denominator.py'))
.. }}}
.. {{{end}}}


.. seealso::

    `fractions <http://docs.python.org/library/fractions.html>`_
        .. The standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント

    :mod:`decimal`
        .. The decimal module provides an API for fixed and floating point math.

        固定小数点数と浮動小数点数の API を提供する decimal モジュール

    :mod:`numbers`
        .. Numeric abstract base classes.

        数値の抽象基底クラス
