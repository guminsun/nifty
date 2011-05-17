import sys

from nifty.analyzer import analyzer_rules as rule
from nifty.environment import helpers as env
import organizer_helpers as helper

##############################################################################
# Organize acer. Put together into an orderly, functional, structured whole.

def organize_acer(module):
    card_list = module.get('card_list')
    card_list = organize_card_list(module)
    return module

def organize_card_list(module):
    card_iter = env.get_card_iterator(module)
    # Card 1 should always be defined.
    organize_card_1(env.next(card_iter), module)
    # Card 2 should always be defined.
    # Extract the identifiers iopt and nxtra from card 2 since they are used
    # to determine which cards that should be defined.
    card_2, iopt, nxtra = organize_card_2(env.next(card_iter), module)
    # Card 3 should always be defined.
    organize_card_3(env.next(card_iter), module)
    # Card 4 should only be defined if nxtra > 0 in card_2.
    if nxtra > 0:
        organize_card_4(nxtra, env.next(card_iter), module)
    ## Card 5, 6 and 7 should only be defined if iopt = 1 in card_2.
    #if iopt == 1:
    #    analyze_acer_card_5(env.next(card_iter), module)
    #    analyze_acer_card_6(env.next(card_iter), module)
    #    analyze_acer_card_7(env.next(card_iter), module)
    ## Card 8, 8a and 9 should only be defined if iopt = 2 in card_2.
    #if iopt == 2:
    #    analyze_acer_card_8(env.next(card_iter), module)
    #    analyze_acer_card_8a(env.next(card_iter), module)
    #    analyze_acer_card_9(env.next(card_iter), module)
    ## Card 10 should only be defined if iopt = 3 in card_2.
    #if iopt == 3:
    #    analyze_acer_card_10(env.next(card_iter), module)
    ## Card 11 should only be defined if iopt = 4 or 5 in card_2.
    #if iopt == 4 or iopt == 5:
    #    analyze_acer_card_11(env.next(card_iter), module)
    ## No more cards are allowed. The next card returned by env.next(card_iter)
    ## should be 'None'.
    #rule.no_card_allowed(env.next(card_iter), module)
    return module

def organize_card_1(card, module):
    # Card 1 must be defined. OrganizeError is raised if 'card' is not card 1
    # (the original syntax tree will be returned).
    helper.card_must_be_defined('card_1', card)
    expected = {
        0 : ('singleton', 'identifier', ('nendf', None)),
        1 : ('singleton', 'identifier', ('npend', None)),
        2 : ('singleton', 'identifier', ('ngend', None)),
        3 : ('singleton', 'identifier', ('nace', None)),
        4 : ('singleton', 'identifier', ('ndir', None)),
    }
    statement_list = card.get('statement_list')
    card['statement_list'] = helper.sort_statement_list(expected, statement_list)
    return card

def organize_card_2(card, module):
    helper.card_must_be_defined('card_2', card)
    expected = {
        0 : ('singleton', 'identifier', ('iopt', None)),
        1 : ('singleton', 'identifier', ('iprint', 1)),
        2 : ('singleton', 'identifier', ('ntype', 1)),
        3 : ('singleton', 'identifier', ('suff', 0.00)),
        4 : ('singleton', 'identifier', ('nxtra', 0)),
    }
    statement_list = card.get('statement_list')
    statement_list = helper.sort_statement_list(expected, statement_list)
    card['statement_list'] = statement_list
    # The statement iterator is used to get the iopt and nxtra values which
    # are used in organize_card_list/1 to determine which cards that are
    # supposed to be defined.
    stmt_iter = env.get_statement_iterator(card)
    # First element in 'statement_list' is assumed to be the iopt node after
    # sorting. 
    iopt = get_iopt(env.next(stmt_iter), card, module)
    # Fifth element in 'statement_list' is assumed to be the nxtra node after
    # sorting.
    env.skip(3, stmt_iter)
    nxtra = get_nxtra(env.next(stmt_iter), card, module)
    return card, iopt, nxtra

