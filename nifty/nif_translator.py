import sys
from pprint import pprint as pprint

import nif_analyzer
import nif_parser

##############################################################################
# Translator.

def translate(ast):
    env = dict()
    translate_program(ast, env)

def translate_program(ast, env):
    return []

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
