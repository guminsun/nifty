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
    # The number of card 2's defines the number of card 3 through 13.
    number_of_card_2 = len(env.get_cards('card_2', module))
    # XXX: Check for at least two card 2's? One definition and one which
    # indicates end of plotr job?
    # The last card 2 should not be considered as a new plot index. It is
    # expected to terminate the execution of plotr.
    # Therefore, 'number_of_card_2-1' is used to create the range to iterate
    # over.
    for c2 in range(number_of_card_2-1):
        card_2, iplot = analyze_plotr_card_2(env.next(card_iter), module)

    # The last card 2 should be defined with iplot = 99, to terminate the
    # plotting job.
    analyze_plotr_card_2_stop(env.next(card_iter), module)
    rule.no_card_allowed(env.next(card_iter), module)
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
    return analyze_color('ipcol', node, card, module)

def analyze_plotr_card_2(card, module):
    rule.card_must_be_defined('card_2', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    iplot = analyze_plotr_card_2_iplot(env.next(stmt_iter), card, module)
    analyze_plotr_card_2_iwcol(env.next(stmt_iter), card, module)
    analyze_plotr_card_2_factx(env.next(stmt_iter), card, module)
    analyze_plotr_card_2_facty(env.next(stmt_iter), card, module)
    # xll, yll pair.
    analyze_plotr_card_2_xll_yll(env.next(stmt_iter), card, module)
    # ww, wh, wr triplet.
    analyze_plotr_card_2_ww_wh_wr(env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card, iplot

def analyze_plotr_card_2_stop(card, module):
    msg = ('expected \'card_2\' with the plot index (\'iplot\') set to 99 ' +
           'to indicate termination of module \'plotr\'.')
    rule.card_must_be_defined('card_2', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    iplot = analyze_plotr_card_2_iplot(env.next(stmt_iter), card, module)
    # The last card is expected to be a card 2 with iplot = 99, to indicate
    # termination of plotr.
    if iplot != 99:
        rule.semantic_error(msg, card)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card, iplot

def analyze_plotr_card_2_iplot(node, card, module):
    # Plot index does not have to be defined, defaults to 1, meaning new axes,
    # new page.
    if node is None:
        return 1
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('iplot', l_value, card, module)
        iplot = rule.must_be_int(l_value, r_value, card, module)
        # XXX: Additional checks?
        return iplot

def analyze_plotr_card_2_iwcol(node, card, module):
    # Window color (iwcol) does not have to be defined, defaults to 0 meaning
    # white page color.
    return analyze_color('iwcol', node, card, module)

def analyze_plotr_card_2_factx(node, card, module):
    # Factor for energies does not have to be defined, defaults to 1.0.
    return analyze_factor('factx', node, card, module)

def analyze_plotr_card_2_facty(node, card, module):
    # Factor for cross-sections does not have to be defined, defaults to 1.0.
    return analyze_factor('facty', node, card, module)

def analyze_plotr_card_2_xll_yll(node, card, module):
    # Lower left corner of plot area (pair: xll, yll) does not have to be
    # defined, defaults to 0, 0 (a pair value).
    if node is None:
        return 0, 0
    else:
        # Expecting a pair.
        l_value_pair, r_value_pair = rule.analyze_pair(node, card, module)
        # xll and yll are expected to be regular identifiers, as such None is
        # given as the array index to indicate that they have none.
        expected_pair = (('xll', None), ('yll', None))
        rule.pair_must_be_defined(expected_pair, l_value_pair, r_value_pair, card, module)
        # XXX: Additional checks?
        xll = r_value_pair[0].get('value')
        yll = r_value_pair[1].get('value')
        return xll, yll

def analyze_plotr_card_2_ww_wh_wr(node, card, module):
    # Triplet: window width (ww), height (wh), and rotation angle (wr) does
    # not have to be defined, defaults to XXX?
    if node is None:
        # XXX: Defaults not documented. Investigate NJOY source code to dig it
        # up. Pass None triplet for now since the return value of this
        # function isn't used in the translator anyway.
        return None, None, None
    else:
        # Expecting a triplet.
        l_value_triplet, r_value_triplet = rule.analyze_triplet(node, card, module)
        # The triplet ww, wh, wr is expected to be defined as regular
        # identifiers, as such None is given as the array index to indicate
        # that the identifiers have none.
        expected_triplet = (('ww', None), ('wh', None), ('wr', None))
        rule.triplet_must_be_defined(expected_triplet, l_value_triplet, r_value_triplet, card, module)
        # XXX: Additional checks?
        ww = r_value_triplet[0].get('value')
        wh = r_value_triplet[1].get('value')
        wr = r_value_triplet[2].get('value')
        return ww, wh, wr

### Local helpers:

def analyze_color(name, node, card, module):
    # Color does not have to be defined, defaults to 0 meaning white.
    if node is None:
        return 0
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined(name, l_value, card, module)
        color = rule.must_be_int(l_value, r_value, card, module)
        if color not in range(0,8):
            id_name = l_value.get('name')
            card_name = card.get('card_name')
            module_name = module.get('module_name')
            msg = ('illegal color option in \'' + card_name + '\', ' +
                   'module \'' + module_name + '\'. Expected an integer in ' +
                   'the range [0,7] (default = 0, meaning white).')
            rule.semantic_error(msg, node)
        return color

def analyze_factor(name, node, card, module):
    # Factor does not have to be defined, defaults to 1.0.
    if node is None:
        return 1.0
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined(name, l_value, card, module)
        # XXX: Additional checks? Must be float?
        return r_value.get('value')
