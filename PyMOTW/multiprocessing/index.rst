..
    ================================================
    multiprocessing -- Manage processes like threads
    ================================================

=====================================================
multiprocessing -- スレッドのようにプロセスを管理する
=====================================================

..
    :synopsis: Manage processes like threads.

.. module:: multiprocessing
    :synopsis: スレッドのようにプロセスを管理する

..
    :Purpose: Provides an API for managing processes.
    :Python Version: 2.6

:目的: プロセスを管理する API を提供する
:Python バージョン: 2.6

..
    The multiprocessing module includes a relatively simple API for dividing work up between multiple processes.  It is based on the API for :mod:`threading`, and in some cases is a drop-in replacement.  Due to the similarity, the first few examples here are modified from the threading examples.  Features provided by multiprocessing but not available in threading are covered later.

multiprocessing モジュールは複数プロセスで分散処理を扱う比較的シンプルな API を提供します。multiprocessing モジュールは :mod:`threading` の API をベースにしていて、処理によっては暫定的に置き換えることができます。2つのモジュールはよく似ているので、最初の数個のサンプルは threading のサンプルから修正しています。multiprocessing で提供される機能は threading では利用できないことを後で説明します。

.. toctree::
    :maxdepth: 2
    
    basics
    communication
    mapreduce


.. seealso::

    `multiprocessing <http://docs.python.org/library/multiprocessing.html>`_
        .. The standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント

    :mod:`threading`
        .. High-level API for working with threads.

        スレッドと連携する高水準 API
