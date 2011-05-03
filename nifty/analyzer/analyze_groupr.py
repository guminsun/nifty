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
