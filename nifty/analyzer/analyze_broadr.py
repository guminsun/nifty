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
    analyze_broadr_card_2(env.next(card_iter), module)
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
    analyze_broadr_card_2_ntemp2(env.next(stmt_iter), card, module)
    analyze_broadr_card_2_istart(env.next(stmt_iter), card, module)
    analyze_broadr_card_2_istrap(env.next(stmt_iter), card, module)
    analyze_broadr_card_2_temp1(env.next(stmt_iter), card, module)
    return card

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
