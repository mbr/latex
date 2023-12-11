from latex import build_pdf, LatexBuildError


# the following inline latex-document is not valid:
src = r"""
\documentclass{article}\begin{document}
\THISCONTROLSEQUENCEDOESNOTEXIT
\end{document}
"""

# when building, catch the exception and print a clean error message
try:
    build_pdf(src)
except LatexBuildError as e:
    for err in e.get_errors():
        print('Error in {0[filename]}, line {0[line]}: {0[error]}'.format(err))
        # also print one line of context
        print('    {}'.format(err['context'][1]))
        print()
