import sys

from nifty.analyzer import analyzer_rules as rule
from nifty.environment import helpers as env
import organizer_helpers as helper

##############################################################################
# Organize plotr. Put together into an orderly, functional, structured whole.

def organize_plotr(module):
    card_list = module.get('card_list')
    organize_card_list(card_list, module)
    return module

def organize_card_list(card_list, module):
    card_iter = env.get_card_iterator(module)
    return card_list
