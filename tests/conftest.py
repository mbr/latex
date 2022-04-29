import pytest


@pytest.fixture
def good_minimal_latex():
    "Return a minimal latex code."
    latex_code = r"""
\documentclass{article}
\begin{document}
Hello, world!
\end{document}
"""
    return latex_code


@pytest.fixture
def bad_minimal_latex(good_minimal_latex):
    return good_minimal_latex.replace("begin", "bgin")


@pytest.fixture
def good_extra_latex():
    "A LaTeX code, which only works with lua and xelatex."
    min_latex = r"""
\documentclass[12pt]{article}
\usepackage{fontspec}

\setmainfont{Times New Roman}

 \title{Sample font document}
 \author{Hubert Farnsworth}
 \date{this month, 2014}

\begin{document}

 \maketitle

 This an \textit{example} of document compiled
 with \textbf{xelatex} compiler. LuaLaTeX should
 work fine also.

\end{document}
"""
    return min_latex


@pytest.fixture
def bad_extra_latex(good_extra_latex):
    "A LateX code for lua and xelatex with error."
    return good_extra_latex.replace("title", "ttle")
