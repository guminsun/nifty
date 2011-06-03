import settings

material_number = settings.material_number
unit_number = settings.unit_number

##############################################################################
# viewr card 0:

# Note that this card is named card 1 in the documentation. The name used by
# the translator is 'card_0' to make it resemble the plotr settings.

# Internal identifier names for card 0. Alter valid_name_list in identifier
# map to add alternative identifier names.
infile = 'infile'
nps = 'nps'

card_0_identifier_map = {
    infile : {
        'internal_name' : infile,
        'is_optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : unit_number,
        },
        'valid_name_list' : [infile, 'input'],
    },
    nps : {
        'internal_name' : nps,
        'is_optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : unit_number,
        },
        'valid_name_list' : [nps, 'output'],
    },
}

card_0_order_map = {
    0 : (infile, None, card_0_identifier_map.get(infile)),
    1 : (nps, None, card_0_identifier_map.get(nps)),
}

##############################################################################
# viewr card 1:

# Internal identifier names for card 1. Alter valid_name_list in identifier
# map to add alternative identifier names.
lori = 'lori'
istyle = 'istyle'
size = 'size'
ipcol = 'ipcol'

card_1_identifier_map = {
    lori : {
        'internal_name' : lori,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 1,
            'slice_list' : [slice(0, 2)],
        },
        'valid_name_list' : [lori],
    },
    istyle : {
        'internal_name' : istyle,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 2,
            'slice_list' : [slice(1, 3)],
        },
        'valid_name_list' : [istyle],
    },
    size : {
        'internal_name' : size,
        'is_optional' : True,
        'value' : {
            # XXX: Type? Range?
            'node_type' : None,
            'default_value' : 0.30,
        },
        'valid_name_list' : [size],
    },
    ipcol : {
        'internal_name' : ipcol,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 0,
            'slice_list' : [slice(0, 8)],
        },
        'valid_name_list' : [ipcol],
    },
}

card_1_order_map = {
    0 : (lori, None, card_1_identifier_map.get(lori)),
    1 : (istyle, None, card_1_identifier_map.get(istyle)),
    2 : (size, None, card_1_identifier_map.get(size)),
    3 : (ipcol, None, card_1_identifier_map.get(ipcol)),
}

##############################################################################
# viewr card 2:

# Internal identifier names for card 2. Alter valid_name_list in identifier
# map to add alternative identifier names.
iplot = 'iplot'
iwcol = 'iwcol'
factx = 'factx'
facty = 'facty'
xll = 'xll'
yll = 'yll'
ww = 'ww'
wh = 'wh'
wr = 'wr'

card_2_identifier_map = {
    iplot : {
        'internal_name' : iplot,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 1,
            # XXX: Range?
            'slice_list' : None,
        },
        'valid_name_list' : [iplot],
    },
    iwcol : {
        'internal_name' : iwcol,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 0,
            'slice_list' : [slice(0, 8)],
        },
        'valid_name_list' : [iwcol],
    },
    factx : {
        'internal_name' : factx,
        'is_optional' : True,
        'value' : {
            # XXX: Type? Range?
            'node_type' : None,
            'default_value' : 1.0,
        },
        'valid_name_list' : [factx],
    },
    facty : {
        'internal_name' : facty,
        'is_optional' : True,
        'value' : {
            # XXX: Type? Range?
            'node_type' : None,
            'default_value' : 1.0,
        },
        'valid_name_list' : [facty],
    },
    xll : {
        'internal_name' : xll,
        'is_optional' : True,
        'value' : {
            # XXX: Type? Range?
            'node_type' : None,
            'default_value' : 0,
        },
        'valid_name_list' : [xll],
    },
    yll : {
        'internal_name' : yll,
        'is_optional' : True,
        'value' : {
            # XXX: Type? Range?
            'node_type' : None,
            'default_value' : 0,
        },
        'valid_name_list' : [yll],
    },
    ww : {
        'internal_name' : ww,
        'is_optional' : True,
        'value' : {
            # XXX: Type? Range?
            'node_type' : None,
            # Default value depends on lori defined in card 1.
            'default_value' : None,
        },
        'valid_name_list' : [ww],
    },
    wh : {
        'internal_name' : wh,
        'is_optional' : True,
        'value' : {
            # XXX: Type? Range?
            'node_type' : None,
            # Default value depends on lori defined in card 1.
            'default_value' : None,
        },
        'valid_name_list' : [wh],
    },
    wr : {
        'internal_name' : wr,
        'is_optional' : True,
        'value' : {
            # XXX: Type? Range?
            'node_type' : None,
            'default_value' : 0,
        },
        'valid_name_list' : [wr],
    },
}

