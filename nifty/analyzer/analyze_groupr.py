from nifty.environment import helpers as env
import analyzer_rules as rule

from nifty.settings import groupr_settings

##############################################################################
# Analyze groupr. Checks if groupr is somewhat semantically correct.

def analyze_groupr(module):
    analyze_groupr_card_list(module)
    return module

def analyze_groupr_card_list(module):
    card_iter = env.get_card_iterator(module)
    # Card 1 must always be defined.
    analyze_groupr_card_1(env.next(card_iter), module)
    # Card 2 must always be defined.
    card_2, ign, igg, iwt, ntemp, nsigz = analyze_groupr_card_2(env.next(card_iter), module)
    # Card 3 must always be defined.
    analyze_groupr_card_3(env.next(card_iter), module)
    # Card 4 must always be defined.
    analyze_groupr_card_4(ntemp, env.next(card_iter), module)
    # Card 5 must always be defined.
    analyze_groupr_card_5(nsigz, env.next(card_iter), module)
    # Card 6a and 6b should only be defined if ign = 1.
    if ign == 1:
        card_6a, ngn = analyze_groupr_card_6a(env.next(card_iter), module)
        analyze_groupr_card_6b(ngn, env.next(card_iter), module)
    # Card 7a and 7b should only be defined if igg = 1.
    if igg == 1:
        card_7a, ngg = analyze_groupr_card_7a(env.next(card_iter), module)
        analyze_groupr_card_7b(ngg, env.next(card_iter), module)
    # Card 8a should only be defined if iwt < 0.
    if iwt < 0:
        analyze_groupr_card_8a(env.next(card_iter), module)
    # Card 8b should only be defined if iwt = 1 or iwt = -1.
    if iwt == 1 or iwt == -1:
        analyze_groupr_card_8b(env.next(card_iter), module)
    # Card 8c should only be defined if iwt = 4 or iwt = -4.
    if iwt == 4 or iwt == -4:
        analyze_groupr_card_8c(env.next(card_iter), module)
    # Card 8d should only be defined if iwt = 0.
    if iwt == 0:
        analyze_groupr_card_8d(env.next(card_iter), module)
    # Number of card_9's should at least be 2 since one card 9 must always be
    # supplied, and there must be an ending card 9 (with mfd = 0) to indicate
    # termination of current temperature/material.
    # XXX: number of temperatures (ntemp) defines the number of card 9 with
    # mfd = 0?
    number_of_card_9 = len(env.get_cards('card_9', module))
    if number_of_card_9 < 2:
        rule.too_few_cards_defined(number_of_card_9, 2, 'card_9', module)
    for c9 in range(number_of_card_9):
        analyze_groupr_card_9(env.next(card_iter), module)
    # Number of card_10's should at least be 1 since one card 10 must always
    # be supplied (an ending card 10 with matd = 0 to indicate termination
    # of groupr).
    number_of_card_10 = len(env.get_cards('card_10', module))
    if number_of_card_10 < 1:
        rule.too_few_cards_defined(number_of_card_10, 1, 'card_10', module)
    # The last card 10 should not be considered as a next material to
    # process, since it is expected to terminate the execution of groupr.
    # Therefore, 'number_of_card_10-1' is used to create the range to iterate
    # over.
    for c10 in range(number_of_card_10-1):
        analyze_groupr_card_10(env.next(card_iter), module)
    # The last card is expected to be a card 10 with matd = 0, to indicate
    # termination of groupr.
    analyze_groupr_card_10_stop(env.next(card_iter), module)
    # No more cards are allowed. The next card returned by env.next(card_iter)
    # should be 'None'.
    rule.no_card_allowed(env.next(card_iter), module)
    return module

