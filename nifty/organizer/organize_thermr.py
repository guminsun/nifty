from nifty.environment.exceptions import OrganizeError
from nifty.environment.exceptions import organize_error
from nifty.environment.exceptions import SemanticError

from nifty.environment import helpers as env

import organizer_helpers as helper

from nifty.settings import settings
from nifty.settings import thermr_settings

##############################################################################
# Organize thermr. Put together into an orderly, functional, structured whole.

def organize_thermr(module):
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
    return helper.organize_card(thermr_settings.card_1_order_map, card)

def organize_card_2(card, module):
    return helper.organize_card(thermr_settings.card_2_order_map, card)

def organize_card_3(card, module):
    card_2 = env.get_card('card_2', module)
    order_map = thermr_settings.card_2_order_map
    ntemp = env.get_identifier_value('ntemp', order_map, card_2)
    if ntemp is None:
        organize_error()
    order_map = {}
    identifier_map = thermr_settings.card_3_identifier_map
    for i in range(ntemp):
        order_map[i] = ('tempr', i, identifier_map.get('tempr'))
    return helper.organize_card(order_map, card)

def organize_card_4(card, module):
    return helper.organize_card(thermr_settings.card_4_order_map, card)
