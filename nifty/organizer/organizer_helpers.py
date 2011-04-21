from nifty.environment import helpers as env

##############################################################################
# Organizer helpers.

def sort_statement_list(ordered_id_names, card):
    '''
        Return a statement list where all identifiers in 'card's statement
        list has been sorted according to the order of the corresponding
        identifier names in 'ordered_id_names'.

        Use this function to sort statement lists where all identifiers must
        be provided.

        For example, if ordered_id_names = ['one', 'two'] and
        card['statement_list'] = ['two', 'one'] then
        statement_list = ['one', 'two'] will be returned.

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
        return statement_list
    new_statement_list = list()
    for id_name in ordered_id_names:
        node = env.get_identifier(id_name, card)
        if env.not_defined(node):
            # All identifiers must be defined. Return the original statement
            # list such that the analyzer can report any semantical errors.
            return statement_list
        else:
            new_statement_list.append(node)
    return new_statement_list
