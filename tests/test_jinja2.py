from latex.jinja2 import make_env
from jinja2.loaders import DictLoader


def test_jinja2_var():
    in_template = r'Hello \VAR{name}!'
    out = r'Hello Eric!'

    env = make_env(loader=DictLoader({"template.tex": in_template}))
    template = env.get_template("template.tex")
    assert out == template.render(name="Eric")


def test_jinja2_escape():
    in_template = r'Hello \VAR{name | e}!'
    out = r'Hello Jo\%h\%n\textasciitilde{} \textbackslash{}emph\{Cle\%ese\}\$!'
    env = make_env(loader=DictLoader({'template.tex': in_template}))
    template = env.get_template('template.tex')
    assert out == template.render(name=r'Jo%h%n~ \emph{Cle%ese}$')


def test_jinja2_newline_escape():
    in_template = r'Hello \VAR{name | e}!'
    out = r'Hello Michael \\Palin!'
    env = make_env(loader=DictLoader({'template.tex': in_template}))
    template = env.get_template('template.tex')
    assert out == template.render(name='Michael \n\n\nPalin')


def test_jinja2_newline_escape_no_folding():
    in_template = r'Hello \VAR{name | e(fold_newlines=false)}!'
    out = r'Hello Michael \\[3\baselineskip]Palin!'
    env = make_env(loader=DictLoader({'template.tex': in_template}))
    template = env.get_template('template.tex')
    assert out == template.render(name='Michael \n\n\nPalin')
