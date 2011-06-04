from nifty.environment.exceptions import OrganizeError
from nifty.environment.exceptions import organize_error
from nifty.environment.exceptions import SemanticError

from nifty.environment import helpers as env

import organizer_helpers as helper

from nifty.settings import gaminr_settings

##############################################################################
# Organize gaminr. Put together into an orderly, functional, structured whole.

def organize_gaminr(module):
    card_list = module.get('card_list')
    organize_card_list(card_list, module)
    return module

def organize_card_list(card_list, module):
    for card in card_list:
        card = organize_card(card, module)
    return card_list

def organize_card(card, module):
    function_map = {
        'card_1' : organize_card_1,
        'card_2' : organize_card_2,
        'card_3' : organize_card_3,
        'card_4' : organize_card_4,
        'card_5' : organize_card_5,
        'card_6' : organize_card_6,
        'card_7' : organize_card_7,
    }
    card_name = card.get('card_name')
    card_function = function_map.get(card_name, card_dummy)
    try:
        card = card_function(card, module)
    except OrganizeError:
        pass
    except SemanticError:
        pass
    return card

def card_dummy(card):
    return card

def organize_card_1(card, module):
    return helper.organize_card(gaminr_settings.card_1_order_map, card)

def organize_card_2(card, module):
    return helper.organize_card(gaminr_settings.card_2_order_map, card)

def organize_card_3(card, module):
    # No need to organize card 3 since it only contains one identifier.
    return card

def organize_card_4(card, module):
    order_map = gaminr_settings.card_4_order_map
    ngg = env.get_identifier_value('ngg', order_map, card)
    if ngg is None:
        organize_error()
    identifier_map = gaminr_settings.card_4_identifier_map
    # Start at index 1, and iterate to ngg+2, since ngg is defined at index 0.
    for i in range(1, ngg+2):
        order_map[i] = ('egg', i, identifier_map.get('egg'))
    return helper.organize_card(order_map, card)

def organize_card_5(card, module):
    # Length of TAB1 record is user defined, retrieve it so that it is
    # possible to sort the statement list.
    wght_length = len(card.get('statement_list'))
    order_map = {}
    identifier_map = gaminr_settings.card_5_identifier_map
    for i in range(wght_length):
        order_map[i] = ('wght', i, identifier_map.get('wght'))
    return helper.organize_card(order_map, card)

def organize_card_6(card, module):
    return helper.organize_card(gaminr_settings.card_6_order_map, card)

def organize_card_7(card, module):
    # No need to organize card 7 since it only contains one identifier.
    return card
