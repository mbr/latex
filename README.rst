pyLaTeX
=======

.. highlight:: python

Documentation can be found at https://pythonhosted.org/latex .

Allows calling LaTeX from Python without leaving a mess. Similar to the
(officially obsolete) `tex <https://pypi.python.org/pypi/tex/>`_ package, whose
`successor <http://www.profv.de/texcaller/>`_ is not PyPi-installable::

     min_latex = (r"\documentclass{article}"
                  r"\begin{document}"
                  r"Hello, world!"
                  r"\end{document}")

     from latex.build import build_pdf

     # this builds a pdf-file inside a temporary directory
     pdf = build_pdf(min_latex)

     # look at the first few bytes of the header
     print pdf[:10]

Also comes with support for using `Jinja2 <http://jinja.pocoo.org/>`_ templates
to generate LaTeX files.

:py:func:`~latex.jinja2.make_env` can be used to create an
:py:class:`~jinja2.Environment` that plays well with LaTex::

   Variables can be used in a LaTeX friendly way: Hello, \VAR{name|e}.

   Note that autoescaping is off. Blocks are creating using the block macro:

   \BLOCK{if weather is 'good'}
   Hooray.
   \BLOCK{endif}

   \#{comments are supported as well}
   %# and so are line comments

   To keep things short, line statements can be used:

   %- if weather is good
   Yay.
   %- endif
