from latex.build import build_pdf


def test_generates_something():
    min_latex = r"""
\documentclass{article}
\begin{document}
Hello, world!
\end{document}
"""

    pdf = build_pdf(min_latex)

    assert pdf
