.. Not using cog because these examples are interactive.

..
    ==========================================================
    getpass -- Prompt the user for a password without echoing.
    ==========================================================

===========================================================
getpass -- パスワードのために入力文字を表示しないプロンプト
===========================================================

..
    :synopsis: Prompt the user for a value, usually a password, without echoing what they type to the console.

.. module:: getpass
    :synopsis: コンソールに入力した文字を表示しないプロンプト、普通はパスワード入力に使用する

..
    :Purpose: Prompt the user for a value, usually a password, without echoing what they type to the console.
    :Available In: 1.5.2

:目的: コンソールに入力した文字を表示しないプロンプト、普通はパスワード入力に使用する
:利用できるバージョン: 1.5.2

..
    Many programs that interact with the user via the terminal need to ask
    the user for password values without showing what the user types on
    the screen.  The :mod:`getpass` module provides a portable way to
    handle such password prompts securely.

ターミナルを通してユーザと対話的にやり取りする多くのプログラムで、スクリーン上にユーザが入力した文字を表示せずにパスワードを尋ねる必要があります。 :mod:`getpass` モジュールは、そういったセキュアなパスワードプロンプトを扱う移植性の高い方法を提供します。

..
    Example
    =======

サンプル
========

..
    The :func:`getpass()` function prints a prompt then reads input from
    the user until they press return. The input is passed back as a string
    to the caller.

:func:`getpass()` 関数はプロンプトを表示して、改行キーを入力するまでユーザからの入力を読み込みます。その入力は呼び出し側へ文字列として渡されます。

.. include:: getpass_defaults.py
    :literal:
    :start-after: #end_pymotw_header

..
    The default prompt, if none is specified by the caller, is
    "``Password:``".

呼び出し側で何も指定しなければ、デフォルトプロンプトは "``Password:``" です。

::

    $ python getpass_defaults.py
    Password:
    You entered: sekret

..
    The prompt can be changed to any value your program needs.

プロンプトはプログラムに応じて任意の文字列に変更できます。

.. include:: getpass_prompt.py
    :literal:
    :start-after: #end_pymotw_header

..
    I don't recommend such an insecure authentication scheme, but it illustrates
    the point.

私はこのような安全ではない認証スキームを推奨しませんが、これはプロンプトが変更できることを説明します。

::

    $ python getpass_prompt.py
    What is your favorite color?
    Right.  Off you go.
    $ python getpass_prompt.py
    What is your favorite color?
    Auuuuugh!

..
    By default, :func:`getpass()` uses stdout to print the prompt
    string. For a program which may produce useful output on
    :ref:`sys.stdout <sys-input-output>`, it is frequently better to send
    the prompt to another stream such as :ref:`sys.stderr
    <sys-input-output>`.

デフォルトでは、 :func:`getpass()` はプロンプトの文字列を表示するのに標準出力を使用します。 :ref:`sys.stdout <sys-input-output>` へ便利な出力を生成する可能性のあるプログラムには :ref:`sys.stderr <sys-input-output>` のような別のストリームからプロンプトを送ると良いです。

.. include:: getpass_stream.py
    :literal:
    :start-after: #end_pymotw_header

..
    This way standard output can be redirected (to a pipe or file) without seeing
    the password prompt. The value entered by the user is still not echoed back to
    the screen.

この方法は、パスワードプロンプトを表示せずに標準出力が(パイプかファイルへ)リダイレクトされます。それでもユーザが入力した文字はスクリーンへエコーバックされません。

::

    $ python getpass_stream.py >/dev/null
    Password:

..
    Using getpass Without a Terminal
    ================================

ターミナル無しで getpass を使用する
===================================

..
    Under Unix, :func:`getpass()` always requires a tty it can control via
    termios, so echo can be disabled. This means values will not be read
    from a non-terminal stream redirected to standard input.

Unix 環境では、 :func:`getpass()` はターミナル経由で制御できる tty を常に必要とするので表示を無効にできます。これは非ターミナルストリームから標準入力へリダイレクトしてもその入力文字が読み込まれないことになります。

::

    $ echo "sekret" | python getpass_defaults.py
    Traceback (most recent call last):
     File "getpass_defaults.py", line 34, in 
       p = getpass.getpass()
     File "/Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5/getpass.py", line 32, in unix_getpass
       old = termios.tcgetattr(fd)     # a copy to save
    termios.error: (25, 'Inappropriate ioctl for device')

..
    It is up to the caller to detect when the input stream is not a tty and use an
    alternate method for reading in that case.

入力ストリームが tty ではないときは呼び出し側で検出して、そのときは代替方法で読み込みます。

.. include:: getpass_noterminal.py
    :literal:
    :start-after: #end_pymotw_header

..
    With a tty:

tty なら次のようになります。

::

    $ python ./getpass_noterminal.py
    Using getpass:
    Read:  sekret

..
    Without a tty:

tty ではないときは次のようになります。

::

    $ echo "sekret" | python ./getpass_noterminal.py
    Using readline
    Read:  sekret

.. seealso::

    `getpass <http://docs.python.org/library/getpass.html>`_
        .. The standard library documentation for this module.

        本モジュールの標準ライブラリドキュメント

    :mod:`readline`
        .. Interactive prompt library.

        対話的なプロンプトライブラリ
