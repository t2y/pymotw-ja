================================================
 Addressing, Protocol Families and Socket Types
================================================

A *socket* is one endpoint of a communication channel used by programs
to pass data back and forth locally or across the Internet.  Sockets
have two primary properties controlling the way they send data: the
*address family* controls the OSI network layer protocol used and the
*socket type* controls the transport layer protocol.

Python supports three address families.  The most common,
:const:`AF_INET`, is used for IPv4 Internet addressing.  IPv4
addresses are made up of four octal values separated by dots (e.g.,
``10.1.1.5`` and ``127.0.0.1``).  These values are more commonly
referred to as "IP addresses."  Almost all Internet networking is done
using IP version 4 at this time.

:const:`AF_INET6` is used for IPv6 Internet addressing.  IPv6 is the
"next generation" version of the Internet protocol, and supports
128-bit addresses, traffic shaping, and routing features not available
under IPv4.  Adoption of IPv6 is still limited, but continues to grow.

:const:`AF_UNIX` is the address family for Unix Domain Sockets (UDS),
an interprocess communication protocol available on POSIX-compliant
systems.  The implementation of UDS typically allows the operating
system to pass data directly from process to process, without going
through the network stack.  This is more efficient than using
:const:`AF_INET`, but because the filesystem is used as the namespace
for addressing, UDS is restricted to processes on the same system.
The appeal of using UDS over other IPC mechanisms such as named pipes
or shared memory is that the programming interface is the same as for
IP networking, so the application can take advantage of efficient
communication when running on a single host, but use the same code
when sending data across the network.

.. note::

  The :const:`AF_UNIX` constant is only defined on systems where UDS
  is supported.

The socket type is usually either :const:`SOCK_DGRAM` for
*user datagram protocol* (UDP) or :const:`SOCK_STREAM` for
*transmission control protocol* (TCP).  UDP does not require
transmission handshaking or other setup, but offers lower reliability
of delivery.  UDP messages may be delivered out of order, more than
once, or not at all.  TCP, by contrast, ensures that each message is
delivered exactly once, and in the correct order.  Most application
protocols that deliver a large amount of data, such as HTTP, are built
on top of TCP.  UDP is commonly used for protocols where order is less
important (since the message fits in a single packet, i.e., DNS), or
for *multicasting* (sending the same data to several hosts).

.. note::

  Python's :mod:`socket` module supports other socket types but they
  are less commonly used, so are not covered here.  Refer to the
  standard library documentation for more details.

Looking up Hosts on the Network
===============================

:mod:`socket` includes functions to interface with the domain name
services on the network, to convert the host name of a server into its
numerical network address.  Applications do not need to convert
addresses explicitly before using them to connect to a server, but it
can be useful when reporting errors to include the numerical address
as well as the name value being used.

To find the official name of the current host, use
:func:`gethostname`.

.. include:: socket_gethostname.py
   :literal:
   :start-after: #end_pymotw_header

The name returned will depend on the network settings for the current
system, and may change if it is on a different network (such as a
laptop attached to a wireless LAN).

::

	$ python socket_gethostname.py

	farnsworth.hellfly.net

Use :func:`gethostbyname` to convert the name of a server to its
numerical address:

.. include:: socket_gethostbyname.py
   :literal:
   :start-after: #end_pymotw_header

The name argument does not need to be a fully qualified name (i.e., it
does not need to include the domain name as well as the base
hostname).  If the name cannot be found, an exception of type
:class:`socket.error` is raised.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'socket_gethostbyname.py'))
.. }}}
.. {{{end}}}

For access to more naming information about a server, use
:func:`gethostbyname_ex`.  It returns the canonical hostname of the
server, any aliases, and all of the available IP addresses that can be
used to reach it.

.. include:: socket_gethostbyname_ex.py
   :literal:
   :start-after: #end_pymotw_header

Having all known IP addresses for a server lets a client implement its
own load balancing or fail-over algorithms.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'socket_gethostbyname_ex.py'))
.. }}}
.. {{{end}}}

Use :func:`getfqdn` to convert a partial name to a fully qualified
domain name.

.. include:: socket_getfqdn.py
   :literal:
   :start-after: #end_pymotw_header

The name returned will not necessarily match the input argument in any
way if the input is an alias, such as ``www`` is here.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'socket_getfqdn.py'))
.. }}}
.. {{{end}}}

When the address of a server is available, use :func:`gethostbyaddr`
to do a "reverse" lookup for the name.

.. include:: socket_gethostbyaddr.py
   :literal:
   :start-after: #end_pymotw_header

