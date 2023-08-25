from jsx import JsxLexer
from jsx.lexer import TOKENS
from pygments.lexers.javascript import TypeScriptLexer
from pygments.lexers._mapping import LEXERS
from pygments.lexers import _lexer_cache


class TypeScriptXLexer(TypeScriptLexer):
    name = 'TypeScriptX'
    aliases = ['tsx', 'typescriptx']
    filenames = ['*.tsx']
    tokens = TOKENS + super.tokens

def patch_pygments():
    # Hack to register an internal lexer.
    _lexer_cache['TypeScriptXLexer'] = TypeScriptXLexer
    _lexer_cache['JsxLexer'] = JsxLexer

    LEXERS['TypeScriptXLexer'] = (
        '',
        'TypeScriptXLexer',
        ('typescriptx', 'tsx'),
        ('*.tsx',),
        ('application/x-typescript', 'text/x-typescript')
    )

    LEXERS['JsxLexers'] = (
        '',
        'JsxLexer',
        ('react', 'jsx'),
        ('*.jsx', '*.react'),
        ('text/jsx')
    )
