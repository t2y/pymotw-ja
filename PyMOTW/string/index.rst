======
string
======
.. module:: string
    :synopsis: Contains useful constants and classes for working with text.

:Module: string
:Purpose: Contains useful constants and classes for working with text.
:Python Version: 2.5
:Abstract:

    Although most of the functions it used to contain have moved to methods
    of string and unicode objects, the string module still contains several
    useful items.

Description
===========

The string module dates from the earliest versions of Python. In version 2.0,
many of the functions previously implemented only in the module were moved to
methods of string objects. Legacy versions of those functions are still
available, but their use is deprecated and they will be dropped in Python 3.0.
The string module still contains several useful constants and classes for
working with string and unicode objects, and this discussion will concentrate
on them.

Constants
=========

The constants in the string module can be used to specify categories of
characters such as ascii_letters and digits. Some of the constants are
locale-dependent, such as lowercase, so the value changes to reflect the
language settings of the user. Others, such as hexdigits, do not change when
the locale changes.

::

    import string

    for n in dir(string):
        if n.startswith('_'):
            continue
        v = getattr(string, n)
        if isinstance(v, basestring):
            print '%s=%s' % (n, repr(v))
            print

Most of the names for the constants are self-explanatory.

::

    $ python string_constants.py
    ascii_letters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    ascii_lowercase='abcdefghijklmnopqrstuvwxyz'

    ascii_uppercase='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    digits='0123456789'

    hexdigits='0123456789abcdefABCDEF'

    letters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    lowercase='abcdefghijklmnopqrstuvwxyz'

    octdigits='01234567'

    printable='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'

    punctuation='!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

    uppercase='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    whitespace='\t\n\x0b\x0c\r '


Functions
=========

There are two functions not moving from the string module. capwords()
capitalizes all of the words in a string.

::

    import string

    s = 'The quick brown fox jumped over the lazy dog.'

    print s
    print string.capwords(s)

The results are the same as if you called split(), capitalized the words in
the resulting list, then called join() to combine the results.

::

    $ python string_capwords.py
    The quick brown fox jumped over the lazy dog.
    The Quick Brown Fox Jumped Over The Lazy Dog.

The other function creates translation tables that can be used with the
translate() method to change one set of characters to another.

::

    import string

    leet = string.maketrans('abegiloprstz', '463611092572')

    s = 'The quick brown fox jumped over the lazy dog.'

    print s
    print s.translate(leet)


In this example, some letters are replaced by their l33t number alternatives.

::

    $ python string_maketrans.py
    The quick brown fox jumped over the lazy dog.
    Th3 qu1ck 620wn f0x jum93d 0v32 7h3 142y d06.

Templates
=========

String templates were added in Python 2.4 as part of PEP 292 and are intended
as an alternative to the built-in interpolation syntax. With string.Template
interpolation, variables are identified by name prefixed with $ (e.g., '$var')
or, if necessary to set them off from surrounding text, they can also be
wrapped with curly braces (e.g., '${var}').

This example compares a simple template with a similar string interpolation
setup::

    import string

    values = { 'var':'foo' }

    t = string.Template("""
    $var
    $$
    ${var}iable
    """)

    print 'TEMPLATE:', t.substitute(values)

    s = """
    %(var)s
    %%
    %(var)siable
    """

    print 'INTERPLOATION:', s % values

As you see, in both cases the trigger character ($ or %) is escaped by
repeating it twice.

::

    $ python string_template.py
    TEMPLATE: 
    foo
    $
    fooiable

    INTERPLOATION: 
    foo
    %
    fooiable

One key difference between templates and standard string interpolation is that
the type of the arguments is not taken into account. The values are converted
to strings and the strings are inserted. No formatting options are available.
For example, there is no way to control the number of digits used to represent
a floating point value.

A benefit, though, is that by using the safe_substitute() method, it is
possible to avoid exceptions if not all of the values needed by the template
are provided as arguments.

::

    import string

    values = { 'var':'foo' }

    t = string.Template("$var is here but $missing is not provided")

    try:
        print 'TEMPLATE:', t.substitute(values)
    except KeyError, err:
        print 'ERROR:', str(err)
        
    print 'TEMPLATE:', t.safe_substitute(values)

Since there is no value for missing in the values dictionary, a KeyError is
raised by substitute(). Instead of raising the error, safe_substitute()
catches it and leaves the variable expression alone in the text.

::

    $ python string_template_missing.py
    TEMPLATE: ERROR: 'missing'
    TEMPLATE: foo is here but $missing is not provided

Advanced Templates
==================

If the default syntax for string.Template is not to your liking, you can
change the behavior by adjusting the regular expression patterns it uses to
find the variable names in the template body. A simple way to do that is to
change the delimiter and idpattern class attributes.

::

    import string

    class MyTemplate(string.Template):
        delimiter = '%'
        idpattern = '[a-z]+_[a-z]+'

    t = MyTemplate('%% %with_underscore %notunderscored')
    d = { 'with_underscore':'replaced', 
          'notunderscored':'not replaced',
          }

    print t.safe_substitute(d)

In this example, variable ids must include an underscore somewhere in the
middle, so %notunderscored is not replaced by anything.

::

    $ python string_template_advanced.py
    % replaced %notunderscored

For more complex changes, you can override the pattern attribute and define an
entirely new regular expression. The pattern provided must contain 4 named
groups for capturing the escaped delimiter, the named variable, a braced
version of the variable name, and invalid delimiter patterns.

Let's look at the default pattern::

    import string

    t = string.Template('$var')
    print t.pattern.pattern

Since t.pattern is a compiled regular expression, we have to access its
pattern attribute to see the actual string.

::

    $ python string_template_defaultpattern.py

        \$(?:
          (?P<escaped>\$) |   # Escape sequence of two delimiters
          (?P<named>[_a-z][_a-z0-9]*)      |   # delimiter and a Python identifier
          {(?P<braced>[_a-z][_a-z0-9]*)}   |   # delimiter and a braced identifier
          (?P<invalid>)              # Other ill-formed delimiter exprs
        )

If we wanted to create a new type of template using, for example, {{var}} as
the variable syntax, we could use a pattern like this::

    import re
    import string

    class MyTemplate(string.Template):
        delimiter = '{{'
        pattern = re.compile(r'''
        \{\{(?:
        (?P<escaped>\{\{)|
        (?P<named>[_a-z][_a-z0-9]*)\}\}|
        (?P<braced>[_a-z][_a-z0-9]*)\}\}|
        (?P<invalid>)
        )
        ''', re.VERBOSE | re.DOTALL)
        
    t = MyTemplate('''
    {{{{
    {{var}}
    ''')

    print 'MATCHES:', t.pattern.findall(t.template)
    print 'SUBSTITUTED:', t.safe_substitute(var='replacement')

Notice that we still have to provide both the named and braced patterns, even
though they are the same. Here's the output::

    $ python string_template_newsyntax.py
    MATCHES: [('{{', '', '', ''), ('', 'var', '', '')]
    SUBSTITUTED: 
    {{
    replacement

Deprecated Functions
====================

For information on the deprecated functions moved to the string and unicode
classes, refer to String Methods in the manual.

