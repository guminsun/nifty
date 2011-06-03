import settings

material_number = settings.material_number
unit_number = settings.unit_number

##############################################################################
# acer card 1:

# Internal identifier names for card 1.
nendf = 'nendf'
npend = 'npend'
ngend = 'ngend'
nace = 'nace'
ndir = 'ndir'

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
        'valid_name_list' : [nendf, 'endf_input'],
    },
    npend : {
        'internal_name' : npend,
        'is_optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : unit_number,
        },
        'valid_name_list' : [npend, 'pendf_input'],
    },
    ngend : {
        'internal_name' : ngend,
        'is_optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : unit_number,
        },
        'valid_name_list' : [ngend, 'multigroup_photon_input'],
    },
    nace : {
        'internal_name' : nace,
        'is_optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : unit_number,
        },
        'valid_name_list' : [nace, 'ace_output'],
    },
    ndir : {
        'internal_name' : ndir,
        'is_optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : unit_number,
        },
        'valid_name_list' : [ndir, 'mcnp_directory_output'],
    },
}

card_1_order_map = {
    0 : (nendf, None, card_1_identifier_map.get(nendf)),
    1 : (npend, None, card_1_identifier_map.get(npend)),
    2 : (ngend, None, card_1_identifier_map.get(ngend)),
    3 : (nace, None, card_1_identifier_map.get(nace)),
    4 : (ndir, None, card_1_identifier_map.get(ndir)),
}

##############################################################################
# acer card 2:

# Internal identifiers names for card 2.
iopt = 'iopt'
iprint = 'iprint'
ntype = 'ntype'
suff = 'suff'
nxtra = 'nxtra'

card_2_identifier_map = {
    iopt : {
        'internal_name' : iopt,
        'is_optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : [slice(-8, -6), slice(-5, 0), slice(1, 6), slice(7, 9)],
        },
        'valid_name_list' : [iopt, 'acer_run_option'],
    },
    iprint : {
        'internal_name' : iprint,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 1,
            # iprint is expected to be either 0 or 1.
            'slice_list' : [slice(0, 2)],
        },
        'valid_name_list' : [iprint, 'print_control'],
    },
    ntype : {
        'internal_name' : ntype,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 1,
            # ntype is expected to be either 1, 2 or 3.
            'slice_list' : [slice(1, 4)],
        },
        'valid_name_list' : [ntype, 'ace_output_type'],
    },
    suff : {
        'internal_name' : suff,
        'is_optional' : True,
        'value' : {
            # XXX: Unknown type, may be either integer or float?
            'node_type' : None,
            'default_value' : 0.00,
        },
        'valid_name_list' : [suff],
    },
    nxtra : {
        'internal_name' : nxtra,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 0,
            # Expecting a non-negative number.
            'slice_list' : [slice(0, float('inf'))],
        },
        'valid_name_list' : [nxtra],
    },
}

card_2_order_map = {
    0 : (iopt, None, card_2_identifier_map.get(iopt)),
    1 : (iprint, None, card_2_identifier_map.get(iprint)),
    2 : (ntype, None, card_2_identifier_map.get(ntype)),
    3 : (suff, None, card_2_identifier_map.get(suff)),
    4 : (nxtra, None, card_2_identifier_map.get(nxtra)),
}

##############################################################################
# acer card 3:

# Internal identifier names for card 3.
hk = 'hk'

card_3_identifier_map = {
    hk : {
        'internal_name' : hk,
        # hk must be defined, it is not optional.
        'is_optional' : False,
        'value' : {
            'node_type' : 'string',
            # hk has no default value since it must be defined.
            'default_value' : None,
            # Allowed length of hk.
            'length' : 70,
        },
        'valid_name_list' : [hk, 'description'],
    },
}

card_3_order_map = {
    0 : (hk, None, card_3_identifier_map.get(hk)),
}

##############################################################################
# acer card 4:

# Internal identifier names for card 4.
iz = 'iz'
aw = 'aw'

card_4_identifier_map = {
    iz : {
        'internal_name' : iz,
        'is_optional' : False,
        'value' : {
            # XXX: Unknown value type.
            'node_type' : None,
            'default_value' : None,
        },
        'valid_name_list' : [iz],
    },
    aw : {
        'internal_name' : aw,
        'is_optional' : False,
        'value' : {
            # XXX: Unknown value type.
            'node_type' : None,
            'default_value' : None,
        },
        'valid_name_list' : [aw],
    },
}

