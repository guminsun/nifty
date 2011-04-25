from nifty.environment import helpers as helper

from organize_acer import organize_acer
#from organize_broadr import organize_broadr
#from organize_ccccr import organize_ccccr
#from organize_covr import organize_covr
#from organize_dtfr import organize_dtfr
#from organize_errorr import organize_errorr
#from organize_gaminr import organize_gaminr
#from organize_gaspr import organize_gaspr
#from organize_groupr import organize_groupr
#from organize_heatr import organize_heatr
#from organize_leapr import organize_leapr
#from organize_matxsr import organize_matxsr
#from organize_mixr import organize_mixr
#from organize_moder import organize_moder
#from organize_plotr import organize_plotr
#from organize_powr import organize_powr
#from organize_purr import organize_purr
#from organize_reconr import organize_reconr
#from organize_resxsr import organize_resxsr
#from organize_thermr import organize_thermr
#from organize_unresr import organize_unresr
#from organize_viewr import organize_viewr
#from organize_wimsr import organize_wimsr

##############################################################################
# Organizer. To put together into an orderly, functional, structured whole.

def organize(ast):
    return organize_program(ast)

def organize_program(program):
    module_list = helper.get_module_list(program)
    module_list = organize_module_list(module_list)
    program = helper.set_module_list(module_list, program)
    return program

def organize_module_list(module_list):
    for module in module_list:
        module = organize_module(module)
    return module_list

def organize_module(module):
    organizer_function = organize_dummy
    organizer_functions = {
        'acer' : organize_acer,
        #'broadr' : organize_broadr,
        #'ccccr' : organize_ccccr,
        #'covr' : organize_covrr,
        #'dtfr' : organize_dtfrr,
        #'errorr' : organize_errorr,
        #'gaminr' : organize_gaminr,
        #'gaspr' : organize_gaspr,
        #'groupr' : organize_groupr,
        #'heatr' : organize_heatr,
        #'leapr' : organize_leapr,
        #'matxsr' : organize_matxsr,
        #'mixr' : organize_mixr,
        #'moder' : organize_moder,
        #'plotr' : organize_plotr,
        #'powr' : organize_powr,
        #'purr' : organize_purr,
        #'reconr' : organize_reconr,
        #'resxsr' : organize_resxsr,
        #'thermr' : organize_thermr,
        #'unresr' : organize_unresr,
        #'viewr' : organize_viewr,
        #'wimsr' : organize_wimsr,
    }
    module_name = helper.get_module_name(module)
    if module_name == 'stop':
        # Nothing to organize.
        return module
    else:
        try:
            organizer_function = organizer_functions[module_name]
        except KeyError:
            msg = ('--- nifty_organizer: XXX not implemented yet: ' +
                   module_name)
            print msg
    return organizer_function(module)

def organize_dummy(module):
    return module
