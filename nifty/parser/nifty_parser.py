import sys
from pprint import pprint

from ply import lex
from ply import yacc

from nifty.environment import ast
from nifty.environment.exceptions import syntax_error

from nifty.lexer import nifty_lexer
# Get the token map from the nifty lexer. Required by PLY Yacc.
from nifty.lexer.nifty_lexer import tokens

##############################################################################
# Grammar rules.

start = 'program'

def p_program(p):
    'program : module_list'
    p[0] = ast.make_program(p)

def p_module_list(p):
    '''
        module_list : module module_list
                    | empty
    '''
    if len(p) == 3:
        p[0] = [p[1]] + p[2]
    # Append 'stop' as the last instruction to be executed.
    if p[0] is None:
        p[0] = [ast.make_stop(p)]

def p_module(p):
    'module : MODULE LEFT_BRACE card_list RIGHT_BRACE'
    p[0] = ast.make_module(p)

def p_card_list(p):
    '''
        card_list : card card_list
                  | empty
    '''
    if len(p) == 3:
        p[0] = [p[1]] + p[2]
    if p[0] is None:
        p[0] = []

def p_card(p):
    'card : CARD LEFT_BRACE statement_list RIGHT_BRACE'
    p[0] = ast.make_card(p)

def p_statement_list(p):
    '''
        statement_list : statement statement_list
                       | empty
    '''
    if len(p) == 3:
        p[0] = [p[1]] + p[2]
    if p[0] is None:
        p[0] = []

def p_statement(p):
    'statement : expression SEMICOLON'
    p[0] = ast.make_statement(p)

def p_expression(p):
    '''
        expression : l_value ASSIGNMENT r_value
    '''
    p[0] = ast.make_assignment(p)

def p_l_value(p):
    '''
        l_value : array
                | identifier
    '''
    p[0] = ast.make_l_value(p)

def p_array(p):
    'array : IDENTIFIER LEFT_BRACKET INTEGER RIGHT_BRACKET'
    p[0] = ast.make_array(p)

def p_identifier(p):
    'identifier : IDENTIFIER'
    p[0] = ast.make_identifier(p)

def p_r_value(p):
    '''
        r_value : number
                | string
    '''
    p[0] = ast.make_r_value(p)

def p_number(p):
    '''
        number : FLOAT
               | INTEGER
    '''
    if isinstance(eval(p[1]), float):
        p[0] = ast.make_float(p)
    elif isinstance(eval(p[1]), int):
        p[0] = ast.make_integer(p)
    else:
        p_error(p)

def p_string(p):
    'string : STRING'
    p[0] = ast.make_string(p)

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    #if p is not None:
    #    print p
    #    msg = ('--- Syntax error on line %d, unexpected token: \'%s\''
    #           % (p.lineno, p.value))
    #else:
    #    msg = ('--- Syntax error, unexpected token: \'%s\'' % (p))
    #raise SyntaxError(msg)
    syntax_error(p)

##############################################################################
# Driver.

def parse(data):
    lexer = lex.lex(module=nifty_lexer)
    parser = yacc.yacc(debug=True)
    # 'tracking' requires extra processing. Turn it off if parsing is slow.
    return parser.parse(data, tracking=True)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        result = parse(open(filename).read())
    else:
        result = parse(sys.stdin.read())
    pprint(result)
