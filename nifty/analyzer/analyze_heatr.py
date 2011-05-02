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
