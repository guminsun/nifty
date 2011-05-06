from nifty.environment import helpers as env

##############################################################################
# Organizer helpers.

def organize_default_values(default_values, card):
    '''
        Return 'card' where the identifiers in default_values (and the
        corresponding values) have been added to the cards statement list if
        they were not already defined.
        If the cards statement list is empty then no default values are
        inserted.

        Use this function to set the default values of identifiers in a cards
        statement list. 
        Don't use this function for cards which are used to terminate
        {temperatures, materials, modules}.

        Make sure to sort the cards statement list with 'sort_statement_list'
        afterwards since this function knows nothing about the order of the
        identifiers.
    '''
    statement_list = env.get_statement_list(card)
    # Don't insert default values for empty cards. This will help keep the
    # output file as uncluttered as possible.
    if len(statement_list) == 0:
        return card
    # Save the original statement list for rollbacks.
    card = env.save_statement_list(statement_list, card)
    # Insert default values if the identifiers haven't been defined.
    for id_index_value in default_values:
        id_name = id_index_value[0]
        id_index = id_index_value[1]
        id_value = id_index_value[2]
        if id_index is None:
            id_node = env.get_identifier(id_name, card)
        else:
            id_node = env.get_array(id_name, id_index, card)
        if env.not_defined(id_node):
            expr_node = make_assignment(id_name, id_index, id_value)
            statement_list.append(expr_node)
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
        if 'original_statement_list' in card:
            original_statement_list = env.get_original_statement_list(card)
            card = env.set_statement_list(original_statement_list, card)
            del card['original_statement_list']
        return card
    new_statement_list = list()
    for name_index_pair in ordered_id_names:
        id_name = name_index_pair[0]
        id_index = name_index_pair[1]
        if id_index is None:
            node = env.get_identifier(id_name, card)
        else:
            node = env.get_array(id_name, id_index, card)
        if env.not_defined(node):
            # All identifiers must be defined. Return the original statement
            # list such that the analyzer can report any semantical errors.
            if 'original_statement_list' in card:
                original_statement_list = env.get_original_statement_list(card)
                card = env.set_statement_list(original_statement_list, card)
                del card['original_statement_list']
            return card
        else:
            new_statement_list.append(node)
    # So far so good, remove original statement list to save space.
    if 'original_statement_list' in card:
        del card['original_statement_list']
    return env.set_statement_list(new_statement_list, card)

##############################################################################
# Constructors for assignment nodes.

def make_assignment(id_name, id_index, id_value):
    node = dict()
    node['line_number'] = None
    node['node_type'] = '='
    node['l_value'] = make_l_value(id_name, id_index)
    node['r_value'] = make_r_value(id_value)
    return node

def make_l_value(id_name, id_index):
    node = dict()
    node['line_number'] = None
    if id_index is None:
        node['node_type'] = 'identifier'
    else:
        node['node_type'] = 'array'
        node['index'] = id_index
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
