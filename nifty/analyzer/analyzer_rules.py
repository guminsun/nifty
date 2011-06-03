import sys

from nifty.environment.exceptions import semantic_error
from nifty.environment import helpers as env
from nifty.settings import settings

##############################################################################
# General analyzers.

def analyze_statement(order_map_tuple, node, card, module):
    # XXX: The only statements implemented so far are assignments.
    # Note that if node is None, must_be_assignment will return two None's.
    l_value, r_value = must_be_assignment(node, card, module)
    # Check for optional statements; identifiers which doesn't have to be
    # defined. Note that if the l_value is not None, e.g. a identifier has
    # been defined, then it needs to be analyzed as usal to make sure it is
    # the expected identifier (that the type is correct, et cetera).
    expected_identifier = settings.expected_identifier(order_map_tuple)
    if expected_identifier.get('is_optional') and l_value is None:
        return node
    analyze_l_value(l_value, order_map_tuple, card, module)
    analyze_r_value(expected_identifier, l_value, r_value, card, module)
    return node

def analyze_l_value(l_value, order_map_tuple, card, module):
    expected_identifier = settings.expected_identifier(order_map_tuple)
    if settings.is_identifier(order_map_tuple):
        return analyze_identifier(expected_identifier, l_value, card, module)
    elif settings.is_array(order_map_tuple):
        expected_array_index = settings.expected_array_index(order_map_tuple)
        return analyze_array(expected_array_index, expected_identifier, l_value, card, module)
    else:
        # Erroneous expected array index has been defined in the tuple?
        raise TypeError('erroneous array index', order_map_tuple)

def analyze_identifier(expected_identifier, node, card, module):
    must_be_identifier(expected_identifier, node, card, module)
    must_be_valid_name(expected_identifier, node, card, module)
    return node

def analyze_array(expected_array_index, expected_identifier, node, card, module):
    must_be_array(expected_identifier, node, card, module)
    must_be_valid_name(expected_identifier, node, card, module)
    must_be_valid_index(expected_array_index, node, card, module)
    return node

def analyze_r_value(identifier, l_value, r_value, card, module):
    value = identifier.get('value')
    if env.is_float(value):
        return analyze_float(identifier, l_value, r_value, card, module)
    elif env.is_integer(value):
        return analyze_integer(identifier, l_value, r_value, card, module)
    elif env.is_null(value):
        return analyze_null(identifier, l_value, r_value, card, module)
    elif env.is_string(value):
        return analyze_string(identifier, l_value, r_value, card, module)
    elif value.get('node_type') is None:
        # Values with unknown type is not analyzed.
        return r_value
    else:
        # Erroneous value type has been defined in the settings?
        raise TypeError('erroneous value type', value)

def analyze_float(expected, l_value, r_value, card, module):
    must_be_float(l_value, r_value, card, module)
    return r_value

def analyze_integer(expected, l_value, r_value, card, module):
    must_be_integer(l_value, r_value, card, module)
    must_be_in_range(expected, l_value, r_value, card, module)
    return r_value

def analyze_null(expected, l_value, r_value, card, module):
    must_be_null(l_value, r_value, card, module)
    return r_value

def analyze_string(expected, l_value, r_value, card, module):
    must_be_string(l_value, r_value, card, module)
    must_be_in_length(expected, l_value, r_value, card, module)
    return r_value

##############################################################################
# Semantic rules.

def card_must_be_defined(card_name, card_node, module_node, explanation):
    module_name = module_node.get('module_name')
    if card_node is None:
        msg = ('expected card \'' + card_name + '\' in module \'' +
               module_name + '\'.')
        if explanation is not None:
            msg += ' (' + explanation + ')'
        semantic_error(msg, module_node)
    must_be_card(card_node, module_node)
    node_name = card_node.get('card_name')
    if not (card_name == node_name):
        msg = ('expected card \'' + card_name + '\' but saw \'' +
               node_name + '\' in module \'' + module_name + '\'.')
        if explanation is not None:
            msg += ' (' + explanation + ')'
        semantic_error(msg, card_node)
    return card_node

def must_be_array(expected_identifier, node, card_node, module_node):
    card_name = card_node.get('card_name')
    module_name = module_node.get('module_name')
    internal_name = expected_identifier.get('internal_name')
    if env.is_array(node):
        return node
    elif node is None:
        msg = ('expected array \'' + internal_name + '\' in \'' + card_name +
               '\', module \'' + module_name + '\'.')
        semantic_error(msg, card_node)
    else:
        node_type = env.get_node_type(node)
        msg = ('expected an array declaration of \'' + internal_name +
               '\' but saw a ' + node_type + ' declaration in \'' +
               card_name + '\', module \'' + module_name + '\'.')
        semantic_error(msg, node)

def must_be_assignment(node, card_node, module_node):
    if env.is_assignment(node):
        return node.get('l_value'), node.get('r_value')
    elif node is None:
        return None, None
    else:
        node_type = env.get_node_type(node)
        card_name = card_node.get('card_name')
        module_name = module_node.get('module_name')
        msg = ('expected an assignment declaration but saw ' +
                node_type + ' in \'' + card_name + '\', module \'' +
                module_name + '\'.')
        semantic_error(msg, module_node)

def must_be_card(node, module_node):
    if env.is_card(node):
        return node
    elif node is None:
        return None
    else:
        node_type = env.get_node_type(node)
        module_name = module_node.get('module_name')
        msg = ('expected a card declaration but saw ' + node_type +
               ' in module \'' + module_name + '\'.')
        semantic_error(msg, module_node)

