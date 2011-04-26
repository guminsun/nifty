import sys

from nifty.environment import helpers as env

##############################################################################
# Semantic rules.

def card_must_be_defined(card_name, module_node, msg):
    card_node = env.get_card(card_name, module_node)
    if card_node is None:
        msg = ('card \'' + card_name + '\' not defined in module \'' +
               module_node['module_name'] + '\' (' + msg + ').')
        semantic_error(msg, module_node)
    return card_node

def card_must_not_be_defined(card_name, module_node, msg):
    card_node = env.get_card(card_name, module_node)
    if card_node is not None:
        msg = ('card \'' + card_name + '\' should not be defined in module ' +
               '\'' + module_node['module_name'] + '\' (' + msg + ').')
        semantic_error(msg, card_node)
    return card_node

def cards_must_be_defined(must_be_defined, module_node):
    cards = list()
    for card_name in must_be_defined:
        msg = ('i.e. expected a declaration of \'' + card_name + '\'')
        c = card_must_be_defined(card_name, module_node, msg)
        cards.append(c)
    return cards

def card_must_be_unique(card_name, module_node):
    card_node = env.get_card(card_name, module_node)
    cards = env.get_cards(card_name, module_node)
    if len(cards) > 1:
        # Found more than one instance of 'card_name' in 'cards'.
        msg = ('card \'' + card_name + '\' declared more than ' +
               'once in module \'' + module_node['module_name'] + '\'.')
        semantic_error(msg, card_node)
    return card_node

def cards_must_be_unique(unique_card_list, module_node):
    for card_name in unique_card_list:
        cards = env.get_cards(card_name, module_node)
        card_must_be_unique(card_name, module_node)
    return cards

def identifier_must_be_defined(name_index, node, card_node, module_node):
    id_name = name_index[0]
    id_index = name_index[1]

    if node is None:
        msg = ('identifier \'' + id_name + '\' not defined in \'' +
               card_node['card_name'] + '\', module \'' +
               module_node['module_name'] + '\'.')
        semantic_error(msg, card_node)

    l_value_node = env.get_l_value(node)
    l_value_node_type = env.get_node_type(node)
    name = env.get_identifier_name(l_value_node)
    # 'index' is an integer if 'l_value_node' is an array, else None.
    index = env.get_array_index(l_value_node)

    if not env.is_valid_name(name, id_name):
        msg = ('expected identifier \'' + id_name + '\' but saw \'' +
               name + '\' in \'' + card_node['card_name'] +
               '\', module \'' + module_node['module_name'] + '.')
        semantic_error(msg, l_value_node)

    if id_index is None:
        node_must_be_identifier(l_value_node, card_node, module_node)
    else:
        node_must_be_array(l_value_node, card_node, module_node)
        if id_index != index:
            msg = ('expected array index ' + str(id_index) + ' for \'' +
                   id_name + '\' but saw ' + str(index) + ' in \'' +
                   card_node['card_name'] + '\', module \'' +
                   module_node['module_name'] + '.')
            semantic_error(msg, l_value_node)

    return node

def identifier_must_be_float(node):
    value = env.get_value(env.get_r_value(node))
    if not isinstance(eval(str(value)), float):
        id_name = env.get_identifier_name(env.get_l_value(node))
        msg = ('identifier \'' + id_name + '\' not defined as a float.')
        semantic_error(msg, node)
    return value

def identifier_must_be_int(node):
    value = env.get_value(env.get_r_value(node))
    if not isinstance(value, int):
        id_name = env.get_identifier_name(env.get_l_value(node))
        msg = ('identifier \'' + id_name + '\' not defined as an integer.')
        semantic_error(msg, node)
    return value

def identifier_must_be_string(id_node, card_node, module_node):
    value = env.get_value(env.get_r_value(id_node))
    if not isinstance(value, str):
        id_name = env.get_identifier_name(env.get_l_value(id_node))
        card_name = card_node['card_name']
        module_name = module_node['module_name']
        msg = ('identifier \'' + id_name + '\' not defined as a string in ' +
               '\'' + card_name + '\', module \'' + module_name + '\'.')
        semantic_error(msg, id_node)
    return value

def identifier_must_be_unit_number(node):
    # Make sure it's an int before continuing.
    identifier_must_be_int(node)
    value = env.get_value(env.get_r_value(node))
    # A unit number must be in [20,99], or [-99,-20] for binary, or 0 (zero)
    # to which denotes no unit.
    if ((value not in range(20, 100)) and
        (value not in range(-99, -19)) and
        (value != 0)):
        id_name = env.get_identifier_name(env.get_l_value(node))
        msg = ('\'' + id_name + '\' illegal unit number (' + str(value) +
               ').')
        semantic_error(msg, node)
    return value

def identifier_string_must_not_exceed_length(id_node, max_length, card_node,
                                             module_node):
    # Make sure it's a string before continuing.
    string = identifier_must_be_string(id_node, card_node, module_node)
    if len(string) > max_length:
        id_name = env.get_identifier_name(env.get_l_value(id_node))
        card_name = card_node['card_name']
        module_name = module_node['module_name']
        msg = ('identifier \'' + id_name + '\' exceeds the ' +
               str(max_length) + ' character length in \'' + card_name +
               '\', module ' + '\'' + module_name + '\'.')
        semantic_error(msg, id_node)
    return 'ok'

def node_must_be_array(l_value_node, card_node, module_node):
    if env.is_array(l_value_node):
        return l_value_node
    else:
        id_name = env.get_identifier_name(l_value_node)
        node_type = env.get_node_type(l_value_node)
        msg = ('identifier \'' + id_name + '\' defined as an ' + node_type +
               ' in \'' + card_node['card_name'] + '\', module \'' +
               module_node['module_name'] + '\' (expected an array ' +
               'identifier declaration).')
        semantic_error(msg, l_value_node)

def node_must_be_identifier(l_value_node, card_node, module_node):
    if env.is_identifier(l_value_node):
        return l_value_node
    else:
        id_name = env.get_identifier_name(l_value_node)
        node_type = env.get_node_type(l_value_node)
        msg = ('identifier \'' + id_name + '\' defined as an ' + node_type +
               ' in \'' + card_node['card_name'] + '\', module \'' +
               module_node['module_name'] + '\' (expected a regular ' +
               'identifier declaration).')
        semantic_error(msg, l_value_node)

def no_more_statement_allowed(node, card_node, module_node):
    if not env.not_defined(node):
        node_name = env.get_identifier_name(env.get_l_value(node))
        node_value = env.get_value(env.get_r_value(node))
        stmt = node_name + ' = ' + str(node_value)
        card_name = card_node['card_name']
        module_name = module_node['module_name']
        msg = ('unexpected statement: \'' + stmt + '\', no more ' +
               'statements was expected in \'' + card_name + '\', module ' +
               '\'' + module_name + '\'.')
        semantic_error(msg, node)

def number_of_cards_must_be(number, card_name_1, card_name_2, module):
    '''
        Return 'number' if the number of cards for 'card_name_1' is equal to
        'number', else a semantic error indicating the ratio mismatch.
    '''
    card_list_1 = env.get_cards(card_name_1, module)
    card_len_1 = len(card_list_1)
    if card_len_1 != number:
        module_name = env.get_module_name(module)
        msg = ('in module \'' + module_name + '\': card \'' + card_name_1 +
               '\' is declared ' + str(card_len_1) + ' time(s) while card \'' +
               card_name_2 + '\' has been ' + 'declared ' + str(number) +
               ' time(s), expected a 1:1 ratio.')
        semantic_error(msg, module)
    return number

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
