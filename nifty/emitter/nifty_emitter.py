##############################################################################
# Emitter. To give or send out.

def emit(program):
    return program_to_string(program)

def program_to_string(program):
    string = ''
    for module in program:
        string += module_to_string(module)
    return string

def module_to_string(module):
    string = ''
    if module[0] == 'stop':
        string += module[0]
    else:
        string += module[0] + newline() + card_list_to_string(module[1])
    return string

def card_list_to_string(card_list):
    string = ''
    for card in card_list:
        string += card_to_string(card) + default() + newline()
    return string

def card_to_string(card):
    string = ''
    card_length = len(card)
    for i in range(card_length):
        if i < card_length-1:
            string += variable_to_string(card[i]) + space()
        else:
            string += variable_to_string(card[i])
    return string

def variable_to_string(variable):
    string = ''
    node_type = variable[0]
    value = variable[1]
    if node_type == 'string':
        string = single_quote() + str(value) + single_quote()
    else:
        string = str(value)
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
