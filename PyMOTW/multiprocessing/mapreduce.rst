..
    ###########################################
    Implementing MapReduce with multiprocessing
    ###########################################

#######################################
multiprocessing で MapReduce を実装する
#######################################

..
    The :class:`Pool` class can be used to create a simple single-server
    MapReduce implementation.  Although it does not give the full benefits
    of distributed processing, it does illustrate how easy it is to break
    some problems down into distributable units of work.

:class:`Pool` クラスは1サーバで簡単な MapReduce 実装を作成するために使用することができます。それは分散処理の最大限の利点を得るものではないですが、ある問題を個々の分散処理の単位に分解することがどのぐらい簡単かを分かり易く説明します。

SimpleMapReduce
===============

..
    In a MapReduce-based system, input data is broken down into chunks for
    processing by different worker instances.  Each chunk of input data is
    *mapped* to an intermediate state using a simple transformation.  The
    intermediate data is then collected together and partitioned based on
    a key value so that all of the related values are together.  Finally,
    the partitioned data is *reduced* to a result set.

MapReduce ベースのシステムでは、入力データを複数のワーカーインスタンスで処理するためにチャンクに分解します。各入力データのチャンクは簡単な変換を行って中間状態に *map* されます。中間データはまとめて集約されて、全ての関連する値が一緒になるように key value に基づいて分割されます。最後に、分割されたデータは結果セットへ *reduce* されます。

.. include:: multiprocessing_mapreduce.py
    :literal:
    :start-after: #end_pymotw_header

..
    Counting Words in Files
    =======================

ファイルの単語を数える
======================

..
    The following example script uses SimpleMapReduce to counts the
    "words" in the reStructuredText source for this article, ignoring some
    of the markup.

次のサンプルスクリプトは、マークアップの幾つかを無視して本稿の reStructuredText のソースファイル内の "単語" を数える SimpleMapReduce を使用します。

.. include:: multiprocessing_wordcount.py
    :literal:
    :start-after: #end_pymotw_header

..
    The :func:`file_to_words` function converts each input file to a
    sequence of tuples containing the word and the number 1 (representing
    a single occurrence) .The data is partitioned by :func:`partition`
    using the word as the key, so the partitioned data consists of a key
    and a sequence of 1 values representing each occurrence of the word.
    The partioned data is converted to a set of suples containing a word
    and the count for that word by :func:`count_words` during the
    reduction phase.

:func:`file_to_words` はそれぞれの入力ファイルを単語と数値1(1つ出現したことを表す)を持つタプルのシーケンスに変換します。そのデータはキーのようにその単語を使用して :func:`partition` で分割されます。そのため、分割したデータはその単語の出現頻度を表す1つの値のシーケンスとキーで構成されます。reduce フェーズでは、分割したデータは :func:`count_words` により単語とその単語の出現数を含むタプルのセットに変換されます。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'multiprocessing_wordcount.py'))
.. }}}

::

	$ python multiprocessing_wordcount.py
	
	PoolWorker-1 reading basics.rst
	PoolWorker-3 reading index.rst
	PoolWorker-4 reading mapreduce.rst
	PoolWorker-2 reading communication.rst
	
	TOP 20 WORDS BY FREQUENCY
	
	process         :    80
	starting        :    52
	multiprocessing :    40
	worker          :    37
	after           :    33
	poolworker      :    32
	running         :    31
	consumer        :    31
	processes       :    30
	start           :    28
	exiting         :    28
	python          :    28
	class           :    27
	literal         :    26
	header          :    26
	pymotw          :    26
	end             :    26
	daemon          :    22
	now             :    21
	func            :    20

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
