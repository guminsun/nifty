import sys
from copy import deepcopy as deepcopy
from pprint import pprint as pprint

import nif_parser

##############################################################################
# Analyzer.

def analyze(ast):
    new_ast = deepcopy(ast)
    return analyze_program(ast, new_ast)

def analyze_program(program, ast):
    module_list = program['module_list']
    return analyze_module_list(module_list, ast)

def analyze_module_list(module_list, ast):
    for module in module_list:
        ast = analyze_module(module, ast)
    return ast

def analyze_module(module, ast):
    # XXX: Fix big ugly switch.
    if module['module_name'] == 'stop':
        pass
    elif module['module_name'] == 'reconr':
        ast = analyze_reconr(module, ast)
    else:
        print '--- analyzer: XXX not implemented yet:', module['module_name']
    return ast

def analyze_reconr(module, ast):
    card_list = module['card_list']
    return analyze_reconr_card_list(card_list, ast)

def analyze_reconr_card_list(card_list, ast):
    # Check for cards which must be unique (e.g. not defined more than once).
    unique_card_list = ['card_1']
    must_be_unique(unique_card_list, card_list)
    # XXX: Need to handle more than one card of the same type.
    card = get_card('card_1', card_list)
    if not_defined(card):
        msg = '\'card_1\' not defined in module \'reconr\'.'
        semantic_error(msg, None)
    analyze_reconr_card_1(card)
    # XXX
    return ast

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

### Rules.
def must_be_unique(unique_card_list, card_list):
    for u in unique_card_list:
        n = 0
        for c in card_list:
            if c['card_name'] == u:
                n += 1
            if n > 1:
                # Found more than one instance of a unique card.
                msg = '\'' + c['card_name'] + '\' previously declared.'
                semantic_error(msg, c)

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
