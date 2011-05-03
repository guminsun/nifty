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

    # No more cards are allowed. The next card returned by env.next(card_iter)
    # should be 'None'.
    #rule.no_card_allowed(env.next(card_iter), module)
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

def analyze_groupr_card_2_matb(matb_node, card_2, module):
    rule.identifier_must_be_defined(('matb', None), matb_node, card_2, module)
    # XXX: Additional checks?
    return env.get_value(env.get_r_value(matb_node))

def analyze_groupr_card_2_ign(ign_node, card_2, module):
    rule.identifier_must_be_defined(('ign', None), ign_node, card_2, module)
    # XXX: Additional checks? Range?
    return env.get_value(env.get_r_value(ign_node))

def analyze_groupr_card_2_igg(igg_node, card_2, module):
    rule.identifier_must_be_defined(('igg', None), igg_node, card_2, module)
    # XXX: Additional checks? Range?
    return env.get_value(env.get_r_value(igg_node))

def analyze_groupr_card_2_iwt(iwt_node, card_2, module):
    rule.identifier_must_be_defined(('iwt', None), iwt_node, card_2, module)
    # XXX: Additional checks? Range?
    return env.get_value(env.get_r_value(iwt_node))

def analyze_groupr_card_2_lord(lord_node, card_2, module):
    rule.identifier_must_be_defined(('lord', None), lord_node, card_2, module)
    # XXX: Additional checks? Range?
    return env.get_value(env.get_r_value(lord_node))

def analyze_groupr_card_2_ntemp(ntemp_node, card_2, module):
    rule.identifier_must_be_defined(('ntemp', None), ntemp_node, card_2, module)
    rule.identifier_must_be_int(ntemp_node)
    # XXX: Additional checks? Range?
    return env.get_value(env.get_r_value(ntemp_node))

def analyze_groupr_card_2_nsigz(nsigz_node, card_2, module):
    rule.identifier_must_be_defined(('nsigz', None), nsigz_node, card_2, module)
    rule.identifier_must_be_int(nsigz_node)
    # XXX: Additional checks? Range?
    return env.get_value(env.get_r_value(nsigz_node))

def analyze_groupr_card_2_iprint(iprint_node, card_2, module):
    # iprint (0 = min, 1 = max) does not have to be defined, defaults to 1
    # meaning maximum print option.
    if env.not_defined(iprint_node):
        return 1
    else:
        # If the node is defined, it has to be 'iprint'.
        rule.identifier_must_be_defined(('iprint', None), iprint_node, card_2, module)
        rule.identifier_must_be_int(iprint_node)
        iprint_r_value = env.get_value(env.get_r_value(iprint_node))
        if iprint_r_value not in range(0,2):
            iprint_l_value = env.get_l_value(iprint_node)
            iprint_id_name = env.get_identifier_name(iprint_l_value)
            msg = ('illegal print option in \'card_2\', module \'groupr\': ' +
                   iprint_id_name + ' = ' + str(iprint_r_value) +
                   ', expected 0 for min, 1 for max (default = 1).')
            rule.semantic_error(msg, iprint_node)
    return iprint_r_value

def analyze_groupr_card_3(card_3, module):
    rule.card_must_be_defined('card_3', card_3, module, None)
    stmt_iter = env.get_statement_iterator(card_3)
    analyze_groupr_card_3_title(env.next(stmt_iter), card_3, module)
    rule.no_statement_allowed(env.next(stmt_iter), card_3, module)
    return card_3

def analyze_groupr_card_3_title(title_node, card_3, module):
    rule.identifier_must_be_defined(('title', None), title_node, card_3, module)
    rule.identifier_must_be_string(title_node, card_3, module)
    rule.identifier_string_must_not_exceed_length(title_node, 80, card_3, module)
    return env.get_value(env.get_r_value(title_node))

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

def analyze_groupr_card_4_temp(expected_index, temp_node, card_4, module):
    expected = ('temp', expected_index)
    rule.identifier_must_be_defined(expected, temp_node, card_4, module)
    return env.get_value(env.get_r_value(temp_node))

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

def analyze_groupr_card_5_sigz(expected_index, sigz_node, card_5, module):
    expected = ('sigz', expected_index)
    rule.identifier_must_be_defined(expected, sigz_node, card_5, module)
    return env.get_value(env.get_r_value(sigz_node))

def analyze_groupr_card_6a(card_6a, module):
    # Note that card 6a should only be defined if ign = 1 in card_2, check if
    # it is before calling this function.
    msg = ('expected \'card_6a\' since ign = 1 in \'card_2\'')
    rule.card_must_be_defined('card_6a', card_6a, module, msg)
    stmt_iter = env.get_statement_iterator(card_6a)
    ngn = analyze_groupr_card_6a_ngn(env.next(stmt_iter), card_6a, module)
    rule.no_statement_allowed(env.next(stmt_iter), card_6a, module)
    return card_6a, ngn

def analyze_groupr_card_6a_ngn(ngn_node, card_6a, module):
    rule.identifier_must_be_defined(('ngn', None), ngn_node, card_6a, module)
    rule.identifier_must_be_int(ngn_node)
    # XXX: Additional checks? Range?
    return env.get_value(env.get_r_value(ngn_node))

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

def analyze_groupr_card_6b_egn(expected_index, egn_node, card_6b, module):
    expected = ('egn', expected_index)
    rule.identifier_must_be_defined(expected, egn_node, card_6b, module)
    return env.get_value(env.get_r_value(egn_node))

def analyze_groupr_card_7a(card_7a, module):
    # Note that card 7a should only be defined if igg = 1 in card_2, check if
    # it is before calling this function.
    msg = ('expected \'card_7a\' since igg = 1 in \'card_2\'')
    rule.card_must_be_defined('card_7a', card_7a, module, msg)
    stmt_iter = env.get_statement_iterator(card_7a)
    ngg = analyze_groupr_card_7a_ngg(env.next(stmt_iter), card_7a, module)
    rule.no_statement_allowed(env.next(stmt_iter), card_7a, module)
    return card_7a, ngg

def analyze_groupr_card_7a_ngg(ngg_node, card_7a, module):
    rule.identifier_must_be_defined(('ngg', None), ngg_node, card_7a, module)
    rule.identifier_must_be_int(ngg_node)
    # XXX: Additional checks? Range?
    return env.get_value(env.get_r_value(ngg_node))

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

def analyze_groupr_card_7b_egg(expected_index, egg_node, card_7b, module):
    expected = ('egg', expected_index)
    rule.identifier_must_be_defined(expected, egg_node, card_7b, module)
    return env.get_value(env.get_r_value(egg_node))
