#
# Tokenizer draft for the NJOY Input Format (nif).
#

import sys
import ply.lex as lex

# List of token names.
tokens = (
    # Modules and cards.
    'MODULE',
    'CARD',

    # Assignment.
    'EQUALS',

    # Numbers.
    'NUMBER',

    # XXX: Operators.
    'PLUS',
    'MINUS',

    # Delimeters: { } , . ;
    'LBRACE',
    'RBRACE',
    'COMMA',
    'PERIOD',
    'SEMI',
)

# Ignore tabs and spaces.
t_ignore = ' \t'

# Newlines.
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    # No return value. Token (\n) discarded.

# XXX: Use reserved words instead for modules?
t_MODULE = r'acer'

# XXX: What about reserved words for cards?
t_CARD = r'card\d+'

# Integers.
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Assignment.
t_EQUALS = r'='

# XXX: Operators. Not binary ones though.
t_PLUS = r'\+'
t_MINUS = r'-'

# Delimeters.
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMMA = r','
t_PERIOD = r'\.'
t_SEMI = r';'

# Comments.
def t_comment(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')
    # No return value. Token (comment) discarded.

# Error handling.
def t_error(t):
    # Print offending character and skip it.
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)

##############################################################################

def stdin2tokens(lexer):
  lexer.input(sys.stdin.read())
  token_list = []
  while True:
      t = lex.token()
      if not t: break
      token_list.append(t)
  return token_list

# Run.
if __name__=='__main__':
    lexer = lex.lex()
    for token in stdin2tokens(lexer):
        print 'Type:', token.type, '\t', 'Value:', token.value, '\t', \
        'Line:', token.lineno, '\t', 'Pos:', token.lexpos
