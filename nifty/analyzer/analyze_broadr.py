from nifty.environment import helpers as env
import analyzer_rules as rule

from nifty.settings import broadr_settings

##############################################################################
# Analyze broadr. Checks if broadr is somewhat semantically correct.

def analyze_broadr(module):
    analyze_broadr_card_list(module)
    return module

def analyze_broadr_card_list(module):
    card_iter = env.get_card_iterator(module)
    analyze_broadr_card_1(env.next(card_iter), module)
    card2, ntemp2 = analyze_broadr_card_2(env.next(card_iter), module)
    analyze_broadr_card_3(env.next(card_iter), module)
    analyze_broadr_card_4(ntemp2, env.next(card_iter), module)
    # Number of card_5's should at least be 1 since one card 5 must always
    # be supplied (an ending card 5 with mat1 = 0 to indicate termination
    # of broadr).
    number_of_card_5 = len(env.get_cards('card_5', module))
    if number_of_card_5 < 1:
        rule.too_few_cards_defined(number_of_card_5, 1, 'card_5', module)
    # The last card 5 should not be considered as a next material to process,
    # since it is expected to terminate the execution of broadr.
    # Therefore, 'number_of_card_5-1' is used to create the range to iterate
    # over.
    for c5 in range(number_of_card_5-1):
        analyze_broadr_card_5(env.next(card_iter), module)
    # The last card is expected to be a card 5 with mat1 = 0, to indicate
    # termination of broadr.
    analyze_broadr_card_5_stop(env.next(card_iter), module)
    # No more cards are allowed. The next card returned by env.next(card_iter)
    # should be 'None'.
    rule.no_card_allowed(env.next(card_iter), module)
    return module

def analyze_broadr_card_1(card, module):
    rule.card_must_be_defined('card_1', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    order_map = broadr_settings.card_1_order_map
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_broadr_card_2(card, module):
    rule.card_must_be_defined('card_2', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    order_map = broadr_settings.card_2_order_map
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    ntemp2 = env.get_identifier_value('ntemp2', order_map, card)
    return card, ntemp2

def analyze_broadr_card_3(card, module):
    rule.card_must_be_defined('card_3', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    order_map = broadr_settings.card_3_order_map
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_broadr_card_4(ntemp2, card, module):
    # Note that the number of temperatures in card 4 should be equal to the
    # number of temperatures ('ntemp2') defined in card 2.
    rule.card_must_be_defined('card_4', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    stmt_len = len(card.get('statement_list'))
    if not stmt_len == ntemp2:
        msg = ('saw ' + str(stmt_len) + ' statements in \'card_4\'' +
               ' but expected ' + str(ntemp2) + ' since ' + 'ntemp2 = ' +
               str(ntemp2) + ' in \'card_2\', module ' + '\'broadr\'.')
        rule.semantic_error(msg, card)
    # The expected order is unknown until ntemp2 has been defined. Therefore,
    # the order map will be defined here.
    order_map = {}
    identifier_map = broadr_settings.card_4_identifier_map
    for i in range(ntemp2):
        order_map[i] = ('temp2', i, identifier_map.get('temp2'))
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_broadr_card_5(card, module):
    rule.card_must_be_defined('card_5', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    order_map = broadr_settings.card_5_order_map
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_broadr_card_5_stop(card, module):
    msg = ('expected a \'card_5\' with the material set to 0 to indicate ' +
           'termination of module \'broadr\'.')
    rule.card_must_be_defined('card_5', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    order_map = broadr_settings.card_5_order_map
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    # The last card is expected to be a card 5 with mat1 = 0, to indicate
    # termination of broadr.
    mat1 = env.get_identifier_value('mat1', order_map, card)
    if mat1 != 0:
        rule.semantic_error(msg, card)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card
