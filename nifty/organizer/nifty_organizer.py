import sys

##############################################################################
# Organizer. To put together into an orderly, functional, structured whole.

def organize(ast):
    return ast

##############################################################################
# Helpers.

def sort_card_lists(program):
    module_list = program['module_list']
    for module in module_list:
        sort_card_list(module['card_list'])
    return program

def sort_card_list(card_list):
    # XXX: Ugly assumption that the card nodes will be sorted on 'card_id'.
    return card_list.sort()

def make_card(id_digit, id_alpha):
    card = dict()
    card['node_type'] = 'card'
    card['line_number'] = None
    card['card_id'] = (id_digit, id_alpha)
    card['card_name'] = 'card_' + str(id_digit) + id_alpha
    card['statement_list'] = list()
    return card

def insert_card(card, card_list):
    index = 0
    for c in card_list:
        if c['card_id'] < card['card_id']:
            index += 1
        else:
            break
    card_list.insert(index, card)
    return card_list
