import sys

import analyzer_helpers as helper

##############################################################################
# Semantic rules.

def cards_must_be_defined(must_be_defined, module_node):
    cards = list()
    for card_name in must_be_defined:
        c = card_must_be_defined(card_name, module_node)
        cards.append(c)
    return cards

def card_must_be_defined(card_name, module_node):
    card_node = helper.get_card(card_name, module_node)
    if card_node is None:
        msg = ('card \'' + card_name + '\' not defined in \'' +
               '\', module \'' + module_node['module_name'] + '\'.')
        semantic_error(msg, module_node)
    return card_node

def cards_must_be_unique(unique_card_list, module_node):
    for card_name in unique_card_list:
        cards = helper.get_cards(card_name, module_node)
        card_must_be_unique(card_name, module_node)
    return cards

def card_must_be_unique(card_name, module_node):
    card_node = helper.get_card(card_name, module_node)
    cards = helper.get_cards(card_name, module_node)
    if len(cards) > 1:
        # Found more than one instance of 'card_name' in 'cards'.
        msg = ('card \'' + card_name + '\' declared more than ' +
               'once in module \'' + module_node['module_name'] + '\'.')
        semantic_error(msg, card_node)
    return card_node

def identifiers_must_be_defined(must_be_defined, card_node, module_node):
    id_node_list = list()
    for id_name in must_be_defined:
        id_node = identifier_must_be_defined(id_name, card_node, module_node)
        id_node_list.append(id_node)
    return id_node_list

def identifier_must_be_defined(id_name, card_node, module_node):
    id_node = helper.get_identifier(id_name, card_node)
    if id_node is None:
        msg = ('identifier \'' + id_name + '\' not defined in \'' +
               card_node['card_name'] + '\', module \'' +
               module_node['module_name'] + '\'.')
        semantic_error(msg, card_node)
    return id_node

def identifier_must_be_int(node):
    value = helper.get_value(helper.get_r_value(node))
    if not isinstance(value, int):
        msg = ('\'' + node['identifier'] + '\' (value: ' + str(value) + ') ' + 
               'must be an integer.')
        semantic_error(msg, node)
    return value

def identifier_must_be_string(node):
    value = helper.get_value(helper.get_r_value(node))
    if not isinstance(value, str):
        msg = ('\'' + node['identifier'] + '\' (value: ' + str(value) + ') ' + 
               'must be a string.')
        semantic_error(msg, node)
    return value

def identifier_must_be_unit_number(node):
    # Make sure it's an int before continuing.
    identifier_must_be_int(node)
    value = helper.get_value(helper.get_r_value(node))
    # A unit number must be in [20,99], or [-99,-20] for binary, or 0 (zero)
    # to which denotes no unit.
    if ((value not in range(20, 100)) and
        (value not in range(-99, -19)) and
        (value != 0)):
        msg = ('\'' + node['identifier'] + '\' illegal unit number (' +
               str(value) + ').')
        semantic_error(msg, node)
    return value

def identifier_must_be_in_range(node, range1, range2=None):
    pass

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
    sys.stderr.write('--- Semantic error on line %s, %s\n' % (line, msg))
    sys.exit('semantic_error')
