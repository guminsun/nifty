import sys
from pprint import pprint as pprint

import ply.lex as lex

##############################################################################
# Tokens.

reserved_cards = {
    'card' : 'CARD',
    'card_1' : 'CARD',
    'card_2' : 'CARD',
    'card_3' : 'CARD',
    'card_4' : 'CARD',
    'card_5' : 'CARD',
    'card_6' : 'CARD',
    'card_7' : 'CARD',
    'card_8' : 'CARD',
    'card_8a' : 'CARD',
    'card_9' : 'CARD',
    'card_10' : 'CARD',
    'card_11' : 'CARD',
}

reserved_identifiers = {
    # Reserved identifiers for card 1.
    'nendf' : 'IDENTIFIER',
    'npend' : 'IDENTIFIER',
    # Reserved identifiers for card 2.
    'tlabel' : 'IDENTIFIER',
    # Reserved identifiers for card 3.
    'mat' : 'IDENTIFIER',
    'ncards' : 'IDENTIFIER',
    'ngrid' : 'IDENTIFIER',
    # Reserved identifiers for card 4.
    'err' : 'IDENTIFIER',
    'tempr' : 'IDENTIFIER',
    'errmax' : 'IDENTIFIER',
    'errint' : 'IDENTIFIER',
    # Reserved identifiers for card 5.
    'cards' : 'IDENTIFIER',
    # Reserved identifiers for card 6.
    'enode' : 'IDENTIFIER',
}

reserved_modules = {
    'acer' : 'MODULE',
    'broadr' : 'MODULE',
    'ccccr' : 'MODULE',
    'covr' : 'MODULE',
    'dtfr' : 'MODULE',
    'errorr' : 'MODULE',
    'gaminr' : 'MODULE',
    'gaspr' : 'MODULE',
    'groupr' : 'MODULE',
    'heatr' : 'MODULE',
    'leapr' : 'MODULE',
    'matxsr' : 'MODULE',
    'mixr' : 'MODULE',
    'moder' : 'MODULE',
    'plotr' : 'MODULE',
    'powr' : 'MODULE',
    'purr' : 'MODULE',
    'reconr' : 'MODULE',
    'resxsr' : 'MODULE',
    'thermr' : 'MODULE',
    'unresr' : 'MODULE',
    'viewr' : 'MODULE',
    'wimsr' : 'MODULE',
    # XXX: 'stop' is not a module, but handled in the same scope.
    'stop' : 'MODULE',
}

# Reserved words.
reserved_words = {}
reserved_words.update(reserved_cards)
reserved_words.update(reserved_identifiers)
reserved_words.update(reserved_modules)

# List of tokens.
tokens = [
    # Assignment.
    'ASSIGNMENT',

    # R-values. Numbers and strings.
    'NUMBER',
    'STRING',

    # Delimeters: { } ;
    'LEFT_BRACE',
    'RIGHT_BRACE',
    'SEMICOLON',
] + list(set(reserved_words.values()))

##############################################################################
# Regular expression rules which recognizes tokens.

# Ignore whitespace; tabs and spaces.
t_ignore = ' \t'

# Count newlines for line numbers.
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')
    # No return value. Token (\n) discarded.

# Handle identifiers and reserved words.
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved_words.get(t.value,"IDENTIFIER")
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
