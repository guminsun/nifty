from nifty.environment import helpers as env
import analyzer_rules as rule

from nifty.settings import thermr_settings

##############################################################################
# Analyze thermr. Checks if thermr is somewhat semantically correct.

def analyze_thermr(module):
    analyze_thermr_card_list(module)
    return module

def analyze_thermr_card_list(module):
    card_iter = env.get_card_iterator(module)
    analyze_thermr_card_1(env.next(card_iter), module)
    card_2, ntemp = analyze_thermr_card_2(env.next(card_iter), module)
    analyze_thermr_card_3(ntemp, env.next(card_iter), module)
    analyze_thermr_card_4(env.next(card_iter), module)
    rule.no_card_allowed(env.next(card_iter), module)
    return module

def analyze_thermr_card_1(card, module):
    rule.card_must_be_defined('card_1', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    order_map = thermr_settings.card_1_order_map
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_thermr_card_2(card, module):
    rule.card_must_be_defined('card_2', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    order_map = thermr_settings.card_2_order_map
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    ntemp = env.get_identifier_value('ntemp', order_map, card)
    return card, ntemp

def analyze_thermr_card_3(ntempr, card, module):
    # Note that the number of temperatures in card 3 should be equal to the
    # number of temperatures ('ntempr') defined in card 2.
    rule.card_must_be_defined('card_3', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    stmt_len = len(card.get('statement_list'))
    if not stmt_len == ntempr:
        card_name = card.get('card_name')
        module_name = module.get('module_name')
        msg = ('saw ' + str(stmt_len) + ' statement(s) in \'' + card_name +
               '\' but expected ' + str(ntempr) + ' since the number of ' +
               'temperatures (\'ntempr\') is ' + str(ntempr) + ' in ' +
               '\'card_2\', module ' + '\'' + module_name + '\'.')
        rule.semantic_error(msg, card)
    order_map = {}
    identifier_map = thermr_settings.card_3_identifier_map
    for i in range(ntempr):
        order_map[i] = ('tempr', i, identifier_map.get('tempr'))
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_thermr_card_4(card, module):
    rule.card_must_be_defined('card_4', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    order_map = thermr_settings.card_4_order_map
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card
