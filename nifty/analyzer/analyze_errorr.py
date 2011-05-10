from nifty.environment import helpers as env
import analyzer_rules as rule

##############################################################################
# Analyze errorr. Checks if errorr is somewhat semantically correct.

def analyze_errorr(module):
    analyze_errorr_card_list(module)
    return module

def analyze_errorr_card_list(module):
    card_iter = env.get_card_iterator(module)
    card_1, ngout = analyze_errorr_card_1(env.next(card_iter), module)
    card_2, ign = analyze_errorr_card_2(env.next(card_iter), module)
    # Card 3 should only be defined for ngout = 0.
    if ngout == 0:
        analyze_errorr_card_3(env.next(card_iter), module)
    # XXX: The rest of the cards depends on the ENDF file version which is
    # being used as input. The translator cannot check this as of yet, hence,
    # just pass the cards along, skipping semantic analysis for them.
    # XXX: rule.no_card_allowed(env.next(card_iter), module)

def analyze_errorr_card_1(card, module):
    rule.card_must_be_defined('card_1', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    rule.analyze_unit_number('nendf', env.next(stmt_iter), card, module)
    rule.analyze_unit_number('npend', env.next(stmt_iter), card, module)
    ngout = rule.analyze_optional_unit_number('ngout', env.next(stmt_iter), card, module)
    rule.analyze_optional_unit_number('nout', env.next(stmt_iter), card, module)
    rule.analyze_optional_unit_number('nin', env.next(stmt_iter), card, module)
    rule.analyze_optional_unit_number('nstan', env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card, ngout

def analyze_errorr_card_2(card, module):
    rule.card_must_be_defined('card_2', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    rule.analyze_material('matd', env.next(stmt_iter), card, module)
    ign = analyze_errorr_card_2_ign(env.next(stmt_iter), card, module)
    iwt = analyze_errorr_card_2_iwt(env.next(stmt_iter), card, module)
    analyze_errorr_card_2_iprint(env.next(stmt_iter), card, module)
    analyze_errorr_card_2_irelco(env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card, ign

def analyze_errorr_card_2_ign(node, card, module):
    # Neutron group option (ign) does not have to be specified, defaults to 1.
    if node is None:
        return 1
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('ign', l_value, card, module)
        ign = rule.must_be_int(l_value, r_value, card, module)
        # XXX: Additional checks? Range?
        return ign

def analyze_errorr_card_2_iwt(node, card, module):
    # Weight function option (iwt) does not have to be specified, defaults to
    # 6.
    if node is None:
        return 6
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('iwt', l_value, card, module)
        iwt = rule.must_be_int(l_value, r_value, card, module)
        # XXX: Additional checks? Range?
        return iwt

def analyze_errorr_card_2_iprint(node, card, module):
    # iprint (0 = min, 1 = max) does not have to be defined, defaults to 1
    # meaning maximum print option.
    if node is None:
        return 1
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('iprint', l_value, card, module)
        iprint = rule.must_be_int(l_value, r_value, card, module)
        if iprint not in range(0,2):
            id_name = l_value.get('name')
            card_name = card.get('card_name')
            module_name = module.get('module_name')
            msg = ('illegal print option in \'' + card_name + '\', module ' +
                   ' \'' + module_name + '\': ' + id_name + ' = ' +
                   str(iprint) + ', expected 0 for min, 1 for max ' + 
                   '(default = 1).')
            rule.semantic_error(msg, node)
        return iprint

def analyze_errorr_card_2_irelco(node, card, module):
    # Type of covariances does not have to be defined, defaults to 1 meaning
    # relative covariances.
    if node is None:
        return 1
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('irelco', l_value, card, module)
        irelco = rule.must_be_int(l_value, r_value, card, module)
        if irelco not in range(0,2):
            id_name = l_value.get('name')
            card_name = card.get('card_name')
            module_name = module.get('module_name')
            msg = ('illegal type of covariance in \'' + card_name + '\',' +
                   ' module \'' + module_name + '\': ' + id_name + ' = ' +
                   str(irelco) + ', expected 0 for absolute or 1 for relative' +
                   ' (default = 1).')
            rule.semantic_error(msg, node)
    return irelco

def analyze_errorr_card_3(card, module):
    rule.card_must_be_defined('card_3', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    # XXX: Clean print, make it general and put it in the rules module?
    analyze_errorr_card_3_mprint(env.next(stmt_iter), card, module)
    rule.analyze_temperature('tempin', env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_errorr_card_3_mprint(node, card, module):
    # Does mprint have to be defined?
    l_value, r_value = rule.analyze_singleton(node, card, module)
    rule.identifier_must_be_defined('mprint', l_value, card, module)
    mprint = rule.must_be_int(l_value, r_value, card, module)
    if mprint not in range(0,2):
        id_name = l_value.get('name')
        card_name = card.get('card_name')
        module_name = module.get('module_name')
        msg = ('illegal print option for group averaging in \'' + card_name +
               '\', module \'' + module_name + '\': ' + id_name + ' = ' +
               str(mprint) + ', expected 0 for min, 1 for max ' +
               '(default = 1).')
        rule.semantic_error(msg, node)
    return mprint
