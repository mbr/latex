import os
import subprocess
from subprocess import CalledProcessError

from future.utils import raise_from
from data import Data as I
from data.decorators import data
from shutilwhich import which
from six.moves import shlex_quote
from tempdir import TempDir

from .exc import LatexBuildError


class LatexBuilder(object):
    """Base class for Latex builders."""

    def build_pdf(self, source, texinputs=[]):
        """Generates a PDF from LaTeX a source.

        If there are errors generating a ``LatexError`` is raised.

        :param source: The LaTeX source.
        :param texinputs: Include paths for TeX. An empty string causes the
                          default path to be added (see the tex manpage).
        :returns: A :class:`~data.Data` instance containing the generated PDF.
        """
        raise NotImplementedError

    def is_available(self):
        """Checks if builder is available.

        Builders that depend on external programs like ``latexmk`` can check
        if these are found on the path or make sure other prerequisites are
        met.

        :return: A boolean indicating availability."""
        raise NotImplementedError


class LatexMkBuilder(LatexBuilder):
    """A latexmk based builder for LaTeX files.

    Uses the `latexmk
    <http://users.phys.psu.edu/~collins/software/latexmk-jcc/>`_ script to
    build latex files, which is part of some popular LaTeX distributions like
    `texlive <https://www.tug.org/texlive/>`_.

    The build process consists of copying the source file to a temporary
    directory and running latexmk on it, which will take care of reruns.

    :param latexmk: The path to the ``latexmk`` binary (will looked up on
                    ``$PATH``).
    :param pdflatex: The path to the ``pdflatex`` binary (will looked up on
                    ``$PATH``).
    """

    def __init__(self, latexmk='latexmk', pdflatex='pdflatex'):
        self.latexmk = latexmk
        self.pdflatex = pdflatex

    @data('source')
    def build_pdf(self, source, texinputs=[]):
        with TempDir() as tmpdir,\
                source.temp_saved(suffix='.latex', dir=tmpdir) as tmp:

            # close temp file, so other processes can access it also on Windows
            tmp.close()

            base_fn = os.path.splitext(tmp.name)[0]
            output_fn = base_fn + '.pdf'

            latex_cmd = [shlex_quote(self.pdflatex),
                         '-interaction=batchmode',
                         '-halt-on-error',
                         '-no-shell-escape',
                         '-file-line-error',
                         '%O',
                         '%S', ]

            args = [self.latexmk,
                    '-pdf',
                    '-pdflatex={}'.format(' '.join(latex_cmd)),
                    tmp.name, ]

            # create environment
            newenv = os.environ.copy()
            newenv['TEXINPUTS'] = os.pathsep.join(texinputs) + os.pathsep

            try:
                subprocess.check_call(args,
                                      cwd=tmpdir,
                                      env=newenv,
                                      stdin=open(os.devnull, 'r'),
                                      stdout=open(os.devnull, 'w'),
                                      stderr=open(os.devnull, 'w'), )
            except CalledProcessError as e:
                raise_from(LatexBuildError(base_fn + '.log'), e)

            return I(open(output_fn, 'rb').read(), encoding=None)

    def is_available(self):
        return bool(which(self.pdflatex)) and bool(which(self.latexmk))


class PdfLatexBuilder(LatexBuilder):
    """A simple pdflatex based buidler for LaTeX files.

    Builds LaTeX files by copying them to a temporary directly and running
    ``pdflatex`` until the associated ``.aux`` file stops changing.

    .. note:: This may miss changes if ``biblatex`` or other additional tools
              are used. Usually, the :class:`~latex.build.LatexMkBuilder` will
              give more reliable results.

    :param pdflatex: The path to the ``pdflatex`` binary (will looked up on
                    ``$PATH``).
    :param max_runs: An integer providing an upper limit on the amount of times
                     ``pdflatex`` can be rerun before an exception is thrown.
    """

    def __init__(self, pdflatex='pdflatex', max_runs=15):
        self.pdflatex = pdflatex
        self.max_runs = 15

    @data('source')
    def build_pdf(self, source, texinputs=[]):
        with TempDir() as tmpdir,\
                source.temp_saved(suffix='.latex', dir=tmpdir) as tmp:

            # close temp file, so other processes can access it also on Windows
            tmp.close()

            # calculate output filename
            base_fn = os.path.splitext(tmp.name)[0]
            output_fn = base_fn + '.pdf'
            aux_fn = base_fn + '.aux'
            args = [self.pdflatex, '-interaction=batchmode', '-halt-on-error',
                    '-no-shell-escape', '-file-line-error', tmp.name]

            # create environment
            newenv = os.environ.copy()
            newenv['TEXINPUTS'] = os.pathsep.join(texinputs) + os.pathsep

            # run until aux file settles
            prev_aux = None
            runs_left = self.max_runs
            while runs_left:
                try:
                    subprocess.check_call(args,
                                          cwd=tmpdir,
                                          env=newenv,
                                          stdin=open(os.devnull, 'r'),
                                          stdout=open(os.devnull, 'w'), )
                except CalledProcessError as e:
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
                    'reached.'.format(self.max_runs))

            return I(open(output_fn, 'rb').read(), encoding=None)

    def is_available(self):
        return bool(which(self.pdflatex))


PREFERRED_BUILDERS = [LatexMkBuilder, PdfLatexBuilder, ]


def build_pdf(source, texinputs=[]):
    """Builds a LaTeX source to PDF.

    Will automatically instantiate an available builder (or raise a
    :class:`exceptions.RuntimeError` if none are available) and build the
    supplied source with it.

    Parameters are passed on to the builder's
    :meth:`~latex.build.LatexBuilder.build_pdf` function.
    """
    for bld_cls in PREFERRED_BUILDERS:
        builder = bld_cls()
        if not builder.is_available():
            continue
        return builder.build_pdf(source, texinputs)
    else:
        raise RuntimeError('No available builder could be instantiated. '
                           'Please make sure LaTeX is installed.')
