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

def get_card(card, card_list):
    '''
        Return card node of 'card' if 'card' is in 'card_list', else None.
    '''
    for c in card_list:
        if c['card_name'] == card:
            return c
    return None

def get_cards(card_name, card_list):
    '''
        Return a list of card nodes with card name 'card_name' if 'card_name'
        is in 'card_list'.
    '''
    cards = list()
    for c in card_list:
        if c['card_name'] == card_name:
            cards.append(c)
    return cards

def get_identifier(id, statement_list):
    '''
        Return identifier node of 'id' if 'id' is in 'statement_list',
        else None.
    '''
    for expression in statement_list:
        if is_assignment(expression) and expression['identifier'] == id:
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
