from nifty.environment import helpers as env
import analyzer_rules as rule

##############################################################################
# Analyze broadr. Checks if broadr is somewhat semantically correct.

def analyze_broadr(module):
    analyze_broadr_card_list(module)
    return module

def analyze_broadr_card_list(module):
    card_iter = env.get_card_iterator(module)
    analyze_broadr_card_1(env.next(card_iter), module)
    # XXX:
    # rule.no_card_allowed(env.next(card_iter), module)
    return module

def analyze_broadr_card_1(card, module):
    rule.card_must_be_defined('card_1', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    rule.analyze_unit_number('nendf', env.next(stmt_iter), card, module)
    rule.analyze_unit_number('nin', env.next(stmt_iter), card, module)
    rule.analyze_unit_number('nout', env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card
