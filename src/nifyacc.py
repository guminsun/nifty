import sys
from pprint import pprint as pprint

import ply.lex as lex
import ply.yacc as yacc

# Get the token map from the lexer.
import niflex
tokens = niflex.tokens

##############################################################################

start = 'program'

def p_program(p):
    'program : module_list'
    p[0] = p[1]

def p_module_list(p):
    '''module_list : module module_list
                   | empty'''
    if p[0] == None:
        p[0] = ['stop']
    if len(p) == 3:
        p[0] = [p[1]] + p[2]

def p_module(p):
    'module : ACER LEFT_BRACE RIGHT_BRACE'
    p[0] = p[1]

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    if p != None:
        sys.stderr.write('--- Syntax error: unexpected token on line %d: %s\n'
            % (p.lineno, p))
    sys.exit('syntax_error')

##############################################################################

def parse(data):
    lexer = lex.lex(module=niflex)
    parser = yacc.yacc(debug=True)
    # 'tracking' requires extra processing. Turn it off if parsing is slow.
    return parser.parse(data, tracking=True)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    # XXX: Ugly.
    else:
        filename = '/home/hessman/src/nifty/slask.nif'
    result = parse(open(filename).read())
    pprint(result)
