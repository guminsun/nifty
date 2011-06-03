import settings

material_number = settings.material_number
unit_number = settings.unit_number

##############################################################################
# purr card 1:

# Internal identifier names for card 1.
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
# purr card 2:

# Internal identifier names for card 2.
matd = 'matd'
ntemp = 'ntemp'
nsigz = 'nsigz'
nbin = 'nbin'
nladr = 'nladr'
iprint = 'iprint'
nunx = 'nunx'

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
    nbin : {
        'internal_name' : nbin,
        'is_optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : [slice(15, float('inf'))],
        },
        'valid_name_list' : [nbin],
    },
    nladr : {
        'internal_name' : nladr,
        'is_optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : [slice(0, float('inf'))],
        },
        'valid_name_list' : [nladr],
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
    nunx : {
        'internal_name' : nunx,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 0,
            'slice_list' : [slice(0, float('inf'))],
        },
        'valid_name_list' : [nunx],
    },
}

card_2_order_map = {
    0 : (matd, None, card_2_identifier_map.get(matd)),
    1 : (ntemp, None, card_2_identifier_map.get(ntemp)),
    2 : (nsigz, None, card_2_identifier_map.get(nsigz)),
    3 : (nbin, None, card_2_identifier_map.get(nbin)),
    4 : (nladr, None, card_2_identifier_map.get(nladr)),
    5 : (iprint, None, card_2_identifier_map.get(iprint)),
    6 : (nunx, None, card_2_identifier_map.get(nunx)),
}

##############################################################################
# purr card 3:

# Internal identifier names for card 3.
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

# Number of temp values is determined by the ntemp value in card 2. Order map
# needs to be constructed when the ntemp value is known.
card_3_order_map = {}

##############################################################################
# purr card 4:

# Internal identifier names for card 4.
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

# Number of sigz values is determined by the nsigz value in card 2. Order map
# needs to be constructed when the nsigz value is known.
card_4_order_map = {}
