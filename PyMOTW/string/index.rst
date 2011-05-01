..
    ===========================
    string -- Working with text
    ===========================

========================
string -- テキストを扱う
========================

..
    :synopsis: Contains constants and classes for working with text.

.. module:: string
    :synopsis: テキストを扱う定数やクラスを提供する

..
    :Purpose: Contains constants and classes for working with text.
    :Available In: 2.5

:目的: テキストを扱う定数やクラスを提供する
:利用できるバージョン: 2.5

..
    The :mod:`string` module dates from the earliest versions of
    Python. In version 2.0, many of the functions previously implemented
    only in the module were moved to methods of :class:`str` and
    :class:`unicode` objects. Legacy versions of those functions are still
    available, but their use is deprecated and they will be dropped in
    Python 3.0. The :mod:`string` module still contains several useful
    constants and classes for working with string and unicode objects, and
    this discussion will concentrate on them.

:mod:`string` モジュールは Python の初期バージョンを端緒とします。バージョン 2.0 では、このモジュールのみに実装されていた多くの関数が :class:`str` と :class:`unicode` オブジェクトのメソッドに移行されました。そういった関数のレガシーバージョンはまだ有効ですが、その使用は非推奨であり Python 3.0 で削除されます。それでも :mod:`string` モジュールは、文字列やユニコードオブジェクトを扱う便利な定数やクラスを提供します。そして、この記事はそういった内容に特化しています。

..
    Constants
    =========

定数
====

..
    The constants in the string module can be used to specify categories
    of characters such as ``ascii_letters`` and ``digits``. Some of the
    constants, such as ``lowercase``, are locale-dependent so the value
    changes to reflect the language settings of the user. Others, such as
    ``hexdigits``, do not change when the locale changes.

:mod:`string` モジュールの定数は、 ``ascii_letters`` や ``digits`` のような特殊な特性のカテゴリで使用されます。定数によっては、 ``lowercase`` のようにロケールに依存するので、その値はユーザの言語設定を考慮して変更します。一方 ``hexdigits`` のような定数は、ロケールが違っても変更する必要はありません。

.. include:: string_constants.py
    :literal:
    :start-after: #end_pymotw_header

..
    Most of the names for the constants are self-explanatory.

ほとんどの定数の名前は自己説明的です。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'string_constants.py'))
.. }}}
.. {{{end}}}

..
    Functions
    =========

関数
====

..
    There are two functions not moving from the string
    module. :func:`capwords()` capitalizes all of the words in a string.

:mod:`string` モジュールから移行されなかった2つの関数があります。 :func:`capwords()` は文字列の全ての単語の先頭を大文字にします。

.. include:: string_capwords.py
    :literal:
    :start-after: #end_pymotw_header

..
    The results are the same as if you called :func:`split()`, capitalized
    the words in the resulting list, then called :func:`join()` to combine
    the results.

文字列を :func:`split()` して、その出力リストの単語の先頭を大文字にしてから、 :func:`join()` でそれらの単語を結合するのと同じ結果です。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'string_capwords.py'))
.. }}}
.. {{{end}}}

..
    The other function creates translation tables that can be used with
    the :func:`translate()` method to change one set of characters to
    another.

もう1つの関数は、文字セットを別のものに変更する :func:`translate()` メソッドで使用される変換テーブルを作成します。

.. include:: string_maketrans.py
    :literal:
    :start-after: #end_pymotw_header

..
    In this example, some letters are replaced by their `l33t
    <http://en.wikipedia.org/wiki/Leet>`_ number alternatives.

このサンプルでは、文字が `l33t <http://en.wikipedia.org/wiki/Leet>`_ による数字で置き換えられます。 

.. {{{cog
.. cog.out(run_script(cog.inFile, 'string_maketrans.py'))
.. }}}
.. {{{end}}}

..
    Templates
    =========

テンプレート
============

..
    String templates were added in Python 2.4 as part of :pep:`292` and
    are intended as an alternative to the built-in interpolation
    syntax. With :class:`string.Template` interpolation, variables are
    identified by name prefixed with ``$`` (e.g., ``$var``) or, if
    necessary to set them off from surrounding text, they can also be
    wrapped with curly braces (e.g., ``${var}``).

文字列テンプレートが :pep:`292` の一部として Python 2.4 で追加されました。それは組み込みの補間構文の代替方法を意図しています。 :class:`string.Template` の補間では、変数は ``$`` (例 ``$var``) を接頭辞とする名前で識別されます。また、変数名の周りの文字列を無効にする必要があるなら、変数名を中括弧で囲むこともできます(例 ``${var}``)。

..
    This example compares a simple template with a similar string
    interpolation setup.

このサンプルは、シンプルなテンプレートと同じような文字列の補間設定を比較します。

.. include:: string_template.py
    :literal:
    :start-after: #end_pymotw_header

..
    As you see, in both cases the trigger character (``$`` or ``%``) is
    escaped by repeating it twice.

