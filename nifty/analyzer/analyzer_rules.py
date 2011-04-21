import sys

from nifty.environment import helpers as helper

##############################################################################
# Misc. analyzer helper rules.

def analyze_identifier_matd(card_node, module_node):
    identifier_must_be_defined('matd', card_node, module_node)
    return 'ok'

def analyze_identifier_tempd(card_node, module_node):
    # XXX: Temperature does not have to be defined. Defaults to 300.
    # Pass for now.
    pass

##############################################################################
# Semantic rules.

def cards_must_be_defined(must_be_defined, module_node):
    cards = list()
    for card_name in must_be_defined:
        msg = ('i.e. expected a declaration of \'' + card_name + '\'')
        c = card_must_be_defined(card_name, module_node, msg)
        cards.append(c)
    return cards

def card_must_be_defined(card_name, module_node, msg):
    card_node = helper.get_card(card_name, module_node)
    if card_node is None:
        msg = ('card \'' + card_name + '\' not defined in module \'' +
               module_node['module_name'] + '\' (' + msg + ').')
        semantic_error(msg, module_node)
    return card_node

def card_must_not_be_defined(card_name, module_node, msg):
    card_node = helper.get_card(card_name, module_node)
    if card_node is not None:
        msg = ('card \'' + card_name + '\' should not be defined in module ' +
               '\'' + module_node['module_name'] + '\' (' + msg + ').')
        semantic_error(msg, card_node)
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

def number_of_cards_must_be(number, card_name_1, card_name_2, module):
    '''
        Return 'ok' if the number of cards for 'card_name_1' is equal to
        'number', else a semantic error indicating the ratio mismatch.
    '''
    card_list_1 = helper.get_cards(card_name_1, module)
    card_len_1 = len(card_list_1)
    if card_len_1 != number:
        module_name = helper.get_module_name(module)
        msg = ('in module \'' + module_name + '\': card \'' + card_name_1 +
               '\' is declared ' + str(card_len_1) + ' time(s) while card \'' +
               card_name_2 + '\' has been ' + 'declared ' + str(number) +
               ' time(s), expected a 1:1 ratio.')
        semantic_error(msg, module)
    return 'ok'

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

def identifier_must_be_float(node):
    value = helper.get_value(helper.get_r_value(node))
    if not isinstance(eval(str(value)), float):
        id_name = helper.get_identifier_name(helper.get_l_value(node))
        msg = ('identifier \'' + id_name + '\' not defined as a float.')
        semantic_error(msg, node)
    return value

def identifier_must_be_int(node):
    value = helper.get_value(helper.get_r_value(node))
    if not isinstance(value, int):
        id_name = helper.get_identifier_name(helper.get_l_value(node))
        msg = ('identifier \'' + id_name + '\' not defined as an integer.')
        semantic_error(msg, node)
    return value

def identifier_must_be_string(id_node, card_node, module_node):
    value = helper.get_value(helper.get_r_value(id_node))
    if not isinstance(value, str):
        id_name = helper.get_identifier_name(helper.get_l_value(id_node))
        card_name = card_node['card_name']
        module_name = module_node['module_name']
        msg = ('identifier \'' + id_name + '\' not defined as a string in ' +
               '\'' + card_name + '\', module \'' + module_name + '\'.')
        semantic_error(msg, id_node)
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
        id_name = helper.get_identifier_name(helper.get_l_value(node))
        msg = ('\'' + id_name + '\' illegal unit number (' + str(value) +
               ').')
        semantic_error(msg, node)
    return value

def identifier_string_must_not_exceed_length(id_node, max_length, card_node,
                                             module_node):
    # Make sure it's a string before continuing.
    string = identifier_must_be_string(id_node, card_node, module_node)
    if len(string) > max_length:
        id_name = helper.get_identifier_name(helper.get_l_value(id_node))
        card_name = card_node['card_name']
        module_name = module_node['module_name']
        msg = ('identifier \'' + id_name + '\' exceeds the ' +
               str(max_length) + ' character length in \'' + card_name +
               '\', module ' + '\'' + module_name + '\'.')
        semantic_error(msg, id_node)
    return 'ok'

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
