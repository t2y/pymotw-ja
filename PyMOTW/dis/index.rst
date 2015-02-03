..
    ===================================
    dis -- Python Bytecode Disassembler
    ===================================

==========================================
dis -- Python バイトコードディスアセンブラ
==========================================

..
    :synopsis: Python Bytecode Disassembler

.. module:: dis
    :synopsis: Python バイトコードディスアセンブラ

..
    :Purpose: Convert code objects to a human-readable representation of the bytecodes for analysis.
    :Available In: 1.4 and later

:目的: 解析のためにコードオブジェクトを人間が読めるバイトコードに変換する
:利用できるバージョン: 1.4 以上

..
    The :mod:`dis` module includes functions for working with Python
    bytecode by "disassembling" it into a more human-readable form.
    Reviewing the bytecodes being executed by the interpreter is a good
    way to hand-tune tight loops and perform other kinds of optimizations.
    It is also useful for finding race conditions in multi-threaded
    applications, since you can estimate the point in your code where
    thread control may switch.

:mod:`dis` モジュールは Python バイトコードを "ディスアセンブル" して人間が読める形態にする機能を提供します。インタープリタが実行するバイトコードをレビューすることは、タイトループを手作業で調整したり、その他の最適化のために効率化したりする良い方法です。さらにスレッド制御が切り替わる位置を推定できるのでマルチスレッドアプリケーションの競合状態を見つけることにも役立ちます。

..
    Basic Disassembly
    =================

基本的なディスアセンブル処理
============================

..
    The function ``dis.dis()`` prints the disassembled representation of a
    Python code source (module, class, method, function, or code object).
    We can disassemble a module such as:

``dis.dis()`` という関数はディスアセンブルされた Python ソースコード(モジュール、クラス、メソッド、関数やコードオブジェクト)を表示します。次のようなモジュールに対して、

.. literalinclude:: dis_simple.py
    :linenos:

..
    by running :mod:`dis` from the command line.  The output is organized
    into columns with the original source line number, the instruction
    "address" within the code object, the opcode name, and any arguments
    passed to the opcode.

コマンドラインから :mod:`dis` モジュールを実行することでディスアセンブルすることができます。その出力はオリジナルソースの行番号、コードオブジェクト内の命令 "アドレス"、オペコード名、オペコードに渡される引数でカラムが構成されます。

.. {{{cog
.. cog.out(run_script(cog.inFile, '-m dis dis_simple.py'))
.. }}}

::

	$ python -m dis dis_simple.py
	
	  4           0 BUILD_MAP                1
	              3 LOAD_CONST               0 (1)
	              6 LOAD_CONST               1 ('a')
	              9 STORE_MAP           
	             10 STORE_NAME               0 (my_dict)
	             13 LOAD_CONST               2 (None)
	             16 RETURN_VALUE        

.. {{{end}}}

..
    In this case, the source translates to 5 different operations to
    create and populate the dictionary, then save the results to a local
    variable.  Since the Python interpreter is stack-based, the first
    steps are to put the constants onto the stack in the correct order
    with LOAD_CONST, and then use STORE_MAP to pop off the new key and
    value to be added to the dictionary.  The resulting object is bound to
    the name "my_dict" with STORE_NAME.

このケースでは、サンプルソースはディクショナリを作成して、そこで存在するために5つの異なるオペレーションに変換されます。それからローカル変数へその結果を保存します。Python インタープリタはスタックベースなので、最初のステップは LOAD_CONST を使用して正しい順番でスタックの中に定数を追加することです。それからディクショナリに追加される新たなキーと値をスタックから取り出すために STORE_MAP を使用します。その結果のオブジェクトは STORE_NAME で "my_dict" という名前に束縛されます。

..
    Disassembling Functions
    =======================

関数をディスアセンブルする
==========================

..
    Unfortunately, disassembling the entire module does not recurse into
    functions automatically.  For example, if we start with this module:

不幸にも、モジュール全体をディスアセンブルしても自動的に関数の内部を取り出すことはできません。例えば、次のようなモジュールを実行します。

.. literalinclude:: dis_function.py
    :linenos:

..
    the results show loading the code object onto the stack and then
    turning it into a function (LOAD_CONST, MAKE_FUNCTION), but *not* the
    body of the function.

