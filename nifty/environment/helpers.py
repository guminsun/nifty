import sys

# Get the identifier map of valid identifier names, for get_identifier_name.
from settings import identifier_map

##############################################################################
# Boolean helpers.

def is_assignment(expression_node):
    '''
        Return True if 'expression_node' is an assignment node, else False.
    '''
    return get_node_type(expression_node) == '='

def not_defined(node):
    '''Return True if 'node' is None, else False.'''
    return node is None

##############################################################################
# Getter helpers.

def get_card(card_name, module_node):
    '''
        Return card node of 'card_name' if 'card_name' is in "module_node"'s
        card list, else None.
    '''
    card_list = get_card_list(module_node)
    for c in card_list:
        if get_card_name(c) == card_name:
            return c
    return None

def get_cards(card_name, module_node):
    '''
        Return a list of card nodes with card name 'card_name' if 'card_name'
        is in 'card_list'.
    '''
    cards = list()
    card_list = get_card_list(module_node)
    for c in card_list:
        if get_card_name(c) == card_name:
            cards.append(c)
    return cards

def get_card_list(module_node):
    '''
        Return the card list of the module 'module_node'.
    '''
    return module_node['card_list']

def get_card_name(card_node):
    '''
        Return the name of the card 'card_node'.
    '''
    return card_node['card_name']

def get_identifier(reserved_id_name, card_node):
    '''
        Return identifier node of 'reserved_id_name' if 'reserved_id_name' is
        defined in "card_node"'s statement list, else None.
    '''
    statement_list = get_statement_list(card_node)
    for expr in statement_list:
        expr_lval = get_l_value(expr)
        expr_id_name = get_identifier_name(expr_lval)
        if is_assignment(expr) and expr_id_name == reserved_id_name:
            return expr
    return None

def get_identifiers(id_name, card_node):
    '''
        Return list of identifier nodes. The resulting list will include all
        identifier nodes in "card_node"'s statement list which have the name
        'id_name'.
    '''
    identifiers = list()
    statement_list = get_statement_list(card_node)
    for expression in statement_list:
        expression_l_value = get_l_value(expression)
        expression_id_name = get_identifier_name(expression_l_value)
        if is_assignment(expression) and expression_id_name == id_name:
            identifiers.append(expression)
    return identifiers

def get_identifier_name(id_node):
    '''
        Return name of the identifier 'id_node', if it is an valid name, else
        report an error.
    '''
    valid_id_names = [i for sub in identifier_map.values() for i in sub]
    if id_node['name'] in valid_id_names:
        return id_node['name']
    else:
        msg = '\'' + id_node['name'] + '\' is not a valid identifier name.'
        semantic_error(msg, id_node)

def get_l_value(assignment_node):
    '''
        Return l-value node of 'assignment_node'.
    '''
    return assignment_node['l_value']

def get_module_list(program_node):
    '''
        Return module list of 'program_node'.
    '''
    return program_node['module_list']

def get_module_name(module_node):
    '''
        Return name of 'module_node'.
    '''
    return module_node['module_name']

def get_node_type(node):
    '''
        Return node type of 'node'.
    '''
    return node['node_type']

def get_r_value(assignment_node):
    '''
        Return r-value node of 'assignment_node'.
    '''
    return assignment_node['r_value']

def get_statement_list(card_node):
    '''
        Return statement list of 'card_node'.
    '''
    return card_node['statement_list']

def get_value(r_value):
    '''
        Return value of 'r_value'.
    '''
    return r_value['value']

##############################################################################
# Error handling.

def semantic_error(msg, node):
    try:
        line = node['line_number']
    # Catch nodes which doesn't have the key 'line_number' defined.
    except KeyError:
        line = None
    # Catch None. E.g. in case of undefined identifier.
    except TypeError:
        line = None
    print('--- Semantic error on line %s, %s' % (line, msg))
    sys.exit('semantic_error')