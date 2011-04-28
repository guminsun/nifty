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

def analyze_reconr_card_1(card_1, module):
    # Card 1 must be defined.
    rule.card_must_be_defined('card_1', card_1, module, None)
    # Use a statement iterator to check whether the identifiers have been
    # defined in the expected order.
    stmt_iter = env.get_statement_iterator(card_1)
    rule.analyze_identifier_nendf(env.next(stmt_iter), card_1, module)
    rule.analyze_identifier_npend(env.next(stmt_iter), card_1, module)
    # No more statements are allowed. The next statement returned by
    # env.next(card_iter) should be 'None'.
    rule.no_statement_allowed(env.next(stmt_iter), card_1, module)
    return card_1

def analyze_reconr_card_2(card_2, module):
    # Card 2 must be defined.
    rule.card_must_be_defined('card_2', card_2, module, None)
    stmt_iter = env.get_statement_iterator(card_2)
    analyze_reconr_card_2_tlabel(env.next(stmt_iter), card_2, module)
    rule.no_statement_allowed(env.next(stmt_iter), card_2, module)
    return card_2

def analyze_reconr_card_2_tlabel(tlabel_node, card_2, module):
    rule.identifier_must_be_defined(('tlabel', None), tlabel_node, card_2,
                                    module)
    rule.identifier_must_be_string(tlabel_node, card_2, module)
    rule.identifier_string_must_not_exceed_length(tlabel_node, 66, card_2,
                                                  module)
    return env.get_value(env.get_r_value(tlabel_node))

def analyze_reconr_card_3(card_3, module):
    # Card 3 must be defined.
    rule.card_must_be_defined('card_3', card_3, module, None)
    stmt_iter = env.get_statement_iterator(card_3)
    rule.analyze_identifier_matd(env.next(stmt_iter), card_3, module)
    ncards = analyze_reconr_card_3_ncards(env.next(stmt_iter), card_3, module)
    ngrid = analyze_reconr_card_3_ngrid(env.next(stmt_iter), card_3, module)
    rule.no_statement_allowed(env.next(stmt_iter), card_3, module)
    return card_3, ncards, ngrid

def analyze_reconr_card_3_ncards(ncards_node, card_3, module):
    # ncards does not have to be defined, defaults to 0.
    if env.not_defined(ncards_node):
        return 0
    else:
        rule.identifier_must_be_defined(('ncards', None), ncards_node, card_3,
                                        module)
        rule.identifier_must_be_int(ncards_node)
        # XXX: Check if ncards is positive, negative number of cards is not a
        #      proper input.
    return env.get_value(env.get_r_value(ncards_node))

def analyze_reconr_card_3_ngrid(ngrid_node, card_3, module):
    # ngrid does not have to be defined, defaults to 0.
    if env.not_defined(ngrid_node):
        return 0
    else:
        rule.identifier_must_be_defined(('ngrid', None), ngrid_node, card_3,
                                        module)
        rule.identifier_must_be_int(ngrid_node)
        # XXX: Check if ngrid is positive, negative number of grids is not a
        #      proper input.
    return env.get_value(env.get_r_value(ngrid_node))

def analyze_reconr_card_3_stop(card_3, module):
    # Card 3 with mat = 0 must be defined.
    rule.card_must_be_defined('card_3', card_3, module, None)
    stmt_iter = env.get_statement_iterator(card_3)
    mat = rule.analyze_identifier_matd(env.next(stmt_iter), card_3, module)
    # The last card is expected to be a card 3 with mat = 0, to indicate
    # termination of reconr.
    if mat != 0:
        msg = ('expected a \'card_3\' with the material set to 0 to ' + 
               'indicate termination of module \'reconr\'.')
        rule.semantic_error(msg, card_3)
    rule.no_statement_allowed(env.next(stmt_iter), card_3, module)
    return mat

