from latex.build import LatexMkBuilder


def test_xelatex():
    # the example below should not compile on pdflatex, but on xelatex
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
    builder = LatexMkBuilder(variant='xelatex')
    pdf = builder.build_pdf(min_latex)

    assert pdf
