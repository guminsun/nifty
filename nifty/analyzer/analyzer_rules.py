import sys

from nifty.environment.exceptions import semantic_error
from nifty.environment import helpers as env

##############################################################################
# Common identifiers are analyzed exactly the same.

def analyze_material(name, node, card, module):
    # XXX: material must not be 0? 0 usually denotes termination of material
    # or module.
    # The node is expected to be an assignment node.
    l_value, r_value = must_be_assignment(node, card, module)
    # The l-value and r-value are both expected to be a singleton node.
    l_value_singleton = must_be_singleton(l_value, card, module)
    r_value_singleton = must_be_singleton(r_value, card, module)
    # The l-value of the assignment is expected to be an identifier; name
    identifier_must_be_defined(name, l_value_singleton, card, module)
    return r_value_singleton.get('value')

def analyze_identifier_tempd(node, card, module):
    # Temperature does not have to be defined. Defaults to 300.
    if node is None:
        return 300
    else:
        # The node is expected to be an assignment node.
        l_value, r_value = must_be_assignment(node, card, module)
        # The l-value and r-value are both expected to be a singleton nodes.
        l_value_singleton = must_be_singleton(l_value, card, module)
        r_value_singleton = must_be_singleton(r_value, card, module)
        # The l-value of the assignment is expected to be an identifier; tempd
        identifier_must_be_defined('tempd', l_value_singleton, card, module)
    return r_value_singleton.get('value')

def analyze_singleton(node, card, module):
    # 'node' is expected to be an assignment node.
    l_value, r_value = must_be_assignment(node, card, module)
    # The l-value and r-value of 'node' are expected to be a singleton nodes.
    l_value_singleton = must_be_singleton(l_value, card, module)
    r_value_singleton = must_be_singleton(r_value, card, module)
    return l_value_singleton, r_value_singleton

def analyze_optional_unit_number(id_name, node, card, module):
    # Assuming that the default value for all optional unit numbers is zero.
    if node is None:
        return 0
    else:
        # The node is expected to be an assignment node.
        l_value, r_value = must_be_assignment(node, card, module)
        # The l-value and r-value are both expected to be a singleton nodes.
        l_value_singleton = must_be_singleton(l_value, card, module)
        r_value_singleton = must_be_singleton(r_value, card, module)
        # The l-value of the assignment is expected to be an identifier.
        identifier_must_be_defined(id_name, l_value_singleton, card, module)
        value = must_be_unit_number(l_value_singleton, r_value_singleton, card, module)
        return value

def analyze_pair(node, card, module):
    # 'node' is expected to be an assignment node.
    l_value, r_value = must_be_assignment(node, card, module)
    # The l-value and r-value of 'node' are expected to be a pair nodes.
    l_value_pair = must_be_pair(l_value, card, module)
    r_value_pair = must_be_pair(r_value, card, module)
    return l_value_pair, r_value_pair

def analyze_unit_number(id_name, node, card, module):
    # The node is expected to be an assignment node.
    l_value, r_value = must_be_assignment(node, card, module)
    # The l-value and r-value are both expected to be a singleton nodes.
    l_value_singleton = must_be_singleton(l_value, card, module)
    r_value_singleton = must_be_singleton(r_value, card, module)
    # The l-value of the assignment is expected to be an identifier; id_name
    identifier_must_be_defined(id_name, l_value_singleton, card, module)
    value = must_be_unit_number(l_value_singleton, r_value_singleton, card, module)
    return value

##############################################################################
# Semantic rules.

def array_must_be_defined(expected, node, card_node, module_node):
    card_name = card_node.get('card_name')
    module_name = module_node.get('module_name')
    expected_name = expected[0]
    expected_index = expected[1]
    expected_name_index = expected_name + '[' + str(expected_index) + ']'
    # If the node is defined, it must be an array node.
    if node is None:
        msg = ('expected array \'' + expected_name_index + '\' in \'' +
               card_name + '\', module \'' + module_name + '\'.')
        semantic_error(msg, card_node)
    must_be_array(node, card_node, module_node)
    # Check if the array is the expected one.
    name = env.get_identifier_name(node)
    index = node.get('index')
    name_index = name + '[' + str(index) + ']'
    if not env.is_valid_name(name, expected_name):
        msg = ('expected array \'' + expected_name_index + '\' but saw \'' +
               name_index + '\' in \'' + card_name + '\', module \'' +
               module_name + '\'.')
        semantic_error(msg, node)
    # Check if the index is the expected one.
    index = node.get('index')
    if expected_index != index:
        msg = ('index mismatch; expected array \'' + expected_name_index +
               '\' but saw \'' + name_index + '\' in \'' + card_name +
               '\', module \'' + module_name + '\'.')
        semantic_error(msg, node)
    return node

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

def identifier_must_be_defined(id_name, node, card_node, module_node):
    card_name = card_node.get('card_name')
    module_name = module_node.get('module_name')
    if node is None:
        msg = ('expected identifier \'' + id_name + '\' in \'' + card_name +
               '\', module \'' + module_name + '\'.')
        semantic_error(msg, card_node)
    must_be_identifier(node, card_node, module_node)
    name = env.get_identifier_name(node)
    if not env.is_valid_name(name, id_name):
        msg = ('expected identifier \'' + id_name + '\' but saw \'' +
               name + '\' in \'' + card_name + '\', module \'' + module_name +
               '\'.')
        semantic_error(msg, node)
    return node

def must_be_array(node, card_node, module_node):
    if env.is_array(node):
        return node
    elif node is None:
        return None
    else:
        node_type = env.get_node_type(node)
        card_name = card_node.get('card_name')
        module_name = module_node.get('module_name')
        msg = ('expected an array declaration but saw ' + node_type +
               ' in \'' + card_name + '\', module \'' + module_name + '\'.')
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

