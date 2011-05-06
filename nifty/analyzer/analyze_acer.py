from nifty.environment import helpers as env
import analyzer_rules as rule

##############################################################################
# Analyze acer. Checks if acer is somewhat semantically correct.

def analyze_acer(module):
    analyze_acer_card_list(module)
    return module

def analyze_acer_card_list(module):
    card_iter = env.get_card_iterator(module)
    # Card 1 should always be defined.
    analyze_acer_card_1(env.next(card_iter), module)
    # Card 2 should always be defined. 
    # Extract the identifiers iopt and nxtra from card 2 since they are used
    # to determine which cards that should be defined.
    card_2, iopt, nxtra = analyze_acer_card_2(env.next(card_iter), module)
    # Card 3 should always be defined.
    analyze_acer_card_3(env.next(card_iter), module)
    # Card 4 should only be defined if nxtra > 0 in card_2.
    if nxtra > 0:
        analyze_acer_card_4(nxtra, env.next(card_iter), module)
    # Card 5, 6 and 7 should only be defined if iopt = 1 in card_2.
    if iopt == 1:
        analyze_acer_card_5(env.next(card_iter), module)
        analyze_acer_card_6(env.next(card_iter), module)
        analyze_acer_card_7(env.next(card_iter), module)
    # Card 8, 8a and 9 should only be defined if iopt = 2 in card_2.
    if iopt == 2:
        analyze_acer_card_8(env.next(card_iter), module)
        analyze_acer_card_8a(env.next(card_iter), module)
        analyze_acer_card_9(env.next(card_iter), module)
    # Card 10 should only be defined if iopt = 3 in card_2.
    if iopt == 3:
        analyze_acer_card_10(env.next(card_iter), module)
    # Card 11 should only be defined if iopt = 4 or 5 in card_2.
    if iopt == 4 or iopt == 5:
        analyze_acer_card_11(env.next(card_iter), module)
    # No more cards are allowed. The next card returned by env.next(card_iter)
    # should be 'None'.
    rule.no_card_allowed(env.next(card_iter), module)
    return module

def analyze_acer_card_1(card, module):
    # Card 1 must be defined.
    rule.card_must_be_defined('card_1', card, module, None)
    # Use a statement iterator to check whether the identifiers have been
    # defined in the expected order.
    stmt_iter = env.get_statement_iterator(card)
    # Unit numbers that must be defined.
    rule.analyze_unit_number('nendf', env.next(stmt_iter), card, module)
    rule.analyze_unit_number('npend', env.next(stmt_iter), card, module)
    rule.analyze_unit_number('ngend', env.next(stmt_iter), card, module)
    rule.analyze_unit_number('nace', env.next(stmt_iter), card, module)
    rule.analyze_unit_number('ndir', env.next(stmt_iter), card, module)
    # No more statements are allowed. The next statement returned by
    # env.next(card_iter) should be 'None'.
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_acer_card_2(card, module):
    rule.card_must_be_defined('card_2', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    iopt = analyze_acer_card_2_iopt(env.next(stmt_iter), card, module)
    analyze_acer_card_2_iprint(env.next(stmt_iter), card, module)
    analyze_acer_card_2_ntype(env.next(stmt_iter), card, module)
    analyze_acer_card_2_suff(env.next(stmt_iter), card, module)
    nxtra = analyze_acer_card_2_nxtra(env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card, iopt, nxtra

def analyze_acer_card_2_iopt(node, card, module):
    # Expecting a singleton value.
    l_value, r_value = rule.analyze_singleton(node, card, module)
    # The l-value of the assignment is expected to be an identifier; iopt
    rule.identifier_must_be_defined('iopt', l_value, card, module)
    # The r-value of the assignment is expected to be an integer.
    iopt = rule.must_be_int(l_value, r_value, card, module)
    # XXX: Ugly:
    if ((iopt not in range(1, 6)) and
        (iopt not in range(-5, 0)) and
        (iopt not in range(7, 9)) and
        (iopt not in range(-8, -6))):
        id_name = l_value.get('name')
        msg = ('illegal run option in \'card_2\', module \'acer\': ' +
               id_name + ' = ' + str(iopt))
        rule.semantic_error(msg, l_value)
    return iopt

def analyze_acer_card_2_iprint(node, card, module):
    if node is None:
        return 1
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        # The l-value of the assignment is expected to be an identifier; iopt
        rule.identifier_must_be_defined('iprint', l_value, card, module)
        # The r-value of the assignment is expected to be an integer.
        iprint = rule.must_be_int(l_value, r_value, card, module)
        if iprint not in range(0,2):
            id_name = l_value.get('name')
            msg = ('illegal print control in \'card_2\', module \'acer\': ' +
                   id_name + ' = ' + str(iprint) +
                   ', expected 0 for min or 1 for max (default = 1).')
            rule.semantic_error(msg, node)
    return iprint

def analyze_acer_card_2_ntype(node, card, module):
    if node is None:
        return 1
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        # The l-value of the assignment is expected to be an identifier; iopt
        rule.identifier_must_be_defined('ntype', l_value, card, module)
        # The r-value of the assignment is expected to be an integer.
        ntype = rule.must_be_int(l_value, r_value, card, module)
        if ntype not in range(1,4):
            id_name = l_value.get('name')
            msg = ('illegal ace output type in \'card_2\', module \'acer\': ' +
                   id_name + ' = ' + str(ntype) +
                   ', expected 1, 2, or 3 (default = 1).')
            rule.semantic_error(msg, node)
    return ntype

def analyze_acer_card_2_suff(node, card, module):
    if node is None:
        return 0.00
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        # The l-value of the assignment is expected to be an identifier.
        rule.identifier_must_be_defined('suff', l_value, card, module)
        # XXX: Check if r_value is a float? Not sure it must be a float 
        #      though. Pass for now.
    return r_value.get('value')

def analyze_acer_card_2_nxtra(node, card, module):
    # nxtra does not have to be defined, defaults to 0.
    if node is None:
        return 0
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        # The l-value of the assignment is expected to be an identifier.
        rule.identifier_must_be_defined('nxtra', l_value, card, module)
        # The r-value of the assignment is expected to be an integer.
        nxtra = rule.must_be_int(l_value, r_value, card, module)
        # nxtra defines the number of iz,aw pairs to read in (default = 0), a
        # negative value does not make sense.
        if nxtra < 0:
            msg = ('expected a non-negative number of iz,aw pairs to read ' + 
                   'in (default = 0) in \'card_2\', module \'acer\'.')
            rule.semantic_error(msg, node)
    return nxtra

def analyze_acer_card_3(card, module):
    rule.card_must_be_defined('card_3', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    analyze_acer_card_3_hk(env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_acer_card_3_hk(node, card, module):
    l_value, r_value = rule.analyze_singleton(node, card, module)
    # The l-value of the assignment is expected to be an identifier.
    rule.identifier_must_be_defined('hk', l_value, card, module)
    # The r-value of the assignment is expected to be a string.
    hk = rule.must_be_string(l_value, r_value, card, module)
    rule.string_must_not_exceed_length(l_value, r_value, 70, card, module)
    return hk

def analyze_acer_card_4(nxtra, card, module):
    # Note that card 4 should only be defined if nxtra > 0 in card_2, check if
    # it is before calling this function.
    msg = ('expected \'card_4\' since nxtra > 0 in \'card_2\'')
    rule.card_must_be_defined('card_4', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    stmt_len = len(stmt_iter)
    if stmt_len == nxtra:
        for i in range(stmt_len):
            analyze_acer_card_4_iz_aw(i, env.next(stmt_iter), card, module)
    else:
        msg = ('saw ' + str(stmt_len) + ' statements in \'card_4\'' +
               ' but expected ' + str(nxtra) + ' since ' +
               'nxtra = ' + str(nxtra) + ' in \'card_2\', module ' +
               '\'acer\'.')
        rule.semantic_error(msg, card)
    return card

def analyze_acer_card_4_iz_aw(expected_index, node, card, module):
    l_value_pair, r_value_pair = rule.analyze_pair(node, card, module)
    expected_pair = (('iz', expected_index), ('aw', expected_index))
    rule.pair_must_be_defined(expected_pair, l_value_pair, r_value_pair, card, module)
    iz = r_value_pair[0].get('value')
    aw = r_value_pair[1].get('value')
    return iz, aw

def analyze_acer_card_5(card, module):
    # Note that card 5 should only be defined if iopt = 1 in card_2, check if
    # it is before calling this function.
    msg = ('expected \'card_5\' since iopt = 1 in \'card_2\'')
    rule.card_must_be_defined('card_5', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    rule.analyze_material('matd', env.next(stmt_iter), card, module)
    rule.analyze_identifier_tempd(env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_acer_card_6(card, module):
    # Note that card 6 should only be defined if iopt = 1 in card_2, check if
    # it is before calling this function.
    msg = ('expected \'card_6\' since iopt = 1 in \'card_2\'')
    rule.card_must_be_defined('card_6', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    analyze_acer_card_6_newfor(env.next(stmt_iter), card, module)
    analyze_acer_card_6_iopp(env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_acer_card_6_newfor(node, card, module):
    if node is None:
        return 1
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('newfor', l_value, card, module)
        newfor = rule.must_be_int(l_value, r_value, card, module)
        if newfor not in range(0,2):
            id_name = l_value.get('name')
            msg = ('illegal value in \'card_6\', module \'acer\': ' +
                   id_name + ' = ' + str(newfor) +
                   ', expected 0 or 1 (default = 1).')
            rule.semantic_error(msg, node)
    return newfor

def analyze_acer_card_6_iopp(node, card, module):
    if node is None:
        return 1
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('iopp', l_value, card, module)
        iopp = rule.must_be_int(l_value, r_value, card, module)
        if iopp not in range(0,2):
            id_name = l_value.get('name')
            msg = ('illegal value in \'card_6\', module \'acer\': ' +
                   id_name + ' = ' + str(iopp) +
                   ', expected 0 or 1 (default = 1).')
            rule.semantic_error(msg, node)
    return iopp

def analyze_acer_card_7(card, module):
    # Note that card 7 should only be defined if iopt = 1 in card_2, check if
    # it is before calling this function.
    msg = ('expected \'card_7\' since iopt = 1 in \'card_2\'')
    rule.card_must_be_defined('card_7', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    # XXX: Treat thin as an array instead?
    analyze_acer_card_7_thin01(env.next(stmt_iter), card, module)
    analyze_acer_card_7_thin02(env.next(stmt_iter), card, module)
    analyze_acer_card_7_thin03(env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_acer_card_7_thin01(node, card, module):
    if node is None:
        return None
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('thin01', l_value, card, module)
        # XXX: Which type (int, float)? Specific range?
    return r_value.get('value')

def analyze_acer_card_7_thin02(node, card, module):
    if node is None:
        return None
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('thin02', l_value, card, module)
        # XXX: Which type (int, float)? Specific range?
    return r_value.get('value')

def analyze_acer_card_7_thin03(node, card, module):
    if node is None:
        return None
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('thin03', l_value, card, module)
        # XXX: Which type (int, float)? Specific range?
    return r_value.get('value')

def analyze_acer_card_8(card, module):
    # Note that card 8 should only be defined if iopt = 2 in card_2, check if
    # it is before calling this function.
    msg = ('expected \'card_8\' since iopt = 2 in \'card_2\'')
    rule.card_must_be_defined('card_8', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    rule.analyze_material('matd', env.next(stmt_iter), card, module)
    rule.analyze_identifier_tempd(env.next(stmt_iter), card, module)
    analyze_acer_card_8_tname(env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_acer_card_8_tname(node, card, module):
    # Thermal zaid name (6 characters max, default = za).
    if node is None:
        return "za"
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('tname', l_value, card, module)
        rule.must_be_string(l_value, r_value, card, module)
        tname = rule.string_must_not_exceed_length(l_value, r_value, 6, card, module)
    return tname

def analyze_acer_card_8a(card, module):
    # Note that card 8a should only be defined if iopt = 2 in card_2, check if
    # it is before calling this function.
    msg = ('expected \'card_8a\' since iopt = 2 in \'card_2\'')
    rule.card_must_be_defined('card_8a', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    # XXX: Treat iza{01,02,03} as an array instead?
    analyze_acer_card_8a_iza01(env.next(stmt_iter), card, module)
    analyze_acer_card_8a_iza02(env.next(stmt_iter), card, module)
    analyze_acer_card_8a_iza03(env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_acer_card_8a_iza01(node, card, module):
    l_value, r_value = rule.analyze_singleton(node, card, module)
    rule.identifier_must_be_defined('iza01', l_value, card, module)
    # XXX: Must be an integer? Ignore for now.
    return r_value.get('value')

def analyze_acer_card_8a_iza02(node, card, module):
    # iza02 does not have to be defined. Defaults to 0.
    if node is None:
        return 0
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('iza02', l_value, card, module)
        # XXX: Must be an integer? Pass for now.
    return r_value.get('value')

def analyze_acer_card_8a_iza03(iza03_node, card_8a, module):
    # iza03 does not have to be defined. Defaults to 0.
    if node is None:
        return 0
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('iza03', l_value, card, module)
        # XXX: Must be an integer? Pass for now.
    return r_value.get('value')

def analyze_acer_card_9(card, module):
    # Note that card 9 should only be defined if iopt = 2 in card_2, check if
    # it is before calling this function.
    msg = ('expected \'card_9\' since iopt = 2 in \'card_2\'')
    rule.card_must_be_defined('card_9', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    analyze_acer_card_9_mti(env.next(stmt_iter), card, module)
    analyze_acer_card_9_nbint(env.next(stmt_iter), card, module)
    analyze_acer_card_9_mte(env.next(stmt_iter), card, module)
    analyze_acer_card_9_ielas(env.next(stmt_iter), card, module)
    analyze_acer_card_9_nmix(env.next(stmt_iter), card, module)
    analyze_acer_card_9_emax(env.next(stmt_iter), card, module)
    analyze_acer_card_9_iwt(env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_acer_card_9_mti(node, card, module):
    l_value, r_value = rule.analyze_singleton(node, card, module)
    rule.identifier_must_be_defined('mti', l_value, card, module)
    # XXX: Type of mti? Ignore for now.
    return r_value.get('value')

def analyze_acer_card_9_nbint(node, card, module):
    l_value, r_value = rule.analyze_singleton(node, card, module)
    rule.identifier_must_be_defined('nbint', l_value, card, module)
    nbint = rule.must_be_int(l_value, r_value, card, module)
    # nbint defines the number of bins for incoherent scattering, therefore,
    # a negative value does not make sense:
    if nbint < 0:
        id_name = l_value.get('name')
        msg = ('expected the number of bins for incoherent scattering (\'' +
               id_name + '\') to be non-negative in \'card_9\', module ' +
               '\'acer\'.')
        rule.semantic_error(msg, node)
    return nbint

def analyze_acer_card_9_mte(node, card, module):
    # XXX: Type of mte? Ignore for now.
    l_value, r_value = rule.analyze_singleton(node, card, module)
    rule.identifier_must_be_defined('mte', l_value, card, module)
    return r_value.get('value')

def analyze_acer_card_9_ielas(node, card, module):
    # ielas = 0 denotes coherent elastic,
    # ielas = 1 denotes incoherent elastic.
    l_value, r_value = rule.analyze_singleton(node, card, module)
    rule.identifier_must_be_defined('ielas', l_value, card, module)
    ielas = rule.must_be_int(l_value, r_value, card, module)
    if ielas not in range(0,2):
        id_name = l_value.get('name')
        msg = ('illegal value in \'card_9\', module \'acer\': ' + id_name +
               ' = ' + str(ielas) + ', expected 0 or 1.')
        rule.semantic_error(msg, node)
    return ielas

def analyze_acer_card_9_nmix(node, card, module):
    # nmix specifies the number of atom types in mixed moderator.
    # nmix does not have to be defined, defaults to 1.
    if node is None:
        return 1
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('nmix', l_value, card, module)
        nmix = rule.must_be_int(l_value, r_value, card, module)
        # XXX: must be non-negative?
    return nmix

def analyze_acer_card_9_emax(node, card, module):
    # emax specifies maximum energy for thermal treatment (ev).
    # emax does not have to be defined, defaults to 1000.0 (determined from
    # mf3, mti).
    if node is None:
        return 1000.0
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('emax', l_value, card, module)
        # XXX: Must be float? Pass for now.
    return r_value.get('value')

def analyze_acer_card_9_iwt(node, card, module):
    # The iwt value specifies the weighting option. It's either variable (0),
    # constant (1) or tabulated (2). Defaults to 0 (variable).
    if node is None:
        return 0
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('iwt', l_value, card, module)
        iwt = rule.must_be_int(l_value, r_value, card, module)
        if iwt not in range(0,3):
            id_name = l_value.get('name')
            msg = ('illegal weighting option in \'card_9\', module ' +
                   '\'acer\': ' + id_name + ' = ' + str(iwt) +
                   ', expected 0, 1 or 2 (default = 0).')
            rule.semantic_error(msg, node)
    return iwt

def analyze_acer_card_10(card, module):
    # Note that card 10 should only be defined if iopt = 3 in card_2, check if
    # it is before calling this function.
    msg = ('expected \'card_10\' since iopt = 3 in \'card_2\'')
    rule.card_must_be_defined('card_10', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    rule.analyze_material('matd', env.next(stmt_iter), card, module)
    rule.analyze_identifier_tempd(env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_acer_card_11(card, module):
    # Note that card 11 should only be defined if iopt = 4 or 5 in card_2,
    # check if it is before calling this function.
    msg = ('expected \'card_11\' since iopt = 4 (or 5) in \'card_2\'')
    rule.card_must_be_defined('card_11', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    rule.analyze_material('matd', env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card
