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
    rule.analyze_unit_number('nendf', env.next(stmt_iter), card, module)
    rule.analyze_unit_number('nin', env.next(stmt_iter), card, module)
    rule.analyze_unit_number('nout', env.next(stmt_iter), card, module)
    rule.analyze_optional_unit_number('nplot', env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_heatr_card_2(card, module):
    rule.card_must_be_defined('card_2', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    rule.analyze_material('matd', env.next(stmt_iter), card, module)
    npk = analyze_heatr_card_2_npk(env.next(stmt_iter), card, module)
    nqa = analyze_heatr_card_2_nqa(env.next(stmt_iter), card, module)
    analyze_heatr_card_2_ntemp(env.next(stmt_iter), card, module)
    analyze_heatr_card_2_local(env.next(stmt_iter), card, module)
    analyze_heatr_card_2_iprint(env.next(stmt_iter), card, module)
    analyze_heatr_card_2_ed(env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card, npk, nqa

def analyze_heatr_card_2_npk(node, card, module):
    # npk (number of partial kermas) does not have to be defined,
    # defaults to 0.
    if node is None:
        return 0
    else:
        # If the node is defined, it has to be 'npk'.
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('npk', l_value, card, module)
        npk = rule.must_be_int(l_value, r_value, card, module)
        # npk defines the number of partial kermas, a negative value does not
        # make sense.
        if npk < 0:
            id_name = l_value.get('name')
            msg = ('expected a non-negative number of partial kermas (\'' +
                   id_name + '\') ' + 'in \'card_2\', module \'heatr\'.')
            rule.semantic_error(msg, node)
        return npk

def analyze_heatr_card_2_nqa(node, card, module):
    # nqa (number of q values) does not have to be defined, defaults to 0.
    if node is None:
        return 0
    else:
        # If the node is defined, it has to be 'nqa'.
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('nqa', l_value, card, module)
        nqa = rule.must_be_int(l_value, r_value, card, module)
        # nqa defines the number of user q values, a negative value does not
        # make sense.
        if nqa < 0:
            id_name = l_value.get('name')
            msg = ('expected a non-negative number of user q values (\'' +
                   id_name + '\') ' + 'in \'card_2\', module \'heatr\'.')
            rule.semantic_error(msg, node)
        return nqa

def analyze_heatr_card_2_ntemp(node, card, module):
    # ntemp (number of temperatures to process) does not have to be defined,
    # defaults to 0 meaning all on pendf.
    if node is None:
        return 0
    else:
        # If the node is defined, it has to be 'ntemp'.
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('ntemp', l_value, card, module)
        ntemp = rule.must_be_int(l_value, r_value, card, module)
        # ntemp defines the number of temperatures to process, a negative
        # value is not a proper input.
        if ntemp < 0:
            id_name = l_value.get('name')
            msg = ('expected a non-negative number of temperatures (\'' +
                   id_name + '\') ' + 'in \'card_2\', module \'heatr\'.')
            rule.semantic_error(msg, node)
        return ntemp

def analyze_heatr_card_2_local(node, card, module):
    # local (0/1=gamma rays transported/deposited locally) does not have to be
    # defined, defaults to 0 meaning gamma rays transported.
    if node is None:
        return 0
    else:
        # If the node is defined, it has to be 'local'.
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('local', l_value, card, module)
        local = rule.must_be_int(l_value, r_value, card, module)
        if local not in range(0,2):
            id_name = l_value.get('name')
            msg = ('illegal value in \'card_2\', module \'heatr\': ' +
                   id_name + ' = ' + str(local) + ', expected 0 for gamma ' +
                   ' rays transported or 1 for deposited locally ' +
                   '(default = 0).')
            rule.semantic_error(msg, node)
        return local

def analyze_heatr_card_2_iprint(node, card, module):
    # iprint (0 = min, 1 = max, 2 = check) does not have to be defined,
    # defaults to 0 meaning minimum.
    if node is None:
        return 0
    else:
        # If the node is defined, it has to be 'iprint'.
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('iprint', l_value, card, module)
        iprint = rule.must_be_int(l_value, r_value, card, module)
        if iprint not in range(0,3):
            id_name = l_value.get('name')
            msg = ('illegal print value in \'card_2\', module \'heatr\': ' +
                   id_name + ' = ' + str(iprint) + ', expected 0 for min, ' +
                   '1 for max or 2 for check (default = 0).')
            rule.semantic_error(msg, node)
    return iprint

def analyze_heatr_card_2_ed(node, card, module):
    # ed (displacement energy for damage) does not have to be defined, default
    # from built-in table.
    if node is None:
        return None
    else:
        # If the node is defined, it has to be 'ed'.
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('ed', l_value, card, module)
        # XXX: Additional checks?
    return r_value.get('value')

def analyze_heatr_card_3(npk, card, module):
    msg = ('expected \'card_3\' since npk > 0 in \'card_2\'')
    rule.card_must_be_defined('card_3', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    stmt_len = len(stmt_iter)
    if stmt_len == npk:
        for i in range(stmt_len):
            analyze_heatr_card_3_mtk(i, env.next(stmt_iter), card, module)
    else:
        msg = ('saw ' + str(stmt_len) + ' statements in \'card_3\'' +
               ' but expected ' + str(npk) + ' since ' +
               'npk = ' + str(npk) + ' in \'card_2\', module ' +
               '\'heatr\'.')
        rule.semantic_error(msg, card)
    # This check is really not required here since we loop over the entire
    # statement list above.
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_heatr_card_3_mtk(expected_index, node, card, module):
    l_value, r_value = rule.analyze_singleton(node, card, module)
    # The l-value of the assignment is expected to be an array.
    expected = ('mtk', expected_index)
    rule.array_must_be_defined(expected, l_value, card, module)
    # XXX: Additional checks? The range of allowed values in the documentation
    # does not seem to be complete. See for example NJOY Test Problem 08 where
    # mtk[0] = 302.
    return r_value.get('value')

def analyze_heatr_card_4(nqa, card, module):
    msg = ('expected \'card_4\' since nqa > 0 in \'card_2\'')
    rule.card_must_be_defined('card_4', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    stmt_len = len(stmt_iter)
    if stmt_len == nqa:
        for i in range(stmt_len):
            analyze_heatr_card_4_mta(i, env.next(stmt_iter), card, module)
    else:
        msg = ('saw ' + str(stmt_len) + ' statements in \'card_4\'' +
               ' but expected ' + str(nqa) + ' since ' +
               'nqa = ' + str(nqa) + ' in \'card_2\', module ' +
               '\'heatr\'.')
        rule.semantic_error(msg, card)
    # This check is really not required here since we loop over the entire
    # statement list above.
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_heatr_card_4_mta(expected_index, node, card, module):
    l_value, r_value = rule.analyze_singleton(node, card, module)
    # The l-value of the assignment is expected to be an array.
    expected = ('mta', expected_index)
    rule.array_must_be_defined(expected, l_value, card, module)
    # XXX: Additional checks?
    return r_value.get('value')

def analyze_heatr_card_5(nqa, card, module):
    msg = ('expected \'card_5\' since nqa > 0 in \'card_2\'')
    rule.card_must_be_defined('card_5', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    stmt_len = len(stmt_iter)
    if stmt_len == nqa:
        for i in range(stmt_len):
            analyze_heatr_card_5_qa(i, env.next(stmt_iter), card, module)
    else:
        msg = ('saw ' + str(stmt_len) + ' statements in \'card_5\'' +
               ' but expected ' + str(nqa) + ' since ' +
               'nqa = ' + str(nqa) + ' in \'card_2\', module ' +
               '\'heatr\'.')
        rule.semantic_error(msg, card)
    # This check is really not required here since we loop over the entire
    # statement list above.
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    # XXX: Should return the number of qa values which are greater than 99e6,
    # such that card 5a can be analyzed.
    return card

def analyze_heatr_card_5_qa(expected_index, node, card, module):
    l_value, r_value = rule.analyze_singleton(node, card, module)
    # The l-value of the assignment is expected to be an array.
    expected = ('qa', expected_index)
    rule.array_must_be_defined(expected, l_value, card, module)
    # XXX: Additional checks?
    return r_value.get('value')
