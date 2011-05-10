from nifty.environment import helpers as env
import analyzer_rules as rule

##############################################################################
# Analyze covr. Checks if covr is somewhat semantically correct.

def analyze_covr(module):
    analyze_covr_card_list(module)
    return module

def analyze_covr_card_list(module):
    card_iter = env.get_card_iterator(module)
    # Card 1 must always be defined.
    card_1, nout = analyze_covr_card_1(env.next(card_iter), module)
    # Card 2, 2a, and 3a should only be defined if nout <= 0.
    if nout <= 0:
        analyze_covr_card_2(env.next(card_iter), module)
        analyze_covr_card_2a(env.next(card_iter), module)
        card_3a, ncase = analyze_covr_card_3a(env.next(card_iter), module)
    # Card 2b, 3b, and 3c should only be defined if nout > 0.
    else:
        card_2b, ncase = analyze_covr_card_2b(env.next(card_iter), module)
        analyze_covr_card_3b(env.next(card_iter), module)
        analyze_covr_card_3c(env.next(card_iter), module)
    # Card 4 should be defined ncase times. XXX: Should there really be no
    # card 4 if ncase = 0?
    number_of_card_4 = len(env.get_cards('card_4', module))
    if number_of_card_4 != ncase:
        # XXX: Provide better descriptive message. Expects ncase card 4's...
        rule.too_few_cards_defined(number_of_card_4, ncase, 'card_4', module)
    for i in range(ncase):
        analyze_covr_card_4(env.next(card_iter), module)
    rule.no_card_allowed(env.next(card_iter), module)
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
    msg = ('expected \'card_2\' since nout <= 0 in \'card_1\'.')
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
    msg = ('expected \'card_2a\' since nout <= 0 in \'card_1\'.')
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

