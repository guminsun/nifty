from nifty.environment import helpers as env
import organizer_helpers as helper

##############################################################################
# Organize acer. Put together into an orderly, functional, structured whole.

def organize_acer(module):
    card_list = env.get_card_list(module)
    card_list = organize_acer_card_list(card_list)
    return module

def organize_acer_card_list(card_list):
    for card in card_list:
        card = organize_card(card)
    return card_list

def organize_card(card):
    organizer_function = card_dummy
    card_functions = {
        'card_1' : organize_card_1,
        'card_2' : organize_card_2,
    }
    card_name = env.get_card_name(card)
    try:
        organizer_function = card_functions[card_name]
    except KeyError:
        msg = ('$--- organize_acer: XXX not implemented yet: ' + card_name)
        print msg
    return organizer_function(card)

def card_dummy(card):
    return card

def organize_card_1(card):
    ordered_id_names = ['nendf', 'npend', 'ngend', 'nace', 'ndir']
    return helper.sort_statement_list(ordered_id_names, card)

def organize_card_2(card):
    default_values = [('iprint', 1), ('ntype', 1), ('suff', 0.00),
                      ('nxtra', 0)]
    card = helper.insert_default_values(default_values, card)
    ordered_id_names = ['iopt', 'iprint', 'ntype', 'suff', 'nxtra']
    return helper.sort_statement_list(ordered_id_names, card)
