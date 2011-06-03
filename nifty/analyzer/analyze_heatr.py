from nifty.environment import helpers as env
import analyzer_rules as rule

from nifty.settings import heatr_settings

##############################################################################
# Analyze heatr. Checks if heatr is somewhat semantically correct.

def analyze_heatr(module):
    analyze_heatr_card_list(module)
    return module

def analyze_heatr_card_list(module):
    card_iter = env.get_card_iterator(module)
    analyze_heatr_card_1(env.next(card_iter), module)
    card_2, npk, nqa = analyze_heatr_card_2(env.next(card_iter), module)
    # Card 3 should only be defined if the number of partial kermas (npk) is
    # greater than zero.
    if npk > 0:
        analyze_heatr_card_3(npk, env.next(card_iter), module)
    # Card 4 and 5 should only be defined if the number of user q values (nqa)
    # is greater than zero.
    if nqa > 0:
        analyze_heatr_card_4(nqa, env.next(card_iter), module)
        analyze_heatr_card_5(nqa, env.next(card_iter), module)
    # XXX: card_5a should be supplied if qa >= 99.e6, but should there be a
    # card_5a for each qa that is >= 99.e6?
    # If the next card is 5a, just pass it along for now, no other cards are
    # allowed though.
    next_card = env.next(card_iter)
    if (next_card is not None) and (next_card.get('card_name') == 'card_5a'):
        rule.no_card_allowed(env.next(card_iter), module)
    else:
        rule.no_card_allowed(next_card, module)
    return module

def analyze_heatr_card_1(card, module):
    rule.card_must_be_defined('card_1', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    order_map = heatr_settings.card_1_order_map
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_heatr_card_2(card, module):
    rule.card_must_be_defined('card_2', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    order_map = heatr_settings.card_2_order_map
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    npk = env.get_identifier_value('npk', order_map, card)
    nqa = env.get_identifier_value('nqa', order_map, card)
    return card, npk, nqa

def analyze_heatr_card_3(npk, card, module):
    msg = ('expected \'card_3\' since npk > 0 in \'card_2\'')
    rule.card_must_be_defined('card_3', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    stmt_len = len(card.get('statement_list'))
    if not stmt_len == npk:
        msg = ('saw ' + str(stmt_len) + ' statements in \'card_3\'' +
               ' but expected ' + str(npk) + ' since ' +
               'npk = ' + str(npk) + ' in \'card_2\', module ' +
               '\'heatr\'.')
        rule.semantic_error(msg, card)
    # The expected order is unknown until npk has been defined. Therefore,
    # the order map will be defined here.
    order_map = {}
    identifier_map = heatr_settings.card_3_identifier_map
    for i in range(npk):
        order_map[i] = ('mtk', i, identifier_map.get('mtk'))
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_heatr_card_4(nqa, card, module):
    msg = ('expected \'card_4\' since nqa > 0 in \'card_2\'')
    rule.card_must_be_defined('card_4', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    stmt_len = len(card.get('statement_list'))
    if not stmt_len == nqa:
        msg = ('saw ' + str(stmt_len) + ' statements in \'card_4\' but ' +
               'expected ' + str(nqa) + ' since nqa = ' + str(nqa) +
               ' in \'card_2\', module \'heatr\'.')
        rule.semantic_error(msg, card)
    # The expected order is unknown until nqa has been defined. Therefore,
    # the order map will be defined here.
    order_map = {}
    identifier_map = heatr_settings.card_4_identifier_map
    for i in range(nqa):
        order_map[i] = ('mta', i, identifier_map.get('mta'))
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_heatr_card_5(nqa, card, module):
    msg = ('expected \'card_5\' since nqa > 0 in \'card_2\'')
    rule.card_must_be_defined('card_5', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    stmt_len = len(card.get('statement_list'))
    if not stmt_len == nqa:
        msg = ('saw ' + str(stmt_len) + ' statements in \'card_5\' but ' +
               'expected ' + str(nqa) + ' since nqa = ' + str(nqa) +
               ' in \'card_2\', module \'heatr\'.')
        rule.semantic_error(msg, card)
    # The expected order is unknown until nqa has been defined. Therefore,
    # the order map will be defined here.
    order_map = {}
    identifier_map = heatr_settings.card_5_identifier_map
    for i in range(nqa):
        order_map[i] = ('qa', i, identifier_map.get('qa'))
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    # XXX: Should return the number of qa values which are greater than 99e6,
    # such that card 5a can be analyzed.
    return card

# XXX: analyze_heatr_card_5a
