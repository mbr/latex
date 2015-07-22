from latex.errors import parse_log


sample_error = r"""
"This is pdfTeX, Version 3.14159265-2.6-1.40.15 (TeX Live 2015/dev/Debian) (preloaded format=pdflatex 2015.7.13)  22 JUL 2015 13:01\nentering extended mode\n file:line:error style messages enabled.\n %&-line parsing enabled.\n**/tmp/tmpy8VAYd/tmpBfplPL.latex\n(/tmp/tmpy8VAYd/tmpBfplPL.latex\nLaTeX2e <2014/05/01>\nBabel <3.9l> and hyphenation patterns for 79 languages loaded.\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2014/09/29 v1.4h Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size10.clo\nFile: size10.clo 2014/09/29 v1.4h Standard LaTeX file (size option)\n)\n\\c@part=\\count79\n\\c@section=\\count80\n\\c@subsection=\\count81\n\\c@subsubsection=\\count82\n\\c@paragraph=\\count83\n\\c@subparagraph=\\count84\n\\c@figure=\\count85\n\\c@table=\\count86\n\\abovecaptionskip=\\skip41\n\\belowcaptionskip=\\skip42\n\\bibindent=\\dimen102\n) (./tmpBfplPL.aux)\n\\openout1 = `tmpBfplPL.aux'.\n\nLaTeX Font Info:    Checking defaults for OML/cmm/m/it on input line 3.\nLaTeX Font Info:    ... okay on input line 3.\nLaTeX Font Info:    Checking defaults for T1/cmr/m/n on input line 3.\nLaTeX Font Info:    ... okay on input line 3.\nLaTeX Font Info:    Checking defaults for OT1/cmr/m/n on input line 3.\nLaTeX Font Info:    ... okay on input line 3.\nLaTeX Font Info:    Checking defaults for OMS/cmsy/m/n on input line 3.\nLaTeX Font Info:    ... okay on input line 3.\nLaTeX Font Info:    Checking defaults for OMX/cmex/m/n on input line 3.\nLaTeX Font Info:    ... okay on input line 3.\nLaTeX Font Info:    Checking defaults for U/cmr/m/n on input line 3.\nLaTeX Font Info:    ... okay on input line 3.\n/tmp/tmpy8VAYd/tmpBfplPL.latex:5: Undefined control sequence.\nl.5 \\undefinedcontrolsequencehere\n                                  \nHere is how much of TeX's memory you used:\n 199 strings out of 493105\n 2182 string characters out of 6137072\n 52476 words of memory out of 5000000\n 3752 multiletter control sequences out of 15000+600000\n 3640 words of font info for 14 fonts, out of 8000000 for 9000\n 1141 hyphenation exceptions out of 8191\n 23i,0n,17p,150b,36s stack positions out of 5000i,500n,10000p,200000b,80000s\n\n/tmp/tmpy8VAYd/tmpBfplPL.latex:5:  ==> Fatal error occurred, no output PDF file\n produced!\n"
(Pdb) print e.log
This is pdfTeX, Version 3.14159265-2.6-1.40.15 (TeX Live 2015/dev/Debian) (preloaded format=pdflatex 2015.7.13)  22 JUL 2015 13:01
entering extended mode
 file:line:error style messages enabled.
 %&-line parsing enabled.
**/tmp/tmpy8VAYd/tmpBfplPL.latex
(/tmp/tmpy8VAYd/tmpBfplPL.latex
LaTeX2e <2014/05/01>
Babel <3.9l> and hyphenation patterns for 79 languages loaded.
(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls
Document Class: article 2014/09/29 v1.4h Standard LaTeX document class
(/usr/share/texlive/texmf-dist/tex/latex/base/size10.clo
File: size10.clo 2014/09/29 v1.4h Standard LaTeX file (size option)
)
\c@part=\count79
\c@section=\count80
\c@subsection=\count81
\c@subsubsection=\count82
\c@paragraph=\count83
\c@subparagraph=\count84
\c@figure=\count85
\c@table=\count86
\abovecaptionskip=\skip41
\belowcaptionskip=\skip42
\bibindent=\dimen102
) (./tmpBfplPL.aux)
\openout1 = `tmpBfplPL.aux'.

LaTeX Font Info:    Checking defaults for OML/cmm/m/it on input line 3.
LaTeX Font Info:    ... okay on input line 3.
LaTeX Font Info:    Checking defaults for T1/cmr/m/n on input line 3.
LaTeX Font Info:    ... okay on input line 3.
LaTeX Font Info:    Checking defaults for OT1/cmr/m/n on input line 3.
LaTeX Font Info:    ... okay on input line 3.
LaTeX Font Info:    Checking defaults for OMS/cmsy/m/n on input line 3.
LaTeX Font Info:    ... okay on input line 3.
LaTeX Font Info:    Checking defaults for OMX/cmex/m/n on input line 3.
LaTeX Font Info:    ... okay on input line 3.
LaTeX Font Info:    Checking defaults for U/cmr/m/n on input line 3.
LaTeX Font Info:    ... okay on input line 3.
/tmp/tmpy8VAYd/tmpBfplPL.latex:5: Undefined control sequence.
l.5 \undefinedcontrolsequencehere

Here is how much of TeX's memory you used:
 199 strings out of 493105
 2182 string characters out of 6137072
 52476 words of memory out of 5000000
 3752 multiletter control sequences out of 15000+600000
 3640 words of font info for 14 fonts, out of 8000000 for 9000
 1141 hyphenation exceptions out of 8191
 23i,0n,17p,150b,36s stack positions out of 5000i,500n,10000p,200000b,80000s

/tmp/tmpy8VAYd/tmpBfplPL.latex:5:  ==> Fatal error occurred, no output PDF file
 produced!

"""


def test_sample_error():
    errs = parse_log(sample_error)
    assert len(errs) == 2
    err = errs[0]

    assert err['error'] == 'Undefined control sequence.'
    assert err['line'] == 5
    assert err['filename'] == '/tmp/tmpy8VAYd/tmpBfplPL.latex'
