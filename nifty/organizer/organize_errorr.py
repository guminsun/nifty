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
    expected_map = {
        0 : ('identifier', ('mprint', None)),
        1 : ('identifier', ('tempin', 300)),
    }
    return helper.organize_card(expected_map, card)

def organize_card_4(card, module):
    # No need to organize card 4 since it only contains one identifier which
    # has no default value.
    pass

def organize_card_5(card, module):
    # XXX: Need to verify with NJOY source code. Documentation fuzzy.
    card_4 = env.get_card('card_4', module)
    nek = helper.get_identifier_value('nek', card_4)
    if nek is None:
        organize_error()
    expected_map = {}
    for i in range(nek+1):
        expected_map[i] = ('array', ('ek', None, i))
    return helper.organize_card(expected_map, card)

def organize_card_6(card, module):
    # XXX: Need to verify with NJOY source code. Documentation fuzzy.
    pass

def organize_card_7(card, module):
    ifissp = helper.get_identifier_value('ifissp', card)
    if ifissp == -1:
        efmean = 2.0
    else:
        efmean = None
    expected_map = {
        0 : ('identifier', ('iread', 0)),
        1 : ('identifier', ('mfcov', 33)),
        2 : ('identifier', ('irespr', 1)),
        3 : ('identifier', ('legord', 1)),
        4 : ('identifier', ('ifissp', -1)),
        5 : ('identifier', ('efmean', efmean)), # XXX: None?
        5 : ('identifier', ('dap', 0)),
    }
    return helper.organize_card(expected_map, card)

def organize_card_8(card, module):
    expected_map = {
        0 : ('identifier', ('nmt', None)),
        1 : ('identifier', ('nek', None)),
    }
    return helper.organize_card(expected_map, card)

def organize_card_8a(card, module):
    card_8 = env.get_card('card_8', module)
    nmt = helper.get_identifier_value('nmt', card_8)
    if nmt is None:
        organize_error()
    expected_map = {}
    for i in range(nmt):
        expected_map[i] = ('array', ('mts', None, i))
    return helper.organize_card(expected_map, card)

def organize_card_8b(card, module):
    card_8 = env.get_card('card_8', module)
    nek = helper.get_identifier_value('nek', card_4)
    if nek is None:
        organize_error()
    expected_map = {}
    for i in range(nek+1):
        expected_map[i] = ('array', ('ek', None, i))
    return helper.organize_card(expected_map, card)

def organize_card_9(card, module):
    # XXX: Need to verify with NJOY source code. Documentation fuzzy.
    pass

def organize_card_10(card, module):
    # XXX: Need to verify with NJOY source code. Documentation fuzzy.
    pass

def organize_card_11(card, module):
    # XXX: Need to verify with NJOY source code. Documentation fuzzy.
    pass

def organize_card_12a(card, module):
    # No need to organize card 12a since it only contains one identifier which
    # has no default value.
    pass

def organize_card_12b(card, module):
    card_12a = env.get_card('card_12a', module)
    ngn = helper.get_identifier_value('ngn', card_12a)
    if ngn is None:
        organize_error()
    expected_map = {}
    for i in range(ngn+1):
        expected_map[i] = ('array', ('egn', None, i))
    return helper.organize_card(expected_map, card)

def organize_card_13a(card, module):
    # Length of TAB1 record is user defined, retrieve it so that it is
    # possible to sort the statement list.
    wght_length = len(card.get('statement_list'))
    expected_map = {}
    # Assuming TAB1 records are defined as NIF arrays.
    for i in range(wght_length):
        expected_map[i] = ('array', ('wght', None, i))
    return helper.organize_card(expected_map, card)

def organize_card_13b(card, module):
    expected_map = {
        0 : ('identifier', ('eb', None)),
        1 : ('identifier', ('tb', None)),
        2 : ('identifier', ('ec', None)),
        3 : ('identifier', ('tc', None)),
    }
    return helper.organize_card(expected_map, card)