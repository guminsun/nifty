from nifty.environment import helpers as helper

##############################################################################
# Organize acer. Put together into an orderly, functional, structured whole.

def organize_acer(acer_module_node):
    acer_card_list = helper.get_card_list(acer_module_node)
    organize_acer_card_list(acer_card_list)
    return acer_module_node

def organize_acer_card_list(acer_card_list):
    return acer_card_list
