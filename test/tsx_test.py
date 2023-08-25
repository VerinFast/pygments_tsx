import pygments

from pygments_tsx.pygments_tsx import TypeScriptXLexer

def test_lexer_on_Blank():
    tsx_lexer = TypeScriptXLexer()
    with open('./Blank.tsx') as f:
        txt = f.read()
        pygments.lex(txt, lexer=tsx_lexer)
