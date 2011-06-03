from nifty.environment.exceptions import OrganizeError
from nifty.environment.exceptions import organize_error
from nifty.environment.exceptions import SemanticError

from nifty.environment import helpers as env

import organizer_helpers as helper

from nifty.settings import groupr_settings

##############################################################################
# Organize groupr. Put together into an orderly, functional, structured whole.

def organize_groupr(module):
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
        'card_6a' : organize_card_6a,
        'card_6b' : organize_card_6b,
        'card_7a' : organize_card_7a,
        'card_7b' : organize_card_7b,
        'card_8a' : organize_card_8a,
        'card_8b' : organize_card_8b,
        'card_8c' : organize_card_8c,
        'card_8d' : organize_card_8d,
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
    return helper.organize_card(groupr_settings.card_1_order_map, card)

def organize_card_2(card, module):
    return helper.organize_card(groupr_settings.card_2_order_map, card)

def organize_card_3(card, module):
    return helper.organize_card(groupr_settings.card_3_order_map, card)

def organize_card_4(card, module):
    card_2 = env.get_card('card_2', module)
    order_map = groupr_settings.card_2_order_map
    ntemp = env.get_identifier_value('ntemp', order_map, card_2)
    if ntemp is None:
        organize_error()
    order_map = {}
    identifier_map = groupr_settings.card_4_identifier_map
    for i in range(ntemp):
        order_map[i] = ('temp', i, identifier_map.get('temp'))
    return helper.organize_card(order_map, card)

def organize_card_5(card, module):
    card_2 = env.get_card('card_2', module)
    order_map = groupr_settings.card_2_order_map
    nsigz = env.get_identifier_value('nsigz', order_map, card_2)
    if nsigz is None:
        organize_error()
    order_map = {}
    identifier_map = groupr_settings.card_5_identifier_map
    for i in range(nsigz):
        order_map[i] = ('sigz', i, identifier_map.get('sigz'))
    return helper.organize_card(order_map, card)

def organize_card_6a(card, module):
    # No need to organize card 6a since it only contains one identifier.
    return card

def organize_card_6b(card, module):
    card_6a = env.get_card('card_6a', module)
    order_map = groupr_settings.card_6a_order_map
    ngn = env.get_identifier_value('ngn', order_map, card_6a)
    # Ugly? 'ngn' must be defined in order to sort the 'egn' array.
    if ngn is None:
        organize_error()
    order_map = {}
    identifier_map = groupr_settings.card_6b_identifier_map
    for i in range(ngn+1):
        order_map[i] = ('egn', i, identifier_map.get('egn'))
    return helper.organize_card(order_map, card)

def organize_card_7a(card, module):
    # No need to organize card 7a since it only contains one identifier.
    return card

def organize_card_7b(card, module):
    card_7a = env.get_card('card_7a', module)
    order_map = groupr_settings.card_7a_order_map
    ngg = env.get_identifier_value('ngg', order_map, card_7a)
    # Ugly? 'ngg' must be defined in order to sort the 'egg' array.
    if ngg is None:
        organize_error()
    order_map = {}
    identifier_map = groupr_settings.card_7b_identifier_map
    for i in range(ngg+1):
        order_map[i] = ('egg', i, identifier_map.get('egg'))
    return helper.organize_card(order_map, card)

def organize_card_8a(card, module):
    return helper.organize_card(groupr_settings.card_8a_order_map, card)

def organize_card_8b(card, module):
    # Length of TAB1 record is user defined, retrieve it so that it is
    # possible to sort the statement list.
    wght_length = len(card.get('statement_list'))
    order_map = {}
    identifier_map = groupr_settings.card_8b_identifier_map
    for i in range(wght_length):
        order_map[i] = ('wght', i, identifier_map.get('wght'))
    return helper.organize_card(order_map, card)

def organize_card_8c(card, module):
    return helper.organize_card(groupr_settings.card_8c_order_map, card)

def organize_card_8d(card, module):
    # No need to organize card 8d since it only contains one identifier.
    return card

def organize_card_9(card, module):
    return helper.organize_card(groupr_settings.card_9_order_map, card)

def organize_card_10(card, module):
    # No need to organize card 10 since it only contains one identifier.
    return card
