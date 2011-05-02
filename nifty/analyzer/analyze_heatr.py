from nifty.environment import helpers as env
import analyzer_rules as rule

##############################################################################
# Analyze heatr. Checks if heatr is somewhat semantically correct.

def analyze_heatr(module):
    analyze_heatr_card_list(module)
    return module

def analyze_heatr_card_list(module):
    card_iter = env.get_card_iterator(module)
    analyze_heatr_card_1(env.next(card_iter), module)
    return module

def analyze_heatr_card_1(card_1, module):
    rule.card_must_be_defined('card_1', card_1, module, None)
    stmt_iter = env.get_statement_iterator(card_1)
    rule.analyze_unit_number('nendf', env.next(stmt_iter), card_1, module)
    rule.analyze_unit_number('nin', env.next(stmt_iter), card_1, module)
    rule.analyze_unit_number('nout', env.next(stmt_iter), card_1, module)
    rule.analyze_optional_unit_number('nplot', env.next(stmt_iter), card_1, module)
    rule.no_statement_allowed(env.next(stmt_iter), card_1, module)
    return card_1
