from nifty.environment.exceptions import OrganizeError
from nifty.environment.exceptions import SemanticError

from nifty.environment import helpers as env

import organizer_helpers as helper

from nifty.settings import moder_settings

##############################################################################
# Organize moder. Put together into an orderly, functional, structured whole.

def organize_moder(module):
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
    return helper.organize_card(moder_settings.card_1_order_map, card)

def organize_card_2(card, module):
    # No need to organize card 2 since it only contains one identifier.
    return card

def organize_card_3(card, module):
    return helper.organize_card(moder_settings.card_3_order_map, card)
