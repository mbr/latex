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

.. py:function:: latex.build.build_pdf(source,
                                       latex_cmd='pdflatex',
                                       texinputs=[''],
                                       max_runs=15)

    Generates a PDF from LaTeX a source, using pdflatex and a temporary
    directory, to avoid leaving behind temporary files.

    pdflatex will be run as many times as necessary; at ``max_runs`` runs, an
    exception is raised and the generation is aborted with a
    :class:`RuntimeError`.

    :param source: The LaTeX source.
    :param latex_cmd: The path for the ``pdflatex`` binary to use.
    :param texinputs: Include paths for TeX. An empty string causes the default
                      path to be added (see the tex manpage).
    :param max_runs: Maximum number of reruns.
    :returns: A binary string of the generated PDF file.
