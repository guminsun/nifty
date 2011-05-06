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
    # Unit numbers that must be defined.
    rule.analyze_unit_number('nendf', env.next(stmt_iter), card, module)
    rule.analyze_unit_number('npend', env.next(stmt_iter), card, module)
    # Optional unit numbers.
    rule.analyze_optional_unit_number('ngout1', env.next(stmt_iter), card, module)
    rule.analyze_optional_unit_number('ngout2', env.next(stmt_iter), card, module)
    # No more statements are allowed. The next statement returned by
    # env.next(card_iter) should be 'None'.
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_groupr_card_2(card, module):
    rule.card_must_be_defined('card_2', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    analyze_groupr_card_2_matb(env.next(stmt_iter), card, module)
    ign = analyze_groupr_card_2_ign(env.next(stmt_iter), card, module)
    igg = analyze_groupr_card_2_igg(env.next(stmt_iter), card, module)
    iwt = analyze_groupr_card_2_iwt(env.next(stmt_iter), card, module)
    analyze_groupr_card_2_lord(env.next(stmt_iter), card, module)
    ntemp = analyze_groupr_card_2_ntemp(env.next(stmt_iter), card, module)
    nsigz = analyze_groupr_card_2_nsigz(env.next(stmt_iter), card, module)
    analyze_groupr_card_2_iprint(env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card, ign, igg, iwt, ntemp, nsigz

def analyze_groupr_card_2_matb(node, card, module):
    # Expecting a singleton value.
    l_value, r_value = rule.analyze_singleton(node, card, module)
    # The l-value of the assignment is expected to be an identifier; matb
    rule.identifier_must_be_defined('matb', l_value, card, module)
    # XXX: Additional checks?
    return r_value.get('value')

def analyze_groupr_card_2_ign(node, card, module):
    l_value, r_value = rule.analyze_singleton(node, card, module)
    rule.identifier_must_be_defined('ign', l_value, card, module)
    # XXX: Additional checks? Range?
    return r_value.get('value')

def analyze_groupr_card_2_igg(node, card, module):
    l_value, r_value = rule.analyze_singleton(node, card, module)
    rule.identifier_must_be_defined('igg', l_value, card, module)
    # XXX: Additional checks? Range?
    return r_value.get('value')

def analyze_groupr_card_2_iwt(node, card, module):
    l_value, r_value = rule.analyze_singleton(node, card, module)
    rule.identifier_must_be_defined('iwt', l_value, card, module)
    # XXX: Additional checks? Range?
    return r_value.get('value')

def analyze_groupr_card_2_lord(node, card, module):
    l_value, r_value = rule.analyze_singleton(node, card, module)
    rule.identifier_must_be_defined('lord', l_value, card, module)
    # XXX: Additional checks? Range?
    return r_value.get('value')

def analyze_groupr_card_2_ntemp(node, card, module):
    l_value, r_value = rule.analyze_singleton(node, card, module)
    rule.identifier_must_be_defined('ntemp', l_value, card, module)
    # XXX: Additional checks? Range?
    return r_value.get('value')

def analyze_groupr_card_2_nsigz(node, card, module):
    l_value, r_value = rule.analyze_singleton(node, card, module)
    rule.identifier_must_be_defined('nsigz', l_value, card, module)
    # XXX: Additional checks? Range?
    return r_value.get('value')

def analyze_groupr_card_2_iprint(node, card, module):
    # iprint (0 = min, 1 = max) does not have to be defined, defaults to 1
    # meaning maximum print option.
    if node is None:
        return 1
    else:
        # If the node is defined, it's expected to be 'iprint'.
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('iprint', l_value, card, module)
        iprint = rule.must_be_int(l_value, r_value, card, module)
        if iprint not in range(0,2):
            id_name = l_value.get('name')
            msg = ('illegal print option in \'card_2\', module \'groupr\': ' +
                   id_name + ' = ' + str(iprint) + ', expected 0 for min, ' +
                   '1 for max (default = 1).')
            rule.semantic_error(msg, node)
    return iprint

def analyze_groupr_card_3(card, module):
    rule.card_must_be_defined('card_3', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    analyze_groupr_card_3_title(env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_groupr_card_3_title(node, card, module):
    l_value, r_value = rule.analyze_singleton(node, card, module)
    # The l-value of the assignment is expected to be an identifier.
    rule.identifier_must_be_defined('title', l_value, card, module)
    # The r-value of the assignment is expected to be a string.
    title = rule.must_be_string(l_value, r_value, card, module)
    rule.string_must_not_exceed_length(l_value, r_value, 80, card, module)
    return title

def analyze_groupr_card_4(ntemp, card, module):
    # Note that the number of temperatures in card 4 should be equal to the
    # number of temperatures ('ntemp') defined in card 2.
    rule.card_must_be_defined('card_4', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    stmt_len = len(stmt_iter)
    if stmt_len == ntemp:
        for i in range(stmt_len):
            analyze_groupr_card_4_temp(i, env.next(stmt_iter), card, module)
    else:
        msg = ('saw ' + str(stmt_len) + ' statements in \'card_4\'' +
               ' but expected ' + str(ntemp) + ' since ' + 'ntemp = ' +
               str(ntemp) + ' in \'card_2\', module ' + '\'groupr\'.')
        rule.semantic_error(msg, card)
    return card

def analyze_groupr_card_4_temp(expected_index, node, card, module):
    l_value, r_value = rule.analyze_singleton(node, card, module)
    # The l-value of the assignment is expected to be an array.
    expected = ('temp', expected_index)
    rule.array_must_be_defined(expected, l_value, card, module)
    # XXX: Additional checks?
    return r_value.get('value')

def analyze_groupr_card_5(nsigz, card, module):
    # Note that the number of sigma zero values in card 5 should be equal to
    # the number of sigma zero values ('nsigz') defined in card 2.
    rule.card_must_be_defined('card_5', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    stmt_len = len(stmt_iter)
    if stmt_len == nsigz:
        for i in range(stmt_len):
            analyze_groupr_card_5_sigz(i, env.next(stmt_iter), card, module)
    else:
        msg = ('saw ' + str(stmt_len) + ' statements in \'card_5\'' +
               ' but expected ' + str(nsigz) + ' since ' + 'nsigz = ' +
               str(nsigz) + ' in \'card_2\', module ' + '\'groupr\'.')
        rule.semantic_error(msg, card)
    return card

def analyze_groupr_card_5_sigz(expected_index, node, card, module):
    l_value, r_value = rule.analyze_singleton(node, card, module)
    # The l-value of the assignment is expected to be an array.
    expected = ('sigz', expected_index)
    rule.array_must_be_defined(expected, l_value, card, module)
    # XXX: Additional checks?
    return r_value.get('value')

def analyze_groupr_card_6a(card, module):
    # Note that card 6a should only be defined if ign = 1 in card_2, check if
    # it is before calling this function.
    msg = ('expected \'card_6a\' since ign = 1 in \'card_2\'')
    rule.card_must_be_defined('card_6a', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    ngn = analyze_groupr_card_6a_ngn(env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card, ngn

def analyze_groupr_card_6a_ngn(node, card, module):
    l_value, r_value = rule.analyze_singleton(node, card, module)
    rule.identifier_must_be_defined('ngn', l_value, card, module)
    ngn = rule.must_be_int(l_value, r_value, card, module)
    # ngn defines the number of neutron groups, a negative value does not make
    # sense.
    if ngn < 0:
        id_name = l_value.get('name')
        msg = ('expected a non-negative number of neutron groups (\'' +
               id_name + '\') ' + 'in \'card_6a\', module \'groupr\'.')
        rule.semantic_error(msg, node)
    return ngn

def analyze_groupr_card_6b(ngn, card, module):
    msg = ('expected \'card_6b\' since ign = 1 in \'card_2\'')
    rule.card_must_be_defined('card_6b', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    stmt_len = len(stmt_iter)
    if stmt_len == ngn+1:
        for i in range(stmt_len):
            # XXX: The ngn+1 group breaks (ev) should be in increasing order.
            analyze_groupr_card_6b_egn(i, env.next(stmt_iter), card, module)
    else:
        msg = ('saw ' + str(stmt_len) + ' statements in \'card_6b\'' +
               ' but expected ' + str(ngn+1) + ' since ' +
               'ngn = ' + str(ngn) + ' in \'card_6a\', module ' +
               '\'groupr\'.')
        rule.semantic_error(msg, card)
    return card

def analyze_groupr_card_6b_egn(expected_index, node, card, module):
    l_value, r_value = rule.analyze_singleton(node, card, module)
    # The l-value of the assignment is expected to be an array.
    expected = ('egn', expected_index)
    rule.array_must_be_defined(expected, l_value, card, module)
    # XXX: Additional checks?
    return r_value.get('value')

def analyze_groupr_card_7a(card, module):
    # Note that card 7a should only be defined if igg = 1 in card_2, check if
    # it is before calling this function.
    msg = ('expected \'card_7a\' since igg = 1 in \'card_2\'')
    rule.card_must_be_defined('card_7a', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    ngg = analyze_groupr_card_7a_ngg(env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card, ngg

def analyze_groupr_card_7a_ngg(node, card, module):
    l_value, r_value = rule.analyze_singleton(node, card, module)
    rule.identifier_must_be_defined('ngg', l_value, card, module)
    ngg = rule.must_be_int(l_value, r_value, card, module)
    # ngg defines the number of gamma groups, a negative value does not make
    # sense.
    if ngg < 0:
        id_name = l_value.get('name')
        msg = ('expected a non-negative number of gamma groups (\'' +
               id_name + '\') ' + 'in \'card_7a\', module \'groupr\'.')
        rule.semantic_error(msg, node)
    return ngg

def analyze_groupr_card_7b(ngg, card, module):
    msg = ('expected \'card_7b\' since igg = 1 in \'card_2\'')
    rule.card_must_be_defined('card_7b', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    stmt_len = len(stmt_iter)
    if stmt_len == ngg+1:
        for i in range(stmt_len):
            # XXX: The ngg+1 group breaks (ev) should be in increasing order.
            analyze_groupr_card_7b_egg(i, env.next(stmt_iter), card, module)
    else:
        msg = ('saw ' + str(stmt_len) + ' statements in \'card_7b\'' +
               ' but expected ' + str(ngg+1) + ' since ' +
               'ngg = ' + str(ngg) + ' in \'card_7a\', module ' +
               '\'groupr\'.')
        rule.semantic_error(msg, card)
    return card

def analyze_groupr_card_7b_egg(expected_index, node, card, module):
    l_value, r_value = rule.analyze_singleton(node, card, module)
    # The l-value of the assignment is expected to be an array.
    expected = ('egg', expected_index)
    rule.array_must_be_defined(expected, l_value, card, module)
    # XXX: Additional checks?
    return r_value.get('value')

def analyze_groupr_card_8a(card, module):
    # Note that card 8a should only be defined if iwt < 0 in card_2, check if
    # it is before calling this function.
    msg = ('expected \'card_8a\' since iwt < 0 in \'card_2\'')
    rule.card_must_be_defined('card_8a', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    # Must be defined.
    analyze_groupr_card_8a_ehi(env.next(stmt_iter), card, module)
    analyze_groupr_card_8a_sigpot(env.next(stmt_iter), card, module)
    analyze_groupr_card_8a_nflmax(env.next(stmt_iter), card, module)
    # Optionals.
    analyze_groupr_card_8a_ninwt(env.next(stmt_iter), card, module)
    analyze_groupr_card_8a_jsigz(env.next(stmt_iter), card, module)
    analyze_groupr_card_8a_alpha2(env.next(stmt_iter), card, module)
    analyze_groupr_card_8a_sam(env.next(stmt_iter), card, module)
    analyze_groupr_card_8a_beta(env.next(stmt_iter), card, module)
    analyze_groupr_card_8a_alpha3(env.next(stmt_iter), card, module)
    analyze_groupr_card_8a_gamma(env.next(stmt_iter), card, module)
    # No more statements are allowed.
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_groupr_card_8a_ehi(node, card, module):
    l_value, r_value = rule.analyze_singleton(node, card, module)
    rule.identifier_must_be_defined('ehi', l_value, card, module)
    # XXX: Additional checks? From documentation: "must be in resolved range"
    return r_value.get('value')

def analyze_groupr_card_8a_sigpot(node, card, module):
    l_value, r_value = rule.analyze_singleton(node, card, module)
    rule.identifier_must_be_defined('sigpot', l_value, card, module)
    # XXX: Additional checks?
    return r_value.get('value')

def analyze_groupr_card_8a_nflmax(node, card, module):
    l_value, r_value = rule.analyze_singleton(node, card, module)
    rule.identifier_must_be_defined('nflmax', l_value, card, module)
    nflmax = rule.must_be_int(l_value, r_value, card, module)
    # XXX: Additional checks?
    return nflmax

def analyze_groupr_card_8a_ninwt(node, card, module):
    # Tape unit for new flux parameters does not have to be defined,
    # defaults to 0.
    return rule.analyze_optional_unit_number('ninwt', node, card, module)

def analyze_groupr_card_8a_jsigz(node, card, module):
    if node is None:
        return 0
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('jsigz', l_value, card, module)
        # XXX: Additional checks?
    return r_value.get('value')

def analyze_groupr_card_8a_alpha2(node, card, module):
    # Alpha for admixed moderator does not have to be defined,
    # defaults to 0 (none).
    if node is None:
        return 0
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('alpha2', l_value, card, module)
        # XXX: Additional checks?
    return r_value.get('value')

def analyze_groupr_card_8a_sam(node, card, module):
    # Admixed moderator does not have to be defined, defaults to 0 (none).
    if node is None:
        return 0
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('sam', l_value, card, module)
        # XXX: Additional checks?
    return r_value.get('value')

def analyze_groupr_card_8a_beta(node, card, module):
    # Heterogeniety parameter does not have to be defined, defaults to 0
    # (meaning none).
    if node is None:
        return 0
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('beta', l_value, card, module)
        # XXX: Additional checks?
    return r_value.get('value')

def analyze_groupr_card_8a_alpha3(node, card, module):
    # Alpha for external moderator does not have to be defined, defaults to 0
    # (meaning none).
    if node is None:
        return 0
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('alpha3', l_value, card, module)
        # XXX: Additional checks?
    return r_value.get('value')

def analyze_groupr_card_8a_gamma(node, card, module):
    # Fraction of admixed moderator cross section in external moderator cross
    # section does not have to be defined, defaults to 0 (meaning none).
    if node is None:
        return 0
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('gamma', l_value, card, module)
        # XXX: Additional checks?
    return r_value.get('value')

def analyze_groupr_card_8b(card, module):
    # Note that card 8b should only be defined if iwt = 1 or iwt = -1 in
    # card_2, check if it is before calling this function.
    msg = ('expected \'card_8b\' since iwt = 1 (or iwt = -1) in \'card_2\'')
    rule.card_must_be_defined('card_8b', card, module, msg)
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
    return card

def analyze_groupr_card_8c(card, module):
    # Note that card 8c should only be defined if iwt = 4 or iwt = -4 in
    # card_2, check if it is before calling this function.
    msg = ('expected \'card_8c\' since iwt = 4 (or iwt = -4) in \'card_2\'')
    rule.card_must_be_defined('card_8c', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    # XXX: Must be defined? No default values specified in documentation.
    analyze_groupr_card_8c_eb(env.next(stmt_iter), card, module)
    analyze_groupr_card_8c_tb(env.next(stmt_iter), card, module)
    analyze_groupr_card_8c_ec(env.next(stmt_iter), card, module)
    analyze_groupr_card_8c_tc(env.next(stmt_iter), card, module)
    # No more statements are allowed.
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_groupr_card_8c_eb(node, card, module):
    l_value, r_value = rule.analyze_singleton(node, card, module)
    rule.identifier_must_be_defined('eb', l_value, card, module)
    # XXX: Additional checks?
    return r_value.get('value')

def analyze_groupr_card_8c_tb(node, card, module):
    l_value, r_value = rule.analyze_singleton(node, card, module)
    rule.identifier_must_be_defined('tb', l_value, card, module)
    # XXX: Additional checks?
    return r_value.get('value')

def analyze_groupr_card_8c_ec(node, card, module):
    l_value, r_value = rule.analyze_singleton(node, card, module)
    rule.identifier_must_be_defined('ec', l_value, card, module)
    # XXX: Additional checks?
    return r_value.get('value')

def analyze_groupr_card_8c_tc(node, card, module):
    l_value, r_value = rule.analyze_singleton(node, card, module)
    rule.identifier_must_be_defined('tc', l_value, card, module)
    # XXX: Additional checks?
    return r_value.get('value')

def analyze_groupr_card_8d(card, module):
    # Note that card 8d should only be defined if iwt = 0 in card_2, check if
    # it is before calling this function.
    msg = ('expected \'card_8d\' since iwt = 0 in \'card_2\'')
    rule.card_must_be_defined('card_8d', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    analyze_groupr_card_8d_ninwt(env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_groupr_card_8d_ninwt(node, card, module):
    # XXX: ninwt must be binary?
    return rule.analyze_unit_number('ninwt', node, card, module)

def analyze_groupr_card_9(card, module):
    rule.card_must_be_defined('card_9', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    # Save the number of statements here since the lenght of stmt_iter
    # decreases when getting the next element from the iterator.
    stmt_length = len(stmt_iter)
    # mfd must always be defined.
    analyze_groupr_card_9_mfd(env.next(stmt_iter), card, module)
    # If the number of statements is one, then:
    #     * mfd = 0 which indicates termination of temperature/material and no
    #       more values are expected for this card, or
    #     * mfd is set to an automatic reaction processing option and no more
    #       values are expected for this card.
    if stmt_length == 1:
        rule.no_statement_allowed(env.next(stmt_iter), card, module)
    # If the number of statements is not 1, then mtd and mtname are expected.
    else:
        analyze_groupr_card_9_mtd(env.next(stmt_iter), card, module)
        analyze_groupr_card_9_mtname(env.next(stmt_iter), card, module)
        rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_groupr_card_9_mfd(node, card, module):
    l_value, r_value = rule.analyze_singleton(node, card, module)
    rule.identifier_must_be_defined('mfd', l_value, card, module)
    # XXX: Additional checks? mfd must be unit number?
    return r_value.get('value')

def analyze_groupr_card_9_mtd(node, card, module):
    l_value, r_value = rule.analyze_singleton(node, card, module)
    rule.identifier_must_be_defined('mtd', l_value, card, module)
    # XXX: Additional checks?
    return r_value.get('value')

def analyze_groupr_card_9_mtname(node, card, module):
    l_value, r_value = rule.analyze_singleton(node, card, module)
    # The l-value of the assignment is expected to be an identifier.
    rule.identifier_must_be_defined('mtname', l_value, card, module)
    # The r-value of the assignment is expected to be a string.
    rule.must_be_string(l_value, r_value, card, module)
    # XXX: Additional checks? Allowed length? (probably 80 characters since
    # ENDF records are limited to 80 characters?)
    return r_value.get('value')

def analyze_groupr_card_10(card, module):
    rule.card_must_be_defined('card_10', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    matd = rule.analyze_material('matd', env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_groupr_card_10_stop(card, module):
    msg = ('expected a \'card_10\' with the material set to 0 to indicate ' + 
           'termination of module \'groupr\'.')
    rule.card_must_be_defined('card_10', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    matd = rule.analyze_material('matd', env.next(stmt_iter), card, module)
    # The last card is expected to be a card 10 with matd = 0, to indicate
    # termination of groupr.
    if matd != 0:
        rule.semantic_error(msg, card)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return matd
