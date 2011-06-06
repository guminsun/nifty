import string

from nifty.environment import helpers as env

##############################################################################
# Emitter. To give or send out.

def emit(program):
    return program_to_string(program)

def program_to_string(program):
    module_list = program.get('module_list')
    return module_list_to_string(module_list)

def module_list_to_string(module_list):
    slist = [module_to_string(module) for module in module_list]
    return ''.join(slist)

def module_to_string(module):
    module_name = module.get('module_name')
    card_list = module.get('card_list')
    s = '%s%s%s' % (module_name, newline(), card_list_to_string(card_list))
    return s

def card_list_to_string(card_list):
    slist = [card_to_string(card) for card in card_list]
    return ''.join(slist)

def card_to_string(card):
    statement_list = card.get('statement_list')
    s = '%s%s%s%s%s' % (statement_list_to_string(statement_list), default(),
                        space(), card_comment(card), newline())
    return s

def statement_list_to_string(statement_list):
    slist = [statement_to_string(statement) for statement in statement_list]
    # Concatenate the statements with intervening occurences of spaces.
    return string.join(slist, space())

def statement_to_string(node):
    # XXX: node is assumed to be an assignment node.
    return assignment_to_string(node)

def assignment_to_string(node):
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
    s = '%s%s%s' % (single_quote(), str(value), single_quote())
    return s

##############################################################################
# Helpers.

def card_comment(card):
    string = '%s%s' % (comment_prefix(), card.get('card_name'))
    return string

def comment_prefix():
    return '### '

def default():
    return '/'

def newline():
    return '\n'

def single_quote():
    return '\''

def space():
    return ' '
