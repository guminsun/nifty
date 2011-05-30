from nifty.environment import helpers as env
import analyzer_rules as rule

from nifty.settings import acer_settings

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
    rule.card_must_be_defined('card_1', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    expected_map = acer_settings.card_1_order_map
    for i in range(len(expected_map)):
        rule.analyze_statement_E(i, expected_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_acer_card_2(card, module):
    rule.card_must_be_defined('card_2', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    expected_map = acer_settings.card_2_order_map
    for i in range(len(expected_map)):
        rule.analyze_statement_E(i, expected_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    expected_map = acer_settings.card_2_identifier_map
    iopt = env.get_identifier_value('iopt', expected_map, card)
    nxtra = env.get_identifier_value('nxtra', expected_map, card)
    return card, iopt, nxtra

def analyze_acer_card_3(card, module):
    rule.card_must_be_defined('card_3', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    expected_map = acer_settings.card_3_order_map
    for i in range(len(expected_map)):
        rule.analyze_statement_E(i, expected_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_acer_card_4(nxtra, card, module):
    # Note that card 4 should only be defined if nxtra > 0 in card_2, check if
    # it is before calling this function.
    msg = ('expected \'card_4\' since nxtra > 0 in \'card_2\'')
    rule.card_must_be_defined('card_4', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    stmt_len = len(card.get('statement_list'))
    # The expected order is unknown until nxtra has been defined. Therefore,
    # the expected order map will be determined here.
    expected_order_map = {}
    expected_identifier_map = acer_settings.card_4_identifier_map
    for i in range(0, nxtra*2, 2):
        expected_order_map[i] = expected_identifier_map['iz']
        expected_order_map[i+1] = expected_identifier_map['aw']
    for i in range(nxtra):
        rule.analyze_statement_E(i, expected_order_map.get(i*2), env.next(stmt_iter), card, module)
        rule.analyze_statement_E(i, expected_order_map.get(i*2+1), env.next(stmt_iter), card, module)
    return card

def analyze_acer_card_5(card, module):
    # Note that card 5 should only be defined if iopt = 1 in card_2, check if
    # it is before calling this function.
    msg = ('expected \'card_5\' since iopt = 1 in \'card_2\'')
    rule.card_must_be_defined('card_5', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    expected_map = acer_settings.card_5_order_map
    for i in range(len(expected_map)):
        rule.analyze_statement_E(i, expected_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_acer_card_6(card, module):
    # Note that card 6 should only be defined if iopt = 1 in card_2, check if
    # it is before calling this function.
    msg = ('expected \'card_6\' since iopt = 1 in \'card_2\'')
    rule.card_must_be_defined('card_6', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    expected_map = acer_settings.card_6_order_map
    for i in range(len(expected_map)):
        rule.analyze_statement_E(i, expected_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_acer_card_7(card, module):
    # Note that card 7 should only be defined if iopt = 1 in card_2, check if
    # it is before calling this function.
    msg = ('expected \'card_7\' since iopt = 1 in \'card_2\'')
    rule.card_must_be_defined('card_7', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    expected_map = acer_settings.card_7_order_map
    for i in range(len(expected_map)):
        rule.analyze_statement_E(i, expected_map.get(i), env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_acer_card_8(card, module):
    # Note that card 8 should only be defined if iopt = 2 in card_2, check if
    # it is before calling this function.
    msg = ('expected \'card_8\' since iopt = 2 in \'card_2\'')
    rule.card_must_be_defined('card_8', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    rule.analyze_material('matd', env.next(stmt_iter), card, module)
    rule.analyze_temperature('tempd', env.next(stmt_iter), card, module)
    analyze_acer_card_8_tname(env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_acer_card_8_tname(node, card, module):
    # Thermal zaid name (6 characters max, default = za).
    if node is None:
        return "za"
    else:
        l_value, r_value = rule.must_be_assignment(node, card, module)
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
    l_value, r_value = rule.must_be_assignment(node, card, module)
    rule.identifier_must_be_defined('iza01', l_value, card, module)
    # XXX: Must be an integer? Ignore for now.
    return r_value.get('value')

def analyze_acer_card_8a_iza02(node, card, module):
    # iza02 does not have to be defined. Defaults to 0.
    if node is None:
        return 0
    else:
        l_value, r_value = rule.must_be_assignment(node, card, module)
        rule.identifier_must_be_defined('iza02', l_value, card, module)
        # XXX: Must be an integer? Pass for now.
    return r_value.get('value')

def analyze_acer_card_8a_iza03(iza03_node, card_8a, module):
    # iza03 does not have to be defined. Defaults to 0.
    if node is None:
        return 0
    else:
        l_value, r_value = rule.must_be_assignment(node, card, module)
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
    l_value, r_value = rule.must_be_assignment(node, card, module)
    rule.identifier_must_be_defined('mti', l_value, card, module)
    # XXX: Type of mti? Ignore for now.
    return r_value.get('value')

def analyze_acer_card_9_nbint(node, card, module):
    l_value, r_value = rule.must_be_assignment(node, card, module)
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
    l_value, r_value = rule.must_be_assignment(node, card, module)
    rule.identifier_must_be_defined('mte', l_value, card, module)
    return r_value.get('value')

def analyze_acer_card_9_ielas(node, card, module):
    # ielas = 0 denotes coherent elastic,
    # ielas = 1 denotes incoherent elastic.
    l_value, r_value = rule.must_be_assignment(node, card, module)
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
        l_value, r_value = rule.must_be_assignment(node, card, module)
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
        l_value, r_value = rule.must_be_assignment(node, card, module)
        rule.identifier_must_be_defined('emax', l_value, card, module)
        # XXX: Must be float? Pass for now.
    return r_value.get('value')

def analyze_acer_card_9_iwt(node, card, module):
    # The iwt value specifies the weighting option. It's either variable (0),
    # constant (1) or tabulated (2). Defaults to 0 (variable).
    if node is None:
        return 0
    else:
        l_value, r_value = rule.must_be_assignment(node, card, module)
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
    rule.analyze_temperature('tempd', env.next(stmt_iter), card, module)
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