def analyze_reconr_card_4(card_4, module):
    msg = ('\'card_4\' must be defined for each material desired (card 3)')
    rule.card_must_be_defined('card_4', card_4, module, msg)
    stmt_iter = env.get_statement_iterator(card_4)
    err = analyze_reconr_card_4_err(env.next(stmt_iter), card_4, module)
    analyze_reconr_card_4_tempr(env.next(stmt_iter), card_4, module)
    analyze_reconr_card_4_errmax(err, env.next(stmt_iter), card_4, module)
    analyze_reconr_card_4_errint(err, env.next(stmt_iter), card_4, module)
    rule.no_statement_allowed(env.next(stmt_iter), card_4, module)
    return card_4

def analyze_reconr_card_4_err(err_node, card_4, module):
    # Fractional reconstruction tolerance used when resonance-integral error
    # criterion (see errint) is not satisfied.
    rule.identifier_must_be_defined(('err', None), err_node, card_4, module)
    rule.identifier_must_be_float(err_node)
    return env.get_value(env.get_r_value(err_node))

def analyze_reconr_card_4_tempr(tempr_node, card_4, module):
    # Reconstruction temperature (degree Kelvin).
    # tempr does not have to be defined, defaults to 0.
    if env.not_defined(tempr_node):
        return 0
    else:
        rule.identifier_must_be_defined(('tempr', None), tempr_node, card_4,
                                        module)
    return env.get_value(env.get_r_value(tempr_node))

def analyze_reconr_card_4_errmax(err_value, errmax_node, card_4, module):
    # Fractional reconstruction tolerance used when resonance-integral error
    # criterion is satisfied.
    # errmax does not have to be defined, defaults to 10*err.
    if env.not_defined(errmax_node):
        return 10*err_value
    else:
        rule.identifier_must_be_defined(('errmax', None), errmax_node, card_4,
                                        module)
        # XXX: criterion: errmax_value >= err_value
    return env.get_value(env.get_r_value(errmax_node))

def analyze_reconr_card_4_errint(err_value, errint_node, card_4, module):
    # Maximum resonance-integral error (in barns) per grid point.
    # errint does not have to be defined, defaults to err/20000.
    if env.not_defined(errint_node):
        # XXX: Will the Python float definition introduce accuracy problems?
        #      Just a heads up if this return value will be used in the
        #      translator.
        return float(err_value)/20000
    else:
        rule.identifier_must_be_defined(('errint', None), errint_node, card_4,
                                        module)
    return env.get_value(env.get_r_value(errint_node))

def analyze_reconr_card_5(ncards_value, card_5, module):
    msg = ('expected ' + str(ncards_value) + ' \'card_5\'s, since ' +
           'ncards = ' + str(ncards_value) + ' in the current \'card_3\'.')
    rule.card_must_be_defined('card_5', card_5, module, msg)
    stmt_iter = env.get_statement_iterator(card_5)
    analyze_reconr_card_5_cards(env.next(stmt_iter), card_5, module)
    rule.no_statement_allowed(env.next(stmt_iter), card_5, module)
    return card_5

def analyze_reconr_card_5_cards(cards_node, card_5, module):
    rule.identifier_must_be_defined(('cards', None), cards_node, card_5, module)
    rule.identifier_must_be_string(cards_node, card_5, module)
    return env.get_value(env.get_r_value(cards_node))

def analyze_reconr_card_6(ngrid_value, card_6, module):
    msg = ('expected ' + str(ngrid_value) + ' \'card_6\'s, since ' +
           'ngrid = ' + str(ngrid_value) + ' in the current \'card_3\'.')
    rule.card_must_be_defined('card_6', card_6, module, msg)
    stmt_iter = env.get_statement_iterator(card_6)
    analyze_reconr_card_6_enode(env.next(stmt_iter), card_6, module)
    rule.no_statement_allowed(env.next(stmt_iter), card_6, module)
    return card_6

def analyze_reconr_card_6_enode(enode_node, card_6, module):
    rule.identifier_must_be_defined(('enode', None), enode_node, card_6, module)
    # XXX: Typecheck?
    return env.get_value(env.get_r_value(enode_node))
