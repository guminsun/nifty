import settings

material_number = settings.material_number
unit_number = settings.unit_number

##############################################################################
# covr card 1:

# Internal identifier names for card 1. Alter valid_name_list in identifier
# map to add alternative identifier names.
nin = 'nin'
nout = 'nout'
nplot = 'nplot'

card_1_identifier_map = {
    nin : {
        'internal_name' : nin,
        'is_optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : unit_number,
        },
        'valid_name_list' : [nin],
    },
    nout : {
        'internal_name' : nout,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 0,
            'slice_list' : unit_number,
        },
        'valid_name_list' : [nout],
    },
    nplot : {
        'internal_name' : nplot,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 0,
            'slice_list' : unit_number,
        },
        'valid_name_list' : [nplot],
    },
}

card_1_order_map = {
    0 : (nin, None, card_1_identifier_map.get(nin)),
    1 : (nout, None, card_1_identifier_map.get(nout)),
    2 : (nplot, None, card_1_identifier_map.get(nplot)),
}

##############################################################################
# covr card 2:

# Internal identifier names for card 2.
icolor = 'icolor'

card_2_identifier_map = {
    icolor : {
        'internal_name' : icolor,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 0,
            'slice_list' : [slice(0, 2)],
        },
        'valid_name_list' : [icolor],
    },
}

card_2_order_map = {
    0 : (icolor, None, card_2_identifier_map.get(icolor)),
}

##############################################################################
# covr card 2a:

# Internal identifier names for card 2a.
epmin = 'epmin'

card_2a_identifier_map = {
    epmin : {
        'internal_name' : epmin,
        'is_optional' : True,
        'value' : {
            # XXX: Must be number?
            'node_type' : None,
            'default_value' : 0.0,
        },
        'valid_name_list' : [epmin],
    },
}

card_2a_order_map = {
    0 : (epmin, None, card_2a_identifier_map.get(epmin)),
}

##############################################################################
# covr card 3a:

# Internal identifier names for card 3a.
irelco = 'irelco'
ncase = 'ncase'
noleg = 'noleg'
nstart = 'nstart'
ndiv = 'ndiv'

card_3a_identifier_map = {
    irelco : {
        'internal_name' : irelco,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 1,
            'slice_list' : [slice(0, 2)],
        },
        'valid_name_list' : [irelco],
    },
    ncase : {
        'internal_name' : ncase,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 1,
            'slice_list' : [slice(0, 61)],
        },
        'valid_name_list' : [ncase],
    },
    noleg : {
        'internal_name' : noleg,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 0,
            'slice_list' : [slice(-1, 2)],
        },
        'valid_name_list' : [noleg],
    },
    nstart : {
        'internal_name' : nstart,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 1,
            'slice_list' : [slice(0, float('inf'))],
        },
        'valid_name_list' : [nstart],
    },
    ndiv : {
        'internal_name' : ndiv,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 1,
            'slice_list' : [slice(0, float('inf'))],
        },
        'valid_name_list' : [ndiv],
    },
}

card_3a_order_map = {
    0 : (irelco, None, card_3a_identifier_map.get(irelco)),
    1 : (ncase, None, card_3a_identifier_map.get(ncase)),
    2 : (noleg, None, card_3a_identifier_map.get(noleg)),
    3 : (nstart, None, card_3a_identifier_map.get(nstart)),
    4 : (ndiv, None, card_3a_identifier_map.get(ndiv)),
}

##############################################################################
# covr card 2b:

# Internal identifier names for card 2b.
matype = 'matype'
ncase = 'ncase'

card_2b_identifier_map = {
    matype : {
        'internal_name' : matype,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 3,
            'slice_list' : [slice(3, 5)],
        },
        'valid_name_list' : [matype],
    },
    ncase : {
        'internal_name' : ncase,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 1,
            'slice_list' : [slice(0, 61)],
        },
        'valid_name_list' : [ncase],
    },
}

card_2b_order_map = {
    0 : (matype, None, card_2b_identifier_map.get(matype)),
    1 : (ncase, None, card_2b_identifier_map.get(ncase)),
}

##############################################################################
# covr card 3b:

# Internal identifier names for card 3b.
hlibid = 'hlibid'

card_3b_identifier_map = {
    hlibid : {
        'internal_name' : hlibid,
        'is_optional' : False,
        'value' : {
            'node_type' : 'string',
            'default_value' : None,
            'length' : 6,
        },
        'valid_name_list' : [hlibid],
    },
}

card_3b_order_map = {
    0 : (hlibid, None, card_3b_identifier_map.get(hlibid)),
}

##############################################################################
# covr card 3c:

# Internal identifier names for card 3c.
hdescr = 'hdescr'

card_3c_identifier_map = {
    hdescr : {
        'internal_name' : hdescr,
        'is_optional' : False,
        'value' : {
            'node_type' : 'string',
            'default_value' : None,
            'length' : 21,
        },
        'valid_name_list' : [hdescr],
    },
}

card_3c_order_map = {
    0 : (hdescr, None, card_3c_identifier_map.get(hdescr)),
}

##############################################################################
# covr card 4:

# Internal identifier names for card 4.
mat = 'mat'
mt = 'mt'
mat1 = 'mat1'
mt1 = 'mt1'

card_4_identifier_map = {
    mat : {
        'internal_name' : mat,
        'is_optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : material_number,
        },
        'valid_name_list' : [mat],
    },
    mt : {
        'internal_name' : mt,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 0,
            # XXX: Range not regular MT number. May be negative.
            'slice_list' : None,
        },
        'valid_name_list' : [mt],
    },
    mat1 : {
        'internal_name' : mat1,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 0,
            # XXX: Range not regular material number. May be negative.
            'slice_list' : None,
        },
        'valid_name_list' : [mat1],
    },
    mt1 : {
        'internal_name' : mt1,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 0,
            # XXX: Range not regular MT number. May be negative.
            'slice_list' : None,
        },
        'valid_name_list' : [mt1],
    },
}

card_4_order_map = {
    0 : (mat, None, card_4_identifier_map.get(mat)),
    1 : (mt, None, card_4_identifier_map.get(mt)),
    2 : (mat1, None, card_4_identifier_map.get(mat1)),
    3 : (mt1, None, card_4_identifier_map.get(mt1)),
}
