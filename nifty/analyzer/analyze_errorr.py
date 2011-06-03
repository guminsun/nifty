from nifty.environment import helpers as env
import analyzer_rules as rule

from nifty.settings import errorr_settings

##############################################################################
# Analyze errorr. Checks if errorr is somewhat semantically correct.

def analyze_errorr(module):
    analyze_errorr_card_list(module)
    return module

def analyze_errorr_card_list(module):
    card_iter = env.get_card_iterator(module)
    card_1, ngout = analyze_errorr_card_1(env.next(card_iter), module)
    card_2, ign = analyze_errorr_card_2(env.next(card_iter), module)
    # Card 3 should only be defined for ngout = 0.
    if ngout == 0:
        analyze_errorr_card_3(env.next(card_iter), module)
    # XXX: The rest of the cards depends on the ENDF file version which is
    # being used as input. The translator cannot check this as of yet, hence,
    # just pass the cards along, skipping semantic analysis for them.
    # Could also make the user specify iverf by introducing the variable in
    # for example card 2.
    # XXX: rule.no_card_allowed(env.next(card_iter), module)

def analyze_errorr_card_1(card, module):
    rule.card_must_be_defined('card_1', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    order_map = errorr_settings.card_1_order_map
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    ngout = env.get_identifier_value('ngout', order_map, card)
    return card, ngout

def analyze_errorr_card_2(card, module):
    rule.card_must_be_defined('card_2', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    order_map = errorr_settings.card_2_order_map
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    ign = env.get_identifier_value('ign', order_map, card)
    return card, ign

def analyze_errorr_card_3(card, module):
    rule.card_must_be_defined('card_3', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    order_map = errorr_settings.card_3_order_map
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card
