from nifty.environment import helpers as env
import analyzer_rules as rule

##############################################################################
# Analyze covr. Checks if covr is somewhat semantically correct.

def analyze_covr(module):
    analyze_covr_card_list(module)
    return module

def analyze_covr_card_list(module):
    card_iter = env.get_card_iterator(module)
    card_1, nout = analyze_covr_card_1(env.next(card_iter), module)
    # Card 2, 2a, and 3a should only be defined if nout <= 0.
    if nout <= 0:
        analyze_covr_card_2(env.next(card_iter), module)
        analyze_covr_card_2a(env.next(card_iter), module)
    # XXX: rule.no_card_allowed(env.next(card_iter), module)
    return module

def analyze_covr_card_1(card, module):
    rule.card_must_be_defined('card_1', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    rule.analyze_unit_number('nin', env.next(stmt_iter), card, module)
    nout = rule.analyze_optional_unit_number('nout', env.next(stmt_iter), card, module)
    rule.analyze_optional_unit_number('nplot', env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card, nout

def analyze_covr_card_2(card, module):
    msg = ('expected \'card_2\' since nout = 0 in \'card_1\'.')
    rule.card_must_be_defined('card_2', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    analyze_covr_card_2_icolor(env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_covr_card_2_icolor(node, card, module):
    # icolor which specifies color (1) or monochrome (0) style must not be
    # defined, defaults to 0 meaning monochrome.
    if node is None:
        return 0
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('icolor', l_value, card, module)
        icolor = rule.must_be_int(l_value, r_value, card, module)
        if icolor not in range(0,2):
            id_name = l_value.get('name')
            card_name = card.get('card_name')
            module_name = module.get('module_name')
            msg = ('illegal color value (\'' + id_name + '\') in \'' +
                   card_name + '\', module \'' + module_name + '\'.' +
                   ' Expected 0 for monochrome style or 1 for color ' +
                   'background and contours (default = 0).')
            rule.semantic_error(msg, node)
        return icolor

def analyze_covr_card_2a(card, module):
    msg = ('expected \'card_2a\' since nout = 0 in \'card_1\'.')
    rule.card_must_be_defined('card_2a', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    analyze_covr_card_2a_epmin(env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_covr_card_2a_epmin(node, card, module):
    # Lowest energy of interest (epmin) does not have to be defined, defaults
    # to 0.0.
    if node is None:
        return 0.0
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('epmin', l_value, card, module)
        # XXX: Additional checks? Must be float?
        return r_value.get('value')
