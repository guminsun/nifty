import sys

from exceptions import semantic_error

from nifty.settings import settings

##############################################################################
# Boolean helpers.

def is_array(node):
    '''
        Return True if 'node' is an array node, else False.
    '''
    return get_node_type(node) == 'array'

def is_assignment(node):
    '''
        Return True if 'node' is an assignment node, else False.
    '''
    return get_node_type(node) == '='

def is_card(node):
    '''
        Return True if 'node' is a card node, else False.
    '''
    return get_node_type(node) == 'card'

def is_float(node):
    '''
        Return True if 'node' is a float node, else False.
    '''
    return get_node_type(node) == 'float'

def is_identifier(node):
    '''
        Return True if 'node' is an identifier node, else False.
    '''
    return get_node_type(node) == 'identifier'

def is_integer(node):
    '''
        Return True if 'node' is an integer node, else False.
    '''
    return get_node_type(node) == 'integer'

def is_null(node):
    '''
        Return True if 'node' is a null node, else False.
    '''
    return get_node_type(node) == 'null'

def is_string(node):
    '''
        Return True if 'node' is a string node, else False.
    '''
    return get_node_type(node) == 'string'

##############################################################################
# Getter helpers.

def get_array_index(id_node):
    if is_array(id_node):
        return id_node.get('index')
    else:
        return None

def get_card(card_name, module_node):
    '''
        Return card node of 'card_name' if 'card_name' is in "module_node"'s
        card list, else None.
    '''
    card_list = module_node.get('card_list')
    for c in card_list:
        if c.get('card_name') == card_name:
            return c
    return None

def get_cards(card_name, module_node):
    '''
        Return a list of card nodes with card name 'card_name' if 'card_name'
        is in 'card_list'.
    '''
    cards = list()
    card_list = module_node.get('card_list')
    for c in card_list:
        if c.get('card_name') == card_name:
            cards.append(c)
    return cards

def get_default_value(name, order_map):
    for k in order_map:
        identifier = settings.expected_identifier(order_map.get(k))
        if name in identifier.get('valid_name_list'):
            return identifier.get('value').get('default_value')
    return None

def get_identifier_value(internal_name, order_map, card_node):
    if card_node is None:
        return None
    statement_list = card_node.get('statement_list')
    for statement in statement_list:
        name = statement.get('l_value').get('name')
        if internal_name == get_internal_name(name, order_map):
            return statement.get('r_value').get('value')
    # Return default value if the identifier wasn't defined in card_node.
    return get_default_value(internal_name, order_map)

def get_internal_name(name, order_map):
    for k in order_map:
        identifier = settings.expected_identifier(order_map.get(k))
        if name in identifier.get('valid_name_list'):
            return identifier.get('internal_name')
    return None

def get_node_type(node):
    if node is None:
        return None
    else:
        return node.get('node_type')

##############################################################################
# Misc. helpers.

def get_card_iterator(module_node):
    '''
        Return an iterator for 'module_node's card list.
    '''
    card_list = module_node.get('card_list')
    return iter(card_list)

def get_statement_iterator(card_node):
    '''
        Return an iterator for 'card_node's statement list.
    '''
    statement_list = card_node.get('statement_list')
    return iter(statement_list)

def next(iterator):
    '''
        Return next object in 'iterator' if there is one, else None.
    '''
    try:
        return iterator.next()
    except StopIteration:
        return None
