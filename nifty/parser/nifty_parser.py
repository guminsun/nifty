import sys
from pprint import pprint

import ply.lex as lex
import ply.yacc as yacc

from nifty.lexer import nifty_lexer
# Get the token map from the nifty lexer.
from nifty.lexer.nifty_lexer import tokens

##############################################################################
# Grammar rules.

start = 'program'

def p_program(p):
    'program : module_list'
    p[0] = make_program(p)

def p_module_list(p):
    '''
        module_list : module module_list
                    | empty
    '''
    if len(p) == 3:
        p[0] = [p[1]] + p[2]
    # Append 'stop' as the last instruction to be executed.
    if p[0] is None:
        p[0] = [make_stop(p)]

def p_module(p):
    'module : MODULE LEFT_BRACE card_list RIGHT_BRACE'
    p[0] = make_module(p)

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
    p[0] = make_card(p)

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
    p[0] = make_statement(p)

def p_expression(p):
    '''
        expression : l_value ASSIGNMENT r_value
    '''
    p[0] = make_assignment(p)

def p_l_value(p):
    '''
        l_value : array
                | identifier
    '''
    p[0] = make_l_value(p)

def p_array(p):
    'array : IDENTIFIER LEFT_BRACKET INTEGER RIGHT_BRACKET'
    p[0] = make_array(p)

def p_identifier(p):
    'identifier : IDENTIFIER'
    p[0] = make_identifier(p)

def p_r_value(p):
    '''
        r_value : number
                | string
    '''
    p[0] = make_r_value(p)

def p_number(p):
    '''
        number : FLOAT
               | INTEGER
    '''
    if isinstance(eval(p[1]), float):
        p[0] = make_float(p)
    elif isinstance(eval(p[1]), int):
        p[0] = make_integer(p)
    else:
        p_error(p)

def p_string(p):
    'string : STRING'
    p[0] = make_string(p)

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    if p is not None:
        sys.stderr.write('--- Syntax error on line %d, unexpected token %s\n'
            % (p.lineno, p))
    sys.exit('syntax_error')

##############################################################################
# Constructors.

def make_program(p):
    node = dict()
    node['node_type'] = 'program'
    node['line_number'] = p.lineno(0)
    node['module_list'] = p[1]
    return node

def make_stop(p):
    node = dict()
    node['node_type'] = 'module'
    node['line_number'] = p.lineno(0)
    node['module_name'] = 'stop'
    node['card_list'] = []
    return node

def make_module(p):
    node = dict()
    node['node_type'] = 'module'
    node['line_number'] = p.lineno(0)
    node['module_name'] = p[1]
    node['card_list'] = p[3]
    return node

def make_card(p):
    node = dict()
    node['node_type'] = 'card'
    node['line_number'] = p.lineno(0)
    node['card_id'] = make_card_id(p[1])
    node['card_name'] = p[1]
    node['statement_list'] = p[3]
    return node

def make_card_id(card_name):
    id_alpha = ''
    id_digit = ''
    # XXX: Handle 'card'.
    if len(card_name) < 5:
        return None
    card_id = card_name[5:]
    for i in card_id:
        if i.isdigit():
            id_digit += i
        if i.isalpha():
            id_alpha += i
    return int(id_digit), id_alpha

def make_statement(p):
    return p[1]

def make_assignment(p):
    node = dict()
    node['line_number'] = p.lineno(2)
    node['node_type'] = p[2]
    node['l_value'] = p[1]
    node['r_value'] = p[3]
    return node

def make_l_value(p):
    return p[1]

def make_r_value(p):
    return p[1]

def make_array(p):
    node = dict()
    node['line_number'] = p.lineno(0)
    node['node_type'] = 'array'
    node['name'] = p[1]
    node['index'] = p[3]
    return node

def make_float(p):
    node = dict()
    node['line_number'] = p.lineno(0)
    node['node_type'] = 'float'
    node['value'] = p[1]
    return node

def make_identifier(p):
    node = dict()
    node['line_number'] = p.lineno(0)
    node['node_type'] = 'identifier'
    node['name'] = p[1]
    return node

def make_integer(p):
    node = dict()
    node['line_number'] = p.lineno(0)
    node['node_type'] = 'integer'
    node['value'] = eval(p[1])
    return node

def make_string(p):
    node = dict()
    node['line_number'] = p.lineno(0)
    node['node_type'] = 'string'
    node['value'] = eval(p[1])
    return node

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
    print '--- nifty parser output:'
    pprint(result)
