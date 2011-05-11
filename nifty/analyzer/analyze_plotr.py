from nifty.environment import helpers as env
import analyzer_rules as rule

##############################################################################
# Analyze plotr. Checks if plotr is somewhat semantically correct.

def analyze_plotr(module):
    analyze_plotr_card_list(module)
    return module

def analyze_plotr_card_list(module):
    card_iter = env.get_card_iterator(module)
    analyze_plotr_card_0(env.next(card_iter), module)
    # XXX: rule.no_card_allowed(env.next(card_iter), module)
    return module

def analyze_plotr_card_0(card, module):
    rule.card_must_be_defined('card_0', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    rule.analyze_unit_number('nplt', env.next(stmt_iter), card, module)
    rule.analyze_optional_unit_number('nplt0', env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card    
