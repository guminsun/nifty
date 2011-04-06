import sys
from pprint import pprint as pprint

import ply.lex as lex

##############################################################################
# Tokens.

reserved_cards = {
    'card' : 'CARD',
    'card_1' : 'CARD_1',
    'card_2' : 'CARD_2',
    'card_3' : 'CARD_3',
    'card_4' : 'CARD_4',
    'card_5' : 'CARD_5',
    'card_6' : 'CARD_6',
    'card_7' : 'CARD_7',
    'card_8' : 'CARD_8',
    'card_8a' : 'CARD_8A',
    'card_9' : 'CARD_9',
    'card_10' : 'CARD_10',
    'card_11' : 'CARD_11',
}

reserved_modules = {
    'acer' : 'ACER',
    'broadr' : 'BROADR',
    'ccccr' : 'CCCCR',
    'covr' : 'COVR',
    'dtfr' : 'DTFR',
    'errorr' : 'ERRORR',
    'gaminr' : 'GAMINR',
    'gaspr' : 'GASPR',
    'groupr' : 'GROUPR',
    'heatr' : 'HEATR',
    'leapr' : 'LEAPR',
    'matxsr' : 'MATXSR',
    'mixr' : 'MIXR',
    'moder' : 'MODER',
    'plotr' : 'PLOTR',
    'powr' : 'POWR',
    'purr' : 'PURR',
    'reconr' : 'RECONR',
    'resxsr' : 'RESXSR',
    'thermr' : 'THERMR',
    'unresr' : 'UNRESR',
    'viewr' : 'VIEWR',
    'wimsr' : 'WIMSR',
    # XXX: 'stop' is not a module, but it is in the same scope as the modules.
    'stop' : 'STOP',
}

# Reserved words.
reserved_words = {}
reserved_words.update(reserved_cards)
reserved_words.update(reserved_modules)

# List of tokens.
tokens = [
    # Assignment.
    'ASSIGNMENT',

    # Identifiers.
    'IDENTIFIER',

    # Numbers.
    'NUMBER',
    # Strings.
    'STRING',

    # Delimeters: { } ;
    'LEFT_BRACE',
    'RIGHT_BRACE',
    'SEMICOLON',
] + list(reserved_words.values())

##############################################################################
# Regular expression rules which recognizes tokens.

# Ignore tabs and spaces.
t_ignore = ' \t'

# Newlines.
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')
    # No return value. Token (\n) discarded.

# Identifiers and reserved words.
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value in reserved_words:
        t.type = reserved_words[t.value]
    return t

# Assignment.
t_ASSIGNMENT = r'='

# Delimeters.
t_LEFT_BRACE = r'\{'
t_RIGHT_BRACE = r'\}'
t_SEMICOLON = r';'

# Numbers.
# Description of the regular definition:
#   number -> optional_sign digits optional_fraction optional_exponent
t_NUMBER = r'(-|\+)?(\d+)(\.\d*)?(((e|E)(-|\+)?\d+))?'

# Strings.
# Recognizes strings delimited by single quotes ("'"), e.g. "'A string.'".
t_STRING = r'(\'([^\\\n]|(\\.))*?\')'

# Comments.
# Recognizes multi-line comments on the form '/* Multi-line comment. */', and
# single line comments on the form '// Single line comment.'.
def t_comment(t):
    r'(/\*(.|\n)*?\*/)|(//.*)'
    # Keep count on newlines. t_newline doesn't match while inside a comment.
    t.lexer.lineno += t.value.count('\n')
    # No return value. Token (comment) discarded.

# Error handling.
def t_error(t):
    sys.stderr.write('--- Lexical error: illegal character on line %d: %s\n'
        % (t.lineno, t.value[0]))
    sys.exit('lexical_error')

##############################################################################
# Misc.

def stdin2tokens(lexer):
    lexer.input(sys.stdin.read())
    token_list = []
    while True:
        t = lex.token()
        if not t: break
        token_list.append(t)
    return token_list

def file2tokens(filename, lexer):
    lexer.input(open(filename).read())
    token_list = []
    while True:
        t = lex.token()
        if not t: break
        token_list.append(t)
    return token_list

if __name__ == '__main__':
    lexer = lex.lex()
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        result = file2tokens(filename, lexer)
    else:
        result = stdin2tokens(lexer)
    pprint(result)
