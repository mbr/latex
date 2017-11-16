from latex.build import LatexMkBuilder


def test_xelatex():
    min_latex = r"""
\documentclass{article}
\begin{document}
Hello, world!
\end{document}
"""
    builder = LatexMkBuilder(variant='xelatex')
    pdf = builder.build_pdf(min_latex)

    assert pdf
