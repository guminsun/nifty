from nifty.environment import helpers as env

##############################################################################
# Translator.

def translate(ast):
    return translate_program(ast)

def translate_program(program):
    module_list = program.get('module_list')
    return translate_module_list(module_list)

def translate_module_list(module_list):
    instructions = list()
    for module in module_list:
        instructions.append(translate_module(module))
    return instructions

def translate_module(module):
    module_name = module.get('module_name')
    card_list = module.get('card_list')
    instructions = translate_card_list(card_list)
    return module_name, instructions

def translate_card_list(card_list):
    instructions = list()
    for card in card_list:
        instructions.append(translate_card(card))
    return instructions

def translate_card(card):
    statement_list = card.get('statement_list')
    instructions = translate_statement_list(statement_list)
    return instructions

def translate_statement_list(statement_list):
    instructions = list()
    for statement in statement_list:
        instructions.append(translate_statement(statement))
    return instructions

def translate_statement(statement):
    if env.is_assignment(statement):
        return translate_assignment(statement)
    else:
        # Catch anything else, just in case.
        print('--- translator: XXX statement not implemented yet:',
              str(statement.get('node_type')))
        return statement

def translate_assignment(statement):
    r_value = statement.get('r_value')
    return translate_r_value(r_value)

def translate_r_value(r_value):
    if env.is_singleton(r_value):
        return translate_r_value_singleton(r_value)
    elif env.is_pair(r_value):
        return translate_r_value_pair(r_value)
    elif env.is_triplet(r_value):
        return translate_r_value_triple(r_value)
    else:
        # Catch anything else, just in case.
        print('--- translator: XXX tuple not implemented yet:',
              str(r_value.get('node_type')))
        return r_value

def translate_r_value_singleton(singleton):
    element_1_value = singleton.get('element_1').get('value')
    value = str(element_1_value)
    node_type = singleton.get('element_1').get('node_type')
    return (node_type, value)

def translate_r_value_pair(pair):
    element_1_value = pair.get('element_1').get('value')
    element_2_value = pair.get('element_2').get('value')
    value = str(element_1_value) + str(element_2_value)
    # XXX: First element determines how the pair will be printed.
    node_type = pair.get('element_1').get('node_type')
    return (node_type, value)

def translate_r_value_triple(triplet):
    element_1_value = triplet.get('element_1').get('value')
    element_2_value = triplet.get('element_2').get('value')
    element_3_value = triplet.get('element_3').get('value')
    value = str(element_1_value) + str(element_2_value) + str(element_3_value)
    # XXX: First element determines how the triplet will be printed.
    node_type = triplet.get('element_1').get('node_type')
    return (node_type, value)
