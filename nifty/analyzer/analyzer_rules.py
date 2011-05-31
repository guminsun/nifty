import sys

from nifty.environment.exceptions import semantic_error
from nifty.environment import helpers as env
from nifty.settings import settings

##############################################################################
# EXPERIMENTAL

def analyze_statement_E(order_map, node, card, module):
    # XXX: The only statements implemented so far are assignments.
    # Note that if node is None, must_be_assignment will return two None's.
    l_value, r_value = must_be_assignment(node, card, module)
    # Check for optional statements; identifiers which doesn't have to be
    # defined. Note that if the l_value is not None, e.g. a identifier has
    # been defined, then it needs to be analyzed as usal to make sure it is
    # the expected identifier, that the type is correct, et cetera.
    expected_identifier = settings.expected_identifier(order_map)
    if expected_identifier.get('is_optional') and l_value is None:
        return node
    if settings.is_identifier(order_map):
        analyze_identifier_E(expected_identifier, l_value, card, module)
    elif settings.is_array(order_map):
        expected_array_index = settings.expected_array_index(order_map)
        analyze_array_E(expected_array_index, expected_identifier, l_value, card, module)
    else:
        # Erroneous expected array index has been defined in the order map?
        raise TypeError('erroneous array index', order_map)
    analyze_value_E(expected_identifier, l_value, r_value, card, module)
    return node

def analyze_identifier_E(expected_identifier, node, card, module):
    must_be_identifier_E(expected_identifier, node, card, module)
    must_be_valid_name_E(expected_identifier, node, card, module)
    return node

def must_be_identifier_E(expected_identifier, node, card_node, module_node):
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

def analyze_array_E(expected_array_index, expected_identifier, node, card, module):
    must_be_array_E(expected_identifier, node, card, module)
    must_be_valid_name_E(expected_identifier, node, card, module)
    must_be_valid_index_E(expected_array_index, node, card, module)
    return node

def must_be_array_E(expected_identifier, node, card_node, module_node):
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

def must_be_valid_index_E(expected_array_index, node, card_node, module_node):
    '''
        Precondition: node is an array node.
    '''
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

def must_be_valid_name_E(expected_identifier, node, card_node, module_node):
    '''
        Precondition: node is an array or identifier node.
    '''
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

def analyze_value_E(expected_identifier, l_value, r_value, card_node, module_node):
    value = expected_identifier.get('value')
    if env.is_float(value):
        return analyze_float_E(expected_identifier, l_value, r_value, card_node, module_node)
    elif env.is_integer(value):
        return analyze_integer_E(expected_identifier, l_value, r_value, card_node, module_node)
    elif env.is_null(value):
        return analyze_null_E(expected_identifier, l_value, r_value, card_node, module_node)
    elif env.is_string(value):
        return analyze_string_E(expected_identifier, l_value, r_value, card_node, module_node)
    elif value.get('node_type') is None:
        # Values with unknown type is not analyzed.
        return r_value
    else:
        # Erroneous value type has been defined in the settings?
        raise TypeError('unknown value type', value.get('node_type'))

def analyze_string_E(expected, l_value, r_value, card_node, module_node):
    must_be_string_E(l_value, r_value, card_node, module_node)
    must_be_in_length_E(expected, l_value, r_value, card_node, module_node)
    return r_value

def analyze_float_E(expected, l_value, r_value, card_node, module_node):
    # XXX: Implement.
    return r_value

def analyze_null_E(expected, l_value, r_value, card_node, module_node):
    # XXX: Implement.
    return r_value

def analyze_integer_E(expected, l_value, r_value, card_node, module_node):
    must_be_integer_E(l_value, r_value, card_node, module_node)
    must_be_in_range_E(expected, l_value, r_value, card_node, module_node)
    return r_value

def must_be_string_E(l_value, r_value, card_node, module_node):
    if not env.is_string(r_value):
        name = l_value.get('name')
        card_name = card_node.get('card_name')
        module_name = module_node.get('module_name')
        msg = ('expected \'' + name + '\' to be defined as a character ' +
               'string in \'' + card_name + '\', module \'' + module_name +
               '\'.')
        semantic_error(msg, l_value)
    return r_value.get('value')

def must_be_in_length_E(expected, l_value, r_value, card_node, module_node):
    length = expected.get('value').get('length')
    value = r_value.get('value')
    # Character string with unknown length is not analyzed.
    if length is None:
        return value
    if len(value) < length:
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

