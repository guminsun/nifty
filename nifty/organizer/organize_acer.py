import sys

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
        'card_3' : organize_card_3,
        'card_4' : organize_card_4,
        'card_5' : organize_card_5,
        'card_6' : organize_card_6,
        'card_7' : organize_card_7,
        'card_8' : organize_card_8,
        'card_8a' : organize_card_8a,
        'card_9' : organize_card_9,
        'card_10' : organize_card_10,
        'card_11' : organize_card_11,
    }
    card_name = env.get_card_name(card)
    try:
        organizer_function = card_functions[card_name]
    except KeyError:
        msg = ('--- organize_acer: card not implemented yet: ' + card_name)
        print msg
        sys.exit('organizer_error')
    return organizer_function(card)

def card_dummy(card):
    return card

def organize_card_1(card):
    ordered_id_names = ['nendf', 'npend', 'ngend', 'nace', 'ndir']
    return helper.organize_statement_list(ordered_id_names, card)

def organize_card_2(card):
    default_values = [('iprint', 1), ('ntype', 1), ('suff', 0.00),
                      ('nxtra', 0)]
    card = helper.organize_default_values(default_values, card)
    ordered_id_names = ['iopt', 'iprint', 'ntype', 'suff', 'nxtra']
    return helper.organize_statement_list(ordered_id_names, card)

def organize_card_3(card):
    # No need to organize card 3; it only contains one variable which has no
    # default value.
    pass

def organize_card_4(card):
    # XXX: TODO.
    # 'nxtra' (variable in card 2) pairs of 'iz' and 'aw'. Not sure how these
    # variables are supposed to be defined yet. Need to find a good example.
    # Pass for now (see TODO).
    # Special case for sorting these arrays?
    pass

def organize_card_5(card):
    default_values = [('tempd', 300)]
    card = helper.organize_default_values(default_values, card)
    ordered_id_names = ['matd', 'tempd']
    return helper.organize_statement_list(ordered_id_names, card)

def organize_card_6(card):
    default_values = [('newfor', 1), ('iopp', 1)]
    card = helper.organize_default_values(default_values, card)
    ordered_id_names = ['newfor', 'iopp']
    return helper.organize_statement_list(ordered_id_names, card)

def organize_card_7(card):
    # XXX: Treat as an array?
    ordered_id_names = ['thin01', 'thin02', 'thin03']
    return helper.organize_statement_list(ordered_id_names, card)

def organize_card_8(card):
    default_values = [('tempd', 300), ('tname', 'za')]
    card = helper.organize_default_values(default_values, card)
    ordered_id_names = ['matd', 'tempd', 'tname']
    return helper.organize_statement_list(ordered_id_names, card)

def organize_card_8a(card):
    # XXX: Treat as an array?
    default_values = [('iza02', 0), ('iza03', 0)]
    card = helper.organize_default_values(default_values, card)
    ordered_id_names = ['iza01', 'iza02', 'iza03']
    return helper.organize_statement_list(ordered_id_names, card)

def organize_card_9(card):
    default_values = [('nmix', 1), ('emax', 1000.0), ('iwt', 1)]
    card = helper.organize_default_values(default_values, card)
    ordered_id_names = ['mti', 'nbint', 'mte', 'ielas', 'nmix', 'emax', 'iwt']
    return helper.organize_statement_list(ordered_id_names, card)

def organize_card_10(card):
    default_values = [('tempd', 300)]
    card = helper.organize_default_values(default_values, card)
    ordered_id_names = ['matd', 'tempd',]
    return helper.organize_statement_list(ordered_id_names, card)

def organize_card_11(card):
    # No need to organize card 11; it only contains one variable which has no
    # default value.
    pass
