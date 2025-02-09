import os

import pygments
from pygments import lexers
from pygments.token import _TokenType
from pygments_tsx.tsx import TypeScriptXLexer, patch_pygments

parent = os.path.dirname(__file__)
file_path = os.path.join(parent, 'Blank.tsx')


def test_lexer_on_Blank():
    tsx_lexer = TypeScriptXLexer()
    with open(file_path) as f:
        txt = f.read()
        tokens = pygments.lex(txt, lexer=tsx_lexer)
        tokens = list(tokens)
        for idx, token in enumerate(tokens):
            print(idx)
            print(token)
        assert tokens[27][1] == 'div'
        assert isinstance(tokens[27][0], _TokenType)


def test_patch_pygments():
    patch_pygments()
    lexers.get_lexer_for_filename(file_path)
    assert True


def test_pygmemts():
    assert True


def test_lexer_on_rsx():
    tsx_lexer = TypeScriptXLexer()
    rsx_path = os.path.join(parent, 'Sample.rsx')
    with open(rsx_path) as f:
        txt = f.read()
        tokens = list(pygments.lex(txt, lexer=tsx_lexer))
        # Test for some RSX-specific tokens
        container_token = next((t for t in
                               tokens if t[1] == 'Container'), None)
        assert container_token is not None
        text_token = next((t for t in tokens if t[1] == 'Text'), None)
        assert text_token is not None
