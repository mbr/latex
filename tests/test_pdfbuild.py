from latex import build_pdf
from latex.exc import LatexBuildError

import pytest


def test_generates_something():
    min_latex = r"""
\documentclass{article}
\begin{document}
Hello, world!
\end{document}
"""

    pdf = build_pdf(min_latex)

    assert pdf


def test_raises_correct_exception_on_fail():
    broken_latex = r"""foo"""

    with pytest.raises(LatexBuildError):
        build_pdf(broken_latex)
