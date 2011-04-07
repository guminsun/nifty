import sys
from pprint import pprint as pprint

import nif_parser

##############################################################################
# Analyzer.

def analyze(ast):
    return analyze_program(ast)

def analyze_program(program):
    return program

##############################################################################
# Misc.

if __name__ == '__main__':
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        ast = nif_parser.parse(open(filename).read())
    else:
        ast = nif_parser.parse(sys.stdin.read())
    ast = analyze(ast)
    pprint(ast)
