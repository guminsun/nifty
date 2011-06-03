import settings

material_number = settings.material_number
unit_number = settings.unit_number

##############################################################################
# groupr card 1:

# Internal identifier names for card 1. Alter valid_name_list in identifier
# map to add alternative identifier names.
nendf = 'nendf'
npend = 'npend'
ngout1 = 'ngout1'
ngout2 = 'ngout2'

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
    ngout1 : {
        'internal_name' : ngout1,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 0,
            'slice_list' : unit_number,
        },
        'valid_name_list' : [ngout1],
    },
    ngout2 : {
        'internal_name' : ngout2,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 0,
            'slice_list' : unit_number,
        },
        'valid_name_list' : [ngout2],
    },
}

card_1_order_map = {
    0 : (nendf, None, card_1_identifier_map.get(nendf)),
    1 : (npend, None, card_1_identifier_map.get(npend)),
    2 : (ngout1, None, card_1_identifier_map.get(ngout1)),
    3 : (ngout2, None, card_1_identifier_map.get(ngout2)),
}

##############################################################################
# groupr card 2:

# Internal identifier names for card 2. Alter valid_name_list in identifier
# map to add alternative identifier names.
matb = 'matb'
ign = 'ign'
igg = 'igg'
iwt = 'iwt'
lord = 'lord'
ntemp = 'ntemp'
nsigz = 'nsigz'
iprint = 'iprint'

card_2_identifier_map = {
    matb : {
        'internal_name' : matb,
        'is_optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            # matb may be negative, as such not a regular material number.
            'slice_list' : None,
        },
        'valid_name_list' : [matb],
    },
    ign : {
        'internal_name' : ign,
        'is_optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : [slice(1, 24)],
        },
        'valid_name_list' : [ign],
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
            # XXX: Range?
            'slice_list' : None,
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
    nsigz : {
        'internal_name' : nsigz,
        'is_optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : [slice(0, float('inf'))],
        },
        'valid_name_list' : [nsigz],
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
    1 : (ign, None, card_2_identifier_map.get(ign)),
    2 : (igg, None, card_2_identifier_map.get(igg)),
    3 : (iwt, None, card_2_identifier_map.get(iwt)),
    4 : (lord, None, card_2_identifier_map.get(lord)),
    5 : (ntemp, None, card_2_identifier_map.get(ntemp)),
    6 : (nsigz, None, card_2_identifier_map.get(nsigz)),
    7 : (iprint, None, card_2_identifier_map.get(iprint)),
}

##############################################################################
# groupr card 3:

# Internal identifier names for card 3. Alter valid_name_list in identifier
# map to add alternative identifier names.
title = 'title'

card_3_identifier_map = {
    title : {
        'internal_name' : title,
        'is_optional' : True,
        'value' : {
            'node_type' : 'string',
            'default_value' : '',
            'length' : 80,
        },
        'valid_name_list' : [title],
    },
}

card_3_order_map = {
    0 : (title, None, card_3_identifier_map.get(title)),
}

##############################################################################
# groupr card 4:

# Internal identifier names for card 4. Alter valid_name_list in identifier
# map to add alternative identifier names.
temp = 'temp'

card_4_identifier_map = {
    temp : {
        'internal_name' : temp,
        'is_optional' : False,
        'value' : {
            # XXX: Must be number?
            'node_type' : None,
            'default_value' : None,
        },
        'valid_name_list' : [temp],
    },
}

# Order map needs to be determined when ntemp has been defined in card 2.
card_4_order_map = {}

##############################################################################
# groupr card 5:

# Internal identifier names for card 5. Alter valid_name_list in identifier
# map to add alternative identifier names.
sigz = 'sigz'

card_5_identifier_map = {
    sigz : {
        'internal_name' : sigz,
        'is_optional' : False,
        'value' : {
            # XXX: Must be number?
            'node_type' : None,
            'default_value' : None,
        },
        'valid_name_list' : [sigz],
    },
}

# Order map needs to be set when nsigz has been defined in card 2.
card_5_order_map = {}

##############################################################################
# groupr card 6a:

# Internal identifier names for card 6a. Alter valid_name_list in identifier
# map to add alternative identifier names.
ngn = 'ngn'

