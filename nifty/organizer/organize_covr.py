from nifty.environment.exceptions import OrganizeError
from nifty.environment.exceptions import organize_error
from nifty.environment.exceptions import SemanticError

from nifty.environment import helpers as env

import organizer_helpers as helper

from nifty.settings import covr_settings

##############################################################################
# Organize covr. Put together into an orderly, functional, structured whole.

def organize_covr(module):
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
        'card_2a' : organize_card_2a,
        'card_3a' : organize_card_3a,
        'card_2b' : organize_card_2b,
        'card_3b' : organize_card_3b,
        'card_3c' : organize_card_3c,
        'card_4' : organize_card_4,
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
    return helper.organize_card(covr_settings.card_1_order_map, card)

def organize_card_2(card, module):
    return helper.organize_card(covr_settings.card_2_order_map, card)

def organize_card_2a(card, module):
    return helper.organize_card(covr_settings.card_2a_order_map, card)

def organize_card_3a(card, module):
    return helper.organize_card(covr_settings.card_3a_order_map, card)

def organize_card_2b(card, module):
    return helper.organize_card(covr_settings.card_2b_order_map, card)

def organize_card_3b(card, module):
    # No need to organize card 3b since it only contains one identifier.
    return card

def organize_card_3c(card, module):
    # No need to organize card 3c since it only contains one identifier.
    return card

def organize_card_4(card, module):
    return helper.organize_card(covr_settings.card_4_order_map, card)
