from nifty.environment import helpers as env

def sort_statement_list(ordered_id_names, card):
    # 'ordered_id_names' specifies in which order the identifiers should be
    # ordered in 'card'.
    statement_list = env.get_statement_list(card)
    new_statement_list = list()
    for id_name in ordered_id_names:
        node = env.get_identifier(id_name, card)
        if env.not_defined(node):
            # XXX Insert default value.
            pass
        else:
            new_statement_list.append(node)
    # If the new list differs from the original, return the original such that
    # the analyzer can report any semantical errors to the user.
    if len(new_statement_list) != len(statement_list):
        return statement_list
    else:
        return new_statement_list