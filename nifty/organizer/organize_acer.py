from nifty.analyzer import analyzer_rules as rule
from nifty.environment import helpers as env
import organizer_helpers as helper

##############################################################################
# Organize acer. Put together into an orderly, functional, structured whole.
#
# Compare the organizer implementation for this module with the organizer
# implementation for e.g. the plotr module.
#
# For acer, the organisation process is similar to the semantic analysis in
# the analyzer. It iterates over the card's statement list, inspecting the
# next card, and only organises expected cards. If an unexpected card is seen,
# an exception is raised and the original syntax tree is returned.
# This approach allows more detailed analysis and makes it possible to e.g.
# insert missing cards with default values (e.g. card 6 may be defaulted in
# this module). The drawbacks are that it takes more time to implement and
# that the implementation is not as straightforward as the approach used for
# plotr.

def organize_acer(module):
    card_list = module.get('card_list')
    organize_card_list(card_list, module)
    return module

def organize_card_list(card_list, module):
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
    # Card 5, 6 and 7 should only be defined if iopt = 1 in card_2.
    if iopt == 1:
        c5 = organize_card_5(env.next(card_iter), module)
        # Card 6 may be defaulted. If card 6 is not defined, insert an empty
        # card.
        if env.get_card('card_6', module) is None:
            index = helper.next_card_list_index(c5, card_list)
            helper.insert_default_card(index, 'card_6', card_list)
            c6 = organize_card_6(env.next(card_iter), module)
        else:
            c6 = organize_card_6(env.next(card_iter), module)
        # Likewise, card 7 may be defaulted. If card 6 is not defined, insert
        # an empty card.
        if env.get_card('card_7', module) is None:
            index = helper.next_card_list_index(c6, card_list)
            helper.insert_default_card(index, 'card_7', card_list)
            organize_card_7(env.next(card_iter), module)
        else:
            organize_card_7(env.next(card_iter), module)
    # Card 8, 8a and 9 should only be defined if iopt = 2 in card_2.
    if iopt == 2:
        organize_card_8(env.next(card_iter), module)
        organize_card_8a(env.next(card_iter), module)
        organize_card_9(env.next(card_iter), module)
    # Card 10 should only be defined if iopt = 3 in card_2.
    if iopt == 3:
        organize_card_10(env.next(card_iter), module)
    # Card 11 should only be defined if iopt = 4 or 5 in card_2.
    if iopt == 4 or iopt == 5:
        organize_card_11(env.next(card_iter), module)
    return card_list

def organize_card_1(card, module):
    # If 'card' is not card 1, then return the original card such that e.g.
    # the analyzer is able to report any semantical errors.
    if not helper.is_expected_card('card_1', card):
        return card
    expected_map = {
        0 : ('identifier', ('nendf', None)),
        1 : ('identifier', ('npend', None)),
        2 : ('identifier', ('ngend', None)),
        3 : ('identifier', ('nace', None)),
        4 : ('identifier', ('ndir', None)),
    }
    return helper.organize_card(expected_map, card)

def organize_card_2(card, module):
    if not helper.is_expected_card('card_2', card):
        return card, None, None
    expected_map = {
        0 : ('identifier', ('iopt', None)),
        1 : ('identifier', ('iprint', 1)),
        2 : ('identifier', ('ntype', 1)),
        3 : ('identifier', ('suff', 0.00)),
        4 : ('identifier', ('nxtra', 0)),
    }
    card = helper.organize_card(expected_map, card)
    # The statement iterator is used to get the iopt and nxtra values which
    # are used in organize_card_list/2 to determine which cards that are
    # supposed to be defined.
    stmt_iter = env.get_statement_iterator(card)
    # First element in 'statement_list' is assumed to be the iopt node after
    # sorting.
    iopt = helper.get_value(env.next(stmt_iter))
    # Fifth element in 'statement_list' is assumed to be the nxtra node after
    # sorting.
    env.skip(3, stmt_iter)
    nxtra = helper.get_optional_value(0, env.next(stmt_iter))
    return card, iopt, nxtra

def organize_card_3(card, module):
    # No need to organize card 3; it only contains one variable which has no
    # default value.
    return card

def organize_card_4(nxtra, card, module):
    if not helper.is_expected_card('card_4', card):
        return card
    expected_map = {}
    order = 0
    for i in range(nxtra):
        expected_map[order] = ('array', ('iz', None, i))
        order += 1
        expected_map[order] = ('array', ('aw', None, i))
        order += 1
    return helper.organize_card(expected_map, card)

def organize_card_5(card, module):
    if not helper.is_expected_card('card_5', card):
        return card
    expected_map = {
        0 : ('identifier', ('matd', None)),
        1 : ('identifier', ('tempd', 300)),
    }
    return helper.organize_card(expected_map, card)

def organize_card_6(card, module):
    if not helper.is_expected_card('card_6', card):
        return card
    expected_map = {
        0 : ('identifier', ('newfor', 1)),
        1 : ('identifier', ('iopp', 1)),
    }
    return helper.organize_card(expected_map, card)

def organize_card_7(card, module):
    if not helper.is_expected_card('card_7', card):
        return card
    expected_map = {
        0 : ('identifier', ('thin01', None)),
        1 : ('identifier', ('thin02', None)),
        2 : ('identifier', ('thin03', None)),
    }
    return helper.organize_card(expected_map, card)

def organize_card_8(card, module):
    if not helper.is_expected_card('card_8', card):
        return card
    expected_map = {
        0 : ('identifier', ('matd', None)),
        1 : ('identifier', ('tempd', 300)),
        2 : ('identifier', ('tname', 'za')),
    }
    return helper.organize_card(expected_map, card)

def organize_card_8a(card, module):
    if not helper.is_expected_card('card_8a', card):
        return card
    expected_map = {
        0 : ('identifier', ('iza01', None)),
        1 : ('identifier', ('iza02', 0)),
        2 : ('identifier', ('iza03', 0)),
    }
    return helper.organize_card(expected_map, card)

def organize_card_9(card, module):
    if not helper.is_expected_card('card_9', card):
        return card
    expected_map = {
        0 : ('identifier', ('mti', None)),
        1 : ('identifier', ('nbint', None)),
        2 : ('identifier', ('mte', None)),
        3 : ('identifier', ('ielas', None)),
        4 : ('identifier', ('nmix', 1)),
        5 : ('identifier', ('emax', 1000.0)),
        6 : ('identifier', ('iwt', 1)),
    }
    return helper.organize_card(expected_map, card)

def organize_card_10(card, module):
    if not helper.is_expected_card('card_10', card):
        return card
    expected_map = {
        0 : ('identifier', ('matd', None)),
        1 : ('identifier', ('tempd', 300)),
    }
    return helper.organize_card(expected_map, card)

def organize_card_11(card, module):
    # No need to organize card 11; it only contains one variable which has no
    # default value.
    return card
