import sys

from nifty.analyzer import analyzer_rules as rule

from nifty.environment import helpers as env
from nifty.environment import syntax_tree as ast

from nifty.environment.exceptions import OrganizeError
from nifty.environment.exceptions import organize_error
from nifty.environment.exceptions import SemanticError

##############################################################################
# Organizer helpers.

def organize_card(expected_map, card_node):
    statement_list = card_node.get('statement_list')
    # Try to organize the card's statement list. Restore the original card
    # node if an OrganizeError or SemanticError is raised.
    try:
        statement_list = organize_statement_list(expected_map, statement_list)
    except OrganizeError:
        return card_node
    # Semantic errors are catched since e.g. get_identifier_name/1 is used
    # when sorting the cards statement lists.
    except SemanticError:
        return card_node
    card_node['statement_list'] = statement_list
    return card_node

def organize_statement_list(expected, statement_list):
    new_statement_list = list(None for i in range(len(expected)))
    for statement in statement_list:
        must_be_assignment(statement)
        l_value = statement.get('l_value')
        # The l-value must hold a valid identifier name.
        id_name = env.get_identifier_name(l_value)
        internal_id_name = env.get_internal_identifier_name(id_name)
        # Identifier node must be defined only once in the statement list,
        # note that identifier_must_be_unique/2 ignores array nodes.
        identifier_must_be_unique(internal_id_name, statement_list)
        # Note that 'array_index' is None if the l-value isn't an array node.
        array_index = env.get_array_index(l_value)
        # The identifier must be one of the expected ones.
        if is_expected_name(internal_id_name, array_index, expected):
            # If the identifier is an expected one, insert it on the expected
            # index in the new statement list.
            index = get_expected_index(internal_id_name, array_index, expected)
            new_statement_list[index] = statement
        else:
            organize_error()
    # Trim 'new_statement_list' by removing trailing None's.
    new_statement_list = trim_statement_list(new_statement_list)
    # Replace possible None's with default values. Error is raised if no
    # default value is available (e.g. identifier must be defined).
    new_statement_list = insert_default_values(expected, new_statement_list)
    return new_statement_list

def trim_statement_list(statement_list):
    try:
        # Pop trailing None's from non-empty statement lists.
        while statement_list[-1] is None:
            statement_list.pop(-1)
    except IndexError:
        # Return empty statement lists.
        return statement_list
    return statement_list

def insert_default_values(expected_map, statement_list):
    # Number of None's to replace.
    n = statement_list.count(None)
    for e in range(n):
        index = statement_list.index(None)
        statement_list[index] = make_node(expected_map[index])
    return statement_list

def insert_default_card(index, card_name, card_list):
    if index is None:
        return card_list
    card = ast.make_card(None, card_name, list())
    card_list.insert(index, card)
    return card_list

def get_identifier_value(id_name, card_node):
    if card_node is None:
        organize_error()
    statement_list = card_node.get('statement_list')
    for statement in statement_list:
        must_be_assignment(statement)
        id_node = statement.get('l_value')
        name = env.get_identifier_name(id_node)
        internal_name = env.get_internal_identifier_name(name)
        if internal_name == id_name:
            return statement.get('r_value').get('value')
    return None

def next_card_list_index(previous_card_node, card_list):
    try:
        index = card_list.index(previous_card_node) + 1
    except ValueError:
        index = None
    return index

def get_value(node):
    if node is None:
        return None
    l_value, r_value = must_be_assignment(node)
    return r_value.get('value')

def get_optional_value(default_value, node):
    if node is None:
        return default_value
    l_value, r_value = must_be_assignment(node)
    return r_value.get('value')

##############################################################################
# Organizer Rules.

def identifier_must_be_unique(internal_id_name, statement_list):
    count = 0
    for statement in statement_list:
        must_be_assignment(statement)
        l_value = statement.get('l_value')
        if env.is_identifier(l_value):
            id_name = env.get_identifier_name(l_value)
            if internal_id_name == env.get_internal_identifier_name(id_name):
                count += 1
    if count <= 1:
        return count
    else:
        organize_error()

def must_be_assignment(node):
    if env.is_assignment(node):
        return node.get('l_value'), node.get('r_value')
    else:
        organize_error()

def must_be_card(node):
    if env.is_card(node):
        return node
    else:
        organize_error()

##############################################################################
# Boolean Helpers.

def is_expected_card(expected_card_name, card_node):
    if card_node is None:
        return False
    return expected_card_name == card_node.get('card_name')

def is_expected_name(name, index, expected_map):
    if index is None:
        return is_expected_identifier(name, expected_map)
    else:
        return is_expected_array(name, index, expected_map)

def is_expected_array(name, index, expected_map):
    for k in expected_map:
        node_type = get_expected_node(k, expected_map)
        if (node_type == 'array' and
            name == get_expected_name(k, expected_map) and
            index == get_expected_array_index(k, expected_map)):
            return True
    return False

def is_expected_identifier(name, expected_map):
    for k in expected_map:
        node_type = get_expected_node(k, expected_map)
        if (node_type == 'identifier' and
            name == get_expected_name(k, expected_map)):
            return True
    return False

##############################################################################
# Expected Map Helpers.

def get_expected_array_index(k, expected_map):
    node_type = get_expected_node(k, expected_map)
    if node_type == 'array':
        return expected_map[k][1][2]
    return None

def get_expected_index(name, array_index, expected_map):
    for k in expected_map:
        if (name == get_expected_name(k, expected_map) and
            array_index == get_expected_array_index(k, expected_map)):
            return k
    return None

def get_expected_name(k, expected_map):
    return expected_map[k][1][0]

def get_expected_node(k, expected_map):
    return expected_map[k][0]

##############################################################################
# Node Constructor Helpers.

def make_node(e):
    node_type = e[0]
    name = e[1][0]
    if node_type == 'array':
        array_index = e[1][2]
        l_value = ast.make_array(None, name, array_index)
    elif node_type == 'identifier':
        l_value = ast.make_identifier(None, name)
    else:
        raise TypeError('unknown node type', node_type)
    value = e[1][1]
    r_value = make_value(value)
    return ast.make_assignment(None, '=', l_value, r_value)

def make_value(value):
    # XXX: Consider adding which type of value it is to the expected map
    # instead of making this isinstance/2 check?
    if isinstance(value, float):
        return ast.make_float(None, value)
    elif isinstance(value, int):
        return ast.make_integer(None, value)
    elif isinstance(value, str):
        return ast.make_string(None, value)
    elif value is None:
        # No default value, i.e. the identifier must be defined.
        organize_error()
    else:
        raise TypeError('unknown value type', value)
