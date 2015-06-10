def test_run_example():
    min_latex = (r"\documentclass{article}"
                 r"\begin{document}"
                 r"Hello, world!"
                 r"\end{document}")

    from latex import build_pdf

    # this builds a pdf-file inside a temporary directory
    pdf = build_pdf(min_latex)

    # look at the first few bytes of the header
    print(bytes(pdf)[:10])
