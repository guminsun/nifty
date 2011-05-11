from nifty.environment import helpers as env
import analyzer_rules as rule

##############################################################################
# Analyze plotr. Checks if plotr is somewhat semantically correct.

def analyze_plotr(module):
    analyze_plotr_card_list(module)
    return module

def analyze_plotr_card_list(module):
    pass