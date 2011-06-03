from nifty.environment import helpers as env
import analyzer_rules as rule

from nifty.settings import plotr_settings

##############################################################################
# Analyze plotr. Checks if plotr is somewhat semantically correct.

def analyze_plotr(module):
    analyze_plotr_card_list(module)
    return module

def analyze_plotr_card_list(module):
    card_iter = env.get_card_iterator(module)
    analyze_plotr_card_0(env.next(card_iter), module)
    card_1, lori = analyze_plotr_card_1(env.next(card_iter), module)
    # The number of card 2's defines the number of cards 3 through 13.
    number_of_card_2 = len(env.get_cards('card_2', module))
    # XXX: Check for at least two card 2's? There's at least one definition
    # and one which indicates end of plotr job?
    # The last card 2 should not be considered as a new plot index. It is
    # expected to terminate the execution of plotr. Therefore,
    # 'number_of_card_2-1' is used to create the range to iterate over.
    for c2 in range(number_of_card_2-1):
        card_2, iplot = analyze_plotr_card_2(lori, env.next(card_iter), module)
        # Card 3 through 7 should only be defined if iplot = 1 or iplot = -1.
        if abs(iplot) == 1:
            analyze_plotr_card_3(env.next(card_iter), module)
            analyze_plotr_card_3a(env.next(card_iter), module)
            c4, itype, jtype, ileg = analyze_plotr_card_4(env.next(card_iter), module)
            analyze_plotr_card_5(env.next(card_iter), module)
            analyze_plotr_card_5a(env.next(card_iter), module)
            analyze_plotr_card_6(env.next(card_iter), module)
            analyze_plotr_card_6a(env.next(card_iter), module)
            # Card 7 and 7a should only be defined if jtype in card 4 is > 0.
            if jtype > 0:
                analyze_plotr_card_7(env.next(card_iter), module)
                analyze_plotr_card_7a(env.next(card_iter), module)
        # Card 8 through 13 is always defined regardless of iplot value.
        card_8, iverf = analyze_plotr_card_8(env.next(card_iter), module)
        # Card 9 and 10 should only be defined for 2D plots (i.e. if itype
        # is positive.)
        if itype > 0:
            analyze_plotr_card_9(env.next(card_iter), module)
            # Card 10 should only be defined if ileg != 0.
            if ileg != 0:
                analyze_plotr_card_10(env.next(card_iter), module)
            # Card 10a should only be defined if ileg = 2.
            if ileg == 2:
                analyze_plotr_card_10a(env.next(card_iter), module)
        # Card 11 should only be defined for 3D plots.
        else:
            analyze_plotr_card_11(env.next(card_iter), module)
        # Card 12 and 13 should only be defined if iverf in card 8 is 0.
        if iverf == 0:
            card_12, nform = analyze_plotr_card_12(env.next(card_iter), module)
            # Card 13 should only be defined when nform = 0 in card 12.
            if nform == 0:
                # An unknown number of card 13's can be defined, keep
                # analyzing them until an empty card 13 is seen.
                while True:
                    card_13, card_13_stmt_len = analyze_plotr_card_13(env.next(card_iter), module)
                    if card_13_stmt_len == 0:
                        break
    # The last card should be card 2 which have been defined with iplot = 99,
    # to terminate the plotting job.
    analyze_plotr_card_2_stop(env.next(card_iter), module)
    rule.no_card_allowed(env.next(card_iter), module)
    return module

