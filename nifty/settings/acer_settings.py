##############################################################################
# acer identifier settings
#
# The identifier maps are used for looking up e.g. valid identifier names in
# a card.
#
# The order maps are used for looking up the expected order of an identifier
# in a card.
#
#### Identifier Maps
#
# The key is the identifier name used internally by the translator and by the
# NJOY documentation. The value associated with each key is a dictionary
# containing meta data for the identifier. Data such as valid, alternative,
# identifier names are set here.
#
# All key-value pairs in the dictionary have the form:
#
#   internal_name : {
#       'node_type' : identifier_declared_as,
#       'optional' : boolean,
#       'value' : value_dict,
#       'valid_name_list' : name_list
#   }
#
# identifier_declared_as is either defined as the string 'array', or
# 'identifier'.
# boolean is either True or False. True indicates that the identifier is
# optional. False indicates that the identifier must be defined.
# value_dict is a dictionary containing meta data which described the expected
# value for the identifier. E.g. whether the expected value is an integer or
# a string value.
# name_list is a list of strings containing valid, alternative, names for the
# identifier.
#
# Each alternative identifier name in name_list must be uniquely associated to
# a single key within the card. Two different keys within the same card are
# not allowed to share an identical, alternative, identifier name.
# It is good practice to keep the internal name, e.g. the key, as the first
# name listed in the valid names list. The keys are of course  assumed to be
# unique within each card as well.
#
# Note the use of Python slices to define the allowed integer ranges in the
# value dictionary.
#
#### Order Maps
#
# Order maps are key-value dictionaries on the form:
#
#   expected_order_index : reference to identifier in identifier map
#
# The key, expected_order_index, in the order maps is an integer number which
# denotes the expected order of the identifier in the card's statement list.
# A key which equals 0 indicates that the associated value is the identifier
# that is expected to appear first in the card's statement list.
# The next expected identifier in the card's statement list should be assigned
# the key 1, and so on.
#

material_number = [slice(0, 10000)]
unit_number = [slice(-99, 0), slice(0, 100)]

##############################################################################
# acer card 1:

card_1_identifier_map = {
    'nendf' : {
        'node_type' : 'identifier',
        # nendf must be defined, it is not optional.
        'optional' : False,
        'value' : {
            'node_type' : 'integer',
            # nendf has no default value since it must be defined.
            'default_value' : None,
            # The integer range of allowed values represented as a list of slices.
            'slice_list' : unit_number,
        },
        'valid_name_list' : ['nendf', 'endf_input'],
    },
    'npend' : {
        'node_type' : 'identifier',
        'optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : unit_number,
        },
        'valid_name_list' : ['npend', 'pendf_input'],
    },
    'ngend' : {
        'node_type' : 'identifier',
        'optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : unit_number,
        },
        'valid_name_list' : ['ngend', 'multigroup_photon_input'],
    },
    'nace' : {
        'node_type' : 'identifier',
        'optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : unit_number,
        },
        'valid_name_list' : ['nace', 'ace_output'],
    },
    'ndir' : {
        'node_type' : 'identifier',
        'optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : unit_number,
        },
        'valid_name_list' : ['ndir', 'mcnp_directory_output'],
    },
}

card_1_order_map = {
    0 : card_1_identifier_map.get('nendf'),
    1 : card_1_identifier_map.get('npend'),
    2 : card_1_identifier_map.get('ngend'),
    3 : card_1_identifier_map.get('nace'),
    4 : card_1_identifier_map.get('ndir'),
}

##############################################################################
# acer card 2:

card_2_identifier_map = {
    'iopt' : {
        'node_type' : 'identifier',
        'optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : [slice(-8, -6), slice(-5, 0), slice(1, 6), slice(7, 9)],
        },
        'valid_name_list' : ['iopt', 'acer_run_option'],
    },
    'iprint' : {
        'node_type' : 'identifier',
        'optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 1,
            # iprint is expected to be either 0 or 1.
            'slice_list' : [slice(0, 2)],
        },
        'valid_name_list' : ['iprint', 'print_control'],
    },
    'ntype' : {
        'node_type' : 'identifier',
        'optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 1,
            # ntype is expected to be either 1, 2 or 3.
            'slice_list' : [slice(1, 4)],
        },
        'valid_name_list' : ['ntype', 'ace_output_type'],
    },
    'suff' : {
        'node_type' : 'identifier',
        'optional' : True,
        'value' : {
            # XXX: Unknown type, may be either integer or float?
            'node_type' : None,
            'default_value' : 0.00,
        },
        'valid_name_list' : ['suff'],
    },
    'nxtra' : {
        'node_type' : 'identifier',
        'optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 0,
            # Expecting a non-negative number.
            'slice_list' : [slice(0, float('inf'))],
        },
        'valid_name_list' : ['nxtra'],
    },
}