def analyze_covr_card_3a(card, module):
    msg = ('expected \'card_3a\' since nout <= 0 in \'card_1\'.')
    rule.card_must_be_defined('card_3a', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    # All values are optional.
    analyze_covr_card_3a_irelco(env.next(stmt_iter), card, module)
    ncase = analyze_covr_ncase(env.next(stmt_iter), card, module)
    analyze_covr_card_3a_noleg(env.next(stmt_iter), card, module)
    analyze_covr_card_3a_nstart(env.next(stmt_iter), card, module)
    analyze_covr_card_3a_ndiv(env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card, ncase

def analyze_covr_card_3a_irelco(node, card, module):
    # Type of covariances present on nin (irelco) does not have to be defined,
    # defaults to 1 meaning relative covariances.
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

def analyze_covr_ncase(node, card, module):
    # Number of cases to be run (ncase) does not have to be defined, defaults
    # to 1.
    if node is None:
        return 1
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('ncase', l_value, card, module)
        ncase = rule.must_be_int(l_value, r_value, card, module)
        if ncase not in range(0,61):
            id_name = l_value.get('name')
            card_name = card.get('card_name')
            module_name = module.get('module_name')
            msg = ('expected the number of cases to run (\'' + id_name +
                   '\') to be in the range [0,60] in \'' + card_name + '\'' +
                   ' module \'' + module_name + '\' (default = 1).')
            rule.semantic_error(msg, node)
    return ncase

def analyze_covr_card_3a_noleg(node, card, module):
    # Plot legend option (noleg) does not have to be defined, defaults to 0.
    if node is None:
        return 0
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('noleg', l_value, card, module)
        noleg = rule.must_be_int(l_value, r_value, card, module)
        if noleg not in range(-1,2):
            id_name = l_value.get('name')
            card_name = card.get('card_name')
            module_name = module.get('module_name')
            msg = ('illegal plot legend option (\'' + id_name + '\') in \'' +
                   card_name + '\' module \'' + module_name +
                   '\'. Expected -1 for legend for first subcase only, 0 ' + 
                   'for legend for all plots or 1 for no legends ' +
                   '(default = 0).')
            rule.semantic_error(msg, node)
    return noleg

def analyze_covr_card_3a_nstart(node, card, module):
    # Sequential figure number (nstart) does not have to be defined, defaults
    # to 1.
    if node is None:
        return 1
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('nstart', l_value, card, module)
        nstart = rule.must_be_int(l_value, r_value, card, module)
        if nstart < 0:
            id_name = l_value.get('name')
            card_name = card.get('card_name')
            module_name = module.get('module_name')
            msg = ('expected a non-negative integer for the sequential ' +
                   'figure number (\'' + id_name + '\') in \'' + card_name +
                   '\' module \'' + module_name + '\' (default = 1).')
            rule.semantic_error(msg, node)
    return nstart

def analyze_covr_card_3a_ndiv(node, card, module):
    # Number of subdivisions of each of the gray shades (ndiv) does not have
    # to be defined, defaults to 1.
    if node is None:
        return 1
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('ndiv', l_value, card, module)
        ndiv = rule.must_be_int(l_value, r_value, card, module)
        if ndiv < 0:
            id_name = l_value.get('name')
            card_name = card.get('card_name')
            module_name = module.get('module_name')
            msg = ('expected a non-negative integer for the number of ' +
                   'subdivisions of each of the gray shades (\'' + id_name +
                   '\') in \'' + card_name + '\' module \'' + module_name +
                   '\' (default = 1).')
            rule.semantic_error(msg, node)
    return ndiv

def analyze_covr_card_2b(card, module):
    msg = ('expected \'card_2b\' since nout > 0 in \'card_1\'.')
    rule.card_must_be_defined('card_2b', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    analyze_covr_card_2b_matype(env.next(stmt_iter), card, module)
    ncase = analyze_covr_ncase(env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card, ncase

def analyze_covr_card_2b_matype(node, card, module):
    # Output library matrix option (matype) does not have to be defined,
    # defaults to 3 meaning covariances.
    if node is None:
        return 3
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('matype', l_value, card, module)
        matype = rule.must_be_int(l_value, r_value, card, module)
        if matype not in range(3,5):
            id_name = l_value.get('name')
            card_name = card.get('card_name')
            module_name = module.get('module_name')
            msg = ('illegal output library matrix option (\'' + id_name +
                   '\') in \'' + card_name + '\' module \'' + module_name +
                   '\'. Expected 3 for covariances or 4 for correlations ' +
                   '(default = 3).')
            rule.semantic_error(msg, node)
    return matype

def analyze_covr_card_3b(card, module):
    msg = ('expected \'card_3b\' since nout > 0 in \'card_1\'.')
    rule.card_must_be_defined('card_3b', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    analyze_covr_card_3b_hlibid(env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_covr_card_3b_hlibid(node, card, module):
    # Identification (hlibid) must be defined?
    l_value, r_value = rule.analyze_singleton(node, card, module)
    rule.identifier_must_be_defined('hlibid', l_value, card, module)
    # The r-value of the assignment is expected to be a string.
    hlibid = rule.must_be_string(l_value, r_value, card, module)
    # The hlibid must not exceed 6 characters in length.
    rule.string_must_not_exceed_length(l_value, r_value, 6, card, module)
    return hlibid

def analyze_covr_card_3c(card, module):
    msg = ('expected \'card_3c\' since nout > 0 in \'card_1\'.')
    rule.card_must_be_defined('card_3c', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    analyze_covr_card_3c_hdescr(env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_covr_card_3c_hdescr(node, card, module):
    # Descriptive information (hdescr) must be defined?
    l_value, r_value = rule.analyze_singleton(node, card, module)
    rule.identifier_must_be_defined('hdescr', l_value, card, module)
    # The r-value of the assignment is expected to be a string.
    hdescr = rule.must_be_string(l_value, r_value, card, module)
    # The hdescr must not exceed 21 characters in length.
    rule.string_must_not_exceed_length(l_value, r_value, 21, card, module)
    return hdescr

def analyze_covr_card_4(card, module):
    rule.card_must_be_defined('card_4', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    rule.analyze_material('mat', env.next(stmt_iter), card, module)
    analyze_covr_card_4_mt(env.next(stmt_iter), card, module)
    analyze_covr_card_4_mat1(env.next(stmt_iter), card, module)
    analyze_covr_card_4_mt1(env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_covr_card_4_mt(node, card, module):
    # MT, MAT1 and MT1 does not have to be defined. They are all defaulted to
    # 0, meaning rocess all mts for this MAT with MAT1 = MAT.
    if node is None:
        return 0
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        # Don't use rule.analyze_mt here since the MT numbers are allowed to 
        # be negative (which means process all MTs for MAT, except for
        # the negative MT numbers.)
        rule.identifier_must_be_defined('mt', l_value, card, module)
        mt = rule.must_be_int(l_value, r_value, card, module)
        # XXX: Additional checks?
        return mt

def analyze_covr_card_4_mat1(node, card, module):
    # MT, MAT1 and MT1 does not have to be defined. They are all defaulted to
    # 0, meaning rocess all mts for this MAT with MAT1 = MAT.
    if node is None:
        return 0
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        # Don't use rule.analyze_mat1 here since the MAT1 numbers are allowed
        # to be negative (which means process all MAT1s for MAT, except
        # for the negative MAT1 numbers.)
        rule.identifier_must_be_defined('mat1', l_value, card, module)
        mat1 = rule.must_be_int(l_value, r_value, card, module)
        # XXX: Additional checks?
        return mat1

def analyze_covr_card_4_mt1(node, card, module):
    # MT, MAT1 and MT1 does not have to be defined. They are all defaulted to
    # 0, meaning rocess all mts for this MAT with MAT1 = MAT.
    if node is None:
        return 0
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        # Don't use rule.analyze_mt1 here since the MT1 numbers are allowed
        # to be negative (which means process all MT1s for MAT, except
        # for the negative MT1 numbers.)
        rule.identifier_must_be_defined('mt1', l_value, card, module)
        mt1 = rule.must_be_int(l_value, r_value, card, module)
        # XXX: Additional checks?
        return mt1
