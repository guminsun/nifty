import settings

material_number = settings.material_number
unit_number = settings.unit_number

##############################################################################
# matxsr card 1:

# Internal identifier names for card 1. Alter valid_name_list in identifier
# map to add alternative identifier names.
ngen1 = 'ngen1'
ngen2 = 'ngen2'
nmatx = 'nmatx'
ngen3 = 'ngen3'
ngen4 = 'ngen4'
ngen5 = 'ngen5'
ngen6 = 'ngen6'
ngen7 = 'ngen7'
ngen8 = 'ngen8'

card_1_identifier_map = {
    ngen1 : {
        'internal_name' : ngen1,
        'is_optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : unit_number,
        },
        'valid_name_list' : [ngen1],
    },
    ngen2 : {
        'internal_name' : ngen2,
        'is_optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : unit_number,
        },
        'valid_name_list' : [ngen2],
    },
    nmatx : {
        'internal_name' : nmatx,
        'is_optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : unit_number,
        },
        'valid_name_list' : [nmatx],
    },
    ngen3 : {
        'internal_name' : ngen3,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 0,
            'slice_list' : unit_number,
        },
        'valid_name_list' : [ngen3],
    },
    ngen4 : {
        'internal_name' : ngen4,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 0,
            'slice_list' : unit_number,
        },
        'valid_name_list' : [ngen4],
    },
    ngen5 : {
        'internal_name' : ngen5,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 0,
            'slice_list' : unit_number,
        },
        'valid_name_list' : [ngen5],
    },
    ngen6 : {
        'internal_name' : ngen6,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 0,
            'slice_list' : unit_number,
        },
        'valid_name_list' : [ngen6],
    },
    ngen7 : {
        'internal_name' : ngen7,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 0,
            'slice_list' : unit_number,
        },
        'valid_name_list' : [ngen7],
    },
    ngen8 : {
        'internal_name' : ngen8,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 0,
            'slice_list' : unit_number,
        },
        'valid_name_list' : [ngen8],
    },
}

card_1_order_map = {
    0 : (ngen1, None, card_1_identifier_map.get(ngen1)),
    1 : (ngen2, None, card_1_identifier_map.get(ngen2)),
    2 : (nmatx, None, card_1_identifier_map.get(nmatx)),
    3 : (ngen3, None, card_1_identifier_map.get(ngen3)),
    4 : (ngen4, None, card_1_identifier_map.get(ngen4)),
    5 : (ngen5, None, card_1_identifier_map.get(ngen5)),
    6 : (ngen6, None, card_1_identifier_map.get(ngen6)),
    7 : (ngen7, None, card_1_identifier_map.get(ngen7)),
    8 : (ngen8, None, card_1_identifier_map.get(ngen8)),
}

##############################################################################
# matxsr card 2:

# Internal identifier names for card 2. Alter valid_name_list in identifier
# map to add alternative identifier names.
ivers = 'ivers'
huse = 'huse'

card_2_identifier_map = {
    ivers : {
        'internal_name' : ivers,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 0,
            'slice_list' : unit_number,
        },
        'valid_name_list' : [ivers],
    },
    huse : {
        'internal_name' : huse,
        'is_optional' : True,
        'value' : {
            'node_type' : 'string',
            'default_value' : '',
            'length' : 16,
        },
        'valid_name_list' : [huse],
    },
}

card_2_order_map = {
    0 : (ivers, None, card_2_identifier_map.get(ivers)),
    1 : (huse, None, card_2_identifier_map.get(huse)),
}

##############################################################################
# matxsr card 3:

# Internal identifier names for card 3. Alter valid_name_list in identifier
# map to add alternative identifier names.
npart = 'npart'
ntype = 'ntype'
nholl = 'nholl'
nmat = 'nmat'

card_3_identifier_map = {
    npart : {
        'internal_name' : npart,
        'is_optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : [slice(0, float('inf'))],
        },
        'valid_name_list' : [npart],
    },
    ntype : {
        'internal_name' : ntype,
        'is_optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : [slice(0, float('inf'))],
        },
        'valid_name_list' : [ntype],
    },
    nholl : {
        'internal_name' : nholl,
        'is_optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : [slice(0, float('inf'))],
        },
        'valid_name_list' : [nholl],
    },
    nmat : {
        'internal_name' : nmat,
        'is_optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : [slice(0, float('inf'))],
        },
        'valid_name_list' : [nmat],
    },
}

