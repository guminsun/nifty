from nifty.env import nifty_helpers as helper
import analyzer_rules as rule

##############################################################################
# Analyze acer. Checks if acer is somewhat semantically correct.

def analyze_acer(module):
    analyze_acer_card_list(module)
    return module

def analyze_acer_card_list(module):
    # Check for cards that always must be defined.
    must_be_defined = ['card_1', 'card_2', 'card_3']
    rule.cards_must_be_defined(must_be_defined, module)

    # Check for cards that must be unique (e.g. not defined more than once).
    unique_card_list = ['card_1', 'card_2', 'card_3', 'card_4']
    rule.cards_must_be_unique(unique_card_list, module)

    card_1 = helper.get_card('card_1', module)
    analyze_acer_card_1(card_1, module)

    card_2 = helper.get_card('card_2', module)
    analyze_acer_card_2(card_2, module)

    card_3 = helper.get_card('card_3', module)
    analyze_acer_card_3(card_3, module)

    card_4 = helper.get_card('card_4', module)
    analyze_acer_card_4(card_2, card_4, module)

    card_5 = helper.get_card('card_5', module)
    analyze_acer_card_5(card_2, card_5, module)

    card_6 = helper.get_card('card_6', module)
    analyze_acer_card_6(card_2, card_6, module)

    card_7 = helper.get_card('card_7', module)
    analyze_acer_card_7(card_2, card_7, module)

    card_8 = helper.get_card('card_8', module)
    analyze_acer_card_8(card_2, card_8, module)

    card_8a = helper.get_card('card_8a', module)
    analyze_acer_card_8a(card_2, card_8a, module)

    card_9 = helper.get_card('card_9', module)
    analyze_acer_card_9(card_2, card_9, module)

    card_10 = helper.get_card('card_10', module)
    analyze_acer_card_10(card_2, card_10, module)

    card_11 = helper.get_card('card_11', module)
    analyze_acer_card_11(card_2, card_11, module)

    return module

def analyze_acer_card_1(card_1, module):
    must_be_defined = ['nendf', 'npend', 'ngend', 'nace', 'ndir']
    for id_name in must_be_defined:
        id_node = rule.identifier_must_be_defined(id_name, card_1, module)
        rule.identifier_must_be_int(id_node)
        rule.identifier_must_be_unit_number(id_node)
    return card_1

def analyze_acer_card_2(card_2, module):
    analyze_acer_card_2_iopt(card_2, module)
    analyze_acer_card_2_iprint(card_2, module)
    analyze_acer_card_2_ntype(card_2, module)
    analyze_acer_card_2_suff(card_2, module)
    analyze_acer_card_2_nxtra(card_2, module)
    return card_2

def analyze_acer_card_2_iopt(card_2, module):
    iopt_node = rule.identifier_must_be_defined('iopt', card_2, module)
    rule.identifier_must_be_int(iopt_node)
    # XXX: Ugly.
    iopt_r_value = helper.get_value(helper.get_r_value(iopt_node))
    if ((iopt_r_value not in range(1, 6)) and
        (iopt_r_value not in range(-5, 0)) and
        (iopt_r_value not in range(7, 9)) and
        (iopt_r_value not in range(-8, -6))):
        iopt_l_value = helper.get_l_value(iopt_node)
        iopt_id_name = helper.get_identifier_name(iopt_l_value)
        msg = ('illegal run option in \'card_2\', module \'acer\': ' +
               iopt_id_name + ' = ' + str(iopt_r_value))
        rule.semantic_error(msg, iopt_node)
    return iopt_node

def analyze_acer_card_2_iprint(card_2, module):
    iprint_node = helper.get_identifier('iprint', card_2)
    if helper.not_defined(iprint_node):
        return iprint_node
    else:
        rule.identifier_must_be_int(iprint_node)
        iprint_r_value = helper.get_value(helper.get_r_value(iprint_node))
        if iprint_r_value not in range(0,2):
            iprint_l_value = helper.get_l_value(iprint_node)
            iprint_id_name = helper.get_identifier_name(iprint_l_value)
            msg = ('illegal print control in \'card_2\', module \'acer\': ' +
                   iprint_id_name + ' = ' + str(iprint_r_value) +
                   ', expected 0 for min or 1 for max (default = 1).')
            rule.semantic_error(msg, iprint_node)
    return iprint_node

