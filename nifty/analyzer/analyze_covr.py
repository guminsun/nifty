from nifty.environment import helpers as env
import analyzer_rules as rule

from nifty.settings import covr_settings

##############################################################################
# Analyze covr. Checks if covr is somewhat semantically correct.

def analyze_covr(module):
    analyze_covr_card_list(module)
    return module

def analyze_covr_card_list(module):
    card_iter = env.get_card_iterator(module)
    # Card 1 must always be defined.
    card_1, nout = analyze_covr_card_1(env.next(card_iter), module)
    # Card 2, 2a, and 3a should only be defined if nout <= 0.
    if nout <= 0:
        analyze_covr_card_2(env.next(card_iter), module)
        analyze_covr_card_2a(env.next(card_iter), module)
        card_3a, ncase = analyze_covr_card_3a(env.next(card_iter), module)
    # Card 2b, 3b, and 3c should only be defined if nout > 0.
    else:
        card_2b, ncase = analyze_covr_card_2b(env.next(card_iter), module)
        analyze_covr_card_3b(env.next(card_iter), module)
        analyze_covr_card_3c(env.next(card_iter), module)
    # Card 4 should be defined ncase times. XXX: Should there really be no
    # card 4 if ncase = 0?
    number_of_card_4 = len(env.get_cards('card_4', module))
    if number_of_card_4 != ncase:
        # XXX: Provide better descriptive message. Expects ncase card 4's...
        rule.too_few_cards_defined(number_of_card_4, ncase, 'card_4', module)
    for i in range(ncase):
        analyze_covr_card_4(env.next(card_iter), module)
    rule.no_card_allowed(env.next(card_iter), module)
    return module

def analyze_covr_card_1(card, module):
    rule.card_must_be_defined('card_1', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    order_map = covr_settings.card_1_order_map
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    nout = env.get_identifier_value('nout', order_map, card)
    return card, nout

def analyze_covr_card_2(card, module):
    msg = ('expected \'card_2\' since nout <= 0 in \'card_1\'.')
    rule.card_must_be_defined('card_2', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    order_map = covr_settings.card_2_order_map
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_covr_card_2a(card, module):
    msg = ('expected \'card_2a\' since nout <= 0 in \'card_1\'.')
    rule.card_must_be_defined('card_2a', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    order_map = covr_settings.card_2a_order_map
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_covr_card_3a(card, module):
    msg = ('expected \'card_3a\' since nout <= 0 in \'card_1\'.')
    rule.card_must_be_defined('card_3a', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    order_map = covr_settings.card_3a_order_map
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    ncase = env.get_identifier_value('ncase', order_map, card)
    return card, ncase

def analyze_covr_card_2b(card, module):
    msg = ('expected \'card_2b\' since nout > 0 in \'card_1\'.')
    rule.card_must_be_defined('card_2b', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    order_map = covr_settings.card_2b_order_map
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    ncase = env.get_identifier_value('ncase', order_map, card)
    return card, ncase

def analyze_covr_card_3b(card, module):
    msg = ('expected \'card_3b\' since nout > 0 in \'card_1\'.')
    rule.card_must_be_defined('card_3b', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    order_map = covr_settings.card_3b_order_map
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_covr_card_3c(card, module):
    msg = ('expected \'card_3c\' since nout > 0 in \'card_1\'.')
    rule.card_must_be_defined('card_3c', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    order_map = covr_settings.card_3c_order_map
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_covr_card_4(card, module):
    rule.card_must_be_defined('card_4', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    order_map = covr_settings.card_4_order_map
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card
