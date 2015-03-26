import os
import subprocess
import tempfile

from tempdir import TempDir


def build_pdf(source,
              latex_cmd='pdflatex',
              texinputs=[''],
              max_runs=15):
    # for documentation, see README.rst

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
                input_fn]

        # create environment
        newenv = os.environ.copy()
        newenv['TEXINPUTS'] = os.pathsep.join(texinputs) + os.pathsep

        prev_aux = None
        while True:
            subprocess.check_call(
                args,
                cwd=tmpdir,
                env=newenv,
                stdin=open(os.devnull, 'r'),
                stdout=open(os.devnull, 'w'),
            )

            # check aux-file
            aux = file(aux_fn, 'rb').read()

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
