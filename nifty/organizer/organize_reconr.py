from nifty.environment.exceptions import OrganizeError
from nifty.environment.exceptions import organize_error
from nifty.environment.exceptions import SemanticError

from nifty.environment import helpers as env

import organizer_helpers as helper

from nifty.settings import settings
from nifty.settings import reconr_settings

##############################################################################
# Organize reconr. Put together into an orderly, functional, structured whole.

def organize_reconr(module):
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
    return helper.organize_card(reconr_settings.card_1_order_map, card)

def organize_card_2(card, module):
    # No need to organize card 2 since it only contains one identifier.
    return card

def organize_card_3(card, module):
    return helper.organize_card(reconr_settings.card_2_order_map, card)

def organize_card_4(card, module):
    order_map = reconr_settings.card_4_order_map
    err = env.get_identifier_value('err', order_map, card)
    if err is None:
        organize_error()
    # XXX: Ugly.
    errmax = 10.0 * float(err)
    errint = float(err) / 20000.0
    for k in order_map:
        if settings.expected_name(order_map.get(k)) == 'errmax':
            order_map[k][2]['value']['default_value'] = errmax
        if settings.expected_name(order_map.get(k)) == 'errint':
            order_map[k][2]['value']['default_value'] = errint
    return helper.organize_card(order_map, card)

def organize_card_5(card, module):
    # No need to organize card 5 since it only contains one identifier.
    return card

def organize_card_6(card, module):
    # No need to organize card 6 since it only contains one identifier.
    return card
