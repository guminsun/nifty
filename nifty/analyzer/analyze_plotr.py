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
    card_1, lori = analyze_plotr_card_1(env.next(card_iter), module)
    # The number of card 2's defines the number of cards 3 through 13.
    number_of_card_2 = len(env.get_cards('card_2', module))
    # XXX: Check for at least two card 2's? There's at least one definition
    # and one which indicates end of plotr job?
    # The last card 2 should not be considered as a new plot index. It is
    # expected to terminate the execution of plotr. Therefore,
    # 'number_of_card_2-1' is used to create the range to iterate over.
    for c2 in range(number_of_card_2-1):
        card_2, iplot = analyze_plotr_card_2(lori, env.next(card_iter), module)
        # Card 3 through 7 should only be defined if iplot = 1 or iplot = -1.
        if abs(iplot) == 1:
            analyze_plotr_card_3(env.next(card_iter), module)
            analyze_plotr_card_3a(env.next(card_iter), module)
            c4, itype, jtype, ileg = analyze_plotr_card_4(env.next(card_iter), module)
            analyze_plotr_card_5(env.next(card_iter), module)
            analyze_plotr_card_5a(env.next(card_iter), module)
            analyze_plotr_card_6(env.next(card_iter), module)
            analyze_plotr_card_6a(env.next(card_iter), module)
            # Card 7 and 7a should only be defined if jtype in card 4 is > 0.
            if jtype > 0:
                analyze_plotr_card_7(env.next(card_iter), module)
                analyze_plotr_card_7a(env.next(card_iter), module)
        # Card 8 through 13 is always defined regardless of iplot value.
        card_8, iverf = analyze_plotr_card_8(env.next(card_iter), module)
        # Card 9 and 10 should only be defined for 2D plots (i.e. if itype
        # is positive.)
        if itype > 0:
            analyze_plotr_card_9(env.next(card_iter), module)
            # Card 10 should only be defined if ileg != 0.
            if ileg != 0:
                analyze_plotr_card_10(env.next(card_iter), module)
            # Card 10a should only be defined if ileg = 2.
            if ileg == 2:
                analyze_plotr_card_10a(env.next(card_iter), module)
        # Card 11 should only be defined for 3D plots.
        else:
            analyze_plotr_card_11(env.next(card_iter), module)
        # Card 12 and 13 should only be defined if iverf in card 8 is 0.
        if iverf == 0:
            card_12, nform = analyze_plotr_card_12(env.next(card_iter), module)
            # Card 13 should only be defined when nform = 0 in card 12.
            if nform == 0:
                # An unknown number of card 13's can be defined, keep
                # analyzing them until an empty card 13 is seen.
                while True:
                    card_13, card_13_stmt_len = analyze_plotr_card_13(env.next(card_iter), module)
                    if card_13_stmt_len == 0:
                        break
    # The last card should be card 2 which have been defined with iplot = 99,
    # to terminate the plotting job.
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
    lori = analyze_plotr_card_1_lori(env.next(stmt_iter), card, module)
    analyze_plotr_card_1_istyle(env.next(stmt_iter), card, module)
    analyze_plotr_card_1_size(env.next(stmt_iter), card, module)
    analyze_plotr_card_1_ipcol(env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card, lori

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

def analyze_plotr_card_2(lori, card, module):
    rule.card_must_be_defined('card_2', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    iplot = analyze_plotr_card_2_iplot(env.next(stmt_iter), card, module)
    analyze_plotr_card_2_iwcol(env.next(stmt_iter), card, module)
    analyze_plotr_card_2_factx(env.next(stmt_iter), card, module)
    analyze_plotr_card_2_facty(env.next(stmt_iter), card, module)
    # XXX: Is xll and yll supposed to be defined as a pair?
    analyze_plotr_card_2_xll(env.next(stmt_iter), card, module)
    analyze_plotr_card_2_yll(env.next(stmt_iter), card, module)
    # ww, wh and wr is not defined as a triplet even though it appears like it
    # in the documentation.
    analyze_plotr_card_2_ww(lori, env.next(stmt_iter), card, module)
    analyze_plotr_card_2_wh(lori, env.next(stmt_iter), card, module)
    analyze_plotr_card_2_wr(env.next(stmt_iter), card, module)
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

def analyze_plotr_card_2_xll(node, card, module):
    # Lower left corner of plot area (pair: xll, yll) does not have to be
    # defined, defaults to 0 and 0.
    if node is None:
        return 0
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('xll', l_value, card, module)
        # XXX: Additional checks?
        return r_value.get('value')

def analyze_plotr_card_2_yll(node, card, module):
    # Lower left corner of plot area (pair: xll, yll) does not have to be
    # defined, defaults to 0 and 0.
    if node is None:
        return 0
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('yll', l_value, card, module)
        # XXX: Additional checks?
        return r_value.get('value')

def analyze_plotr_card_2_ww(lori, node, card, module):
    # Triplet: window width (ww), height (wh), and rotation angle (wr) does
    # not have to be defined.
    # Default values for ww and wh depends on the page orientation (lori):
    #
    # According to the NJOY source code: default paper size is US letter size,
    # default page size is paper size with 0.5in margins all around.
    #
    # If page orientation (lori) is portrait then the page size is 7.5 x 10
    # inches, else if the page orientation is landscape then the page size is
    # 10 x 7.5 inches (Rotation angle, 'wr', defaults to 0).
    if node is None:
        if lori == 0:
            return 7.5
        else:
            return 10.0
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('ww', l_value, card, module)
        # XXX: Additional checks?
        return r_value.get('value')

def analyze_plotr_card_2_wh(lori, node, card, module):
    if node is None:
        if lori == 0:
            return 10.0
        else:
            return 7.5
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('wh', l_value, card, module)
        # XXX: Additional checks?
        return r_value.get('value')

def analyze_plotr_card_2_wr(node, card, module):
    if node is None:
        return 0
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('wr', l_value, card, module)
        # XXX: Additional checks?
        return r_value.get('value')

def analyze_plotr_card_3(card, module):
    msg = ('expected \'card_3\' since the plot index (\'iplot\') is 1 or ' +
           '-1 in \'card_2\'.')
    rule.card_must_be_defined('card_3', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    # First line of title (t1) does not have to be defined, defaults to empty
    # string.
    rule.analyze_optional_string(60, 't1', env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_plotr_card_3a(card, module):
    msg = ('expected \'card_3a\' since the plot index (\'iplot\') is 1 or ' +
           '-1 in \'card_2\'.')
    rule.card_must_be_defined('card_3a', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    # Second line of title (t2) does not have to be defined, defaults to empty
    # string.
    rule.analyze_optional_string(60, 't2', env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_plotr_card_4(card, module):
    msg = ('expected \'card_4\' since the plot index (\'iplot\') is 1 or ' +
           '-1 in \'card_2\'.')
    rule.card_must_be_defined('card_4', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    itype = analyze_plotr_card_4_itype(env.next(stmt_iter), card, module)
    jtype = analyze_plotr_card_4_jtype(env.next(stmt_iter), card, module)
    analyze_plotr_card_4_igrid(env.next(stmt_iter), card, module)
    ileg = analyze_plotr_card_4_ileg(env.next(stmt_iter), card, module)
    # XXX: Is xtag and ytag a possible pair definition?
    analyze_plotr_card_4_xtag(env.next(stmt_iter), card, module)
    analyze_plotr_card_4_ytag(env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card, itype, jtype, ileg

def analyze_plotr_card_4_itype(node, card, module):
    # Type for primary axes does not have to be defined, defaults to 4,
    # meaning log x - log y. (Negative number indicates 3D plot.)
    if node is None:
        return 4
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('itype', l_value, card, module)
        itype = rule.must_be_int(l_value, r_value, card, module)
        if abs(itype) not in range(1,5):
            id_name = l_value.get('name')
            card_name = card.get('card_name')
            module_name = module.get('module_name')
            msg = ('illegal type for primary axes (\'' + id_name + '\') in ' +
                   '\'' + card_name + '\', ' + 'module \'' + module_name +
                   '\'.')
            rule.semantic_error(msg, node)
        return itype

def analyze_plotr_card_4_jtype(node, card, module):
    # Type for alternate y axis or z axis does not have to be defined,
    # defaults to 0, meaning none.
    if node is None:
        return 0
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('jtype', l_value, card, module)
        jtype = rule.must_be_int(l_value, r_value, card, module)
        if jtype not in range(0,3):
            id_name = l_value.get('name')
            card_name = card.get('card_name')
            module_name = module.get('module_name')
            msg = ('illegal type for alternate y axis or z axis (\'' +
                   id_name + '\') in \'' + card_name + '\', ' + 'module \'' +
                   module_name + '\'.')
            rule.semantic_error(msg, node)
        return jtype

def analyze_plotr_card_4_igrid(node, card, module):
    # Grid and tic mark control does not have to be defined, defaults to 2,
    # meaning tic marks on outside.
    if node is None:
        return 2
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('igrid', l_value, card, module)
        igrid = rule.must_be_int(l_value, r_value, card, module)
        if igrid not in range(0,4):
            id_name = l_value.get('name')
            card_name = card.get('card_name')
            module_name = module.get('module_name')
            msg = ('illegal grid and tic mark control (\'' + id_name +
                   '\') in \'' + card_name + '\', ' + 'module \'' +
                   module_name + '\'.')
            rule.semantic_error(msg, node)
        return igrid

def analyze_plotr_card_4_ileg(node, card, module):
    # Option to write a legend does not have to be defined, defaults to 0,
    # meaning no legend.
    if node is None:
        return 0
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('ileg', l_value, card, module)
        ileg = rule.must_be_int(l_value, r_value, card, module)
        if ileg not in range(0,3):
            id_name = l_value.get('name')
            card_name = card.get('card_name')
            module_name = module.get('module_name')
            msg = ('illegal option to write a legend (\'' + id_name +
                   '\') in \'' + card_name + '\', ' + 'module \'' +
                   module_name + '\' (default = 0, meaning no legend).')
            rule.semantic_error(msg, node)
        return ileg

def analyze_plotr_card_4_xtag(node, card, module):
    # x coordinate of upper left corner of legend block does not have to be
    # defined, defaults to 0.
    if node is None:
        return 0
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('xtag', l_value, card, module)
        # XXX: Additional checks?
        return r_value.get('value')

def analyze_plotr_card_4_ytag(node, card, module):
    # y coordinate of upper left corner of legend block does not have to be
    # defined, defaults to 0.
    if node is None:
        return 0
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('ytag', l_value, card, module)
        # XXX: Additional checks?
        return r_value.get('value')

def analyze_plotr_card_5(card, module):
    msg = ('expected \'card_5\' since the plot index (\'iplot\') is 1 or ' +
           '-1 in \'card_2\'.')
    rule.card_must_be_defined('card_5', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    # 'el' and 'eh' are either both defined, or both undefined. 'xstep' is
    # optional.
    if len(stmt_iter) > 0:
        analyze_plotr_card_5_el(env.next(stmt_iter), card, module)
        analyze_plotr_card_5_eh(env.next(stmt_iter), card, module)
        analyze_plotr_card_5_xstep(env.next(stmt_iter), card, module)
        rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_plotr_card_5_el(node, card, module):
    # Lowest energy to be plotted.
    l_value, r_value = rule.analyze_singleton(node, card, module)
    rule.identifier_must_be_defined('el', l_value, card, module)
    # XXX: Additional checks?
    return r_value.get('value')

def analyze_plotr_card_5_eh(node, card, module):
    # Highest energy to be plotted.
    l_value, r_value = rule.analyze_singleton(node, card, module)
    rule.identifier_must_be_defined('eh', l_value, card, module)
    # XXX: Additional checks?
    return r_value.get('value')

def analyze_plotr_card_5_xstep(node, card, module):
    if node is None:
        return None
    else:
        # x axis step for energy to be plotted, default = automatic scales.
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('xstep', l_value, card, module)
        # XXX: Additional checks?
        return r_value.get('value')

def analyze_plotr_card_5a(card, module):
    msg = ('expected \'card_5a\' since the plot index (\'iplot\') is 1 or ' +
           '-1 in \'card_2\'.')
    rule.card_must_be_defined('card_5a', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    analyze_plotr_card_5a_xlabl(env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_plotr_card_5a_xlabl(node, card, module):
    # Label for x axis does not have to be defined, defaults to "energy (ev)".
    if node is None:
        return 'energy (ev)'
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('xlabl', l_value, card, module)
        # The r-value of the assignment is expected to be a string.
        string = rule.must_be_string(l_value, r_value, card, module)
        rule.string_must_not_exceed_length(l_value, r_value, 60, card, module)
        return string

def analyze_plotr_card_6(card, module):
    msg = ('expected \'card_6\' since the plot index (\'iplot\') is 1 or ' +
           '-1 in \'card_2\'.')
    rule.card_must_be_defined('card_6', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    # 'yl' and 'yh' are either both defined, or both undefined. 'ystep' is
    # optional.
    if len(stmt_iter) > 0:
        analyze_plotr_card_6_yl(env.next(stmt_iter), card, module)
        analyze_plotr_card_6_yh(env.next(stmt_iter), card, module)
        analyze_plotr_card_6_ystep(env.next(stmt_iter), card, module)
        rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_plotr_card_6_yl(node, card, module):
    # Lowest value of y axis.
    l_value, r_value = rule.analyze_singleton(node, card, module)
    rule.identifier_must_be_defined('yl', l_value, card, module)
    # XXX: Additional checks?
    return r_value.get('value')

def analyze_plotr_card_6_yh(node, card, module):
    # Highest value of y axis.
    l_value, r_value = rule.analyze_singleton(node, card, module)
    rule.identifier_must_be_defined('yh', l_value, card, module)
    # XXX: Additional checks?
    return r_value.get('value')

def analyze_plotr_card_6_ystep(node, card, module):
    if node is None:
        return None
    else:
        # Step for y axis. Default -> automatic scales.
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('ystep', l_value, card, module)
        # XXX: Additional checks?
        return r_value.get('value')

def analyze_plotr_card_6a(card, module):
    msg = ('expected \'card_6a\' since the plot index (\'iplot\') is 1 or ' +
           '-1 in \'card_2\'.')
    rule.card_must_be_defined('card_6a', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    analyze_plotr_card_6a_ylabl(env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_plotr_card_6a_ylabl(node, card, module):
    # Label for y axis does not have to be defined, defaults to
    # "cross section (barns)".
    if node is None:
        return 'cross section (barns)'
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('ylabl', l_value, card, module)
        # The r-value of the assignment is expected to be a string.
        string = rule.must_be_string(l_value, r_value, card, module)
        rule.string_must_not_exceed_length(l_value, r_value, 60, card, module)
        return string

def analyze_plotr_card_7(card, module):
    msg = ('expected \'card_7\' since the plot index (\'iplot\') is 1 or ' +
           '-1 and the type for alternate y axis or z axis (\'jtype\') is ' +
           'defined, in \'card_2\'.')
    rule.card_must_be_defined('card_7', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    # 'rbot' and 'rtop' are either both defined, or both undefined. 'rstep' is
    # optional.
    if len(stmt_iter) > 0:
        analyze_plotr_card_7_rbot(env.next(stmt_iter), card, module)
        analyze_plotr_card_7_rtop(env.next(stmt_iter), card, module)
        analyze_plotr_card_7_rstep(env.next(stmt_iter), card, module)
        rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_plotr_card_7_rbot(node, card, module):
    # Lowest value of secondary y axis or z axis.
    l_value, r_value = rule.analyze_singleton(node, card, module)
    rule.identifier_must_be_defined('rbot', l_value, card, module)
    # XXX: Additional checks?
    return r_value.get('value')

def analyze_plotr_card_7_rtop(node, card, module):
    # Highest value of secondary y axis or z axis.
    l_value, r_value = rule.analyze_singleton(node, card, module)
    rule.identifier_must_be_defined('rtop', l_value, card, module)
    # XXX: Additional checks?
    return r_value.get('value')

def analyze_plotr_card_7_rstep(node, card, module):
    if node is None:
        return None
    else:
        # Step for secondary y axis or z axis.
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('rstep', l_value, card, module)
        # XXX: Additional checks?
        return r_value.get('value')

def analyze_plotr_card_7a(card, module):
    msg = ('expected \'card_7a\' since the plot index (\'iplot\') is 1 or ' +
           '-1 and the type for alternate y axis or z axis (\'jtype\') is ' +
           'defined, in \'card_2\'.')
    rule.card_must_be_defined('card_7a', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    rule.analyze_optional_string(60, 'rl', env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_plotr_card_8(card, module):
    rule.card_must_be_defined('card_8', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    iverf = analyze_plotr_card_8_iverf(env.next(stmt_iter), card, module)
    # Ignore rest of parameters on card if data on input file is used (i.e. if
    # iverf = 0.)
    if iverf != 0:
        rule.analyze_unit_number('nin', env.next(stmt_iter), card, module)
        rule.analyze_material('matd', env.next(stmt_iter), card, module)
        analyze_plotr_card_8_mfd(env.next(stmt_iter), card, module)
        analyze_plotr_card_8_mtd(env.next(stmt_iter), card, module)
        analyze_plotr_card_8_temper(env.next(stmt_iter), card, module)
        # Triplet nth,ntp,nkh
        analyze_plotr_card_8_nth_ntp_nkh(env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card, iverf

def analyze_plotr_card_8_iverf(node, card, module):
    # Version of ENDF tape.
    l_value, r_value = rule.analyze_singleton(node, card, module)
    rule.identifier_must_be_defined('iverf', l_value, card, module)
    iverf = rule.must_be_int(l_value, r_value, card, module)
    # XXX: Additional checks?
    return iverf

def analyze_plotr_card_8_mfd(node, card, module):
    l_value, r_value = rule.analyze_singleton(node, card, module)
    rule.identifier_must_be_defined('mfd', l_value, card, module)
    mfd = rule.must_be_int(l_value, r_value, card, module)
    # XXX: Additional checks?
    return mfd

def analyze_plotr_card_8_mtd(node, card, module):
    l_value, r_value = rule.analyze_singleton(node, card, module)
    rule.identifier_must_be_defined('mtd', l_value, card, module)
    # XXX: Additional checks?
    return r_value.get('value')

def analyze_plotr_card_8_temper(node, card, module):
    if node is None:
        return 0.0
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('temper', l_value, card, module)
        # XXX: Additional checks?
        return r_value.get('value')

def analyze_plotr_card_8_nth_ntp_nkh(node, card, module):
    if node is None:
        return 1, 1, 1
    else:
        # Expecting a triplet.
        l_value_triplet, r_value_triplet = rule.analyze_triplet(node, card, module)
        # The triplet nth, ntp, nkh is expected to be defined as regular
        # identifiers, as such None is given as the array index to indicate
        # that the identifiers have none.
        # The order in which the identifiers appears in 'expected_triplet'
        # denotes the expected order of the identifiers in the NIF program.
        expected_triplet = (('nth', None), ('ntp', None), ('nkh', None))
        rule.triplet_must_be_defined(expected_triplet, l_value_triplet, r_value_triplet, card, module)
        # XXX: Additional checks?
        nth = r_value_triplet[0].get('value')
        ntp = r_value_triplet[1].get('value')
        nkh = r_value_triplet[2].get('value')
        return nth, ntp, nkh

def analyze_plotr_card_9(card, module):
    # XXX: Provide a descriptive message of why card 9 should be supplied.
    rule.card_must_be_defined('card_9', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    analyze_plotr_card_9_icon(env.next(stmt_iter), card, module)
    analyze_plotr_card_9_isym(env.next(stmt_iter), card, module)
    analyze_plotr_card_9_idash(env.next(stmt_iter), card, module)
    analyze_plotr_card_9_iccol(env.next(stmt_iter), card, module)
    analyze_plotr_card_9_ithick(env.next(stmt_iter), card, module)
    analyze_plotr_card_9_ishade(env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_plotr_card_9_icon(node, card, module):
    # Symbol and connection option does not have to be defined, defaults to 0.
    if node is None:
        return 0
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('icon', l_value, card, module)
        icon = rule.must_be_int(l_value, r_value, card, module)
        # XXX: Additional checks?
        return icon

def analyze_plotr_card_9_isym(node, card, module):
    # Symbol to be used, default = 0 meaning square symbol.
    if node is None:
        return 0
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('isym', l_value, card, module)
        isym = rule.must_be_int(l_value, r_value, card, module)
        if isym not in range(0,19):
            id_name = l_value.get('name')
            card_name = card.get('card_name')
            module_name = module.get('module_name')
            msg = ('illegal symbol option (\'' + id_name +
                   '\') in \'' + card_name + '\', ' + 'module \'' +
                   module_name + '\' (default = 0, meaning square).')
            rule.semantic_error(msg, node)
        return isym

def analyze_plotr_card_9_idash(node, card, module):
    # Type of line to plot, default = 0 meaning solid line.
    if node is None:
        return 0
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('idash', l_value, card, module)
        idash = rule.must_be_int(l_value, r_value, card, module)
        if idash not in range(0,5):
            id_name = l_value.get('name')
            card_name = card.get('card_name')
            module_name = module.get('module_name')
            msg = ('illegal line option (\'' + id_name +
                   '\') in \'' + card_name + '\', ' + 'module \'' +
                   module_name + '\' (default = 0, meaning solid line).')
            rule.semantic_error(msg, node)
        return idash

def analyze_plotr_card_9_iccol(node, card, module):
    # Curve color, default = 0 meaning black.
    if node is None:
        return 0
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('iccol', l_value, card, module)
        iccol = rule.must_be_int(l_value, r_value, card, module)
        if iccol not in range(0,8):
            id_name = l_value.get('name')
            card_name = card.get('card_name')
            module_name = module.get('module_name')
            msg = ('illegal curve color option (\'' + id_name +
                   '\') in \'' + card_name + '\', ' + 'module \'' +
                   module_name + '\' (default = 0, meaning black).')
            rule.semantic_error(msg, node)
        return iccol

def analyze_plotr_card_9_ithick(node, card, module):
    # Thickness of curve, default = 1.
    if node is None:
        return 1
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('ithick', l_value, card, module)
        ithick = rule.must_be_int(l_value, r_value, card, module)
        # XXX: Additional checks?
        return ithick

def analyze_plotr_card_9_ishade(node, card, module):
    # Shade pattern, default = 0 meaning none.
    if node is None:
        return 0
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('ishade', l_value, card, module)
        ishade = rule.must_be_int(l_value, r_value, card, module)
        if ishade not in range(0,81):
            id_name = l_value.get('name')
            card_name = card.get('card_name')
            module_name = module.get('module_name')
            msg = ('illegal shade pattern option (\'' + id_name +
                   '\') in \'' + card_name + '\', ' + 'module \'' +
                   module_name + '\' (default = 0, meaning none).')
            rule.semantic_error(msg, node)
        return ishade

def analyze_plotr_card_10(card, module):
    # XXX: Provide a descriptive message of why card 10 should be supplied.
    rule.card_must_be_defined('card_10', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    # Title for curve tag or legend block, defaults to blank.
    rule.analyze_optional_string(60, 'aleg', env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_plotr_card_10a(card, module):
    rule.card_must_be_defined('card_10a', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    analyze_plotr_card_10a_xtag(env.next(stmt_iter), card, module)
    analyze_plotr_card_10a_ytag(env.next(stmt_iter), card, module)
    analyze_plotr_card_10a_xpoint(env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_plotr_card_10a_xtag(node, card, module):
    if node is None:
        return 0
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('xtag', l_value, card, module)
        # XXX: Additional checks?
        return r_value.get('value')

def analyze_plotr_card_10a_ytag(node, card, module):
    if node is None:
        return 0
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('ytag', l_value, card, module)
        # XXX: Additional checks?
        return r_value.get('value')

def analyze_plotr_card_10a_xpoint(node, card, module):
    if node is None:
        return 0
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('xpoint', l_value, card, module)
        # XXX: Additional checks?
        return r_value.get('value')

def analyze_plotr_card_11(card, module):
    rule.card_must_be_defined('card_11', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    # Assuming that xv,yv,zv and x3,y3,z3 should not be defined as triplets
    # due to possible float values. E.g. 2.56.52.5 is an odd input to NJOY.
    analyze_plotr_card_11_xv(env.next(stmt_iter), card, module)
    analyze_plotr_card_11_yv(env.next(stmt_iter), card, module)
    analyze_plotr_card_11_zv(env.next(stmt_iter), card, module)
    analyze_plotr_card_11_x3(env.next(stmt_iter), card, module)
    analyze_plotr_card_11_y3(env.next(stmt_iter), card, module)
    analyze_plotr_card_11_z3(env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card

def analyze_plotr_card_11_xv(node, card, module):
    if node is None:
        return 15.0
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('xv', l_value, card, module)
        # XXX: Additional checks?
        return r_value.get('value')

def analyze_plotr_card_11_yv(node, card, module):
    if node is None:
        return -15.0
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('yv', l_value, card, module)
        # XXX: Additional checks?
        return r_value.get('value')

def analyze_plotr_card_11_zv(node, card, module):
    if node is None:
        return 15.0
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('zv', l_value, card, module)
        # XXX: Additional checks?
        return r_value.get('value')

def analyze_plotr_card_11_x3(node, card, module):
    if node is None:
        return 2.5
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('x3', l_value, card, module)
        # XXX: Additional checks?
        return r_value.get('value')

def analyze_plotr_card_11_y3(node, card, module):
    if node is None:
        return 6.5
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('y3', l_value, card, module)
        # XXX: Additional checks?
        return r_value.get('value')

def analyze_plotr_card_11_z3(node, card, module):
    if node is None:
        return 2.5
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('z3', l_value, card, module)
        # XXX: Additional checks?
        return r_value.get('value')

def analyze_plotr_card_12(card, module):
    msg = ('expected \'card_12\' since the ENDF version (\'iverf\') is 0 ' +
           'in \'card_8\'.')
    rule.card_must_be_defined('card_12', card, module, msg)
    stmt_iter = env.get_statement_iterator(card)
    nform = analyze_plotr_card_12_nform(env.next(stmt_iter), card, module)
    rule.no_statement_allowed(env.next(stmt_iter), card, module)
    return card, nform

def analyze_plotr_card_12_nform(node, card, module):
    # Format code for input data.
    l_value, r_value = rule.analyze_singleton(node, card, module)
    rule.identifier_must_be_defined('nform', l_value, card, module)
    nform = rule.must_be_int(l_value, r_value, card, module)
    # XXX: Additional checks?
    return nform

def analyze_plotr_card_13(card, module):
    msg = ('expected a \'card_13\' since \'nform\' is 0 in \'card_12\'.')
    rule.card_must_be_defined('card_13', card, module, None)
    stmt_iter = env.get_statement_iterator(card)
    stmt_len = len(stmt_iter)
    if stmt_len == 0:
        return card, stmt_len
    else:
        analyze_plotr_card_13_xdata(env.next(stmt_iter), card, module)
        analyze_plotr_card_13_ydata(env.next(stmt_iter), card, module)
        analyze_plotr_card_13_yerr1(env.next(stmt_iter), card, module)
        analyze_plotr_card_13_yerr2(env.next(stmt_iter), card, module)
        analyze_plotr_card_13_xerr1(env.next(stmt_iter), card, module)
        analyze_plotr_card_13_xerr2(env.next(stmt_iter), card, module)
        rule.no_statement_allowed(env.next(stmt_iter), card, module)
        return card, stmt_len

def analyze_plotr_card_13_xdata(node, card, module):
    if node is None:
        return 0
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('xdata', l_value, card, module)
        # XXX: Additional checks?
        return r_value.get('value')

def analyze_plotr_card_13_ydata(node, card, module):
    if node is None:
        return 0
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('ydata', l_value, card, module)
        # XXX: Additional checks?
        return r_value.get('value')

def analyze_plotr_card_13_yerr1(node, card, module):
    if node is None:
        return 0
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('yerr1', l_value, card, module)
        # XXX: Additional checks?
        return r_value.get('value')

def analyze_plotr_card_13_yerr2(node, card, module):
    if node is None:
        return 0
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('yerr2', l_value, card, module)
        # XXX: Additional checks?
        return r_value.get('value')

def analyze_plotr_card_13_xerr1(node, card, module):
    if node is None:
        return 0
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('xerr1', l_value, card, module)
        # XXX: Additional checks?
        return r_value.get('value')

def analyze_plotr_card_13_xerr2(node, card, module):
    if node is None:
        return 0
    else:
        l_value, r_value = rule.analyze_singleton(node, card, module)
        rule.identifier_must_be_defined('xerr2', l_value, card, module)
        # XXX: Additional checks?
        return r_value.get('value')

##############################################################################
# Local helpers.

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
