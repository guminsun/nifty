from nifty.environment import helpers as env
import analyzer_rules as rule

from nifty.settings import reconr_settings

##############################################################################
# Analyze reconr. Checks if reconr is somewhat semantically correct.

def analyze_reconr(module):
    analyze_reconr_card_list(module)
    return module

def analyze_reconr_card_list(module):
    # Use a card iterator to check whether the cards have been defined in the
    # expected order.
    card_iter = env.get_card_iterator(module)
    # Card 1 must always be defined.
    analyze_reconr_card_1(env.next(card_iter), module)
    # Card 2 must always be defined.
    analyze_reconr_card_2(env.next(card_iter), module)
    # Number of card_3's should at least be 2 since one card 3 must always be
    # supplied, and there must be an ending card 3 (with mat = 0) to indicate
    # termination of reconr.
    number_of_card_3 = len(env.get_cards('card_3', module))
    if number_of_card_3 < 2:
        rule.too_few_cards_defined(number_of_card_3, 2, 'card_3', module)
    # The last card 3 should not be considered, since it is expected to
    # terminate the execution of reconr (i.e. mat = 0), therefore,
    # 'number_of_card_3-1' is used to create the range to iterate over.
    for c3 in range(number_of_card_3-1):
        # Card 3 must always be defined.
        card_3, ncards, ngrid = analyze_reconr_card_3(env.next(card_iter), module)
        # Card 4 must be defined for each material desired (card 3).
        analyze_reconr_card_4(env.next(card_iter), module)
        # Card 5 must be defined 'ncards' number of times.
        for c5 in range(ncards):
            analyze_reconr_card_5(ncards, env.next(card_iter), module)
        # XXX Not sure about this; assuming that it works in the same way as
        #     for card 5:
        # Card 6 must be defined 'ngrid' number of times.
        for c6 in range(ngrid):
            analyze_reconr_card_6(ngrid, env.next(card_iter), module)
    # The last card is expected to be a card 3 with mat = 0, to indicate
    # termination of reconr.
    analyze_reconr_card_3_stop(env.next(card_iter), module)
    # No more cards are allowed. The next card returned by env.next(card_iter)
    # should be 'None'.
    rule.no_card_allowed(env.next(card_iter), module)
    return module

def analyze_reconr_card_1(card, module):
    rule.card_must_be_defined('card_1', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    order_map = reconr_settings.card_1_order_map
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_reconr_card_2(card, module):
    rule.card_must_be_defined('card_2', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    order_map = reconr_settings.card_2_order_map
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_reconr_card_3(card, module):
    rule.card_must_be_defined('card_3', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    order_map = reconr_settings.card_3_order_map
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    ncards = env.get_identifier_value('ncards', order_map, card)
    ngrid = env.get_identifier_value('ngrid', order_map, card)
    return card, ncards, ngrid

def analyze_reconr_card_3_stop(card, module):
    # Card 3 with mat = 0 must be defined.
    rule.card_must_be_defined('card_3', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    order_map = reconr_settings.card_3_order_map
    rule.analyze_statement(order_map.get(0), env.next(stmt_iter), card, module)
    mat = env.get_identifier_value('mat', order_map, card)
    # The last card is expected to be a card 3 with mat = 0, to indicate
    # termination of reconr.
    if mat != 0:
        msg = ('expected a \'card_3\' with the material set to 0 to ' +
               'indicate termination of module \'reconr\'.')
        rule.semantic_error(msg, card)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return mat

def analyze_reconr_card_4(card, module):
    msg = ('\'card_4\' must be defined for each material desired (card 3)')
    rule.card_must_be_defined('card_4', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    order_map = reconr_settings.card_4_order_map
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_reconr_card_5(ncards, card, module):
    msg = ('expected ' + str(ncards) + ' \'card_5\'s, since ' +
           'ncards = ' + str(ncards) + ' in the current \'card_3\'.')
    rule.card_must_be_defined('card_5', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    order_map = reconr_settings.card_5_order_map
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_reconr_card_6(ngrid, card, module):
    msg = ('expected ' + str(ngrid) + ' \'card_6\'s, since ' +
           'ngrid = ' + str(ngrid) + ' in the current \'card_3\'.')
    rule.card_must_be_defined('card_6', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    order_map = reconr_settings.card_6_order_map
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card
