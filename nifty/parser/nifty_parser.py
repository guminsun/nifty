import sys
from pprint import pprint

from ply import lex
from ply import yacc

from nifty.environment import syntax_tree

from nifty.environment.exceptions import SyntaxError
from nifty.environment.exceptions import syntax_error

from nifty.lexer import nifty_lexer
# Get the token map from the nifty lexer. Required by PLY Yacc.
from nifty.lexer.nifty_lexer import tokens

##############################################################################
# Grammar rules.

start = 'program'

def p_program(p):
    'program : module_list'
    p[0] = syntax_tree.make_program(p.lineno(0), p[1])

def p_module_list(p):
    '''
        module_list : module module_list
                    | empty
    '''
    if len(p) == 3:
        p[0] = [p[1]] + p[2]
    # Append 'stop' as the last instruction to be executed.
    if p[0] is None:
        p[0] = [syntax_tree.make_stop(p.lineno(0))]

def p_module(p):
    'module : MODULE LEFT_BRACE card_list RIGHT_BRACE'
    p[0] = syntax_tree.make_module(p.lineno(0), p[1], p[3])

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
    p[0] = syntax_tree.make_card(p.lineno(0), p[1], p[3])

def p_statement_list(p):
    '''
        statement_list : statement statement_list
                       | empty
    '''
    if len(p) == 3:
        if isinstance(p[1], list):
            # Unpack the list produced by p_assignment.
            p[0] = p[1] + p[2]
        else:
            p[0] = [p[1]] + p[2]
    if p[0] is None:
        p[0] = []

def p_statement(p):
    'statement : expression SEMICOLON'
    p[0] = syntax_tree.make_statement(p[1])

def p_expression(p):
    '''
        expression : assignment
    '''
    p[0] = syntax_tree.make_expression(p[1])

def p_assignment(p):
    '''
        assignment : l_value_list ASSIGNMENT r_value_list
    '''
    if len(p[1]) == len(p[3]):
        p[0] = []
        for i in range(len(p[1])):
            p[0].append(syntax_tree.make_assignment(p.lineno(2), p[2], p[1][i], p[3][i]))
    else:
        msg = ('number of elements in the left hand side differs from the ' +
               'right hand side')
        msg = ('--- Syntax error on line %d, %s.'
               % (p.lineno(2), msg))
        raise SyntaxError(msg)

def p_l_value_list(p):
    '''
        l_value_list : l_value
                     | l_value COMMA l_value_list
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_l_value(p):
    '''
        l_value : array
                | identifier
    '''
    p[0] = syntax_tree.make_l_value(p[1])

def p_array(p):
    'array : IDENTIFIER LEFT_BRACKET INTEGER RIGHT_BRACKET'
    p[0] = syntax_tree.make_array(p.lineno(0), p[1], eval(p[3]))

def p_identifier(p):
    'identifier : IDENTIFIER'
    p[0] = syntax_tree.make_identifier(p.lineno(0), p[1])

def p_r_value_list(p):
    '''
        r_value_list : r_value
                     | r_value COMMA r_value_list
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_r_value(p):
    '''
        r_value : null
                | number
                | string
    '''
    p[0] = syntax_tree.make_r_value(p[1])

def p_null(p):
    '''
        null : NULL
    '''
    p[0] = syntax_tree.make_null(p.lineno(0), p[1])

def p_number(p):
    '''
        number : FLOAT
               | INTEGER
    '''
    if isinstance(eval(p[1]), float):
        # Floats are encapsulated as strings to preserve the float in its
        # original form. For example, Python would evaluate '3e2' to '300.0'.
        p[0] = syntax_tree.make_float(p.lineno(0), p[1])
    elif isinstance(eval(p[1]), int):
        p[0] = syntax_tree.make_integer(p.lineno(0), eval(p[1]))
    else:
        p_error(p)

def p_string(p):
    'string : STRING'
    p[0] = syntax_tree.make_string(p.lineno(0), eval(p[1]))

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    if p is None:
        syntax_error(None, p)
    else:
        syntax_error(p.lineno, p.value)

##############################################################################
# Driver.

def parse(data):
    lexer = lex.lex(module=nifty_lexer, optimize=1)
    parser = yacc.yacc(debug=True)
    # tracking is required for line numbers. Although, tracking requires extra
    # processing. Turn it off if parsing is slow.
    return parser.parse(data, tracking=True)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        result = parse(open(filename).read())
    else:
        result = parse(sys.stdin.read())
    pprint(result)
