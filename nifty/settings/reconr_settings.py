import settings

material_number = settings.material_number
unit_number = settings.unit_number

##############################################################################
# reconr card 1:

# Internal identifier names for card 1. Alter valid_name_list in identifier
# map to add alternative identifier names.
nendf = 'nendf'
npend = 'npend'

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
}

card_1_order_map = {
    0 : (nendf, None, card_1_identifier_map.get(nendf)),
    1 : (npend, None, card_1_identifier_map.get(npend)),
}

##############################################################################
# reconr card 2:

# Internal identifier names for card 2. Alter valid_name_list in identifier
# map to add alternative identifier names.
tlabel = 'tlabel'

card_2_identifier_map = {
    tlabel : {
        'internal_name' : tlabel,
        'is_optional' : False,
        'value' : {
            'node_type' : 'string',
            'default_value' : None,
            'length' : 66,
        },
        'valid_name_list' : [tlabel],
    },
}

card_2_order_map = {
    0 : (tlabel, None, card_2_identifier_map.get(tlabel)),
}

##############################################################################
# reconr card 3:

# Internal identifier names for card 3. Alter valid_name_list in identifier
# map to add alternative identifier names.
mat = 'mat'
ncards = 'ncards'
ngrid = 'ngrid'

card_3_identifier_map = {
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
    ncards : {
        'internal_name' : ncards,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 0,
            'slice_list' : [slice(0, float('inf'))],
        },
        'valid_name_list' : [ncards],
    },
    ngrid : {
        'internal_name' : ngrid,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 0,
            'slice_list' : [slice(0, float('inf'))],
        },
        'valid_name_list' : [ngrid],
    },
}

card_3_order_map = {
    0 : (mat, None, card_3_identifier_map.get(mat)),
    1 : (ncards, None, card_3_identifier_map.get(ncards)),
    2 : (ngrid, None, card_3_identifier_map.get(ngrid)),
}

##############################################################################
# reconr card 4:

# Internal identifier names for card 4. Alter valid_name_list in identifier
# map to add alternative identifier names.
err = 'err'
tempr = 'tempr'
errmax = 'errmax'
errint = 'errint'

card_4_identifier_map = {
    err : {
        'internal_name' : err,
        'is_optional' : False,
        'value' : {
            'node_type' : 'float',
            'default_value' : None,
        },
        'valid_name_list' : [err],
    },
    tempr : {
        'internal_name' : tempr,
        'is_optional' : True,
        'value' : {
            # XXX: Type? Range?
            'node_type' : None,
            'default_value' : None,
        },
        'valid_name_list' : [tempr],
    },
    errmax : {
        'internal_name' : errmax,
        'is_optional' : True,
        'value' : {
            'node_type' : 'float',
            # Defaults to 10*err. Needs to be updated in organizer when err
            # has been defined.
            'default_value' : None,
        },
        'valid_name_list' : [errmax],
    },
    errint : {
        'internal_name' : errint,
        'is_optional' : True,
        'value' : {
            'node_type' : 'float',
            # Defaults to err/20000. Needs to be updated in organizer when err
            # has been defined.
            'default_value' : None,
        },
        'valid_name_list' : [errint],
    },
}

card_4_order_map = {
    0 : (err, None, card_4_identifier_map.get(err)),
    1 : (tempr, None, card_4_identifier_map.get(tempr)),
    2 : (errmax, None, card_4_identifier_map.get(errmax)),
    3 : (errint, None, card_4_identifier_map.get(errint)),
}

##############################################################################
# reconr card 5:

# Internal identifier names for card 5. Alter valid_name_list in identifier
# map to add alternative identifier names.
cards = 'cards'

card_5_identifier_map = {
    cards : {
        'internal_name' : cards,
        'is_optional' : False,
        'value' : {
            'node_type' : 'string',
            'default_value' : None,
            'length' : 80,
        },
        'valid_name_list' : [cards],
    },
}

card_5_order_map = {
    0 : (cards, None, card_5_identifier_map.get(cards)),
}

##############################################################################
# reconr card 6:

# Internal identifier names for card 6. Alter valid_name_list in identifier
# map to add alternative identifier names.
enode = 'enode'

card_6_identifier_map = {
    enode : {
        'internal_name' : enode,
        'is_optional' : False,
        'value' : {
            # XXX: Type? Range?
            'node_type' : None,
            'default_value' : None,
        },
        'valid_name_list' : [enode],
    },
}

card_6_order_map = {
    0 : (enode, None, card_6_identifier_map.get(enode)),
}
