import analyzer_helpers as helper
import analyzer_rules as rule

##############################################################################
# Analyze acer. Checks if acer is somewhat semantically correct.

def analyze_acer(module):
    analyze_acer_card_list(module)
    return 'ok'

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

    return 'ok'

def analyze_acer_card_1(card_1, module):
    must_be_defined = ['nendf', 'npend', 'ngend', 'nace', 'ndir']
    for id_name in must_be_defined:
        id_node = rule.identifier_must_be_defined(id_name, card_1, module)
        rule.identifier_must_be_int(id_node)
        rule.identifier_must_be_unit_number(id_node)
    return 'ok'

def analyze_acer_card_2(card_2, module):
    analyze_acer_card_2_iopt(card_2, module)
    analyze_acer_card_2_iprint(card_2, module)
    analyze_acer_card_2_ntype(card_2, module)
    analyze_acer_card_2_suff(card_2, module)
    analyze_acer_card_2_nxtra(card_2, module)
    return 'ok'

def analyze_acer_card_2_iopt(card_2, module):
    iopt_node = rule.identifier_must_be_defined('iopt', card_2, module)
    rule.identifier_must_be_int(iopt_node)
    # XXX: Ugly.
    iopt_r_value = helper.get_value(helper.get_r_value(iopt_node))
    if ((iopt_r_value not in range(1, 6)) and
        (iopt_r_value not in range(-5, 0)) and
        (iopt_r_value not in range(7, 9)) and
        (iopt_r_value not in range(-8, -6))):
        msg = ('illegal run option in \'card_2\', module \'acer\': ' +
               iopt_node['identifier'] + ' = ' + str(iopt_r_value))
        rule.semantic_error(msg, iopt_node)
    return iopt_node

def analyze_acer_card_2_iprint(card_2, module):
    iprint_node = helper.get_identifier('iprint', card_2)
    if helper.not_defined(iprint_node):
        return 'ok'
    else:
        rule.identifier_must_be_int(iprint_node)
        iprint_r_value = helper.get_value(helper.get_r_value(iprint_node))
        if iprint_r_value not in range(0,2):
            msg = ('illegal print control in \'card_2\', module \'acer\': ' +
                   iprint_node['identifier'] + ' = ' + str(iprint_r_value) +
                   ', expected 0 for min or 1 for max (default = 1).')
            rule.semantic_error(msg, iprint_node)
    return 'ok'

def analyze_acer_card_2_ntype(card_2, module):
    ntype_node = helper.get_identifier('ntype', card_2)
    if helper.not_defined(ntype_node):
        return 'ok'
    else:
        rule.identifier_must_be_int(ntype_node)
        ntype_r_value = helper.get_value(helper.get_r_value(ntype_node))
        if ntype_r_value not in range(1,4):
            msg = ('illegal ace output type in \'card_2\', module \'acer\': ' +
                   ntype_node['identifier'] + ' = ' + str(ntype_r_value) +
                   ', expected 1, 2, or 3 (default = 1).')
            rule.semantic_error(msg, ntype_node)
    return 'ok'

def analyze_acer_card_2_suff(card_2, module):
    suff_node = helper.get_identifier('suff', card_2)
    if helper.not_defined(suff_node):
        return 'ok'
    else:
        # XXX: Check if suff_r_value is a float? Not sure it must be a float
        #      though. Pass for now.
        pass
    return 'ok'

def analyze_acer_card_2_nxtra(card_2, module):
    nxtra_node = helper.get_identifier('nxtra', card_2)
    if helper.not_defined(nxtra_node):
        return 'ok'
    else:
        rule.identifier_must_be_int(nxtra_node)
        nxtra_r_value = helper.get_value(helper.get_r_value(nxtra_node))
        # nxtra defines the number of iz,aw pairs to read in (default=0), a
        # negative value does not make sense.
        if nxtra_r_value < 0:
            msg = ('the number of iz,aw pairs to read in is negative in ' + 
                   '\'card_2\', module \'acer\': ' +
                   nxtra_node['identifier'] + ' = ' + str(nxtra_r_value) +
                   ', expected a non-negative value (default = 0).')
            rule.semantic_error(msg, nxtra_node)
        pass
    return 'ok'

def analyze_acer_card_3(card_3, module):
    analyze_acer_card_3_hk(card_3, module)
    return 'ok'

