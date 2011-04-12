import sys
from pprint import pprint as pprint

import nif_parser

##############################################################################
# Analyzer.

def analyze(ast):
    ast = sort_card_lists(ast)
    return analyze_program(ast)

def analyze_program(program):
    module_list = program['module_list']
    return analyze_module_list(module_list, program)

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
    reconr_card_list = ['card_1', 'card_2', 'card_3', 'card_3', 'card_4',
                        'card_5', 'card_6']

    # Check for cards that must be defined.
    # XXX: More cards? According to documentation:
    #   "cards 3, 4, 5, 6 must be input for each material desired"
    # ... but in the last example on http://t2.lanl.gov/njoy/reco02.html
    # card 6 is not part of the input?
    must_be_defined = ['card_1']
    card_must_be_defined(must_be_defined, card_list, 'reconr')

    # Check for cards that must be unique (e.g. not defined more than once).
    unique_card_list = ['card_1', 'card_2']
    card_must_be_unique(unique_card_list, card_list, 'reconr')

    card = get_card('card_1', card_list)
    analyze_reconr_card_1(card)

    card = get_card('card_2', card_list)
    if not_defined(card):
        insert_card(make_card(2, ''), card_list)

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
# Semantic rules.

def card_must_be_defined(must_be_defined, card_list, module_name):
    for m in must_be_defined:
        for c in card_list:
            if c['card_name'] == m:
                return 'ok'
        # 'm' not defined.
        msg = '\'' + m + '\' not defined in module \'' + module_name + '\'.'
        semantic_error(msg, None)

def card_must_be_unique(unique_card_list, card_list, module_name):
    for u in unique_card_list:
        n = 0
        for c in card_list:
            if c['card_name'] == u:
                n += 1
            if n > 1:
                # Found more than one instance of 'u' in card_list.
                msg = ('\'' + c['card_name'] + 
                       '\' declared more than once in module \'' +
                       module_name + '\'.')
                semantic_error(msg, c)

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

def sort_card_lists(program):
    module_list = program['module_list']
    for module in module_list:
        sort_card_list(module['card_list'])
    return program

def sort_card_list(card_list):
    # XXX: Ugly assumption that the card nodes will be sorted on 'card_id'.
    return card_list.sort()

def make_card(id_digit, id_alpha):
    card = dict()
    card['node_type'] = 'card'
    card['line_number'] = None
    card['card_id'] = (id_digit, id_alpha)
    card['card_name'] = 'card_' + str(id_digit) + id_alpha
    card['statement_list'] = list()
    return card

def insert_card(card, card_list):
    card_list.append(card)
    return sort_card_list(card_list)

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
