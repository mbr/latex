import os
import subprocess

from future.utils import raise_from
from data import Data as I
from data.decorators import data
from shutilwhich import which
from six.moves import shlex_quote
from tempdir import TempDir

from .exc import LatexBuildError


class LatexBuilder(object):
    """Generates a PDF from LaTeX a source.

    If there are errors generating a :class:`~latex.build.LaTeXError` is
    raised.

    :param source: The LaTeX source.
    :param texinputs: Include paths for TeX. An empty string causes the default
                      path to be added (see the tex manpage).
    :returns: A :class:`~data.Data` instance containing the generated PDF.
    """
    def build_pdf(self, source, texinputs=[]):
        raise NotImplementedError


class LatexMkBuilder(LatexBuilder):
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
                raise_from(LatexBuildError(base_fn + '.log'), e)

            return I(open(output_fn, 'rb'), encoding=None)

    def is_available(self):
        return bool(which(self.pdflatex)) and bool(which(self.latexmk))


class PdfLatexBuilder(LatexBuilder):
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
                    raise_from(LatexBuildError(base_fn + '.log'), e)

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

    def is_available(self):
        return bool(which(self.pdflatex))


def build_pdf(source, texinputs=[]):
    builder = LatexMkBuilder()

    return builder.build_pdf(source, texinputs)