def analyze_acer_card_3_hk(card_3, module):
    hk_node = rule.identifier_must_be_defined('hk', card_3, module)
    hk_r_value = rule.identifier_must_be_string(hk_node, card_3, module)
    rule.identifier_string_must_not_exceed_length(hk_node, 70, card_3, module)
    return 'ok'

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
    return 'ok'

def analyze_acer_card_4_iz(nxtra_r_value, card_4, module):
    iz_node_list = helper.get_identifiers('iz', card_4)
    if len(iz_node_list) != nxtra_r_value:
        # The number of iz values does not match the nxtra value defined in
        # card 2.
        msg = ('identifier \'iz\' declared ' + str(len(iz_node_list)) +
               ' time(s) in \'card_4\' while \'nxtra\' = ' +
               str(nxtra_r_value) + ' in \'card_2\', module \'acer\'.')
        rule.semantic_error(msg, card_4)
    return 'ok'

def analyze_acer_card_4_aw(nxtra_r_value, card_4, module):
    aw_node_list = helper.get_identifiers('aw', card_4)
    if len(aw_node_list) != nxtra_r_value:
        # The number of aw values does not match the nxtra value defined in
        # card 2.
        msg = ('identifier \'aw\' declared ' + str(len(aw_node_list)) +
               ' time(s) in \'card_4\' while \'nxtra\' is set to ' +
               str(nxtra_r_value) + ' in \'card_2\', module \'acer\'.')
        rule.semantic_error(msg, card_4)
    return 'ok'

def analyze_acer_card_5(card_2, card_5, module):
    # Note that card 5 should only be defined if iopt = 1 in card_2.
    iopt_node = helper.get_identifier('iopt', card_2)
    iopt_r_value = helper.get_value(helper.get_r_value(iopt_node))
    if iopt_r_value == 1:
        # Prepare a descriptive message if card_5 is not defined.
        msg = ('expected \'card_5\' since iopt = ' + str(iopt_r_value) +
               ' in \'card_2\'')
        rule.card_must_be_defined('card_5', module, msg)
        analyze_acer_card_5_matd(card_5, module)
        analyze_acer_card_5_tempd(card_5, module)
    else:
        # Prepare a descriptive message of why card_5 should not defined.
        msg = 'since iopt = ' + str(iopt_r_value) + ' in \'card_2\''
        rule.card_must_not_be_defined('card_5', module, msg)
    return 'ok'

def analyze_acer_card_5_matd(card_5, module):
    rule.identifier_must_be_defined('matd', card_5, module)
    return 'ok'

def analyze_acer_card_5_tempd(card_5, module):
    rule.identifier_must_be_defined('tempd', card_5, module)
    return 'ok'

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
        rule.card_must_not_be_defined('card_5', module, msg)
    return 'ok'

def analyze_acer_card_6_newfor(card_6, module):
    newfor_node = helper.get_identifier('newfor', card_6)
    if helper.not_defined(newfor_node):
        return 'ok'
    else:
        rule.identifier_must_be_int(newfor_node)
        newfor_r_value = helper.get_value(helper.get_r_value(newfor_node))
        if newfor_r_value not in range(0,2):
            msg = ('illegal value in \'card_6\', module \'acer\': ' +
                   newfor_node['identifier'] + ' = ' + str(newfor_r_value) +
                   ', expected 0 or 1 (default = 1).')
            rule.semantic_error(msg, newfor_node)
    return 'ok'

def analyze_acer_card_6_iopp(card_6, module):
    iopp_node = helper.get_identifier('iopp', card_6)
    if helper.not_defined(iopp_node):
        return 'ok'
    else:
        rule.identifier_must_be_int(iopp_node)
        iopp_r_value = helper.get_value(helper.get_r_value(iopp_node))
        if iopp_r_value not in range(0,2):
            msg = ('illegal value in \'card_6\', module \'acer\': ' +
                   iopp_node['identifier'] + ' = ' + str(iopp_r_value) +
                   ', expected 0 or 1 (default = 1).')
            rule.semantic_error(msg, iopp_node)
    return 'ok'

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
    return 'ok'

def analyze_acer_card_7_thin01(card_7, module):
    # XXX: Which type (int, float)? Specific range?
    pass

def analyze_acer_card_7_thin02(card_7, module):
    # XXX: Which type (int, float)? Specific range?
    pass

def analyze_acer_card_7_thin03(card_7, module):
    # XXX: Which type (int, float)? Specific range?
    pass
