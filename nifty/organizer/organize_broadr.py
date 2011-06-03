from nifty.environment.exceptions import OrganizeError
from nifty.environment.exceptions import organize_error
from nifty.environment.exceptions import SemanticError

from nifty.environment import helpers as env

import organizer_helpers as helper

from nifty.settings import settings
from nifty.settings import broadr_settings

##############################################################################
# Organize broadr. Put together into an orderly, functional, structured whole.

def organize_broadr(module):
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
    return helper.organize_card(broadr_settings.card_1_order_map, card)

def organize_card_2(card, module):
    return helper.organize_card(broadr_settings.card_2_order_map, card)

def organize_card_3(card, module):
    order_map = broadr_settings.card_3_order_map
    errthn = env.get_identifier_value('errthn', order_map, card)
    if errthn is None:
        organize_error()
    # XXX: Ugly.
    for k in order_map:
        if settings.expected_name(order_map.get(k)) == 'errmax':
            order_map[k][2]['value']['default_value'] = 10.0 * float(errthn)
        if settings.expected_name(order_map.get(k)) == 'errint':
            order_map[k][2]['value']['default_value'] = float(errthn) / 20000.0
    return helper.organize_card(order_map, card)

def organize_card_4(card, module):
    card_2 = env.get_card('card_2', module)
    card_2_order_map = broadr_settings.card_2_order_map
    ntemp2 = env.get_identifier_value('ntemp2', card_2_order_map, card_2)
    if ntemp2 is None:
        organize_error()
    identifier_map = broadr_settings.card_4_identifier_map
    order_map = {}
    for i in range(ntemp2):
        order_map[i] = ('temp2', i, identifier_map.get('temp2'))
    return helper.organize_card(order_map, card)

def organize_card_5(card, module):
    # No need to organize card 5 since it only contains one identifier.
    return card
