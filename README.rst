latex
=====

Documentation can be found at https://pythonhosted.org/latex .

Allows calling LaTeX from Python without leaving a mess. Similar to the
(officially obsolete) `tex <https://pypi.python.org/pypi/tex/>`_ package, whose
`successor <http://www.profv.de/texcaller/>`_ is not PyPi-installable:

.. code-block:: python

     min_latex = (r"\documentclass{article}"
                  r"\begin{document}"
                  r"Hello, world!"
                  r"\end{document}")

     from latex import build_pdf

     # this builds a pdf-file inside a temporary directory
     pdf = build_pdf(min_latex)

     # look at the first few bytes of the header
     print bytes(pdf)[:10]

Also comes with support for using `Jinja2 <http://jinja.pocoo.org/>`_ templates
to generate LaTeX files.

``make_env`` can be used to create an ``Environment`` that plays well with
LaTex::

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


Example use
-----------

.. code-block:: python

    from jinja2.loaders import FileSystemLoader
    from latex.jinja2 import make_env

    env = make_env(loader=FileSystemLoader('.'))
    tpl = env.get_template('doc.latex')

    print(tpl.render(name="Alice"))

The ``base.latex`` demonstrates how ``\BLOCK{...}`` is substituted for
``{% ... %}``:

.. code-block:: latex

    \documentclass{article}
    \begin{document}
    \BLOCK{block body}\BLOCK{endblock}
    \end{document}

Finally, ``doc.latex`` shows why the ``%-`` syntax is usually preferable:

.. code-block:: latex

    %- extends "base.latex"

    %- block body
    Hello, \VAR{name|e}.
    %- endblock


Translations using Babel
------------------------

Strings from ``.latex``-templates can be extracted, provided your  `babel.cfg` is setup correctly:

.. code-block:: ini

    [jinja2: *.latex]
    block_start_string = \BLOCK{
    block_end_string = }
    variable_start_string = \VAR{
    variable_end_string = }
    comment_start_string = \#{
    comment_end_string = }
    line_statement_prefix = %-
    line_comment_prefix = %#
    trim_blocks = True
    autoescape = False
