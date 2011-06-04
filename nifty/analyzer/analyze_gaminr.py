from nifty.environment import helpers as env
import analyzer_rules as rule

from nifty.settings import gaminr_settings

##############################################################################
# Analyze gaminr. Checks if gaminr is somewhat semantically correct.

def analyze_gaminr(module):
    analyze_card_list(module)
    return module

def analyze_card_list(module):
    card_iter = env.get_card_iterator(module)
    analyze_card_1(env.next(card_iter), module)
    card_2, igg, iwt = analyze_card_2(env.next(card_iter), module)
    analyze_card_3(env.next(card_iter), module)
    if igg == 1:
        analyze_card_4(env.next(card_iter), module)
    if iwt == 1:
        analyze_card_5(env.next(card_iter), module)
    # XXX: Ugly.
    while True:
        # Keep analyzing card 6's until mfd = 0 or mfd = -1 is seen.
        while True:
            card_6, mfd = analyze_card_6(env.next(card_iter), module)
            if mfd == 0 or mfd == -1:
                break
        # Keep analyzing card 7's until matd = 0.
        card_7, matd = analyze_card_7(env.next(card_iter), module)
        if matd == 0:
            break
    rule.no_card_allowed(env.next(card_iter), module)
    return module

def analyze_card_1(card, module):
    rule.card_must_be_defined('card_1', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    order_map = gaminr_settings.card_1_order_map
    rule.analyze_statement(order_map.get(0), env.next(stmt_iter), card, module)
    rule.analyze_statement(order_map.get(1), env.next(stmt_iter), card, module)
    rule.analyze_statement(order_map.get(2), env.next(stmt_iter), card, module)
    rule.analyze_statement(order_map.get(3), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_card_2(card, module):
    rule.card_must_be_defined('card_2', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    order_map = gaminr_settings.card_2_order_map
    rule.analyze_statement(order_map.get(0), env.next(stmt_iter), card, module)
    rule.analyze_statement(order_map.get(1), env.next(stmt_iter), card, module)
    rule.analyze_statement(order_map.get(2), env.next(stmt_iter), card, module)
    rule.analyze_statement(order_map.get(3), env.next(stmt_iter), card, module)
    rule.analyze_statement(order_map.get(4), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    igg = env.get_identifier_value('igg', order_map, card)
    iwt = env.get_identifier_value('iwt', order_map, card)
    return card, igg, iwt

def analyze_card_3(card, module):
    rule.card_must_be_defined('card_3', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    order_map = gaminr_settings.card_3_order_map
    rule.analyze_statement(order_map.get(0), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_card_4(card, module):
    msg = ('expected a \'card_4\' since igg = 1 in \'card_2\'')
    rule.card_must_be_defined('card_4', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    ngg = env.get_identifier_value('ngg', order_map, card)
    identifier_map = gaminr_settings.card_4_identifier_map
    order_map = gaminr_settings.card_4_order_map
    for i in range(1, ngg+2):
        order_map[i] = ('egg', i, identifier_map.get('egg'))
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_card_5(card, module):
    msg = ('expected a \'card_5\' since iwt = 1 in \'card_2\'')
    rule.card_must_be_defined('card_5', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    stmt_len = len(card.get('statement_list'))
    identifier_map = gaminr_settings.card_5_identifier_map
    order_map = {}
    for i in range(stmt_len):
        order_map[i] = ('wght', i, identifier_map.get('wght'))
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_card_6(card, module):
    rule.card_must_be_defined('card_6', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    order_map = gaminr_settings.card_6_order_map
    rule.analyze_statement(order_map.get(0), env.next(stmt_iter), card, module)
    rule.analyze_statement(order_map.get(1), env.next(stmt_iter), card, module)
    rule.analyze_statement(order_map.get(2), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    mfd = env.get_identifier_value('mfd', order_map, card)
    return card, mfd

def analyze_card_7(card, module):
    rule.card_must_be_defined('card_7', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    order_map = gaminr_settings.card_7_order_map
    rule.analyze_statement(order_map.get(0), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    matd = env.get_identifier_value('matd', order_map, card)
    return card, matd
