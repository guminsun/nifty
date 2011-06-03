from nifty.environment import helpers as env
import analyzer_rules as rule

from nifty.settings import purr_settings

##############################################################################
# Analyze purr. Checks if purr is somewhat semantically correct.

def analyze_purr(module):
    analyze_card_list(module)
    return module

def analyze_card_list(module):
    card_iter = env.get_card_iterator(module)
    analyze_card_1(env.next(card_iter), module)
    # Number of card_2's should at least be 1 since one card 2 must always
    # be supplied (an ending card 2 with matd = 0 to indicate termination
    # of purr).
    number_of_card_2 = len(env.get_cards('card_2', module))
    if number_of_card_2 < 1:
        rule.too_few_cards_defined(number_of_card_2, 1, 'card_2', module)
    # The last card 2 should not be considered as a next material to process,
    # since it is expected to terminate the execution of purr.
    # Therefore, 'number_of_card_2-1' is used to create the range to iterate
    # over.
    for c2 in range(number_of_card_2-1):
        card2, ntemp, nsigz = analyze_card_2(env.next(card_iter), module)
        # XXX: Assuming card 3 is only defined when there actually are temps
        # that should be defined.
        if ntemp > 0:
            analyze_card_3(ntemp, env.next(card_iter), module)
        # XXX: Assuming card 4 is only defined when there actually are sigz
        # that should be defined.
        if nsigz > 0:
            analyze_card_4(nsigz, env.next(card_iter), module)
    # The last card is expected to be a card 2 with matd = 0, to indicate
    # termination of purr.
    analyze_card_2_stop(env.next(card_iter), module)
    # No more cards are allowed. The next card returned by env.next(card_iter)
    # should be 'None'.
    rule.no_card_allowed(env.next(card_iter), module)
    return module

def analyze_card_1(card, module):
    rule.card_must_be_defined('card_1', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    order_map = purr_settings.card_1_order_map
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_card_2(card, module):
    rule.card_must_be_defined('card_2', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    order_map = purr_settings.card_2_order_map
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    ntemp = env.get_identifier_value('ntemp', order_map, card)
    nsigz = env.get_identifier_value('nsigz', order_map, card)
    return card, ntemp, nsigz

def analyze_card_3(ntemp, card, module):
    # Note that the number of temperatures in card 3 should be equal to the
    # number of temperatures ('ntemp') defined in card 2.
    msg = ('expected \'card_3\' since the number of temperatures ' +
           '(\'ntemp\') in \'card_2\' is greater than zero.')
    rule.card_must_be_defined('card_3', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    stmt_len = len(card.get('statement_list'))
    if not stmt_len == ntemp:
        msg = ('saw ' + str(stmt_len) + ' statements in \'card_3\'' +
               ' but expected ' + str(ntemp) + ' since ' + 'ntemp = ' +
               str(ntemp) + ' in \'card_2\', module ' + '\'purr\'.')
        rule.semantic_error(msg, card)
    order_map = {}
    identifier_map = purr_settings.card_3_identifier_map
    for i in range(ntemp):
        order_map[i] = ('temp', i, identifier_map.get('temp'))
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    return card

def analyze_card_4(nsigz, card, module):
    # Note that the number of sigma zero values in card 4 should be equal to
    # the number of sigma zero values ('nsigz') defined in card 2.
    rule.card_must_be_defined('card_4', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    stmt_len = len(card.get('statement_list'))
    if not stmt_len == nsigz:
        msg = ('saw ' + str(stmt_len) + ' statements in \'card_4\'' +
               ' but expected ' + str(nsigz) + ' since ' + 'nsigz = ' +
               str(nsigz) + ' in \'card_2\', module ' + '\'purr\'.')
        rule.semantic_error(msg, card)
    order_map = {}
    identifier_map = purr_settings.card_4_identifier_map
    for i in range(nsigz):
        order_map[i] = ('sigz', i, identifier_map.get('sigz'))
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    return card

def analyze_card_2_stop(card, module):
    msg = ('expected a \'card_2\' with the material set to 0 to indicate ' +
           'termination of module \'purr\'.')
    rule.card_must_be_defined('card_2', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    order_map = purr_settings.card_2_order_map
    rule.analyze_statement(order_map.get(0), env.next(stmt_iter), card, module)
    matd = env.get_identifier_value('matd', order_map, card)
    # The last card is expected to be a card 2 with matd = 0, to indicate
    # termination of purr.
    if matd != 0:
        rule.semantic_error(msg, card)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card