def must_be_float(l_value, r_value, card_node, module_node):
    if not env.is_float(r_value):
        name = l_value.get('name')
        card_name = card_node.get('card_name')
        module_name = module_node.get('module_name')
        msg = ('expected \'' + name + '\' to be defined as a float in \'' +
               card_name + '\', module \'' + module_name + '\'.')
        semantic_error(msg, l_value)
    return r_value.get('value')

def must_be_identifier(expected_identifier, node, card_node, module_node):
    card_name = card_node.get('card_name')
    module_name = module_node.get('module_name')
    internal_name = expected_identifier.get('internal_name')
    if env.is_identifier(node):
        return node
    elif node is None:
        msg = ('expected identifier \'' + internal_name + '\' in \'' +
               card_name + '\', module \'' + module_name + '\'.')
        semantic_error(msg, card_node)
    else:
        node_type = env.get_node_type(node)
        msg = ('expected an identifier declaration of \'' + internal_name +
               '\' but saw a ' + node_type + ' declaration in \'' +
               card_name + '\', module \'' + module_name + '\'.')
        semantic_error(msg, node)

def must_be_integer(l_value, r_value, card_node, module_node):
    if not env.is_integer(r_value):
        name = l_value.get('name')
        card_name = card_node.get('card_name')
        module_name = module_node.get('module_name')
        msg = ('expected \'' + name + '\' to be defined as an integer in \'' +
               card_name + '\', module \'' + module_name + '\'.')
        semantic_error(msg, l_value)
    return r_value.get('value')

def must_be_in_length(expected, l_value, r_value, card_node, module_node):
    length = expected.get('value').get('length')
    value = r_value.get('value')
    # Character string with unknown length is not analyzed.
    if length is None:
        return value
    if len(value) <= length:
        return value
    else:
        # value exceeds the allowed character string length.
        name = l_value.get('name')
        card_name = card_node.get('card_name')
        module_name = module_node.get('module_name')
        msg = ('expected \'' + name + '\' to be at most ' + str(length) +
               ' characters in \'' + card_name + '\', module ' + '\'' +
               module_name + '\'.')
        semantic_error(msg, l_value)

def must_be_in_range(expected, l_value, r_value, card_node, module_node):
    slice_list = expected.get('value').get('slice_list')
    value = r_value.get('value')
    # Identifier with unknown range is not analyzed.
    if slice_list is None or len(slice_list) == 0:
        return value
    for s in slice_list:
        if s.start <= value and value < s.stop:
            return value
    # value is not within any of the defined slices, as such, raise an error.
    name = l_value.get('name')
    card_name = card_node.get('card_name')
    module_name = module_node.get('module_name')
    msg = ('integer value is not in the expected range for \'' + name +
           '\' in \'' + card_name + '\', module \'' + module_name + '\'.')
    semantic_error(msg, l_value)

def must_be_null(l_value, r_value, card_node, module_node):
    if not env.is_null(r_value):
        name = l_value.get('name')
        card_name = card_node.get('card_name')
        module_name = module_node.get('module_name')
        msg = ('expected \'' + name + '\' to be defined as null in \'' +
               card_name + '\', module \'' + module_name + '\'.')
        semantic_error(msg, l_value)
    return r_value.get('value')

def must_be_string(l_value, r_value, card_node, module_node):
    if not env.is_string(r_value):
        name = l_value.get('name')
        card_name = card_node.get('card_name')
        module_name = module_node.get('module_name')
        msg = ('expected \'' + name + '\' to be defined as a character ' +
               'string in \'' + card_name + '\', module \'' + module_name +
               '\'.')
        semantic_error(msg, l_value)
    return r_value.get('value')

def must_be_valid_index(expected_array_index, node, card_node, module_node):
    index = node.get('index')
    if expected_array_index == index:
        return node
    else:
        name = node.get('name')
        card_name = card_node.get('card_name')
        module_name = module_node.get('module_name')
        msg = ('expected array index ' + str(expected_array_index) +
               ' for \'' + name + '\' but saw \'' + str(index) + '\' in \'' +
               card_name + '\', module \'' + module_name + '\'.')
        semantic_error(msg, node)

def must_be_valid_name(expected_identifier, node, card_node, module_node):
    name = node.get('name')
    valid_name_list = expected_identifier.get('valid_name_list')
    if name in valid_name_list:
        return name
    else:
        card_name = card_node.get('card_name')
        module_name = module_node.get('module_name')
        internal_name = expected_identifier.get('internal_name')
        msg = ('expected identifier \'' + internal_name + '\' but saw \'' +
               name + '\' in \'' + card_name + '\', module \'' + module_name +
               '\'.')
        semantic_error(msg, node)

def no_card_allowed(card_node, module_node):
    if card_node is not None:
        card_name = card_node.get('card_name')
        module_name = module_node.get('module_name')
        msg = ('unexpected card: \'' + card_name + '\', no more cards was ' +
               'expected in module \'' + module_name + '\'.')
        semantic_error(msg, card_node)

def no_statement_allowed(node, card_node, module_node):
    if node is not None:
        # XXX: Provide better error message? E.g. include the faulting
        # statement in the error message as well.
        card_name = card_node.get('card_name')
        module_name = module_node.get('module_name')
        msg = ('unexpected statement, no more statements was expected in \'' +
               card_name + '\', module \'' + module_name + '\'.')
        semantic_error(msg, node)

def too_few_cards_defined(number_of_cards, expected_number, card_name, module):
    module_name = module.get('module_name')
    msg = ('expected ' + str(expected_number) + ' \'' + card_name + '\'s ' +
           'but saw ' + str(number_of_cards) + ', in module \'' +
           module_name + '\'.')
    semantic_error(msg, module)