card_2_order_map = {
    0 : card_2_identifier_map.get('iopt'),
    1 : card_2_identifier_map.get('iprint'),
    2 : card_2_identifier_map.get('ntype'),
    3 : card_2_identifier_map.get('suff'),
    4 : card_2_identifier_map.get('nxtra'),
}

##############################################################################
# acer card 3:

card_3_identifier_map = {
    'hk' : {
        'node_type' : 'identifier',
        # hk must be defined, it is not optional.
        'optional' : False,
        'value' : {
            'node_type' : 'string',
            # hk has no default value since it must be defined.
            'default_value' : None,
            # Allowed length of hk.
            'length' : 70,
        },
        'valid_name_list' : ['hk', 'description'],
    },
}

card_3_order_map = {
    0 : card_3_identifier_map.get('hk'),
}

##############################################################################
# acer card 4:

card_4_identifier_map = {
    'iz' : {
        'node_type' : 'array',
        'optional' : False,
        'value' : {
            # XXX: Unknown value type.
            'node_type' : None,
            'default_value' : None,
        },
        'valid_name_list' : ['iz'],
    },
    'aw' : {
        'node_type' : 'array',
        'optional' : False,
        'value' : {
            # XXX: Unknown value type.
            'node_type' : None,
            'default_value' : None,
        },
        'valid_name_list' : ['aw'],
    },
}

# The expected order is unknown until nxtra has been defined in card 2. The
# expected order map will be constructed locally in the acer analyzer,
# function analyze_acer_card_4.
card_4_order_map = {}

##############################################################################
# acer card 5:

card_5_identifier_map = {
    'matd' : {
        'node_type' : 'identifier',
        'optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : material_number,
        },
        'valid_name_list' : ['matd', 'material'],
    },
    'tempd' : {
        'node_type' : 'identifier',
        'optional' : True,
        'value' : {
            # XXX: Not fixed value type. May be either float or integer.
            # Introduce 'number' and must_be_number?
            'node_type' : None,
            'default_value' : 300,
        },
        'valid_name_list' : ['tempd', 'temperature'],
    },
}

card_5_order_map = {
    0 : card_5_identifier_map.get('matd'),
    1 : card_5_identifier_map.get('tempd'),
}

##############################################################################
# acer card 6:

card_6_identifier_map = {
    'newfor' : {
        'node_type' : 'identifier',
        'optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 1,
            'slice_list' : [slice(0, 2)],
        },
        'valid_name_list' : ['newfor'],
    },
    'iopp' : {
        'node_type' : 'identifier',
        'optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 1,
            'slice_list' : [slice(0, 2)],
        },
        'valid_name_list' : ['iopp'],
    },
}

card_6_order_map = {
    0 : card_6_identifier_map.get('newfor'),
    1 : card_6_identifier_map.get('iopp'),
}

##############################################################################
# acer card 7:

# Note the names of the identifiers. Differs slightly from the NJOY
# documentation. Consider defining thin as an array declaration instead?

card_7_identifier_map = {
    'thin01' : {
        'node_type' : 'identifier',
        'optional' : True,
        'value' : {
            # XXX: Must be number?
            'node_type' : None,
            'default_value' : None,
        },
        'valid_name_list' : ['thin01'],
    },
    'thin02' : {
        'node_type' : 'identifier',
        'optional' : True,
        'value' : {
            # XXX: Must be number?
            'node_type' : None,
            'default_value' : None,
        },
        'valid_name_list' : ['thin02'],
    },
    'thin03' : {
        'node_type' : 'identifier',
        'optional' : True,
        'value' : {
            # XXX: Must be number?
            'node_type' : None,
            'default_value' : None,
        },
        'valid_name_list' : ['thin03'],
    },
}

card_7_order_map = {
    0 : card_7_identifier_map.get('thin01'),
    1 : card_7_identifier_map.get('thin02'),
    2 : card_7_identifier_map.get('thin03'),
}

##############################################################################
# acer card 8:

card_8_identifier_map = {
    'matd' : {
        'node_type' : 'identifier',
        'optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : material_number,
        },
        'valid_name_list' : ['matd', 'material'],
    },
    'tempd' : {
        'node_type' : 'identifier',
        'optional' : True,
        'value' : {
            # XXX: Must be number?
            'node_type' : None,
            'default_value' : 300,
        },
        'valid_name_list' : ['tempd'],
    },
    'tname' : {
        'node_type' : 'identifier',
        'optional' : True,
        'value' : {
            'node_type' : 'string',
            'default_value' : 'za',
            'length' : 6,
        },
        'valid_name_list' : ['tname'],
    },
}

