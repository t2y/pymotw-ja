..
    ==================================================
    base64 -- Encode binary data into ASCII characters
    ==================================================

=====================================================
base64 -- バイナリデータを ASCII 文字へエンコードする
=====================================================

..
    :synopsis: Encode binary data into ASCII characters.

.. module:: base64
    :synopsis: バイナリデータを ASCII 文字へエンコードする

..
    :Purpose: The base64 module contains functions for translating binary data into a subset of ASCII suitable for transmission using plaintext protocols.
    :Python Version: 1.4 and later

:Purpose: base64 モジュールは、プレーンテキストプロトコルによる通信に適した ASCII 文字のサブセットへバイナリデータを変換する機能を持ちます。
:Python Version: 1.4 以上

..
    The base64, base32, and base16 encodings convert 8 bit bytes to values with 6, 5, or 4 bits of useful data per byte, allowing non-ASCII bytes to be encoded as ASCII characters for transmission over protocols that require plain ASCII, such as SMTP.  The *base* values correspond to the length of the alphabet used in each encoding.  There are also URL-safe variations of the original encodings that use slightly different results.

base64, base32 と base16 エンコーディングは、例えば SMTP のような、プレーンな ASCII 文字を必要とするプロトコルの通信で ASCII 文字としてエンコードされるように非 ASCII 文字を許容して、8ビットのバイト値を1バイト毎に扱い易い 6, 5 又は 4ビットに変換します。 *基数* となる値は各々のエンコーディングで使用されるアルファベットの長さに対応します。また、少し違う結果を使用するオリジナルエンコーディングの URL セーフな変形もあります。

..
    Base 64 Encoding
    ================

Base64 エンコーディング
=======================

..
    A basic example of encoding some text looks like this:

基本的なテキストのエンコーディング例は次のようになります:

.. include:: base64_b64encode.py
    :literal:
    :start-after: #end_pymotw_header

..
    The output shows the 558 bytes of the original source expand to 744 bytes after being encoded.

その出力はオリジナルソースが558バイトだとすると、エンコードされると744バイトに展開されます。

..
    There are no carriage returns in the output produced by the library, so I have broken the encoded data up artificially to make it fit better on the page.

.. note::
    本来ライブラリが生成した出力には改行がありません。そのため、本ページ上で見易いようにわざとエンコードデータを改行しています。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'base64_b64encode.py'))
.. }}}
.. {{{end}}}


..
    Base 64 Decoding
    ================

Base64 デコーディング
=====================

..
    The encoded string can be converted back to the original form by taking 4 bytes and converting them to the original 3, using a reverse lookup.  The ``b64decode()`` function does that for you.

エンコードされた文字列は、可逆的に4バイトからオリジナルの3バイトへ変換することでオリジナルの文字列へ戻すことができます。 ``b64decode()`` がその機能になります。

.. include:: base64_b64decode.py
    :literal:
    :start-after: #end_pymotw_header

..
    The encoding process looks at each sequence of 24 bits in the input (3 bytes) and encodes those same 24 bits spread over 4 bytes in the output.  The last two characters, the ``==``, are padding because the number of bits in the original string was not evenly divisible by 24 in this example.

エンコーディング処理は24ビット(3バイト)の入力シーケンスを見て、その24ビットの入力から4バイトへ展開した出力へエンコードします。最後の2文字 ``==`` はパディングになります。オリジナル文字列のビット数がこの例ではちょうど24ビットで分割できるサイズではなかったからです。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'base64_b64decode.py'))
.. }}}
.. {{{end}}}

..
    URL-safe Variations
    ===================

URL セーフな変形
================

..
    Because the default base64 alphabet may use ``+`` and ``/``, and those two characters are used in URLs, it became necessary to specify an alternate encoding with substitutes for those characters.  The ``+`` is replaced with a ``-``, and ``/`` is replaced with underscore (``_``).  Otherwise, the alphabet is the same.

デフォルトの base64 のアルファベットは ``+`` や ``/`` が使用されるかもしれません。その2つの文字は URL の文字列内でも使用されます。そのため、その2つの文字は代替のエンコーディング文字へ置換する必要性がありました。そして ``+`` は ``-`` へ ``/`` はアンダースコア(``_``) に置換されました。他の部分のアルファベットは同じです。

.. include:: base64_urlsafe.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'base64_urlsafe.py'))
.. }}}
.. {{{end}}}

..
    Other Encodings
    ===============

その他のエンコーディング
========================

..
    Besides base 64, the module provides functions for working with base 32 and base 16 (hex) encoded data.

このモジュールは base64 に加えて、base32 と base16(16進数) でデータをエンコードする機能も提供します。

.. include:: base64_base32.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'base64_base32.py'))
.. }}}
.. {{{end}}}

..
    The base 16 functions work with the hexadecimal alphabet.

base16 の機能は16進数のアルファベットを出力します。

.. include:: base64_base16.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'base64_base16.py'))
.. }}}
.. {{{end}}}

..
    `base64 <http://docs.python.org/library/base64.html>`_
        The standard library documentation for this module.
    :rfc:`3548`
        The Base16, Base32, and Base64 Data Encodings

.. seealso::

    `base64 <http://docs.python.org/library/base64.html>`_
        本モジュールの標準ライブラリドキュメント
    :rfc:`3548`
        Base16, Base32 と Base64 データエンコーディング