その出力結果はスタック上にコードオブジェクトが読み込まれることを表示して、そのコードオブジェクトが関数(LOAD_CONST, MAKE_FUNCTION)に変わりますが、それはその関数の内部では *ありません* 。

.. {{{cog
.. cog.out(run_script(cog.inFile, '-m dis dis_function.py'))
.. }}}

::

	$ python -m dis dis_function.py
	
	  4           0 LOAD_CONST               0 (<code object f at 0x10046db30, file "dis_function.py", line 4>)
	              3 MAKE_FUNCTION            0
	              6 STORE_NAME               0 (f)
	
	  8           9 LOAD_NAME                1 (__name__)
	             12 LOAD_CONST               1 ('__main__')
	             15 COMPARE_OP               2 (==)
	             18 POP_JUMP_IF_FALSE       49
	
	  9          21 LOAD_CONST               2 (-1)
	             24 LOAD_CONST               3 (None)
	             27 IMPORT_NAME              2 (dis)
	             30 STORE_NAME               2 (dis)
	
	 10          33 LOAD_NAME                2 (dis)
	             36 LOAD_ATTR                2 (dis)
	             39 LOAD_NAME                0 (f)
	             42 CALL_FUNCTION            1
	             45 POP_TOP             
	             46 JUMP_FORWARD             0 (to 49)
	        >>   49 LOAD_CONST               3 (None)
	             52 RETURN_VALUE        

.. {{{end}}}

..
    To see inside the function, we need to pass it to ``dis.dis()``.

関数の内部を見るためには ``dis.dis()`` にその関数を渡す必要があります。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'dis_function.py'))
.. }}}

::

	$ python dis_function.py
	
	  5           0 LOAD_GLOBAL              0 (len)
	              3 LOAD_FAST                0 (args)
	              6 CALL_FUNCTION            1
	              9 STORE_FAST               1 (nargs)
	
	  6          12 LOAD_FAST                1 (nargs)
	             15 PRINT_ITEM          
	             16 LOAD_FAST                0 (args)
	             19 PRINT_ITEM          
	             20 PRINT_NEWLINE       
	             21 LOAD_CONST               0 (None)
	             24 RETURN_VALUE        

.. {{{end}}}

..
    Classes
    =======

クラス
======

..
    You can also pass classes to ``dis``, in which case all of the methods
    are disassembled in turn.

同様にコードオブジェクトに変わる全てのメソッドがディスアセンブルされるように ``dis`` へクラスを渡すこともできます。

.. literalinclude:: dis_class.py
    :linenos:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'dis_class.py'))
.. }}}

::

	$ python dis_class.py
	
	Disassembly of __init__:
	 12           0 LOAD_FAST                1 (name)
	              3 LOAD_FAST                0 (self)
	              6 STORE_ATTR               0 (name)
	              9 LOAD_CONST               0 (None)
	             12 RETURN_VALUE        
	
	Disassembly of __str__:
	 15           0 LOAD_CONST               1 ('MyObject(%s)')
	              3 LOAD_FAST                0 (self)
	              6 LOAD_ATTR                0 (name)
	              9 BINARY_MODULO       
	             10 RETURN_VALUE        
	

.. {{{end}}}

..
    Using Disassembly to Debug
    ==========================

デバッグのためにディスアセンブルする
====================================

..
    Sometimes when debugging an exception it can be useful to see which
    bytecode caused a problem.  There are a couple of ways to disassemble
    the code around an error.

例外をデバッグするとき、バイトコードが問題を引き起こすことを確認するために役に立つときがあります。エラーが発生する付近のコードをディスアセンブルする方法があります。

..
    The first is by using ``dis.distb()`` in the interactive interpreter to
    report about the last exception.  If no argument is passed to ``dis.distb()``,
    then it looks for an exception and shows the disassembly of the top of
    the stack that caused it.

1つ目は最後に発生した例外に関するレポートのためにインタープリタで ``dis.distb()`` を使用します。 ``dis.distb()`` に引数が渡されなかったら最後に発生した例外を探して、その例外を引き起こしたスタックをディスアセンブルして表示します。

