import sys

from nifty.environment.exceptions import lexical_error

##############################################################################
# Tokens.

reserved_cards = {
    'card_0' : 'CARD',
    'card_1' : 'CARD',
    'card_2' : 'CARD',
    'card_2a' : 'CARD',
    'card_2b' : 'CARD',
    'card_3' : 'CARD',
    'card_3a' : 'CARD',
    'card_3b' : 'CARD',
    'card_3c' : 'CARD',
    'card_4' : 'CARD',
    'card_5' : 'CARD',
    'card_5a' : 'CARD',
    'card_6' : 'CARD',
    'card_6a' : 'CARD',
    'card_6b' : 'CARD',
    'card_7' : 'CARD',
    'card_7a' : 'CARD',
    'card_7b' : 'CARD',
    'card_8' : 'CARD',
    'card_8a' : 'CARD',
    'card_8b' : 'CARD',
    'card_8c' : 'CARD',
    'card_8d' : 'CARD',
    'card_9' : 'CARD',
    'card_10' : 'CARD',
    'card_10a' : 'CARD',
    'card_11' : 'CARD',
    'card_12' : 'CARD',
    'card_12a' : 'CARD',
    'card_12b' : 'CARD',
    'card_13' : 'CARD',
    'card_13a' : 'CARD',
    'card_13b' : 'CARD',
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
reserved_words = {
    'NULL' : 'NULL',
}
reserved_words.update(reserved_cards)
reserved_words.update(reserved_modules)

# List of tokens.
tokens = [
    'ASSIGNMENT',
    'IDENTIFIER',
    # R-values. Numbers and strings.
    'INTEGER',
    'FLOAT',
    'STRING',
    # Delimeters: { } [ ] ; ,
    'LEFT_BRACE',
    'RIGHT_BRACE',
    'LEFT_BRACKET',
    'RIGHT_BRACKET',
    'SEMICOLON',
    'COMMA',
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

# Assignment.
t_ASSIGNMENT = r'='

# Delimeters.
t_LEFT_BRACE = r'\{'
t_RIGHT_BRACE = r'\}'
t_LEFT_BRACKET = r'\['
t_RIGHT_BRACKET = r'\]'
t_SEMICOLON = r';'
t_COMMA = r','

# Handle identifiers and reserved words.
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved_words.get(t.value,"IDENTIFIER")
    return t

# Integers. Signed or unsigned.
t_INTEGER = r'[-+]?\d+'

# C-style floats. Signed or unsigned.
#    optional_sign digits dot digits optional_(exponent optional_sign digits)
# or,
#    optional_sign digits exponent optional_sign digits
t_FLOAT = r'[-+]?((\d+)(\.\d+)([eE][-+]?(\d+))? | (\d+)[eE][-+]?(\d+))'

# Strings.
# Recognizes strings delimited by double quotes ("), e.g. "A string.".
t_STRING = r'(\"([^\\\n]|(\\.))*?\")'

# Comments.
# Recognizes multi-line comments on the form:
#   /* Multi-line comment. */
# and single line comments on the form:
#   // Single line comment.
def t_comment(t):
    r'(/\*(.|\n)*?\*/)|(//.*)'
    # Keep count on newlines. t_newline doesn't match while inside a comment.
    t.lexer.lineno += t.value.count('\n')
    # No return value. Token (comment) discarded.

# Error handling.
def t_error(t):
    lexical_error(t)
