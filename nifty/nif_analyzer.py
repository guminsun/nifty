import sys
from pprint import pprint as pprint

import nif_parser

##############################################################################
# Analyzer.

def analyze(ast):
    analyze_program(ast)
    return ast

def analyze_program(program):
    modules = program['module_list']
    analyze_module_list(modules)
    # XXX
    return None

def analyze_module_list(module_list):
    for module in module_list:
        analyze_module(module)
    # XXX
    return None

def analyze_module(module):
    # XXX: Fix big ugly switch.
    if module['module_name'] == 'stop':
        return None
    elif module['module_name'] == 'reconr':
        analyze_reconr(module)
    else:
        print '--- analyzer: XXX not implemented yet:', module['module_name']
        return None
    # XXX
    return None

def analyze_reconr(module):
    card_list = module['card_list']
    analyze_reconr_card_list(card_list)
    # XXX
    return None

def analyze_reconr_card_list(card_list):
    card = get_card('card_1', card_list)
    analyze_reconr_card_1(card)
    # XXX
    return None

def analyze_reconr_card_1(card_1):
    statement_list = card_1['statement_list']
    
    # XXX: Neat to construct a list of identifiers which must be defined and
    #      check whether they are defined or not?

    nendf = get_identifier('nendf', statement_list)
    # nendf must be defined. Translator cannot guess unit numbers.
    if not_defined(nendf):
        semantic_error('identifier "nendf" not defined.', nendf)
    
    nendf_value = get_value(get_r_value(nendf))
    # The nendf unit number must be an integer.
    if not isinstance(nendf_value, int):
        error_msg = 'illegal nendf unit number (' + str(nendf_value) + ').'
        semantic_error(error_msg, nendf)

    # The nendf unit number must in [20,99], or [-99,-20] for binary.
    if ((nendf_value not in range(20, 100)) and
        (nendf_value not in range(-99, -19))):
        error_msg = 'illegal nendf unit number (' + str(nendf_value) + ').'
        semantic_error(error_msg, nendf)
    
    npend = get_identifier('npend', statement_list)
    # npend must be defined. Translator cannot guess unit numbers.
    if not_defined(npend):
        semantic_error('identifier "npend" not defined.', npend)

    npend_value = get_value(get_r_value(npend))
    # The npend unit number must be an integer.
    if not isinstance(npend_value, int):
        error_msg = 'illegal npend unit number (' + str(npend_value) + ').'
        semantic_error(error_msg, nendf)

    # The npend unit number must in [20,99], or [-99,-20] for binary.
    if ((npend_value not in range(20, 100)) and
        (npend_value not in range(-99, -19))):
        error_msg = 'illegal npend unit number (' + str(npend_value) + ').'
        semantic_error(error_msg, nendf)

    # XXX
    return None

##############################################################################
# Helpers.


### Getter helpers.

def get_card(card, card_list):
    '''
        Return card node of 'card' if 'card' is in 'card_list', else None.
    '''
    for c in card_list:
        if c['card_name'] == card:
            return c
    return None

def get_identifier(id, statement_list):
    '''
        Return identifier node of 'id' if 'id' is in 'statement_list',
        else None.
    '''
    for expression in statement_list:
        if is_assignment(expression) and expression['identifier'] == id:
            return expression
    return None

def get_r_value(assignment):
    '''
        Return the r_value node of the 'assignment' node.
    '''
    return assignment['r_value']

def get_value(r_value):
    '''
        Return the value of the 'r_value' node.
    '''
    return r_value['value']

### Boolean helpers.

def is_assignment(expr):
    '''
        Return True if 'expr' is an assignment node, else False.
    '''
    return expr['node_type'] == '='

def not_defined(node):
    '''Return True if 'node' is None, else False.'''
    return node is None

### Misc helpers.

# XXX: Better to raise an exception and catch on a higher level?
def semantic_error(msg, node):
    try:
        line = node['line_number']
    # Catch nodes which doesn't have the key 'line_number' defined.
    except KeyError:
        line = None
    # Catch None. E.g. in case of undefined identifier.
    except TypeError:
        line = None
    sys.stderr.write('--- Semantic error on line %s, %s\n' % (line, msg))
    sys.exit('semantic_error')

##############################################################################
# Misc.

if __name__ == '__main__':
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        ast = nif_parser.parse(open(filename).read())
    else:
        ast = nif_parser.parse(sys.stdin.read())
    ast = analyze(ast)
    print '--- analyzer: XXX AST:'
    pprint(ast)