card_6a_identifier_map = {
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

card_6a_order_map = {
    0 : (ngn, None, card_6a_identifier_map.get(ngn)),
}

##############################################################################
# groupr card 6b:

# Internal identifier names for card 6b. Alter valid_name_list in identifier
# map to add alternative identifier names.
egn = 'egn'

card_6b_identifier_map = {
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

# Order map needs to be set when egn in card 6a has been defined.
card_6b_order_map = {}

##############################################################################
# groupr card 7a:

# Internal identifier names for card 7a. Alter valid_name_list in identifier
# map to add alternative identifier names.
ngg = 'ngg'

card_7a_identifier_map = {
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
}

card_7a_order_map = {
    0 : (ngg, None, card_7a_identifier_map.get(ngg)),
}

##############################################################################
# groupr card 7b:

# Internal identifier names for card 7b. Alter valid_name_list in identifier
# map to add alternative identifier names.
egg = 'egg'

card_7b_identifier_map = {
    egg : {
        'internal_name' : egg,
        'is_optional' : False,
        'value' : {
            # XXX: Type? Range?
            'node_type' : None,
            'default_value' : None,
        },
        'valid_name_list' : [egg],
    },
}

# Order map needs to be set when ngg in card 7a has been defined.
card_7b_order_map = {}

##############################################################################
# groupr card 8a:

# Internal identifier names for card 8a. Alter valid_name_list in identifier
# map to add alternative identifier names.
ehi = 'ehi'
sigpot = 'sigpot'
nflmax = 'nflmax'
ninwt = 'ninwt'
jsigz = 'jsigz'
alpha2 = 'alpha2'
sam = 'sam'
beta = 'beta'
alpha3 = 'alpha3'
gamma = 'gamma'

card_8a_identifier_map = {
    ehi : {
        'internal_name' : ehi,
        'is_optional' : False,
        'value' : {
            # XXX: Type? Range?
            'node_type' : None,
            'default_value' : None,
        },
        'valid_name_list' : [ehi],
    },
    sigpot : {
        'internal_name' : sigpot,
        'is_optional' : False,
        'value' : {
            # XXX: Type? Range?
            'node_type' : None,
            'default_value' : None,
        },
        'valid_name_list' : [sigpot],
    },
    nflmax : {
        'internal_name' : nflmax,
        'is_optional' : False,
        'value' : {
            # XXX: Range?
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : None,
        },
        'valid_name_list' : [nflmax],
    },
    ninwt : {
        'internal_name' : ninwt,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 0,
            'slice_list' : unit_number,
        },
        'valid_name_list' : [ninwt],
    },
    jsigz : {
        'internal_name' : jsigz,
        'is_optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 0,
            # XXX: Range?
            'slice_list' : None,
        },
        'valid_name_list' : [jsigz],
    },
    alpha2 : {
        'internal_name' : alpha2,
        'is_optional' : True,
        'value' : {
            # XXX: Type? Range?
            'node_type' : None,
            'default_value' : 0,
        },
        'valid_name_list' : [alpha2],
    },
    sam : {
        'internal_name' : sam,
        'is_optional' : True,
        'value' : {
            # XXX: Type? Range?
            'node_type' : None,
            'default_value' : 0,
        },
        'valid_name_list' : [sam],
    },
    beta : {
        'internal_name' : beta,
        'is_optional' : True,
        'value' : {
            # XXX: Type? Range?
            'node_type' : None,
            'default_value' : 0,
        },
        'valid_name_list' : [beta],
    },
    alpha3 : {
        'internal_name' : alpha3,
        'is_optional' : True,
        'value' : {
            # XXX: Type? Range?
            'node_type' : None,
            'default_value' : 0,
        },
        'valid_name_list' : [alpha3],
    },
    gamma : {
        'internal_name' : gamma,
        'is_optional' : True,
        'value' : {
            # XXX: Type? Range?
            'node_type' : None,
            'default_value' : 0,
        },
        'valid_name_list' : [gamma],
    },
}

card_8a_order_map = {
    0 : (ehi, None, card_8a_identifier_map.get(ehi)),
    1 : (sigpot, None, card_8a_identifier_map.get(sigpot)),
    2 : (nflmax, None, card_8a_identifier_map.get(nflmax)),
    3 : (ninwt, None, card_8a_identifier_map.get(ninwt)),
    4 : (jsigz, None, card_8a_identifier_map.get(jsigz)),
    5 : (alpha2, None, card_8a_identifier_map.get(alpha2)),
    6 : (sam, None, card_8a_identifier_map.get(sam)),
    7 : (beta, None, card_8a_identifier_map.get(beta)),
    8 : (alpha3, None, card_8a_identifier_map.get(alpha3)),
    9 : (gamma, None, card_8a_identifier_map.get(gamma)),
}

