from nifty.environment.exceptions import OrganizeError
from nifty.environment.exceptions import SemanticError

from nifty.environment import helpers as env

import organizer_helpers as helper

from nifty.settings import matxsr_settings

##############################################################################
# Organize matxsr. Put together into an orderly, functional, structured whole.

def organize_matxsr(module):
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
        'card_8' : organize_card_8,
        'card_9' : organize_card_9,
        'card_10' : organize_card_10,
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
    return helper.organize_card(matxsr_settings.card_1_order_map, card)

def organize_card_2(card, module):
    return helper.organize_card(matxsr_settings.card_2_order_map, card)

def organize_card_3(card, module):
    return helper.organize_card(matxsr_settings.card_3_order_map, card)

def organize_card_4(card, module):
    # No need to organize card 4 since it only contains one identifier.
    return card

def organize_card_5(card, module):
    card_3 = env.get_card('card_3', module)
    order_map = matxsr_settings.card_3_order_map
    npart = env.get_identifier_value('npart', order_map, card_3)
    if npart is None:
        organize_error()
    identifier_map = matxsr_settings.card_5_identifier_map
    order_map = {}
    for i in range(npart):
        order_map[i] = ('hpart', i, identifier_map.get('hpart'))
    return helper.organize_card(order_map, card)

def organize_card_6(card, module):
    # No need to organize card 6 since it only contains one identifier.
    return card

def organize_card_7(card, module):
    card_3 = env.get_card('card_3', module)
    order_map = matxsr_settings.card_3_order_map
    ntype = env.get_identifier_value('ntype', order_map, card_3)
    if ntype is None:
        organize_error()
    identifier_map = matxsr_settings.card_7_identifier_map
    order_map = {}
    for i in range(ntype):
        order_map[i] = ('htype', i, identifier_map.get('htype'))
    return helper.organize_card(order_map, card)

def organize_card_8(card, module):
    card_3 = env.get_card('card_3', module)
    order_map = matxsr_settings.card_3_order_map
    ntype = env.get_identifier_value('ntype', order_map, card_3)
    if ntype is None:
        organize_error()
    identifier_map = matxsr_settings.card_8_identifier_map
    order_map = {}
    for i in range(ntype):
        order_map[i] = ('jinp', i, identifier_map.get('jinp'))
    return helper.organize_card(order_map, card)

def organize_card_9(card, module):
    card_3 = env.get_card('card_3', module)
    order_map = matxsr_settings.card_3_order_map
    ntype = env.get_identifier_value('ntype', order_map, card_3)
    if ntype is None:
        organize_error()
    identifier_map = matxsr_settings.card_9_identifier_map
    order_map = {}
    for i in range(ntype):
        order_map[i] = ('joutp', i, identifier_map.get('joutp'))
    return helper.organize_card(order_map, card)

def organize_card_10(card, module):
    return helper.organize_card(matxsr_settings.card_10_order_map, card)
