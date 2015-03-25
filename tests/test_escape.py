from latex import escape_chars


def test_escape_chars():
    inp = u'He%%llo~ World$!'
    out = u'He\\%\\%llo\\textasciitilde{} World\\$!'

    assert out == escape_chars(inp)
