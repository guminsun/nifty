import sys
from pprint import pprint as pprint

import nif_analyzer
import nif_parser

##############################################################################
# Translator.

def translate(ast):
    return translate_program(ast)

def translate_program(program):
    module_list = program['module_list']
    return translate_module_list(module_list)

def translate_module_list(module_list):
    instructions = list()
    for module in module_list:
        instructions.append(translate_module(module))
    return instructions

def translate_module(module):
    module_name = module['module_name']
    card_list = module['card_list']
    instructions = translate_card_list(card_list)
    return module_name, instructions

def translate_card_list(card_list):
    instructions = list()
    for card in card_list:
        instructions.append(translate_card(card))
    return instructions

def translate_card(card):
    statement_list = card['statement_list']
    instructions = translate_statement_list(statement_list)
    return instructions

def translate_statement_list(statement_list):
    instructions = list()
    for statement in statement_list:
        instructions.append(translate_statement(statement))
    return instructions

def translate_statement(statement):
    return None

##############################################################################
# Misc.

if __name__ == '__main__':
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        ast = nif_parser.parse(open(filename).read())
    else:
        ast = nif_parser.parse(sys.stdin.read())
    ast = nif_analyzer.analyze(ast)
    instructions = translate(ast)
    print '--- translator output:'
    pprint(instructions)