card_2_order_map = {
    0 : (iplot, None, card_2_identifier_map.get(iplot)),
    1 : (iwcol, None, card_2_identifier_map.get(iwcol)),
    2 : (factx, None, card_2_identifier_map.get(factx)),
    3 : (facty, None, card_2_identifier_map.get(facty)),
    4 : (xll, None, card_2_identifier_map.get(xll)),
    5 : (yll, None, card_2_identifier_map.get(yll)),
    6 : (ww, None, card_2_identifier_map.get(ww)),
    7 : (wh, None, card_2_identifier_map.get(wh)),
    8 : (wr, None, card_2_identifier_map.get(wr)),
}

##############################################################################
# viewr card 3:

# Internal identifier names for card 3. Alter valid_name_list in identifier
# map to add alternative identifier names.
t1 = 't1'

card_3_identifier_map = {
    t1 : {
        'internal_name' : t1,
        'is_optional' : True,
        'value' : {
            'node_type' : 'string',
            'default_value' : '',
            'length' : 80,
        },
        'valid_name_list' : [t1],
    },
}

card_3_order_map = {
    0 : (t1, None, card_3_identifier_map.get(t1)),
}

##############################################################################
# viewr card 3a:

# Internal identifier names for card 3a. Alter valid_name_list in identifier
# map to add alternative identifier names.
t2 = 't2'

card_3a_identifier_map = {
    t2 : {
        'internal_name' : t2,
        'is_optional' : True,
        'value' : {
            'node_type' : 'string',
            'default_value' : '',
            'length' : 80,
        },
        'valid_name_list' : [t2],
    },
}

card_3a_order_map = {
    0 : (t2, None, card_3a_identifier_map.get(t2)),
}

##############################################################################
# viewr card 4:

# Internal identifier names for card 4. Alter valid_name_list in identifier
# map to add alternative identifier names.
itype = 'itype'
jtype = 'jtype'
igrid = 'igrid'
ileg = 'ileg'
xtag = 'xtag'
ytag = 'ytag'

card_4_identifier_map = {
    itype : {
        'internal_name' : itype,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 4,
            'slice_list' : [slice(-4, 0), slice(1, 5)],
        },
        'valid_name_list' : [itype],
    },
    jtype : {
        'internal_name' : jtype,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 0,
            'slice_list' : [slice(0, 3)],
        },
        'valid_name_list' : [jtype],
    },
    igrid : {
        'internal_name' : igrid,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 2,
            'slice_list' : [slice(0, 4)],
        },
        'valid_name_list' : [igrid],
    },
    ileg : {
        'internal_name' : ileg,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 0,
            'slice_list' : [slice(0, 3)],
        },
        'valid_name_list' : [ileg],
    },
    xtag : {
        'internal_name' : xtag,
        'is_optional' : True,
        'value' : {
            # XXX: Type? Range?
            'node_type' : None,
            'default_value' : 0,
        },
        'valid_name_list' : [xtag],
    },
    ytag : {
        'internal_name' : ytag,
        'is_optional' : True,
        'value' : {
            # XXX: Type? Range?
            'node_type' : None,
            'default_value' : 0,
        },
        'valid_name_list' : [ytag],
    },
}

