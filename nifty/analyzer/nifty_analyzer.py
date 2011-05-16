from analyze_acer import analyze_acer
from analyze_broadr import analyze_broadr
#from analyze_ccccr import analyze_ccccr
from analyze_covr import analyze_covr
#from analyze_dtfr import analyze_dtfr
from analyze_errorr import analyze_errorr
#from analyze_gaminr import analyze_gaminr
#from analyze_gaspr import analyze_gaspr
from analyze_groupr import analyze_groupr
from analyze_heatr import analyze_heatr
#from analyze_leapr import analyze_leapr
#from analyze_matxsr import analyze_matxsr
#from analyze_mixr import analyze_mixr
from analyze_moder import analyze_moder
from analyze_plotr import analyze_plotr
#from analyze_powr import analyze_powr
#from analyze_purr import analyze_purr
from analyze_reconr import analyze_reconr
#from analyze_resxsr import analyze_resxsr
from analyze_thermr import analyze_thermr
#from analyze_unresr import analyze_unresr
from analyze_viewr import analyze_viewr
#from analyze_wimsr import analyze_wimsr

##############################################################################
# Analyzer.

def analyze(ast):
    analyze_program(ast)
    return ast

def analyze_program(program):
    module_list = program.get('module_list')
    analyze_module_list(module_list)
    return program

def analyze_module_list(module_list):
    for module in module_list:
        analyze_module(module)
    return module_list

def analyze_module(module):
    analyzer_functions = {
        'acer' : analyze_acer,
        'broadr' : analyze_broadr,
        #'ccccr' : analyze_ccccr,
        'covr' : analyze_covr,
        #'dtfr' : analyze_dtfrr,
        'errorr' : analyze_errorr,
        #'gaminr' : analyze_gaminr,
        #'gaspr' : analyze_gaspr,
        'groupr' : analyze_groupr,
        'heatr' : analyze_heatr,
        #'leapr' : analyze_leapr,
        #'matxsr' : analyze_matxsr,
        #'mixr' : analyze_mixr,
        'moder' : analyze_moder,
        'plotr' : analyze_plotr,
        #'powr' : analyze_powr,
        #'purr' : analyze_purr,
        'reconr' : analyze_reconr,
        #'resxsr' : analyze_resxsr,
        'thermr' : analyze_thermr,
        #'unresr' : analyze_unresr,
        'viewr' : analyze_viewr,
        #'wimsr' : analyze_wimsr,
    }
    module_name = module.get('module_name')
    if module_name == 'stop':
        # Nothing to analyze.
        return module
    else:
        analyzer_function = analyzer_functions.get(module_name, analyze_dummy)
    analyzer_function(module)
    return module

def analyze_dummy(module):
    pass
