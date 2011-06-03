import settings

material_number = settings.material_number
unit_number = settings.unit_number

##############################################################################
# thermr card 1:

# Internal identifier names for card 1. Alter valid_name_list in identifier
# map to add alternative identifier names.
nendf = 'nendf'
nin = 'nin'
nout = 'nout'

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
}

card_1_order_map = {
    0 : (nendf, None, card_1_identifier_map.get(nendf)),
    1 : (nin, None, card_1_identifier_map.get(nin)),
    2 : (nout, None, card_1_identifier_map.get(nout)),
}

##############################################################################
# thermr card 2:

# Internal identifier names for card 1. Alter valid_name_list in identifier
# map to add alternative identifier names.
matde = 'matde'
matdp = 'matdp'
nbin = 'nbin'
ntemp = 'ntemp'
iinc = 'iinc'
icoh = 'icoh'
natom = 'natom'
mtref = 'mtref'
iprint = 'iprint'

card_2_identifier_map = {
    matde : {
        'internal_name' : matde,
        'is_optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : material_number,
        },
        'valid_name_list' : [matde],
    },
    matdp : {
        'internal_name' : matdp,
        'is_optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : material_number,
        },
        'valid_name_list' : [matdp],
    },
    nbin : {
        'internal_name' : nbin,
        'is_optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : [slice(0, float('inf'))],
        },
        'valid_name_list' : [nbin],
    },
    ntemp : {
        'internal_name' : ntemp,
        'is_optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : [slice(0, float('inf'))],
        },
        'valid_name_list' : [ntemp],
    },
    iinc : {
        'internal_name' : iinc,
        'is_optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : [slice(0, 5)],
        },
        'valid_name_list' : [iinc],
    },
    icoh : {
        'internal_name' : icoh,
        'is_optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            # XXX: Check range depending on which ENDF version it is.
            'slice_list' : [slice(0, 4), slice(11, 14)],
        },
        'valid_name_list' : [icoh],
    },
    natom : {
        'internal_name' : natom,
        'is_optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : [slice(0, float('inf'))],
        },
        'valid_name_list' : [natom],
    },
    mtref : {
        'internal_name' : mtref,
        'is_optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : [slice(221, 251)],
        },
        'valid_name_list' : [mtref],
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
}

card_2_order_map = {
    0 : (matde, None, card_2_identifier_map.get(matde)),
    1 : (matdp, None, card_2_identifier_map.get(matdp)),
    2 : (nbin, None, card_2_identifier_map.get(nbin)),
    3 : (ntemp, None, card_2_identifier_map.get(ntemp)),
    4 : (iinc, None, card_2_identifier_map.get(iinc)),
    5 : (icoh, None, card_2_identifier_map.get(icoh)),
    6 : (natom, None, card_2_identifier_map.get(natom)),
    7 : (mtref, None, card_2_identifier_map.get(mtref)),
    8 : (iprint, None, card_2_identifier_map.get(iprint)),
}

##############################################################################
# thermr card 3:

# Internal identifier names for card 3. Alter valid_name_list in identifier
# map to add alternative identifier names.
tempr = 'tempr'

card_3_identifier_map = {
    tempr : {
        'internal_name' : tempr,
        'is_optional' : False,
        'value' : {
            # XXX: Type? Range?
            'node_type' : None,
            'default_value' : None,
        },
        'valid_name_list' : [tempr],
    },
}

card_3_order_map = {}

##############################################################################
# thermr card 4:

# Internal identifier names for card 4. Alter valid_name_list in identifier
# map to add alternative identifier names.
tol = 'tol'
emax = 'emax'

card_4_identifier_map = {
    tol : {
        'internal_name' : tol,
        'is_optional' : False,
        'value' : {
            # XXX: Type? Range?
            'node_type' : None,
            'default_value' : None,
        },
        'valid_name_list' : [tol],
    },
    emax : {
        'internal_name' : emax,
        'is_optional' : False,
        'value' : {
            # XXX: Type? Range?
            'node_type' : None,
            'default_value' : None,
        },
        'valid_name_list' : [emax],
    },
}

card_4_order_map = {
    0 : (tol, None, card_4_identifier_map.get(tol)),
    1 : (emax, None, card_4_identifier_map.get(emax)),
}
