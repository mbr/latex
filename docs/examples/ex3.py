import os

from latex import build_pdf

# we need to supply absolute paths
current_dir = os.path.abspath(os.path.dirname(__file__))

# we are adding an empty string to include the default locations (this is
# described on the tex manpage)
pdf = build_pdf(open('ex3.latex'), texinputs=[current_dir, ''])

pdf.save_to('ex3.pdf')
