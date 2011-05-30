from nifty.environment import helpers as env
import analyzer_rules as rule

from nifty.settings import acer_settings

##############################################################################
# Analyze acer. Checks if acer is somewhat semantically correct.

def analyze_acer(module):
    analyze_acer_card_list(module)
    return module

def analyze_acer_card_list(module):
    card_iter = env.get_card_iterator(module)
    # Card 1 should always be defined.
    analyze_acer_card_1(env.next(card_iter), module)
    # Card 2 should always be defined.
    # Extract the identifiers iopt and nxtra from card 2 since they are used
    # to determine which cards that should be defined.
    card_2, iopt, nxtra = analyze_acer_card_2(env.next(card_iter), module)
    # Card 3 should always be defined.
    analyze_acer_card_3(env.next(card_iter), module)
    # Card 4 should only be defined if nxtra > 0 in card_2.
    if nxtra > 0:
        analyze_acer_card_4(nxtra, env.next(card_iter), module)
    # Card 5, 6 and 7 should only be defined if iopt = 1 in card_2.
    if iopt == 1:
        analyze_acer_card_5(env.next(card_iter), module)
        analyze_acer_card_6(env.next(card_iter), module)
        analyze_acer_card_7(env.next(card_iter), module)
    # Card 8, 8a and 9 should only be defined if iopt = 2 in card_2.
    if iopt == 2:
        analyze_acer_card_8(env.next(card_iter), module)
        analyze_acer_card_8a(env.next(card_iter), module)
        analyze_acer_card_9(env.next(card_iter), module)
    # Card 10 should only be defined if iopt = 3 in card_2.
    if iopt == 3:
        analyze_acer_card_10(env.next(card_iter), module)
    # Card 11 should only be defined if iopt = 4 or 5 in card_2.
    if iopt == 4 or iopt == 5:
        analyze_acer_card_11(env.next(card_iter), module)
    # No more cards are allowed. The next card returned by env.next(card_iter)
    # should be 'None'.
    rule.no_card_allowed(env.next(card_iter), module)
    return module

def analyze_acer_card_1(card, module):
    rule.card_must_be_defined('card_1', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    expected_map = acer_settings.card_1_order_map
    for i in range(len(expected_map)):
        rule.analyze_statement_E(i, expected_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_acer_card_2(card, module):
    rule.card_must_be_defined('card_2', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    expected_map = acer_settings.card_2_order_map
    for i in range(len(expected_map)):
        rule.analyze_statement_E(i, expected_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    expected_map = acer_settings.card_2_identifier_map
    iopt = env.get_identifier_value('iopt', expected_map, card)
    nxtra = env.get_identifier_value('nxtra', expected_map, card)
    return card, iopt, nxtra

def analyze_acer_card_3(card, module):
    rule.card_must_be_defined('card_3', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    expected_map = acer_settings.card_3_order_map
    for i in range(len(expected_map)):
        rule.analyze_statement_E(i, expected_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_acer_card_4(nxtra, card, module):
    # Note that card 4 should only be defined if nxtra > 0 in card_2, check if
    # it is before calling this function.
    msg = ('expected \'card_4\' since nxtra > 0 in \'card_2\'')
    rule.card_must_be_defined('card_4', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    stmt_len = len(card.get('statement_list'))
    # The expected order is unknown until nxtra has been defined. Therefore,
    # the expected order map will be determined here.
    expected_order_map = {}
    expected_identifier_map = acer_settings.card_4_identifier_map
    for i in range(0, nxtra*2, 2):
        expected_order_map[i] = expected_identifier_map['iz']
        expected_order_map[i+1] = expected_identifier_map['aw']
    for i in range(nxtra):
        rule.analyze_statement_E(i, expected_order_map.get(i*2), env.next(stmt_iter), card, module)
        rule.analyze_statement_E(i, expected_order_map.get(i*2+1), env.next(stmt_iter), card, module)
    return card

def analyze_acer_card_5(card, module):
    # Note that card 5 should only be defined if iopt = 1 in card_2, check if
    # it is before calling this function.
    msg = ('expected \'card_5\' since iopt = 1 in \'card_2\'')
    rule.card_must_be_defined('card_5', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    expected_map = acer_settings.card_5_order_map
    for i in range(len(expected_map)):
        rule.analyze_statement_E(i, expected_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_acer_card_6(card, module):
    # Note that card 6 should only be defined if iopt = 1 in card_2, check if
    # it is before calling this function.
    msg = ('expected \'card_6\' since iopt = 1 in \'card_2\'')
    rule.card_must_be_defined('card_6', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    expected_map = acer_settings.card_6_order_map
    for i in range(len(expected_map)):
        rule.analyze_statement_E(i, expected_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_acer_card_7(card, module):
    # Note that card 7 should only be defined if iopt = 1 in card_2, check if
    # it is before calling this function.
    msg = ('expected \'card_7\' since iopt = 1 in \'card_2\'')
    rule.card_must_be_defined('card_7', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    expected_map = acer_settings.card_7_order_map
    for i in range(len(expected_map)):
        rule.analyze_statement_E(i, expected_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_acer_card_8(card, module):
    # Note that card 8 should only be defined if iopt = 2 in card_2, check if
    # it is before calling this function.
    msg = ('expected \'card_8\' since iopt = 2 in \'card_2\'')
    rule.card_must_be_defined('card_8', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    expected_map = acer_settings.card_8_order_map
    for i in range(len(expected_map)):
        rule.analyze_statement_E(i, expected_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_acer_card_8a(card, module):
    # Note that card 8a should only be defined if iopt = 2 in card_2, check if
    # it is before calling this function.
    msg = ('expected \'card_8a\' since iopt = 2 in \'card_2\'')
    rule.card_must_be_defined('card_8a', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    expected_map = acer_settings.card_8a_order_map
    for i in range(len(expected_map)):
        rule.analyze_statement_E(i, expected_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_acer_card_9(card, module):
    # Note that card 9 should only be defined if iopt = 2 in card_2, check if
    # it is before calling this function.
    msg = ('expected \'card_9\' since iopt = 2 in \'card_2\'')
    rule.card_must_be_defined('card_9', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    expected_map = acer_settings.card_9_order_map
    for i in range(len(expected_map)):
        rule.analyze_statement_E(i, expected_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_acer_card_10(card, module):
    # Note that card 10 should only be defined if iopt = 3 in card_2, check if
    # it is before calling this function.
    msg = ('expected \'card_10\' since iopt = 3 in \'card_2\'')
    rule.card_must_be_defined('card_10', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    expected_map = acer_settings.card_10_order_map
    for i in range(len(expected_map)):
        rule.analyze_statement_E(i, expected_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_acer_card_11(card, module):
    # Note that card 11 should only be defined if iopt = 4 or 5 in card_2,
    # check if it is before calling this function.
    msg = ('expected \'card_11\' since iopt = 4 (or 5) in \'card_2\'')
    rule.card_must_be_defined('card_11', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    expected_map = acer_settings.card_11_order_map
    for i in range(len(expected_map)):
        rule.analyze_statement_E(i, expected_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card
