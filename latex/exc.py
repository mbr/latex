import os

from .errors import parse_log


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

    def get_errors(self, *args, **kwargs):
        """Parse the log for errors.

        Any arguments are passed on to :func:`.parse_log`.

        :return: The return of :func:`.parse_log`, applied to the log
                 associated with this build error.
        """
        return parse_log(self.log)
