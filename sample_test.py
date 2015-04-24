from latex.build import build_pdf

r = build_pdf(open('sample.latex'))
r.save_to('sample.pdf')
