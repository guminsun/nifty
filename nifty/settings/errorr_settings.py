import settings

material_number = settings.material_number
unit_number = settings.unit_number

##############################################################################
# errorr card 1:

# Internal identifier names for card 1. Alter valid_name_list in identifier
# map to add alternative identifier names.
nendf = 'nendf'
npend = 'npend'
ngout = 'ngout'
nout = 'nout'
nin = 'nin'
nstan = 'nstan'

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
    ngout : {
        'internal_name' : ngout,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 0,
            'slice_list' : unit_number,
        },
        'valid_name_list' : [ngout],
    },
    nout : {
        'internal_name' : nout,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 0,
            'slice_list' : unit_number,
        },
        'valid_name_list' : [nout],
    },
    nin : {
        'internal_name' : nin,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 0,
            'slice_list' : unit_number,
        },
        'valid_name_list' : [nin],
    },
    nstan : {
        'internal_name' : nstan,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 0,
            'slice_list' : unit_number,
        },
        'valid_name_list' : [nstan],
    },
}

card_1_order_map = {
    0 : (nendf, None, card_1_identifier_map.get(nendf)),
    1 : (npend, None, card_1_identifier_map.get(npend)),
    2 : (ngout, None, card_1_identifier_map.get(ngout)),
    3 : (nout, None, card_1_identifier_map.get(nout)),
    4 : (nin, None, card_1_identifier_map.get(nin)),
    5 : (nstan, None, card_1_identifier_map.get(nstan)),
}

##############################################################################
# errorr card 2:

# Internal identifier names for card 2.
matd = 'matd'
ign = 'ign'
iwt = 'iwt'
iprint = 'iprint'
irelco = 'irelco'

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
    ign : {
        'internal_name' : ign,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 1,
            'slice_list' : [slice(1, 20)],
        },
        'valid_name_list' : [ign],
    },
    iwt : {
        'internal_name' : iwt,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 6,
            'slice_list' : [slice(1, 13)],
        },
        'valid_name_list' : [iwt],
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
    irelco : {
        'internal_name' : irelco,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 1,
            'slice_list' : [slice(0, 2)],
        },
        'valid_name_list' : [irelco],
    },
}

card_2_order_map = {
    0 : (matd, None, card_2_identifier_map.get(matd)),
    1 : (ign, None, card_2_identifier_map.get(ign)),
    2 : (iwt, None, card_2_identifier_map.get(iwt)),
    3 : (iprint, None, card_2_identifier_map.get(iprint)),
    4 : (irelco, None, card_2_identifier_map.get(irelco)),
}

##############################################################################
# errorr card 3:

# Internal identifier names for card 3.
mprint = 'mprint'
tempin = 'tempin'

card_3_identifier_map = {
    mprint : {
        'internal_name' : mprint,
        'is_optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : [slice(0, 2)],
        },
        'valid_name_list' : [mprint],
    },
    tempin : {
        'internal_name' : tempin,
        'is_optional' : True,
        'value' : {
            # XXX: Must be number?
            'node_type' : None,
            'default_value' : 300,
        },
        'valid_name_list' : [tempin],
    },
}

card_3_order_map = {
    0 : (mprint, None, card_3_identifier_map.get(mprint)),
    1 : (tempin, None, card_3_identifier_map.get(tempin)),
}

##############################################################################
# errorr card 4:

# Internal identifier names for card 4.
nek = 'nek'

card_4_identifier_map = {
    nek : {
        'internal_name' : nek,
        'is_optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : [slice(0, float('inf'))],
        },
        'valid_name_list' : [nek],
    },
}

card_4_order_map = {
    0 : (nek, None, card_4_identifier_map.get(nek)),
}

##############################################################################
# errorr card 5:

# Internal identifier names for card 5.
ek = 'ek'

card_5_identifier_map = {
    ek : {
        'internal_name' : ek,
        'is_optional' : False,
        'value' : {
            # XXX: Must be number?
            'node_type' : None,
            'default_value' : None,
        },
        'valid_name_list' : [ek],
    },
}

# Number ek values depends on nek defined in card 4. Order map needs to be
# constructed when the nek value is known. Note that card 5 should be omitted
# if nek = 0.
card_5_order_map = {}

##############################################################################
# errorr card 6:

# Internal identifier names for card 6.
akxy = 'akxy'

