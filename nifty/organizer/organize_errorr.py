from nifty.environment.exceptions import OrganizeError
from nifty.environment.exceptions import organize_error
from nifty.environment.exceptions import SemanticError

from nifty.environment import helpers as env

import organizer_helpers as helper

from nifty.settings import errorr_settings

##############################################################################
# Organize errorr. Put together into an orderly, functional, structured whole.

def organize_errorr(module):
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
        'card_8a' : organize_card_8a,
        'card_8b' : organize_card_8b,
        'card_9' : organize_card_9,
        'card_10' : organize_card_10,
        'card_11' : organize_card_11,
        'card_12a' : organize_card_12a,
        'card_12b' : organize_card_12b,
        'card_13a' : organize_card_13a,
        'card_13b' : organize_card_13b,
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
    return helper.organize_card(errorr_settings.card_1_order_map, card)

def organize_card_2(card, module):
    return helper.organize_card(errorr_settings.card_2_order_map, card)

def organize_card_3(card, module):
    return helper.organize_card(errorr_settings.card_3_order_map, card)

def organize_card_4(card, module):
    # No need to organize card 4 since it only contains one identifier.
    return card

def organize_card_5(card, module):
    # XXX: Need to verify with NJOY source code. Documentation fuzzy.
    return card

def organize_card_6(card, module):
    # XXX: Need to verify with NJOY source code. Documentation fuzzy.
    return card

def organize_card_7(card, module):
    return helper.organize_card(errorr_settings.card_7_order_map, card)

def organize_card_8(card, module):
    return helper.organize_card(errorr_settings.card_8_order_map, card)

def organize_card_8a(card, module):
    card_8 = env.get_card('card_8', module)
    order_map = errorr_settings.card_8_order_map
    nmt = env.get_identifier_value('nmt', order_map, card_8)
    if nmt is None:
        organize_error()
    order_map = {}
    identifier_map = errorr_settings.card_8a_identifier_map
    for i in range(nmt):
        order_map[i] = ('mts', i, identifier_map.get('mts'))
    return helper.organize_card(order_map, card)

def organize_card_8b(card, module):
    card_8 = env.get_card('card_8', module)
    order_map = errorr_settings.card_8_order_map
    nek = env.get_identifier_value('nek', order_map, card_8)
    if nek is None:
        organize_error()
    order_map = {}
    identifier_map = errorr_settings.card_8b_identifier_map
    for i in range(nek+1):
        order_map[i] = ('ek', i, identifier_map.get('ek'))
    return helper.organize_card(order_map, card)

def organize_card_9(card, module):
    # XXX: Need to verify with NJOY source code. Documentation fuzzy.
    return card

def organize_card_10(card, module):
    # XXX: Need to verify with NJOY source code. Documentation fuzzy.
    return card

def organize_card_11(card, module):
    # XXX: Need to verify with NJOY source code. Documentation fuzzy.
    return card

def organize_card_12a(card, module):
    # No need to organize card 12a since it only contains one identifier.
    return card

def organize_card_12b(card, module):
    card_12a = env.get_card('card_12a', module)
    order_map = errorr_settings.card_12a_order_map
    ngn = env.get_identifier_value('ngn', order_map, card_12a)
    if ngn is None:
        organize_error()
    order_map = {}
    identifier_map = errorr_settings.card_12b_identifier_map
    for i in range(ngn+1):
        order_map[i] = ('egn', i, identifier_map.get('egn'))
    return helper.organize_card(order_map, card)

def organize_card_13a(card, module):
    # Length of TAB1 record is user defined, retrieve it so that it is
    # possible to sort the statement list.
    wght_length = len(card.get('statement_list'))
    order_map = {}
    identifier_map = errorr_settings.card_13a_identifier_map
    for i in range(wght_length):
        order_map[i] = ('wght', i, identifier_map.get('wght'))
    return helper.organize_card(order_map, card)

def organize_card_13b(card, module):
    return helper.organize_card(errorr_settings.card_13b_identifier_map, card)