card_8_order_map = {
    0 : card_8_identifier_map.get('matd'),
    1 : card_8_identifier_map.get('tempd'),
    2 : card_8_identifier_map.get('tname'),
}

##############################################################################
# acer card 8a:

# XXX: Treat iza{01,02,03} as an array instead?
card_8a_identifier_map = {
    'iza01' : {
        'node_type' : 'identifier',
        'optional' : False,
        'value' : {
            # XXX: Must be an integer?
            'node_type' : None,
            'default_value' : None,
        },
        'valid_name_list' : ['iza01'],
    },
    'iza02' : {
        'node_type' : 'identifier',
        'optional' : True,
        'value' : {
            # XXX: Must be an integer?
            'node_type' : None,
            'default_value' : 0,
        },
        'valid_name_list' : ['iza02'],
    },
    'iza03' : {
        'node_type' : 'identifier',
        'optional' : True,
        'value' : {
            # XXX: Must be an integer?
            'node_type' : None,
            'default_value' : 0,
        },
        'valid_name_list' : ['iza03'],
    },
}

card_8a_order_map = {
    0 : card_8a_identifier_map.get('iza01'),
    1 : card_8a_identifier_map.get('iza02'),
    2 : card_8a_identifier_map.get('iza03'),
}

##############################################################################
# acer card 9:

card_9_identifier_map = {
    'mti' : {
        'node_type' : 'identifier',
        'optional' : False,
        'value' : {
            # XXX: Type?
            'node_type' : None,
            'default_value' : None,
        },
        'valid_name_list' : ['mti'],
    },
    'nbint' : {
        'node_type' : 'identifier',
        'optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            # Expecting a non-negative number.
            'slice_list' : [slice(0, float('inf'))],
        },
        'valid_name_list' : ['nbint'],
    },
    'mte' : {
        'node_type' : 'identifier',
        'optional' : False,
        'value' : {
            # XXX: Type?
            'node_type' : None,
            'default_value' : None,
        },
        'valid_name_list' : ['mte'],
    },
    'ielas' : {
        'node_type' : 'identifier',
        'optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : [slice(0, 2)],
        },
        'valid_name_list' : ['ielas'],
    },
    'nmix' : {
        'node_type' : 'identifier',
        'optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 1,
            # Expecting a non-negative number.
            'slice_list' : [slice(0, float('inf'))],
        },
        'valid_name_list' : ['nmix'],
    },
    'emax' : {
        'node_type' : 'identifier',
        'optional' : True,
        'value' : {
            # XXX: Must be number?
            'node_type' : None,
            'default_value' : 1000.0,
        },
        'valid_name_list' : ['emax'],
    },
    'iwt' : {
        'node_type' : 'identifier',
        'optional' : True,
        'value' : {
            'node_type' : 'integer',
            'default_value' : 1,
            'slice_list' : [slice(0, 3)],
        },
        'valid_name_list' : ['iwt'],
    },
}

card_9_order_map = {
    0 : card_9_identifier_map.get('mti'),
    1 : card_9_identifier_map.get('nbint'),
    2 : card_9_identifier_map.get('mte'),
    3 : card_9_identifier_map.get('ielas'),
    4 : card_9_identifier_map.get('nmix'),
    5 : card_9_identifier_map.get('emax'),
    6 : card_9_identifier_map.get('iwt'),
}

##############################################################################
# acer card 10:

card_10_identifier_map = {
    'matd' : {
        'node_type' : 'identifier',
        'optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : material_number,
        },
        'valid_name_list' : ['matd', 'material'],
    },
    'tempd' : {
        'node_type' : 'identifier',
        'optional' : True,
        'value' : {
            # XXX: Must be number?
            'node_type' : None,
            'default_value' : 300,
        },
        'valid_name_list' : ['tempd', 'temperature'],
    },
}

card_10_order_map = {
    0 : card_10_identifier_map.get('matd'),
    1 : card_10_identifier_map.get('tempd'),
}

##############################################################################
# acer card 11:

card_11_identifier_map = {
    'matd' : {
        'node_type' : 'identifier',
        'optional' : False,
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'slice_list' : material_number,
        },
        'valid_name_list' : ['matd', 'material'],
    },
}

card_11_order_map = {
    0 : card_11_identifier_map.get('matd'),
}