The return value is a tuple containing the full hostname, any aliases,
and all IP addresses associated with the name.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'socket_gethostbyaddr.py'))
.. }}}
.. {{{end}}}

Finding Service Information
===========================

In addition to an IP address, each socket address includes an integer
*port number*.  Many applications can run on the same host, listening
on a single IP address, but only one socket at a time can use a port
at that address.  The combination of IP address, protocol, and port
number uniquely identify a communication channel and ensure that
messages sent through a socket arrive at the correct destination.

Some of the port numbers are pre-allocated for a specific protocol.
For example, communication between email servers using SMTP occurs
over port number 25 using TCP, and web clients and servers use port 80
for HTTP.  The port numbers for network services with standardized
names can be looked up with :func:`getservbyname`.

.. include:: socket_getservbyname.py
   :literal:
   :start-after: #end_pymotw_header

Although a standardized service is unlikely to change ports, looking
up the value with a system call instead of hard-coding it is more
flexible when new services are added in the future.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'socket_getservbyname.py'))
.. }}}
.. {{{end}}}

To reverse the service port lookup, use :func:`getservbyport`.

.. include:: socket_getservbyport.py
   :literal:
   :start-after: #end_pymotw_header

The reverse lookup is useful for constructing URLs to services from
arbitrary addresses.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'socket_getservbyport.py'))
.. }}}
.. {{{end}}}

The number assigned to a transport protocol can be retrieved with
:func:`getprotobyname`.

.. include:: socket_getprotobyname.py
   :literal:
   :start-after: #end_pymotw_header

The values for protocol numbers are standardized, and defined as
constants in :mod:`socket` with the prefix ``IPPROTO_``.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'socket_getprotobyname.py'))
.. }}}
.. {{{end}}}


Looking Up Server Addresses
===========================

:func:`getaddrinfo` converts the basic address of a service into a
list of tuples with all of the information necessary to make a
connection.  The contents of each tuple will vary, containing
different network families or protocols.

.. include:: socket_getaddrinfo.py
   :literal:
   :start-after: #end_pymotw_header

This program demonstrates how to look up the connection information
for ``www.python.org``.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'socket_getaddrinfo.py'))
.. }}}
.. {{{end}}}

:func:`getaddrinfo` takes several arguments to filter the result
list. The *host* and *port* values given in the example are required
arguments.  The optional arguments are *family*, *socktype*, *proto*,
and *flags*.  The family, socktype, and proto values should be ``0``
or one of the constants defined by :mod:`socket`.

.. include:: socket_getaddrinfo_extra_args.py
   :literal:
   :start-after: #end_pymotw_header

Since *flags* includes :const:`AI_CANONNAME` the canonical name of the
server (different from the value used for the lookup) is included in
the results this time.  Without the flag, the canonical name value is
left empty.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'socket_getaddrinfo_extra_args.py'))
.. }}}
.. {{{end}}}

IP Address Representations
==========================

Network programs written in C use the data type :class:`struct
sockaddr` to represent IP addresses as binary values (instead of the
string addresses usually found in Python programs).  Convert IPv4
addresses between the Python representation and the C representation
with :func:`inet_aton` and :func:`inet_ntoa`.

.. include:: socket_address_packing.py
   :literal:
   :start-after: #end_pymotw_header

The four bytes in the packed format can be passed to C libraries,
transmitted safely over the network, or saved to a database compactly.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'socket_address_packing.py 192.168.1.1'))
.. cog.out(run_script(cog.inFile, 'socket_address_packing.py 127.0.0.1', include_prefix=False))
.. }}}
.. {{{end}}}

The related functions :func:`inet_pton` and :func:`inet_ntop` work
with both IPv4 and IPv6 addresses, producing the appropriate format
based on the address family parameter passed in.

.. include:: socket_ipv6_address_packing.py
   :literal:
   :start-after: #end_pymotw_header

An IPv6 address is already a hexadecimal value, so converting the
packed version to a series of hex digits produces a string similar to
the original value.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'socket_ipv6_address_packing.py 2002:ac10:10a:1234:21e:52ff:fe74:40e'))
.. }}}
.. {{{end}}}

.. seealso::


    `Wikipedia: IPv6 <http://en.wikipedia.org/wiki/IPv6>`__
        Article discussing Internet Protocol Version 6 (IPv6).

    `Wikipedia: OSI Networking Model <http://en.wikipedia.org/wiki/OSI_model>`__
        Article describing the seven layer model of networking implementation.

    `Assigned Internet Protocol Numbers <http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xml>`__
        List of standard protocol names and numbers.
