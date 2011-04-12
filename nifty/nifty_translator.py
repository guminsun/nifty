import sys
from pprint import pprint as pprint

import nifty_analyzer
import nifty_organizer
import nifty_parser

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
    if statement['node_type'] == '=':
        return translate_assignment(statement)
    else:
        print('--- translator: XXX statement not implemented yet:',
              statement['node_type'])
        return None

def translate_assignment(statement):
    r_value = statement['r_value']
    return translate_r_value(r_value)

def translate_r_value(r_value):
    return r_value['value']

##############################################################################
# Misc.

if __name__ == '__main__':
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        ast = nifty_parser.parse(open(filename).read())
    else:
        ast = nifty_parser.parse(sys.stdin.read())
    ast = nifty_analyzer.analyze(ast)
    ast = nifty_organizer.organize(ast)
    instructions = translate(ast)
    print '--- nifty translator output:'
    pprint(instructions)