from nifty.environment import helpers as env
from nifty.environment.exceptions import OrganizeError
from nifty.environment.exceptions import organize_error
from nifty.environment.exceptions import SemanticError
import organizer_helpers as helper

##############################################################################
# Organize broadr. Put together into an orderly, functional, structured whole.

def organize_broadr(module):
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
        0 : ('identifier', ('mat1', None)),
        1 : ('identifier', ('ntemp2', None)),
        2 : ('identifier', ('istart', 0)),
        3 : ('identifier', ('istrap', 0)),
        4 : ('identifier', ('temp1', 0.0)),
    }
    return helper.organize_card(expected_map, card)

def organize_card_3(card, module):
    errthn = helper.get_identifier_value('errthn', card)
    if errthn is None:
        organize_error()
    expected_map = {
        0 : ('identifier', ('errthn', None)),
        1 : ('identifier', ('thnmax', 1)),
        2 : ('identifier', ('errmax', 10*float(errthn))),
        3 : ('identifier', ('errint', float(errthn)/20000)),
    }
    return helper.organize_card(expected_map, card)

def organize_card_4(card, module):
    card_2 = env.get_card('card_2', module)
    ntemp2 = helper.get_identifier_value('ntemp2', card_2)
    if ntemp2 is None:
        organize_error()
    expected_map = {}
    for i in range(ntemp2):
        expected_map[i] = ('array', ('temp2', None, i))
    return helper.organize_card(expected_map, card)

def organize_card_5(card, module):
    # No need to organize card 5 since it only contains one value which has
    # no default value.
    return card
