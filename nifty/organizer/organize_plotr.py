import sys

from nifty.analyzer import analyzer_rules as rule
from nifty.environment import helpers as env
import organizer_helpers as helper

##############################################################################
# Organize plotr. Put together into an orderly, functional, structured whole.

def organize_plotr(module):
    card_list = module.get('card_list')
    organize_card_list(card_list, module)
    return module

def organize_card_list(card_list, module):
    card_iter = env.get_card_iterator(module)
    # Card 0 should always be defined.
    c0 = organize_card_0(env.next(card_iter), module)
    # Card 1 may be defaulted. If card 1 is not defined, insert a empty card.
    if env.get_card('card_1', module) is None:
        index = card_list.index(c0) + 1
        helper.insert_default_card(index, 'card_1', card_list)
        c1 = organize_card_1(env.next(card_iter), module)
    else:
        c1 = organize_card_1(env.next(card_iter), module)
    # No more cards are allowed. The next card returned by env.next(card_iter)
    # should be 'None'.
    # XXX: rule.no_card_allowed(env.next(card_iter), module)
    return card_list

def organize_card_0(card, module):
    # Card 0 must be defined. OrganizeError is raised if 'card' is not card 0
    # (the original syntax tree will be returned).
    helper.card_must_be_defined('card_0', card)
    expected_map = {
        0 : ('singleton', 'identifier', ('nplt', None)),
        1 : ('singleton', 'identifier', ('nplt0', 0)),
    }
    return helper.organize_card(expected_map, card)

def organize_card_1(card, module):
    helper.card_must_be_defined('card_1', card)
    expected_map = {
        0 : ('singleton', 'identifier', ('lori', 1)),
        1 : ('singleton', 'identifier', ('istyle', 2)),
        2 : ('singleton', 'identifier', ('size', 0.30)),
        3 : ('singleton', 'identifier', ('ipcol', 0)),
    }
    return helper.organize_card(expected_map, card)