card_6_identifier_map = {
    akxy : {
        'internal_name' : akxy,
        'is_optional' : False,
        'value' : {
            # XXX: Must be number?
            'node_type' : None,
            'default_value' : None,
        },
        'valid_name_list' : [akxy],
    },
}

# Note that card 6 should be omitted if nek = 0 in card 4.
card_6_order_map = {}

##############################################################################
# errorr card 7:

# Internal identifier names for card 7.
iread = 'iread'
mfcov = 'mfcov'
irespr = 'irespr'
legord = 'legord'
ifissp = 'ifissp'
emean = 'emean'
dap = 'dap'

card_7_identifier_map = {
    iread : {
        'internal_name' : iread,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 0,
            'slice_list' : [slice(0, 4)],
        },
        'valid_name_list' : [iread],
    },
    mfcov : {
        'internal_name' : mfcov,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 33,
            'slice_list' : [slice(31, 32), slice(33, 36), slice(40, 41)],
        },
        'valid_name_list' : [mfcov],
    },
    irespr : {
        'internal_name' : irespr,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 1,
            'slice_list' : [slice(0, 2)],
        },
        'valid_name_list' : [irespr],
    },
    legord : {
        'internal_name' : legord,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 1,
            'slice_list' : None,
        },
        'valid_name_list' : [legord],
    },
    ifissp : {
        'internal_name' : ifissp,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : -1,
            'slice_list' : None,
        },
        'valid_name_list' : [ifissp],
    },
    efmean : {
        'internal_name' : efmean,
        'is_optional' : True,
        'value' : {
            # XXX: Must be float? Range?
            'node_type' : None,
            'default_value' : 2.0,
        },
        'valid_name_list' : [efmean],
    },
    dap : {
        'internal_name' : dap,
        'is_optional' : True,
        'value' : {
            'node_type' : 'float',
            'default_value' : 0.0,
        },
        'valid_name_list' : [dap],
    },
}

card_7_order_map = {
    0 : (iread, None, card_7_identifier_map.get(iread)),
    1 : (mfcov, None, card_7_identifier_map.get(mfcov)),
    2 : (irespr, None, card_7_identifier_map.get(irespr)),
    3 : (legord, None, card_7_identifier_map.get(legord)),
    4 : (ifissp, None, card_7_identifier_map.get(ifissp)),
    5 : (efmean, None, card_7_identifier_map.get(efmean)),
    6 : (dap, None, card_7_identifier_map.get(dap)),
}

##############################################################################
# errorr card 8:

# Internal identifier names for card 8.
nmt = 'nmt'
nek = 'nek'

card_8_identifier_map = {
    nmt : {
        'internal_name' : nmt,
        'is_optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : [slice(0, float('inf'))],
        },
        'valid_name_list' : [nmt],
    },
    nek : {
        'internal_name' : nek,
        'is_optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : [slice(0, float('inf'))],
        },
        'valid_name_list' : [nek],
    },
}

card_8_order_map = {
    0 : (nmt, None, card_8_identifier_map.get(nmt)),
    1 : (nek, None, card_8_identifier_map.get(nek)),
}

##############################################################################
# errorr card 8a:

# Internal identifier names for card 8a.
mts = 'mts'

card_8a_identifier_map = {
    mts : {
        'internal_name' : mts,
        'is_optional' : False,
        'value' : {
            # XXX: Must be number? Range?
            'node_type' : None,
            'default_value' : None,
        },
        'valid_name_list' : [mts],
    },
}

# Number of mts values depends on nmt defined in card 8. Order map needs to be
# constructed when the nmt value is known.
card_8a_order_map = {}

##############################################################################
# errorr card 8b:

# Internal identifier names for card 8b.
ek = 'ek'

card_8b_identifier_map = {
    ek : {
        'internal_name' : ek,
        'is_optional' : False,
        'value' : {
            # XXX: Must be number? Range?
            'node_type' : None,
            'default_value' : None,
        },
        'valid_name_list' : [ek],
    },
}

# Number of ek values depends on nek defined in card 8. Order map needs to be
# constructed when the nek value is known. Note that card 8b should be omitted
# if nek = 0.
card_8b_order_map = {}

##############################################################################
# errorr card 9:

card_9_identifier_map = card_6_identifier_map

# Note that card 9 should be omitted if nek = 0 in card 8.
card_9_order_map = {}

