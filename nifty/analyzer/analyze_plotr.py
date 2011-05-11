from nifty.environment import helpers as env
import analyzer_rules as rule

##############################################################################
# Analyze plotr. Checks if plotr is somewhat semantically correct.

def analyze_plotr(module):
    analyze_plotr_card_list(module)
    return module

def analyze_plotr_card_list(module):
    card_iter = env.get_card_iterator(module)
    analyze_plotr_card_0(env.next(card_iter), module)
    analyze_plotr_card_1(env.next(card_iter), module)
    # XXX: rule.no_card_allowed(env.next(card_iter), module)
    return module

def analyze_plotr_card_0(card, module):
    rule.card_must_be_defined('card_0', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    rule.analyze_unit_number('nplt', env.next(stmt_iter), card, module)
    rule.analyze_optional_unit_number('nplt0', env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_plotr_card_1(card, module):
    rule.card_must_be_defined('card_1', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    analyze_plotr_card_1_lori(env.next(stmt_iter), card, module)
    analyze_plotr_card_1_istyle(env.next(stmt_iter), card, module)
    analyze_plotr_card_1_size(env.next(stmt_iter), card, module)
    analyze_plotr_card_1_ipcol(env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_plotr_card_1_lori(node, card, module):
    # Page orientation (lori) does not have to be defined, defaults to 1
    # meaning landscape orientation.
    if node is None:
        return 1
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('lori', l_value, card, module)
        lori = rule.must_be_int(l_value, r_value, card, module)
        if lori not in range(0,2):
            id_name = l_value.get('name')
            card_name = card.get('card_name')
            module_name = module.get('module_name')
            msg = ('illegal page orientation in \'' + card_name + '\', ' +
                   'module \'' + module_name + '\'. Expected 0 for portrait ' +
                   'or 1 for landscape orientation (default = 1).')
            rule.semantic_error(msg, node)
    return lori

def analyze_plotr_card_1_istyle(node, card, module):
    # Character style (istyle) does not have to be defined, defaults to 2
    # meaning swiss character style.
    if node is None:
        return 2
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('istyle', l_value, card, module)
        istyle = rule.must_be_int(l_value, r_value, card, module)
        if istyle not in range(1,3):
            id_name = l_value.get('name')
            card_name = card.get('card_name')
            module_name = module.get('module_name')
            msg = ('illegal character style in \'' + card_name + '\', ' +
                   'module \'' + module_name + '\'. Expected 1 for roman ' +
                   'or 2 for swiss character style (default = 2).')
            rule.semantic_error(msg, node)
    return istyle

def analyze_plotr_card_1_size(node, card, module):
    # Character size option (size) does not have to be defined, defaults to
    # 0.3 (height in page units).
    if node is None:
        return 0.3
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('size', l_value, card, module)
        # XXX: Additional checks? Must be number?
    return r_value.get('value')

def analyze_plotr_card_1_ipcol(node, card, module):
    # Page color (ipcol) does not have to be defined, defaults to 0 meaning
    # white page color.
    if node is None:
        return 0
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('ipcol', l_value, card, module)
        ipcol = rule.must_be_int(l_value, r_value, card, module)
        if ipcol not in range(0,8):
            id_name = l_value.get('name')
            card_name = card.get('card_name')
            module_name = module.get('module_name')
            msg = ('illegal page color option in \'' + card_name + '\', ' +
                   'module \'' + module_name + '\'. Expected an integer in ' +
                   'the range [0,7] (default = 0, meaning white).')
            rule.semantic_error(msg, node)
    return ipcol
