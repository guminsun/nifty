from nifty.environment import helpers as env
import analyzer_rules as rule

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
    # The last card is expected to be a card 10 with matd = 0, to indicate
    # termination of groupr.
    analyze_reconr_card_10(env.next(card_iter), module)
    # No more cards are allowed. The next card returned by env.next(card_iter)
    # should be 'None'.
    rule.no_card_allowed(env.next(card_iter), module)
    return module

def analyze_groupr_card_1(card_1, module):
    rule.card_must_be_defined('card_1', card_1, module, None)
    stmt_iter = env.get_statement_iterator(card_1)
    rule.analyze_unit_number('nendf', env.next(stmt_iter), card_1, module)
    rule.analyze_unit_number('npend', env.next(stmt_iter), card_1, module)
    rule.analyze_optional_unit_number('ngout1', env.next(stmt_iter), card_1, module)
    rule.analyze_optional_unit_number('ngout2', env.next(stmt_iter), card_1, module)
    rule.no_statement_allowed(env.next(stmt_iter), card_1, module)
    return card_1

def analyze_groupr_card_2(card_2, module):
    rule.card_must_be_defined('card_2', card_2, module, None)
    stmt_iter = env.get_statement_iterator(card_2)
    analyze_groupr_card_2_matb(env.next(stmt_iter), card_2, module)
    ign = analyze_groupr_card_2_ign(env.next(stmt_iter), card_2, module)
    igg = analyze_groupr_card_2_igg(env.next(stmt_iter), card_2, module)
    iwt = analyze_groupr_card_2_iwt(env.next(stmt_iter), card_2, module)
    analyze_groupr_card_2_lord(env.next(stmt_iter), card_2, module)
    ntemp = analyze_groupr_card_2_ntemp(env.next(stmt_iter), card_2, module)
    nsigz = analyze_groupr_card_2_nsigz(env.next(stmt_iter), card_2, module)
    analyze_groupr_card_2_iprint(env.next(stmt_iter), card_2, module)
    rule.no_statement_allowed(env.next(stmt_iter), card_2, module)
    return card_2, ign, igg, iwt, ntemp, nsigz

def analyze_groupr_card_2_matb(node, card, module):
    expected = ('matb', None)
    rule.identifier_must_be_defined(expected, node, card, module)
    # XXX: Additional checks?
    return env.get_value(env.get_r_value(node))

def analyze_groupr_card_2_ign(node, card, module):
    expected = ('ign', None)
    rule.identifier_must_be_defined(expected, node, card, module)
    # XXX: Additional checks? Range?
    return env.get_value(env.get_r_value(node))

def analyze_groupr_card_2_igg(node, card, module):
    expected = ('igg', None)
    rule.identifier_must_be_defined(expected, node, card, module)
    # XXX: Additional checks? Range?
    return env.get_value(env.get_r_value(node))

def analyze_groupr_card_2_iwt(node, card, module):
    expected = ('iwt', None)
    rule.identifier_must_be_defined(expected, node, card, module)
    # XXX: Additional checks? Range?
    return env.get_value(env.get_r_value(node))

def analyze_groupr_card_2_lord(node, card, module):
    expected = ('lord', None)
    rule.identifier_must_be_defined(expected, node, card, module)
    # XXX: Additional checks? Range?
    return env.get_value(env.get_r_value(node))

def analyze_groupr_card_2_ntemp(node, card, module):
    expected = ('ntemp', None)
    rule.identifier_must_be_defined(expected, node, card, module)
    rule.identifier_must_be_int(node)
    # XXX: Additional checks? Range?
    return env.get_value(env.get_r_value(node))

def analyze_groupr_card_2_nsigz(node, card, module):
    expected = ('nsigz', None)
    rule.identifier_must_be_defined(expected, node, card, module)
    rule.identifier_must_be_int(node)
    # XXX: Additional checks? Range?
    return env.get_value(env.get_r_value(node))

def analyze_groupr_card_2_iprint(node, card, module):
    # iprint (0 = min, 1 = max) does not have to be defined, defaults to 1
    # meaning maximum print option.
    if env.not_defined(node):
        return 1
    else:
        # If the node is defined, it's expected to be 'iprint'.
        expected = ('iprint', None)
        rule.identifier_must_be_defined(expected, node, card, module)
        rule.identifier_must_be_int(node)
        iprint_r_value = env.get_value(env.get_r_value(node))
        if iprint_r_value not in range(0,2):
            iprint_l_value = env.get_l_value(node)
            iprint_id_name = env.get_identifier_name(iprint_l_value)
            msg = ('illegal print option in \'card_2\', module \'groupr\': ' +
                   iprint_id_name + ' = ' + str(iprint_r_value) +
                   ', expected 0 for min, 1 for max (default = 1).')
            rule.semantic_error(msg, node)
    return iprint_r_value

