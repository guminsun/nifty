import sys

from analyze_reconr import analyze_reconr

##############################################################################
# Analyzer.

def analyze(ast):
    analyze_program(ast)
    return ast

def analyze_program(program):
    module_list = program['module_list']
    analyze_module_list(module_list)
    return 'ok'

def analyze_module_list(module_list):
    for module in module_list:
        analyze_module(module)
    return 'ok'

def analyze_module(module):
    # XXX: Fix big ugly switch.
    if module['module_name'] == 'stop':
        pass
    elif module['module_name'] == 'reconr':
        analyze_reconr(module)
    else:
        print '--- analyzer: XXX not implemented yet:', module['module_name']
    return 'ok'
