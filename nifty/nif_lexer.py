import sys
from pprint import pprint as pprint

import ply.lex as lex

# Reserved words.
reserved = {
    # Modules.
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
    # Cards.
    'card' : 'CARD',
    # Stop.
    'stop' : 'STOP',
}

# List of tokens and reserved words.
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
] + list(set(reserved.values()))

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
    if t.value in reserved:
        t.type = reserved[t.value]
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
# Recognizes strings delimited by '"'.
t_STRING = r'(\"([^\\\n]|(\\.))*?\")'

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

# Run.
if __name__ == '__main__':
    lexer = lex.lex()
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        result = file2tokens(filename, lexer)
    else:
        result = stdin2tokens(lexer)
    pprint(result)
