import sys

##############################################################################
# Tokens.

reserved_cards = {
    'card' : 'CARD',
    'card_1' : 'CARD',
    'card_2' : 'CARD',
    'card_2a' : 'CARD',
    'card_3' : 'CARD',
    'card_3a' : 'CARD',
    'card_4' : 'CARD',
    'card_5' : 'CARD',
    'card_6' : 'CARD',
    'card_7' : 'CARD',
    'card_8' : 'CARD',
    'card_8a' : 'CARD',
    'card_9' : 'CARD',
    'card_10' : 'CARD',
    'card_11' : 'CARD',
    'card_12a' : 'CARD',
    'card_12b' : 'CARD',
}

reserved_identifiers = {
    ##########################################################################
    # acer
    # Reserved identifiers for acer card 1.
    'nendf' : 'IDENTIFIER',
    'npend' : 'IDENTIFIER',
    'ngend' : 'IDENTIFIER',
    'nace' : 'IDENTIFIER',
    'ndir' : 'IDENTIFIER',
    # Reserved identifiers for acer card 2.
    'iopt' : 'IDENTIFIER',
    'iprint' : 'IDENTIFIER',
    'ntype' : 'IDENTIFIER',
    'suff' : 'IDENTIFIER',
    'nxtra' : 'IDENTIFIER',
    # Reserved identifiers for acer card 3.
    'hk' : 'IDENTIFIER',
    # Reserved identifiers for acer card 4.
    'iz' : 'IDENTIFIER',
    'aw' : 'IDENTIFIER',
    # Reserved identifiers for acer card 5.
    'matd' : 'IDENTIFIER',
    'tempd' : 'IDENTIFIER',
    # Reserved identifiers for acer card 6.
    'err' : 'IDENTIFIER',
    'iopp' : 'IDENTIFIER',
    # Reserved identifiers for acer card 7.
    'thin_1' : 'IDENTIFIER',
    'thin_2' : 'IDENTIFIER',
    'thin_3' : 'IDENTIFIER',
    # Reserved identifiers for acer card 8.
    'matd' : 'IDENTIFIER',
    'tempd' : 'IDENTIFIER',
    'tname' : 'IDENTIFIER',
    # Reserved identifiers for acer card 8a.
    'iza01' : 'IDENTIFIER',
    'iza02' : 'IDENTIFIER',
    'iza03' : 'IDENTIFIER',
    # Reserved identifiers for acer card 9.
    'mti' : 'IDENTIFIER',
    'nbint' : 'IDENTIFIER',
    'mte' : 'IDENTIFIER',
    'ielas' : 'IDENTIFIER',
    'nmix' : 'IDENTIFIER',
    'emax' : 'IDENTIFIER',
    'iwt' : 'IDENTIFIER',
    # Reserved identifiers for acer card 10.
    'matd' : 'IDENTIFIER',
    'tempd' : 'IDENTIFIER',
    # Reserved identifiers for acer card 11.
    'matd' : 'IDENTIFIER',
    ##########################################################################
    # reconr
    # Reserved identifiers for reconr card 1.
    'nendf' : 'IDENTIFIER',
    'npend' : 'IDENTIFIER',
    # Reserved identifiers for reconr card 2.
    'tlabel' : 'IDENTIFIER',
    # Reserved identifiers for reconr card 3.
    'mat' : 'IDENTIFIER',
    'ncards' : 'IDENTIFIER',
    'ngrid' : 'IDENTIFIER',
    # Reserved identifiers for reconr card 4.
    'err' : 'IDENTIFIER',
    'tempr' : 'IDENTIFIER',
    'errmax' : 'IDENTIFIER',
    'errint' : 'IDENTIFIER',
    # Reserved identifiers for reconr card 5.
    'cards' : 'IDENTIFIER',
    # Reserved identifiers for reconr card 6.
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
    'INTEGER',
    'FLOAT',
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
    # XXX Check if identifier is a reserved word, otherwise raise an error?
    t.type = reserved_words.get(t.value,"IDENTIFIER")
    return t

# Assignment.
t_ASSIGNMENT = r'='

# Delimeters.
t_LEFT_BRACE = r'\{'
t_RIGHT_BRACE = r'\}'
t_SEMICOLON = r';'

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
    sys.stderr.write('--- Lexical error on line %d, illegal character %s\n'
        % (t.lineno, t.value[0]))
    sys.exit('lexical_error')
