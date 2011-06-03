from nifty.analyzer import analyzer_rules as rule
from nifty.environment import helpers as env
import organizer_helpers as helper

from nifty.settings import acer_settings

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
    order_map = acer_settings.card_1_order_map
    return helper.organize_card(order_map, card)

def organize_card_2(card, module):
    if not helper.is_expected_card('card_2', card):
        return card, None, None
    order_map = acer_settings.card_2_order_map
    card = helper.organize_card(order_map, card)
    iopt = env.get_identifier_value('iopt', order_map, card)
    nxtra = env.get_identifier_value('nxtra', order_map, card)
    return card, iopt, nxtra

def organize_card_3(card, module):
    # No need to organize card 3 since it only contains one identifier.
    return card

def organize_card_4(nxtra, card, module):
    if not helper.is_expected_card('card_4', card):
        return card
    order_map = {}
    identifier_map = acer_settings.card_4_identifier_map
    for i in range(nxtra):
        order_map[i*2] = ('iz', i, identifier_map.get('iz'))
        order_map[i*2+1] = ('aw', i, identifier_map.get('aw'))
    return helper.organize_card(order_map, card)

def organize_card_5(card, module):
    if not helper.is_expected_card('card_5', card):
        return card
    return helper.organize_card(acer_settings.card_5_order_map, card)

def organize_card_6(card, module):
    if not helper.is_expected_card('card_6', card):
        return card
    return helper.organize_card(acer_settings.card_6_order_map, card)

def organize_card_7(card, module):
    if not helper.is_expected_card('card_7', card):
        return card
    return helper.organize_card(acer_settings.card_7_order_map, card)

def organize_card_8(card, module):
    if not helper.is_expected_card('card_8', card):
        return card
    return helper.organize_card(acer_settings.card_8_order_map, card)

def organize_card_8a(card, module):
    if not helper.is_expected_card('card_8a', card):
        return card
    return helper.organize_card(acer_settings.card_8a_order_map, card)

def organize_card_9(card, module):
    if not helper.is_expected_card('card_9', card):
        return card
    return helper.organize_card(acer_settings.card_9_order_map, card)

def organize_card_10(card, module):
    if not helper.is_expected_card('card_10', card):
        return card
    return helper.organize_card(acer_settings.card_10_order_map, card)

def organize_card_11(card, module):
    # No need to organize card 11 since it only contains one identifier.
    return card
