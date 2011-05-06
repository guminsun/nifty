from nifty.environment import helpers as env
import analyzer_rules as rule

##############################################################################
# Analyze reconr. Checks if reconr is somewhat semantically correct.

def analyze_reconr(module):
    analyze_reconr_card_list(module)
    return module

def analyze_reconr_card_list(module):
    # Use a card iterator to check whether the cards have been defined in the
    # expected order.
    card_iter = env.get_card_iterator(module)
    # Card 1 must always be defined.
    analyze_reconr_card_1(env.next(card_iter), module)
    # Card 2 must always be defined.
    analyze_reconr_card_2(env.next(card_iter), module)
    # Number of card_3's should at least be 2 since one card 3 must always be
    # supplied, and there must be an ending card 3 (with mat = 0) to indicate 
    # termination of reconr.
    number_of_card_3 = len(env.get_cards('card_3', module))
    if number_of_card_3 < 2:
        rule.too_few_cards_defined(number_of_card_3, 2, 'card_3', module)
    # The last card 3 should not be considered, since it is expected to
    # terminate the execution of reconr (i.e. mat = 0), therefore,
    # 'number_of_card_3-1' is used to create the range to iterate over.
    for c3 in range(number_of_card_3-1):
        # Card 3 must always be defined.
        card_3, ncards, ngrid = analyze_reconr_card_3(env.next(card_iter), module)
        # Card 4 must be defined for each material desired (card 3).
        analyze_reconr_card_4(env.next(card_iter), module)
        # Card 5 must be defined 'ncards' number of times.
        for c5 in range(ncards):
            analyze_reconr_card_5(ncards, env.next(card_iter), module)
        # XXX Not sure about this; assuming that it works in the same way as
        #     for card 5:
        # Card 6 must be defined 'ngrid' number of times.
        for c6 in range(ngrid):
            analyze_reconr_card_6(ngrid, env.next(card_iter), module)
    # The last card is expected to be a card 3 with mat = 0, to indicate
    # termination of reconr.
    analyze_reconr_card_3_stop(env.next(card_iter), module)
    # No more cards are allowed. The next card returned by env.next(card_iter)
    # should be 'None'.
    rule.no_card_allowed(env.next(card_iter), module)
    return module