card_3_order_map = {
    0 : (npart, None, card_3_identifier_map.get(npart)),
    1 : (ntype, None, card_3_identifier_map.get(ntype)),
    2 : (nholl, None, card_3_identifier_map.get(nholl)),
    3 : (nmat, None, card_3_identifier_map.get(nmat)),
}

##############################################################################
# matxsr card 4:

# Internal identifier names for card 4. Alter valid_name_list in identifier
# map to add alternative identifier names.
hsetid = 'hsetid'

card_4_identifier_map = {
    hsetid : {
        'internal_name' : hsetid,
        'is_optional' : False,
        'value' : {
            'node_type' : 'string',
            'default_value' : None,
            'length' : 72,
        },
        'valid_name_list' : [hsetid],
    },
}

card_4_order_map = {
    0 : (hsetid, None, card_4_identifier_map.get(hsetid)),
}

##############################################################################
# matxsr card 5:

# Internal identifier names for card 5. Alter valid_name_list in identifier
# map to add alternative identifier names.
hpart = 'hpart'

card_5_identifier_map = {
    hpart : {
        'internal_name' : hpart,
        'is_optional' : False,
        'value' : {
            'node_type' : 'string',
            'default_value' : None,
            'length' : 8,
        },
        'valid_name_list' : [hpart],
    },
}

card_5_order_map = {
    0 : (hpart, None, card_5_identifier_map.get(hpart)),
}

##############################################################################
# matxsr card 6:

# Internal identifier names for card 6. Alter valid_name_list in identifier
# map to add alternative identifier names.
ngrp = 'ngrp'

card_6_identifier_map = {
    ngrp : {
        'internal_name' : ngrp,
        'is_optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : [slice(0, float('inf'))],
        },
        'valid_name_list' : [ngrp],
    },
}

card_6_order_map = {
    0 : (ngrp, None, card_6_identifier_map.get(ngrp)),
}

##############################################################################
# matxsr card 7:

# Internal identifier names for card 7. Alter valid_name_list in identifier
# map to add alternative identifier names.
htype = 'htype'

card_7_identifier_map = {
    htype : {
        'internal_name' : htype,
        'is_optional' : False,
        'value' : {
            'node_type' : 'string',
            'default_value' : None,
            'length' : 8,
        },
        'valid_name_list' : [htype],
    },
}

card_7_order_map = {
    0 : (htype, None, card_7_identifier_map.get(htype)),
}

##############################################################################
# matxsr card 8:

# Internal identifier names for card 8. Alter valid_name_list in identifier
# map to add alternative identifier names.
jinp = 'jinp'

card_8_identifier_map = {
    jinp : {
        'internal_name' : jinp,
        'is_optional' : False,
        'value' : {
            # XXX: Range?
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : None,
        },
        'valid_name_list' : [jinp],
    },
}

card_8_order_map = {
    0 : (jinp, None, card_8_identifier_map.get(jinp)),
}

##############################################################################
# matxsr card 9:

# Internal identifier names for card 9. Alter valid_name_list in identifier
# map to add alternative identifier names.
joutp = 'joutp'

card_9_identifier_map = {
    joutp : {
        'internal_name' : joutp,
        'is_optional' : False,
        'value' : {
            # XXX: Range?
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : None,
        },
        'valid_name_list' : [joutp],
    },
}

card_9_order_map = {
    0 : (joutp, None, card_9_identifier_map.get(joutp)),
}

##############################################################################
# matxsr card 10:

# Internal identifier names for card 10. Alter valid_name_list in identifier
# map to add alternative identifier names.
hmat = 'hmat'
matno = 'matno'
matgg = 'matgg'

card_10_identifier_map = {
    hmat : {
        'internal_name' : hmat,
        'is_optional' : False,
        'value' : {
            'node_type' : 'string',
            'default_value' : None,
            'length' : 8,
        },
        'valid_name_list' : [hmat],
    },
    matno : {
        'internal_name' : matno,
        'is_optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : material_number,
        },
        'valid_name_list' : [matno],
    },
    matgg : {
        'internal_name' : matgg,
        'is_optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : material_number,
        },
        'valid_name_list' : [matgg],
    },
}

card_10_order_map = {
    0 : (hmat, None, card_10_identifier_map.get(hmat)),
    1 : (matno, None, card_10_identifier_map.get(matno)),
    2 : (matgg, None, card_10_identifier_map.get(matgg)),
}
