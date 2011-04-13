import sys

##############################################################################
# Analyzer.

def analyze(ast):
    analyze_program(ast)
    return ast

def analyze_program(program):
    module_list = program['module_list']
    analyze_module_list(module_list)
    return 'ok'

def analyze_module_list(module_list):
    for module in module_list:
        analyze_module(module)
    return 'ok'

def analyze_module(module):
    # XXX: Fix big ugly switch.
    if module['module_name'] == 'stop':
        pass
    elif module['module_name'] == 'reconr':
        analyze_reconr(module)
    else:
        print '--- analyzer: XXX not implemented yet:', module['module_name']
    return 'ok'

def analyze_reconr(module):
    card_list = module['card_list']
    analyze_reconr_card_list(card_list, module)
    return 'ok'

def analyze_reconr_card_list(card_list, module):
    # Check for cards that always must be defined.
    must_be_defined = ['card_1', 'card_2', 'card_3', 'card_4']
    cards_must_be_defined(must_be_defined, card_list, module)

    # Check for cards that must be unique (e.g. not defined more than once).
    unique_card_list = ['card_1', 'card_2', 'card_4']
    cards_must_be_unique(unique_card_list, card_list, module)

    card_1 = get_card('card_1', card_list)
    analyze_reconr_card_1(card_1)

    card_2 = get_card('card_2', card_list)
    analyze_reconr_card_2(card_2)

    # Cards 3, 4, 5, 6 must be input for each material desired.
    cards_3 = get_cards('card_3', card_list)
    for card_3 in cards_3:
        analyze_reconr_card_3(card_3)
        card_3_statement_list = card_3['statement_list']
        
        # Break loop if mat = 0, which indicates termination of execution.
        mat = get_identifier('mat', card_3_statement_list)
        mat_value = get_value(get_r_value(mat))
        if mat_value == 0:
            break

        card_4 = get_card('card_4', card_list)
        analyze_reconr_card_4(card_4)

        # card_5 must be defined 'ncards' times for each card_3 (see card 3).
        ncards = get_identifier('ncards', card_3_statement_list)
        if not_defined(ncards):
            ncards_value = 0
        else:
            ncards_value = get_value(get_r_value(ncards))
        cards_5 = get_cards('card_5', card_list)
        if len(cards_5) != ncards_value:
            # Number of card_5 does not match ncards definition in card 3. 
            msg = ('\'card_5\' declared ' + str(len(cards_5)) + ' time(s) ' + 
                   'while \'ncards\' is set to ' + str(ncards_value) +
                   ' in \'card_3\', module \'reconr\'.')
            semantic_error(msg, module)
        for card_5 in cards_5:
            analyze_reconr_card_5(card_5)

        # card_6 must be defined 'ngrid' times for each card_3 (see card 3).
        ngrid = get_identifier('ngrid', card_3_statement_list)
        if not_defined(ngrid):
            ngrid_value = 0
        else:
            ngrid_value = get_value(get_r_value(ngrid))
        cards_6 = get_cards('card_6', card_list)
        if len(cards_6) != ngrid_value:
            # Number of card_6 does not match ncards definition in card 3. 
            msg = ('\'card_6\' declared ' + str(len(cards_6)) + ' time(s) ' + 
                   'while \'ngrid\' is set to ' + str(ngrid_value) +
                   ' in \'card_3\', module \'reconr\'.')
            semantic_error(msg, module)
        for card_6 in cards_6:
            analyze_reconr_card_6(card_6)

    return 'ok'

def analyze_reconr_card_1(card_1):
    ''' Return 'ok' if 'card_1' is semantically correct.
        
        Precondition: 'card_1' is a card node from the reconr module with 
                      card_id = (1, '').
    '''
    statement_list = card_1['statement_list']

    # XXX: Neat to construct a list of identifiers which must be defined and
    #      check whether they are defined or not?

    nendf = get_identifier('nendf', statement_list)
    # nendf must be defined. Translator cannot guess unit numbers.
    identifier_must_be_defined(nendf, 'nendf', card_1, 'reconr')

    nendf_value = get_value(get_r_value(nendf))
    # The nendf unit number must be an integer.
    value_must_be_int(nendf_value, nendf)

    # The nendf unit number must be in [20,99], or [-99,-20] for binary.
    if ((nendf_value not in range(20, 100)) and
        (nendf_value not in range(-99, -19))):
        msg = 'illegal nendf unit number (' + str(nendf_value) + ').'
        semantic_error(msg, nendf)

    npend = get_identifier('npend', statement_list)
    # npend must be defined. Translator cannot guess unit numbers.
    identifier_must_be_defined(npend, 'npend', card_1, 'reconr')

    npend_value = get_value(get_r_value(npend))
    # The npend unit number must be an integer.
    value_must_be_int(npend_value, npend)

    # The npend unit number must be in [20,99], or [-99,-20] for binary.
    if ((npend_value not in range(20, 100)) and
        (npend_value not in range(-99, -19))):
        msg = 'illegal npend unit number (' + str(npend_value) + ').'
        semantic_error(msg, nendf)

    return 'ok'