card_4_order_map = {
    0 : (itype, None, card_4_identifier_map.get(itype)),
    1 : (jtype, None, card_4_identifier_map.get(jtype)),
    2 : (igrid, None, card_4_identifier_map.get(igrid)),
    3 : (ileg, None, card_4_identifier_map.get(ileg)),
    4 : (xtag, None, card_4_identifier_map.get(xtag)),
    5 : (ytag, None, card_4_identifier_map.get(ytag)),
}

##############################################################################
# viewr card 5:

# Internal identifier names for card 5. Alter valid_name_list in identifier
# map to add alternative identifier names.
xmin = 'xmin'
xmax = 'xmax'
xstep = 'xstep'

card_5_identifier_map = {
    xmin : {
        'internal_name' : xmin,
        'is_optional' : False,
        'value' : {
            # XXX: Type? Range?
            'node_type' : None,
            'default_value' : None,
        },
        'valid_name_list' : [xmin],
    },
    xmax : {
        'internal_name' : xmax,
        'is_optional' : False,
        'value' : {
            # XXX: Type? Range?
            'node_type' : None,
            'default_value' : None,
        },
        'valid_name_list' : [xmax],
    },
    xstep : {
        'internal_name' : xstep,
        'is_optional' : True,
        'value' : {
            # XXX: Type? Range?
            'node_type' : None,
            'default_value' : None,
        },
        'valid_name_list' : [xstep],
    },
}

card_5_order_map = {
    0 : (xmin, None, card_5_identifier_map.get(xmin)),
    1 : (xmax, None, card_5_identifier_map.get(xmax)),
    2 : (xstep, None, card_5_identifier_map.get(xstep)),
}

##############################################################################
# viewr card 5a:

# Internal identifier names for card 5a. Alter valid_name_list in identifier
# map to add alternative identifier names.
xlabl = 'xlabl'

card_5a_identifier_map = {
    xlabl : {
        'internal_name' : xlabl,
        'is_optional' : True,
        'value' : {
            'node_type' : 'string',
            'default_value' : '',
            'length' : 80,
        },
        'valid_name_list' : [xlabl],
    },
}

card_5a_order_map = {
    0 : (xlabl, None, card_5a_identifier_map.get(xlabl)),
}

##############################################################################
# viewr card 6:

# Internal identifier names for card 6. Alter valid_name_list in identifier
# map to add alternative identifier names.
ymin = 'ymin'
ymax = 'ymax'
ystep = 'ystep'

card_6_identifier_map = {
    ymin : {
        'internal_name' : ymin,
        'is_optional' : False,
        'value' : {
            # XXX: Type? Range?
            'node_type' : None,
            'default_value' : None,
        },
        'valid_name_list' : [ymin],
    },
    ymax : {
        'internal_name' : ymax,
        'is_optional' : False,
        'value' : {
            # XXX: Type? Range?
            'node_type' : None,
            'default_value' : None,
        },
        'valid_name_list' : [ymax],
    },
    ystep : {
        'internal_name' : ystep,
        'is_optional' : True,
        'value' : {
            # XXX: Type? Range?
            'node_type' : None,
            'default_value' : None,
        },
        'valid_name_list' : [ystep],
    },
}

card_6_order_map = {
    0 : (ymin, None, card_6_identifier_map.get(ymin)),
    1 : (ymax, None, card_6_identifier_map.get(ymax)),
    2 : (ystep, None, card_6_identifier_map.get(ystep)),
}

##############################################################################
# viewr card 6a:

# Internal identifier names for card 6a. Alter valid_name_list in identifier
# map to add alternative identifier names.
ylabl = 'ylabl'

