from nifty.environment import helpers as env
from nifty.environment.exceptions import OrganizeError
from nifty.environment.exceptions import organize_error
from nifty.environment.exceptions import SemanticError
import organizer_helpers as helper

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
    expected_map = {
        0 : ('identifier', ('nendf', None)),
        1 : ('identifier', ('npend', None)),
        2 : ('identifier', ('ngout', 0)),
        3 : ('identifier', ('nout', 0)),
        4 : ('identifier', ('nin', 0)),
        5 : ('identifier', ('nstan', 0)),
    }
    return helper.organize_card(expected_map, card)

def organize_card_2(card, module):
    expected_map = {
        0 : ('identifier', ('matd', None)),
        1 : ('identifier', ('ign', 1)),
        2 : ('identifier', ('iwt', 6)),
        3 : ('identifier', ('iprint', 1)),
        4 : ('identifier', ('irelco', 1)),
    }
    return helper.organize_card(expected_map, card)

def organize_card_3(card, module):
    pass

def organize_card_4(card, module):
    pass

def organize_card_5(card, module):
    pass

def organize_card_6(card, module):
    pass

def organize_card_7(card, module):
    pass

def organize_card_8(card, module):
    pass

def organize_card_8a(card, module):
    pass

def organize_card_8b(card, module):
    pass

def organize_card_9(card, module):
    pass

def organize_card_10(card, module):
    pass

def organize_card_11(card, module):
    pass

def organize_card_12a(card, module):
    pass

def organize_card_12b(card, module):
    pass

def organize_card_13a(card, module):
    pass

def organize_card_13b(card, module):
    pass