def analyze_groupr_card_3(card_3, module):
    rule.card_must_be_defined('card_3', card_3, module, None)
    stmt_iter = env.get_statement_iterator(card_3)
    analyze_groupr_card_3_title(env.next(stmt_iter), card_3, module)
    rule.no_statement_allowed(env.next(stmt_iter), card_3, module)
    return card_3

def analyze_groupr_card_3_title(node, card, module):
    expected = ('title', None)
    rule.identifier_must_be_defined(expected, node, card, module)
    rule.identifier_must_be_string(node, card, module)
    rule.identifier_string_must_not_exceed_length(node, 80, card, module)
    return env.get_value(env.get_r_value(node))

def analyze_groupr_card_4(ntemp_value, card_4, module):
    # Note that the number of temperatures in card 4 should be equal to the
    # number of temperatures ('ntemp_value') defined in card 2.
    rule.card_must_be_defined('card_4', card_4, module, None)
    stmt_iter = env.get_statement_iterator(card_4)
    stmt_len = len(stmt_iter)
    if stmt_len == ntemp_value:
        for i in range(stmt_len):
            analyze_groupr_card_4_temp(i, env.next(stmt_iter), card_4, module)
    else:
        msg = ('saw ' + str(stmt_len) + ' statements in \'card_4\'' +
               ' but expected ' + str(ntemp_value) + ' since ' +
               'ntemp = ' + str(ntemp_value) + ' in \'card_2\', module ' +
               '\'groupr\'.')
        rule.semantic_error(msg, card_4)
    return card_4

def analyze_groupr_card_4_temp(expected_index, node, card, module):
    expected = ('temp', expected_index)
    rule.identifier_must_be_defined(expected, node, card, module)
    return env.get_value(env.get_r_value(node))

def analyze_groupr_card_5(nsigz_value, card_5, module):
    # Note that the number of sigma zero values in card 5 should be equal to
    # the number of sigma zero values ('nsigz_value') defined in card 2.
    rule.card_must_be_defined('card_5', card_5, module, None)
    stmt_iter = env.get_statement_iterator(card_5)
    stmt_len = len(stmt_iter)
    if stmt_len == nsigz_value:
        for i in range(stmt_len):
            analyze_groupr_card_5_sigz(i, env.next(stmt_iter), card_5, module)
    else:
        msg = ('saw ' + str(stmt_len) + ' statements in \'card_5\'' +
               ' but expected ' + str(nsigz_value) + ' since ' +
               'nsigz = ' + str(nsigz_value) + ' in \'card_2\', module ' +
               '\'groupr\'.')
        rule.semantic_error(msg, card_5)
    return card_5

def analyze_groupr_card_5_sigz(expected_index, node, card, module):
    expected = ('sigz', expected_index)
    rule.identifier_must_be_defined(expected, node, card, module)
    return env.get_value(env.get_r_value(node))

def analyze_groupr_card_6a(card_6a, module):
    # Note that card 6a should only be defined if ign = 1 in card_2, check if
    # it is before calling this function.
    msg = ('expected \'card_6a\' since ign = 1 in \'card_2\'')
    rule.card_must_be_defined('card_6a', card_6a, module, msg)
    stmt_iter = env.get_statement_iterator(card_6a)
    ngn = analyze_groupr_card_6a_ngn(env.next(stmt_iter), card_6a, module)
    rule.no_statement_allowed(env.next(stmt_iter), card_6a, module)
    return card_6a, ngn

def analyze_groupr_card_6a_ngn(node, card, module):
    expected = ('ngn', None)
    rule.identifier_must_be_defined(expected, node, card, module)
    rule.identifier_must_be_int(node)
    # XXX: Additional checks? Range?
    return env.get_value(env.get_r_value(node))