def analyze_acer_card_2_ntype(card_2, module):
    ntype_node = helper.get_identifier('ntype', card_2)
    if helper.not_defined(ntype_node):
        return ntype_node
    else:
        rule.identifier_must_be_int(ntype_node)
        ntype_r_value = helper.get_value(helper.get_r_value(ntype_node))
        if ntype_r_value not in range(1,4):
            ntype_l_value = helper.get_l_value(ntype_node)
            ntype_id_name = helper.get_identifier_name(iprint_l_value)
            msg = ('illegal ace output type in \'card_2\', module \'acer\': ' +
                   ntype_id_name + ' = ' + str(ntype_r_value) +
                   ', expected 1, 2, or 3 (default = 1).')
            rule.semantic_error(msg, ntype_node)
    return ntype_node

def analyze_acer_card_2_suff(card_2, module):
    suff_node = helper.get_identifier('suff', card_2)
    if helper.not_defined(suff_node):
        return suff_node
    else:
        # XXX: Check if suff_r_value is a float? Not sure it must be a float
        #      though. Pass for now.
        pass
    return suff_node

def analyze_acer_card_2_nxtra(card_2, module):
    nxtra_node = helper.get_identifier('nxtra', card_2)
    if helper.not_defined(nxtra_node):
        return nxtra_node
    else:
        rule.identifier_must_be_int(nxtra_node)
        nxtra_r_value = helper.get_value(helper.get_r_value(nxtra_node))
        # nxtra defines the number of iz,aw pairs to read in (default=0), a
        # negative value does not make sense.
        if nxtra_r_value < 0:
            nxtra_l_value = helper.get_l_value(nxtra_node)
            nxtra_id_name = helper.get_identifier_name(nxtra_l_value)
            msg = ('the number of iz,aw pairs to read in is negative in ' + 
                   '\'card_2\', module \'acer\': ' +
                   nxtra_id_name + ' = ' + str(nxtra_r_value) +
                   ', expected a non-negative value (default = 0).')
            rule.semantic_error(msg, nxtra_node)
    return nxtra_node

def analyze_acer_card_3(card_3, module):
    analyze_acer_card_3_hk(card_3, module)
    return card_3

def analyze_acer_card_3_hk(card_3, module):
    hk_node = rule.identifier_must_be_defined('hk', card_3, module)
    hk_r_value = rule.identifier_must_be_string(hk_node, card_3, module)
    rule.identifier_string_must_not_exceed_length(hk_node, 70, card_3, module)
    return hk_node

def analyze_acer_card_4(card_2, card_4, module):
    # Note that card 4 should only be defined if nxtra > 0 in card_2.
    nxtra_node = helper.get_identifier('nxtra', card_2)
    if helper.not_defined(nxtra_node):
        # If nxtra is not defined, then the default value is 0.
        nxtra_r_value = 0
    else:
        nxtra_r_value = helper.get_value(helper.get_r_value(nxtra_node))

    if nxtra_r_value > 0:
        msg = ('expected \'card_4\' since nxtra = ' + str(nxtra_r_value) +
               'in \'card_2\'')
        rule.card_must_be_defined('card_4', module, msg)
        analyze_acer_card_4_iz(nxtra_r_value, card_4, module)
        analyze_acer_card_4_aw(nxtra_r_value, card_4, module)
    else:
        # Supply message of why the card shouldn't be defined.
        msg = 'since nxtra = ' + str(nxtra_r_value) + ' in \'card_2\''
        rule.card_must_not_be_defined('card_4', module, msg)
    return card_4

def analyze_acer_card_4_iz(nxtra_r_value, card_4, module):
    iz_node_list = helper.get_identifiers('iz', card_4)
    if len(iz_node_list) != nxtra_r_value:
        # The number of iz values does not match the nxtra value defined in
        # card 2.
        msg = ('identifier \'iz\' declared ' + str(len(iz_node_list)) +
               ' time(s) in \'card_4\' while \'nxtra\' = ' +
               str(nxtra_r_value) + ' in \'card_2\', module \'acer\'.')
        rule.semantic_error(msg, card_4)
    return iz_node_list

def analyze_acer_card_4_aw(nxtra_r_value, card_4, module):
    aw_node_list = helper.get_identifiers('aw', card_4)
    if len(aw_node_list) != nxtra_r_value:
        # The number of aw values does not match the nxtra value defined in
        # card 2.
        msg = ('identifier \'aw\' declared ' + str(len(aw_node_list)) +
               ' time(s) in \'card_4\' while \'nxtra\' is set to ' +
               str(nxtra_r_value) + ' in \'card_2\', module \'acer\'.')
        rule.semantic_error(msg, card_4)
    return aw_node_list

