from nifty.environment import helpers as env

##############################################################################
# Emitter. To give or send out.

def emit(program):
    return program_to_string(program)

def program_to_string(program):
    module_list = program.get('module_list')
    return module_list_to_string(module_list)

def module_list_to_string(module_list):
    string = str()
    for module in module_list:
        string += module_to_string(module)
    return string

def module_to_string(module):
    module_name = module.get('module_name')
    string = module_name + newline()
    card_list = module.get('card_list')
    string += card_list_to_string(card_list)
    return string

def card_list_to_string(card_list):
    string = str()
    for card in card_list:
        string += card_to_string(card)
    return string

def card_to_string(card):
    statement_list = card.get('statement_list')
    string = statement_list_to_string(statement_list) + default() + newline()
    return string

def statement_list_to_string(statement_list):
    string = str()
    statement_list_length = len(statement_list)
    for i in range(statement_list_length):
        # Append a space to every statement except the last one.
        if i < statement_list_length-1:
            string += statement_to_string(statement_list[i]) + space()
        else:
            string += statement_to_string(statement_list[i])
    return string

def statement_to_string(node):
    if env.is_assignment(node):
        return assignment_to_string(node)
    else:
        # Catch anything else, just in case.
        print('--- emitter: XXX statement not implemented yet:',
              env.get_node_type(node))
        return node

def assignment_to_string(node):
    l_value = node.get('l_value')
    r_value = node.get('r_value')
    return r_value_to_string(r_value)

def r_value_to_string(node):
    if env.is_float(node):
        return float_to_string(node)
    elif env.is_integer(node):
        return integer_to_string(node)
    elif env.is_null(node):
        return null_to_string(node)
    elif env.is_string(node):
        return string_to_string(node)
    else:
        # Catch anything else, just in case.
        print('--- emitter: XXX element node not implemented yet:',
              env.get_node_type(node))
        return node

def float_to_string(node):
    value = node.get('value')
    string = str(value)
    return string

def integer_to_string(node):
    value = node.get('value')
    string = str(value)
    return string

def null_to_string(node):
    return ''

def string_to_string(node):
    value = node.get('value')
    # Format the string as a NJOY string, i.e. delimited by single quotes.
    string = single_quote() + str(value) + single_quote()
    return string

##############################################################################
# Helpers.

def default():
    return '/'

def newline():
    return '\n'

def single_quote():
    return '\''

def space():
    return ' '
