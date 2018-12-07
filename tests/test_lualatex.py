from latex import build_pdf, LatexBuildError
from latex.build import LatexMkBuilder


# the example below should not compile on pdflatex, but on lualatex
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

def test_lualatex():
    builder = LatexMkBuilder(variant='lualatex')
    pdf = builder.build_pdf(min_latex)

    assert pdf


def test_lualatexmk():
    pdf = build_pdf(min_latex, builder='lualatexmk')

    assert pdf


def test_luatextmk_errorlog():
    """Check if parsing of error lines works."""
    f_min_latex = min_latex.replace(r"\maketitle", r"\makexxx")
    try:
        build_pdf(f_min_latex, builder='lualatexmk')
    except LatexBuildError as err:
        assert err.get_errors()
