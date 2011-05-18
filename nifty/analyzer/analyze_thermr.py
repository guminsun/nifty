from nifty.environment import helpers as env
import analyzer_rules as rule

##############################################################################
# Analyze thermr. Checks if thermr is somewhat semantically correct.

def analyze_thermr(module):
    analyze_thermr_card_list(module)
    return module

def analyze_thermr_card_list(module):
    card_iter = env.get_card_iterator(module)
    analyze_thermr_card_1(env.next(card_iter), module)
    card_2, ntemp = analyze_thermr_card_2(env.next(card_iter), module)
    analyze_thermr_card_3(ntemp, env.next(card_iter), module)
    analyze_thermr_card_4(env.next(card_iter), module)
    rule.no_card_allowed(env.next(card_iter), module)
    return module

def analyze_thermr_card_1(card, module):
    rule.card_must_be_defined('card_1', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    rule.analyze_unit_number('nendf', env.next(stmt_iter), card, module)
    rule.analyze_unit_number('nin', env.next(stmt_iter), card, module)
    rule.analyze_unit_number('nout', env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_thermr_card_2(card, module):
    rule.card_must_be_defined('card_2', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    rule.analyze_material('matde', env.next(stmt_iter), card, module)
    rule.analyze_material('matdp', env.next(stmt_iter), card, module)
    analyze_thermr_card_2_nbin(env.next(stmt_iter), card, module)
    ntemp = analyze_thermr_card_2_ntemp(env.next(stmt_iter), card, module)
    analyze_thermr_card_2_iinc(env.next(stmt_iter), card, module)
    analyze_thermr_card_2_icoh(env.next(stmt_iter), card, module)
    analyze_thermr_card_2_natom(env.next(stmt_iter), card, module)
    analyze_thermr_card_2_mtref(env.next(stmt_iter), card, module)
    analyze_thermr_card_2_iprint(env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card, ntemp

def analyze_thermr_card_2_nbin(node, card, module):
    # Number of equi-probable angles should be a non-negative number.
    l_value, r_value = rule.must_be_assignment(node, card, module)
    rule.identifier_must_be_defined('nbin', l_value, card, module)
    nbin = rule.must_be_int(l_value, r_value, card, module)
    if nbin < 0:
        id_name = l_value.get('name')
        card_name = card.get('card_name')
        module_name = module.get('module_name')
        msg = ('expected a non-negative number of equi-probable angles (\'' +
               id_name + '\') ' + 'in \'' + card_name + '\', module \'' +
               module_name + '\'.')
        rule.semantic_error(msg, node)
    return nbin

def analyze_thermr_card_2_ntemp(node, card, module):
    # Number of temperatures should be a non-negative number.
    l_value, r_value = rule.must_be_assignment(node, card, module)
    rule.identifier_must_be_defined('ntemp', l_value, card, module)
    ntemp = rule.must_be_int(l_value, r_value, card, module)
    if ntemp < 0:
        id_name = l_value.get('name')
        card_name = card.get('card_name')
        module_name = module.get('module_name')
        msg = ('expected a non-negative number of equi-probable angles (\'' +
               id_name + '\') ' + 'in \'' + card_name + '\', module \'' +
               module_name + '\'.')
        rule.semantic_error(msg, node)
    return ntemp

def analyze_thermr_card_2_iinc(node, card, module):
    # Inelastic option should be in the range [0,4]
    l_value, r_value = rule.must_be_assignment(node, card, module)
    rule.identifier_must_be_defined('iinc', l_value, card, module)
    iinc = rule.must_be_int(l_value, r_value, card, module)
    if iinc not in range(0,5):
        id_name = l_value.get('name')
        card_name = card.get('card_name')
        module_name = module.get('module_name')
        msg = ('illegal inelastic option in \'' + card_name + '\', module \'' +
               module_name +'\': ' + id_name + ' = ' + str(iinc) +
               ', expected an integer in the range [0,4].')
        rule.semantic_error(msg, node)
    return iinc

def analyze_thermr_card_2_icoh(node, card, module):
    # Elastic option should be in the range [0,1] or [1,3], [11,13] for
    # pre-ENDF6 input.
    # XXX: No check to determine if it's a pre-ENDF6 yet, it just checks
    # whether the number is in [0,3] or [11,13].
    l_value, r_value = rule.must_be_assignment(node, card, module)
    rule.identifier_must_be_defined('icoh', l_value, card, module)
    icoh = rule.must_be_int(l_value, r_value, card, module)
    if ((icoh not in range(0,4)) and
        (icoh not in range(11,14))):
        id_name = l_value.get('name')
        card_name = card.get('card_name')
        module_name = module.get('module_name')
        msg = ('illegal elastic option in \'' + card_name + '\', module \'' +
               module_name +'\': ' + id_name + ' = ' + str(icoh) +
               ', expected an integer in the range [0,1] (or in the range ' +
               '[1,3] or [11,13] for pre-ENDF6 input).')
        rule.semantic_error(msg, node)
    return icoh

def analyze_thermr_card_2_natom(node, card, module):
    # Number of principal atoms should be a non-negative number.
    l_value, r_value = rule.must_be_assignment(node, card, module)
    rule.identifier_must_be_defined('natom', l_value, card, module)
    natom = rule.must_be_int(l_value, r_value, card, module)
    if natom < 0:
        id_name = l_value.get('name')
        card_name = card.get('card_name')
        module_name = module.get('module_name')
        msg = ('expected a non-negative number of principal atoms (\'' +
               id_name + '\') ' + 'in \'' + card_name + '\', module \'' +
               module_name + '\'.')
        rule.semantic_error(msg, node)
    return natom

def analyze_thermr_card_2_mtref(node, card, module):
    # mt for inelastic reaction should be in the range [221,250].
    l_value, r_value = rule.must_be_assignment(node, card, module)
    rule.identifier_must_be_defined('mtref', l_value, card, module)
    mtref = rule.must_be_int(l_value, r_value, card, module)
    if mtref not in range(221,251):
        id_name = l_value.get('name')
        card_name = card.get('card_name')
        module_name = module.get('module_name')
        msg = ('expected mt (\'' + id_name + '\') for inelastic reaction ' +
               'to be in the range [221,250] in \'' + card_name +
               '\', module \'' + module_name +'\'.')
        rule.semantic_error(msg, node)
    return mtref

def analyze_thermr_card_2_iprint(node, card, module):
    # iprint does not have to be defined, defaults to 0.
    if node is None:
        return 0
    else:
        l_value, r_value = rule.must_be_assignment(node, card, module)
        rule.identifier_must_be_defined('iprint', l_value, card, module)
        iprint = rule.must_be_int(l_value, r_value, card, module)
        if iprint not in range(0,3):
            id_name = l_value.get('name')
            card_name = card.get('card_name')
            module_name = module.get('module_name')
            msg = ('illegal print option in \'' + card_name + '\', module \'' +
                   module_name + '\': ' + id_name + ' = ' + str(iprint) +
                   ', expected 0 for min, 1 for max or 2 for max. normal + ' +
                   'intermediate results (default = 0).')
            rule.semantic_error(msg, node)
    return iprint

def analyze_thermr_card_3(ntempr, card, module):
    # Note that the number of temperatures in card 3 should be equal to the
    # number of temperatures ('ntempr') defined in card 2.
    rule.card_must_be_defined('card_3', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    stmt_len = len(stmt_iter)
    if stmt_len == ntempr:
        for i in range(stmt_len):
            analyze_thermr_card_3_tempr(i, env.next(stmt_iter), card, module)
    else:
        card_name = card.get('card_name')
        module_name = module.get('module_name')
        msg = ('saw ' + str(stmt_len) + ' statement(s) in \'' + card_name +
               '\' but expected ' + str(ntempr) + ' since the number of ' +
               'temperatures (\'ntempr\') is ' + str(ntempr) + ' in ' +
               '\'card_2\', module ' + '\'' + module_name + '\'.')
        rule.semantic_error(msg, card)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_thermr_card_3_tempr(expected_index, node, card, module):
    l_value, r_value = rule.must_be_assignment(node, card, module)
    # The l-value of the assignment is expected to be an array.
    expected = ('tempr', expected_index)
    rule.array_must_be_defined(expected, l_value, card, module)
    # XXX: Additional checks?
    return r_value.get('value')

def analyze_thermr_card_4(card, module):
    rule.card_must_be_defined('card_4', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    analyze_thermr_card_4_tol(env.next(stmt_iter), card, module)
    analyze_thermr_card_4_emax(env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_thermr_card_4_tol(node, card, module):
    l_value, r_value = rule.must_be_assignment(node, card, module)
    rule.identifier_must_be_defined('tol', l_value, card, module)
    # XXX: Additional checks? Must be float?
    return r_value.get('value')

def analyze_thermr_card_4_emax(node, card, module):
    l_value, r_value = rule.must_be_assignment(node, card, module)
    rule.identifier_must_be_defined('emax', l_value, card, module)
    # XXX: Additional checks? Must be float?
    return r_value.get('value')