def analyze_acer_card_5(card_2, card_5, module):
    # Note that card 5 should only be defined if iopt = 1 in card_2.
    iopt_node = helper.get_identifier('iopt', card_2)
    iopt_r_value = helper.get_value(helper.get_r_value(iopt_node))
    if iopt_r_value == 1:
        # Prepare a descriptive message if card_5 is not defined.
        msg = ('expected \'card_5\' since iopt = ' + str(iopt_r_value) +
               ' in \'card_2\'')
        rule.card_must_be_defined('card_5', module, msg)
        rule.analyze_identifier_matd(card_5, module)
        rule.analyze_identifier_tempd(card_5, module)
    else:
        # Prepare a descriptive message of why card_5 should not defined.
        msg = 'since iopt = ' + str(iopt_r_value) + ' in \'card_2\''
        rule.card_must_not_be_defined('card_5', module, msg)
    return card_5

def analyze_acer_card_6(card_2, card_6, module):
    # Note that card 6 should only be defined if iopt = 1 in card_2.
    iopt_node = helper.get_identifier('iopt', card_2)
    iopt_r_value = helper.get_value(helper.get_r_value(iopt_node))
    if iopt_r_value == 1:
        # Prepare a descriptive message if card_6 is not defined.
        msg = ('expected \'card_6\' since iopt = ' + str(iopt_r_value) +
               ' in \'card_2\'')
        rule.card_must_be_defined('card_6', module, msg)
        analyze_acer_card_6_newfor(card_6, module)
        analyze_acer_card_6_iopp(card_6, module)
    else:
        # Prepare a descriptive message of why card_6 should not defined.
        msg = 'since iopt = ' + str(iopt_r_value) + ' in \'card_2\''
        rule.card_must_not_be_defined('card_6', module, msg)
    return card_6

def analyze_acer_card_6_newfor(card_6, module):
    newfor_node = helper.get_identifier('newfor', card_6)
    if helper.not_defined(newfor_node):
        return newfor_node
    else:
        rule.identifier_must_be_int(newfor_node)
        newfor_r_value = helper.get_value(helper.get_r_value(newfor_node))
        if newfor_r_value not in range(0,2):
            newfor_l_value = helper.get_l_value(newfor_node)
            newfor_id_name = helper.get_identifier_name(newfor_l_value)
            msg = ('illegal value in \'card_6\', module \'acer\': ' +
                   newfor_id_name + ' = ' + str(newfor_r_value) +
                   ', expected 0 or 1 (default = 1).')
            rule.semantic_error(msg, newfor_node)
    return newfor_node

def analyze_acer_card_6_iopp(card_6, module):
    iopp_node = helper.get_identifier('iopp', card_6)
    if helper.not_defined(iopp_node):
        return iopp_node
    else:
        rule.identifier_must_be_int(iopp_node)
        iopp_r_value = helper.get_value(helper.get_r_value(iopp_node))
        if iopp_r_value not in range(0,2):
            iopp_l_value = helper.get_l_value(iopp_node)
            iopp_id_name = helper.get_identifier_name(iopp_l_value)
            msg = ('illegal value in \'card_6\', module \'acer\': ' +
                   iopp_id_name + ' = ' + str(iopp_r_value) +
                   ', expected 0 or 1 (default = 1).')
            rule.semantic_error(msg, iopp_node)
    return iopp_node

def analyze_acer_card_7(card_2, card_7, module):
    # Note that card 7 should only be defined if iopt = 1 in card_2.
    iopt_node = helper.get_identifier('iopt', card_2)
    iopt_r_value = helper.get_value(helper.get_r_value(iopt_node))
    if iopt_r_value == 1:
        # Prepare a descriptive message if card_7 is not defined.
        msg = ('expected \'card_7\' since iopt = ' + str(iopt_r_value) +
               ' in \'card_2\'')
        rule.card_must_be_defined('card_7', module, msg)
        analyze_acer_card_7_thin01(card_7, module)
        analyze_acer_card_7_thin02(card_7, module)
        analyze_acer_card_7_thin03(card_7, module)
    else:
        # Prepare a descriptive message of why card_7 should not defined.
        msg = 'since iopt = ' + str(iopt_r_value) + ' in \'card_2\''
        rule.card_must_not_be_defined('card_7', module, msg)
    return card_7

def analyze_acer_card_7_thin01(card_7, module):
    # XXX: Which type (int, float)? Specific range?
    pass

def analyze_acer_card_7_thin02(card_7, module):
    # XXX: Which type (int, float)? Specific range?
    pass