def analyze_groupr_card_6b(ngn_value, card_6b, module):
    msg = ('expected \'card_6b\' since ign = 1 in \'card_2\'')
    rule.card_must_be_defined('card_6b', card_6b, module, msg)
    stmt_iter = env.get_statement_iterator(card_6b)
    stmt_len = len(stmt_iter)
    if stmt_len == ngn_value+1:
        for i in range(stmt_len):
            # XXX: The ngn+1 group breaks (ev) should be in increasing order.
            analyze_groupr_card_6b_egn(i, env.next(stmt_iter), card_6b, module)
    else:
        msg = ('saw ' + str(stmt_len) + ' statements in \'card_6b\'' +
               ' but expected ' + str(ngn_value+1) + ' since ' +
               'ngn = ' + str(ngn_value) + ' in \'card_6a\', module ' +
               '\'groupr\'.')
        rule.semantic_error(msg, card_6b)
    return card_6b

def analyze_groupr_card_6b_egn(expected_index, node, card, module):
    expected = ('egn', expected_index)
    rule.identifier_must_be_defined(expected, node, card, module)
    return env.get_value(env.get_r_value(node))

def analyze_groupr_card_7a(card_7a, module):
    # Note that card 7a should only be defined if igg = 1 in card_2, check if
    # it is before calling this function.
    msg = ('expected \'card_7a\' since igg = 1 in \'card_2\'')
    rule.card_must_be_defined('card_7a', card_7a, module, msg)
    stmt_iter = env.get_statement_iterator(card_7a)
    ngg = analyze_groupr_card_7a_ngg(env.next(stmt_iter), card_7a, module)
    rule.no_statement_allowed(env.next(stmt_iter), card_7a, module)
    return card_7a, ngg

def analyze_groupr_card_7a_ngg(node, card, module):
    expected = ('ngg', None)
    rule.identifier_must_be_defined(expected, node, card, module)
    rule.identifier_must_be_int(node)
    # XXX: Additional checks? Range?
    return env.get_value(env.get_r_value(node))

def analyze_groupr_card_7b(ngg_value, card_7b, module):
    msg = ('expected \'card_7b\' since igg = 1 in \'card_2\'')
    rule.card_must_be_defined('card_7b', card_7b, module, msg)
    stmt_iter = env.get_statement_iterator(card_7b)
    stmt_len = len(stmt_iter)
    if stmt_len == ngg_value+1:
        for i in range(stmt_len):
            # XXX: The ngg+1 group breaks (ev) should be in increasing order.
            analyze_groupr_card_7b_egg(i, env.next(stmt_iter), card_7b, module)
    else:
        msg = ('saw ' + str(stmt_len) + ' statements in \'card_7b\'' +
               ' but expected ' + str(ngg_value+1) + ' since ' +
               'ngg = ' + str(ngg_value) + ' in \'card_7a\', module ' +
               '\'groupr\'.')
        rule.semantic_error(msg, card_7b)
    return card_7b

def analyze_groupr_card_7b_egg(expected_index, node, card, module):
    expected = ('egg', expected_index)
    rule.identifier_must_be_defined(expected, node, card, module)
    return env.get_value(env.get_r_value(node))

def analyze_groupr_card_8a(card_8a, module):
    # Note that card 8a should only be defined if iwt < 0 in card_2, check if
    # it is before calling this function.
    msg = ('expected \'card_8a\' since iwt < 0 in \'card_2\'')
    rule.card_must_be_defined('card_8a', card_8a, module, msg)
    stmt_iter = env.get_statement_iterator(card_8a)
    # Must be defined.
    analyze_groupr_card_8a_ehi(env.next(stmt_iter), card_8a, module)
    analyze_groupr_card_8a_sigpot(env.next(stmt_iter), card_8a, module)
    analyze_groupr_card_8a_nflmax(env.next(stmt_iter), card_8a, module)
    # Optionals.
    analyze_groupr_card_8a_ninwt(env.next(stmt_iter), card_8a, module)
    analyze_groupr_card_8a_jsigz(env.next(stmt_iter), card_8a, module)
    analyze_groupr_card_8a_alpha2(env.next(stmt_iter), card_8a, module)
    analyze_groupr_card_8a_sam(env.next(stmt_iter), card_8a, module)
    analyze_groupr_card_8a_beta(env.next(stmt_iter), card_8a, module)
    analyze_groupr_card_8a_alpha3(env.next(stmt_iter), card_8a, module)
    analyze_groupr_card_8a_gamma(env.next(stmt_iter), card_8a, module)
    # No more statements are allowed.
    rule.no_statement_allowed(env.next(stmt_iter), card_8a, module)
    return card_8a

def analyze_groupr_card_8a_ehi(node, card, module):
    expected = ('ehi', None)
    rule.identifier_must_be_defined(expected, node, card, module)
    # XXX: Additional checks? From documentation: "must be in resolved range"
    return env.get_value(env.get_r_value(node))