def analyze_groupr_card_1(card, module):
    # Card 1 must be defined.
    rule.card_must_be_defined('card_1', card, module, None)
    # Use a statement iterator to check whether the identifiers have been
    # defined in the expected order.
    stmt_iter = env.get_statement_iterator(card)
    order_map = groupr_settings.card_1_order_map
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    # No more statements are allowed. The next statement returned by
    # env.next(card_iter) should be 'None'.
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_groupr_card_2(card, module):
    rule.card_must_be_defined('card_2', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    order_map = groupr_settings.card_2_order_map
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    ign = env.get_identifier_value('ign', order_map, card)
    igg = env.get_identifier_value('igg', order_map, card)
    iwt = env.get_identifier_value('iwt', order_map, card)
    ntemp = env.get_identifier_value('ntemp', order_map, card)
    nsigz = env.get_identifier_value('nsigz', order_map, card)
    return card, ign, igg, iwt, ntemp, nsigz

def analyze_groupr_card_3(card, module):
    rule.card_must_be_defined('card_3', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    order_map = groupr_settings.card_3_order_map
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_groupr_card_4(ntemp, card, module):
    # Note that the number of temperatures in card 4 should be equal to the
    # number of temperatures ('ntemp') defined in card 2.
    rule.card_must_be_defined('card_4', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    stmt_len = len(card.get('statement_list'))
    if not stmt_len == ntemp:
        msg = ('saw ' + str(stmt_len) + ' statements in \'card_4\'' +
               ' but expected ' + str(ntemp) + ' since ' + 'ntemp = ' +
               str(ntemp) + ' in \'card_2\', module ' + '\'groupr\'.')
        rule.semantic_error(msg, card)
    order_map = {}
    identifier_map = groupr_settings.card_4_identifier_map
    for i in range(ntemp):
        order_map[i] = ('temp', i, identifier_map.get('temp'))
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_groupr_card_5(nsigz, card, module):
    # Note that the number of sigma zero values in card 5 should be equal to
    # the number of sigma zero values ('nsigz') defined in card 2.
    rule.card_must_be_defined('card_5', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    stmt_len = len(card.get('statement_list'))
    if not stmt_len == nsigz:
        msg = ('saw ' + str(stmt_len) + ' statements in \'card_5\'' +
               ' but expected ' + str(nsigz) + ' since ' + 'nsigz = ' +
               str(nsigz) + ' in \'card_2\', module ' + '\'groupr\'.')
        rule.semantic_error(msg, card)
    order_map = {}
    identifier_map = groupr_settings.card_5_identifier_map
    for i in range(nsigz):
        order_map[i] = ('sigz', i, identifier_map.get('sigz'))
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_groupr_card_6a(card, module):
    # Note that card 6a should only be defined if ign = 1 in card_2, check if
    # it is before calling this function.
    msg = ('expected \'card_6a\' since ign = 1 in \'card_2\'')
    rule.card_must_be_defined('card_6a', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    order_map = groupr_settings.card_6a_order_map
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    ngn = env.get_identifier_value('ngn', order_map, card)
    return card, ngn

def analyze_groupr_card_6b(ngn, card, module):
    msg = ('expected \'card_6b\' since ign = 1 in \'card_2\'')
    rule.card_must_be_defined('card_6b', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    stmt_len = len(card.get('statement_list'))
    if not stmt_len == ngn+1:
        msg = ('saw ' + str(stmt_len) + ' statements in \'card_6b\'' +
               ' but expected ' + str(ngn+1) + ' since ' +
               'ngn = ' + str(ngn) + ' in \'card_6a\', module ' +
               '\'groupr\'.')
        rule.semantic_error(msg, card)
    # XXX: The ngn+1 group breaks (ev) should be in increasing order.
    order_map = {}
    identifier_map = groupr_settings.card_6b_identifier_map
    for i in range(ngn + 1):
        order_map[i] = ('egn', i, identifier_map.get('egn'))
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_groupr_card_7a(card, module):
    # Note that card 7a should only be defined if igg = 1 in card_2, check if
    # it is before calling this function.
    msg = ('expected \'card_7a\' since igg = 1 in \'card_2\'')
    rule.card_must_be_defined('card_7a', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    order_map = groupr_settings.card_7a_order_map
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    ngg = env.get_identifier_value('ngg', order_map, card)
    return card, ngg

def analyze_groupr_card_7b(ngg, card, module):
    msg = ('expected \'card_7b\' since igg = 1 in \'card_2\'')
    rule.card_must_be_defined('card_7b', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    stmt_len = len(card.get('statement_list'))
    if not stmt_len == ngg+1:
        msg = ('saw ' + str(stmt_len) + ' statements in \'card_7b\' but ' +
               'expected ' + str(ngg+1) + ' since ngg = ' + str(ngn) +
               ' in \'card_7a\', module \'groupr\'.')
        rule.semantic_error(msg, card)
    # XXX: The ngg+1 group breaks (ev) should be in increasing order.
    order_map = {}
    identifier_map = groupr_settings.card_7b_identifier_map
    for i in range(ngg + 1):
        order_map[i] = ('egg', i, identifier_map.get('egg'))
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_groupr_card_8a(card, module):
    # Note that card 8a should only be defined if iwt < 0 in card_2, check if
    # it is before calling this function.
    msg = ('expected \'card_8a\' since iwt < 0 in \'card_2\'')
    rule.card_must_be_defined('card_8a', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    order_map = groupr_settings.card_8a_order_map
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_groupr_card_8b(card, module):
    # Note that card 8b should only be defined if iwt = 1 or iwt = -1 in
    # card_2, check if it is before calling this function.
    msg = ('expected \'card_8b\' since iwt = 1 (or iwt = -1) in \'card_2\'')
    rule.card_must_be_defined('card_8b', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    order_map = {}
    identifier_map = groupr_settings.card_8b_identifier_map
    for i in range(len(card.get('statement_list'))):
        order_map[i] = ('wght', i, identifier_map.get('wght'))
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_groupr_card_8c(card, module):
    # Note that card 8c should only be defined if iwt = 4 or iwt = -4 in
    # card_2, check if it is before calling this function.
    msg = ('expected \'card_8c\' since iwt = 4 (or iwt = -4) in \'card_2\'')
    rule.card_must_be_defined('card_8c', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    order_map = groupr_settings.card_8c_order_map
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_groupr_card_8d(card, module):
    # Note that card 8d should only be defined if iwt = 0 in card_2, check if
    # it is before calling this function.
    msg = ('expected \'card_8d\' since iwt = 0 in \'card_2\'')
    rule.card_must_be_defined('card_8d', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    order_map = groupr_settings.card_8d_order_map
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_groupr_card_9(card, module):
    rule.card_must_be_defined('card_9', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    # Save the number of statements here since the lenght of stmt_iter
    # decreases when getting the next element from the iterator.
    stmt_length = len(card.get('statement_list'))
    order_map = groupr_settings.card_9_order_map
    # mfd must always be defined.
    rule.analyze_statement(order_map.get(0), env.next(stmt_iter), card, module)
    # If the number of statements is one, then:
    #     * mfd = 0 which indicates termination of temperature/material and no
    #       more values are expected for this card, or
    #     * mfd is set to an automatic reaction processing option and no more
    #       values are expected for this card.
    if stmt_length == 1:
        rule.no_statement_allowed(env.next(stmt_iter), card, module)
    # If the number of statements is not 1, then mtd and mtname are expected.
    else:
        # mtd
        rule.analyze_statement(order_map.get(1), env.next(stmt_iter), card, module)
        # mtname
        rule.analyze_statement(order_map.get(2), env.next(stmt_iter), card, module)
        rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_groupr_card_10(card, module):
    rule.card_must_be_defined('card_10', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    order_map = groupr_settings.card_10_order_map
    rule.analyze_statement(order_map.get(0), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_groupr_card_10_stop(card, module):
    msg = ('expected a \'card_10\' with the material set to 0 to indicate ' +
           'termination of module \'groupr\'.')
    rule.card_must_be_defined('card_10', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    order_map = groupr_settings.card_10_order_map
    rule.analyze_statement(order_map.get(0), env.next(stmt_iter), card, module)
    # The last card is expected to be a card 10 with matd = 0, to indicate
    # termination of groupr.
    matd = env.get_identifier_value('matd', order_map, card)
    if matd != 0:
        rule.semantic_error(msg, card)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card
