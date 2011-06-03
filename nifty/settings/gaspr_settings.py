import settings

material_number = settings.material_number
unit_number = settings.unit_number

##############################################################################
# gaspr card 1:

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
