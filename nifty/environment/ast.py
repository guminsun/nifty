##############################################################################
# nifty abstract syntax tree.

##############################################################################
# Constructors.

def make_program(p):
    node = dict()
    node['node_type'] = 'program'
    node['line_number'] = p.lineno(0)
    node['module_list'] = p[1]
    return node

def make_stop(p):
    node = dict()
    node['node_type'] = 'module'
    node['line_number'] = p.lineno(0)
    node['module_name'] = 'stop'
    node['card_list'] = []
    return node

def make_module(p):
    node = dict()
    node['node_type'] = 'module'
    node['line_number'] = p.lineno(0)
    node['module_name'] = p[1]
    node['card_list'] = p[3]
    return node

def make_card(p):
    node = dict()
    node['node_type'] = 'card'
    node['line_number'] = p.lineno(0)
    node['card_id'] = make_card_id(p[1])
    node['card_name'] = p[1]
    node['statement_list'] = p[3]
    return node

def make_card_id(card_name):
    id_alpha = ''
    id_digit = ''
    # XXX: Handle 'card'.
    if len(card_name) < 5:
        return None
    card_id = card_name[5:]
    for i in card_id:
        if i.isdigit():
            id_digit += i
        if i.isalpha():
            id_alpha += i
    return int(id_digit), id_alpha

def make_statement(p):
    return p[1]

def make_assignment(p):
    node = dict()
    node['line_number'] = p.lineno(2)
    node['node_type'] = p[2]
    node['l_value'] = p[1]
    node['r_value'] = p[3]
    return node

def make_l_value(p):
    return p[1]

def make_r_value(p):
    return p[1]

def make_pair(p):
    node = dict()
    node['line_number'] = p.lineno(2)
    node['node_type'] = 'pair'
    node['element_1'] = p[1]
    node['element_2'] = p[3]
    return node

def make_array(p):
    node = dict()
    node['line_number'] = p.lineno(0)
    node['node_type'] = 'array'
    node['name'] = p[1]
    node['index'] = eval(p[3])
    return node

def make_float(p):
    node = dict()
    node['line_number'] = p.lineno(0)
    node['node_type'] = 'float'
    # Floats are encapsulated as strings to preserve the float in its original
    # form. For example, Python would evaluate '3e2' to '300.0'.
    node['value'] = p[1]
    return node

def make_identifier(p):
    node = dict()
    node['line_number'] = p.lineno(0)
    node['node_type'] = 'identifier'
    node['name'] = p[1]
    return node

def make_integer(p):
    node = dict()
    node['line_number'] = p.lineno(0)
    node['node_type'] = 'integer'
    node['value'] = eval(p[1])
    return node

def make_string(p):
    node = dict()
    node['line_number'] = p.lineno(0)
    node['node_type'] = 'string'
    node['value'] = eval(p[1])
    return node
