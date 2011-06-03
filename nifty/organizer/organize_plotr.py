from nifty.environment.exceptions import OrganizeError
from nifty.environment.exceptions import SemanticError

from nifty.environment import helpers as env

import organizer_helpers as helper

from nifty.settings import settings
from nifty.settings import plotr_settings

##############################################################################
# Organize plotr. Put together into an orderly, functional, structured whole.

def organize_plotr(module):
    card_list = module.get('card_list')
    organize_card_list(card_list, module)
    return module

def organize_card_list(card_list, module):
    for card in card_list:
        card = organize_card(card, module)
    return card_list

def organize_card(card, module):
    function_map = {
        'card_0' : organize_card_0,
        'card_1' : organize_card_1,
        'card_2' : organize_card_2,
        'card_3' : organize_card_3,
        'card_3a' : organize_card_3a,
        'card_4' : organize_card_4,
        'card_5' : organize_card_5,
        'card_5a' : organize_card_5a,
        'card_6' : organize_card_6,
        'card_6a' : organize_card_6a,
        'card_7' : organize_card_7,
        'card_7a' : organize_card_7a,
        'card_8' : organize_card_8,
        'card_9' : organize_card_9,
        'card_10' : organize_card_10,
        'card_10a' : organize_card_10a,
        'card_11' : organize_card_11,
        'card_12' : organize_card_12,
        'card_13' : organize_card_13,
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

def organize_card_0(card, module):
    return helper.organize_card(plotr_settings.card_0_order_map, card)

def organize_card_1(card, module):
    return helper.organize_card(plotr_settings.card_1_order_map, card)

def organize_card_2(card, module):
    # Default values for ww and wh depends on the page orientation (lori),
    # defined in card 1.
    #
    # According to the NJOY source code: default paper size is US letter size,
    # default page size is paper size with 0.5 inches margins all around.
    #
    # If page orientation is portrait (lori = 0) then the page size is
    # 7.5 x 10 inches, else if the page orientation is landscape (lori = 1)
    # then the page size is 10 x 7.5 inches.
    # Rotation angle, 'wr', defaults to 0.
    card_1 = env.get_card('card_1', module)
    order_map = plotr_settings.card_1_order_map
    lori = env.get_identifier_value('lori', order_map, card_1)
    if lori == 0:
        ww = 7.5
        wh = 10.0
    else:
        ww = 10.0
        wh = 7.5
    order_map = plotr_settings.card_2_order_map
    # XXX: Ugly.
    for k in order_map:
        if settings.expected_name(order_map.get(k)) == 'ww':
            order_map[k][2]['value']['default_value'] = ww
        if settings.expected_name(order_map.get(k)) == 'wh':
            order_map[k][2]['value']['default_value'] = wh
    return helper.organize_card(order_map, card)

def organize_card_3(card, module):
    return helper.organize_card(plotr_settings.card_3_order_map, card)

def organize_card_3a(card, module):
    return helper.organize_card(plotr_settings.card_3a_order_map, card)

def organize_card_4(card, module):
    return helper.organize_card(plotr_settings.card_4_order_map, card)

def organize_card_5(card, module):
    # 'el' and 'eh' are either both defined, or both undefined. 'xstep' is
    # optional. Hence, only organize when there are statements to organize.
    if len(card.get('statement_list')) > 0:
        return helper.organize_card(plotr_settings.card_5_order_map, card)
    else:
        return card

def organize_card_5a(card, module):
    return helper.organize_card(plotr_settings.card_5a_order_map, card)

def organize_card_6(card, module):
    # 'yl' and 'yh' are either both defined, or both undefined. 'ystep' is
    # optional. Hence, only organize when there are statements to organize.
    if len(card.get('statement_list')) > 0:
        return helper.organize_card(plotr_settings.card_6_order_map, card)
    else:
        return card

def organize_card_6a(card, module):
    return helper.organize_card(plotr_settings.card_6a_order_map, card)

def organize_card_7(card, module):
    # 'rbot' and 'rtop' are either both defined, or both undefined. 'rstep' is
    # optional. Hence, only organize when there are statements to organize.
    if len(card.get('statement_list')) > 0:
        return helper.organize_card(plotr_settings.card_7_order_map, card)
    else:
        return card

def organize_card_7a(card, module):
    return helper.organize_card(plotr_settings.card_7a_order_map, card)

def organize_card_8(card, module):
    order_map = plotr_settings.card_8_order_map
    iverf = env.get_identifier_value('iverf', order_map, card)
    if iverf > 0:
        return helper.organize_card(order_map, card)
    else:
        return card

def organize_card_9(card, module):
    return helper.organize_card(plotr_settings.card_9_order_map, card)

def organize_card_10(card, module):
    return helper.organize_card(plotr_settings.card_10_order_map, card)

def organize_card_10a(card, module):
    return helper.organize_card(plotr_settings.card_10a_order_map, card)

def organize_card_11(card, module):
    return helper.organize_card(plotr_settings.card_11_order_map, card)

def organize_card_12(card, module):
    return helper.organize_card(plotr_settings.card_12_order_map, card)

def organize_card_13(card, module):
    return helper.organize_card(plotr_settings.card_13_order_map, card)
