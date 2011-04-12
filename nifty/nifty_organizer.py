import sys
from pprint import pprint as pprint

import nifty_analyzer
import nifty_parser

##############################################################################
# Organizer. To put together into an orderly, functional, structured whole.

def organize(ast):
    return ast

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
