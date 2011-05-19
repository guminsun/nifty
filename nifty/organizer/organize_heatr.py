from nifty.environment import helpers as env
from nifty.environment.exceptions import OrganizeError
from nifty.environment.exceptions import SemanticError
import organizer_helpers as helper

##############################################################################
# Organize heatr. Put together into an orderly, functional, structured whole.

def organize_heatr(module):
    card_list = module.get('card_list')
    organize_card_list(card_list, module)
    return module

# Use this approach since there's no idea to use the detailed approach (as
# seen in the organizer for module acer) when all cards needs to be defined
# (cannot be defaulted).
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
        'card_5a' : organize_card_5a,
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
        3 : ('identifier', ('nplot', None)),
    }
    return helper.organize_card(expected_map, card)

def organize_card_2(card, module):
    expected_map = {
        0 : ('identifier', ('matd', None)),
        1 : ('identifier', ('npk', 0)),
        2 : ('identifier', ('nqa', 0)),
        3 : ('identifier', ('ntemp', 0)),
        4 : ('identifier', ('local', 0)),
        5 : ('identifier', ('iprint', 0)),
        6 : ('identifier', ('ed', '')), # Default from built-in table in NJOY.
    }
    return helper.organize_card(expected_map, card)

def organize_card_3(card, module):
    card_2 = env.get_card('card_2', module)
    npk = helper.get_identifier_value('npk', card_2)
    # XXX: Ugly default value assignment. Fix with global dictionary for each
    # module card? (with type info, default value info, etc)
    if npk is None:
        npk = 0
    expected_map = {}
    for i in range(npk):
        expected_map[i] = ('array', ('mtk', None, i))
    return helper.organize_card(expected_map, card)

def organize_card_4(card, module):
    card_2 = env.get_card('card_2', module)
    nqa = helper.get_identifier_value('nqa', card_2)
    # XXX: Ugly.
    if nqa is None:
        nqa = 0
    expected_map = {}
    for i in range(nqa):
        expected_map[i] = ('array', ('mta', None, i))
    return helper.organize_card(expected_map, card)

def organize_card_5(card, module):
    card_2 = env.get_card('card_2', module)
    nqa = helper.get_identifier_value('nqa', card_2)
    # XXX: Ugly.
    if nqa is None:
        nqa = 0
    expected_map = {}
    for i in range(nqa):
        expected_map[i] = ('array', ('qa', None, i))
    return helper.organize_card(expected_map, card)

def organize_card_5a(card, module):
    # XXX: Variable qbar; assuming ENDF TAB1 record defined as a NIF array.
    stmt_len = len(card.get('statement_list'))
    expected_map = {}
    for i in range(stmt_len):
        expected_map[i] = ('array', ('qbar', None, i))
    return helper.organize_card(expected_map, card)
