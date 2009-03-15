======================
Cookie -- HTTP Cookies
======================

.. module:: Cookie
    :synopsis: Working with HTTP cookies from the server side.

:Purpose: The Cookie module defines classes for parsing and creating HTTP cookie headers.
:Python Version: 2.1 and later

Cookies have been a part of the HTTP protocol for a long time. All of the
modern web development frameworks provide easy access to cookies so a
programmer almost never has to worry about how to format them or make sure the
headers are sent properly. It can be instructive to understand how cookies
work, though, and the options available.

The Cookie module implements a parser for cookies that is mostly RFC 2109
compliant. It is a little less strict than the standard because MSIE 3.0x does
not support the entire standard.

Creating and Setting a Cookie
=============================

Cookies are used as state management, and as such as usually set by the server
to be stored and returned by the client. The most trivial example of creating
a cookie looks something like:

.. include:: Cookie_setheaders.py
    :literal:
    :start-after: #end_pymotw_header

The output is a valid Set-Cookie header ready to be passed to the client as
part of the HTTP response:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'Cookie_setheaders.py'))
.. }}}
.. {{{end}}}


Morsels
=======

It is also possible to control the other aspects of a cookie, such as the
expiration, path, and domain. In fact, all of the RFC attributes for cookies
can be managed through the Morsel object representing the cookie value.

.. include:: Cookie_Morsel.py
    :literal:
    :start-after: #end_pymotw_header

The above example includes two different methods for setting stored cookies
that expire. You can set max-age to a number of seconds, or expires to a date
and time when the cookie should be discarded.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'Cookie_Morsel.py'))
.. }}}
.. {{{end}}}


Both the Cookie and Morsel objects act like dictionaries. The Morsel responds
to a fixed set of keys:

- expires
- path
- comment
- domain
- max-age
- secure
- version

The keys for the Cookie instance are the names of the individual cookies being
stored. That information is also available from the key attribute of the
Morsel.

Encoded Values
==============

The cookie header may require values to be encoded so they can be parsed
properly. 

.. include:: Cookie_coded_value.py
    :literal:
    :start-after: #end_pymotw_header

The Morsel.value is always the decoded value of the cookie, while
Morsel.coded_value is always the representation to be used for transmitting
the value to the client. Both values are always strings. Values saved to a
cookie that are not strings are converted automatically.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'Cookie_coded_value.py'))
.. }}}
.. {{{end}}}

Receiving and Parsing Cookie Headers
====================================

Once the Set-Cookie headers are received by the client, it will return those
cookies to the server on subsequent requests using the Cookie header. The
incoming header will look like::

    Cookie: integer=5; string_with_quotes="He said, \"Hello, World!\""

The cookies are either available directly from the headers or, depending on
your web server/framework, the HTTP_COOKIE environment variable. To decode
them, pass the string without the header prefix to the SimpleCookie when
instantiating it, or use the load() method.

.. include:: Cookie_parse.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'Cookie_parse.py'))
.. }}}
.. {{{end}}}

Alternative Output Formats
==========================

Besides using the Set-Cookie header, it is possible to use JavaScript to add
cookies to a client. SimpleCookie and Morsel provide JavaScript output via the
js_output() method.

.. include:: Cookie_js_output.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'Cookie_js_output.py'))
.. }}}
.. {{{end}}}


Deprecated Classes
==================

All of these examples have used SimpleCookie. The Cookie module also provides
2 other classes, SerialCookie and SmartCookie. SerialCookie can handle any
values that can be pickled. SmartCookie figures out whether a value needs to
be unpickled or if it is a simple value. Since both of these classes use
pickles, they are potential security holes in your application and you should
not use them. It is safer to store state on the server, and give the client a
session key instead.

.. seealso::

    `Cookie <http://docs.python.org/library/cookie.html>`_
        The standard library documentation for this module.

    :mod:`cookielib`
        The :mod:`cookielib` module, for working with cookies on the client-side.

    `RFC 2109`_
        RFC 2109 -- HTTP State Management Mechanism
        
        .. _RFC 2109: http://www.ietf.org/rfc/rfc2109.txt
