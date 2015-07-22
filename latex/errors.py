import re

LATEX_ERR_RE = re.compile(r'(?P<filename>[^:]+):(?P<line>[0-9]*):'
                          r'\s*(?P<error>.*)')


def parse_log(log, context_size=3):
    lines = log.splitlines()
    errors = []

    for n, line in enumerate(lines):
        m = LATEX_ERR_RE.match(line)
        if m:
            err = m.groupdict().copy()
            err['context'] = lines[n:n+context_size]
            err['line'] = int(err['line'])
            errors.append(err)

    return errors
