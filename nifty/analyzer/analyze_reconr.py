import analyzer_helpers as helper
import analyzer_rules as rule

##############################################################################
# Analyze reconr. Checks if reconr is somewhat semantically correct.

def analyze_reconr(module):
    analyze_reconr_card_list(module)
    return 'ok'

def analyze_reconr_card_list(module):
    # Check for cards that always must be defined.
    must_be_defined = ['card_1', 'card_2', 'card_3', 'card_4']
    rule.cards_must_be_defined(must_be_defined, module)

    # Check for cards that must be unique (e.g. not defined more than once).
    unique_card_list = ['card_1', 'card_2']
    rule.cards_must_be_unique(unique_card_list, module)

    card_1 = helper.get_card('card_1', module)
    analyze_reconr_card_1(card_1, module)

    card_2 = helper.get_card('card_2', module)
    analyze_reconr_card_2(card_2, module)

    card_list_3 = helper.get_cards('card_3', module)
    card_list_4 = helper.get_cards('card_4', module)
    card_list_5 = helper.get_cards('card_5', module)
    # XXX: card_list_6 = helper.get_cards('card_6', module)

    # Cards 4 must be input for each material desired (card 3), make a simple
    # check to see if the number of cards is a 1:1 ratio. Note that the last
    # card_3, where mat = 0, should not be considered.
    cards_3_len = len(card_list_3)-1
    rule.number_of_cards_must_be(cards_3_len, 'card_4', 'card_3', module)

    # XXX: Ugly.
    for i in range(len(card_list_3)):
        # Assuming that the AST is organized. I.e. that the cards and 
        # variables are declared in the correct order.
        # For example, card_list_4[i] is the card_4 which maps to the card_3
        # in card_list_3[i].
        # XXX: Could make a check that the last card_3 in 'card_list_3' indeed
        # has a mat value equal to 0.

        analyze_reconr_card_3(card_list_3[i], module)
        # Skip the last card_3 in 'card_list_3'. I.e. break loop if mat = 0,
        # which indicates termination of execution.
        mat_node = helper.get_identifier('mat', card_list_3[i])
        mat_r_value = helper.get_value(helper.get_r_value(mat_node))
        if mat_r_value == 0:
            break

        analyze_reconr_card_4(card_list_4[i], module)

        # XXX: Ugly.
        # Note that card_5 should only be defined if ncards > 0 in card_3.
        ncards_node = helper.get_identifier('ncards', card_list_3[i])
        if helper.not_defined(ncards_node):
            ncards_r_value = 0
        else:
            ncards_r_value = helper.get_value(helper.get_r_value(ncards_node))
        if ncards_r_value > 0:
            # Extract the correct card_5 to analyze.
            for j in range(ncards_r_value):
                i5 = j*(i+1)
                # XXX: Ugly. Card 'i5' must be defined.
                try:
                    analyze_reconr_card_5(card_list_5[i5], module)
                except:
                    msg = ('expected a \'card_5\' since ncards = ' +
                           str(ncards_r_value) + ' in \'card_3\', module ' +
                           '\'' + helper.get_module_name(module) + '\'.')
                    rule.semantic_error(msg, card_list_3[i])
        else:
            msg = 'since ncards = ' + str(ncards_r_value) + ' in \'card_3\''
            rule.card_must_not_be_defined('card_5', module, msg)

    return 'ok'

def analyze_reconr_card_1(card_1, module):
    must_be_defined = ['nendf', 'npend']
    for id_name in must_be_defined:
        rule.identifier_must_be_defined(id_name, card_1, module)
        id_node = helper.get_identifier(id_name, card_1)
        rule.identifier_must_be_int(id_node)
        rule.identifier_must_be_unit_number(id_node)
    return card_1

def analyze_reconr_card_2(card_2, module):
    analyze_reconr_card_2_tlabel(card_2, module)
    return card_2

def analyze_reconr_card_2_tlabel(card_2, module):
    tlabel = rule.identifier_must_be_defined('tlabel', card_2, module)
    rule.identifier_must_be_string(tlabel, card_2, module)
    rule.identifier_string_must_not_exceed_length(tlabel, 66, card_2, module)
    return tlabel

def analyze_reconr_card_3(card_3, module):
    analyze_reconr_card_3_mat(card_3, module)
    analyze_reconr_card_3_ncards(card_3, module)
    analyze_reconr_card_3_ngrid(card_3, module)
    return card_3

def analyze_reconr_card_3_mat(card_3, module):
    mat_node = rule.identifier_must_be_defined('mat', card_3, module)
    return mat_node

def analyze_reconr_card_3_ncards(card_3, module):
    # ncards does not have to be defined, defaults to 0.
    ncards_node = helper.get_identifier('ncards', card_3)
    if helper.not_defined(ncards_node):
        return ncards_node
    else:
        rule.identifier_must_be_int(ncards_node)
        # XXX: Check if ncards is positive, negative number of cards is not a
        #      proper input.
    return ncards_node

def analyze_reconr_card_3_ngrid(card_3, module):
    # ngrid does not have to be defined, defaults to 0.
    ngrid_node = helper.get_identifier('ngrid', card_3)
    if helper.not_defined(ngrid_node):
        return ngrid_node
    else:
        rule.identifier_must_be_int(ngrid_node)
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