card_6a_identifier_map = {
    ylabl : {
        'internal_name' : ylabl,
        'is_optional' : True,
        'value' : {
            'node_type' : 'string',
            'default_value' : '',
            'length' : 80,
        },
        'valid_name_list' : [ylabl],
    },
}

card_6a_order_map = {
    0 : (ylabl, None, card_6a_identifier_map.get(ylabl)),
}

##############################################################################
# viewr card 7:

# Internal identifier names for card 7. Alter valid_name_list in identifier
# map to add alternative identifier names.
rmin = 'rmin'
rmax = 'rmax'
rstep = 'rstep'

card_7_identifier_map = {
    rmin : {
        'internal_name' : rmin,
        'is_optional' : False,
        'value' : {
            # XXX: Type? Range?
            'node_type' : None,
            'default_value' : None,
        },
        'valid_name_list' : [rmin],
    },
    rmax : {
        'internal_name' : rmax,
        'is_optional' : False,
        'value' : {
            # XXX: Type? Range?
            'node_type' : None,
            'default_value' : None,
        },
        'valid_name_list' : [rmax],
    },
    rstep : {
        'internal_name' : rstep,
        'is_optional' : True,
        'value' : {
            # XXX: Type? Range?
            'node_type' : None,
            'default_value' : None,
        },
        'valid_name_list' : [rstep],
    },
}

card_7_order_map = {
    0 : (rmin, None, card_7_identifier_map.get(rmin)),
    1 : (rmax, None, card_7_identifier_map.get(rmax)),
    2 : (rstep, None, card_7_identifier_map.get(rstep)),
}

##############################################################################
# viewr card 7a:

# Internal identifier names for card 7a. Alter valid_name_list in identifier
# map to add alternative identifier names.
rl = 'rl'

card_7a_identifier_map = {
    rl : {
        'internal_name' : rl,
        'is_optional' : True,
        'value' : {
            'node_type' : 'string',
            'default_value' : '',
            'length' : 80,
        },
        'valid_name_list' : [rl],
    },
}

card_7a_order_map = {
    0 : (rl, None, card_7a_identifier_map.get(rl)),
}

##############################################################################
# viewr card 8: dummy card

card_8_identifier_map = {}
card_8_order_map = {}

##############################################################################
# viewr card 9:

# Internal identifier names for card 9. Alter valid_name_list in identifier
# map to add alternative identifier names.
icon = 'icon'
isym = 'isym'
idash = 'idash'
iccol = 'iccol'
ithick = 'ithick'
ishade = 'ishade'

card_9_identifier_map = {
    icon : {
        'internal_name' : icon,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 0,
            # XXX: Range?
            'slice_list' : None,
        },
        'valid_name_list' : [icon],
    },
    isym : {
        'internal_name' : isym,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 0,
            'slice_list' : [slice(0, 25)],
        },
        'valid_name_list' : [isym],
    },
    idash : {
        'internal_name' : idash,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 0,
            'slice_list' : [slice(0, 6)],
        },
        'valid_name_list' : [idash],
    },
    iccol : {
        'internal_name' : iccol,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 0,
            'slice_list' : [slice(0, 9)],
        },
        'valid_name_list' : [iccol],
    },
    ithick : {
        'internal_name' : ithick,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 1,
            # XXX: Range is [0,1]?
            'slice_list' : None,
        },
        'valid_name_list' : [ithick],
    },
    ishade : {
        'internal_name' : ishade,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 0,
            'slice_list' : [slice(0, 81)],
        },
        'valid_name_list' : [ishade],
    },
}

card_9_order_map = {
    0 : (icon, None, card_9_identifier_map.get(icon)),
    1 : (isym, None, card_9_identifier_map.get(isym)),
    2 : (idash, None, card_9_identifier_map.get(idash)),
    3 : (iccol, None, card_9_identifier_map.get(iccol)),
    4 : (ithick, None, card_9_identifier_map.get(ithick)),
    5 : (ishade, None, card_9_identifier_map.get(ishade)),
}

