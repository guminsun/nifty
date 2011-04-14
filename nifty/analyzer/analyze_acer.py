import analyzer_helpers as helper
import analyzer_rules as rule

##############################################################################
# Analyze acer.

def analyze_acer(module):
    card_list = module['card_list']
    analyze_acer_card_list(card_list, module)
    return 'ok'

def analyze_acer_card_list(card_list, module):
    pass