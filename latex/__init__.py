import re

CHAR_ESCAPE = {
    u'&': u'\\&',
    u'%': u'\\%',
    u'$': u'\\$',
    u'#': u'\\#',
    u'_': u'\\_',
    u'{': u'\\{',
    u'}': u'\\}',
    u'~': u'\\textasciitilde{}',
    u'^': u'\\textasciicircum{}',
    u'\\': u'\\textbackslash{}',

    # these may be optional:
    u'<': u'\\textless{}',
    u'>': u'\\textgreater{}',
    u'|': u'\\textbar{}',
    u'"': u'\\textquoteddbl{}',
}


def _tbl_re(tbl):
    return re.compile(r'|'.join(re.escape(k) for k in sorted(tbl.keys())))


def _re_translate(exp, tbl, s):
    return exp.sub(lambda m: tbl[m.group()], s)


ESCAPE_RE = _tbl_re(CHAR_ESCAPE)


def escape_chars(s):
    return _re_translate(ESCAPE_RE, CHAR_ESCAPE, s)