def analyze_groupr_card_8a_sigpot(node, card, module):
    expected = ('sigpot', None)
    rule.identifier_must_be_defined(expected, node, card, module)
    # XXX: Additional checks?
    return env.get_value(env.get_r_value(node))

def analyze_groupr_card_8a_nflmax(node, card, module):
    expected = ('nflmax', None)
    rule.identifier_must_be_defined(expected, node, card, module)
    rule.identifier_must_be_int(node)
    # XXX: Additional checks?
    return env.get_value(env.get_r_value(node))

def analyze_groupr_card_8a_ninwt(node, card, module):
    # Tape unit for new flux parameters does not have to be defined,
    # defaults to 0.
    return rule.analyze_optional_unit_number('ninwt', node, card, module)

def analyze_groupr_card_8a_jsigz(node, card, module):
    expected = ('jsigz', None)
    if env.not_defined(node):
        return 0
    else:
        rule.identifier_must_be_defined(expected, node, card, module)
        # XXX: Additional checks?
    return env.get_value(env.get_r_value(node))

def analyze_groupr_card_8a_alpha2(node, card, module):
    # Alpha for admixed moderator does not have to be defined, 
    # defaults to 0 (none).
    expected = ('alpha2', None)
    if env.not_defined(node):
        return 0
    else:
        rule.identifier_must_be_defined(expected, node, card, module)
        # XXX: Additional checks?
    return env.get_value(env.get_r_value(node))

def analyze_groupr_card_8a_sam(node, card, module):
    # Admixed moderator does not have to be defined, defaults to 0 (none).
    expected = ('sam', None)
    if env.not_defined(node):
        return 0
    else:
        rule.identifier_must_be_defined(expected, node, card, module)
        # XXX: Additional checks?
    return env.get_value(env.get_r_value(node))

def analyze_groupr_card_8a_beta(node, card, module):
    # Heterogeniety parameter does not have to be defined,
    # defaults to 0 (none).
    expected = ('beta', None)
    if env.not_defined(node):
        return 0
    else:
        rule.identifier_must_be_defined(expected, node, card, module)
        # XXX: Additional checks?
    return env.get_value(env.get_r_value(node))

def analyze_groupr_card_8a_alpha3(node, card, module):
    # Alpha for external moderator does not have to be defined,
    # defaults to 0 (none).
    expected = ('alpha3', None)
    if env.not_defined(node):
        return 0
    else:
        rule.identifier_must_be_defined(expected, node, card, module)
        # XXX: Additional checks?
    return env.get_value(env.get_r_value(node))

def analyze_groupr_card_8a_gamma(node, card, module):
    # Fraction of admixed moderator cross section in external moderator cross
    # section does not have to be defined, defaults to 0 (none).
    expected = ('gamma', None)
    if env.not_defined(node):
        return 0
    else:
        rule.identifier_must_be_defined(expected, node, card, module)
        # XXX: Additional checks?
    return env.get_value(env.get_r_value(node))

def analyze_groupr_card_8b(card_8b, module):
    # Note that card 8b should only be defined if iwt = 1 or iwt = -1 in
    # card_2, check if it is before calling this function.
    msg = ('expected \'card_8b\' since iwt = 1 (or iwt = -1) in \'card_2\'')
    rule.card_must_be_defined('card_8b', card_8b, module, msg)
    # XXX:
    # Skip analysis of 'wght' for now.
    # Could implement it as an array declaration with variable length, but
    # chose to leave it out for now.
    # If wght is needed, and assuming it should be provided as a space
    # separated list to NJOY, then just assign each value to an identifier.
    # E.g.:
    #   wght[0] = value1;
    #   wght[1] = value2;
    #   ...
    #   wght[N] = valueN;
    #
    # XXX: 
    # Would it be neat to implement TAB1 records as variable lists assigned to
    # one variable? For example:
    #     wght = value1 value2 ... valueN;
    return card_8b

def analyze_groupr_card_8c(card_8c, module):
    # Note that card 8c should only be defined if iwt = 4 or iwt = -4 in
    # card_2, check if it is before calling this function.
    msg = ('expected \'card_8c\' since iwt = 4 (or iwt = -4) in \'card_2\'')
    rule.card_must_be_defined('card_8c', card_8c, module, msg)
    stmt_iter = env.get_statement_iterator(card_8c)
    # XXX: Must be defined? No default values specified.
    analyze_groupr_card_8c_eb(env.next(stmt_iter), card_8c, module)
    analyze_groupr_card_8c_tb(env.next(stmt_iter), card_8c, module)
    analyze_groupr_card_8c_ec(env.next(stmt_iter), card_8c, module)
    analyze_groupr_card_8c_tc(env.next(stmt_iter), card_8c, module)
    # No more statements are allowed.
    rule.no_statement_allowed(env.next(stmt_iter), card_8c, module)
    return card_8c

