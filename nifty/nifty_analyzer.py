import sys
from pprint import pprint as pprint

import nifty_parser

##############################################################################
# Analyzer.

def analyze(ast):
    analyze_program(ast)
    return ast

def analyze_program(program):
    module_list = program['module_list']
    analyze_module_list(module_list)

def analyze_module_list(module_list):
    for module in module_list:
        analyze_module(module)

def analyze_module(module):
    # XXX: Fix big ugly switch.
    if module['module_name'] == 'stop':
        pass
    elif module['module_name'] == 'reconr':
        analyze_reconr(module)
    else:
        print '--- analyzer: XXX not implemented yet:', module['module_name']

def analyze_reconr(module):
    card_list = module['card_list']
    analyze_reconr_card_list(card_list)

def analyze_reconr_card_list(card_list):
    # Check for cards that must be defined.
    # XXX: card_6 must be defined if ngrid > 0 in card 3.
    must_be_defined = ['card_1', 'card_3', 'card_4', 'card_5']
    cards_must_be_defined(must_be_defined, card_list, 'reconr')

    # Check for cards that must be unique (e.g. not defined more than once).
    unique_card_list = ['card_1', 'card_2', 'card_4', 'card_6']
    cards_must_be_unique(unique_card_list, card_list, 'reconr')

    card = get_card('card_1', card_list)
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
        msg = ('identifier \'nendf\' not defined in \'card_1\', module ' +
               '\'reconr\'.')
        semantic_error(msg, nendf)

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
        msg = ('identifier \'npend\' not defined in \'card_1\', module ' +
               '\'reconr\'.')
        semantic_error(msg, npend)

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
# Semantic rules.

def cards_must_be_defined(must_be_defined, card_list, module_name):
    found = False
    for m in must_be_defined:
        for card in card_list:
            if card['card_name'] == m:
                found = True
                break
            else:
                found = False
        if not found:
            # 'm' not defined.
            msg = ('\'' + m + '\' not defined in module \'' +
                   module_name + '\'.')
            semantic_error(msg, None)

def cards_must_be_unique(unique_card_list, card_list, module_name):
    for unique in unique_card_list:
        n = 0
        for card in card_list:
            if card['card_name'] == unique:
                n += 1
            if n > 1:
                # Found more than one instance of 'unique' in card_list.
                msg = ('\'' + card['card_name'] +
                       '\' declared more than once in module \'' +
                       module_name + '\'.')
                semantic_error(msg, card)

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
        ast = nifty_parser.parse(open(filename).read())
    else:
        ast = nifty_parser.parse(sys.stdin.read())
    ast = analyze(ast)
    print '--- nifty analyzer output:'
    pprint(ast)
