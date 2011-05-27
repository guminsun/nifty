from nifty.environment import helpers as env
from nifty.environment.exceptions import OrganizeError
from nifty.environment.exceptions import SemanticError
import organizer_helpers as helper

##############################################################################
# Organize viewr. Put together into an orderly, functional, structured whole.

def organize_viewr(module):
    card_list = module.get('card_list')
    organize_card_list(card_list, module)
    return module

def organize_card_list(card_list, module):
    for card in card_list:
        card = organize_card(card, module)
    return card_list

def organize_card(card, module):
    function_map = {
        'card_0' : organize_card_0,
        'card_1' : organize_card_1,
        'card_2' : organize_card_2,
        'card_3' : organize_card_3,
        'card_3a' : organize_card_3a,
        'card_4' : organize_card_4,
        'card_5' : organize_card_5,
        'card_5a' : organize_card_5a,
        'card_6' : organize_card_6,
        'card_6a' : organize_card_6a,
        'card_7' : organize_card_7,
        'card_7a' : organize_card_7a,
        'card_8' : organize_card_8,
        'card_9' : organize_card_9,
        'card_10' : organize_card_10,
        'card_10a' : organize_card_10a,
        'card_11' : organize_card_11,
        'card_12' : organize_card_12,
        'card_13' : organize_card_13,
        'card_14' : organize_card_14,
        'card_14a' : organize_card_14a,
    }
    card_name = card.get('card_name')
    card_function = function_map.get(card_name, card_dummy)
    try:
        card = card_function(card, module)
    except OrganizeError:
        pass
    except SemanticError:
        pass
    return card

def card_dummy(card):
    return card

def organize_card_0(card, module):
    expected_map = {
        0 : ('identifier', ('infile', None)),
        1 : ('identifier', ('nps', None)),
    }
    return helper.organize_card(expected_map, card)

def organize_card_1(card, module):
    expected_map = {
        0 : ('identifier', ('lori', 1)),
        1 : ('identifier', ('istyle', 2)),
        2 : ('identifier', ('size', 0.30)),
        3 : ('identifier', ('ipcol', 0)),
    }
    return helper.organize_card(expected_map, card)

def organize_card_2(card, module):
    # Default values for ww and wh depends on the page orientation (lori),
    # defined in card 1.
    #
    # According to the NJOY source code: default paper size is US letter size,
    # default page size is paper size with 0.5 inches margins all around.
    #
    # If page orientation is portrait (lori = 0) then the page size is
    # 7.5 x 10 inches, else if the page orientation is landscape (lori = 1)
    # then the page size is 10 x 7.5 inches.
    # Rotation angle, 'wr', defaults to 0.
    card_1 = env.get_card('card_1', module)
    lori = helper.get_identifier_value('lori', card_1)
    if lori == 0:
        ww = 7.5
        wh = 10.0
    else:
        ww = 10.0
        wh = 7.5
    expected_map = {
        0 : ('identifier', ('iplot', 1)),
        1 : ('identifier', ('iwcol', 0)),
        2 : ('identifier', ('factx', 1.0)),
        3 : ('identifier', ('facty', 1.0)),
        4 : ('identifier', ('xll', 0.0)),
        5 : ('identifier', ('yll', 0.0)),
        6 : ('identifier', ('ww', ww)),
        7 : ('identifier', ('wh', wh)),
        8 : ('identifier', ('wr', 0)),
    }
    return helper.organize_card(expected_map, card)

def organize_card_3(card, module):
    # No need to organize card 3 since it only contains one identifier.
    return card

def organize_card_3a(card, module):
    # No need to organize card 3a since it only contains one identifier.
    return card

def organize_card_4(card, module):
    expected_map = {
        0 : ('identifier', ('itype', 4)),
        1 : ('identifier', ('jtype', 0)),
        2 : ('identifier', ('igrid', 2)),
        3 : ('identifier', ('ileg', 0)),
        4 : ('identifier', ('xtag', 0)),
        5 : ('identifier', ('ytag', 0)),
    }
    return helper.organize_card(expected_map, card)

