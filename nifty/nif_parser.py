import sys
from pprint import pprint as pprint

import ply.lex as lex
import ply.yacc as yacc

# Get the token map from the lexer.
import nif_lexer
tokens = nif_lexer.tokens

##############################################################################
# Grammar rules.

start = 'program'

def p_program(p):
    'program : module_list'
    p[0] = p[1]

# XXX: Catch 'STOP' just in case since it isn't an illegal instruction when
#      declared in this scope.
def p_module_list(p):
    '''
        module_list : module module_list
                    | STOP
                    | empty
    '''
    if len(p) == 3:
        p[0] = [p[1]] + p[2]
    # Append 'stop' as the last instruction to be executed.
    if p[0] is None:
        p[0] = ['stop']

def p_module(p):
    'module : module_name LEFT_BRACE card_list RIGHT_BRACE'
    p[0] = make_module(p)

def p_module_name(p):
    '''
        module_name : ACER
                    | BROADR
                    | CCCCR
                    | COVR
                    | DTFR
                    | ERRORR
                    | GAMINR
                    | GASPR
                    | GROUPR
                    | HEATR
                    | LEAPR
                    | MATXSR
                    | MIXR
                    | MODER
                    | PLOTR
                    | POWR
                    | PURR
                    | RECONR
                    | RESXSR
                    | THERMR
                    | UNRESR
                    | VIEWR
                    | WIMSR
    '''
    p[0] = p[1]

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
    'card : card_name LEFT_BRACE statement_list RIGHT_BRACE'
    p[0] = make_card(p)

def p_card_name(p):
    '''
        card_name : CARD
                  | CARD_1
                  | CARD_2
                  | CARD_3
                  | CARD_4
                  | CARD_5
                  | CARD_6
                  | CARD_7
                  | CARD_8
                  | CARD_8A
                  | CARD_9
                  | CARD_10
                  | CARD_11
    '''
    p[0] = p[1]

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
    p[0] = make_statement(p[1])

def p_expression(p):
    'expression : assignment'
    p[0] = make_expression(p[1])

def p_assignment(p):
    'assignment : IDENTIFIER ASSIGNMENT factor'
    p[0] = make_assignment(p[1], p[2], p[3])

def p_factor(p):
    '''
        factor : NUMBER
               | STRING
    '''
    p[0] = p[1]

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    if p is not None:
        sys.stderr.write('--- Syntax error: unexpected token on line %d: %s\n'
            % (p.lineno, p))
    sys.exit('syntax_error')

##############################################################################
# Constructors.

def make_module(module_token):
    return make_module_node(module_token)

def make_module_node(module_token):
    node = dict()
    node['line_number'] = module_token.lineno(1)
    node['type'] = module_token[1]
    node['card_list'] = module_token[3]
    return node

def make_card(card_token):
    return make_card_node(card_token)

def make_card_node(card_token):
    node = dict()
    node['line_number'] = card_token.lineno(1)
    node['type'] = card_token[1]
    node['statement_list'] = card_token[3]
    return node

def make_statement(statement):
    return statement

def make_expression(expression):
    return expression

def make_assignment(rval, operator, lval):
    return (operator, rval, lval)

##############################################################################
# Misc.

def parse(data):
    lexer = lex.lex(module=nif_lexer)
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
