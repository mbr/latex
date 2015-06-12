.. include:: ../README.rst


More examples
-------------

Reading ``latex``-source from a file:

.. literalinclude:: examples/ex1.latex
   :caption: ex1.latex
   :language: tex

.. literalinclude:: examples/ex1.py
   :caption: ex1.py


Using the `Jinja2 <http://jinja.pocoo.org/>`_-template support:


.. literalinclude:: examples/ex2.latex
   :caption: ex2.latex
   :language: tex

.. literalinclude:: examples/ex2.py
   :caption: ex2.py


Since the LaTeX source file is copied to a temporary directory, no additional
files of the same folder are found by TeX by default. This is alleviated by
using the ``TEXINPUTS`` [1]_ environment variable:

.. literalinclude:: examples/ex3.latex
   :caption: ex3.latex
   :language: tex

.. literalinclude:: examples/ex3.sty
   :caption: ex3.sty
   :language: tex

.. literalinclude:: examples/ex3.py
   :caption: ex3.py

.. [1] See ``man 1 tex``, the ``TEXINPUTS`` section.


API
===

.. autofunction:: latex.escape

.. automodule:: latex.build
   :members:

.. autofunction:: latex.jinja2.make_env

.. automodule:: latex.exc
   :members:
