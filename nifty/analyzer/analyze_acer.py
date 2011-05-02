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

def analyze_acer_card_1(card_1, module):
    # Card 1 must be defined.
    rule.card_must_be_defined('card_1', card_1, module, None)
    # Use a statement iterator to check whether the identifiers have been
    # defined in the expected order.
    stmt_iter = env.get_statement_iterator(card_1)
    rule.analyze_identifier_nendf(env.next(stmt_iter), card_1, module)
    rule.analyze_identifier_npend(env.next(stmt_iter), card_1, module)
    analyze_acer_card_1_ngend(env.next(stmt_iter), card_1, module)
    analyze_acer_card_1_nace(env.next(stmt_iter), card_1, module)
    analyze_acer_card_1_ndir(env.next(stmt_iter), card_1, module)
    # No more statements are allowed. The next statement returned by
    # env.next(card_iter) should be 'None'.
    rule.no_statement_allowed(env.next(stmt_iter), card_1, module)
    return card_1

def analyze_acer_card_1_ngend(node, card_1, module):
    rule.identifier_must_be_defined(('ngend', None), node, card_1, module)
    rule.identifier_must_be_int(node)
    rule.identifier_must_be_unit_number(node)
    return env.get_value(env.get_r_value(node))

def analyze_acer_card_1_nace(node, card_1, module):
    rule.identifier_must_be_defined(('nace', None), node, card_1, module)
    rule.identifier_must_be_int(node)
    rule.identifier_must_be_unit_number(node)
    return env.get_value(env.get_r_value(node))

def analyze_acer_card_1_ndir(node, card_1, module):
    rule.identifier_must_be_defined(('ndir', None), node, card_1, module)
    # XXX: 'ndir' must be a string? Pass typecheck for now.
    return env.get_value(env.get_r_value(node))

def analyze_acer_card_2(card_2, module):
    rule.card_must_be_defined('card_2', card_2, module, None)
    stmt_iter = env.get_statement_iterator(card_2)
    iopt_value = analyze_acer_card_2_iopt(env.next(stmt_iter), card_2, module)
    analyze_acer_card_2_iprint(env.next(stmt_iter), card_2, module)
    analyze_acer_card_2_ntype(env.next(stmt_iter), card_2, module)
    analyze_acer_card_2_suff(env.next(stmt_iter), card_2, module)
    nxtra_value = analyze_acer_card_2_nxtra(env.next(stmt_iter), card_2, module)
    rule.no_statement_allowed(env.next(stmt_iter), card_2, module)
    return card_2, iopt_value, nxtra_value

def analyze_acer_card_2_iopt(iopt_node, card_2, module):
    rule.identifier_must_be_defined(('iopt', None), iopt_node, card_2, module)
    rule.identifier_must_be_int(iopt_node)
    # XXX: Ugly.
    iopt_r_value = env.get_value(env.get_r_value(iopt_node))
    if ((iopt_r_value not in range(1, 6)) and
        (iopt_r_value not in range(-5, 0)) and
        (iopt_r_value not in range(7, 9)) and
        (iopt_r_value not in range(-8, -6))):
        iopt_l_value = env.get_l_value(iopt_node)
        iopt_id_name = env.get_identifier_name(iopt_l_value)
        msg = ('illegal run option in \'card_2\', module \'acer\': ' +
               iopt_id_name + ' = ' + str(iopt_r_value))
        rule.semantic_error(msg, iopt_node)
    return iopt_r_value

def analyze_acer_card_2_iprint(iprint_node, card_2, module):
    if env.not_defined(iprint_node):
        return iprint_node
    else:
        rule.identifier_must_be_defined(('iprint', None), iprint_node, card_2,
                                        module)
        rule.identifier_must_be_int(iprint_node)
        iprint_r_value = env.get_value(env.get_r_value(iprint_node))
        if iprint_r_value not in range(0,2):
            iprint_l_value = env.get_l_value(iprint_node)
            iprint_id_name = env.get_identifier_name(iprint_l_value)
            msg = ('illegal print control in \'card_2\', module \'acer\': ' +
                   iprint_id_name + ' = ' + str(iprint_r_value) +
                   ', expected 0 for min or 1 for max (default = 1).')
            rule.semantic_error(msg, iprint_node)
    return iprint_r_value

def analyze_acer_card_2_ntype(ntype_node, card_2, module):
    if env.not_defined(ntype_node):
        return ntype_node
    else:
        rule.identifier_must_be_defined(('ntype', None), ntype_node, card_2,
                                        module)
        rule.identifier_must_be_int(ntype_node)
        ntype_r_value = env.get_value(env.get_r_value(ntype_node))
        if ntype_r_value not in range(1,4):
            ntype_l_value = env.get_l_value(ntype_node)
            ntype_id_name = env.get_identifier_name(ntype_l_value)
            msg = ('illegal ace output type in \'card_2\', module \'acer\': ' +
                   ntype_id_name + ' = ' + str(ntype_r_value) +
                   ', expected 1, 2, or 3 (default = 1).')
            rule.semantic_error(msg, ntype_node)
    return ntype_r_value

def analyze_acer_card_2_suff(suff_node, card_2, module):
    if env.not_defined(suff_node):
        return suff_node
    else:
        # XXX: Check if suff_r_value is a float? Not sure it must be a float
        #      though. Pass for now.
        rule.identifier_must_be_defined(('suff', None), suff_node, card_2,
                                        module)
    return env.get_value(env.get_r_value(suff_node))

def analyze_acer_card_2_nxtra(nxtra_node, card_2, module):
    if env.not_defined(nxtra_node):
        return nxtra_node
    else:
        rule.identifier_must_be_defined(('nxtra', None), nxtra_node, card_2,
                                        module)
        rule.identifier_must_be_int(nxtra_node)
        nxtra_r_value = env.get_value(env.get_r_value(nxtra_node))
        # nxtra defines the number of iz,aw pairs to read in (default = 0), a
        # negative value does not make sense.
        if nxtra_r_value < 0:
            nxtra_l_value = env.get_l_value(nxtra_node)
            nxtra_id_name = env.get_identifier_name(nxtra_l_value)
            msg = ('the number of iz,aw pairs to read in is negative in ' +
                   '\'card_2\', module \'acer\': ' +
                   nxtra_id_name + ' = ' + str(nxtra_r_value) +
                   ', expected a non-negative value (default = 0).')
            rule.semantic_error(msg, nxtra_node)
    return nxtra_r_value

def analyze_acer_card_3(card_3, module):
    rule.card_must_be_defined('card_3', card_3, module, None)
    stmt_iter = env.get_statement_iterator(card_3)
    analyze_acer_card_3_hk(env.next(stmt_iter), card_3, module)
    rule.no_statement_allowed(env.next(stmt_iter), card_3, module)
    return card_3

def analyze_acer_card_3_hk(hk_node, card_3, module):
    rule.identifier_must_be_defined(('hk', None), hk_node, card_3, module)
    hk_r_value = rule.identifier_must_be_string(hk_node, card_3, module)
    rule.identifier_string_must_not_exceed_length(hk_node, 70, card_3, module)
    return hk_r_value

def analyze_acer_card_4(nxtra_value, card_4, module):
    # Note that card 4 should only be defined if nxtra > 0 in card_2, check if
    # it is before calling this function.
    msg = ('expected \'card_4\' since nxtra > 0 in \'card_2\'')
    rule.card_must_be_defined('card_4', card_4, module, msg)
    stmt_iter = env.get_statement_iterator(card_4)
    # XXX:
    # Assuming that pairs should be supplied as e.g. "12" (where iz = 1 and
    # aw = 2) to NJOY, in a similar manner how the "nth,ntp,nkh" triplets are
    # defined in the NJOY Test Problem 06 (plotr, card 8).
    # Unknown if all the iz,aw pairs should be defined in one card, or if one
    # card is supposed to hold only one pair. Assuming that one card holds all
    # pairs since documentation says "nxtra pairs".
    #
    # This is a dirty solution. Pairs, triplets, etc should be defined as some
    # kind of tuple node in the AST instead.
    stmt_len = len(stmt_iter)
    if stmt_len == nxtra_value:
        for i in range(stmt_len):
            analyze_acer_card_4_iz_aw(i, env.next(stmt_iter), card_4, module)
    else:
        msg = ('saw ' + str(stmt_len) + ' \'iz_aw\' pair(s) in \'card_4\'' +
               ' but expected ' + str(nxtra_value) + ' pair(s) since ' +
               'nxtra = ' + str(nxtra_value) + ' in \'card_2\', module ' +
               '\'acer\'.')
        rule.semantic_error(msg, card_4)
    return card_4

def analyze_acer_card_4_iz_aw(expected_index, iz_aw_node, card_4, module):
    rule.identifier_must_be_defined(('iz_aw', expected_index), iz_aw_node,
                                    card_4, module)
    return env.get_value(env.get_r_value(iz_aw_node))

def analyze_acer_card_5(card_5, module):
    # Note that card 5 should only be defined if iopt = 1 in card_2, check if
    # it is before calling this function.
    # Prepare a descriptive message if card_5 is not defined.
    msg = ('expected \'card_5\' since iopt = 1 in \'card_2\'')
    rule.card_must_be_defined('card_5', card_5, module, msg)
    stmt_iter = env.get_statement_iterator(card_5)
    rule.analyze_identifier_matd(env.next(stmt_iter), card_5, module)
    rule.analyze_identifier_tempd(env.next(stmt_iter), card_5, module)
    rule.no_statement_allowed(env.next(stmt_iter), card_5, module)
    return card_5

def analyze_acer_card_6(card_6, module):
    # Note that card 6 should only be defined if iopt = 1 in card_2, check if
    # it is before calling this function.
    # Prepare a descriptive message if card_6 is not defined.
    msg = ('expected \'card_6\' since iopt = 1 in \'card_2\'')
    rule.card_must_be_defined('card_6', card_6, module, msg)
    stmt_iter = env.get_statement_iterator(card_6)
    analyze_acer_card_6_newfor(env.next(stmt_iter), card_6, module)
    analyze_acer_card_6_iopp(env.next(stmt_iter), card_6, module)
    rule.no_statement_allowed(env.next(stmt_iter), card_6, module)
    return card_6

def analyze_acer_card_6_newfor(newfor_node, card_6, module):
    if env.not_defined(newfor_node):
        return None
    else:
        rule.identifier_must_be_defined(('newfor', None), newfor_node, card_6,
                                        module)
        rule.identifier_must_be_int(newfor_node)
        newfor_r_value = env.get_value(env.get_r_value(newfor_node))
        if newfor_r_value not in range(0,2):
            newfor_l_value = env.get_l_value(newfor_node)
            newfor_id_name = env.get_identifier_name(newfor_l_value)
            msg = ('illegal value in \'card_6\', module \'acer\': ' +
                   newfor_id_name + ' = ' + str(newfor_r_value) +
                   ', expected 0 or 1 (default = 1).')
            rule.semantic_error(msg, newfor_node)
    return newfor_r_value

def analyze_acer_card_6_iopp(iopp_node, card_6, module):
    if env.not_defined(iopp_node):
        return None
    else:
        rule.identifier_must_be_defined(('iopp', None), iopp_node, card_6,
                                        module)
        rule.identifier_must_be_int(iopp_node)
        iopp_r_value = env.get_value(env.get_r_value(iopp_node))
        if iopp_r_value not in range(0,2):
            iopp_l_value = env.get_l_value(iopp_node)
            iopp_id_name = env.get_identifier_name(iopp_l_value)
            msg = ('illegal value in \'card_6\', module \'acer\': ' +
                   iopp_id_name + ' = ' + str(iopp_r_value) +
                   ', expected 0 or 1 (default = 1).')
            rule.semantic_error(msg, iopp_node)
    return iopp_r_value

def analyze_acer_card_7(card_7, module):
    # Note that card 7 should only be defined if iopt = 1 in card_2, check if
    # it is before calling this function.
    # Prepare a descriptive message if card_7 is not defined.
    msg = ('expected \'card_7\' since iopt = 1 in \'card_2\'')
    rule.card_must_be_defined('card_7', card_7, module, msg)
    stmt_iter = env.get_statement_iterator(card_7)
    # XXX: Treat thin as an array instead?
    analyze_acer_card_7_thin01(env.next(stmt_iter), card_7, module)
    analyze_acer_card_7_thin02(env.next(stmt_iter), card_7, module)
    analyze_acer_card_7_thin03(env.next(stmt_iter), card_7, module)
    rule.no_statement_allowed(env.next(stmt_iter), card_7, module)
    return card_7

def analyze_acer_card_7_thin01(thin01_node, card_7, module):
    # XXX: Which type (int, float)? Specific range?
    if env.not_defined(thin01_node):
        return thin01_node
    else:
        rule.identifier_must_be_defined(('thin01', None), thin01_node, card_7,
                                        module)
    return env.get_value(env.get_r_value(thin01_node))

def analyze_acer_card_7_thin02(thin02_node, card_7, module):
    # XXX: Which type (int, float)? Specific range?
    if env.not_defined(thin02_node):
        return thin02_node
    else:
        rule.identifier_must_be_defined(('thin02', None), thin02_node, card_7,
                                        module)
    return env.get_value(env.get_r_value(thin02_node))

def analyze_acer_card_7_thin03(thin03_node, card_7, module):
    # XXX: Which type (int, float)? Specific range?
    if env.not_defined(thin03_node):
        return thin03_node
    else:
        rule.identifier_must_be_defined(('thin03', None), thin03_node, card_7,
                                        module)
    return env.get_value(env.get_r_value(thin03_node))

def analyze_acer_card_8(card_8, module):
    # Note that card 8 should only be defined if iopt = 2 in card_2, check if
    # it is before calling this function.
    # Prepare a descriptive message if card_8 is not defined.
    msg = ('expected \'card_8\' since iopt = 2 in \'card_2\'')
    rule.card_must_be_defined('card_8', card_8, module, msg)
    stmt_iter = env.get_statement_iterator(card_8)
    rule.analyze_identifier_matd(env.next(stmt_iter), card_8, module)
    rule.analyze_identifier_tempd(env.next(stmt_iter), card_8, module)
    analyze_acer_card_8_tname(env.next(stmt_iter), card_8, module)
    rule.no_statement_allowed(env.next(stmt_iter), card_8, module)
    return card_8

def analyze_acer_card_8_tname(tname_node, card_8, module):
    # Thermal zaid name (6 characters max, default = za).
    if env.not_defined(tname_node):
        return tname_node
    else:
        rule.identifier_must_be_defined(('tname', None), tname_node, card_8,
                                        module)
        rule.identifier_must_be_string(tname_node, card_8, module)
        rule.identifier_string_must_not_exceed_length(tname_node, 6, card_8,
                                                      module)
    return env.get_value(env.get_r_value(tname_node))

def analyze_acer_card_8a(card_8a, module):
    # Note that card 8a should only be defined if iopt = 2 in card_2, check if
    # it is before calling this function.
    # Prepare a descriptive message if card_8a is not defined.
    msg = ('expected \'card_8a\' since iopt = 2 in \'card_2\'')
    rule.card_must_be_defined('card_8a', card_8a, module, msg)
    stmt_iter = env.get_statement_iterator(card_8a)
    # XXX: Treat iza{01,02,03} as an array instead?
    analyze_acer_card_8a_iza01(env.next(stmt_iter), card_8a, module)
    analyze_acer_card_8a_iza02(env.next(stmt_iter), card_8a, module)
    analyze_acer_card_8a_iza03(env.next(stmt_iter), card_8a, module)
    rule.no_statement_allowed(env.next(stmt_iter), card_8a, module)
    return card_8a

def analyze_acer_card_8a_iza01(iza01_node, card_8a, module):
    # XXX: Must be an integer? Ignore for now.
    rule.identifier_must_be_defined(('iza01', None), iza01_node, card_8a,
                                    module)
    return env.get_value(env.get_r_value(iza01_node))

def analyze_acer_card_8a_iza02(iza02_node, card_8a, module):
    # iza02 does not have to be defined. Defaults to 0.
    # XXX: Must be an integer? Pass for now.
    if env.not_defined(iza02_node):
        return 0
    else:
        rule.identifier_must_be_defined(('iza02', None), iza02_node, card_8a,
                                        module)
    return env.get_value(env.get_r_value(iza02_node))

def analyze_acer_card_8a_iza03(iza03_node, card_8a, module):
    # iza03 does not have to be defined. Defaults to 0.
    # XXX: Must be an integer? Pass for now.
    if env.not_defined(iza03_node):
        return 0
    else:
        rule.identifier_must_be_defined(('iza03', None), iza03_node, card_8a,
                                        module)
    return env.get_value(env.get_r_value(iza03_node))

def analyze_acer_card_9(card_9, module):
    # Note that card 9 should only be defined if iopt = 2 in card_2, check if
    # it is before calling this function.
    # Prepare a descriptive message if card_9 is not defined.
    msg = ('expected \'card_9\' since iopt = 2 in \'card_2\'')
    rule.card_must_be_defined('card_9', card_9, module, msg)
    stmt_iter = env.get_statement_iterator(card_9)
    analyze_acer_card_9_mti(env.next(stmt_iter), card_9, module)
    analyze_acer_card_9_nbint(env.next(stmt_iter), card_9, module)
    analyze_acer_card_9_mte(env.next(stmt_iter), card_9, module)
    analyze_acer_card_9_ielas(env.next(stmt_iter), card_9, module)
    analyze_acer_card_9_nmix(env.next(stmt_iter), card_9, module)
    analyze_acer_card_9_emax(env.next(stmt_iter), card_9, module)
    analyze_acer_card_9_iwt(env.next(stmt_iter), card_9, module)
    rule.no_statement_allowed(env.next(stmt_iter), card_9, module)
    return card_9

def analyze_acer_card_9_mti(mti_node, card_9, module):
    # XXX: Type of mti? Ignore for now.
    rule.identifier_must_be_defined(('mti', None), mti_node, card_9, module)
    return env.get_value(env.get_r_value(mti_node))

def analyze_acer_card_9_nbint(nbint_node, card_9, module):
    rule.identifier_must_be_defined(('nbint', None), nbint_node, card_9,
                                    module)
    nbint_r_value = rule.identifier_must_be_int(nbint_node)
    # nbint defines the number of bins for incoherent scattering, therefore,
    # a negative value does not make sense:
    if nbint_r_value < 0:
        nbint_l_value = env.get_l_value(nbint_node)
        nbint_id_name = env.get_identifier_name(nbint_l_value)
        msg = ('the number of bins for incoherent scattering is negative ' +
               'in \'card_9\', module \'acer\': ' + nbint_id_name + ' = ' +
               str(nbint_r_value) + ', expected a non-negative value.')
        rule.semantic_error(msg, nbint_node)
    return nbint_r_value

def analyze_acer_card_9_mte(mte_node, card_9, module):
    # XXX: Type of mte? Ignore for now.
    rule.identifier_must_be_defined(('mte', None), mte_node, card_9, module)
    return env.get_value(env.get_r_value(mte_node))

def analyze_acer_card_9_ielas(ielas_node, card_9, module):
    # ielas = 0 denotes coherent elastic,
    # ielas = 1 denotes incoherent elastic.
    rule.identifier_must_be_defined(('ielas', None), ielas_node, card_9,
                                    module)
    ielas_r_value = rule.identifier_must_be_int(ielas_node)
    if ielas_r_value not in range(0,2):
        ielas_l_value = env.get_l_value(ielas_node)
        ielas_id_name = env.get_identifier_name(ielas_l_value)
        msg = ('illegal value in \'card_9\', module \'acer\': ' +
               ielas_id_name + ' = ' + str(ielas_r_value) +
               ', expected 0 or 1.')
        rule.semantic_error(msg, ielas_node)
    return ielas_r_value

def analyze_acer_card_9_nmix(nmix_node, card_9, module):
    # nmix specifies the number of atom types in mixed moderator.
    # nmix does not have to be defined, defaults to 1.
    if env.not_defined(nmix_node):
        return 1
    else:
        rule.identifier_must_be_defined(('nmix', None), nmix_node, card_9,
                                        module)
        rule.identifier_must_be_int(nmix_node)
    return env.get_value(env.get_r_value(nmix_node))

def analyze_acer_card_9_emax(emax_node, card_9, module):
    # emax specifies maximum energy for thermal treatment (ev).
    # emax does not have to be defined, defaults to 1000.0 (determined from
    # mf3, mti).
    # XXX: Type must be float? Ignore for now.
    if env.not_defined(emax_node):
        return 1000.0
    else:
        rule.identifier_must_be_defined(('emax', None), emax_node, card_9,
                                        module)
    return env.get_value(env.get_r_value(emax_node))

def analyze_acer_card_9_iwt(iwt_node, card_9, module):
    # The iwt value specifies the weighting option. It's either variable (0),
    # constant (1) or tabulated (2). Defaults to 0 (variable).
    if env.not_defined(iwt_node):
        return 0
    else:
        rule.identifier_must_be_defined(('iwt', None), iwt_node, card_9,
                                        module)
        iwt_r_value = rule.identifier_must_be_int(iwt_node)
        if iwt_r_value not in range(0,3):
            iwt_l_value = env.get_l_value(iwt_node)
            iwt_id_name = env.get_identifier_name(iwt_l_value)
            msg = ('illegal weighting option in \'card_9\', module ' +
                   '\'acer\': ' + iwt_id_name + ' = ' + str(iwt_r_value) +
                   ', expected 0, 1 or 2 (default = 0).')
            rule.semantic_error(msg, iwt_node)
    return iwt_r_value

def analyze_acer_card_10(card_10, module):
    # Note that card 10 should only be defined if iopt = 3 in card_2, check if
    # it is before calling this function.
    # Prepare a descriptive message if card_10 is not defined.
    msg = ('expected \'card_10\' since iopt = 3 in \'card_2\'')
    rule.card_must_be_defined('card_10', card_10, module, msg)
    stmt_iter = env.get_statement_iterator(card_10)
    rule.analyze_identifier_matd(env.next(stmt_iter), card_10, module)
    rule.analyze_identifier_tempd(env.next(stmt_iter), card_10, module)
    rule.no_statement_allowed(env.next(stmt_iter), card_10, module)
    return card_10

def analyze_acer_card_11(card_11, module):
    # Note that card 11 should only be defined if iopt = 4 or 5 in card_2,
    # check if it is before calling this function.
    # Prepare a descriptive message if card_11 is not defined.
    msg = ('expected \'card_11\' since iopt = 4 (or 5) in \'card_2\'')
    rule.card_must_be_defined('card_11', card_11, module, msg)
    stmt_iter = env.get_statement_iterator(card_11)
    rule.analyze_identifier_matd(env.next(stmt_iter), card_11, module)
    rule.no_statement_allowed(env.next(stmt_iter), card_11, module)
    return card_11
