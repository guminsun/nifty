import sys

from nifty.environment.exceptions import semantic_error
from nifty.environment import helpers as env

##############################################################################
# Common identifiers are analyzed exactly the same.

def analyze_identifier_matd(node, card, module):
    # XXX: material must not be 0? 0 usually denotes termination of material
    # or module.
    identifier_must_be_defined(('matd', None), node, card, module)
    return env.get_value(env.get_r_value(node))

def analyze_identifier_nendf(node, card, module):
    identifier_must_be_defined(('nendf', None), node, card, module)
    identifier_must_be_int(node)
    identifier_must_be_unit_number(node)
    return env.get_value(env.get_r_value(node))

def analyze_identifier_npend(node, card, module):
    identifier_must_be_defined(('npend', None), node, card, module)
    identifier_must_be_int(node)
    identifier_must_be_unit_number(node)
    return env.get_value(env.get_r_value(node))

def analyze_identifier_tempd(node, card, module):
    # Temperature does not have to be defined. Defaults to 300.
    if env.not_defined(node):
        return 300
    else:
        # If 'node' is defined, make sure it's a tempd node.
        identifier_must_be_defined(('tempd', None), node, card, module)
    return env.get_value(env.get_r_value(node))

##############################################################################
# Semantic rules.

def card_must_be_defined(card_name, node, module_node, explanation):
    '''
        Return 'node' if its name is 'card_name', else report a semantic error
        where 'explanation' has been appended to the error message.
    '''
    if node is None:
        msg = ('card \'' + card_name + '\' not defined in module \'' +
               module_node['module_name'] + '\'.')
        if explanation is not None:
            msg += ' (' + explanation + ')'
        semantic_error(msg, module_node)

    node_name = env.get_card_name(node)
    if not (card_name == node_name):
        msg = ('expected card \'' + card_name + '\' but saw \'' +
               node_name + '\' in module \'' + module_node['module_name'] +
               '\'.')
        if explanation is not None:
            msg += ' (' + explanation + ')'
        semantic_error(msg, node)
    return node

def identifier_must_be_defined(name_index, node, card_node, module_node):
    id_name = name_index[0]
    id_index = name_index[1]

    if node is None:
        msg = ('identifier \'' + id_name + '\' not defined in \'' +
               card_node['card_name'] + '\', module \'' +
               module_node['module_name'] + '\'.')
        semantic_error(msg, card_node)

    l_value_node = env.get_l_value(node)
    l_value_node_type = env.get_node_type(l_value_node)

    # 'index' is an integer if 'l_value_node' is an array, else None.
    index = env.get_array_index(l_value_node)
    if id_index is None:
        node_must_be_identifier(l_value_node, card_node, module_node)
    else:
        node_must_be_array(l_value_node, card_node, module_node)
        if id_index != index:
            msg = ('expected array index ' + str(id_index) + ' for \'' +
                   id_name + '\' but saw ' + str(index) + ' in \'' +
                   card_node['card_name'] + '\', module \'' +
                   module_node['module_name'] + '\'.')
            semantic_error(msg, l_value_node)

    name = env.get_identifier_name(l_value_node)
    if not env.is_valid_name(name, id_name):
        msg = ('expected identifier \'' + id_name + '\' but saw \'' +
               name + '\' in \'' + card_node['card_name'] +
               '\', module \'' + module_node['module_name'] + '.')
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
    # A unit number must be in [20,99], or [-99,-20] for binary.
    # Or possible 0 (zero) which denotes no unit.
    if ((value not in range(20, 100)) and
        (value not in range(-99, -19)) and
        (value != 0)):
        id_name = env.get_identifier_name(env.get_l_value(node))
        msg = ('\'' + id_name + '\' illegal unit number (' + str(value) + ').')
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

def no_card_allowed(card_node, module_node):
    if not env.not_defined(card_node):
        card_name = env.get_card_name(card_node)
        module_name = env.get_module_name(module_node)
        msg = ('unexpected card: \'' + card_name + '\', no more cards was ' +
               'expected in module \'' + module_name + '\'.')
        semantic_error(msg, card_node)

def no_statement_allowed(node, card_node, module_node):
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

def node_must_be_array(l_value_node, card_node, module_node):
    if env.is_array(l_value_node):
        return l_value_node
    else:
        name = env.get_identifier_name(l_value_node)
        node_type = env.get_node_type(l_value_node)
        msg = ('identifier \'' + name + '\' defined as an ' + node_type +
               ' in \'' + card_node['card_name'] + '\', module \'' +
               module_node['module_name'] + '\'. Expected an array ' +
               'identifier declaration.')
        semantic_error(msg, l_value_node)