##############################################################################
# viewr card 10:

# Internal identifier names for card 10. Alter valid_name_list in identifier
# map to add alternative identifier names.
aleg = 'aleg'

card_10_identifier_map = {
    aleg : {
        'internal_name' : aleg,
        'is_optional' : True,
        'value' : {
            'node_type' : 'string',
            'default_value' : '',
            'length' : 80,
        },
        'valid_name_list' : [aleg],
    },
}

card_10_order_map = {
    0 : (aleg, None, card_10_identifier_map.get(aleg)),
}

##############################################################################
# viewr card 10a:

# Internal identifier names for card 10a. Alter valid_name_list in identifier
# map to add alternative identifier names.
xtag = 'xtag'
ytag = 'ytag'
xpoint = 'xpoint'

card_10a_identifier_map = {
    xtag : {
        'internal_name' : xtag,
        'is_optional' : True,
        'value' : {
            'node_type' : None,
            'default_value' : 0,
        },
        'valid_name_list' : [xtag],
    },
    ytag : {
        'internal_name' : ytag,
        'is_optional' : True,
        'value' : {
            'node_type' : None,
            'default_value' : 0,
        },
        'valid_name_list' : [ytag],
    },
    xpoint : {
        'internal_name' : xpoint,
        'is_optional' : True,
        'value' : {
            'node_type' : None,
            'default_value' : 0,
        },
        'valid_name_list' : [xpoint],
    },
}

card_10a_order_map = {
    0 : (xtag, None, card_10a_identifier_map.get(xtag)),
    1 : (ytag, None, card_10a_identifier_map.get(ytag)),
    2 : (xpoint, None, card_10a_identifier_map.get(xpoint)),
}

##############################################################################
# viewr card 11:

# Internal identifier names for card 11. Alter valid_name_list in identifier
# map to add alternative identifier names.
xv = 'xv'
yv = 'yv'
zv = 'zv'

x3 = 'x3'
y3 = 'y3'
z3 = 'z3'

card_11_identifier_map = {
    xv : {
        'internal_name' : xv,
        'is_optional' : True,
        'value' : {
            'node_type' : None,
            'default_value' : 15.0,
        },
        'valid_name_list' : [xv],
    },
    yv : {
        'internal_name' : yv,
        'is_optional' : True,
        'value' : {
            'node_type' : None,
            'default_value' : -15.0,
        },
        'valid_name_list' : [yv],
    },
    zv : {
        'internal_name' : zv,
        'is_optional' : True,
        'value' : {
            'node_type' : None,
            'default_value' : 15.0,
        },
        'valid_name_list' : [zv],
    },
    x3 : {
        'internal_name' : x3,
        'is_optional' : True,
        'value' : {
            'node_type' : None,
            'default_value' : 2.5,
        },
        'valid_name_list' : [x3],
    },
    y3 : {
        'internal_name' : y3,
        'is_optional' : True,
        'value' : {
            'node_type' : None,
            'default_value' : 6.5,
        },
        'valid_name_list' : [y3],
    },
    z3 : {
        'internal_name' : z3,
        'is_optional' : True,
        'value' : {
            'node_type' : None,
            'default_value' : 2.5,
        },
        'valid_name_list' : [z3],
    },
}

card_11_order_map = {
    0 : (xv, None, card_11_identifier_map.get(xv)),
    1 : (yv, None, card_11_identifier_map.get(yv)),
    2 : (zv, None, card_11_identifier_map.get(zv)),
    3 : (x3, None, card_11_identifier_map.get(x3)),
    4 : (y3, None, card_11_identifier_map.get(y3)),
    5 : (z3, None, card_11_identifier_map.get(z3)),
}

##############################################################################
# viewr card 12:

# Internal identifier names for card 12. Alter valid_name_list in identifier
# map to add alternative identifier names.
nform = 'nform'

