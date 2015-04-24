import os
import subprocess
import tempfile

from data import Data as I
from data.decorators import data
from six.moves import shlex_quote
from tempdir import TempDir


class LaTeXError(Exception):
    """LaTeX call exception."""

    #: Contents of the log-file that was generated (if any).
    log = None

    #: The :class:`subprocess.CalledProcessError` that was thrown originally.
    call_exc = None

    def __str__(self):
        return str(self.log)

    @classmethod
    def from_proc_error(cls, e, logfn=None):
        err = cls()
        err.log = None
        err.call_exc = e

        if os.path.exists(logfn):
            err.log = open(logfn).read()

        return err


def build_pdf_old(source, latex_cmd='pdflatex', texinputs=[''], max_runs=15):
    """Generates a PDF from LaTeX a source, using pdflatex and a temporary
    directory, to avoid leaving behind temporary files.

    pdflatex will be run as many times as necessary; at ``max_runs`` runs, an
    exception is raised and the generation is aborted with a
    :class:`RuntimeError`.

    If there are errors calling pdflatex, a :class:`~latex.build.LaTeXError` is
    raised.

    :param source: The LaTeX source.
    :param latex_cmd: The path for the ``pdflatex`` binary to use.
    :param texinputs: Include paths for TeX. An empty string causes the default
                      path to be added (see the tex manpage).
    :param max_runs: Maximum number of reruns.
    :returns: A binary string of the generated PDF file.
    """

    with TempDir() as tmpdir:
        input_fd, input_fn = tempfile.mkstemp(suffix='.latex', dir=tmpdir)
        input_file = os.fdopen(input_fd, 'w')

        # write the source file
        input_file.write(source)
        input_file.close()

        # calculate output filename
        base_fn = os.path.splitext(input_fn)[0]
        output_fn = base_fn + '.pdf'
        aux_fn = base_fn + '.aux'
        args = [latex_cmd,
                '-interaction=batchmode',
                '-halt-on-error',
                '-no-shell-escape',
                '-file-line-error',
                input_fn]

        # create environment
        newenv = os.environ.copy()
        newenv['TEXINPUTS'] = os.pathsep.join(texinputs) + os.pathsep

        prev_aux = None
        while True:
            try:
                subprocess.check_call(
                    args,
                    cwd=tmpdir,
                    env=newenv,
                    stdin=open(os.devnull, 'r'),
                    stdout=open(os.devnull, 'w'),
                    stderr=open(os.devnull, 'w'),
                )
            except subprocess.CalledProcessError as e:
                raise LaTeXError.from_proc_error(e, base_fn + '.log')

            # check aux-file
            aux = open(aux_fn, 'rb').read()

            if aux == prev_aux:
                break

            prev_aux = aux

            max_runs -= 1

            if max_runs == 0:
                raise RuntimeError(
                    'Maximum number of runs ({}) without a stable .aux file '
                    'reached.'.format(max_runs)
                )

        # read generated .pdf
        return open(output_fn, 'rb').read()

        # FIXME: http://vim-latex.sourceforge.net/documentation/latex-suite
        #        /compiling-multiple.html


class LatexMkBuilder(object):
    def __init__(self, latexmk='latexmk', pdflatex='pdflatex'):
        self.latexmk = latexmk
        self.pdflatex = pdflatex

    @data('source')
    def build_pdf(self, source, texinputs=[]):
        with TempDir() as tmpdir,\
                source.temp_saved(suffix='.latex', dir=tmpdir) as tmp:

            base_fn = os.path.splitext(tmp.name)[0]
            output_fn = base_fn + '.pdf'

            latex_cmd = [shlex_quote(self.pdflatex),
                         '-interaction=batchmode',
                         '-halt-on-error',
                         '-no-shell-escape',
                         '-file-line-error',
                         '%O',
                         '%S',
                         ]

            args = [self.latexmk,
                    '-pdf',
                    '-pdflatex={}'.format(' '.join(latex_cmd)),
                    tmp.name,
                    ]

            # create environment
            newenv = os.environ.copy()
            newenv['TEXINPUTS'] = os.pathsep.join(texinputs) + os.pathsep

            try:
                subprocess.check_call(
                    args,
                    cwd=tmpdir,
                    env=newenv,
                    stdin=open(os.devnull, 'r'),
                    stdout=open(os.devnull, 'w'),
                    stderr=open(os.devnull, 'w'),
                )
            except subprocess.CalledProcessError as e:
                raise LaTeXError.from_proc_error(e, base_fn + '.log')

            return I(open(output_fn, 'rb'), encoding=None)


class PdfLatexBuilder(object):
    def __init__(self, pdflatex='pdflatex', max_runs=15):
        self.pdflatex = pdflatex
        self.max_runs = 15

    @data('source')
    def build_pdf(self, source, texinputs=[]):
        with TempDir() as tmpdir,\
                source.temp_saved(suffix='.latex', dir=tmpdir) as tmp:

            # calculate output filename
            base_fn = os.path.splitext(tmp.name)[0]
            output_fn = base_fn + '.pdf'
            aux_fn = base_fn + '.aux'
            args = [self.pdflatex,
                    '-interaction=batchmode',
                    '-halt-on-error',
                    '-no-shell-escape',
                    '-file-line-error',
                    tmp.name]

            # create environment
            newenv = os.environ.copy()
            newenv['TEXINPUTS'] = os.pathsep.join(texinputs) + os.pathsep

            # run until aux file settles
            prev_aux = None
            runs_left = self.max_runs
            while runs_left:
                try:
                    subprocess.check_call(
                        args,
                        cwd=tmpdir,
                        env=newenv,
                        stdin=open(os.devnull, 'r'),
                        stdout=open(os.devnull, 'w'),
                    )
                except subprocess.CalledProcessError as e:
                    raise LaTeXError.from_proc_error(e, base_fn + '.log')

                # check aux-file
                aux = open(aux_fn, 'rb').read()

                if aux == prev_aux:
                    break

                prev_aux = aux
                runs_left -= 1
            else:
                raise RuntimeError(
                    'Maximum number of runs ({}) without a stable .aux file '
                    'reached.'.format(self.max_runs)
                )

            # by opening the file, a handle will be kept open, even though the
            # tempdir gets removed. upon garbage collection, it will disappear,
            # unless the caller used it somehow
            return I(open(output_fn, 'r'), encoding=None)


def build_pdf(source):
    builder = LatexMkBuilder()

    return builder.build_pdf(source)
