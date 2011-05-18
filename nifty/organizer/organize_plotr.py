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
        c1, lori = organize_card_1(env.next(card_iter), module)
    else:
        c1, lori = organize_card_1(env.next(card_iter), module)
    # Likewise, card 2 may be defaulted. If card 2 is not defined, insert a
    # empty card.
    if env.get_card('card_2', module) is None:
        index = card_list.index(c1) + 1
        helper.insert_default_card(index, 'card_2', card_list)
        c2 = organize_card_2(lori, env.next(card_iter), module)
    else:
        c2 = organize_card_2(lori, env.next(card_iter), module)
    # The number of card 2's defines the number of cards 3 through 13.
    number_of_card_2 = len(env.get_cards('card_2', module))
    # XXX: Check for at least two card 2's? There's at least one definition
    # and one which indicates end of plotr job?
    # The last card 2 should not be considered as a new plot index. It is
    # expected to terminate the execution of plotr. Therefore,
    # 'number_of_card_2-1' is used to create the range to iterate over.
#    for c2 in range(number_of_card_2-1):
#        card_2, iplot = analyze_plotr_card_2(lori, env.next(card_iter), module)
#        # Card 3 through 7 should only be defined if iplot = 1 or iplot = -1.
#        if abs(iplot) == 1:
#            analyze_plotr_card_3(env.next(card_iter), module)
#            analyze_plotr_card_3a(env.next(card_iter), module)
#            c4, itype, jtype, ileg = analyze_plotr_card_4(env.next(card_iter), module)
#            analyze_plotr_card_5(env.next(card_iter), module)
#            analyze_plotr_card_5a(env.next(card_iter), module)
#            analyze_plotr_card_6(env.next(card_iter), module)
#            analyze_plotr_card_6a(env.next(card_iter), module)
#            # Card 7 and 7a should only be defined if jtype in card 4 is > 0.
#            if jtype > 0:
#                analyze_plotr_card_7(env.next(card_iter), module)
#                analyze_plotr_card_7a(env.next(card_iter), module)
#        # Card 8 through 13 is always defined regardless of iplot value.
#        card_8, iverf = analyze_plotr_card_8(env.next(card_iter), module)
#        # Card 9 and 10 should only be defined for 2D plots (i.e. if itype
#        # is positive.)
#        if itype > 0:
#            analyze_plotr_card_9(env.next(card_iter), module)
#            # Card 10 should only be defined if ileg != 0.
#            if ileg != 0:
#                analyze_plotr_card_10(env.next(card_iter), module)
#            # Card 10a should only be defined if ileg = 2.
#            if ileg == 2:
#                analyze_plotr_card_10a(env.next(card_iter), module)
#        # Card 11 should only be defined for 3D plots.
#        else:
#            analyze_plotr_card_11(env.next(card_iter), module)
#        # Card 12 and 13 should only be defined if iverf in card 8 is 0.
#        if iverf == 0:
#            card_12, nform = analyze_plotr_card_12(env.next(card_iter), module)
#            # Card 13 should only be defined when nform = 0 in card 12.
#            if nform == 0:
#                # An unknown number of card 13's can be defined, keep
#                # analyzing them until an empty card 13 is seen.
#                while True:
#                    card_13, card_13_stmt_len = analyze_plotr_card_13(env.next(card_iter), module)
#                    if card_13_stmt_len == 0:
#                        break
#    # The last card should be card 2 which have been defined with iplot = 99,
#    # to terminate the plotting job.
#    analyze_plotr_card_2_stop(env.next(card_iter), module)

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
    card = helper.organize_card(expected_map, card)
    # The statement iterator is used to get the lori value which is used in
    # organize_card_2/3 to determine default values.
    stmt_iter = env.get_statement_iterator(card)
    # The first element in the card's statement list is assumed to be the lori
    # node after sorting.
    lori = get_lori(env.next(stmt_iter), card, module)
    return card, lori

def get_lori(node, card, module):
    # lori does not have to be defined, defaults to 1.
    if node is None:
        return 1
    else:
        # Expecting a singleton value.
        l_value, r_value = rule.analyze_singleton(node, card, module)
        # The l-value of the assignment is expected to be an identifier; lori
        rule.identifier_must_be_defined('lori', l_value, card, module)
        # The r-value of the assignment is expected to be an integer.
        lori = rule.must_be_int(l_value, r_value, card, module)
        # Expecting lori to be either 0 or 1.
        if lori not in range(0,2):
            organize_error()
        return lori

def organize_card_2(lori, card, module):
    helper.card_must_be_defined('card_2', card)
    ## Default values for ww and wh depends on the page orientation (lori):
    #
    # According to the NJOY source code: default paper size is US letter size,
    # default page size is paper size with 0.5in margins all around.
    #
    # If page orientation (lori) is portrait then the page size is 7.5 x 10
    # inches, else if the page orientation is landscape then the page size is
    # 10 x 7.5 inches (Rotation angle, 'wr', defaults to 0).
    if lori == 0:
        ww = 7.5
        wh = 10.0
    else:
        ww = 10.0
        wh = 7.5
    expected_map = {
        0 : ('singleton', 'identifier', ('iplot', 1)),
        1 : ('singleton', 'identifier', ('iwcol', 0)),
        2 : ('singleton', 'identifier', ('factx', 1.0)),
        3 : ('singleton', 'identifier', ('facty', 1.0)),
        4 : ('singleton', 'identifier', ('xll', 0.0)),
        5 : ('singleton', 'identifier', ('yll', 0.0)),
        6 : ('singleton', 'identifier', ('ww', ww)),
        7 : ('singleton', 'identifier', ('wh', wh)),
        8 : ('singleton', 'identifier', ('wr', 0)),
    }
    card = helper.organize_card(expected_map, card)
    # The statement iterator is used to get the iplot value which is used in
    # organize_card_list/2 to determine which cards that should be defined and
    # thus be organized.
    stmt_iter = env.get_statement_iterator(card)
    # The first element in the card's statement list is assumed to be the
    # iplot node after organisation.
    iplot = get_iplot(env.next(stmt_iter), card, module)
    return card, iplot

def get_iplot(node, card, module):
    # iplot does not have to be defined, defaults to 1.
    if node is None:
        return 1
    else:
        # Expecting a singleton value.
        l_value, r_value = rule.analyze_singleton(node, card, module)
        # The l-value of the assignment is expected to be an identifier; iplot
        rule.identifier_must_be_defined('iplot', l_value, card, module)
        # The r-value of the assignment is expected to be an integer.
        iplot = rule.must_be_int(l_value, r_value, card, module)
        return iplot