card_12_identifier_map = {
    nform : {
        'internal_name' : nform,
        'is_optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : [slice(0, 2)],
        },
        'valid_name_list' : [nform],
    },
}

card_12_order_map = {
    0 : (nform, None, card_12_identifier_map.get(nform)),
}

##############################################################################
# viewr card 13:

# Internal identifier names for card 13. Alter valid_name_list in identifier
# map to add alternative identifier names.
xdata = 'xdata'
ydata = 'ydata'
yerr1 = 'yerr1'
yerr2 = 'yerr2'
xerr1 = 'xerr1'
xerr2 = 'xerr2'

card_13_identifier_map = {
    xdata : {
        'internal_name' : xdata,
        'is_optional' : True,
        'value' : {
            # XXX: Type? Range?
            'node_type' : None,
            'default_value' : 0,
        },
        'valid_name_list' : [xdata],
    },
    ydata : {
        'internal_name' : ydata,
        'is_optional' : True,
        'value' : {
            # XXX: Type? Range?
            'node_type' : None,
            'default_value' : 0,
        },
        'valid_name_list' : [ydata],
    },
    yerr1 : {
        'internal_name' : yerr1,
        'is_optional' : True,
        'value' : {
            # XXX: Type? Range?
            'node_type' : None,
            'default_value' : 0,
        },
        'valid_name_list' : [yerr1],
    },
    yerr2 : {
        'internal_name' : yerr2,
        'is_optional' : True,
        'value' : {
            # XXX: Type? Range?
            'node_type' : None,
            'default_value' : 0,
        },
        'valid_name_list' : [yerr2],
    },
    xerr1 : {
        'internal_name' : xerr1,
        'is_optional' : True,
        'value' : {
            # XXX: Type? Range?
            'node_type' : None,
            'default_value' : 0,
        },
        'valid_name_list' : [xerr1],
    },
    xerr2 : {
        'internal_name' : xerr2,
        'is_optional' : True,
        'value' : {
            # XXX: Type? Range?
            'node_type' : None,
            'default_value' : 0,
        },
        'valid_name_list' : [xerr2],
    },
}

card_13_order_map = {
    0 : (xdata, None, card_13_identifier_map.get(xdata)),
    1 : (ydata, None, card_13_identifier_map.get(ydata)),
    2 : (yerr1, None, card_13_identifier_map.get(yerr1)),
    3 : (yerr2, None, card_13_identifier_map.get(yerr2)),
    4 : (xerr1, None, card_13_identifier_map.get(xerr1)),
    5 : (xerr2, None, card_13_identifier_map.get(xerr2)),
}

##############################################################################
# viewr card 14:

# Internal identifier names for card 14. Alter valid_name_list in identifier
# map to add alternative identifier names.
y = 'y'

card_14_identifier_map = {
    y : {
        'internal_name' : y,
        'is_optional' : False,
        'value' : {
            # XXX: Type? Range?
            'node_type' : None,
            'default_value' : None,
        },
        'valid_name_list' : [y],
    },
}

card_14_order_map = {
    0 : (y, None, card_14_identifier_map.get(y)),
}

##############################################################################
# viewr card 14a:

# Internal identifier names for card 14a. Alter valid_name_list in identifier
# map to add alternative identifier names.
x = 'x'
z = 'z'

card_14a_identifier_map = {
    x : {
        'internal_name' : x,
        'is_optional' : False,
        'value' : {
            # XXX: Type? Range?
            'node_type' : None,
            'default_value' : None,
        },
        'valid_name_list' : [x],
    },
    z : {
        'internal_name' : z,
        'is_optional' : False,
        'value' : {
            # XXX: Type? Range?
            'node_type' : None,
            'default_value' : None,
        },
        'valid_name_list' : [z],
    },
}

card_14a_order_map = {
    0 : (x, None, card_14a_identifier_map.get(x)),
    1 : (z, None, card_14a_identifier_map.get(z)),
}