# The expected order is unknown until nxtra has been defined in card 2. The
# expected order map will be constructed locally in the acer analyzer,
# function analyze_acer_card_4.
card_4_order_map = {}

##############################################################################
# acer card 5:

# Internal names for card 5.
matd = 'matd'
tempd = 'tempd'

card_5_identifier_map = {
    matd : {
        'internal_name' : matd,
        'is_optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : material_number,
        },
        'valid_name_list' : [matd, 'material'],
    },
    tempd : {
        'internal_name' : tempd,
        'is_optional' : True,
        'value' : {
            # XXX: Not fixed value type. May be either float or integer.
            # Introduce 'number' and must_be_number?
            'node_type' : None,
            'default_value' : 300,
        },
        'valid_name_list' : [tempd, 'temperature'],
    },
}

card_5_order_map = {
    0 : (matd, None, card_5_identifier_map.get(matd)),
    1 : (tempd, None, card_5_identifier_map.get(tempd)),
}

##############################################################################
# acer card 6:

# Internal identifier names for card 6.
newfor = 'newfor'
iopp = 'iopp'

card_6_identifier_map = {
    newfor : {
        'internal_name' : newfor,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 1,
            'slice_list' : [slice(0, 2)],
        },
        'valid_name_list' : [newfor],
    },
    iopp : {
        'internal_name' : iopp,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 1,
            'slice_list' : [slice(0, 2)],
        },
        'valid_name_list' : [iopp],
    },
}

card_6_order_map = {
    0 : (newfor, None, card_6_identifier_map.get(newfor)),
    1 : (iopp, None, card_6_identifier_map.get(iopp)),
}

##############################################################################
# acer card 7:

# Note the names of the identifiers. Differs slightly from the NJOY
# documentation. Consider defining thin as an array declaration instead?

# Internal identifier names for card 7.
thin01 = 'thin01'
thin02 = 'thin02'
thin03 = 'thin03'

card_7_identifier_map = {
    thin01 : {
        'internal_name' : thin01,
        'is_optional' : True,
        'value' : {
            # XXX: Must be number?
            'node_type' : None,
            'default_value' : None,
        },
        'valid_name_list' : [thin01],
    },
    thin02 : {
        'internal_name' : thin02,
        'is_optional' : True,
        'value' : {
            # XXX: Must be number?
            'node_type' : None,
            'default_value' : None,
        },
        'valid_name_list' : [thin02],
    },
    thin03 : {
        'internal_name' : thin03,
        'is_optional' : True,
        'value' : {
            # XXX: Must be number?
            'node_type' : None,
            'default_value' : None,
        },
        'valid_name_list' : [thin03],
    },
}

card_7_order_map = {
    0 : (thin01, None, card_7_identifier_map.get(thin01)),
    1 : (thin02, None, card_7_identifier_map.get(thin02)),
    2 : (thin03, None, card_7_identifier_map.get(thin03)),
}

##############################################################################
# acer card 8:

# Internal identifier names for card 8.
matd = 'matd'
tempd = 'tempd'
tname = 'tname'

card_8_identifier_map = {
    matd : {
        'internal_name' : matd,
        'is_optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : material_number,
        },
        'valid_name_list' : [matd, 'material'],
    },
    tempd : {
        'internal_name' : tempd,
        'is_optional' : True,
        'value' : {
            # XXX: Must be number?
            'node_type' : None,
            'default_value' : 300,
        },
        'valid_name_list' : [tempd],
    },
    tname : {
        'internal_name' : tname,
        'is_optional' : True,
        'value' : {
            'node_type' : 'string',
            'default_value' : 'za',
            'length' : 6,
        },
        'valid_name_list' : [tname],
    },
}

card_8_order_map = {
    0 : (matd, None, card_8_identifier_map.get(matd)),
    1 : (tempd, None, card_8_identifier_map.get(tempd)),
    2 : (tname, None, card_8_identifier_map.get(tname)),
}

##############################################################################
# acer card 8a:

# XXX: Treat iza{01,02,03} as an array instead?

# Internal identifier names for card 8a.
iza01 = 'iza01'
iza02 = 'iza02'
iza03 = 'iza03'

