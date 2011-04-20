from nifty.environment import helpers as helper

##############################################################################
# Organize acer. Put together into an orderly, functional, structured whole.

def organize_acer(module):
    card_list = helper.get_card_list(module)
    organize_acer_card_list(card_list, module)
    return module

def organize_acer_card_list(card_list, module):
    for card in card_list:
        organize_card(card)
    return card_list

def organize_card(card):
    organizer_function = organizer_function_dummy
    card_functions = {
        'card_1' : organize_card_1,
    }
    card_name = helper.get_card_name(card)
    try:
        organizer_function = card_functions[card_name]
    except KeyError:
        msg = ('--- organize_acer: XXX not implemented yet: ' + card_name)
        print msg
    organizer_function(card)
    return card

def organizer_function_dummy(card):
    pass

def organize_card_1(card):
    pass
