import sys
from pprint import pprint as pprint

import nifty_analyzer
import nifty_parser

##############################################################################
# Organizer. To put together into an orderly, functional, structured whole.

def organize(ast):
    return ast

##############################################################################
# Helpers.

def sort_card_lists(program):
    module_list = program['module_list']
    for module in module_list:
        sort_card_list(module['card_list'])
    return program

def sort_card_list(card_list):
    # XXX: Ugly assumption that the card nodes will be sorted on 'card_id'.
    return card_list.sort()

def make_card(id_digit, id_alpha):
    card = dict()
    card['node_type'] = 'card'
    card['line_number'] = None
    card['card_id'] = (id_digit, id_alpha)
    card['card_name'] = 'card_' + str(id_digit) + id_alpha
    card['statement_list'] = list()
    return card

def insert_card(card, card_list):
    index = 0
    for c in card_list:
        if c['card_id'] < card['card_id']:
            index += 1
        else:
            break
    card_list.insert(index, card)
    return card_list

##############################################################################
# Misc.

if __name__ == '__main__':
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        ast = nifty_parser.parse(open(filename).read())
    else:
        ast = nifty_parser.parse(sys.stdin.read())
    ast = nifty_analyzer.analyze(ast)
    ast = organize(ast)
    print '--- nifty organizer output:'
    pprint(ast)
