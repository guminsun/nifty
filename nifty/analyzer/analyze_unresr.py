from nifty.environment import helpers as env
import analyzer_rules as rule

##############################################################################
# Analyze unresr. Checks if unresr is somewhat semantically correct.

def analyze_unresr(module):
    analyze_card_list(module)
    return module

def analyze_card_list(module):
    card_iter = env.get_card_iterator(module)
    analyze_card_1(env.next(card_iter), module)
    # Number of card_2's should at least be 1 since one card 2 must always
    # be supplied (an ending card 2 with matd = 0 to indicate termination
    # of unresr).
    number_of_card_2 = len(env.get_cards('card_2', module))
    if number_of_card_2 < 1:
        rule.too_few_cards_defined(number_of_card_2, 1, 'card_2', module)
    # The last card 2 should not be considered as a next material to process,
    # since it is expected to terminate the execution of unresr.
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
    # termination of unresr.
    analyze_card_2_stop(env.next(card_iter), module)
    # No more cards are allowed. The next card returned by env.next(card_iter)
    # should be 'None'.
    rule.no_card_allowed(env.next(card_iter), module)
    return module

def analyze_card_1(card, module):
    rule.card_must_be_defined('card_1', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    rule.analyze_unit_number('nendf', env.next(stmt_iter), card, module)
    rule.analyze_unit_number('nin', env.next(stmt_iter), card, module)
    rule.analyze_unit_number('nout', env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_card_2(card, module):
    rule.card_must_be_defined('card_2', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    rule.analyze_material('matd', env.next(stmt_iter), card, module)
    ntemp = analyze_card_2_ntemp(env.next(stmt_iter), card, module)
    nsigz = analyze_card_2_nsigz(env.next(stmt_iter), card, module)
    analyze_card_2_iprint(env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card, ntemp, nsigz

def analyze_card_2_ntemp(node, card, module):
    l_value, r_value = rule.must_be_assignment(node, card, module)
    rule.identifier_must_be_defined('ntemp', l_value, card, module)
    ntemp = rule.must_be_int(l_value, r_value, card, module)
    if ntemp < 0:
        id_name = l_value.get('name')
        msg = ('expected a non-negative number of temperatures (\'' +
               id_name + '\') ' + 'in \'card_2\', module \'unresr\'.')
        rule.semantic_error(msg, node)
    if ntemp > 10:
        id_name = l_value.get('name')
        msg = ('expected at most 10 temperatures (\'' + id_name + '\') ' +
               'in \'card_2\', module \'unresr\'.')
        rule.semantic_error(msg, node)
    return ntemp

def analyze_card_2_nsigz(node, card, module):
    l_value, r_value = rule.must_be_assignment(node, card, module)
    rule.identifier_must_be_defined('nsigz', l_value, card, module)
    nsigz = rule.must_be_int(l_value, r_value, card, module)
    if nsigz < 0:
        id_name = l_value.get('name')
        msg = ('expected a non-negative number of sigma zero values (\'' +
               id_name + '\') in \'card_2\', module \'unresr\'.')
        rule.semantic_error(msg, node)
    if nsigz > 10:
        id_name = l_value.get('name')
        msg = ('expected at most 10 sigma zero values (\'' + id_name +
               '\') in \'card_2\', module \'unresr\'.')
        rule.semantic_error(msg, node)
    return nsigz

def analyze_card_2_iprint(node, card, module):
    # iprint (0 = min, 1 = max) does not have to be defined, defaults to 0
    # meaning minimum print option.
    if node is None:
        return 0
    else:
        l_value, r_value = rule.must_be_assignment(node, card, module)
        rule.identifier_must_be_defined('iprint', l_value, card, module)
        iprint = rule.must_be_int(l_value, r_value, card, module)
        if iprint not in range(0,2):
            id_name = l_value.get('name')
            msg = ('illegal print option in \'card_2\', module \'unresr\': ' +
                   id_name + ' = ' + str(iprint) + ', expected 0 for min, ' +
                   '1 for max (default = 1).')
            rule.semantic_error(msg, node)
        return iprint

def analyze_card_3(ntemp, card, module):
    # Note that the number of temperatures in card 3 should be equal to the
    # number of temperatures ('ntemp') defined in card 2.
    msg = ('expected \'card_3\' since the number of temperatures ' +
           '(\'ntemp\') in \'card_2\' is greater than zero.')
    rule.card_must_be_defined('card_3', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    stmt_len = len(stmt_iter)
    if stmt_len == ntemp:
        for i in range(stmt_len):
            analyze_card_3_temp(i, env.next(stmt_iter), card, module)
    else:
        msg = ('saw ' + str(stmt_len) + ' statements in \'card_3\'' +
               ' but expected ' + str(ntemp) + ' since ' + 'ntemp = ' +
               str(ntemp) + ' in \'card_2\', module ' + '\'unresr\'.')
        rule.semantic_error(msg, card)
    return card

def analyze_card_3_temp(expected_index, node, card, module):
    l_value, r_value = rule.must_be_assignment(node, card, module)
    # The l-value of the assignment is expected to be an array.
    expected = ('temp', expected_index)
    rule.array_must_be_defined(expected, l_value, card, module)
    # XXX: Additional checks?
    return r_value.get('value')

def analyze_card_4(nsigz, card, module):
    # Note that the number of sigma zero values in card 4 should be equal to
    # the number of sigma zero values ('nsigz') defined in card 2.
    rule.card_must_be_defined('card_4', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    stmt_len = len(stmt_iter)
    if stmt_len == nsigz:
        for i in range(stmt_len):
            analyze_card_4_sigz(i, env.next(stmt_iter), card, module)
    else:
        msg = ('saw ' + str(stmt_len) + ' statements in \'card_4\'' +
               ' but expected ' + str(nsigz) + ' since ' + 'nsigz = ' +
               str(nsigz) + ' in \'card_2\', module ' + '\'unresr\'.')
        rule.semantic_error(msg, card)
    return card

def analyze_card_4_sigz(expected_index, node, card, module):
    l_value, r_value = rule.must_be_assignment(node, card, module)
    # The l-value of the assignment is expected to be an array.
    expected = ('sigz', expected_index)
    rule.array_must_be_defined(expected, l_value, card, module)
    # XXX: Additional checks?
    return r_value.get('value')

def analyze_card_2_stop(card, module):
    msg = ('expected a \'card_2\' with the material set to 0 to indicate ' +
           'termination of module \'unresr\'.')
    rule.card_must_be_defined('card_2', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    matd = rule.analyze_material('matd', env.next(stmt_iter), card, module)
    # The last card is expected to be a card 2 with matd = 0, to indicate
    # termination of unresr.
    if matd != 0:
        rule.semantic_error(msg, card)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return matd
