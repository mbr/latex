from latex import build_pdf, LatexBuildError
from latex.errors import parse_log

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


def test_finds_errors_correctly():
    broken_latex = r"""
\documentclass{article}
\begin{document}
All good
\undefinedcontrolsequencehere
\end{document}
"""

    try:
        build_pdf(broken_latex)
    except LatexBuildError as e:
        assert parse_log(e.log) == e.get_errors()
    else:
        assert False, 'no exception raised'
