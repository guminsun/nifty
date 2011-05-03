from nifty.environment import helpers as env
import analyzer_rules as rule

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
    return module

def analyze_heatr_card_1(card_1, module):
    rule.card_must_be_defined('card_1', card_1, module, None)
    stmt_iter = env.get_statement_iterator(card_1)
    rule.analyze_unit_number('nendf', env.next(stmt_iter), card_1, module)
    rule.analyze_unit_number('nin', env.next(stmt_iter), card_1, module)
    rule.analyze_unit_number('nout', env.next(stmt_iter), card_1, module)
    rule.analyze_optional_unit_number('nplot', env.next(stmt_iter), card_1, module)
    rule.no_statement_allowed(env.next(stmt_iter), card_1, module)
    return card_1

def analyze_heatr_card_2(card_2, module):
    rule.card_must_be_defined('card_2', card_2, module, None)
    stmt_iter = env.get_statement_iterator(card_2)
    rule.analyze_identifier_matd(env.next(stmt_iter), card_2, module)
    npk = analyze_heatr_card_2_npk(env.next(stmt_iter), card_2, module)
    nqa = analyze_heatr_card_2_nqa(env.next(stmt_iter), card_2, module)
    analyze_heatr_card_2_ntemp(env.next(stmt_iter), card_2, module)
    analyze_heatr_card_2_local(env.next(stmt_iter), card_2, module)
    analyze_heatr_card_2_iprint(env.next(stmt_iter), card_2, module)
    analyze_heatr_card_2_ed(env.next(stmt_iter), card_2, module)
    rule.no_statement_allowed(env.next(stmt_iter), card_2, module)
    return card_2, npk, nqa

def analyze_heatr_card_2_npk(npk_node, card_2, module):
    # npk (number of partial kermas) does not have to be defined,
    # defaults to 0.
    if env.not_defined(npk_node):
        return 0
    else:
        # If the node is defined, it has to be 'npk'.
        rule.identifier_must_be_defined(('npk', None), npk_node, card_2, module)
        rule.identifier_must_be_int(npk_node)
        # XXX: Check if npk is positive, negative number of partial kermas is
        #      not a proper input.
    return env.get_value(env.get_r_value(npk_node))


def analyze_heatr_card_2_nqa(nqa_node, card_2, module):
    # nqa (number of q values) does not have to be defined, defaults to 0.
    if env.not_defined(nqa_node):
        return 0
    else:
        # If the node is defined, it has to be 'nqa'.
        rule.identifier_must_be_defined(('nqa', None), nqa_node, card_2, module)
        rule.identifier_must_be_int(nqa_node)
        # XXX: Check if nqa is positive, negative number of user q values is
        #      not a proper input.
    return env.get_value(env.get_r_value(nqa_node))

def analyze_heatr_card_2_ntemp(ntemp_node, card_2, module):
    # ntemp (number of temperatures to process) does not have to be defined,
    # defaults to 0 meaning all on pendf.
    if env.not_defined(ntemp_node):
        return 0
    else:
        # If the node is defined, it has to be 'ntemp'.
        rule.identifier_must_be_defined(('ntemp', None), ntemp_node, card_2, module)
        rule.identifier_must_be_int(ntemp_node)
        # XXX: Check if ntemp is positive, negative number of temperatures to
        #      process is not a proper input.
    return env.get_value(env.get_r_value(ntemp_node))

def analyze_heatr_card_2_local(local_node, card_2, module):
    # local (0/1=gamma rays transported/deposited locally) does not have to be
    # defined, defaults to 0 meaning gamma rays transported.
    if env.not_defined(local_node):
        return 0
    else:
        # If the node is defined, it has to be 'local'.
        rule.identifier_must_be_defined(('local', None), local_node, card_2, module)
        rule.identifier_must_be_int(local_node)
        local_r_value = env.get_value(env.get_r_value(local_node))
        if local_r_value not in range(0,2):
            local_l_value = env.get_l_value(local_node)
            local_id_name = env.get_identifier_name(local_l_value)
            msg = ('illegal value in \'card_2\', module \'heatr\': ' +
                   local_id_name + ' = ' + str(local_r_value) +
                   ', expected 0 for gamma rays transported or 1 for ' +
                   'deposited locally (default = 0).')
            rule.semantic_error(msg, local_node)
    return local_r_value

