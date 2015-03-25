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


ESCAPE_RE = re.compile(r'|'.join(re.escape(k) for k in
                                 sorted(CHAR_ESCAPE.keys())))


def escape_chars(s):
    return ESCAPE_RE.sub(lambda m: CHAR_ESCAPE[m.group()], s)
