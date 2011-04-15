##############################################################################
# Boolean helpers.

def is_assignment(expr):
    '''
        Return True if 'expr' is an assignment node, else False.
    '''
    return expr['node_type'] == '='

def not_defined(node):
    '''Return True if 'node' is None, else False.'''
    return node is None

##############################################################################
# Getter helpers.

def get_card(card_name, module_node):
    '''
        Return card node of 'card_name' if 'card_name' is in "module_node"'s
        card list, else None.
    '''
    card_list = module_node['card_list']
    for c in card_list:
        if c['card_name'] == card_name:
            return c
    return None

def get_cards(card_name, module_node):
    '''
        Return a list of card nodes with card name 'card_name' if 'card_name'
        is in 'card_list'.
    '''
    cards = list()
    card_list = module_node['card_list']
    for c in card_list:
        if c['card_name'] == card_name:
            cards.append(c)
    return cards

def get_identifier(id_name, card_node):
    '''
        Return identifier node of 'id_name' if 'id_name' is defined in 
        "card_node"'s statement list, else None.
    '''
    statement_list = card_node['statement_list']
    for expression in statement_list:
        if is_assignment(expression) and expression['identifier'] == id_name:
            return expression
    return None

def get_r_value(assignment):
    '''
        Return the r_value node of the 'assignment' node.
    '''
    return assignment['r_value']

def get_value(r_value):
    '''
        Return the value of the 'r_value' node.
    '''
    return r_value['value']
