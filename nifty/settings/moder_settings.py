import settings

material_number = settings.material_number
unit_number = settings.unit_number

##############################################################################
# moder card 1:

# Internal identifier names for card 1. Alter valid_name_list in identifier
# map to add alternative identifier names.
nin = 'nin'
nout = 'nout'

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
        'is_optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : unit_number,
        },
        'valid_name_list' : [nout],
    },
}

card_1_order_map = {
    0 : (nin, None, card_1_identifier_map.get(nin)),
    1 : (nout, None, card_1_identifier_map.get(nout)),
}

##############################################################################
# moder card 2:

# Internal identifier names for card 2. Alter valid_name_list in identifier
# map to add alternative identifier names.
tpid = 'tpid'

card_2_identifier_map = {
    tpid : {
        'internal_name' : tpid,
        'is_optional' : False,
        'value' : {
            'node_type' : 'string',
            'default_value' : None,
            'length' : 66,
        },
        'valid_name_list' : [tpid],
    },
}

card_2_order_map = {
    0 : (tpid, None, card_2_identifier_map.get(tpid)),
}

##############################################################################
# moder card 3:

# Internal identifier names for card 3. Alter valid_name_list in identifier
# map to add alternative identifier names.
nin = 'nin'
matd = 'matd'

card_3_identifier_map = {
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
}

card_3_order_map = {
    0 : (nin, None, card_3_identifier_map.get(nin)),
    1 : (matd, None, card_3_identifier_map.get(matd)),
}