def analyze_acer_card_7_thin03(card_7, module):
    # XXX: Which type (int, float)? Specific range?
    pass

def analyze_acer_card_8(card_2, card_8, module):
    # Note that card 8 should only be defined if iopt = 2 in card_2.
    iopt_node = helper.get_identifier('iopt', card_2)
    iopt_r_value = helper.get_value(helper.get_r_value(iopt_node))
    if iopt_r_value == 2:
        # Prepare a descriptive message if card_8 is not defined.
        msg = ('expected \'card_8\' since iopt = ' + str(iopt_r_value) +
               ' in \'card_2\'')
        rule.card_must_be_defined('card_8', module, msg)
        rule.analyze_identifier_matd(card_8, module)
        rule.analyze_identifier_tempd(card_8, module)
        analyze_acer_card_8_tname(card_8, module)
    else:
        # Prepare a descriptive message of why card_8 should not defined.
        msg = 'since iopt = ' + str(iopt_r_value) + ' in \'card_2\''
        rule.card_must_not_be_defined('card_8', module, msg)
    return card_8

def analyze_acer_card_8_tname(card_8, module):
    # Thermal zaid name (6 characters max, default = za).
    tname_node = helper.get_identifier('tname', card_8)
    if helper.not_defined(tname_node):
        return tname_node
    else:
        rule.identifier_must_be_string(tname_node, card_8, module)
        rule.identifier_string_must_not_exceed_length(tname_node, 6, card_8,
                                                      module)
    return tname_node

def analyze_acer_card_8a(card_2, card_8a, module):
    # Note that card 8a should only be defined if iopt = 2 in card_2.
    iopt_node = helper.get_identifier('iopt', card_2)
    iopt_r_value = helper.get_value(helper.get_r_value(iopt_node))
    if iopt_r_value == 2:
        # Prepare a descriptive message if card_8a is not defined.
        msg = ('expected \'card_8a\' since iopt = ' + str(iopt_r_value) +
               ' in \'card_2\'')
        rule.card_must_be_defined('card_8a', module, msg)
        analyze_acer_card_8a_iza01(card_8a, module)
        analyze_acer_card_8a_iza02(card_8a, module)
        analyze_acer_card_8a_iza03(card_8a, module)
    else:
        # Prepare a descriptive message of why card_8 should not defined.
        msg = 'since iopt = ' + str(iopt_r_value) + ' in \'card_2\''
        rule.card_must_not_be_defined('card_8', module, msg)
    return card_8a

def analyze_acer_card_8a_iza01(card_8a, module):
    # XXX: Must be an integer? Ignore for now.
    iza01_node = rule.identifier_must_be_defined('iza01', card_8a, module)
    return iza01_node

def analyze_acer_card_8a_iza02(card_8a, module):
    # iza02 does not have to be defined. Defaults to 0.
    # XXX: Must be an integer? Pass for now.
    pass

def analyze_acer_card_8a_iza03(card_8a, module):
    # iza03 does not have to be defined. Defaults to 0.
    # XXX: Must be an integer? Pass for now.
    pass

def analyze_acer_card_9(card_2, card_9, module):
    # Note that card 9 should only be defined if iopt = 2 in card_2.
    iopt_node = helper.get_identifier('iopt', card_2)
    iopt_r_value = helper.get_value(helper.get_r_value(iopt_node))
    if iopt_r_value == 2:
        # Prepare a descriptive message if card_9 is not defined.
        msg = ('expected \'card_9\' since iopt = ' + str(iopt_r_value) +
               ' in \'card_2\'')
        rule.card_must_be_defined('card_9', module, msg)
        analyze_acer_card_9_mti(card_9, module)
        analyze_acer_card_9_nbint(card_9, module)
        analyze_acer_card_9_mte(card_9, module)
        analyze_acer_card_9_ielas(card_9, module)
        analyze_acer_card_9_nmix(card_9, module)
        analyze_acer_card_9_emax(card_9, module)
        analyze_acer_card_9_iwt(card_9, module)
    else:
        # Prepare a descriptive message of why card_9 should not defined.
        msg = 'since iopt = ' + str(iopt_r_value) + ' in \'card_2\''
        rule.card_must_not_be_defined('card_9', module, msg)
    return card_9

def analyze_acer_card_9_mti(card_9, module):
    # XXX: Type of mti? Ignore for now.
    mti_node = rule.identifier_must_be_defined('mti', card_9, module)
    return mti_node

