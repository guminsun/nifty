from nifty.environment import ast
from nifty.environment import helpers as env

##############################################################################
# Organizer helpers.

def organize_default_values(default_values, card):
    '''
        Return 'card' where the identifiers in default_values (and the
        corresponding values) have been added to the cards statement list if
        they were not already defined.

        Use this function to set the default values of identifiers in a cards
        statement list.
        Make sure to sort the cards statement list with 'sort_statement_list'
        since this function knows nothing about the order of the identifiers.
    '''
    statement_list = env.get_statement_list(card)
    for id_value_pair in default_values:
        id_name = id_value_pair[0]
        id_value = id_value_pair[1]
        id_node = env.get_identifier(id_name, card)
        if env.not_defined(id_node):
            node = make_assignment(id_name, id_value)
            statement_list.append(node)
    return card

def organize_statement_list(ordered_id_names, card):
    '''
        Return 'card' where the identifiers in the cards statement list is
        sorted. The identifiers are sorted according to the order they appear
        in 'ordered_id_names'.

        Use this function to sort a cards statement list where all identifiers
        have been defined.

        For example, if ordered_id_names = ['one', 'two'] and
        card['statement_list'] = ['two', 'one'] then
        new_statement_list = ['one', 'two'] will be returned.

        If the number of defined identifiers in the card's statement list are
        more than the number of names given in 'ordered_id_names', then the
        original statement list will be returned.

        If any of the names given in 'ordered_id_names' is not defined in the
        card's statement list, then the original statement list will be
        returned.
    '''
    statement_list = env.get_statement_list(card)
    # If the number of expected identifiers is less than the number of defined
    # identifiers, then return the original statement list such that the
    # analyzer can report any semantical errors.
    if len(ordered_id_names) < len(statement_list):
        return card
    new_statement_list = list()
    for id_name in ordered_id_names:
        # XXX: Special case to sort arrays; e.g. variables with multiple
        # values. Handle multiple variables w/o arrays as well?
        node = env.get_identifier(id_name, card)
        if env.not_defined(node):
            # All identifiers must be defined. Return the original statement
            # list such that the analyzer can report any semantical errors.
            return statement_list
        else:
            new_statement_list.append(node)
    return env.set_statement_list(new_statement_list, card)

##############################################################################
# Constructors for assignment nodes.

def make_assignment(id_name, id_value):
    node = dict()
    node['line_number'] = None
    node['node_type'] = '='
    node['l_value'] = make_l_value(id_name)
    node['r_value'] = make_r_value(id_value)
    return node

def make_l_value(id_name):
    node = dict()
    node['line_number'] = None
    # XXX: What about arrays?
    node['node_type'] = 'identifier'
    node['name'] = id_name
    return node

def make_r_value(value):
    if isinstance(value, float):
        return make_float(value)
    elif isinstance(value, int):
        return make_integer(value)
    # XXX: Assume string.
    else:
        return make_string(value)

def make_float(value):
    node = dict()
    node['line_number'] = None
    node['node_type'] = 'float'
    # Floats are encapsulated as strings in the parser - use strings here as
    # well to keep it consistent.
    node['value'] = str(value)
    return node

def make_integer(value):
    node = dict()
    node['line_number'] = None
    node['node_type'] = 'integer'
    node['value'] = value
    return node

def make_string(value):
    node = dict()
    node['line_number'] = None
    node['node_type'] = 'string'
    node['value'] = value
    return node
