import settings

material_number = settings.material_number
unit_number = settings.unit_number

##############################################################################
# broadr card 1:

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
# broadr card 2:

# Internal identifier names for card 2.
mat1 = 'mat1'
ntemp2 = 'ntemp2'
istart = 'istart'
istrap = 'istrap'
temp1 = 'temp1'

card_2_identifier_map = {
    mat1 : {
        'internal_name' : mat1,
        'is_optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : material_number,
        },
        'valid_name_list' : [mat1],
    },
    ntemp2 : {
        'internal_name' : ntemp2,
        'is_optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            # Range of number of final temperatures, maximum is 10.
            'slice_list' : [slice(0, 11)],
        },
        'valid_name_list' : [ntemp2],
    },
    istart : {
        'internal_name' : istart,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 0,
            # Restart value. 0 indicates no, 1 indicates yes.
            'slice_list' : [slice(0, 2)],
        },
        'valid_name_list' : [istart],
    },
    istrap : {
        'internal_name' : istrap,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 0,
            # Bootstrap value. 0 indicates no, 1 indicates yes.
            'slice_list' : [slice(0, 2)],
        },
        'valid_name_list' : [istrap],
    },
    temp1 : {
        'internal_name' : temp1,
        'is_optional' : True,
        'value' : {
            # XXX: Must be number?
            'node_type' : None,
            'default_value' : 0.0,
        },
        'valid_name_list' : [temp1],
    },
}

card_2_order_map = {
    0 : (mat1, None, card_2_identifier_map.get(mat1)),
    1 : (ntemp2, None, card_2_identifier_map.get(ntemp2)),
    2 : (istart, None, card_2_identifier_map.get(istart)),
    3 : (istrap, None, card_2_identifier_map.get(istrap)),
    4 : (temp1, None, card_2_identifier_map.get(temp1)),
}

##############################################################################
# broadr card 3:

# Internal identifier names for card 3.
errthn = 'errthn'
thnmax = 'thnmax'
errmax = 'errmax'
errint = 'errint'

card_3_identifier_map = {
    errthn : {
        'internal_name' : errthn,
        'is_optional' : False,
        'value' : {
            'node_type' : 'float',
            'default_value' : None,
        },
        'valid_name_list' : [errthn],
    },
    thnmax : {
        'internal_name' : thnmax,
        'is_optional' : True,
        'value' : {
            # XXX: Type and range for energy in mev?
            'node_type' : None,
            'default_value' : 1,
        },
        'valid_name_list' : [thnmax],
    },
    errmax : {
        'internal_name' : errmax,
        'is_optional' : True,
        'value' : {
            # XXX: Must be number?
            'node_type' : None,
            # Default value is 10.0*errthn, which cannot be set until the
            # value of errthn is known. When errthn is known, update the
            # errmax default value in e.g. the appropriate organizer and
            # analyzer functions.
            'default_value' : None,
        },
        'valid_name_list' : [errmax],
    },
    errint : {
        'internal_name' : errint,
        'is_optional' : True,
        'value' : {
            # XXX: Must be number?
            'node_type' : None,
            # Default value is errthn/20000.0, which cannot be set until the
            # value of errthn is known. When errthn is known, update the
            # errint default value in e.g. the appropriate organizer and
            # analyzer functions.
            'default_value' : None,
        },
        'valid_name_list' : [errint],
    },
}

card_3_order_map = {
    0 : (errthn, None, card_3_identifier_map.get(errthn)),
    1 : (thnmax, None, card_3_identifier_map.get(thnmax)),
    2 : (errmax, None, card_3_identifier_map.get(errmax)),
    3 : (errint, None, card_3_identifier_map.get(errint)),
}

##############################################################################
# broadr card 4:

# Internal identifier names for card 4.
temp2 = 'temp2'

card_4_identifier_map = {
    temp2 : {
        'internal_name' : temp2,
        'is_optional' : False,
        'value' : {
            # XXX: Must be number?
            'node_type' : None,
            'default_value' : None,
        },
        'valid_name_list' : [temp2],
    },
}

# Order map is defined when the number of temperatures are known. Construct
# order map in the appropriate functions where it is needed.
card_4_order_map = {}

##############################################################################
# broadr card 5:

# Internal identifier names for card 5.
mat1 = 'mat1'

card_5_identifier_map = {
    mat1 : {
        'internal_name' : mat1,
        'is_optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : material_number,
        },
        'valid_name_list' : [mat1],
    },
}

card_5_order_map = {
    0 : (mat1, None, card_5_identifier_map.get(mat1)),
}
