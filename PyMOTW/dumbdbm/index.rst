..
    ======================================
    dumbdbm -- Portable DBM Implementation
    ======================================

================================
dumbdbm -- 移植性の高い DBM 実装
================================

..
    :synopsis: Portable DBM Implementation

.. module:: dumbdbm
    :synopsis: 移植性の高い DBM 実装

..
    :Purpose: Last-resort backend implementation for :mod:`anydbm`.
    :Available In: 1.4 and later

:目的: :mod:`anydbm` のバックエンド実装における最終手段
:利用できるバージョン: 1.4 以上

..
    The :mod:`dumbdbm` module is a portable fallback implementation of the DBM API when no other implementations are available.  No external dependencies are required to use :mod:`dumbdbm`, but it is slower than most other implementations.

:mod:`dumbdbm` モジュールは、その他の実装が使用できないときに DBM API の代替となる移植性の高い実装です。 :mod:`dumbdbm` を使用するのに外部ライブラリを必要としませんが、その他の実装と比べて遅くなります。

..
    It follows the semantics of the :mod:`anydbm` module.

:mod:`anydbm` モジュールと仕組みや動作は同じです。

.. seealso::

    `dumbdbm <http://docs.python.org/library/dumbdbm.html>`_
        .. The standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント

    :mod:`anydbm`
        .. The :mod:`anydbm` module.

        :mod:`anydbm` モジュール
