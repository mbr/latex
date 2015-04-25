import os


class LatexError(Exception):
    pass


class LatexBuildError(LatexError):
    """LaTeX call exception."""

    def __init__(self, logfn=None):
        if os.path.exists(logfn):
            self.log = open(logfn).read()
        else:
            self.log = None

    def __str__(self):
        return str(self.log)