def analyze_groupr_card_8c_eb(node, card, module):
    expected = ('eb', None)
    rule.identifier_must_be_defined(expected, node, card, module)
    # XXX: Additional checks?
    return env.get_value(env.get_r_value(node))

def analyze_groupr_card_8c_tb(node, card, module):
    expected = ('tb', None)
    rule.identifier_must_be_defined(expected, node, card, module)
    # XXX: Additional checks?
    return env.get_value(env.get_r_value(node))

def analyze_groupr_card_8c_ec(node, card, module):
    expected = ('ec', None)
    rule.identifier_must_be_defined(expected, node, card, module)
    # XXX: Additional checks?
    return env.get_value(env.get_r_value(node))

def analyze_groupr_card_8c_tc(node, card, module):
    expected = ('tc', None)
    rule.identifier_must_be_defined(expected, node, card, module)
    # XXX: Additional checks?
    return env.get_value(env.get_r_value(node))

def analyze_groupr_card_8d(card_8d, module):
    # Note that card 8d should only be defined if iwt = 0 in card_2, check if
    # it is before calling this function.
    msg = ('expected \'card_8d\' since iwt = 0 in \'card_2\'')
    rule.card_must_be_defined('card_8d', card_8d, module, msg)
    stmt_iter = env.get_statement_iterator(card_8d)
    analyze_groupr_card_8d_ninwt(env.next(stmt_iter), card_8d, module)
    rule.no_statement_allowed(env.next(stmt_iter), card_8d, module)
    return card_8d

def analyze_groupr_card_8d_ninwt(node, card, module):
    # XXX: ninwt must be binary?
    return rule.analyze_unit_number('ninwt', node, card, module)

def analyze_groupr_card_9(card_9, module):
    rule.card_must_be_defined('card_9', card_9, module, None)
    stmt_iter = env.get_statement_iterator(card_9)
    # Save the number of statements here since the lenght of stmt_iter
    # decreases when getting the next element from the iterator.
    stmt_length = len(stmt_iter)
    # mfd must always be defined.
    analyze_groupr_card_9_mfd(env.next(stmt_iter), card_9, module)
    # If the number of statements is one; mfd is either
    #     * mfd = 0 which indicates termination of temperature/material and no
    #       more values are expected for this card.
    #     * mfd is set to an automatic reaction processing option and no more
    #       values are expected for this card.
    if stmt_length == 1:
        rule.no_statement_allowed(env.next(stmt_iter), card_9, module)
    # If the number of statements is not 1, then we expect to see mtd and
    # mtname.
    else:
        analyze_groupr_card_9_mtd(env.next(stmt_iter), card_9, module)
        analyze_groupr_card_9_mtname(env.next(stmt_iter), card_9, module)
        rule.no_statement_allowed(env.next(stmt_iter), card_9, module)
    return card_9

def analyze_groupr_card_9_mfd(node, card, module):
    expected = ('mfd', None)
    rule.identifier_must_be_defined(expected, node, card, module)
    # XXX: mfd must be unit number? Additional checks?
    return env.get_value(env.get_r_value(node))

def analyze_groupr_card_9_mtd(node, card, module):
    expected = ('mtd', None)
    rule.identifier_must_be_defined(expected, node, card, module)
    # XXX: Additional checks?
    return env.get_value(env.get_r_value(node))

def analyze_groupr_card_9_mtname(node, card, module):
    expected = ('mtname', None)
    rule.identifier_must_be_defined(expected, node, card, module)
    rule.identifier_must_be_string(node, card, module)
    # XXX: Additional checks? Allowed length? (probably 80 characters since
    # ENDF records are limited to 80 characters?)
    return env.get_value(env.get_r_value(node))

def analyze_reconr_card_10(card_10, module):
    rule.card_must_be_defined('card_10', card_10, module, None)
    stmt_iter = env.get_statement_iterator(card_10)
    matd = rule.analyze_identifier_matd(env.next(stmt_iter), card_10, module)
    rule.no_statement_allowed(env.next(stmt_iter), card_10, module)
    return card_10