def analyze_acer_card_9_nbint(card_9, module):
    nbint_node = rule.identifier_must_be_defined('nbint', card_9, module)
    nbint_r_value = rule.identifier_must_be_int(nbint_node)
    # nbint defines the number of bins for incoherent scattering, therefore, 
    # a negative value does not make sense:
    if nbint_r_value < 0:
        nbint_l_value = helper.get_l_value(nbint_node)
        nbint_id_name = helper.get_identifier_name(nbint_l_value)
        msg = ('the number of bins for incoherent scattering is negative ' + 
               'in \'card_9\', module \'acer\': ' + nbint_id_name + ' = ' +
               str(nbint_r_value) + ', expected a non-negative value.')
        rule.semantic_error(msg, nbint_node)    
    return nbint_node

def analyze_acer_card_9_mte(card_9, module):
    # XXX: Type of mte? Ignore for now.
    mte_node = rule.identifier_must_be_defined('mte', card_9, module)
    return mte_node

def analyze_acer_card_9_ielas(card_9, module):
    # ielas = 0 denotes coherent elastic, ielas = 1 denotes incoherent elastic
    ielas_node = rule.identifier_must_be_defined('ielas', card_9, module)
    ielas_r_value = rule.identifier_must_be_int(ielas_node)
    if ielas_r_value not in range(0,2):
        ielas_l_value = helper.get_l_value(ielas_node)
        ielas_id_name = helper.get_identifier_name(ielas_l_value)
        msg = ('illegal value in \'card_9\', module \'acer\': ' +
               ielas_id_name + ' = ' + str(ielas_r_value) +
               ', expected 0 or 1.')
        rule.semantic_error(msg, ielas_node)
    return ielas_node

def analyze_acer_card_9_nmix(card_9, module):
    # nmix specifies the number of atom types in mixed moderator.
    # nmix does not have to be defined, defaults to 1.
    nmix_node = helper.get_identifier('nmix', card_9)
    if helper.not_defined(nmix_node):
        return nmix_node
    else:
        nmix_r_value = rule.identifier_must_be_int(nmix_node)
    return nmix_node

def analyze_acer_card_9_emax(card_9, module):
    # emax specifies maximum energy for thermal treatment (ev).
    # emax does not have to be defined, defaults to 1000.0 (determined from
    # mf3, mti).
    # XXX: Type must be float? Ignore for now and just pass along.
    pass

def analyze_acer_card_9_iwt(card_9, module):
    # The first iwt value specifies the weighting option, the second iwt value
    # specifies whether it's variable (0), constant (1) or tabulated (2).
    # The second value does not have to be defined, defaults to 0 (variable).
    # XXX: Add the ability to specify e.g. 
    #   iwt[0] = weighting_option;
    #   iwt[1] = 0;
    # Pass for now.
    pass

def analyze_acer_card_10(card_2, card_10, module):
    # Note that card 10 should only be defined if iopt = 3 in card_2.
    iopt_node = helper.get_identifier('iopt', card_2)
    iopt_r_value = helper.get_value(helper.get_r_value(iopt_node))
    if iopt_r_value == 3:
        # Prepare a descriptive message if card_10 is not defined.
        msg = ('expected \'card_10\' since iopt = ' + str(iopt_r_value) +
               ' in \'card_2\'')
        rule.card_must_be_defined('card_10', module, msg)
        rule.analyze_identifier_matd(card_10, module)
        rule.analyze_identifier_tempd(card_10, module)
    else:
        # Prepare a descriptive message of why card_10 should not defined.
        msg = 'since iopt = ' + str(iopt_r_value) + ' in \'card_2\''
        rule.card_must_not_be_defined('card_10', module, msg)
    return card_10

def analyze_acer_card_11(card_2, card_11, module):
    # Note that card 11 should only be defined if iopt = 4 or 5 in card_2.
    iopt_node = helper.get_identifier('iopt', card_2)
    iopt_r_value = helper.get_value(helper.get_r_value(iopt_node))
    if iopt_r_value in range(4,6):
        # Prepare a descriptive message if card_11 is not defined.
        msg = ('expected \'card_11\' since iopt = ' + str(iopt_r_value) +
               ' in \'card_2\'')
        rule.card_must_be_defined('card_11', module, msg)
        rule.analyze_identifier_matd(card_11, module)
    else:
        # Prepare a descriptive message of why card_11 should not defined.
        msg = 'since iopt = ' + str(iopt_r_value) + ' in \'card_2\''
        rule.card_must_not_be_defined('card_11', module, msg)
    return card_11
