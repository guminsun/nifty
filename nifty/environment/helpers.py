import sys
from copy import deepcopy

from exceptions import semantic_error
# Get the identifier map of valid identifier names. The map is used in the
# functions 'get_identifier_name' and 'is_valid_name'.
from settings import identifier_map

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

def is_valid_name(name_to_validate, reserved_id_name):
    '''
        Return True if 'name_to_validate' is a valid, possible alternative,
        name for 'reserved_id_name', else False.
    '''
    id_name_value = identifier_map.get(reserved_id_name, reserved_id_name)
    if isinstance(id_name_value, list):
        return name_to_validate in id_name_value
    else:
        return name_to_validate == reserved_id_name

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

def get_identifier_name(id_node):
    '''
        Return name of the identifier 'id_node', if it is an valid name, else
        report an error.
    '''
    valid_id_names = get_valid_id_names()
    id_name = id_node.get('name')
    if id_name in valid_id_names:
        return id_name
    else:
        msg = '\'' + id_name + '\' is not a valid identifier name.'
        semantic_error(msg, id_node)

def get_identifier_value(id_name, expected_map, card_node):
    if card_node is None:
        return None
    statement_list = card_node.get('statement_list')
    for statement in statement_list:
        name = statement.get('l_value').get('name')
        internal_name = get_internal_name(name, expected_map)
        if internal_name == id_name:
            return statement.get('r_value').get('value')
    # Return default value if the identifier wasn't defined in card_node.
    return expected_map.get(id_name).get('value').get('default_value')

def get_internal_name(name, expected_map):
    for internal_name in expected_map:
        if name in expected_map.get(internal_name).get('valid_name_list'):
            return internal_name
    return None

def get_internal_identifier_name(id_name):
    for internal_name in identifier_map:
        if id_name in identifier_map[internal_name]:
            return internal_name
    return None

def get_node_type(node):
    if node is None:
        return None
    else:
        return node.get('node_type')

def get_valid_id_names():
    return [i for sub in identifier_map.values() for i in sub]

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

def skip(n, iterator):
    '''
        Skips 'n' objects in 'iterator'.
    '''
    for i in range(n): next(iterator)