##############################################################################
# errorr card 10:

# Internal identifier names for card 10.
mat1 = 'mat1'
mt1 = 'mt1'

card_10_identifier_map = {
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
    mt1 : {
        'internal_name' : mt1,
        'is_optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            # XXX: MT range?
            'slice_list' : None,
        },
        'valid_name_list' : [mt1],
    },
}

# Order map needs to be constructed when the length of the card's statement
# list is known, since there can be an arbitrary number of mat1,mt1 pairs.
card_10_order_map = {}

##############################################################################
# errorr card 11:

# Internal identifier names for card 11.
matb = 'matb'
mtb = 'mtb'
matc = 'matc'
mtc = 'mtc'

# XXX: Need to verify with NJOY source code. Documentation fuzzy.
card_11_identifier_map = {
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
    mtb : {
        'internal_name' : mtb,
        'is_optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            # XXX: MT range?
            'slice_list' : None,
        },
        'valid_name_list' : [mtb],
    },
    matc : {
        'internal_name' : matc,
        'is_optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : material_number,
        },
        'valid_name_list' : [matc],
    },
    mtc : {
        'internal_name' : mtc,
        'is_optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            # XXX: MT range?
            'slice_list' : None,
        },
        'valid_name_list' : [mtc],
    },
}

# Order map needs to be constructed when the length of the card's statement
# list is known, since there can be an arbitrary number of statements.
card_11_order_map = {}

##############################################################################
# errorr card 12a:

# Internal identifier names for card 12a.
ngn = 'ngn'

card_12a_identifier_map = {
    ngn : {
        'internal_name' : ngn,
        'is_optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : [slice(0, float('inf'))],
        },
        'valid_name_list' : [ngn],
    },
}

card_12a_order_map = {
    0 : (ngn, None, card_12a_identifier_map.get(ngn)),
}

##############################################################################
# errorr card 12b:

# Internal identifier names for card 12b.
egn = 'egn'

card_12b_identifier_map = {
    egn : {
        'internal_name' : egn,
        'is_optional' : False,
        'value' : {
            # XXX: Type? Range?
            'node_type' : None,
            'default_value' : None,
        },
        'valid_name_list' : [egn],
    },
}

# The number of egn values depends on the ngn value defined in card 12a. Order
# map needs to be constructed when the ngn value is known.
card_12b_order_map = {}

##############################################################################
# errorr card 13a:

# Internal identifier names for card 13a.
wght = 'wght'

card_13a_identifier_map = {
    wght : {
        'internal_name' : wght,
        'is_optional' : False,
        'value' : {
            # XXX: Must be number? Range?
            'node_type' : None,
            'default_value' : None,
        },
        'valid_name_list' : [wght],
    },
}

# The number of wght values depends on the length of the card's statement list
# since it is a TAB1 record. Order map needs to be constructed when the length
# of thet statement list is known.
card_13a_order_map = {}

##############################################################################
# errorr card 13b:

# Internal identifier names for card 13b.
eb = 'eb'
tb = 'tb'
ec = 'ec'
tc = 'tc'

card_13b_identifier_map = {
    eb : {
        'internal_name' : eb,
        'is_optional' : False,
        'value' : {
            # XXX: Must be number? Range?
            'node_type' : None,
            'default_value' : None,
        },
        'valid_name_list' : [eb],
    },
    tb : {
        'internal_name' : tb,
        'is_optional' : False,
        'value' : {
            # XXX: Must be number? Range?
            'node_type' : None,
            'default_value' : None,
        },
        'valid_name_list' : [tb],
    },
    ec : {
        'internal_name' : ec,
        'is_optional' : False,
        'value' : {
            # XXX: Must be number? Range?
            'node_type' : None,
            'default_value' : None,
        },
        'valid_name_list' : [ec],
    },
    tc : {
        'internal_name' : tc,
        'is_optional' : False,
        'value' : {
            # XXX: Must be number? Range?
            'node_type' : None,
            'default_value' : None,
        },
        'valid_name_list' : [tc],
    },
}

card_13b_order_map = {
    0 : (eb, None, card_13b_identifier_map.get(eb)),
    1 : (tb, None, card_13b_identifier_map.get(tb)),
    2 : (ec, None, card_13b_identifier_map.get(ec)),
    3 : (tc, None, card_13b_identifier_map.get(tc)),
}
