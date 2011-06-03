from nifty.environment.exceptions import OrganizeError
from nifty.environment.exceptions import SemanticError

from nifty.environment import helpers as env

import organizer_helpers as helper

from nifty.settings import heatr_settings

##############################################################################
# Organize heatr. Put together into an orderly, functional, structured whole.

def organize_heatr(module):
    card_list = module.get('card_list')
    organize_card_list(card_list, module)
    return module

# Use this approach since there's no idea to use the detailed approach (as
# seen in the organizer for module acer) when all cards needs to be defined
# (cannot be defaulted).
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
        'card_5a' : organize_card_5a,
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
    return helper.organize_card(heatr_settings.card_1_order_map, card)

def organize_card_2(card, module):
    return helper.organize_card(heatr_settings.card_2_order_map, card)

def organize_card_3(card, module):
    card_2 = env.get_card('card_2', module)
    order_map = heatr_settings.card_2_order_map
    npk = env.get_identifier_value('npk', order_map, card_2)
    order_map = {}
    identifier_map = heatr_settings.card_3_identifier_map
    for i in range(npk):
        order_map[i] = ('mtk', i, identifier_map.get('mtk'))
    return helper.organize_card(order_map, card)

def organize_card_4(card, module):
    card_2 = env.get_card('card_2', module)
    order_map = heatr_settings.card_2_order_map
    nqa = env.get_identifier_value('nqa', order_map, card_2)
    order_map = {}
    identifier_map = heatr_settings.card_4_identifier_map
    for i in range(nqa):
        order_map[i] = ('mta', i, identifier_map.get('mta'))
    return helper.organize_card(order_map, card)

def organize_card_5(card, module):
    card_2 = env.get_card('card_2', module)
    order_map = heatr_settings.card_2_order_map
    nqa = env.get_identifier_value('nqa', order_map, card_2)
    order_map = {}
    identifier_map = heatr_settings.card_5_identifier_map
    for i in range(nqa):
        order_map[i] = ('qa', i, identifier_map.get('qa'))
    return helper.organize_card(order_map, card)

def organize_card_5a(card, module):
    # Variable qbar; ENDF TAB1 record.
    stmt_len = len(card.get('statement_list'))
    order_map = {}
    identifier_map = heatr_settings.card_5a_identifier_map
    for i in range(stmt_len):
        order_map[i] = ('qbar', i, identifier_map.get('qbar'))
    return helper.organize_card(order_map, card)
