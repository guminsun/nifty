import settings

material_number = settings.material_number
unit_number = settings.unit_number

##############################################################################
# unresr card 1:

# Internal identifier names for card 1. Alter valid_name_list in identifier
# map to add alternative identifier names.
nendf = 'nendf'
nin = 'nin'
nout = 'nout'

card_1_identifier_map = {
    nendf : {
        'internal_name' : nendf,
        # nendf must be defined, it is not optional.
        'is_optional' : False,
        'value' : {
            'node_type' : 'integer',
            # nendf has no default value since it must be defined.
            'default_value' : None,
            # The integer range of allowed values represented as a list of slices.
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
}

card_1_order_map = {
    0 : (nendf, None, card_1_identifier_map.get(nendf)),
    1 : (nin, None, card_1_identifier_map.get(nin)),
    2 : (nout, None, card_1_identifier_map.get(nout)),
}

##############################################################################
# unresr card 2:

# Internal identifier names for card 2. Alter valid_name_list in identifier
# map to add alternative identifier names.
matd = 'matd'
ntemp = 'ntemp'
nsigz = 'nsigz'
iprint = 'iprint'

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
    ntemp : {
        'internal_name' : ntemp,
        'is_optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : [slice(0, 11)],
        },
        'valid_name_list' : [ntemp],
    },
    nsigz : {
        'internal_name' : nsigz,
        'is_optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : [slice(0, 11)],
        },
        'valid_name_list' : [nsigz],
    },
    iprint : {
        'internal_name' : iprint,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 0,
            'slice_list' : [slice(0, 2)],
        },
        'valid_name_list' : [iprint],
    },
}

card_2_order_map = {
    0 : (matd, None, card_2_identifier_map.get(matd)),
    1 : (ntemp, None, card_2_identifier_map.get(ntemp)),
    2 : (nsigz, None, card_2_identifier_map.get(nsigz)),
    3 : (iprint, None, card_2_identifier_map.get(iprint)),
}

##############################################################################
# unresr card 3:

# Internal identifier names for card 3. Alter valid_name_list in identifier
# map to add alternative identifier names.
temp = 'temp'

card_3_identifier_map = {
    temp : {
        'internal_name' : temp,
        'is_optional' : False,
        'value' : {
            # XXX: Type? Range?
            'node_type' : None,
            'default_value' : None,
        },
        'valid_name_list' : [temp],
    },
}

card_3_order_map = {}

##############################################################################
# unresr card 4:

# Internal identifier names for card 4. Alter valid_name_list in identifier
# map to add alternative identifier names.
sigz = 'sigz'

card_4_identifier_map = {
    sigz : {
        'internal_name' : sigz,
        'is_optional' : False,
        'value' : {
            # XXX: Type? Range?
            'node_type' : None,
            'default_value' : None,
        },
        'valid_name_list' : [sigz],
    },
}

card_4_order_map = {}