::

    $ python
    Python 2.6.2 (r262:71600, Apr 16 2009, 09:17:39) 
    [GCC 4.0.1 (Apple Computer, Inc. build 5250)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import dis
    >>> j = 4
    >>> i = i + 4
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'i' is not defined
    >>> dis.distb()
      1 -->       0 LOAD_NAME                0 (i)
                  3 LOAD_CONST               0 (4)
                  6 BINARY_ADD          
                  7 STORE_NAME               0 (i)
                 10 LOAD_CONST               1 (None)
                 13 RETURN_VALUE        
    >>>

..
    Notice the ``-->`` indicating the opcode that caused the error.  There
    is no ``i`` variable defined, so the value associated with the name
    can't be loaded onto the stack.

``-->`` はエラーを引き起こしたオペコードを指していることに注意してください。 ``i`` という変数が定義されていないので、その名前で関連付けられた値をスタック上にロードすることができません。

..
    Within your code you can also print the information about an active
    traceback by passing it to ``dis.distb()`` directly.  In this example,
    there is a DivideByZero exception, but since the formula has two
    divisions it isn't clear which part is zero.

コード内で ``dis.distb()`` に直接アクティブなトレースバックを渡すことでそれに関する情報を表示することもできます。このサンプルでは DivideByZero 例外が発生しますが、コード内の数式は2つの除算があるので、どちらがゼロかは分かりません。

.. literalinclude:: dis_traceback.py
    :linenos:

..
    The bad value is easy to spot when it is loaded onto the stack in the
    disassembled version.  The bad operation is highlighted with the
    ``-->``, and we just need to look up a few lines higher to find where
    ``j``'s ``0`` value was pushed onto the stack.

ディスアセンブルされたソースでスタック上に問題のある値がロードされるとき、その値を見つけることは簡単です。問題のあるオペレーションは ``-->`` でハイライトされます。そして ``j`` に格納されている ``0`` という値がスタック上に追加された場所を見つけるためにほんの数行前を探すだけです。

.. {{{cog
.. cog.out(run_script(cog.inFile, 'dis_traceback.py'))
.. }}}

::

	$ python dis_traceback.py
	
	  4           0 LOAD_CONST               0 (1)
	              3 STORE_NAME               0 (i)
	
	  5           6 LOAD_CONST               1 (0)
	              9 STORE_NAME               1 (j)
	
	  6          12 LOAD_CONST               2 (3)
	             15 STORE_NAME               2 (k)
	
	 10          18 SETUP_EXCEPT            26 (to 47)
	
	 11          21 LOAD_NAME                2 (k)
	             24 LOAD_NAME                0 (i)
	             27 LOAD_NAME                1 (j)
	    -->      30 BINARY_DIVIDE       
	             31 BINARY_MULTIPLY     
	             32 LOAD_NAME                0 (i)
	             35 LOAD_NAME                2 (k)
	             38 BINARY_DIVIDE       
	             39 BINARY_ADD          
	             40 STORE_NAME               3 (result)
	             43 POP_BLOCK           
	             44 JUMP_FORWARD            65 (to 112)
	
	 12     >>   47 POP_TOP             
	             48 POP_TOP             
	             49 POP_TOP             
	
	 13          50 LOAD_CONST               3 (-1)
	             53 LOAD_CONST               4 (None)
	             56 IMPORT_NAME              4 (dis)
	             59 STORE_NAME               4 (dis)
	
	 14          62 LOAD_CONST               3 (-1)
	             65 LOAD_CONST               4 (None)
	             68 IMPORT_NAME              5 (sys)
	             71 STORE_NAME               5 (sys)
	
	 15          74 LOAD_NAME                5 (sys)
	             77 LOAD_ATTR                6 (exc_info)
	             80 CALL_FUNCTION            0
	             83 UNPACK_SEQUENCE          3
	             86 STORE_NAME               7 (exc_type)
	             89 STORE_NAME               8 (exc_value)
	             92 STORE_NAME               9 (exc_tb)
	
	 16          95 LOAD_NAME                4 (dis)
	             98 LOAD_ATTR               10 (distb)
	            101 LOAD_NAME                9 (exc_tb)
	            104 CALL_FUNCTION            1
	            107 POP_TOP             
	            108 JUMP_FORWARD             1 (to 112)
	            111 END_FINALLY         
	        >>  112 LOAD_CONST               4 (None)
	            115 RETURN_VALUE        

.. {{{end}}}

..
    Performance Analysis of Loops
    =============================

ループのパフォーマンス解析
==========================

..
    Aside from debugging errors, :mod:`dis` can also help you identify
    performance issues in your code. Examining the disassembled code is
    especially useful with tight loops where the number of exposed Python
    instructions is low but they translate to an inefficient set of
    bytecodes.  We can see how the disassembly is helpful by examining a
    few different implementations of a class, ``Dictionary``, that reads a
    list of words and groups them by their first letter.

エラーをデバッグすることとは別に :mod:`dis` はパフォーマンスの問題を特定することにも役立ちます。ディスアセンブルされたコードを調べることは、数少ない Python のバイトコード命令が非効率なバイトコードセットへ変換するタイトループで特に役に立ちます。単語のリストを読み込み、その最初の文字で単語をグループ分けするクラス ``Dictionary`` の異なる実装を数個調べることで、ディスアセンブルすることがどのように役に立つかを理解できます。

..
    First, the test driver application:

先ずはテストドライバアプリケーションです。

.. include:: dis_test_loop.py
    :literal:
    :start-after: #end_pymotw_header

..
    We can use ``dis_test_loop.py`` to run each incarnation of the
    ``Dictionary`` class.

``Dictionary`` クラスの個々の実体化を処理するために ``dis_test_loop.py`` を使用します。

..
    A straightforward implementation of ``Dictionary`` might look
    something like:

率直に考えた ``Dictionary`` の実装は次のように単語を探すかもしれません。

.. literalinclude:: dis_slow_loop.py
    :linenos:

..
    The output shows this version taking 0.1074 seconds to load the 234936
    words in my copy of ``/usr/share/dict/words`` on OS X.  That's not too
    bad, but as you can see from the disassembly below, the loop is doing
    more work than it needs to.  As it enters the loop in opcode 13, it
    sets up an exception context (``SETUP_EXCEPT``).  Then it takes 6
    opcodes to find ``self.by_letter[word[0]]`` before appending ``word``
    to the list.  If there is an exception because ``word[0]`` isn't in
    the dictionary yet, the exception handler does all of the same work to
    determine ``word[0]`` (3 opcodes) and sets ``self.by_letter[word[0]]``
    to a new list containing the word.

このソースの出力結果は Mac OS X で ``/usr/share/dict/words`` のコピーである 234936 単語を読み込むために 0.1074 秒かかりました。それはあまり悪い結果ではありませんが、次のようにディスアセンブルして、必要ならもっと効率的に動作することを理解できます。オペコード13でループに入ると、例外コンテキスト(``SETUP_EXCEPT``)をセットアップします。それからリストへ ``word`` を追加する前に ``self.by_letter[word[0]]`` を見つけるために6個のオペコードを取ります。ディクショナリにまだ ``word[0]`` が存在しないために例外が発生するなら、その例外ハンドラは ``word[0]`` (3 オペコード) を調べるために全て同じように動作します。そして、その単語を含む新たなリストに対して ``self.by_letter[word[0]]`` をセットします。

.. timing values are sensitive to other operations, so don't cog

::

	$ python dis_test_loop.py dis_slow_loop
	 11           0 SETUP_LOOP              84 (to 87)
	              3 LOAD_FAST                1 (words)
	              6 GET_ITER            
	        >>    7 FOR_ITER                76 (to 86)
	             10 STORE_FAST               2 (word)
	
	 12          13 SETUP_EXCEPT            28 (to 44)
	
	 13          16 LOAD_FAST                0 (self)
	             19 LOAD_ATTR                0 (by_letter)
	             22 LOAD_FAST                2 (word)
	             25 LOAD_CONST               1 (0)
	             28 BINARY_SUBSCR       
	             29 BINARY_SUBSCR       
	             30 LOAD_ATTR                1 (append)
	             33 LOAD_FAST                2 (word)
	             36 CALL_FUNCTION            1
	             39 POP_TOP             
	             40 POP_BLOCK           
	             41 JUMP_ABSOLUTE            7
	
	 14     >>   44 DUP_TOP             
	             45 LOAD_GLOBAL              2 (KeyError)
	             48 COMPARE_OP              10 (exception match)
	             51 JUMP_IF_FALSE           27 (to 81)
	             54 POP_TOP             
	             55 POP_TOP             
	             56 POP_TOP             
	             57 POP_TOP             
	
	 15          58 LOAD_FAST                2 (word)
	             61 BUILD_LIST               1
	             64 LOAD_FAST                0 (self)
	             67 LOAD_ATTR                0 (by_letter)
	             70 LOAD_FAST                2 (word)
	             73 LOAD_CONST               1 (0)
	             76 BINARY_SUBSCR       
	             77 STORE_SUBSCR        
	             78 JUMP_ABSOLUTE            7
	        >>   81 POP_TOP             
	             82 END_FINALLY         
	             83 JUMP_ABSOLUTE            7
	        >>   86 POP_BLOCK           
	        >>   87 LOAD_CONST               0 (None)
	             90 RETURN_VALUE        
	
	TIME: 0.1074

..
    One technique to eliminate the exception setup is to pre-populate
    ``self.by_letter`` with one list for each letter of the alphabet.
    That means we should always find the list we want for the new word,
    and can just do the lookup and save the value.

例外のセットアップを取り除くための1つのテクニックは全てのアルファベット ``self.by_letter`` を事前に1つのリスト内に存在させることです。それはつまり、新たな単語はいつもそのリストで見つかるので、最初の文字の値の探索と単語の保存処理だけになります。

.. literalinclude:: dis_faster_loop.py
    :linenos:

..
    The change cuts the number of opcodes in half, but only shaves the
    time down to 0.0984 seconds.  Obviously the exception handling had
    some overhead, but not a huge amount.

その変更はオペコード数を半分に減らしますが、たった 0.0984 秒に実行時間を短縮できただけです。例外の扱いは明らかにオーバヘッドになりますが、そう大きなものではありません。

.. timing values are sensitive to other operations, so don't cog

::

	$ python dis_test_loop.py dis_faster_loop
	 14           0 SETUP_LOOP              38 (to 41)
	              3 LOAD_FAST                1 (words)
	              6 GET_ITER            
	        >>    7 FOR_ITER                30 (to 40)
	             10 STORE_FAST               2 (word)
	
	 15          13 LOAD_FAST                0 (self)
	             16 LOAD_ATTR                0 (by_letter)
	             19 LOAD_FAST                2 (word)
	             22 LOAD_CONST               1 (0)
	             25 BINARY_SUBSCR       
	             26 BINARY_SUBSCR       
	             27 LOAD_ATTR                1 (append)
	             30 LOAD_FAST                2 (word)
	             33 CALL_FUNCTION            1
	             36 POP_TOP             
	             37 JUMP_ABSOLUTE            7
	        >>   40 POP_BLOCK           
	        >>   41 LOAD_CONST               0 (None)
	             44 RETURN_VALUE        
	
	TIME: 0.0984

..
    We can further improve the performance by moving the lookup for
    ``self.by_letter`` outside of the loop (the value doesn't change,
    after all).

``self.by_letter`` の名前のルックアップをループの外側に移動することで、そのパフォーマンスを大幅に改善することができます(そうしても、その値は変更しません)。

.. literalinclude:: dis_fastest_loop.py
    :linenos:

..
    Opcodes 0-6 now find the value of ``self.by_letter`` and save it as a
    local variable ``by_letter``.  Using a local variable only takes a
    single opcode, instead of 2 (statement 22 uses ``LOAD_FAST`` to place
    the dictionary onto the stack).  After this change, the run time is
    down to 0.0842 seconds.

今、オペコード0-6は ``self.by_letter`` の値を見つけます。そして ``self.by_letter`` の値をローカル変数 ``by_letter`` に保存します。
2つのオペコードの代わりに、ローカル変数を使用することで1つのオペコードのみを取ります(ステートメント22はそのディクショナリをスタック上に追加するために ``LOAD_FAST`` を使用する)。この変更後に実行時間は 0.0842 秒へ減少します。

.. timing values are sensitive to other operations, so don't cog

::

	$ python dis_test_loop.py dis_fastest_loop
	 13           0 LOAD_FAST                0 (self)
	              3 LOAD_ATTR                0 (by_letter)
	              6 STORE_FAST               2 (by_letter)
	
	 14           9 SETUP_LOOP              35 (to 47)
	             12 LOAD_FAST                1 (words)
	             15 GET_ITER            
	        >>   16 FOR_ITER                27 (to 46)
	             19 STORE_FAST               3 (word)
	
	 15          22 LOAD_FAST                2 (by_letter)
	             25 LOAD_FAST                3 (word)
	             28 LOAD_CONST               1 (0)
	             31 BINARY_SUBSCR       
	             32 BINARY_SUBSCR       
	             33 LOAD_ATTR                1 (append)
	             36 LOAD_FAST                3 (word)
	             39 CALL_FUNCTION            1
	             42 POP_TOP             
	             43 JUMP_ABSOLUTE           16
	        >>   46 POP_BLOCK           
	        >>   47 LOAD_CONST               0 (None)
	             50 RETURN_VALUE        
	
	TIME: 0.0842

..
    A further optimization, suggested by Brandon Rhodes, is to eliminate
    the Python version of the ``for`` loop entirely. If we use
    :ref:`itertools.groupby() <itertools-groupby>` to arrange the input,
    the iteration is moved to C.  We can do this safely because we know
    the inputs are already sorted.  If you didn't know they were sorted
    you would need to sort them first.

Brandon Rhodes が提案したさらなる最適化は Python のソースから ``for`` ループを完全に排除することです。もし入力の単語を配置するために :ref:`itertools.groupby() <itertools-groupby>` を使用するなら、その繰り返し処理は C 言語側へ移動されます。このサンプルではその入力の単語が既にソートされていることが分かっているので安全に実行することができます。もし入力の単語がソートされているか分からなかったら、先に入力の単語をソートする必要があります。

.. literalinclude:: dis_eliminate_loop.py
    :linenos:

..
    The :mod:`itertools` version takes only 0.0543 seconds to run, just
    over half of the original time.

:mod:`itertools` を使用すると実行時間はたった 0.0543 秒です。オリジナルの実行時間のちょうど半分です。

.. timing values are sensitive to other operations, so don't cog

::

	$ python dis_test_loop.py dis_eliminate_loop
	 15           0 LOAD_GLOBAL              0 (itertools)
	              3 LOAD_ATTR                1 (groupby)
	              6 LOAD_FAST                1 (words)
	              9 LOAD_CONST               1 ('key')
	             12 LOAD_GLOBAL              2 (operator)
	             15 LOAD_ATTR                3 (itemgetter)
	             18 LOAD_CONST               2 (0)
	             21 CALL_FUNCTION            1
	             24 CALL_FUNCTION          257
	             27 STORE_FAST               2 (grouped)
	
	 17          30 LOAD_GLOBAL              4 (dict)
	             33 LOAD_CONST               3 (<code object <genexpr> at 0x7e7b8, file "/Users/dhellmann/Documents/PyMOTW/dis/PyMOTW/dis/dis_eliminate_loop.py", line 17>)
	             36 MAKE_FUNCTION            0
	             39 LOAD_FAST                2 (grouped)
	             42 GET_ITER            
	             43 CALL_FUNCTION            1
	             46 CALL_FUNCTION            1
	             49 LOAD_FAST                0 (self)
	             52 STORE_ATTR               5 (by_letter)
	             55 LOAD_CONST               0 (None)
	             58 RETURN_VALUE        
	
	TIME: 0.0543

..
    Compiler Optimizations
    ======================

コンパイラの最適化
==================

..
    Disassembling compiled source also exposes some of the optimizations
    made by the compiler.  For example, literal expressions are folded
    during compilation, when possible.

コンパイルされたソースをディスアセンブルすることはコンパイラによって最適化が行われたことを表します。例えば、リテラル表記はコンパイル中にできるだけ折り畳まれます。

.. literalinclude:: dis_constant_folding.py
    :linenos:

..
    The expressions on lines 5-7 can be computed at compilation time and
    collapsed into single LOAD_CONST instructions because nothing in the
    expression can change the way the operation is performed.  That isn't
    true about lines 10-12. Because a variable is involved in those
    expressions, and the variable might refer to an object that overloads
    the operator involved, the evaluation has to be delayed to runtime.

5-7行目のリテラル表記はオペレーションが実行されている途中で変更されないのでコンパイル時に1つの LOAD_CONST 命令に折り畳まれて算出されます。10-12行目に関してはそうではありません。というのは、変数は評価されて、その変数が実行したオペレータをオーバーロードするオブジェクトを参照する可能性があるからです。そのため、変数の評価は実行時に遅延させる必要があります。

.. {{{cog
.. cog.out(run_script(cog.inFile, '-m dis dis_constant_folding.py'))
.. }}}

::

	$ python -m dis dis_constant_folding.py
	
	  5           0 LOAD_CONST              11 (3)
	              3 STORE_NAME               0 (i)
	
	  6           6 LOAD_CONST              12 (19.04)
	              9 STORE_NAME               1 (f)
	
	  7          12 LOAD_CONST              13 ('Hello, World!')
	             15 STORE_NAME               2 (s)
	
	 10          18 LOAD_NAME                0 (i)
	             21 LOAD_CONST               6 (3)
	             24 BINARY_MULTIPLY     
	             25 LOAD_CONST               7 (4)
	             28 BINARY_MULTIPLY     
	             29 STORE_NAME               3 (I)
	
	 11          32 LOAD_NAME                1 (f)
	             35 LOAD_CONST               1 (2)
	             38 BINARY_DIVIDE       
	             39 LOAD_CONST               6 (3)
	             42 BINARY_DIVIDE       
	             43 STORE_NAME               4 (F)
	
	 12          46 LOAD_NAME                2 (s)
	             49 LOAD_CONST               8 ('\n')
	             52 BINARY_ADD          
	             53 LOAD_CONST               9 ('Fantastic!')
	             56 BINARY_ADD          
	             57 STORE_NAME               5 (S)
	             60 LOAD_CONST              10 (None)
	             63 RETURN_VALUE        

.. {{{end}}}


.. seealso::

    `dis <http://docs.python.org/library/dis.html>`_
        ..
            The standard library documentation for this module, including
            the list of `bytecode instructions
            <http://docs.python.org/library/dis.html#python-bytecode-instructions>`_.
        
        `バイトコード命令 <http://docs.python.org/library/dis.html#python-bytecode-instructions>`_ を含む本モジュールの標準ライブラリドキュメント

    *Python Essential Reference*, 4th Edition, David M. Beazley
        http://www.informit.com/store/product.aspx?isbn=0672329786

    `thomas.apestaart.org "Python Disassembly" <http://thomas.apestaart.org/log/?p=927>`_
        ..
            A short discussion of the difference between storing values in
            a dictionary between Python 2.5 and 2.6.

        Python 2.5 と 2.6 でディクショナリへ値を格納することの違いに関する短い議論

    ..
        `Why is looping over range() in Python faster than using a while loop? <http://stackoverflow.com/questions/869229/why-is-looping-over-range-in-python-faster-than-using-a-while-loop>`_
            A discussion on StackOverflow.com comparing 2 looping examples
            via their disassembled bytecodes.

    `Python の range() 上のループは while ループを使用するよりなぜ速いか？ <http://stackoverflow.com/questions/869229/why-is-looping-over-range-in-python-faster-than-using-a-while-loop>`_
        ディスアセンブルされたバイトコードを通して2つのループのサンプルを比較する StackOverflow.com の議論

    ..
        `Decorator for binding constants at compile time <http://code.activestate.com/recipes/277940/>`_
            Python Cookbook recipe by Raymond Hettinger and Skip Montanaro
            with a function decorator that re-writes the bytecodes for a
            function to insert global constants to avoid runtime name
            lookups.

    `コンパイル時に定数を束縛するためのデコレータ <http://code.activestate.com/recipes/277940/>`_
        Raymond Hettinger と Skip Montanaro による Python クックブックのレシピで実行時に名前を検索しないようにグローバル定数を追加する関数のバイトコードを書き直すデコレータ
