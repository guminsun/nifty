from nifty.environment import helpers as env
import analyzer_rules as rule

##############################################################################
# Analyze reconr. Checks if reconr is somewhat semantically correct.

def analyze_reconr(module):
    analyze_reconr_card_list(module)
    return module

def analyze_reconr_card_list(module):
    # Check for cards that always must be defined.
    must_be_defined = ['card_1', 'card_2', 'card_3', 'card_4']
    rule.cards_must_be_defined(must_be_defined, module)

    # Check for cards that must be unique (e.g. not defined more than once).
    unique_card_list = ['card_1', 'card_2']
    rule.cards_must_be_unique(unique_card_list, module)

    card_1 = env.get_card('card_1', module)
    analyze_reconr_card_1(card_1, module)

    card_2 = env.get_card('card_2', module)
    analyze_reconr_card_2(card_2, module)

    card_list_3 = env.get_cards('card_3', module)
    card_list_4 = env.get_cards('card_4', module)
    card_list_5 = env.get_cards('card_5', module)
    card_list_6 = env.get_cards('card_6', module)

    # Cards 4 must be input for each material desired (card 3), make a simple
    # check to see if the number of cards is a 1:1 ratio. Note that the last
    # card_3, where mat = 0, should not be considered.
    cards_3_len = len(card_list_3)-1
    rule.number_of_cards_must_be(cards_3_len, 'card_4', 'card_3', module)

    # XXX: Ugly.
    for i in range(len(card_list_3)):

        analyze_reconr_card_3(card_list_3[i], module)
        # Skip the checks of card 4,5,6 if the current 'card_3' is the last.
        # I.e. break loop if mat = 0, which indicate termination of execution.
        mat_node = env.get_identifier('mat', card_list_3[i])
        mat_r_value = env.get_value(env.get_r_value(mat_node))
        if mat_r_value == 0:
            break

#        analyze_reconr_card_4(card_list_4[i], module)
#
#        # XXX: Ugly.
#        # Note that card_5 should only be defined if ncards > 0 in card_3.
#        ncards_node = env.get_identifier('ncards', card_list_3[i])
#        if env.not_defined(ncards_node):
#            ncards_r_value = 0
#        else:
#            ncards_r_value = env.get_value(env.get_r_value(ncards_node))
#        c5_start = i*ncards_r_value
#        c5_end = c5_start+ncards_r_value
#        if ncards_r_value > 0:
#            # XXX: Check that the number of cards are correct? Assume they are
#            #      for now.
#            # Extract the correct card_5(s) to analyze.
#            for j in range(c5_start, c5_end):
#                # XXX: Ugly. 'card_list_5[j]' must be defined.
#                try:
#                    analyze_reconr_card_5(card_list_5[j], module)
#                except:
#                    msg = ('expected a \'card_5\' since ncards = ' +
#                           str(ncards_r_value) + ' in \'card_3\', module ' +
#                           '\'' + env.get_module_name(module) + '\'.')
#                    rule.semantic_error(msg, card_list_3[i])
#        else:
#            if len(card_list_5) > c5_start:
#                msg = ('unexpected definition of card \'card_5\' in module \'' +
#                       env.get_module_name(module) + '\' (since ncards = ' +
#                       str(ncards_r_value) + ' in \'card_3\').')
#                rule.semantic_error(msg, card_list_3[i])
#
#        # XXX: Ugly.
#        # Note that card_6 should only be defined if ngrid > 0 in card_3.
#        ngrid_node = env.get_identifier('ngrid', card_list_3[i])
#        if env.not_defined(ngrid_node):
#            ngrid_r_value = 0
#        else:
#            ngrid_r_value = env.get_value(env.get_r_value(ngrid_node))
#        c6_start = i*ngrid_r_value
#        c6_end = c6_start+ngrid_r_value
#        if ngrid_r_value > 0:
#            # XXX: Check that the number of cards are correct? Assume they are
#            #      for now.
#            # Extract the correct card_6(s) to analyze.
#            for j in range(c6_start, c6_end):
#                # XXX: Ugly. 'card_list_6[j]' must be defined.
#                try:
#                    analyze_reconr_card_6(card_list_6[j], module)
#                except:
#                    msg = ('expected a \'card_6\' since ngrid = ' +
#                           str(ngrid_r_value) + ' in \'card_3\', module ' +
#                           '\'' + env.get_module_name(module) + '\'.')
#                    rule.semantic_error(msg, card_list_3[i])
#        else:
#            if len(card_list_6) > c6_start:
#                msg = ('unexpected definition of card \'card_6\' in module \'' +
#                       env.get_module_name(module) + '\' (since ngrid = ' +
#                       str(ngrid_r_value) + ' in \'card_3\').')
#                rule.semantic_error(msg, card_list_3[i])
#
    return module

def analyze_reconr_card_1(card_1, module):
    stmt_iter = env.get_statement_iterator(card_1)
    rule.analyze_identifier_nendf(env.next(stmt_iter), card_1, module)
    rule.analyze_identifier_npend(env.next(stmt_iter), card_1, module)
    rule.no_more_statement_allowed(env.next(stmt_iter), card_1, module)
    return card_1

def analyze_reconr_card_2(card_2, module):
    stmt_iter = env.get_statement_iterator(card_2)
    analyze_reconr_card_2_tlabel(env.next(stmt_iter), card_2, module)
    rule.no_more_statement_allowed(env.next(stmt_iter), card_2, module)
    return card_2

def analyze_reconr_card_2_tlabel(tlabel_node, card_2, module):
    rule.identifier_must_be_defined(('tlabel', None), tlabel_node, card_2,
                                    module)
    rule.identifier_must_be_string(tlabel_node, card_2, module)
    rule.identifier_string_must_not_exceed_length(tlabel_node, 66, card_2,
                                                  module)
    return tlabel_node

def analyze_reconr_card_3(card_3, module):
    stmt_iter = env.get_statement_iterator(card_3)
    analyze_reconr_card_3_mat(env.next(stmt_iter), card_3, module)
    analyze_reconr_card_3_ncards(env.next(stmt_iter), card_3, module)
    analyze_reconr_card_3_ngrid(env.next(stmt_iter), card_3, module)
    rule.no_more_statement_allowed(env.next(stmt_iter), card_3, module)
    return card_3

def analyze_reconr_card_3_mat(mat_node, card_3, module):
    rule.identifier_must_be_defined(('mat', None), mat_node, card_3, module)
    return mat_node

def analyze_reconr_card_3_ncards(ncards_node, card_3, module):
    # ncards does not have to be defined, defaults to 0.
    if env.not_defined(ncards_node):
        return ncards_node
    else:
        rule.identifier_must_be_defined(('ncards', None), ncards_node, card_3,
                                        module)
        rule.identifier_must_be_int(ncards_node)
        # XXX: Check if ncards is positive, negative number of cards is not a
        #      proper input.
    return ncards_node

def analyze_reconr_card_3_ngrid(ngrid_node, card_3, module):
    # ngrid does not have to be defined, defaults to 0.
    if env.not_defined(ngrid_node):
        return ngrid_node
    else:
        rule.identifier_must_be_defined(('ngrid', None), ngrid_node, card_3,
                                        module)
        # XXX: Check if ngrid is positive, negative number of grids is not a
        #      proper input.
    return ngrid_node

def analyze_reconr_card_4(card_4, module):
    err_node = rule.identifier_must_be_defined('err', card_4, module)
    rule.identifier_must_be_float(err_node)
    # XXX: Check tempr, errmax, errint if they are defined.
    return card_4

def analyze_reconr_card_5(card_5, module):
    analyze_reconr_card_5_cards(card_5, module)
    return card_5

def analyze_reconr_card_5_cards(card_5, module):
    cards_node = rule.identifier_must_be_defined('cards', card_5, module)
    rule.identifier_must_be_string(cards_node, card_5, module)

def analyze_reconr_card_6(card_6, module):
    # XXX: Check that the number of enode's corresponds to the ngrid value
    #      defined in card_3
    return card_6
