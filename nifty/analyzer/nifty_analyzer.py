import sys

from analyze_acer import analyze_acer
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
    module_analyzers = {
        'acer' : analyze_acer,
        #'broadr' : analyze_broadr,
        #'ccccr' : analyze_ccccr,
        #'covr' : analyze_covrr,
        #'dtfr' : analyze_dtfrr,
        #'errorr' : analyze_errorr,
        #'gaminr' : analyze_gaminr,
        #'gaspr' : analyze_gaspr,
        #'groupr' : analyze_groupr,
        #'heatr' : analyze_heatr,
        #'leapr' : analyze_leapr,
        #'matxsr' : analyze_matxsr,
        #'mixr' : analyze_mixr,
        #'moder' : analyze_moder,
        #'plotr' : analyze_plotr,
        #'powr' : analyze_powr,
        #'purr' : analyze_purr,
        'reconr' : analyze_reconr,
        #'resxsr' : analyze_resxsr,
        #'thermr' : analyze_thermr,
        #'unresr' : analyze_unresr,
        #'viewr' : analyze_viewr,
        #'wimsr' : analyze_wimsr,
    }
    module_name = module['module_name']
    if module_name == 'stop':
        pass
    else:
        try:
            analyze = module_analyzers[module_name]
            analyze(module)
        except KeyError:
            msg = ('--- nifty_analyzer: XXX not implemented yet: ' +
                   module_name)
            print msg
    return 'ok'
