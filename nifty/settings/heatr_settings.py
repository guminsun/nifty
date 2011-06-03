import settings

material_number = settings.material_number
unit_number = settings.unit_number

##############################################################################
# heatr card 1:

# Internal identifier names for card 1. Alter valid_name_list in identifier
# map to add alternative identifier names.
nendf = 'nendf'
nin = 'nin'
nout = 'nout'
nplot = 'nplot'

card_1_identifier_map = {
    nendf : {
        'internal_name' : nendf,
        'is_optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : unit_number,
        },
        'valid_name_list' : [nendf],
    },
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
        'is_optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
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
    0 : (nendf, None, card_1_identifier_map.get(nendf)),
    1 : (nin, None, card_1_identifier_map.get(nin)),
    2 : (nout, None, card_1_identifier_map.get(nout)),
    3 : (nplot, None, card_1_identifier_map.get(nplot)),
}

##############################################################################
# heatr card 2:

# Internal identifier names for card 2. Alter valid_name_list in identifier
# map to add alternative identifier names.
matd = 'matd'
npk = 'npk'
nqa = 'nqa'
ntemp = 'ntemp'
local = 'local'
iprint = 'iprint'
ed = 'ed'

card_2_identifier_map = {
    matd : {
        'internal_name' : matd,
        'is_optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : material_number,
        },
        'valid_name_list' : [matd],
    },
    npk : {
        'internal_name' : npk,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 0,
            'slice_list' : [slice(0, float('inf'))],
        },
        'valid_name_list' : [npk],
    },
    nqa : {
        'internal_name' : nqa,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 0,
            'slice_list' : [slice(0, float('inf'))],
        },
        'valid_name_list' : [nqa],
    },
    ntemp : {
        'internal_name' : ntemp,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 0,
            'slice_list' : [slice(0, float('inf'))],
        },
        'valid_name_list' : [ntemp],
    },
    local : {
        'internal_name' : local,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 0,
            'slice_list' : [slice(0, 2)],
        },
        'valid_name_list' : [local],
    },
    iprint : {
        'internal_name' : iprint,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 0,
            'slice_list' : [slice(0, 3)],
        },
        'valid_name_list' : [iprint],
    },
    ed : {
        'internal_name' : ed,
        'is_optional' : True,
        'value' : {
            # XXX: Type? Range?
            'node_type' : None,
            'default_value' : None,
        },
        'valid_name_list' : [ed],
    },
}

card_2_order_map = {
    0 : (matd, None, card_2_identifier_map.get(matd)),
    1 : (npk, None, card_2_identifier_map.get(npk)),
    2 : (nqa, None, card_2_identifier_map.get(nqa)),
    3 : (ntemp, None, card_2_identifier_map.get(ntemp)),
    4 : (local, None, card_2_identifier_map.get(local)),
    5 : (iprint, None, card_2_identifier_map.get(iprint)),
    6 : (ed, None, card_2_identifier_map.get(ed)),
}

##############################################################################
# heatr card 3:

# Internal identifier names for card 3.
mtk = 'mtk'

card_3_identifier_map = {
    mtk : {
        'internal_name' : mtk,
        'is_optional' : False,
        'value' : {
            # Range? MT number?
            # The range of allowed values in the documentation does not seem
            # to be complete. See for example NJOY Test Problem 08 where
            # mtk[0] = 302.
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : None,
        },
        'valid_name_list' : [mtk],
    },
}

# Number of mtk values depends on the npk value defined in card 2. Order map
# needs to be constructed when the npk value is known.
card_3_order_map = {}

##############################################################################
# heatr card 4:

# Internal identifier names for card 4.
mta = 'mta'

card_4_identifier_map = {
    mta : {
        'internal_name' : mta,
        'is_optional' : False,
        'value' : {
            # Range? MT number?
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : None,
        },
        'valid_name_list' : [mta],
    },
}

# Number of mtk values depends on the nqa value defined in card 2. Order map
# needs to be constructed when the nqa value is known.
card_4_order_map = {}

##############################################################################
# heatr card 5:

# Internal identifier names for card 5.
qa = 'qa'

card_5_identifier_map = {
    qa : {
        'internal_name' : qa,
        'is_optional' : False,
        'value' : {
            # Type? Range?
            'node_type' : None,
            'default_value' : None,
        },
        'valid_name_list' : [qa],
    },
}

# Number of qa values depends on the nqa value defined in card 2. Order map
# needs to be constructed when the nqa value is known.
card_5_order_map = {}

##############################################################################
# heatr card 5a:

# Internal identifier names for card 5a.
qbar = 'qbar'

card_5a_identifier_map = {
    qbar : {
        'internal_name' : qbar,
        'is_optional' : False,
        'value' : {
            # Type? Range?
            'node_type' : None,
            'default_value' : None,
        },
        'valid_name_list' : [qbar],
    },
}

# qbar variable TAB1 record. Order map needs to be constructed when the length
# of the card's statement list is known.
card_5a_order_map = {}
