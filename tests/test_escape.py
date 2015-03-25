from latex import escape_chars


def test_escape_chars():
    inp = u'He%%llo~ World$!'
    out = u'He\\%\\%llo\\textasciitilde{} World\\$!'

    assert out == escape_chars(inp)


def test_newline_escape():
    inp = 'Hello\n\n\nWorld'
    out = r'Hello\\World'

    assert out == escape_chars(inp)


def test_newline_escape_no_folding():
    inp = 'Hello\n\n\nWorld'
    out = r'Hello\\[3\baselineskip]World'

    assert out == escape_chars(inp, False)
