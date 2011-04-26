import sys

from nifty.environment import helpers as env
import organizer_helpers as helper

##############################################################################
# Organize acer. Put together into an orderly, functional, structured whole.

def organize_acer(module):
    card_list = env.get_card_list(module)
    card_list = organize_acer_card_list(card_list, module)
    return module

def organize_acer_card_list(card_list, module):
    for card in card_list:
        card = organize_card(card, module)
    return card_list

def organize_card(card, module):
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
    return organizer_function(card, module)

def card_dummy(card, module):
    return card

def organize_card_1(card, module):
    ordered_id_names = [('nendf', None), ('npend', None), ('ngend', None), 
                        ('nace', None), ('ndir', None)]
    return helper.organize_statement_list(ordered_id_names, card)

def organize_card_2(card, module):
    default_values = [('iprint', None, 1), ('ntype', None, 1), 
                      ('suff', None, 0.00), ('nxtra', None, 0)]
    card = helper.organize_default_values(default_values, card)
    ordered_id_names = ['iopt', 'iprint', 'ntype', 'suff', 'nxtra']
    return helper.organize_statement_list(ordered_id_names, card)

def organize_card_3(card, module):
    # No need to organize card 3; it only contains one variable which has no
    # default value.
    pass

def organize_card_4(card, module):
    card_2 = env.get_card('card_2', module)
    # If card 2 is not defined, then neither is 'nxtra'. Return the original
    # card such that the analyzer can detect and report any semantical errors. 
    if env.not_defined(card_2):
        return card
    nxtra_node = env.get_identifier('nxtra', card_2)
    # If nxtra isn't defined in card_2, return the original card such that the
    # analyzer can detect and report any semantical errors. 
    if env.not_defined(nxtra_node):
        return card
    nxtra_value = env.get_value(env.get_r_value(nxtra_node))
    # Construct iz,aw pairs as an ordered list to feed organize_statement_list
    ordered_id_names = list()
    for i in range(nxtra_value):
        ordered_id_names.append(('iz', i))
        ordered_id_names.append(('aw', i))
    return helper.organize_statement_list(ordered_id_names, card)

def organize_card_5(card, module):
    default_values = [('tempd', None, 300)]
    card = helper.organize_default_values(default_values, card)
    ordered_id_names = [('matd', None), ('tempd', None)]
    return helper.organize_statement_list(ordered_id_names, card)

def organize_card_6(card, module):
    default_values = [('newfor', None, 1), ('iopp', None, 1)]
    card = helper.organize_default_values(default_values, card)
    ordered_id_names = [('newfor', None), ('iopp', None)]
    return helper.organize_statement_list(ordered_id_names, card)

def organize_card_7(card, module):
    # XXX: Treat as an array? What about default values?
    ordered_id_names = [('thin01', None), ('thin02', None), ('thin03', None)]
    return helper.organize_statement_list(ordered_id_names, card)

def organize_card_8(card, module):
    default_values = [('tempd', None, 300), ('tname', None, 'za')]
    card = helper.organize_default_values(default_values, card)
    ordered_id_names = [('matd', None), ('tempd', None), ('tname', None)]
    return helper.organize_statement_list(ordered_id_names, card)

def organize_card_8a(card, module):
    # XXX: Treat as an array?
    default_values = [('iza02', None, 0), ('iza03', None, 0)]
    card = helper.organize_default_values(default_values, card)
    ordered_id_names = [('iza01', None), ('iza02', None), ('iza03', None)]
    return helper.organize_statement_list(ordered_id_names, card)

def organize_card_9(card, module):
    default_values = [('nmix', None, 1), ('emax', None, 1000.0), 
                      ('iwt', None, 1)]
    card = helper.organize_default_values(default_values, card)
    ordered_id_names = [('mti', None), ('nbint', None), ('mte', None),
                        ('ielas', None), ('nmix', None), ('emax', None),
                        ('iwt', None)]
    return helper.organize_statement_list(ordered_id_names, card)

def organize_card_10(card, module):
    default_values = [('tempd', None, 300)]
    card = helper.organize_default_values(default_values, card)
    ordered_id_names = [('matd', None), ('tempd', None)]
    return helper.organize_statement_list(ordered_id_names, card)

def organize_card_11(card, module):
    # No need to organize card 11; it only contains one variable which has no
    # default value.
    pass