##############################################################################
# groupr card 8b:

# Internal identifier names for card 8b. Alter valid_name_list in identifier
# map to add alternative identifier names.
wght = 'wght'

card_8b_identifier_map = {
    wght : {
        'internal_name' : wght,
        'is_optional' : False,
        'value' : {
            # XXX: Type? Range?
            'node_type' : None,
            'default_value' : None,
        },
        'valid_name_list' : [wght],
    },
}

# Order map needs to be set when the number of wght values is known since it
# is supposed to be defined as a ENDF TAB1 record.
card_8b_order_map = {}

##############################################################################
# groupr card 8c:

# Internal identifier names for card 8c. Alter valid_name_list in identifier
# map to add alternative identifier names.
eb = 'eb'
tb = 'tb'
ec = 'ec'
tc = 'tc'

card_8c_identifier_map = {
    eb : {
        'internal_name' : eb,
        'is_optional' : False,
        'value' : {
            # XXX: Type? Range?
            'node_type' : None,
            'default_value' : None,
        },
        'valid_name_list' : [eb],
    },
    tb : {
        'internal_name' : tb,
        'is_optional' : False,
        'value' : {
            # XXX: Type? Range?
            'node_type' : None,
            'default_value' : None,
        },
        'valid_name_list' : [tb],
    },
    ec : {
        'internal_name' : ec,
        'is_optional' : False,
        'value' : {
            # XXX: Type? Range?
            'node_type' : None,
            'default_value' : None,
        },
        'valid_name_list' : [ec],
    },
    tc : {
        'internal_name' : tc,
        'is_optional' : False,
        'value' : {
            # XXX: Type? Range?
            'node_type' : None,
            'default_value' : None,
        },
        'valid_name_list' : [tc],
    },
}

card_8c_order_map = {
    0 : (eb, None, card_8c_identifier_map.get(eb)),
    1 : (tb, None, card_8c_identifier_map.get(tb)),
    2 : (ec, None, card_8c_identifier_map.get(ec)),
    3 : (tc, None, card_8c_identifier_map.get(tc)),
}

##############################################################################
# groupr card 8d:

# Internal identifier names for card 8d. Alter valid_name_list in identifier
# map to add alternative identifier names.
ninwt = 'ninwt'

card_8d_identifier_map = {
    ninwt : {
        'internal_name' : ninwt,
        'is_optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            # Binary unit number.
            'slice_list' : [slice(-99, 0)],
        },
        'valid_name_list' : [ninwt],
    },
}

card_8d_order_map = {
    0 : (ninwt, None, card_8d_identifier_map.get(ninwt)),
}

##############################################################################
# groupr card 9:

# Internal identifier names for card 9. Alter valid_name_list in identifier
# map to add alternative identifier names.
mfd = 'mfd'
mtd = 'mtd'
mtname = 'mtname'

card_9_identifier_map = {
    mfd : {
        'internal_name' : mfd,
        'is_optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            # XXX: ENDF file number?
            'slice_list' : None,
        },
        'valid_name_list' : [mfd],
    },
    mtd : {
        'internal_name' : mtd,
        'is_optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            # XXX: ENDF section number?
            'slice_list' : None,
        },
        'valid_name_list' : [mtd],
    },
    mtname : {
        'internal_name' : mtname,
        'is_optional' : False,
        'value' : {
            'node_type' : 'string',
            'default_value' : None,
            # XXX: Length?
            'length' : None,
        },
        'valid_name_list' : [mtname],
    },
}

card_9_order_map = {
    0 : (mfd, None, card_9_identifier_map.get(mfd)),
    1 : (mtd, None, card_9_identifier_map.get(mtd)),
    2 : (mtname, None, card_9_identifier_map.get(mtname)),
}

##############################################################################
# groupr card 10:

# Internal identifier names for card 10. Alter valid_name_list in identifier
# map to add alternative identifier names.
matd = 'matd'

card_10_identifier_map = {
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

card_10_order_map = {
    0 : (matd, None, card_10_identifier_map.get(matd)),
}