def organize_card_5(card, module):
    expected_map = {
        0 : ('identifier', ('xmin', None)),
        1 : ('identifier', ('xmax', None)),
        # XXX: empty string is used to denote default automatic scales, since
        # it will be outputted as a blank.
        2 : ('identifier', ('xstep', '')),
    }
    # 'xmin' and 'xmax' are either both defined, or both undefined. 'xstep' is
    # optional. Hence, only organize when there are statements to organize.
    if len(card.get('statement_list')) > 0:
        return helper.organize_card(expected_map, card)
    else:
        return card

def organize_card_5a(card, module):
    # No need to organize card 5a since it only contains one identifier.
    return card

def organize_card_6(card, module):
    expected_map = {
        0 : ('identifier', ('ymin', None)),
        1 : ('identifier', ('ymax', None)),
        # XXX: empty string is used to denote default automatic scales, since
        # it will be outputted as a blank.
        2 : ('identifier', ('ystep', '')),
    }
    # 'ymin' and 'ymax' are either both defined, or both undefined. 'ystep' is
    # optional. Hence, only organize when there are statements to organize.
    if len(card.get('statement_list')) > 0:
        return helper.organize_card(expected_map, card)
    else:
        return card

def organize_card_6a(card, module):
    # No need to organize card 6a since it only contains one identifier.
    return card

def organize_card_7(card, module):
    expected_map = {
        0 : ('identifier', ('rmin', None)),
        1 : ('identifier', ('rmax', None)),
        # XXX: empty string is used to denote default automatic scales, since
        # it will be outputted as a blank.
        2 : ('identifier', ('rstep', '')),
    }
    # 'rmin' and 'rmax' are either both defined, or both undefined. 'rstep' is
    # optional. Hence, only organize when there are statements to organize.
    if len(card.get('statement_list')) > 0:
        return helper.organize_card(expected_map, card)
    else:
        return card

def organize_card_7a(card, module):
    # No need to organize card 7a since it only contains one identifier.
    return card

def organize_card_8(card, module):
    # No need to organize card 8 since it only contains one identifier.
    return card

def organize_card_9(card, module):
    expected_map = {
        0 : ('identifier', ('icon', 0)),
        1 : ('identifier', ('isym', 0)),
        2 : ('identifier', ('idash', 0)),
        3 : ('identifier', ('iccol', 0)),
        4 : ('identifier', ('ithick', 1)),
        5 : ('identifier', ('ishade', 0)),
    }
    return helper.organize_card(expected_map, card)

def organize_card_10(card, module):
    # No need to organize card 10 since it only contains one identifier.
    return card

def organize_card_10a(card, module):
    expected_map = {
        0 : ('identifier', ('xtag', 0)),
        1 : ('identifier', ('ytag', 0)),
        2 : ('identifier', ('xpoint', 0)),
    }
    return helper.organize_card(expected_map, card)

def organize_card_11(card, module):
    expected_map = {
        0 : ('identifier', ('xv', 15.0)),
        1 : ('identifier', ('yv', -15.0)),
        2 : ('identifier', ('zv', 15.0)),
        3 : ('identifier', ('x3', 2.5)),
        4 : ('identifier', ('y3', 6.5)),
        5 : ('identifier', ('z3', 2.5)),
    }
    return helper.organize_card(expected_map, card)

def organize_card_12(card, module):
    # No need to organize card 12 since it only contains one identifier.
    return card

def organize_card_13(card, module):
    expected_map = {
        # XXX: Default values unknown. Use None instead to force 'em to be
        # specified?
        0 : ('identifier', ('xdata', '')),
        1 : ('identifier', ('ydata', '')),
        2 : ('identifier', ('yerr1', '')),
        3 : ('identifier', ('yerr2', '')),
        4 : ('identifier', ('xerr1', '')),
        5 : ('identifier', ('xerr2', '')),
    }
    return helper.organize_card(expected_map, card)

def organize_card_14(card, module):
    # No need to organize card 14 since it only contains one identifier.
    return card

def organize_card_14a(card, module):
    expected_map = {
        # XXX: Assuming that 'x' and 'z' needs to be defined. Need to verify
        # with the NJOY source code.
        0 : ('identifier', ('x', None)),
        1 : ('identifier', ('z', None)),
    }
    return helper.organize_card(expected_map, card)