def analyze_heatr_card_2_iprint(iprint_node, card_2, module):
    # iprint (0 = min, 1 = max, 2 = check) does not have to be defined,
    # defaults to 0 meaning minimum.
    if env.not_defined(iprint_node):
        return 0
    else:
        # If the node is defined, it has to be 'iprint'.
        rule.identifier_must_be_defined(('iprint', None), iprint_node, card_2, module)
        rule.identifier_must_be_int(iprint_node)
        iprint_r_value = env.get_value(env.get_r_value(iprint_node))
        if iprint_r_value not in range(0,3):
            iprint_l_value = env.get_l_value(iprint_node)
            iprint_id_name = env.get_identifier_name(iprint_l_value)
            msg = ('illegal print value in \'card_2\', module \'heatr\': ' +
                   iprint_id_name + ' = ' + str(iprint_r_value) +
                   ', expected 0 for min, 1 for max or 2 for check ' +
                   '(default = 0).')
            rule.semantic_error(msg, iprint_node)
    return iprint_r_value

def analyze_heatr_card_2_ed(ed_node, card_2, module):
    # ed (displacement energy for damage) does not have to be defined,
    # default from built-in table. 
    if env.not_defined(ed_node):
        return None
    else:
        # If the node is defined, it has to be 'ed'.
        rule.identifier_must_be_defined(('ed', None), ed_node, card_2, module)
        # XXX: Type for 'ed'?
    return env.get_value(env.get_r_value(ed_node))

def analyze_heatr_card_3(npk_value, card_3, module):
    msg = ('expected \'card_3\' since npk > 0 in \'card_2\'')
    rule.card_must_be_defined('card_3', card_3, module, msg)
    stmt_iter = env.get_statement_iterator(card_3)
    stmt_len = len(stmt_iter)
    if stmt_len == npk_value:
        for i in range(stmt_len):
            analyze_heatr_card_3_mtk(i, env.next(stmt_iter), card_3, module)
    else:
        msg = ('saw ' + str(stmt_len) + ' statements in \'card_3\'' +
               ' but expected ' + str(npk_value) + ' since ' +
               'npk = ' + str(npk_value) + ' in \'card_2\', module ' +
               '\'heatr\'.')
        rule.semantic_error(msg, card_3)
    # This check is really not required here since we loop over the entire
    # statement list above.
    rule.no_statement_allowed(env.next(stmt_iter), card_3, module)
    return card_3

def analyze_heatr_card_3_mtk(expected_index, mtk_node, card_3, module):
    rule.identifier_must_be_defined(('mtk', expected_index), mtk_node, card_3,
                                    module)
    rule.identifier_must_be_int(mtk_node)
    # XXX: Additional checks? The range of allowed values in the documentation
    # does not seem to be complete. See for example NJOY Test Problem 08 where
    # mtk[0] = 302.
    return env.get_value(env.get_r_value(mtk_node))

def analyze_heatr_card_4(nqa_value, card_4, module):
    msg = ('expected \'card_4\' since nqa > 0 in \'card_2\'')
    rule.card_must_be_defined('card_4', card_4, module, msg)
    stmt_iter = env.get_statement_iterator(card_4)
    stmt_len = len(stmt_iter)
    if stmt_len == nqa_value:
        for i in range(stmt_len):
            analyze_heatr_card_4_mta(i, env.next(stmt_iter), card_4, module)
    else:
        msg = ('saw ' + str(stmt_len) + ' statements in \'card_4\'' +
               ' but expected ' + str(nqa_value) + ' since ' +
               'nqa = ' + str(nqa_value) + ' in \'card_2\', module ' +
               '\'heatr\'.')
        rule.semantic_error(msg, card_4)
    # This check is really not required here since we loop over the entire
    # statement list above.
    rule.no_statement_allowed(env.next(stmt_iter), card_4, module)
    return card_4

def analyze_heatr_card_4_mta(expected_index, mta_node, card_4, module):
    rule.identifier_must_be_defined(('mta', expected_index), mta_node, card_4,
                                    module)
    # XXX: Additional checks?
    return env.get_value(env.get_r_value(mta_node))

def analyze_heatr_card_5(nqa_value, card_5, module):
    # XXX: Need to implement.
    pass