def must_be_integer_E(l_value, r_value, card_node, module_node):
    if not env.is_integer(r_value):
        name = l_value.get('name')
        card_name = card_node.get('card_name')
        module_name = module_node.get('module_name')
        msg = ('expected \'' + name + '\' to be defined as an integer in \'' +
               card_name + '\', module \'' + module_name + '\'.')
        semantic_error(msg, l_value)
    return r_value.get('value')

def must_be_in_range_E(expected, l_value, r_value, card_node, module_node):
    slice_list = expected.get('value').get('slice_list')
    value = r_value.get('value')
    # Identifier with unknown range is not analyzed.
    if len(slice_list) == 0 or slice_list is None:
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

##############################################################################
# Common identifiers are analyzed exactly the same.

def analyze_material(name, node, card, module):
    # XXX: material must not be 0? 0 usually denotes termination of material
    # or module. Materials are supposed to be MAT numbers as specified in the
    # ENDF formats, that is; an integer in the range [1,9999].
    l_value, r_value = must_be_assignment(node, card, module)
    # The l-value of the assignment is expected to be an identifier; name
    identifier_must_be_defined(name, l_value, card, module)
    return r_value.get('value')

def analyze_mat1(name, node, card, module):
    # MAT1 is MAT for the second energy-depedent cross section?
    return analyze_material(name, node, card, module)

def analyze_mt(name, node, card, module):
    # Reaction types (MT) are identified in the ENDF formats by an integer
    # number from 1 through 999.
    l_value, r_value = must_be_assignment(node, card, module)
    # The l-value of the assignment is expected to be an identifier; name
    identifier_must_be_defined(name, l_value, card, module)
    mt_number = must_be_int(l_value, r_value, card, module)
    if mt_number not in range(1,1000):
        id_name = l_value.get('name')
        card_name = card.get('card_name')
        module_name = module.get('module_name')
        msg = ('illegal reaction type (MT number, \'' + id_name +
               '\') in \'' + card_name + '\' module \'' + module_name +
               '\'. Expected an integer in the range [1,999].')
        rule.semantic_error(msg, node)
    return mt_number

def analyze_optional_string(max_length, name, node, card, module):
    if node is None:
        return str()
    else:
        l_value, r_value = must_be_assignment(node, card, module)
        identifier_must_be_defined(name, l_value, card, module)
        # The r-value of the assignment is expected to be a string.
        string = must_be_string(l_value, r_value, card, module)
        string_must_not_exceed_length(l_value, r_value, max_length, card, module)
        return string

def analyze_temperature(name, node, card, module):
    # Temperature does not have to be defined. Defaults to 300.
    if node is None:
        return 300
    else:
        l_value, r_value = must_be_assignment(node, card, module)
        # The l-value of the assignment is expected to be an identifier; tempd
        identifier_must_be_defined(name, l_value, card, module)
        # XXX: Additional checks? E.g. must be number.
        return r_value.get('value')

def analyze_unit_number(id_name, node, card, module):
    l_value, r_value = must_be_assignment(node, card, module)
    identifier_must_be_defined(id_name, l_value, card, module)
    unit_number = must_be_unit_number(l_value, r_value, card, module)
    return unit_number

def analyze_optional_unit_number(id_name, node, card, module):
    # Assuming that the default value for all optional unit numbers is zero.
    if node is None:
        return 0
    else:
        l_value, r_value = must_be_assignment(node, card, module)
        # The l-value of the assignment is expected to be an identifier.
        identifier_must_be_defined(id_name, l_value, card, module)
        unit_number = must_be_unit_number(l_value, r_value, card, module)
        return unit_number

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
    if not env.is_float(rval):
        id_name = lval.get('name')
        card_name = card_node.get('card_name')
        module_name = module_node.get('module_name')
        msg = ('expected \'' + id_name + '\' to be defined as a float in \'' +
               card_name + '\', module \'' + module_name + '\'.')
        semantic_error(msg, lval)
    return rval.get('value')

def must_be_int(lval, rval, card_node, module_node):
    if not env.is_integer(rval):
        name = lval.get('name')
        card_name = card_node.get('card_name')
        module_name = module_node.get('module_name')
        msg = ('expected \'' + name + '\' to be defined as an integer in \'' +
               card_name + '\', module \'' + module_name + '\'.')
        semantic_error(msg, lval)
    return rval.get('value')

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
    # A unit number must be in [0,99], or [-99,-1] for binary.
    # Or possible 0 (zero) which denotes no unit.
    if ((value not in range(0, 100)) and
        (value not in range(-99, 0))):
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

def string_must_not_exceed_length(lval, rval, max_length, card_node, module_node):
    # Make sure it's a string before continuing.
    string = must_be_string(lval, rval, card_node, module_node)
    if len(card_node.get('statement_list')) > max_length:
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
