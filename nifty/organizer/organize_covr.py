from nifty.environment import helpers as env
from nifty.environment.exceptions import OrganizeError
from nifty.environment.exceptions import organize_error
from nifty.environment.exceptions import SemanticError
import organizer_helpers as helper

##############################################################################
# Organize covr. Put together into an orderly, functional, structured whole.

def organize_covr(module):
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
        'card_2a' : organize_card_2a,
        'card_3a' : organize_card_3a,
        'card_2b' : organize_card_2b,
        'card_3b' : organize_card_3b,
        'card_3c' : organize_card_3c,
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
    expected_map = {
        0 : ('identifier', ('nin', None)),
        1 : ('identifier', ('nout', 0)),
        2 : ('identifier', ('nplot', 0)),
    }
    return helper.organize_card(expected_map, card)

def organize_card_2(card, module):
    expected_map = {
        0 : ('identifier', ('icolor', 0)),
    }
    return helper.organize_card(expected_map, card)

def organize_card_2a(card, module):
    expected_map = {
        0 : ('identifier', ('epmin', 0.0)),
    }
    return helper.organize_card(expected_map, card)

def organize_card_3a(card, module):
    expected_map = {
        0 : ('identifier', ('irelco', 1)),
        1 : ('identifier', ('ncase', 1)),
        2 : ('identifier', ('noleg', 0)),
        3 : ('identifier', ('nstart', 1)),
        4 : ('identifier', ('ndiv', 1)),
    }
    return helper.organize_card(expected_map, card)

def organize_card_2b(card, module):
    expected_map = {
        0 : ('identifier', ('matype', 3)),
        1 : ('identifier', ('ncase', 1)),
    }
    return helper.organize_card(expected_map, card)

def organize_card_3b(card, module):
    # No need to organize card 3b since it only contains one value which has
    # no default value.
    return card

def organize_card_3c(card, module):
    # No need to organize card 3c since it only contains one value which has
    # no default value.
    return card

def organize_card_4(card, module):
    expected_map = {
        0 : ('identifier', ('mat', None)),
        1 : ('identifier', ('mt', 0)),
        2 : ('identifier', ('mat1', 0)),
        3 : ('identifier', ('mt1', 0)),
    }
    return helper.organize_card(expected_map, card)