ご覧の通り、両方のケースでトリガー文字 (``$`` や ``%``) は2文字続けることでエスケープされます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'string_template.py'))
.. }}}
.. {{{end}}}

..
    One key difference between templates and standard string interpolation
    is that the type of the arguments is not taken into account. The
    values are converted to strings, and the strings are inserted into the
    result. No formatting options are available. For example, there is no
    way to control the number of digits used to represent a floating point
    value.

テンプレートと標準の文字列補間の大きな違いの1つは、引数の型を考慮しない点です。その値は文字列に変換されて、その変換された文字列は結果出力に追加されます。フォーマットオプションは指定しなくても構いません。例えば、浮動小数を表す数値の桁数を管理する方法はありません。

..
    A benefit, though, is that by using the :func:`safe_substitute()`
    method, it is possible to avoid exceptions if not all of the values
    needed by the template are provided as arguments.

:func:`safe_substitute()` を使用することの利点でもありますが、テンプレートが要求する全ての値が引数として提供されない場合でも例外を発生させません。

.. include:: string_template_missing.py
    :literal:
    :start-after: #end_pymotw_header

..
    Since there is no value for missing in the values dictionary, a
    :ref:`KeyError <exceptions-KeyError>` is raised by
    :func:`substitute()`. Instead of raising the error,
    :func:`safe_substitute()` catches it and leaves the variable
    expression alone in the text.

values ディクショナリには missing の値はないので、 :func:`substitute()` は :ref:`KeyError <exceptions-KeyError>` を発生させます。 :func:`safe_substitute()` は、このエラーを発生させずに捕捉して、テキストに変数表現がそのまま残ります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'string_template_missing.py'))
.. }}}
.. {{{end}}}

..
    Advanced Templates
    ==================

高度なテンプレート
==================

..
    If the default syntax for :class:`string.Template` is not to your
    liking, you can change the behavior by adjusting the regular
    expression patterns it uses to find the variable names in the template
    body. A simple way to do that is to change the *delimiter* and
    *idpattern* class attributes.

:class:`string.Template` のデフォルトの構文が好みではないなら、テンプレート本文の変数名を見つける正規表現を調整することでその振る舞いを変更できます。最も簡単な方法は *delimiter* と *idpattern* のクラス属性を変更します。

.. include:: string_template_advanced.py
    :literal:
    :start-after: #end_pymotw_header

..
    In this example, variable ids must include an underscore somewhere in
    the middle, so ``%notunderscored`` is not replaced by anything.

このサンプルでは、変数の ID は中間にアンダースコアを含めなければならないので、 ``%notunderscored`` は置き換えられません。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'string_template_advanced.py'))
.. }}}
.. {{{end}}}

..
    For more complex changes, you can override the *pattern* attribute and
    define an entirely new regular expression. The pattern provided must
    contain four named groups for capturing the escaped delimiter, the
    named variable, a braced version of the variable name, and invalid
    delimiter patterns.

もっと複雑な変更だと、 *pattern* 属性をオーバーライドして全く新しい正規表現を定義できます。そのパターンは、エスケープされるデリミタ、名前付き変数、括弧付きの名前付き変数、不正なデリミタパターンの4つの名前付きグループを含めなければなりません。

..
    Let's look at the default pattern:

デフォルトのパターンを見てみましょう。

.. include:: string_template_defaultpattern.py
    :literal:
    :start-after: #end_pymotw_header

..
    Since ``t.pattern`` is a compiled regular expression, we have to
    access its pattern attribute to see the actual string.

``t.pattern`` は複雑な正規表現なので、実際の文字列を見るためにその *pattern* 属性にアクセスする必要があります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'string_template_defaultpattern.py'))
.. }}}
.. {{{end}}}

..
    If we wanted to create a new type of template using, for example,
    ``{{var}}`` as the variable syntax, we could use a pattern like this:

例えば、変数の構文として ``{{var}}`` といったテンプレートの新しい型を作成したいなら、次のようなパターンを使用できます。

.. include:: string_template_newsyntax.py
    :literal:
    :start-after: #end_pymotw_header

..
    We still have to provide both the named and braced patterns, even
    though they are the same. Here's the output:

変数名と括弧付きの変数名のパターンが同じだったとしても、両方とも提供する必要があります。実行結果は次のようになります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'string_template_newsyntax.py'))
.. }}}
.. {{{end}}}

..
    Deprecated Functions
    ====================

非推奨な関数
============

..
    For information on the deprecated functions moved to the string and
    unicode classes, refer to `String Methods
    <http://docs.python.org/lib/string-methods.html#string-methods>`_ in
    the manual.

非推奨なメソッドの情報は :class:`string` と :class:`unicode`  クラスへ移行されました。 `String メソッド <http://docs.python.org/lib/string-methods.html#string-methods>`_ のドキュメントを参照してください。

.. seealso::

    `string <http://docs.python.org/lib/module-string.html>`_
        .. Standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント

    :pep:`292`
        .. Simpler String Substitutions

        シンプルな文字列置換

    :ref:`article-text-processing`
