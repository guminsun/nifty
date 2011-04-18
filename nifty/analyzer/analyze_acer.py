import analyzer_helpers as helper
import analyzer_rules as rule

##############################################################################
# Analyze acer. Checks if acer is semantically correct.

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
                   ', expected 0 for min or 1 for max (default=1).')
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
                   ', expected 1, 2, or 3 (default=1).')
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
                   ', expected a non-negative value (default=0).')
            rule.semantic_error(msg, nxtra_node)
        pass
    return 'ok'