def get_iopt(node, card, module):
    # Expecting a singleton value.
    l_value, r_value = rule.analyze_singleton(node, card, module)
    # The l-value of the assignment is expected to be an identifier; iopt
    rule.identifier_must_be_defined('iopt', l_value, card, module)
    # The r-value of the assignment is expected to be an integer.
    iopt = rule.must_be_int(l_value, r_value, card, module)
    return iopt

def get_nxtra(node, card, module):
    # nxtra does not have to be defined, defaults to 0.
    if node is None:
        return 0
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        # The l-value of the assignment is expected to be an identifier.
        rule.identifier_must_be_defined('nxtra', l_value, card, module)
        # The r-value of the assignment is expected to be an integer.
        nxtra = rule.must_be_int(l_value, r_value, card, module)
        return nxtra

def organize_card_3(card, module):
    # No need to organize card 3; it only contains one variable which has no
    # default value. Card 3 must be defined though. If card 3 is not defined
    # then there's no need to organize the rest of the program
    helper.card_must_be_defined('card_3', card)
    return card

def organize_card_4(nxtra, card, module):
    helper.card_must_be_defined('card_4', card)
    expected = {}
    for i in range(nxtra):
        expected[i] = ('pair', 'array', (('iz', None, i), ('aw', None, i)))
    statement_list = card.get('statement_list')
    statement_list = helper.sort_statement_list(expected, statement_list)
    card['statement_list'] = statement_list
    return card

def organize_card_5(card, module):
    #default_values = [('tempd', None, 300)]
    #card = helper.organize_default_values(default_values, card)
    #ordered_id_names = [('matd', None), ('tempd', None)]
    #return helper.organize_statement_list(ordered_id_names, card)
    pass

def organize_card_6(card, module):
    #default_values = [('newfor', None, 1), ('iopp', None, 1)]
    #card = helper.organize_default_values(default_values, card)
    #ordered_id_names = [('newfor', None), ('iopp', None)]
    #return helper.organize_statement_list(ordered_id_names, card)
    pass

def organize_card_7(card, module):
    # XXX: Treat as an array? What about default values?
    #ordered_id_names = [('thin01', None), ('thin02', None), ('thin03', None)]
    #return helper.organize_statement_list(ordered_id_names, card)
    pass

def organize_card_8(card, module):
    #default_values = [('tempd', None, 300), ('tname', None, 'za')]
    #card = helper.organize_default_values(default_values, card)
    #ordered_id_names = [('matd', None), ('tempd', None), ('tname', None)]
    #return helper.organize_statement_list(ordered_id_names, card)
    pass

def organize_card_8a(card, module):
    # XXX: Treat as an array?
    #default_values = [('iza02', None, 0), ('iza03', None, 0)]
    #card = helper.organize_default_values(default_values, card)
    #ordered_id_names = [('iza01', None), ('iza02', None), ('iza03', None)]
    #return helper.organize_statement_list(ordered_id_names, card)
    pass

def organize_card_9(card, module):
    #default_values = [('nmix', None, 1), ('emax', None, 1000.0),
    #                  ('iwt', None, 1)]
    #card = helper.organize_default_values(default_values, card)
    #ordered_id_names = [('mti', None), ('nbint', None), ('mte', None),
    #                    ('ielas', None), ('nmix', None), ('emax', None),
    #                    ('iwt', None)]
    #return helper.organize_statement_list(ordered_id_names, card)
    pass

def organize_card_10(card, module):
    #default_values = [('tempd', None, 300)]
    #card = helper.organize_default_values(default_values, card)
    #ordered_id_names = [('matd', None), ('tempd', None)]
    #return helper.organize_statement_list(ordered_id_names, card)
    pass

def organize_card_11(card, module):
    # No need to organize card 11; it only contains one variable which has no
    # default value.
    pass
