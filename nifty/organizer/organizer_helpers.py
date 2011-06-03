import sys

from nifty.environment.exceptions import OrganizeError
from nifty.environment.exceptions import organize_error
from nifty.environment.exceptions import SemanticError

from nifty.analyzer import analyzer_rules as rule

from nifty.environment import helpers as env
from nifty.environment import syntax_tree as ast

from nifty.settings import settings

##############################################################################
# Organizer helpers.

def organize_card(order_map, card_node):
    statement_list = card_node.get('statement_list')
    # Try to organize the card's statement list. Restore the original card
    # node if an OrganizeError or SemanticError is raised.
    try:
        statement_list = organize_statement_list(order_map, statement_list)
    except OrganizeError:
        return card_node
    # Semantic errors are catched since e.g. get_identifier_name/1 is used
    # when sorting the cards statement lists.
    except SemanticError:
        return card_node
    card_node['statement_list'] = statement_list
    return card_node

def organize_statement_list(order_map, statement_list):
    # A new statement list is created and the expected nodes are inserted into
    # the new list in their expected order as indicated by order_map.
    new_statement_list = list(None for i in range(len(order_map)))
    for statement in statement_list:
        l_value, r_value = must_be_assignment(statement)
        name = l_value.get('name')
        internal_name = env.get_internal_name(name, order_map)
        # Identifier node must be defined only once in the statement list,
        # note that identifier_must_be_unique/2 ignores array nodes.
        identifier_must_be_unique(internal_name, order_map, statement_list)
        # Note that 'array_index' is None if the l-value isn't an array node.
        array_index = env.get_array_index(l_value)
        # The identifier must be one of the expected ones.
        if is_expected_name(internal_name, array_index, order_map):
            # If the identifier is an expected one, insert it on the expected
            # index in the new statement list.
            index = get_expected_index(internal_name, array_index, order_map)
            new_statement_list[index] = statement
        else:
            organize_error()
    # Trim new_statement_list by removing trailing None's.
    new_statement_list = trim_statement_list(new_statement_list)
    # Replace possible None's with default values. Error is raised if no
    # default value is available (e.g. identifier must be defined).
    new_statement_list = insert_default_values(order_map, new_statement_list)
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

def insert_default_values(order_map, statement_list):
    # Number of None's to replace.
    n = statement_list.count(None)
    for e in range(n):
        index = statement_list.index(None)
        statement_list[index] = make_node(order_map.get(index))
    return statement_list

def insert_default_card(index, card_name, card_list):
    if index is None:
        return card_list
    card = ast.make_card(None, card_name, list())
    card_list.insert(index, card)
    return card_list

def get_expected_index(name, index, order_map):
    for k in order_map:
        if (name == settings.expected_name(order_map.get(k)) and
            index == settings.expected_array_index(order_map.get(k))):
            return k
    return None

def next_card_list_index(previous_card_node, card_list):
    try:
        index = card_list.index(previous_card_node) + 1
    except ValueError:
        index = None
    return index

##############################################################################
# Organizer Rules.

def identifier_must_be_unique(internal_name, order_map, statement_list):
    count = 0
    for statement in statement_list:
        l_value, r_value = must_be_assignment(statement)
        if env.is_identifier(l_value):
            name = l_value.get('name')
            if internal_name == env.get_internal_name(name, order_map):
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

def must_be_optional(order_tuple):
    identifier = settings.expected_identifier(order_tuple)
    if identifier.get('is_optional'):
        return order_tuple
    else:
        organize_error()

##############################################################################
# Boolean Helpers.

def is_expected_card(expected_card_name, card_node):
    if card_node is None:
        return False
    return expected_card_name == card_node.get('card_name')

def is_expected_name(name, index, order_map):
    if index is None:
        return is_expected_identifier(name, order_map)
    else:
        return is_expected_array(name, index, order_map)

def is_expected_array(name, index, order_map):
    for k in order_map:
        if (name == settings.expected_name(order_map.get(k)) and
            index == settings.expected_array_index(order_map.get(k))):
            return True
    return False

def is_expected_identifier(name, order_map):
    for k in order_map:
        if name == settings.expected_name(order_map.get(k)):
            return True
    return False

##############################################################################
# Node Constructor Helpers.

def make_node(order_tuple):
    must_be_optional(order_tuple)
    name = settings.expected_name(order_tuple)
    if settings.is_array(order_tuple):
        array_index = settings.expected_array_index(order_tuple)
        l_value = ast.make_array(None, name, array_index)
    elif settings.is_identifier(order_tuple):
        l_value = ast.make_identifier(None, name)
    else:
        raise TypeError('unknown order tuple', order_tuple)
    value = settings.expected_identifier(order_tuple).get('value')
    r_value = make_value(value)
    return ast.make_assignment(None, '=', l_value, r_value)

def make_value(value_map):
    default_value = value_map.get('default_value')
    if env.is_float(value_map) or isinstance(default_value, float):
        return ast.make_float(None, default_value)
    elif env.is_integer(value_map) or isinstance(default_value, int):
        return ast.make_integer(None, default_value)
    elif env.is_null(value_map):
        return ast.make_null(None, default_value)
    elif env.is_string(value_map) or isinstance(default_value, str):
        return ast.make_string(None, default_value)
    else:
        raise TypeError('unknown value type', value_map)
