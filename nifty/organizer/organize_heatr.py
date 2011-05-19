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
    pass

def organize_card_2(card, module):
    pass

def organize_card_3(card, module):
    pass

def organize_card_4(card, module):
    pass

def organize_card_5(card, module):
    pass

def organize_card_5a(card, module):
    pass