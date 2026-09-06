"""Tests for build_pdf with the new halt_on_error parameter.
"""

import pytest
from latex import LatexBuildError, build_pdf


##### default (no builder specified)


def test_default_good_true(good_minimal_latex):
    "Valid LaTeX with halt_on_error=True"
    pdf = build_pdf(good_minimal_latex, halt_on_error=True)
    assert pdf


def test_default_good_false(good_minimal_latex):
    "If halt-on-error=False, no BuildError should be thrown."
    pdf = build_pdf(good_minimal_latex, halt_on_error=False)
    assert pdf


def test_default_bad_true(bad_minimal_latex):
    "If halt-on-error=True (default), BuildError should be thrown if error arises."
    with pytest.raises(LatexBuildError):
        # builder.build_pdf(bad_latex)
        build_pdf(bad_minimal_latex)


def test_default_bad_false(bad_minimal_latex):
    "If halt-on-error=False, no BuildError should be thrown."
    pdf = build_pdf(bad_minimal_latex, halt_on_error=False)
    assert pdf


##### builder=latexmk


def test_pdflatexmk_good_true(good_minimal_latex):
    "Valid LaTeX with halt_on_error=True"
    pdf = build_pdf(good_minimal_latex, builder="latexmk", halt_on_error=True)
    assert pdf


def test_pdflatexmk_good_false(good_minimal_latex):
    "Valid LaTeX with halt_on_error=True"
    pdf = build_pdf(good_minimal_latex, builder="latexmk", halt_on_error=False)
    assert pdf


def test_pdflatmk_bad_true(bad_minimal_latex):
    "Invalid LaTeX with halt_on_error=True"
    with pytest.raises(LatexBuildError):
        build_pdf(bad_minimal_latex, builder="latexmk", halt_on_error=True)


def test_pdflatexmk_bad_false(bad_minimal_latex):
    "Invalid LaTeX with halt_on_error=True"
    pdf = build_pdf(bad_minimal_latex, builder="latexmk", halt_on_error=False)
    assert pdf


#####  builder=pdflatex


def test_pdflatex_good_true(good_minimal_latex):
    "Valid LaTeX with halt_on_error=True"
    pdf = build_pdf(good_minimal_latex, builder="pdflatex", halt_on_error=True)
    assert pdf


def test_pdflatex_good_false(good_minimal_latex):
    "Valid LaTeX with halt_on_error=True"
    pdf = build_pdf(good_minimal_latex, builder="pdflatex", halt_on_error=False)
    assert pdf


def test_pdflatex_bad_true(bad_minimal_latex):
    "Invalid LaTeX with halt_on_error=True"
    with pytest.raises(LatexBuildError):
        build_pdf(bad_minimal_latex, builder="pdflatex", halt_on_error=True)


#  this one does not work because pdflatex does ot produce any output???
def test_pdflatex_bad_false(bad_minimal_latex):
    "Invalid LaTeX with halt_on_error=True"
    pdf = build_pdf(bad_minimal_latex, builder="pdflatex", halt_on_error=False)
    assert pdf


##### builder=lualatex


def test_lualatexmk_good_true(good_extra_latex):
    "Valid LaTeX with halt_on_error=True"
    pdf = build_pdf(good_extra_latex, builder="lualatexmk", halt_on_error=True)
    assert pdf


def test_lualatexmk_good_false(good_extra_latex):
    "Valid LaTeX with halt_on_error=True"
    pdf = build_pdf(good_extra_latex, builder="lualatexmk", halt_on_error=False)
    assert pdf


def test_lualatexmk_bad_true(bad_extra_latex):
    "Invalid LaTeX with halt_on_error=True"
    with pytest.raises(LatexBuildError):
        build_pdf(bad_extra_latex, builder="lualatexmk", halt_on_error=True)


def test_lualatexmk_bad_false(bad_extra_latex):
    "Invalid LaTeX with halt_on_error=True"
    pdf = build_pdf(bad_extra_latex, builder="lualatexmk", halt_on_error=False)
    assert pdf


##### builder=xelatex


def test_xelatexmk_good_true(good_extra_latex):
    "Valid LaTeX with halt_on_error=True"
    pdf = build_pdf(good_extra_latex, builder="xelatexmk", halt_on_error=True)
    assert pdf


def test_xelatexmk_good_false(good_extra_latex):
    "Valid LaTeX with halt_on_error=True"
    pdf = build_pdf(good_extra_latex, builder="xelatexmk", halt_on_error=False)
    assert pdf


def test_xelatexmk_bad_true(bad_extra_latex):
    "Invalid LaTeX with halt_on_error=True"
    with pytest.raises(LatexBuildError):
        build_pdf(bad_extra_latex, builder="xelatexmk", halt_on_error=True)


def test_xelatexmk_bad_false(bad_extra_latex):
    "Invalid LaTeX with halt_on_error=True"
    pdf = build_pdf(bad_extra_latex, builder="lualatexmk", halt_on_error=False)
    assert pdf
