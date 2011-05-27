from nifty.environment.exceptions import OrganizeError
from nifty.environment.exceptions import organize_error
from nifty.environment.exceptions import SemanticError
import organizer_helpers as helper

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
    expected_map = {
        0 : ('identifier', ('nendf', None)),
        1 : ('identifier', ('npend', None)),
    }
    return helper.organize_card(expected_map, card)

def organize_card_2(card, module):
    # No need to organize card 2 since it only contains one identifier.
    return card

def organize_card_3(card, module):
    expected_map = {
        0 : ('identifier', ('mat', None)),
        1 : ('identifier', ('ncards', 0)),
        1 : ('identifier', ('ngrid', 0)),
    }
    return helper.organize_card(expected_map, card)

def organize_card_4(card, module):
    err = helper.get_identifier_value('err', card)
    if err is None:
        organize_error()
    expected_map = {
        0 : ('identifier', ('err', None)),
        1 : ('identifier', ('tempr', 0)),
        2 : ('identifier', ('errmax', 10*float(err))),
        3 : ('identifier', ('errint', float(err)/20000)),
    }
    return helper.organize_card(expected_map, card)

def organize_card_5(card, module):
    # No need to organize card 5 since it only contains one identifier.
    return card

def organize_card_6(card, module):
    # No need to organize card 6 since it only contains one identifier.
    return card