def analyze_reconr_card_2(card_2):
    ''' Return 'ok' if 'card_2' is semantically correct.
        
        Precondition: 'card_2' is a card node from the reconr module with 
                      card_id = (2, '').
    '''
    statement_list = card_2['statement_list']
    tlabel = get_identifier('tlabel', statement_list)
    if not_defined(tlabel):
        pass
    else:
        tlabel_value = get_value(get_r_value(tlabel))
        # At most 66 characters are allowed in labels.
        if len(tlabel_value) > 66:
            msg = ('label exceeds 66 character length in \'card_2\',' +
                   'module \'reconr\'.')
            semantic_error(msg, tlabel)
    return 'ok'

def analyze_reconr_card_3(card_3):
    ''' Return 'ok' if 'card_3' is semantically correct.

        Precondition: 'card_3' is a card node from the reconr module with 
                      card_id = (3, '').
    '''
    statement_list = card_3['statement_list']

    mat = get_identifier('mat', statement_list)
    identifier_must_be_defined(mat, 'mat', card_3, 'reconr')

    ncards = get_identifier('ncards', statement_list)
    if not_defined(ncards):
        pass
    else:
        ncards_value = get_value(get_r_value(ncards))
        value_must_be_int(ncards_value, ncards)

    ngrid = get_identifier('ngrid', statement_list)
    if not_defined(ngrid):
        pass
    else:
        ngrid_value = get_value(get_r_value(ngrid))
        value_must_be_int(ngrid_value, ngrid)

    return 'ok'

def analyze_reconr_card_4(card_4):
    ''' Return 'ok' if 'card_4' is semantically correct.

        Precondition: 'card_4' is a card node from the reconr module with 
                      card_id = (4, '').
    '''
    statement_list = card_4['statement_list']
    err = get_identifier('err', statement_list)
    identifier_must_be_defined(err, 'err', card_4, 'reconr')
    return 'ok'

def analyze_reconr_card_5(card_5):
    ''' Return 'ok' if 'card_5' is semantically correct.

        Precondition: 'card_5' is a card node from the reconr module with 
                      card_id = (5, '').
    '''
    statement_list = card_5['statement_list']

    cards = get_identifier('cards', statement_list)
    identifier_must_be_defined(cards, 'cards', card_5, 'reconr')
    cards_value = get_value(get_r_value(cards))
    value_must_be_string(cards_value, cards)
    return 'ok'

def analyze_reconr_card_6(card_6):
    ''' Return 'ok' if 'card_6' is semantically correct.

        Precondition: 'card_6' is a card node from the reconr module with 
                      card_id = (6, '').
    '''
    statement_list = card_6['statement_list']
    enode = get_identifier('enode', statement_list)
    identifier_must_be_defined(enode, 'enode', card_6, 'reconr')
    return 'ok'

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

def identifier_must_be_defined(id, id_name, card_node, module_name):
    if id is None:
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
# Helpers.

### Getter helpers.

def get_card(card, card_list):
    '''
        Return card node of 'card' if 'card' is in 'card_list', else None.
    '''
    for c in card_list:
        if c['card_name'] == card:
            return c
    return None

def get_cards(card_name, card_list):
    '''
        Return a list of card nodes with card name 'card_name' if 'card_name'
        is in 'card_list'.
    '''
    cards = list()
    for c in card_list:
        if c['card_name'] == card_name:
            cards.append(c)
    return cards

def get_identifier(id, statement_list):
    '''
        Return identifier node of 'id' if 'id' is in 'statement_list',
        else None.
    '''
    for expression in statement_list:
        if is_assignment(expression) and expression['identifier'] == id:
            return expression
    return None

def get_r_value(assignment):
    '''
        Return the r_value node of the 'assignment' node.
    '''
    return assignment['r_value']

def get_value(r_value):
    '''
        Return the value of the 'r_value' node.
    '''
    return r_value['value']

### Boolean helpers.

def is_assignment(expr):
    '''
        Return True if 'expr' is an assignment node, else False.
    '''
    return expr['node_type'] == '='

def not_defined(node):
    '''Return True if 'node' is None, else False.'''
    return node is None

### Misc helpers.

# XXX: Better to raise an exception and catch on a higher level?
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
