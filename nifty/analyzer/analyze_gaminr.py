from nifty.environment import helpers as env
import analyzer_rules as rule

##############################################################################
# Analyze gaminr. Checks if gaminr is somewhat semantically correct.

def analyze_gaminr(module):
    analyze_card_list(module)
    return module

def analyze_card_list(module):
    card_iter = env.get_card_iterator(module)
    analyze_card_1(env.next(card_iter), module)
    card_2, igg, iwt = analyze_card_2(env.next(card_iter), module)
    return module

def analyze_card_1(card, module):
    rule.card_must_be_defined('card_1', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    # Unit numbers that must be defined.
    rule.analyze_unit_number('nendf', env.next(stmt_iter), card, module)
    rule.analyze_unit_number('npend', env.next(stmt_iter), card, module)
    # Optional unit numbers.
    rule.analyze_optional_unit_number('ngam1', env.next(stmt_iter), card, module)
    rule.analyze_optional_unit_number('ngam2', env.next(stmt_iter), card, module)
    # No more statements are allowed. The next statement returned by
    # env.next(card_iter) should be 'None'.
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_card_2(card, module):
    rule.card_must_be_defined('card_2', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    rule.analyze_material('matb', env.next(stmt_iter), card, module)
    igg = analyze_card_2_igg(env.next(stmt_iter), card, module)
    iwt = analyze_card_2_iwt(env.next(stmt_iter), card, module)
    lord = analyze_card_2_lord(env.next(stmt_iter), card, module)
    analyze_card_2_iprint(env.next(stmt_iter), card, module)
    # No more statements are allowed. The next statement returned by
    # env.next(card_iter) should be 'None'.
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card, igg, iwt

def analyze_card_2_igg(node, card, module):
    l_value, r_value = rule.must_be_assignment(node, card, module)
    rule.identifier_must_be_defined('igg', l_value, card, module)
    # XXX: Additional checks? Range [0,10]
    return r_value.get('value')

def analyze_card_2_iwt(node, card, module):
    l_value, r_value = rule.must_be_assignment(node, card, module)
    rule.identifier_must_be_defined('iwt', l_value, card, module)
    iwt = rule.must_be_int(l_value, r_value, card, module)
    # XXX: Additional checks? Range [1,3]
    return iwt

def analyze_card_2_lord(node, card, module):
    l_value, r_value = rule.must_be_assignment(node, card, module)
    rule.identifier_must_be_defined('lord', l_value, card, module)
    # XXX: Additional checks? Range?
    return r_value.get('value')


def analyze_card_2_iprint(node, card, module):
    # iprint (0 = min, 1 = max) does not have to be defined, defaults to 1
    # meaning maximum print option.
    if node is None:
        return 1
    else:
        # If the node is defined, it's expected to be 'iprint'.
        l_value, r_value = rule.must_be_assignment(node, card, module)
        rule.identifier_must_be_defined('iprint', l_value, card, module)
        iprint = rule.must_be_int(l_value, r_value, card, module)
        if iprint not in range(0,2):
            id_name = l_value.get('name')
            msg = ('illegal print option in \'card_2\', module \'groupr\': ' +
                   id_name + ' = ' + str(iprint) + ', expected 0 for min, ' +
                   '1 for max (default = 1).')
            rule.semantic_error(msg, node)
        return iprint
