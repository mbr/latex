import re

from .exc import LatexBuildError
from .build import build_pdf

CHAR_ESCAPE = {
    '&': '\\&',
    '%': '\\%',
    '$': '\\$',
    '#': '\\#',
    '_': '\\_',
    '{': '\\{',
    '}': '\\}',
    '~': '\\textasciitilde{}',
    '^': '\\textasciicircum{}',
    '\\': '\\textbackslash{}',

    # these may be optional:
    '<': '\\textless{}',
    '>': '\\textgreater{}',
    '|': '\\textbar{}',
    '"': '\\textquotedbl{}',

    # to prevent issues with '\\' linebreaks
    '[': '{[}',
    ']': '{]}',
}


def _sub_tbl(tbl):
    return r'|'.join(re.escape(k) for k in sorted(tbl.keys()))


ESCAPE_RE = re.compile(r'\n+|' + _sub_tbl(CHAR_ESCAPE))


def escape(s, fold_newlines=True):
    """Escapes a string to make it usable in LaTeX text mode. Will replace
    special characters as well as newlines.

    Some problematic characters like ``[`` and ``]`` are escaped into groups
    (e.g. ``{[}``), because they tend to cause problems when mixed with ``\\``
    newlines otherwise.

    :param s: The string to escape.
    :param fold_newlines: If true, multiple newlines will be reduced to just a
                          single ``\\``. Otherwise, whitespace is kept intact
                          by adding multiple ``[n\baselineskip]``.
    """

    def sub(m):
        c = m.group()
        if c in CHAR_ESCAPE:
            return CHAR_ESCAPE[c]

        if c.isspace():
            if fold_newlines:
                return r'\\'
            return r'\\[{}\baselineskip]'.format(len(c))

    return ESCAPE_RE.sub(sub, s)