def analyze_reconr_card_1(card, module):
    # Card 1 must be defined.
    rule.card_must_be_defined('card_1', card, module, None)
    # Use a statement iterator to check whether the identifiers have been
    # defined in the expected order.
    stmt_iter = env.get_statement_iterator(card)
    rule.analyze_unit_number('nendf', env.next(stmt_iter), card, module)
    rule.analyze_unit_number('npend', env.next(stmt_iter), card, module)
    # No more statements are allowed. The next statement returned by
    # env.next(card_iter) should be 'None'.
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_reconr_card_2(card, module):
    # Card 2 must be defined.
    rule.card_must_be_defined('card_2', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    analyze_reconr_card_2_tlabel(env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_reconr_card_2_tlabel(node, card, module):
    l_value, r_value = rule.analyze_singleton(node, card, module)
    # The l-value of the assignment is expected to be an identifier.
    rule.identifier_must_be_defined('tlabel', l_value, card, module)
    # The r-value of the assignment is expected to be a string.
    tlabel = rule.must_be_string(l_value, r_value, card, module)
    rule.string_must_not_exceed_length(l_value, r_value, 66, card, module)
    return tlabel

def analyze_reconr_card_3(card, module):
    # Card 3 must be defined.
    rule.card_must_be_defined('card_3', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    rule.analyze_material('mat', env.next(stmt_iter), card, module)
    ncards = analyze_reconr_card_3_ncards(env.next(stmt_iter), card, module)
    ngrid = analyze_reconr_card_3_ngrid(env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card, ncards, ngrid

def analyze_reconr_card_3_ncards(node, card, module):
    # ncards does not have to be defined, defaults to 0.
    if node is None:
        return 0
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('ncards', l_value, card, module)
        ncards = rule.must_be_int(l_value, r_value, card, module)
        # ncards defines the number of cards of descriptive data for new mf1,
        # a negative value is not a valid input.
        if ncards < 0:
            id_name = l_value.get('name')
            msg = ('expected a non-negative number of cards (\'' + id_name +
                   '\') ' + 'in \'card_3\', module \'reconr\'.')
            rule.semantic_error(msg, node)
        return ncards

def analyze_reconr_card_3_ngrid(node, card, module):
    # ngrid does not have to be defined, defaults to 0.
    if node is None:
        return 0
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('ngrid', l_value, card, module)
        ngrid = rule.must_be_int(l_value, r_value, card, module)
        # ngrid defines the number of user energy grid points to be added,
        # a negative value is not a valid input.
        if ngrid < 0:
            id_name = l_value.get('name')
            msg = ('expected a non-negative number of user energy grid ' +
                   'points (\'' + id_name + '\') ' + 'in \'card_3\', ' +
                   'module \'reconr\'.')
            rule.semantic_error(msg, node)
        return ngrid

def analyze_reconr_card_3_stop(card, module):
    # Card 3 with mat = 0 must be defined.
    rule.card_must_be_defined('card_3', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    mat = rule.analyze_material('mat', env.next(stmt_iter), card, module)
    # The last card is expected to be a card 3 with mat = 0, to indicate
    # termination of reconr.
    if mat != 0:
        msg = ('expected a \'card_3\' with the material set to 0 to ' + 
               'indicate termination of module \'reconr\'.')
        rule.semantic_error(msg, card)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return mat

def analyze_reconr_card_4(card, module):
    msg = ('\'card_4\' must be defined for each material desired (card 3)')
    rule.card_must_be_defined('card_4', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    err = analyze_reconr_card_4_err(env.next(stmt_iter), card, module)
    analyze_reconr_card_4_tempr(env.next(stmt_iter), card, module)
    analyze_reconr_card_4_errmax(err, env.next(stmt_iter), card, module)
    analyze_reconr_card_4_errint(err, env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_reconr_card_4_err(node, card, module):
    # Fractional reconstruction tolerance used when resonance-integral error
    # criterion (see errint) is not satisfied.
    l_value, r_value = rule.analyze_singleton(node, card, module)
    rule.identifier_must_be_defined('err', l_value, card, module)
    err = rule.must_be_float(l_value, r_value, card, module)
    return err

def analyze_reconr_card_4_tempr(node, card, module):
    # Reconstruction temperature (degree Kelvin).
    # tempr does not have to be defined, defaults to 0.
    if node is None:
        return 0
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('tempr', l_value, card, module)
        # XXX: Additional checks?
    return r_value.get('value')

def analyze_reconr_card_4_errmax(err, node, card, module):
    # Fractional reconstruction tolerance used when resonance-integral error
    # criterion is satisfied.
    # errmax does not have to be defined, defaults to 10*err.
    if node is None:
        return 10*float(err)
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('errmax', l_value, card, module)
        # XXX: Additional checks? criterion: errmax_value >= err
    return r_value.get('value')

def analyze_reconr_card_4_errint(err, node, card, module):
    # Maximum resonance-integral error (in barns) per grid point.
    # errint does not have to be defined, defaults to err/20000.
    if node is None:
        # XXX: Will the Python float definition introduce accuracy problems?
        #      Just a heads up if this return value will be used in the
        #      translator.
        return float(err)/20000
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('errint', l_value, card, module)
        # XXX: Additional checks?
    return r_value.get('value')

def analyze_reconr_card_5(ncards, card, module):
    msg = ('expected ' + str(ncards) + ' \'card_5\'s, since ' +
           'ncards = ' + str(ncards) + ' in the current \'card_3\'.')
    rule.card_must_be_defined('card_5', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    analyze_reconr_card_5_cards(env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_reconr_card_5_cards(node, card, module):
    l_value, r_value = rule.analyze_singleton(node, card, module)
    # The l-value of the assignment is expected to be an identifier.
    rule.identifier_must_be_defined('cards', l_value, card, module)
    # The r-value of the assignment is expected to be a string.
    cards = rule.must_be_string(l_value, r_value, card, module)
    # XXX: Additional checks? Length of 'cards' limited to 80 characaters?
    return cards

def analyze_reconr_card_6(ngrid, card, module):
    msg = ('expected ' + str(ngrid) + ' \'card_6\'s, since ' +
           'ngrid = ' + str(ngrid) + ' in the current \'card_3\'.')
    rule.card_must_be_defined('card_6', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    analyze_reconr_card_6_enode(env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_reconr_card_6_enode(node, card, module):
    l_value, r_value = rule.analyze_singleton(node, card, module)
    rule.identifier_must_be_defined('enode', l_value, card, module)
    # XXX: Additional checks?
    return r_value.get('value')
