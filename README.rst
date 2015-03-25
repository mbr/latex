LaTeX wrappers
==============

Allows calling LaTeX from Python script without leaving a mess. Similar to the
(officially obsolete) `tex <https://pypi.python.org/pypi/tex/>`_ package, whose
successor is not PyPi-installable.

Also comes with support for using `Jinja2 <http://jinja.pocoo.org/>`_ templates
to generate LaTeX files.


Jinja2 templates
~~~~~~~~~~~~~~~~

:py:function:`~latex.jinja2.make_env` can be used to create an
:py:class:`~jinja2.Environment` that plays well with LaTex:

.. highlight:: jinja2

   Variables can be used in a LaTeX friendly way: Hello, \VAR{name|e}.

   Note that autoescaping is off. Blocks are creating using the block macro:

   \BLOCK{if weather is 'good'}
   Hooray.
   \BLOCK{endif}

   \#{comments are supported as well}
   %# and so are line comments

   To keep things short, line statements can be used:

   %- if weather is good
   %- endif


API
===

.. py:function:: latex.escape(s, fold_newlines=True)

   Escapes a string to make it usable in LaTeX text mode. Will replace special
   characters as well as newlines.

   :param s: The string to escape.
   :param fold_newlines: If true, multiple newlines will be reduced to just a
                         single ``\\``. Otherwise, whitespace is kept intact
                         by adding multiple ``[n\baselineskip]``.
