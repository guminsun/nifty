import sys

import analyzer_helpers as helper

##############################################################################
# Semantic rules.

def cards_must_be_defined(must_be_defined, card_list, module):
    found = False
    for m in must_be_defined:
        for card in card_list:
            if card['card_name'] == m:
                found = True
                break
            else:
                found = False
        if not found:
            # 'm' not defined.
            msg = ('\'' + m + '\' not defined in module \'' +
                   module['module_name'] + '\'.')
            semantic_error(msg, module)
    return 'ok'

def cards_must_be_unique(unique_card_list, card_list, module):
    for unique in unique_card_list:
        n = 0
        for card in card_list:
            if card['card_name'] == unique:
                n += 1
            if n > 1:
                # Found more than one instance of 'unique' in card_list.
                msg = ('\'' + card['card_name'] +
                       '\' declared more than once in module \'' +
                       module['module_name'] + '\'.')
                semantic_error(msg, card)
    return 'ok'

def identifiers_must_be_defined(must_be_defined, card_node, module):
    for id_name in must_be_defined:
        identifier = helper.get_identifier(id_name,
                                           card_node['statement_list'])
        identifier_must_be_defined(identifier, id_name, card_node,
                                   module['module_name'])
    return 'ok'

def identifier_must_be_defined(identifier, id_name, card_node, module_name):
    if identifier is None:
        msg = ('identifier \'' + id_name + '\' not defined in \'' +
               card_node['card_name'] + '\', module \'' +
               module_name + '\'.')
        semantic_error(msg, card_node)
    return 'ok'

def value_must_be_int(value, node):
    if not isinstance(value, int):
        msg = ('\'' + node['identifier'] + '\' (value: ' + str(value) + ') ' + 
               'must be an integer.')
        semantic_error(msg, node)
    return 'ok'

def value_must_be_string(value, node):
    if not isinstance(value, str):
        msg = ('\'' + node['identifier'] + '\' (value: ' + str(value) + ') ' + 
               'must be a string.')
        semantic_error(msg, node)
    return 'ok'

##############################################################################
# Error handling.

def semantic_error(msg, node):
    try:
        line = node['line_number']
    # Catch nodes which doesn't have the key 'line_number' defined.
    except KeyError:
        line = None
    # Catch None. E.g. in case of undefined identifier.
    except TypeError:
        line = None
    sys.stderr.write('--- Semantic error on line %s, %s\n' % (line, msg))
    sys.exit('semantic_error')