def analyze_plotr_card_0(card, module):
    rule.card_must_be_defined('card_0', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    order_map = plotr_settings.card_0_order_map
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_plotr_card_1(card, module):
    rule.card_must_be_defined('card_1', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    order_map = plotr_settings.card_1_order_map
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    lori = env.get_identifier_value('lori', order_map, card)
    return card, lori

def analyze_plotr_card_2(lori, card, module):
    rule.card_must_be_defined('card_2', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    order_map = plotr_settings.card_2_order_map
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    iplot = env.get_identifier_value('iplot', order_map, card)
    return card, iplot

def analyze_plotr_card_2_stop(card, module):
    msg = ('expected \'card_2\' with the plot index (\'iplot\') set to 99 ' +
           'to indicate termination of module \'plotr\'.')
    rule.card_must_be_defined('card_2', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    order_map = plotr_settings.card_2_order_map
    rule.analyze_statement(order_map.get(0), env.next(stmt_iter), card, module)
    iplot = env.get_identifier_value('iplot', order_map, card)
    # The last card is expected to be a card 2 with iplot = 99, to indicate
    # termination of plotr.
    if iplot != 99:
        rule.semantic_error(msg, card)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card, iplot

def analyze_plotr_card_3(card, module):
    msg = ('expected \'card_3\' since the plot index (\'iplot\') is 1 or ' +
           '-1 in \'card_2\'.')
    rule.card_must_be_defined('card_3', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    order_map = plotr_settings.card_3_order_map
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_plotr_card_3a(card, module):
    msg = ('expected \'card_3a\' since the plot index (\'iplot\') is 1 or ' +
           '-1 in \'card_2\'.')
    rule.card_must_be_defined('card_3a', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    order_map = plotr_settings.card_3a_order_map
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_plotr_card_4(card, module):
    msg = ('expected \'card_4\' since the plot index (\'iplot\') is 1 or ' +
           '-1 in \'card_2\'.')
    rule.card_must_be_defined('card_4', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    order_map = plotr_settings.card_4_order_map
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    itype = env.get_identifier_value('itype', order_map, card)
    jtype = env.get_identifier_value('jtype', order_map, card)
    ileg = env.get_identifier_value('ileg', order_map, card)
    return card, itype, jtype, ileg

def analyze_plotr_card_5(card, module):
    msg = ('expected \'card_5\' since the plot index (\'iplot\') is 1 or ' +
           '-1 in \'card_2\'.')
    rule.card_must_be_defined('card_5', card, module, msg)
    # 'el' and 'eh' are either both defined, or both undefined. 'xstep' is
    # optional.
    if len(card.get('statement_list')) > 0:
        stmt_iter = env.get_statement_iterator(card)
        order_map = plotr_settings.card_5_order_map
        for i in range(len(order_map)):
            rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
        rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_plotr_card_5a(card, module):
    msg = ('expected \'card_5a\' since the plot index (\'iplot\') is 1 or ' +
           '-1 in \'card_2\'.')
    rule.card_must_be_defined('card_5a', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    order_map = plotr_settings.card_5a_order_map
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_plotr_card_6(card, module):
    msg = ('expected \'card_6\' since the plot index (\'iplot\') is 1 or ' +
           '-1 in \'card_2\'.')
    rule.card_must_be_defined('card_6', card, module, msg)
    # 'yl' and 'yh' are either both defined, or both undefined. 'ystep' is
    # optional.
    if len(card.get('statement_list')) > 0:
        stmt_iter = env.get_statement_iterator(card)
        order_map = plotr_settings.card_6_order_map
        for i in range(len(order_map)):
            rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
        rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_plotr_card_6a(card, module):
    msg = ('expected \'card_6a\' since the plot index (\'iplot\') is 1 or ' +
           '-1 in \'card_2\'.')
    rule.card_must_be_defined('card_6a', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    order_map = plotr_settings.card_6a_order_map
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_plotr_card_7(card, module):
    msg = ('expected \'card_7\' since the plot index (\'iplot\') is 1 or ' +
           '-1 and the type for alternate y axis or z axis (\'jtype\') is ' +
           'defined, in \'card_2\'.')
    rule.card_must_be_defined('card_7', card, module, msg)
    # 'rbot' and 'rtop' are either both defined, or both undefined. 'rstep' is
    # optional.
    if len(card.get('statement_list')) > 0:
        stmt_iter = env.get_statement_iterator(card)
        order_map = plotr_settings.card_7_order_map
        for i in range(len(order_map)):
            rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
        rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_plotr_card_7a(card, module):
    msg = ('expected \'card_7a\' since the plot index (\'iplot\') is 1 or ' +
           '-1 and the type for alternate y axis or z axis (\'jtype\') is ' +
           'defined, in \'card_2\'.')
    rule.card_must_be_defined('card_7a', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    order_map = plotr_settings.card_7a_order_map
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_plotr_card_8(card, module):
    rule.card_must_be_defined('card_8', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    order_map = plotr_settings.card_8_order_map
    rule.analyze_statement(order_map.get(0), env.next(stmt_iter), card, module)
    iverf = env.get_identifier_value('iverf', order_map, card)
    # Ignore rest of parameters on card if data on input file is used (i.e. if
    # iverf = 0.)
    if iverf > 0:
        for i in range(1, len(order_map)):
            rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card, iverf

def analyze_plotr_card_9(card, module):
    # XXX: Provide a descriptive message of why card 9 should be supplied.
    rule.card_must_be_defined('card_9', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    order_map = plotr_settings.card_9_order_map
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_plotr_card_10(card, module):
    # XXX: Provide a descriptive message of why card 10 should be supplied.
    rule.card_must_be_defined('card_10', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    order_map = plotr_settings.card_10_order_map
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_plotr_card_10a(card, module):
    rule.card_must_be_defined('card_10a', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    order_map = plotr_settings.card_10a_order_map
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_plotr_card_11(card, module):
    rule.card_must_be_defined('card_11', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    order_map = plotr_settings.card_11_order_map
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_plotr_card_12(card, module):
    msg = ('expected \'card_12\' since the ENDF version (\'iverf\') is 0 ' +
           'in \'card_8\'.')
    rule.card_must_be_defined('card_12', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    order_map = plotr_settings.card_12_order_map
    for i in range(len(order_map)):
        rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    nform = env.get_identifier_value('nform', order_map, card)
    return card, nform

def analyze_plotr_card_13(card, module):
    msg = ('expected a \'card_13\' since \'nform\' is 0 in \'card_12\'.')
    rule.card_must_be_defined('card_13', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    stmt_len = len(card.get('statement_list'))
    if stmt_len == 0:
        return card, stmt_len
    else:
        order_map = plotr_settings.card_13_order_map
        for i in range(len(order_map)):
            rule.analyze_statement(order_map.get(i), env.next(stmt_iter), card, module)
        rule.no_statement_allowed(env.next(stmt_iter), card, module)
        return card, stmt_len
