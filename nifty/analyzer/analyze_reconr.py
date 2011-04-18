import analyzer_helpers as helper
import analyzer_rules as rule

##############################################################################
# Analyze reconr.

def analyze_reconr(module):
    analyze_reconr_card_list(module)
    return 'ok'

def analyze_reconr_card_list(module):
    # Check for cards that always must be defined.
    must_be_defined = ['card_1', 'card_2', 'card_3', 'card_4']
    rule.cards_must_be_defined(must_be_defined, module)

    # Check for cards that must be unique (e.g. not defined more than once).
    unique_card_list = ['card_1', 'card_2', 'card_4']
    rule.cards_must_be_unique(unique_card_list, module)

    card_1 = helper.get_card('card_1', module)
    analyze_reconr_card_1(card_1, module)

    card_2 = helper.get_card('card_2', module)
    analyze_reconr_card_2(card_2, module)

    # XXX: Needs serious cleaning.
    # Cards 3, 4, 5, 6 must be input for each material desired.
    cards_3 = helper.get_cards('card_3', module)
    for card_3 in cards_3:
        analyze_reconr_card_3(card_3, module)
        
        # Break loop if mat = 0, which indicates termination of execution.
        mat = helper.get_identifier('mat', card_3)
        mat_value = helper.get_value(helper.get_r_value(mat))
        if mat_value == 0:
            break

        card_4 = helper.get_card('card_4', module)
        analyze_reconr_card_4(card_4, module)

        # card_5 must be defined 'ncards' times for each card_3 (see card 3).
        ncards = helper.get_identifier('ncards', card_3)
        if helper.not_defined(ncards):
            ncards_value = 0
        else:
            ncards_value = helper.get_value(helper.get_r_value(ncards))
        cards_5 = helper.get_cards('card_5', module)
        if len(cards_5) != ncards_value:
            # Number of card_5 does not match ncards definition in card 3. 
            msg = ('\'card_5\' declared ' + str(len(cards_5)) + ' time(s) ' + 
                   'while \'ncards\' is set to ' + str(ncards_value) +
                   ' in \'card_3\', module \'reconr\'.')
            rule.semantic_error(msg, module)
        for card_5 in cards_5:
            analyze_reconr_card_5(card_5, module)

        # card_6 must be defined 'ngrid' times for each card_3 (see card 3).
        ngrid = helper.get_identifier('ngrid', card_3)
        if helper.not_defined(ngrid):
            ngrid_value = 0
        else:
            ngrid_value = helper.get_value(helper.get_r_value(ngrid))
        cards_6 = helper.get_cards('card_6', module)
        if len(cards_6) != ngrid_value:
            # Number of card_6 does not match ncards definition in card 3. 
            msg = ('\'card_6\' declared ' + str(len(cards_6)) + ' time(s) ' + 
                   'while \'ngrid\' is set to ' + str(ngrid_value) +
                   ' in \'card_3\', module \'reconr\'.')
            rule.semantic_error(msg, module)
        for card_6 in cards_6:
            analyze_reconr_card_6(card_6, module)

    return 'ok'

def analyze_reconr_card_1(card_1, module):
    must_be_defined = ['nendf', 'npend']
    for id_name in must_be_defined:
        rule.identifier_must_be_defined(id_name, card_1, module)
        id_node = helper.get_identifier(id_name, card_1)
        rule.identifier_must_be_int(id_node)
        rule.identifier_must_be_unit_number(id_node)
    return 'ok'

def analyze_reconr_card_2(card_2, module):
    tlabel = helper.get_identifier('tlabel', card_2)
    if helper.not_defined(tlabel):
        pass
    else:
        tlabel_value = rule.identifier_must_be_string(tlabel, card_2, module)
        # XXX: Add a function which checks that the allowed length is not
        #      exceeded?
        # At most 66 characters are allowed in labels.
        if len(tlabel_value) > 66:
            msg = ('\'tlabel\' exceeds the 66 character length in ' + 
                   '\'card_2\', module \'reconr\'.')
            rule.semantic_error(msg, tlabel)
    return 'ok'

def analyze_reconr_card_3(card_3, module):
    rule.identifier_must_be_defined('mat', card_3, module)

    ncards = helper.get_identifier('ncards', card_3)
    if helper.not_defined(ncards):
        pass
    else:
        rule.identifier_must_be_int(ncards)
        # XXX: check if ncards is positive, negative number of cards is not a
        #      proper input.

    ngrid = helper.get_identifier('ngrid', card_3)
    if helper.not_defined(ngrid):
        pass
    else:
        rule.identifier_must_be_int(ngrid)
        # XXX: check if ngrid is positive, negative number of grids is not a
        #      proper input.

    return 'ok'

def analyze_reconr_card_4(card_4, module):
    rule.identifier_must_be_defined('err', card_4, module)
    return 'ok'

def analyze_reconr_card_5(card_5, module):
    cards = rule.identifier_must_be_defined('cards', card_5, module)
    rule.identifier_must_be_string(cards, card_5, module)
    return 'ok'

def analyze_reconr_card_6(card_6, module):
    rule.identifier_must_be_defined('enode', card_6, module)
    return 'ok'
