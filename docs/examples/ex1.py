from latex import build_pdf

# build_pdf's source parameter can be a file-like object or a string
pdf = build_pdf(open('ex1.latex'))

# pdf is an instance of a data object (see http://pythonhosted.org/data/)
# most often, we will want to save it to a file, as with this example
pdf.save_to('ex1.pdf')
