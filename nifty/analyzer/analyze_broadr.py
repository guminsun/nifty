from nifty.environment import helpers as env
import analyzer_rules as rule

##############################################################################
# Analyze broadr. Checks if broadr is somewhat semantically correct.

def analyze_broadr(module):
    analyze_broadr_card_list(module)
    return module

def analyze_broadr_card_list(module):
    card_iter = env.get_card_iterator(module)
    analyze_broadr_card_1(env.next(card_iter), module)
    card2, ntemp2 = analyze_broadr_card_2(env.next(card_iter), module)
    analyze_broadr_card_3(env.next(card_iter), module)
    analyze_broadr_card_4(ntemp2, env.next(card_iter), module)
    # XXX:
    # rule.no_card_allowed(env.next(card_iter), module)
    return module

def analyze_broadr_card_1(card, module):
    rule.card_must_be_defined('card_1', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    rule.analyze_unit_number('nendf', env.next(stmt_iter), card, module)
    rule.analyze_unit_number('nin', env.next(stmt_iter), card, module)
    rule.analyze_unit_number('nout', env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_broadr_card_2(card, module):
    rule.card_must_be_defined('card_2', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    rule.analyze_material('mat1', env.next(stmt_iter), card, module)
    ntemp2 = analyze_broadr_card_2_ntemp2(env.next(stmt_iter), card, module)
    analyze_broadr_card_2_istart(env.next(stmt_iter), card, module)
    analyze_broadr_card_2_istrap(env.next(stmt_iter), card, module)
    analyze_broadr_card_2_temp1(env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card, ntemp2

def analyze_broadr_card_2_ntemp2(node, card, module):
    l_value, r_value = rule.analyze_singleton(node, card, module)
    rule.identifier_must_be_defined('ntemp2', l_value, card, module)
    ntemp2 = rule.must_be_int(l_value, r_value, card, module)
    if ntemp2 < 0:
        id_name = l_value.get('name')
        msg = ('expected a non-negative number of final temperatures (\'' +
               id_name + '\') ' + 'in \'card_2\', module \'groupr\'.')
        rule.semantic_error(msg, node)
    if ntemp2 > 10:
        id_name = l_value.get('name')
        msg = ('expected at most 10 final temperatures (\'' + id_name +
               '\') ' + 'in \'card_2\', module \'groupr\'.')
        rule.semantic_error(msg, node)
    # XXX: Additional checks?
    return ntemp2

def analyze_broadr_card_2_istart(node, card, module):
    # istart does not have to be defined. Defaults to 0.
    if node is None:
        return 0
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('istart', l_value, card, module)
        istart = rule.must_be_int(l_value, r_value, card, module)
        if istart not in range(0,2):
            id_name = l_value.get('name')
            msg = ('illegal restart value in \'card_2\', module ' +
                   '\'broadr\': ' + id_name + ' = ' + str(istart) +
                   ', expected 0 (no) or 1 (yes) (default = 0).')
            rule.semantic_error(msg, node)
        # XXX: Additional checks?
        return istart

def analyze_broadr_card_2_istrap(node, card, module):
    # istrap does not have to be defined, defaults to 0.
    if node is None:
        return 0
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('istrap', l_value, card, module)
        istrap = rule.must_be_int(l_value, r_value, card, module)
        if istrap not in range(0,2):
            id_name = l_value.get('name')
            msg = ('illegal bootstrap value in \'card_2\', module ' +
                   '\'broadr\': ' + id_name + ' = ' + str(istrap) +
                   ', expected 0 (no) or 1 (yes) (default = 0).')
            rule.semantic_error(msg, node)
        # XXX: Additional checks?
        return istrap

def analyze_broadr_card_2_temp1(node, card, module):
    # Starting temperature (temp1) does not have to be defined, defaults to 0.
    if node is None:
        return 0.0
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('temp1', l_value, card, module)
        # XXX: Additional checks?
        return r_value.get('value')

def analyze_broadr_card_3(card, module):
    rule.card_must_be_defined('card_3', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    errthn = analyze_broadr_card_3_errthn(env.next(stmt_iter), card, module)
    analyze_broadr_card_3_thnmax(env.next(stmt_iter), card, module)
    analyze_broadr_card_3_errmax(errthn, env.next(stmt_iter), card, module)
    analyze_broadr_card_3_errint(errthn, env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_broadr_card_3_errthn(node, card, module):
    l_value, r_value = rule.analyze_singleton(node, card, module)
    rule.identifier_must_be_defined('errthn', l_value, card, module)
    errthn = rule.must_be_float(l_value, r_value, card, module)
    # XXX: Additional checks?
    return errthn

def analyze_broadr_card_3_thnmax(node, card, module):
    if node is None:
        return None
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('thnmax', l_value, card, module)
        # XXX: Additional checks?
        return r_value.get('value')

def analyze_broadr_card_3_errmax(errthn, node, card, module):
    # Fractional reconstruction tolerance used when resonance-integral error
    # criterion is satisfied.
    # errmax does not have to be defined, defaults to 10*errthn.
    if node is None:
        return 10*float(errthn)
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('errmax', l_value, card, module)
        # XXX: Additional checks? criterion: errmax_value >= err
        return r_value.get('value')

def analyze_broadr_card_3_errint(errthn, node, card, module):
    # Maximum resonance-integral error (in barns) per grid point.
    # errint does not have to be defined, defaults to errthn/20000.
    if node is None:
        # XXX: Will the Python float definition introduce accuracy problems?
        #      Just a heads up if this return value will be used in the
        #      translator.
        return float(errthn)/20000
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('errint', l_value, card, module)
        # XXX: Additional checks?
        return r_value.get('value')

def analyze_broadr_card_4(ntemp2, card, module):
    # Note that the number of temperatures in card 4 should be equal to the
    # number of temperatures ('ntemp2') defined in card 2.
    rule.card_must_be_defined('card_4', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    stmt_len = len(stmt_iter)
    if stmt_len == ntemp2:
        for i in range(stmt_len):
            analyze_broadr_card_4_temp2(i, env.next(stmt_iter), card, module)
    else:
        msg = ('saw ' + str(stmt_len) + ' statements in \'card_4\'' +
               ' but expected ' + str(ntemp2) + ' since ' + 'ntemp2 = ' +
               str(ntemp2) + ' in \'card_2\', module ' + '\'broadr\'.')
        rule.semantic_error(msg, card)
    return card

def analyze_broadr_card_4_temp2(expected_index, node, card, module):
    l_value, r_value = rule.analyze_singleton(node, card, module)
    # The l-value of the assignment is expected to be an array.
    expected = ('temp2', expected_index)
    rule.array_must_be_defined(expected, l_value, card, module)
    # XXX: Additional checks?
    return r_value.get('value')