def node_must_be_identifier(l_value_node, card_node, module_node):
    if env.is_identifier(l_value_node):
        return l_value_node
    else:
        name = env.get_identifier_name(l_value_node)
        node_type = env.get_node_type(l_value_node)
        msg = ('identifier \'' + name + '\' defined as an ' + node_type +
               ' in \'' + card_node['card_name'] + '\', module \'' +
               module_node['module_name'] + '\'. Expected a regular ' +
               'identifier declaration.')
        semantic_error(msg, l_value_node)

def node_must_be_pair(l_value_node, card_node, module_node):
    if env.is_pair(l_value_node):
        return l_value_node
    else:
        node_type = env.get_node_type(l_value_node)
        msg = ('expected a pair declaration but saw ' + node_type +
               ' declaration, in \'' + card_node['card_name'] +
               '\' module \'' + module_node['module_name'] + '\'.')
        semantic_error(msg, l_value_node)

def pair_must_be_defined(pair, node, card_node, module_node):
    # XXX: Ugh. Ugly. Needs cleaning.
    element_1_name = pair[0][0]
    element_2_name = pair[1][0]
    element_1_index = pair[0][1]
    element_2_index = pair[1][1]
    pair_name = element_1_name + ',' + element_2_name

    if node is None:
        msg = ('pair \'' + pair_name + '\' not defined in \'' +
               card_node['card_name'] + '\', module \'' +
               module_node['module_name'] + '\'.')
        semantic_error(msg, card_node)

    l_value_node = env.get_l_value(node)
    node_must_be_pair(l_value_node, card_node, module_node)

    element_1_node = l_value_node['element_1']
    element_2_node = l_value_node['element_2']

    # 'first_index' is an integer if 'l_value_node' is an array, else None.
    first_index = env.get_array_index(element_1_node)
    if element_1_index is None:
        node_must_be_identifier(element_1_node, card_node, module_node)
    else:
        node_must_be_array(element_1_node, card_node, module_node)
        if element_1_index != first_index:
            msg = ('expected array index ' + str(element_1_index) + ' for \'' +
                   element_1_name + '\' but saw ' + str(first_index) + ' in \'' +
                   card_node['card_name'] + '\', module \'' +
                   module_node['module_name'] + '\'.')
            semantic_error(msg, element_1_node)

    # 'second_index' is an integer if 'l_value_node' is an array, else None.
    second_index = env.get_array_index(element_2_node)
    if element_2_index is None:
        node_must_be_identifier(element_2_node, card_node, module_node)
    else:
        node_must_be_array(element_2_node, card_node, module_node)
        if element_2_index != second_index:
            msg = ('expected array index ' + str(element_2_index) + ' for \'' +
                   element_2_name + '\' but saw ' + str(second_index) + ' in \'' +
                   card_node['card_name'] + '\', module \'' +
                   module_node['module_name'] + '\'.')
            semantic_error(msg, element_2_node)

    # The indicies must match; must be defined as a pair. (This check should
    # not be necessary if the function is called properly.)
    if first_index != second_index:
        msg = ('array index mismatch for \'' + pair_name + '\' pair in \'' +
               card_node['card_name'] + '\', module \'' +
               module_node['module_name'] + '\'. ' +
               'The array indices must be the same for a pair.')
        semantic_error(msg, node)

    # Check that the first elements name is the expected one.
    first_name = env.get_identifier_name(element_1_node)
    if not env.is_valid_name(first_name, element_1_name):
        msg = ('expected first identifier in pair to be \'' + element_1_name + 
               '\' but saw \'' + first_name + '\' in \'' + 
               card_node['card_name'] + '\', module \'' + 
               module_node['module_name'] + '.')
        semantic_error(msg, element_1_node)

    # Check that the second elements name is the expected one.
    second_name = env.get_identifier_name(element_2_node)
    if not env.is_valid_name(second_name, element_2_name):
        msg = ('expected second identifier in pair to be \'' + element_2_name +
               '\' but saw \'' + second_name + '\' in \'' +
               card_node['card_name'] + '\', module \'' +
               module_node['module_name'] + '.')
        semantic_error(msg, element_2_node)
    
    # XXX: Check the type of the nodes? Must not differ?

    return node

def too_few_cards_defined(number_of_cards, expected_number, card_name, module):
    module_name = env.get_module_name(module)
    msg = ('number of \'' + card_name + '\'s is ' + str(number_of_cards) +
           ' in module \'' + module_name + '\'. ' + 'Expected at least ' +
           str(expected_number) + ' \'' + card_name + '\'s.')
    semantic_error(msg, module)
