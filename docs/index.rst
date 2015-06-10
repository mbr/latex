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



API
===

.. autofunction:: latex.escape

.. automodule:: latex.build
   :members:

.. autofunction:: latex.jinja2.make_env

.. automodule:: latex.exc
   :members:
