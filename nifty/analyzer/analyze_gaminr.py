from nifty.environment import helpers as env
import analyzer_rules as rule

##############################################################################
# Analyze gaminr. Checks if gaminr is somewhat semantically correct.

def analyze_gaminr(module):
    analyze_card_list(module)
    return module

def analyze_card_list(module):
    card_iter = env.get_card_iterator(module)
    # Card 1 must always be defined.
    analyze_card_1(env.next(card_iter), module)
    return module

def analyze_card_1(card, module):
    # Card 1 must be defined.
    rule.card_must_be_defined('card_1', card, module, None)
    # Use a statement iterator to check whether the identifiers have been
    # defined in the expected order.
    stmt_iter = env.get_statement_iterator(card)
    # Unit numbers that must be defined.
    rule.analyze_unit_number('nendf', env.next(stmt_iter), card, module)
    rule.analyze_unit_number('npend', env.next(stmt_iter), card, module)
    # Optional unit numbers.
    rule.analyze_optional_unit_number('ngam1', env.next(stmt_iter), card, module)
    rule.analyze_optional_unit_number('ngam2', env.next(stmt_iter), card, module)
    # No more statements are allowed. The next statement returned by
    # env.next(card_iter) should be 'None'.
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card
