from nifty.environment import helpers as env
from nifty.environment.exceptions import OrganizeError
from nifty.environment.exceptions import organize_error
from nifty.environment.exceptions import SemanticError
import organizer_helpers as helper

##############################################################################
# Organize purr. Put together into an orderly, functional, structured whole.

def organize_purr(module):
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
        0 : ('identifier', ('matd', None)),
        1 : ('identifier', ('ntemp', None)),
        2 : ('identifier', ('nsigz', None)),
        3 : ('identifier', ('nbin', None)),
        4 : ('identifier', ('nladr', None)),
        5 : ('identifier', ('iprint', 1)),
        6 : ('identifier', ('nunx', 0)),
    }
    return helper.organize_card(expected_map, card)

def organize_card_3(card, module):
    card_2 = env.get_card('card_2', module)
    ntemp = helper.get_identifier_value('ntemp', card_2)
    if ntemp is None:
        organize_error()
    expected_map = {}
    for i in range(ntemp):
        expected_map[i] = ('array', ('ntemp', None, i))
    return helper.organize_card(expected_map, card)

def organize_card_4(card, module):
    card_2 = env.get_card('card_2', module)
    nsigz = helper.get_identifier_value('nsigz', card_2)
    if nsigz is None:
        organize_error()
    expected_map = {}
    for i in range(nsigz):
        expected_map[i] = ('array', ('sigz', None, i))
    return helper.organize_card(expected_map, card)
