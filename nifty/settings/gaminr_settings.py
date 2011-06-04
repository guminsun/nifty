import settings

material_number = settings.material_number
unit_number = settings.unit_number

##############################################################################
# gaminr card 1:

# Internal identifier names for card 1. Alter valid_name_list in identifier
# map to add alternative identifier names.
nendf = 'nendf'
npend = 'npend'
ngam1 = 'ngam1'
ngam2 = 'ngam2'

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
    npend : {
        'internal_name' : npend,
        'is_optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : unit_number,
        },
        'valid_name_list' : [npend],
    },
    ngam1 : {
        'internal_name' : ngam1,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 0,
            'slice_list' : unit_number,
        },
        'valid_name_list' : [ngam1],
    },
    ngam2 : {
        'internal_name' : ngam2,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 0,
            'slice_list' : unit_number,
        },
        'valid_name_list' : [ngam2],
    },
}

card_1_order_map = {
    0 : (nendf, None, card_1_identifier_map.get(nendf)),
    1 : (npend, None, card_1_identifier_map.get(npend)),
    2 : (ngam1, None, card_1_identifier_map.get(ngam1)),
    3 : (ngam2, None, card_1_identifier_map.get(ngam2)),
}

##############################################################################
# gaminr card 2:

# Internal identifier names for card 2.
matb = 'matb'
igg = 'igg'
iwt = 'iwt'
lord = 'lord'
iprint = 'iprint'

card_2_identifier_map = {
    matb : {
        'internal_name' : matb,
        'is_optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : material_number,
        },
        'valid_name_list' : [matb],
    },
    igg : {
        'internal_name' : igg,
        'is_optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : [slice(0, 11)],
        },
        'valid_name_list' : [igg],
    },
    iwt : {
        'internal_name' : iwt,
        'is_optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : [slice(1, 4)],
        },
        'valid_name_list' : [iwt],
    },
    lord : {
        'internal_name' : lord,
        'is_optional' : False,
        'value' : {
            # XXX: Type? Range?
            'node_type' : None,
            'default_value' : None,
        },
        'valid_name_list' : [lord],
    },
    iprint : {
        'internal_name' : iprint,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 1,
            'slice_list' : [slice(0, 2)],
        },
        'valid_name_list' : [iprint],
    },
}

card_2_order_map = {
    0 : (matb, None, card_2_identifier_map.get(matb)),
    1 : (igg, None, card_2_identifier_map.get(igg)),
    2 : (iwt, None, card_2_identifier_map.get(iwt)),
    3 : (lord, None, card_2_identifier_map.get(lord)),
    4 : (iprint, None, card_2_identifier_map.get(iprint)),
}

##############################################################################
# gaminr card 3:

# Internal identifier names for card 3.
title = 'title'

card_3_identifier_map = {
    title : {
        'internal_name' : title,
        'is_optional' : False,
        'value' : {
            'node_type' : 'string',
            'default_value' : None,
            'length' : 80,
        },
        'valid_name_list' : [title],
    },
}

card_3_order_map = {
    0 : (title, None, card_3_identifier_map.get(title)),
}

##############################################################################
# gaminr card 4:

# Internal identifier names for card 4.
ngg = 'ngg'
egg = 'egg'

card_4_identifier_map = {
    ngg : {
        'internal_name' : ngg,
        'is_optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : [slice(0, float('inf'))],
        },
        'valid_name_list' : [ngg],
    },
    egg : {
        'internal_name' : egg,
        'is_optional' : False,
        'value' : {
            # XXX: Type? (must be number?) Range?
            'node_type' : None,
            'default_value' : None,
        },
        'valid_name_list' : [egg],
    },
}

# The order map needs to be updated with the expected egg values when ngg has
# been defined.
card_4_order_map = {
    0 : (ngg, None, card_4_identifier_map.get(ngg)),
}

##############################################################################
# gaminr card 5:

# Internal identifier names for card 5.
wght = 'wght'

card_5_identifier_map = {
    wght : {
        'internal_name' : wght,
        'is_optional' : False,
        'value' : {
            # XXX: Type? (must be number?) Range?
            'node_type' : None,
            'default_value' : None,
        },
        'valid_name_list' : [wght],
    },
}

# The order map needs to be updated with the number of expected wght values
# has been defined.
card_5_order_map = {}

##############################################################################
# gaminr card 6:

# Internal identifier names for card 6.
mfd = 'mfd'
mtd = 'mtd'
mtname = 'mtname'

card_6_identifier_map = {
    mfd : {
        'internal_name' : mfd,
        'is_optional' : False,
        'value' : {
            # XXX: Range?
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : None,
        },
        'valid_name_list' : [mfd],
    },
    mtd : {
        'internal_name' : mtd,
        'is_optional' : False,
        'value' : {
            # XXX: Range?
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : None,
        },
        'valid_name_list' : [mtd],
    },
    mtname : {
        'internal_name' : mtname,
        'is_optional' : True,
        'value' : {
            'node_type' : 'string',
            'default_value' : '',
            'length' : 80,
        },
        'valid_name_list' : [mtname],
    },
}

card_6_order_map = {
    0 : (mfd, None, card_6_identifier_map.get(mfd)),
    1 : (mtd, None, card_6_identifier_map.get(mtd)),
    2 : (mtname, None, card_6_identifier_map.get(mtname)),
}

##############################################################################
# gaminr card 7:

# Internal identifier names for card 7.
matd = 'matd'

card_7_identifier_map = {
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

card_7_order_map = {
    0 : (matd, None, card_7_identifier_map.get(matd)),
}
