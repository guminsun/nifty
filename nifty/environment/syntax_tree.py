##############################################################################
# Syntax Tree Node Constructors.

def make_program(line_number, module_list):
    node = dict()
    node['node_type'] = 'program'
    node['line_number'] = line_number
    node['module_list'] = module_list
    return node

def make_stop(line_number):
    node = dict()
    node['node_type'] = 'module'
    node['line_number'] = line_number
    node['module_name'] = 'stop'
    node['card_list'] = list()
    return node

def make_module(line_number, module_name, card_list):
    node = dict()
    node['node_type'] = 'module'
    node['line_number'] = line_number
    node['module_name'] = module_name
    node['card_list'] = card_list
    return node

def make_card(line_number, card_name, statement_list):
    node = dict()
    node['node_type'] = 'card'
    node['line_number'] = line_number
    node['card_name'] = card_name
    node['statement_list'] = statement_list
    return node

def make_statement(statement):
    return statement

def make_expression(expression):
    return expression

def make_assignment(line_number, node_type, l_value, r_value):
    node = dict()
    node['line_number'] = line_number
    node['node_type'] = node_type
    node['l_value'] = l_value
    node['r_value'] = r_value
    return node

def make_singleton(line_number, element_1):
    node = dict()
    node['line_number'] = line_number
    node['node_type'] = 'singleton'
    node['element_1'] = element_1
    return node

def make_pair(line_number, element_1, element_2):
    node = dict()
    node['line_number'] = line_number
    node['node_type'] = 'pair'
    node['element_1'] = element_1
    node['element_2'] = element_2
    return node

def make_triplet(line_number, element_1, element_2, element_3):
    node = dict()
    node['line_number'] = line_number
    node['node_type'] = 'triplet'
    node['element_1'] = element_1
    node['element_2'] = element_2
    node['element_3'] = element_3
    return node

def make_l_value(l_value):
    return l_value

def make_array(line_number, name, index):
    node = dict()
    node['line_number'] = line_number
    node['node_type'] = 'array'
    node['name'] = name
    node['index'] = index
    return node

def make_identifier(line_number, name):
    node = dict()
    node['line_number'] = line_number
    node['node_type'] = 'identifier'
    node['name'] = name
    return node

def make_r_value(r_value):
    return r_value

def make_float(line_number, value):
    node = dict()
    node['line_number'] = line_number
    node['node_type'] = 'float'
    node['value'] = value
    return node

def make_integer(line_number, value):
    node = dict()
    node['line_number'] = line_number
    node['node_type'] = 'integer'
    node['value'] = value
    return node

def make_null(line_number, value):
    node = dict()
    node['line_number'] = line_number
    node['node_type'] = 'null'
    node['value'] = None
    return node

def make_string(line_number, value):
    node = dict()
    node['line_number'] = line_number
    node['node_type'] = 'string'
    node['value'] = value
    return node
