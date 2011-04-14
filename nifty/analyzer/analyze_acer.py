import analyzer_helpers as helper
import analyzer_rules as rule

##############################################################################
# Analyze acer.

def analyze_acer(module):
    card_list = module['card_list']
    analyze_acer_card_list(card_list, module)
    return 'ok'

def analyze_acer_card_list(card_list, module):
    # Check for cards that always must be defined.
    must_be_defined = ['card_1', 'card_2', 'card_3', 'card_4']
    rule.cards_must_be_defined(must_be_defined, card_list, module)

    # Check for cards that must be unique (e.g. not defined more than once).
    unique_card_list = ['card_1', 'card_2', 'card_4']
    rule.cards_must_be_unique(unique_card_list, card_list, module)

    card_1 = helper.get_card('card_1', card_list)
    analyze_acer_card_1(card_1, module)

    return 'ok'

def analyze_acer_card_1(card_1, module):
    ''' Return 'ok' if 'card_1' is semantically correct.
        
        Precondition: 'card_1' is a card node from the acer module with 
                      card_id = (1, '').
    '''
    must_be_defined = ['nendf', 'npend', 'ngend', 'nace', 'ndir']
    rule.identifiers_must_be_defined(must_be_defined, card_1, module)

    return 'ok'