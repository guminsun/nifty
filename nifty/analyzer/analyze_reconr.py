import analyzer_helpers as helper
import analyzer_rules as rule

##############################################################################
# Analyze reconr.

def analyze_reconr(module):
    card_list = module['card_list']
    analyze_reconr_card_list(card_list, module)
    return 'ok'

def analyze_reconr_card_list(card_list, module):
    # Check for cards that always must be defined.
    must_be_defined = ['card_1', 'card_2', 'card_3', 'card_4']
    rule.cards_must_be_defined(must_be_defined, card_list, module)

    # Check for cards that must be unique (e.g. not defined more than once).
    unique_card_list = ['card_1', 'card_2', 'card_4']
    rule.cards_must_be_unique(unique_card_list, card_list, module)

    card_1 = helper.get_card('card_1', card_list)
    analyze_reconr_card_1(card_1)

    card_2 = helper.get_card('card_2', card_list)
    analyze_reconr_card_2(card_2)

    # Cards 3, 4, 5, 6 must be input for each material desired.
    cards_3 = helper.get_cards('card_3', card_list)
    for card_3 in cards_3:
        analyze_reconr_card_3(card_3)
        card_3_statement_list = card_3['statement_list']
        
        # Break loop if mat = 0, which indicates termination of execution.
        mat = helper.get_identifier('mat', card_3_statement_list)
        mat_value = helper.get_value(helper.get_r_value(mat))
        if mat_value == 0:
            break

        card_4 = helper.get_card('card_4', card_list)
        analyze_reconr_card_4(card_4)

        # card_5 must be defined 'ncards' times for each card_3 (see card 3).
        ncards = helper.get_identifier('ncards', card_3_statement_list)
        if helper.not_defined(ncards):
            ncards_value = 0
        else:
            ncards_value = helper.get_value(helper.get_r_value(ncards))
        cards_5 = helper.get_cards('card_5', card_list)
        if len(cards_5) != ncards_value:
            # Number of card_5 does not match ncards definition in card 3. 
            msg = ('\'card_5\' declared ' + str(len(cards_5)) + ' time(s) ' + 
                   'while \'ncards\' is set to ' + str(ncards_value) +
                   ' in \'card_3\', module \'reconr\'.')
            rule.semantic_error(msg, module)
        for card_5 in cards_5:
            analyze_reconr_card_5(card_5)

        # card_6 must be defined 'ngrid' times for each card_3 (see card 3).
        ngrid = helper.get_identifier('ngrid', card_3_statement_list)
        if helper.not_defined(ngrid):
            ngrid_value = 0
        else:
            ngrid_value = helper.get_value(helper.get_r_value(ngrid))
        cards_6 = helper.get_cards('card_6', card_list)
        if len(cards_6) != ngrid_value:
            # Number of card_6 does not match ncards definition in card 3. 
            msg = ('\'card_6\' declared ' + str(len(cards_6)) + ' time(s) ' + 
                   'while \'ngrid\' is set to ' + str(ngrid_value) +
                   ' in \'card_3\', module \'reconr\'.')
            rule.semantic_error(msg, module)
        for card_6 in cards_6:
            analyze_reconr_card_6(card_6)

    return 'ok'

def analyze_reconr_card_1(card_1):
    ''' Return 'ok' if 'card_1' is semantically correct.
        
        Precondition: 'card_1' is a card node from the reconr module with 
                      card_id = (1, '').
    '''
    statement_list = card_1['statement_list']

    # XXX: Neat to construct a list of identifiers which must be defined and
    #      check whether they are defined or not?

    nendf = helper.get_identifier('nendf', statement_list)
    # nendf must be defined. Translator cannot guess unit numbers.
    rule.identifier_must_be_defined(nendf, 'nendf', card_1, 'reconr')

    nendf_value = helper.get_value(helper.get_r_value(nendf))
    # The nendf unit number must be an integer.
    rule.value_must_be_int(nendf_value, nendf)

    # The nendf unit number must be in [20,99], or [-99,-20] for binary.
    if ((nendf_value not in range(20, 100)) and
        (nendf_value not in range(-99, -19))):
        msg = 'illegal nendf unit number (' + str(nendf_value) + ').'
        rule.semantic_error(msg, nendf)

    npend = helper.get_identifier('npend', statement_list)
    # npend must be defined. Translator cannot guess unit numbers.
    rule.identifier_must_be_defined(npend, 'npend', card_1, 'reconr')

    npend_value = helper.get_value(helper.get_r_value(npend))
    # The npend unit number must be an integer.
    rule.value_must_be_int(npend_value, npend)

    # The npend unit number must be in [20,99], or [-99,-20] for binary.
    if ((npend_value not in range(20, 100)) and
        (npend_value not in range(-99, -19))):
        msg = 'illegal npend unit number (' + str(npend_value) + ').'
        rule.semantic_error(msg, nendf)

    return 'ok'

def analyze_reconr_card_2(card_2):
    ''' Return 'ok' if 'card_2' is semantically correct.
        
        Precondition: 'card_2' is a card node from the reconr module with 
                      card_id = (2, '').
    '''
    statement_list = card_2['statement_list']
    tlabel = helper.get_identifier('tlabel', statement_list)
    if helper.not_defined(tlabel):
        pass
    else:
        tlabel_value = helper.get_value(helper.get_r_value(tlabel))
        # At most 66 characters are allowed in labels.
        if len(tlabel_value) > 66:
            msg = ('label exceeds 66 character length in \'card_2\',' +
                   'module \'reconr\'.')
            rule.semantic_error(msg, tlabel)
    return 'ok'

def analyze_reconr_card_3(card_3):
    ''' Return 'ok' if 'card_3' is semantically correct.

        Precondition: 'card_3' is a card node from the reconr module with 
                      card_id = (3, '').
    '''
    statement_list = card_3['statement_list']

    mat = helper.get_identifier('mat', statement_list)
    rule.identifier_must_be_defined(mat, 'mat', card_3, 'reconr')

    ncards = helper.get_identifier('ncards', statement_list)
    if helper.not_defined(ncards):
        pass
    else:
        ncards_value = helper.get_value(helper.get_r_value(ncards))
        rule.value_must_be_int(ncards_value, ncards)

    ngrid = helper.get_identifier('ngrid', statement_list)
    if helper.not_defined(ngrid):
        pass
    else:
        ngrid_value = helper.get_value(helper.get_r_value(ngrid))
        rule.value_must_be_int(ngrid_value, ngrid)

    return 'ok'

def analyze_reconr_card_4(card_4):
    ''' Return 'ok' if 'card_4' is semantically correct.

        Precondition: 'card_4' is a card node from the reconr module with 
                      card_id = (4, '').
    '''
    statement_list = card_4['statement_list']
    err = helper.get_identifier('err', statement_list)
    rule.identifier_must_be_defined(err, 'err', card_4, 'reconr')
    return 'ok'

def analyze_reconr_card_5(card_5):
    ''' Return 'ok' if 'card_5' is semantically correct.

        Precondition: 'card_5' is a card node from the reconr module with 
                      card_id = (5, '').
    '''
    statement_list = card_5['statement_list']

    cards = helper.get_identifier('cards', statement_list)
    rule.identifier_must_be_defined(cards, 'cards', card_5, 'reconr')
    cards_value = helper.get_value(helper.get_r_value(cards))
    rule.value_must_be_string(cards_value, cards)
    return 'ok'

def analyze_reconr_card_6(card_6):
    ''' Return 'ok' if 'card_6' is semantically correct.

        Precondition: 'card_6' is a card node from the reconr module with 
                      card_id = (6, '').
    '''
    statement_list = card_6['statement_list']
    enode = helper.get_identifier('enode', statement_list)
    rule.identifier_must_be_defined(enode, 'enode', card_6, 'reconr')
    return 'ok'
