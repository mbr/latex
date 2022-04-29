"""Tests for build_pdf with the new halt_on_error parameter.
"""
import pytest
from latex.build import LatexMkBuilder
from latex import LatexBuildError


##### builder is not specified


def test_default_good_true(good_minimal_latex):
    "Valid LaTeX with halt_on_error=True"
    builder = LatexMkBuilder()
    pdf = builder.build_pdf(good_minimal_latex, halt_on_error=True)
    assert pdf


def test_default_good_false(good_minimal_latex):
    "Valid LaTeX with halt_on_error=True"
    builder = LatexMkBuilder()
    pdf = builder.build_pdf(good_minimal_latex, halt_on_error=False)
    assert pdf


def test_default_bad_true(bad_minimal_latex):
    "Invalid LaTeX with halt_on_error=True"
    builder = LatexMkBuilder()
    with pytest.raises(LatexBuildError):
        builder.build_pdf(bad_minimal_latex, halt_on_error=True)


def test_default_bad_false(bad_minimal_latex):
    "Invalid LaTeX with halt_on_error=True"
    builder = LatexMkBuilder()
    pdf = builder.build_pdf(bad_minimal_latex, halt_on_error=False)
    assert pdf


##### builder=latexmk

# this is missleading: if user specified pdflatex, latexmk ist used


##### builder=pdflatex


def test_pdflatex_good_true(good_minimal_latex):
    "Valid LaTeX with halt_on_error=True"
    builder = LatexMkBuilder(variant="pdflatex")
    pdf = builder.build_pdf(good_minimal_latex, halt_on_error=True)
    assert pdf


def test_pdflatex_good_false(good_minimal_latex):
    "Valid LaTeX with halt_on_error=True"
    builder = LatexMkBuilder(variant="pdflatex")
    pdf = builder.build_pdf(good_minimal_latex, halt_on_error=False)
    assert pdf


def test_pdflatex_bad_true(bad_minimal_latex):
    "Invalid LaTeX with halt_on_error=True"
    builder = LatexMkBuilder(variant="pdflatex")
    with pytest.raises(LatexBuildError):
        builder.build_pdf(bad_minimal_latex, halt_on_error=True)


def test_pdflatex_bad_false(bad_minimal_latex):
    "Invalid LaTeX with halt_on_error=True"
    builder = LatexMkBuilder(variant="pdflatex")
    pdf = builder.build_pdf(bad_minimal_latex, halt_on_error=False)
    assert pdf


##### builder=lualatex


def test_lualatex_good_true(good_extra_latex):
    "Valid LaTeX with halt_on_error=True"
    builder = LatexMkBuilder(variant="lualatex")
    pdf = builder.build_pdf(good_extra_latex, halt_on_error=True)
    assert pdf


def test_lualatex_good_false(good_extra_latex):
    "Valid LaTeX with halt_on_error=True"
    builder = LatexMkBuilder(variant="lualatex")
    pdf = builder.build_pdf(good_extra_latex, halt_on_error=False)
    assert pdf


def test_lualatex_bad_true(bad_extra_latex):
    "Invalid LaTeX with halt_on_error=True"
    builder = LatexMkBuilder(variant="lualatex")
    with pytest.raises(LatexBuildError):
        builder.build_pdf(bad_extra_latex, halt_on_error=True)


def test_lualatex_bad_false(bad_extra_latex):
    "Invalid LaTeX with halt_on_error=True"
    builder = LatexMkBuilder(variant="lualatex")
    pdf = builder.build_pdf(bad_extra_latex, halt_on_error=False)
    assert pdf


###### builder=xelatex


def test_xelatex_good_true(good_extra_latex):
    "Valid LaTeX with halt_on_error=True"
    builder = LatexMkBuilder(variant="xelatex")
    pdf = builder.build_pdf(good_extra_latex, halt_on_error=True)
    assert pdf


def test_xelatex_good_false(good_extra_latex):
    "Valid LaTeX with halt_on_error=True"
    builder = LatexMkBuilder(variant="xelatex")
    pdf = builder.build_pdf(good_extra_latex, halt_on_error=False)
    assert pdf


def test_xelatex_bad_true(bad_extra_latex):
    "Invalid LaTeX with halt_on_error=True"
    builder = LatexMkBuilder(variant="xelatex")
    with pytest.raises(LatexBuildError):
        builder.build_pdf(bad_extra_latex, halt_on_error=True)


def test_xelatex_bad_false(bad_extra_latex):
    "Invalid LaTeX with halt_on_error=True"
    builder = LatexMkBuilder(variant="xelatex")
    pdf = builder.build_pdf(bad_extra_latex, halt_on_error=False)
    assert pdf
