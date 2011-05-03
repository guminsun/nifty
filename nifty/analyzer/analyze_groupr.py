from nifty.environment import helpers as env
import analyzer_rules as rule

##############################################################################
# Analyze groupr. Checks if groupr is somewhat semantically correct.

def analyze_groupr(module):
    analyze_groupr_card_list(module)
    return module

def analyze_groupr_card_list(module):
    card_iter = env.get_card_iterator(module)
    # Card 1 must always be defined.
    analyze_groupr_card_1(env.next(card_iter), module)
    
    # No more cards are allowed. The next card returned by env.next(card_iter)
    # should be 'None'.
    #rule.no_card_allowed(env.next(card_iter), module)
    return module

def analyze_groupr_card_1(card_1, module):
    # Card 1 must be defined.
    rule.card_must_be_defined('card_1', card_1, module, None)
    stmt_iter = env.get_statement_iterator(card_1)
    rule.analyze_unit_number('nendf', env.next(stmt_iter), card_1, module)
    rule.analyze_unit_number('npend', env.next(stmt_iter), card_1, module)
    rule.analyze_optional_unit_number('ngout1', env.next(stmt_iter), card_1, module)
    rule.analyze_optional_unit_number('ngout2', env.next(stmt_iter), card_1, module)
    rule.no_statement_allowed(env.next(stmt_iter), card_1, module)
    return card_1
