from nifty.environment import helpers as env
from nifty.environment.exceptions import OrganizeError
from nifty.environment.exceptions import organize_error
from nifty.environment.exceptions import SemanticError
import organizer_helpers as helper

##############################################################################
# Organize thermr. Put together into an orderly, functional, structured whole.

def organize_thermr(module):
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
        1 : ('identifier', ('nin', None)),
        2 : ('identifier', ('nout', None)),
    }
    return helper.organize_card(expected_map, card)

def organize_card_2(card, module):
    expected_map = {
        0 : ('identifier', ('matde', None)),
        1 : ('identifier', ('matdp', None)),
        2 : ('identifier', ('nbin', None)),
        3 : ('identifier', ('ntemp', None)),
        4 : ('identifier', ('iinc', None)),
        5 : ('identifier', ('icoh', None)),
        6 : ('identifier', ('natom', None)),
        7 : ('identifier', ('mtref', None)),
        8 : ('identifier', ('iprint', 0)),
    }
    return helper.organize_card(expected_map, card)

def organize_card_3(card, module):
    card_2 = env.get_card('card_2', module)
    ntemp = helper.get_identifier_value('ntemp', card_2)
    if ntemp is None:
        organize_error()
    expected_map = {}
    for i in range(ntemp):
        expected_map[i] = ('array', ('tempr', None, i))
    return helper.organize_card(expected_map, card)

def organize_card_4(card, module):
    expected_map = {
        0 : ('identifier', ('tol', None)),
        1 : ('identifier', ('emax', None)),
    }
    return helper.organize_card(expected_map, card)
