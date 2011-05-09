from nifty.environment import helpers as env
import analyzer_rules as rule

##############################################################################
# Analyze covr. Checks if covr is somewhat semantically correct.

def analyze_covr(module):
    analyze_covr_card_list(module)
    return module

def analyze_covr_card_list(module):
    card_iter = env.get_card_iterator(module)
    # XXX: rule.no_card_allowed(env.next(card_iter), module)
    return module
