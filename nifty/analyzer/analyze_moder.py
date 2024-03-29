from nifty.environment import helpers as env
import analyzer_rules as rule

from nifty.settings import moder_settings

##############################################################################
# Analyze moder. Checks if moder is somewhat semantically correct.

def analyze_moder(module):
    analyze_moder_card_list(module)
    return module

def analyze_moder_card_list(module):
    card_iter = env.get_card_iterator(module)
    card_1, nin = analyze_moder_card_1(env.next(card_iter), module)
    # Card 2 and 3 should only be defined if abs(nin) is in the range [1,19].
    if abs(nin) in range(1,20):
        analyze_moder_card_2(env.next(card_iter), module)
        # The number of card 3's cannot be predicted, need to count 'em.
        number_of_card_3 = len(env.get_cards('card_3', module))
        # Need at least two card 3's? One to indicate the next material and
        # one to terminate the moder run.
        if number_of_card_3 < 2:
            rule.too_few_cards_defined(number_of_card_3, 2, 'card_3', module)
        # The last card 3 should not be considered as a next material to
        # process, since it is expected to terminate the execution of moder.
        # Therefore, 'number_of_card_3-1' is used to create the range to
        # iterate over.
        for c3 in range(number_of_card_3-1):
            analyze_moder_card_3(env.next(card_iter), module)
        # The last card is expected to be a card 3 with nin = 0, to indicate
        # termination of moder.
        analyze_moder_card_3_stop(env.next(card_iter), module)
    # No more cards are allowed. The next card returned by env.next(card_iter)
    # should be 'None'.
    rule.no_card_allowed(env.next(card_iter), module)
    return module

def analyze_moder_card_1(card, module):
    rule.card_must_be_defined('card_1', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    order_map = moder_settings.card_1_order_map
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    nin = env.get_identifier_value('nin', order_map, card)
    return card, nin

def analyze_moder_card_2(card, module):
    msg = ('expected \'card_2\' since the absolute value of the input unit ' +
           '(\'nin\') is in the range [1,19] in \'card_1\', module \'moder\'.')
    rule.card_must_be_defined('card_2', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    order_map = moder_settings.card_2_order_map
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_moder_card_3(card, module):
    msg = ('expected \'card_3\' since the absolute value of the input unit ' +
           '(\'nin\') is in the range [1,19] in \'card_1\'.')
    rule.card_must_be_defined('card_3', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    order_map = moder_settings.card_3_order_map
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_moder_card_3_stop(card, module):
    msg = ('expected \'card_3\' with the input unit (\'nin\') set to 0 ' +
           'to indicate termination of module \'moder\'.')
    rule.card_must_be_defined('card_3', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    order_map = moder_settings.card_3_order_map
    rule.analyze_statement(order_map.get(0), env.next(stmt_iter), card, module)
    nin = env.get_identifier_value('nin', order_map, card)
    if nin != 0:
        rule.semantic_error(msg, card)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card
