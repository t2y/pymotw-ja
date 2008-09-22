=====================
BaseHTTPServer
=====================
.. module:: BaseHTTPServer
    :synopsis: Provides base classes for implementing web servers.

:Module: BaseHTTPServer
:Purpose: Provides base classes for implementing web servers.
:Python Version: 1.4 and later
:Abstract:

    The BaseHTTPServer module includes classes which can form the basis of a
    web server.

Description
===========

BaseHTTPServer uses classes from SocketServer to create base classes for
making HTTP servers. HTTPServer can be used directly, but the
BaseHTTPRequestHandler is intended to be extended to handle each protocol
method (GET, POST, etc.).

Simple GET Example
==================

To add support for an HTTP method in your request handler class, implement the
method do_METHOD(), replacing METHOD with the name of the HTTP method. For
example, do_GET(), do_POST(), etc. For consistency, the method takes no
arguments. All of the parameters for the request are parsed by
BaseHTTPRequestHandler and stored as instance attributes where you can easily
retrieve them.

This example request handler illustrates how to return a response to the
client and some of the local attributes which can be useful in building the
response:

::

    from BaseHTTPServer import BaseHTTPRequestHandler
    import urlparse

    class GetHandler(BaseHTTPRequestHandler):
        
        def do_GET(self):
            parsed_path = urlparse.urlparse(self.path)
            message = '\n'.join([
                    'CLIENT VALUES:',
                    'client_address=%s (%s)' % (self.client_address,
                                                self.address_string()),
                    'command=%s' % self.command,
                    'path=%s' % self.path,
                    'real path=%s' % parsed_path.path,
                    'query=%s' % parsed_path.query,
                    'request_version=%s' % self.request_version,
                    '',
                    'SERVER VALUES:',
                    'server_version=%s' % self.server_version,
                    'sys_version=%s' % self.sys_version,
                    'protocol_version=%s' % self.protocol_version,
                    '',
                    ]) 
            self.send_response(200)
            self.end_headers()
            self.wfile.write(message)
            return

The message text is assembled and then written to self.wfile, the file handle
wrapping the response socket. Each response needs a response code, set via
self.send_response(). If an error code is used (404, 501, etc.), an
appropriate default error message is included in the header, or you can pass a
message along with the error code.

To run the request handler in a server, pass it to the constructor of
HTTPServer.

::

    if __name__ == '__main__':
        from BaseHTTPServer import HTTPServer
        server = HTTPServer(('localhost', 8080), GetHandler)
        print 'Starting server, use <Ctrl-C> to stop'
        server.serve_forever()

Then start the server:

::

    $ python BaseHTTPServer_GET.py 
    Starting server, use  to stop

And in a separate terminal, use curl to access it:

::

    $ curl -i http://localhost:8080/?foo=barHTTP/1.0 200 OK
    Server: BaseHTTP/0.3 Python/2.5.1
    Date: Sun, 09 Dec 2007 16:00:34 GMT

    CLIENT VALUES:
    client_address=('127.0.0.1', 51275) (localhost)
    command=GET
    path=/?foo=bar
    real path=/
    query=foo=bar
    request_version=HTTP/1.1

    SERVER VALUES:
    server_version=BaseHTTP/0.3
    sys_version=Python/2.5.1
    protocol_version=HTTP/1.0

Threading and Forking
=====================

HTTPServer is a simple subclass of SocketServer.TCPServer, and does not use
multiple threads or processes to handle requests. To add threading or forking,
create a new class using the appropriate mix-in from SocketServer.

::

    from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
    from SocketServer import ThreadingMixIn
    import threading

    class Handler(BaseHTTPRequestHandler):
        
        def do_GET(self):
            self.send_response(200)
            self.end_headers()
            message =  threading.currentThread().getName()
            self.wfile.write(message)
            self.wfile.write('\n')
            return

    class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
        """Handle requests in a separate thread."""

    if __name__ == '__main__':
        server = ThreadedHTTPServer(('localhost', 8080), Handler)
        print 'Starting server, use <Ctrl-C> to stop'
        server.serve_forever()

Each time a request comes in, a new thread or process is created to handle it:

::

    $ curl http://localhost:8080/
    Thread-1
    $ curl http://localhost:8080/
    Thread-2
    $ curl http://localhost:8080/
    Thread-3

Swapping ForkingMixIn for ThreadingMixIn above would achieve similar results,
using separate processes instead of threads.

POST
====

Supporting POST requests is a little more work, because the base class does
not parse the form data for us. The cgi module provides the FieldStorage class
which knows how to parse the form, if we give it the correct inputs.

::

    from BaseHTTPServer import BaseHTTPRequestHandler
    import cgi

    class PostHandler(BaseHTTPRequestHandler):
        
        def do_POST(self):
            # Parse the form data posted
            form = cgi.FieldStorage(
                fp=self.rfile, 
                headers=self.headers,
                environ={'REQUEST_METHOD':'POST',
                         'CONTENT_TYPE':self.headers['Content-Type'],
                         })

            # Begin the response
            self.send_response(200)
            self.end_headers()
            self.wfile.write('Client: %s\n' % str(self.client_address))
            self.wfile.write('Path: %s\n' % self.path)
            self.wfile.write('Form data:\n')

            # Echo back information about what was posted in the form
            for field in form.keys():
                field_item = form[field]
                if field_item.filename:
                    # The field contains an uploaded file
                    file_data = field_item.file.read()
                    file_len = len(file_data)
                    del file_data
                    self.wfile.write('\tUploaded %s (%d bytes)\n' % (field, 
                                                                     file_len))
                else:
                    # Regular form value
                    self.wfile.write('\t%s=%s\n' % (field, form[field].value))
            return

    if __name__ == '__main__':
        from BaseHTTPServer import HTTPServer
        server = HTTPServer(('localhost', 8080), PostHandler)
        print 'Starting server, use <Ctrl-C> to stop'
        server.serve_forever()

Using curl again, we can include form data, which automatically sets the
method to POST. The last argument, ``-F datafile=@BaseHTTPServer_GET.py``, posts
the contents of the file BaseHTTPServer_GET.py to illustrate reading file data
from the form.

::

    $ curl http://localhost:8080/ -F name=dhellmann -F foo=bar -F  datafile=@BaseHTTPServer_GET.py
    Client: ('127.0.0.1', 51128)
    Path: /
    Form data:
            name=dhellmann
            foo=bar
            Uploaded datafile (2222 bytes)


Errors
======

Error handling is made easy with the send_error() method. Simply pass the
appropriate error code and an optional error message, and the entire response
(with headers, status code, and body) is generated for you.

::

    from BaseHTTPServer import BaseHTTPRequestHandler

    class ErrorHandler(BaseHTTPRequestHandler):
        
        def do_GET(self):
            self.send_error(404)
            return

    if __name__ == '__main__':
        from BaseHTTPServer import HTTPServer
        server = HTTPServer(('localhost', 8080), ErrorHandler)
        print 'Starting server, use <Ctrl-C> to stop'
        server.serve_forever()


In this case, a 404 error is always returned.

::

    $ curl -i http://localhost:8080/
    HTTP/1.0 404 Not Found
    Server: BaseHTTP/0.3 Python/2.5.1
    Date: Sun, 09 Dec 2007 15:49:44 GMT
    Content-Type: text/html
    Connection: close

    <head>
    <title>Error response</title>
    </head>
    <body>
    <h1>Error response</h1>
    <p>Error code 404.
    <p>Message: Not Found.
    <p>Error code explanation: 404 = Nothing matches the given URI.
    </body>

