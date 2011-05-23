from nifty.environment import helpers as env
from nifty.environment.exceptions import OrganizeError
from nifty.environment.exceptions import SemanticError
import organizer_helpers as helper

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
    expected_map = {
        0 : ('identifier', ('nendf', None)),
        1 : ('identifier', ('npend', None)),
        2 : ('identifier', ('ngout1', 0)),
        3 : ('identifier', ('ngout2', 0)),
    }
    return helper.organize_card(expected_map, card)

def organize_card_2(card, module):
    expected_map = {
        0 : ('identifier', ('matb', None)),
        1 : ('identifier', ('ign', None)),
        2 : ('identifier', ('igg', None)),
        3 : ('identifier', ('iwt', None)),
        4 : ('identifier', ('lord', None)),
        5 : ('identifier', ('ntemp', None)),
        6 : ('identifier', ('nsigz', None)),
        7 : ('identifier', ('iprint', 1)),
    }
    return helper.organize_card(expected_map, card)

def organize_card_3(card, module):
    expected_map = {
        0 : ('identifier', ('title', '')),
    }
    return helper.organize_card(expected_map, card)

def organize_card_4(card, module):
    card_2 = env.get_card('card_2', module)
    ntemp = helper.get_identifier_value('ntemp', card_2)
    expected_map = {}
    for i in range(ntemp):
        expected_map[i] = ('array', ('temp', None, i))
    return helper.organize_card(expected_map, card)

def organize_card_5(card, module):
    pass

def organize_card_6a(card, module):
    pass

def organize_card_6b(card, module):
    pass

def organize_card_7a(card, module):
    pass

def organize_card_7b(card, module):
    pass

def organize_card_8a(card, module):
    pass

def organize_card_8b(card, module):
    pass

def organize_card_8c(card, module):
    pass

def organize_card_8d(card, module):
    pass

def organize_card_9(card, module):
    pass

def organize_card_10(card, module):
    pass
