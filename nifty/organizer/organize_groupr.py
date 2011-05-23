from nifty.environment import helpers as env
from nifty.environment.exceptions import OrganizeError
from nifty.environment.exceptions import organize_error
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
    card_2 = env.get_card('card_2', module)
    nsigz = helper.get_identifier_value('nsigz', card_2)
    expected_map = {}
    for i in range(nsigz):
        expected_map[i] = ('array', ('sigz', None, i))
    return helper.organize_card(expected_map, card)

def organize_card_6a(card, module):
    expected_map = {
        0 : ('identifier', ('ngn', None)),
    }
    return helper.organize_card(expected_map, card)

def organize_card_6b(card, module):
    card_6a = env.get_card('card_6a', module)
    ngn = helper.get_identifier_value('ngn', card_6a)
    # Ugly? 'ngn' must be defined in order to sort the 'egn' array.
    if ngn is None:
        organize_error()
    expected_map = {}
    for i in range(ngn+1):
        expected_map[i] = ('array', ('egn', None, i))
    return helper.organize_card(expected_map, card)

def organize_card_7a(card, module):
    expected_map = {
        0 : ('identifier', ('ngg', None)),
    }
    return helper.organize_card(expected_map, card)

def organize_card_7b(card, module):
    card_7a = env.get_card('card_7a', module)
    ngg = helper.get_identifier_value('ngg', card_7a)
    # Ugly? 'ngg' must be defined in order to sort the 'egg' array.
    if ngg is None:
        organize_error()
    expected_map = {}
    for i in range(ngg+1):
        expected_map[i] = ('array', ('egg', None, i))
    return helper.organize_card(expected_map, card)

def organize_card_8a(card, module):
    expected_map = {
        0 : ('identifier', ('ehi', None)),
        1 : ('identifier', ('sigpot', None)),
        2 : ('identifier', ('nflmax', None)),
        3 : ('identifier', ('ninwt', 0)),
        4 : ('identifier', ('jsigz', 0)),
        5 : ('identifier', ('alpha2', 0)),
        6 : ('identifier', ('sam', 0)),
        7 : ('identifier', ('beta', 0)),
        8 : ('identifier', ('alpha3', 0)),
        9 : ('identifier', ('gamma', 0)),
    }
    return helper.organize_card(expected_map, card)

def organize_card_8b(card, module):
    # Length of TAB1 record is user defined, retrieve it so that it is
    # possible to sort the statement list.
    wght_length = len(card.get('statement_list'))
    expected_map = {}
    # Assuming TAB1 records are defined as NIF arrays.
    for i in range(wght_length):
        expected_map[i] = ('array', ('wght', None, i))
    return helper.organize_card(expected_map, card)

def organize_card_8c(card, module):
    expected_map = {
        0 : ('identifier', ('eb', None)),
        1 : ('identifier', ('tb', None)),
        2 : ('identifier', ('ec', None)),
        3 : ('identifier', ('tc', None)),
    }
    return helper.organize_card(expected_map, card)

def organize_card_8d(card, module):
    pass

def organize_card_9(card, module):
    pass

def organize_card_10(card, module):
    pass
