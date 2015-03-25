LaTeX wrappers
==============

Allows calling LaTeX from Python script without leaving a mess. Similar to the
(officially obsolete) `tex <https://pypi.python.org/pypi/tex/>`_ package, whose
successor is not PyPi-installable.

Also comes with support for using `Jinja2 <http://jinja.pocoo.org/>`_ templates
to generate LaTeX files.


API
===

.. py:method:: latex.escape(s, fold_newlines=True)

   Escapes a string to make it usable in LaTeX text mode. Will replace special
   characters as well as newlines.

   :param s: The string to escape.
   :param fold_newlines: If true, multiple newlines will be reduced to just a
                         single ``\\``. Otherwise, whitespace is kept intact
                         by adding multiple ``[n\baselineskip]``.
