..
    ###########################################
    Implementing MapReduce with multiprocessing
    ###########################################

#######################################
multiprocessing で MapReduce を実装する
#######################################

..
    The Pool class can be used to create a simple single-server MapReduce implementation.  Although it does not give the full benefits of distributed processing, it does illustrate how easy it is to break some problems down into distributable units of work.

Pool クラスは1サーバで簡単な MapReduce 実装を作成するために使用することができます。それは分散処理の最大限の利点を得るものではないですが、ある問題を個々の分散処理の単位に解体することがどのぐらい簡単かを分かり易く説明します。

SimpleMapReduce
===============

..
    In MapReduce, input data is broken down into chunks for processing by different worker instances.  Each chunk of input data is *mapped* to an intermediate state using a simple transformation.  The intermediate data is then collected together and partitioned based on a key value so that all of the related values are together.  Finally, the partitioned data is *reduced* to a result set.

MapReduce では、入力データを複数のワーカーインスタンスで処理するためにチャンクに解体します。各入力データのチャンクは簡単な変換を行って中間状態に *map* されます。中間データはまとめて集約されて、全ての関連する値が一緒になるように key value に基づいて分割されます。最後に、分割されたデータは結果セットへ *reduce* されます。

.. include:: multiprocessing_mapreduce.py
    :literal:
    :start-after: #end_pymotw_header

..
    Counting Words in Files
    =======================

ファイルの単語を数える
======================

..
    The following example script uses SimpleMapReduce to counts the "words" in the reStructuredText source for this article, ignoring some of the markup.  

次のサンプルスクリプトは、マークアップの幾つかを無視して本稿の reStructuredText のソースファイル内の "単語" を数える SimpleMapReduce を使用します。

.. include:: multiprocessing_wordcount.py
    :literal:
    :start-after: #end_pymotw_header

..
    Each input filename is converted to a sequence of ``(word, 1)`` pairs by ``file_to_words``.  The data is partitioned by ``SimpleMapReduce.partition()`` using the word as the key, so the partitioned data consists of a key and a sequence of 1 values representing the number of occurrences of the word.  The reduction phase converts that to a pair of ``(word, count)`` values by calling ``count_words`` for each element of the partitioned data set.

各入力ファイル名は ``file_to_words`` で ``(word, 1)`` タプルのシーケンスへ変換されます。そのデータはキーのように単語を使用して ``SimpleMapReduce.partition()`` で分割されます。そのため、分割したデータは単語が発生した数を表す1つの値のシーケンスとキーで構成されます。reduce フェーズは分割データセットの各要素に ``count_words`` を呼び出すことで ``(word, count)`` のペアに対して変換します。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'multiprocessing_wordcount.py'))
.. }}}
.. {{{end}}}

.. seealso::

    `MapReduce - Wikipedia <http://en.wikipedia.org/wiki/MapReduce>`_
        .. Overview of MapReduce on Wikipedia.

        Wikipedia の MapReduce 概要
    
    `MapReduce: Simplified Data Processing on Large Clusters <http://labs.google.com/papers/mapreduce.html>`_
        .. Google Labs presentation and paper on MapReduce.

        MapReduce に関する Google Labs のプレゼンテーションと論文

    :mod:`operator`
        .. Operator tools such as ``itemgetter()``.

        ``itemgetter()`` のようなオペレータツール

..
    *Special thanks to Jesse Noller for helping review this information.*

*本稿のレビューを手伝ってくれた Jesse Noller に感謝します。*