card_8a_identifier_map = {
    iza01 : {
        'internal_name' : iza01,
        'is_optional' : False,
        'value' : {
            # XXX: Must be an integer?
            'node_type' : None,
            'default_value' : None,
        },
        'valid_name_list' : [iza01],
    },
    iza02 : {
        'internal_name' : iza02,
        'is_optional' : True,
        'value' : {
            # XXX: Must be an integer?
            'node_type' : None,
            'default_value' : 0,
        },
        'valid_name_list' : [iza02],
    },
    iza03 : {
        'internal_name' : iza03,
        'is_optional' : True,
        'value' : {
            # XXX: Must be an integer?
            'node_type' : None,
            'default_value' : 0,
        },
        'valid_name_list' : [iza03],
    },
}

card_8a_order_map = {
    0 : (iza01, None, card_8a_identifier_map.get(iza01)),
    1 : (iza02, None, card_8a_identifier_map.get(iza02)),
    2 : (iza03, None, card_8a_identifier_map.get(iza03)),
}

##############################################################################
# acer card 9:

# Internal identifier names for card 9.
mti = 'mti'
nbint = 'nbint'
mte = 'mte'
ielas = 'ielas'
nmix = 'nmix'
emax = 'emax'
iwt = 'iwt'

card_9_identifier_map = {
    mti : {
        'internal_name' : mti,
        'is_optional' : False,
        'value' : {
            # XXX: Type?
            'node_type' : None,
            'default_value' : None,
        },
        'valid_name_list' : [mti],
    },
    nbint : {
        'internal_name' : nbint,
        'is_optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            # Expecting a non-negative number.
            'slice_list' : [slice(0, float('inf'))],
        },
        'valid_name_list' : [nbint],
    },
    mte : {
        'internal_name' : mte,
        'is_optional' : False,
        'value' : {
            # XXX: Type?
            'node_type' : None,
            'default_value' : None,
        },
        'valid_name_list' : [mte],
    },
    ielas : {
        'internal_name' : ielas,
        'is_optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : [slice(0, 2)],
        },
        'valid_name_list' : [ielas],
    },
    nmix : {
        'internal_name' : nmix,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 1,
            # Expecting a non-negative number.
            'slice_list' : [slice(0, float('inf'))],
        },
        'valid_name_list' : [nmix],
    },
    emax : {
        'internal_name' : emax,
        'is_optional' : True,
        'value' : {
            # XXX: Must be number?
            'node_type' : None,
            'default_value' : 1000.0,
        },
        'valid_name_list' : [emax],
    },
    iwt : {
        'internal_name' : iwt,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 1,
            'slice_list' : [slice(0, 3)],
        },
        'valid_name_list' : [iwt],
    },
}

card_9_order_map = {
    0 : (mti, None, card_9_identifier_map.get(mti)),
    1 : (nbint, None, card_9_identifier_map.get(nbint)),
    2 : (mte, None, card_9_identifier_map.get(mte)),
    3 : (ielas, None, card_9_identifier_map.get(ielas)),
    4 : (nmix, None, card_9_identifier_map.get(nmix)),
    5 : (emax, None, card_9_identifier_map.get(emax)),
    6 : (iwt, None, card_9_identifier_map.get(iwt)),
}

##############################################################################
# acer card 10:

# Internal identifier names for card 10.
matd = 'matd'
tempd = 'tempd'

card_10_identifier_map = {
    matd : {
        'internal_name' : matd,
        'is_optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : material_number,
        },
        'valid_name_list' : [matd, 'material'],
    },
    tempd : {
        'internal_name' : tempd,
        'is_optional' : True,
        'value' : {
            # XXX: Must be number?
            'node_type' : None,
            'default_value' : 300,
        },
        'valid_name_list' : [tempd, 'temperature'],
    },
}

card_10_order_map = {
    0 : (matd, None, card_10_identifier_map.get(matd)),
    1 : (tempd, None, card_10_identifier_map.get(tempd)),
}

##############################################################################
# acer card 11:

# Internal identifier names for card 11.
matd = 'matd'

card_11_identifier_map = {
    matd : {
        'internal_name' : matd,
        'is_optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : material_number,
        },
        'valid_name_list' : [matd, 'material'],
    },
}

card_11_order_map = {
    0 : (matd, None, card_11_identifier_map.get(matd)),
}