def must_be_identifier(node, card_node, module_node):
    if env.is_identifier(node):
        return node
    elif node is None:
        return None
    else:
        node_type = env.get_node_type(node)
        card_name = card_node.get('card_name')
        module_name = module_node.get('module_name')
        msg = ('expected an identifier declaration but saw ' + node_type +
               ' in \'' + card_name + '\', module \'' + module_name + '\'.')
        semantic_error(msg, node)

def must_be_float(lval, rval, card_node, module_node):
    value = rval.get('value')
    if not isinstance(eval(str(value)), float):
        id_name = lval.get('name')
        card_name = card_node.get('card_name')
        module_name = module_node.get('module_name')
        msg = ('expected \'' + id_name + '\' to be defined as a float in \'' +
               card_name + '\', module \'' + module_name + '\'.')
        semantic_error(msg, lval)
    return value

def must_be_int(lval, rval, card_node, module_node):
    value = rval.get('value')
    if not isinstance(value, int):
        name = lval.get('name')
        card_name = card_node.get('card_name')
        module_name = module_node.get('module_name')
        msg = ('expected \'' + name + '\' to be defined as an integer in \'' +
               card_name + '\', module \'' + module_name + '\'.')
        semantic_error(msg, lval)
    return value

def must_be_pair(node, card_node, module_node):
    # XXX: Supply expected pair to generate a better error message?
    if env.is_pair(node):
        return node.get('element_1'), node.get('element_2')
    elif node is None:
        return None, None
    else:
        node_type = env.get_node_type(node)
        card_name = card_node.get('card_name')
        module_name = module_node.get('module_name')
        msg = ('expected a pair declaration but saw ' + node_type +
               ' declaration, in \'' + card_name + '\' module \'' +
               module_name + '\'.')
        semantic_error(msg, card_node)

def must_be_singleton(node, card_node, module_node):
    if env.is_singleton(node):
        return node.get('element_1')
    elif node is None:
        return None
    else:
        node_type = env.get_node_type(node)
        card_name = card_node.get('card_name')
        module_name = module_node.get('module_name')
        msg = ('expected a singleton declaration but saw ' + node_type +
               ' declaration, in \'' + card_name + '\' module \'' +
               module_name + '\'.')
        semantic_error(msg, card_node)

def must_be_string(lval, rval, card_node, module_node):
    if not env.is_string(rval):
        id_name = lval.get('name')
        card_name = card_node.get('card_name')
        module_name = module_node.get('module_name')
        msg = ('expected \'' + id_name + '\' to be defined as a string in ' +
               '\'' + card_name + '\', module \'' + module_name + '\'.')
        semantic_error(msg, lval)
    return rval.get('value')

def must_be_unit_number(lval, rval, card_node, module_node):
    must_be_int(lval, rval, card_node, module_node)
    value = rval.get('value')
    # A unit number must be in [20,99], or [-99,-20] for binary.
    # Or possible 0 (zero) which denotes no unit.
    if ((value not in range(20, 100)) and
        (value not in range(-99, -19)) and
        (value != 0)):
        name = lval.get('name')
        card_name = card_node.get('card_name')
        module_name = module_node.get('module_name')
        msg = ('expected \'' + name + '\' to be defined as an unit number ' +
               'in \'' + card_name + '\', module \'' + module_name + '\'.')
        semantic_error(msg, lval)
    return value

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

def pair_must_be_defined(expected_pair, l_value_pair, r_value_pair, card_node, module_node):
    # XXX: Describe workflow with analyze_pair and pair_must_be_defined.
    card_name = card_node.get('card_name')
    module_name = module_node.get('module_name')
    # Unpack expected data.
    expected_name_1 = expected_pair[0][0]
    expected_name_2 = expected_pair[1][0]
    expected_index_1 = expected_pair[0][1]
    expected_index_2 = expected_pair[1][1]
    expected_pair_name = expected_name_1 + ',' + expected_name_2
    # Make sure both nodes are defined.
    if (l_value_pair is None) or (r_value_pair is None):
        msg = ('expected pair \'' + expected_pair_name + '\' in \'' +
               card_name + '\', module \'' + module_name + '\'.')
        semantic_error(msg, card_node)
    # Check the expected pair depending on whether they are supposed to be
    # defined as regular identifiers or arrays.
    if (expected_index_1 is None) and (expected_index_2 is None):
        identifier_must_be_defined(expected_name_1, l_value_pair[0], card_node, module_node)
        identifier_must_be_defined(expected_name_2, l_value_pair[1], card_node, module_node)
    else:
        array_must_be_defined(expected_pair[0], l_value_pair[0], card_node, module_node)
        array_must_be_defined(expected_pair[1], l_value_pair[1], card_node, module_node)
    # XXX: Check the type of the nodes? Must not differ?
    return l_value_pair, r_value_pair

def string_must_not_exceed_length(lval, rval, max_length, card_node, module_node):
    # Make sure it's a string before continuing.
    string = must_be_string(lval, rval, card_node, module_node)
    if len(string) > max_length:
        id_name = lval.get('name')
        card_name = card_node.get('card_name')
        module_name = module_node.get('module_name')
        msg = ('expected \'' + id_name + '\' to be at most ' +
               str(max_length) + ' characters in \'' + card_name +
               '\', module ' + '\'' + module_name + '\'.')
        semantic_error(msg, lval)
    return string

def too_few_cards_defined(number_of_cards, expected_number, card_name, module):
    module_name = module.get('module_name')
    msg = ('expected ' + str(expected_number) + ' \'' + card_name + '\'s ' +
           'but saw ' + str(number_of_cards) + ', in module \'' +
           module_name + '\'.')
    semantic_error(msg, module)
