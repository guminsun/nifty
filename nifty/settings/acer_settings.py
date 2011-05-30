##############################################################################
# acer identifier settings
#
# The identifier maps are used for looking up e.g. valid identifier names in
# a card.
#
# The order maps are used for looking up the expected order of an identifier
# in a card.
#
### Identifier Maps
#
# The key is the identifier name used internally by the translator and by the
# NJOY documentation. The value associated with each key is a dictionary
# containing meta data for the identifier. Data such as valid, alternative,
# identifier names are set here.
#
# All key-value pairs in the dictionary have the form:
#
#   internal_name : {
#       'node_type' : identifier_declared_as
#   }
#
# identifier_declared_as is either defined as the string 'array', or
# 'identifier'.
#
# Each alternative identifier name must be uniquely associated to a single key
# within the card. Two different keys within the same card are not allowed to
# share an identical, alternative, identifier name. It is good practice to
# keep the internal name, e.g. the key, as the first name listed in the valid
# names list. The keys are of course  assumed to be unique within each card as
# well.
#
# The value associated to each key is a dictionary. Each value dictionary are
# assumed to have the key 'node_type', which denotes whether the identifier
# is expected to be declared as an 'array' or a regular 'identifier'.
#
# Each value dictionary also has the key 'value', which is another dictionary
# denoting the type of the value, it's default value if it has any, and more.
#
# Some identifiers have a default value as documented in the NJOY input
# instructions. 'default_value' should be set to this default value. If the
# identifier does not have a default value, i.e. must be defined, then
# 'default_value' should be None.
#
#
### Expected Order Maps
#
# Expected maps are key-value dictionaries on the form:
#
#   expected_order_index : reference to identifier in identifier map
#
# The key, expected_order_index, in the expected maps is an integer number
# which denotes the expected order of the identifier in the card's statement
# list.  A key which equals 0 indicates that the associated value is the
# identifier that is expected to appear first in the card's statement list.
# The next expected identifier in the card's statement list should be assigned
# the key 1, and so on.
#

unit_number_range = range(0, 100), range(-99, 0)

### acer card 1:

card_1_identifier_map = {
    'nendf' : {
        'node_type' : 'identifier',
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'range' : unit_number_range
        },
        'valid_name_list' : ['nendf', 'endf_input'],
    },
    'npend' : {
        'node_type' : 'identifier',
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'range' : unit_number_range
        },
        'valid_name_list' : ['npend', 'pendf_input'],
    },
    'ngend' : {
        'node_type' : 'identifier',
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'range' : unit_number_range
        },
        'valid_name_list' : ['ngend', 'multigroup_photon_input'],
    },
    'nace' : {
        'node_type' : 'identifier',
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'range' : unit_number_range
        },
        'valid_name_list' : ['nace', 'ace_output'],
    },
    'ndir' : {
        'node_type' : 'identifier',
        'value' : {
            'node_type' : 'integer',
            'default_value' : None,
            'range' : unit_number_range
        },
        'valid_name_list' : ['ndir', 'mcnp_directory_output'],
    },
}

card_1_order_map = {
    0 : card_1_identifier_map['nendf'],
    1 : card_1_identifier_map['npend'],
    2 : card_1_identifier_map['ngend'],
    3 : card_1_identifier_map['nace'],
    4 : card_1_identifier_map['ndir'],
}


### acer card 2:

card_2_identifier_map = {
    'iopt' : ['iopt'],
    'iprint' : ['iprint'],
    'ntype' : ['ntype'],
    'suff' : ['suff'],
    'nxtra' : ['nxtra'],
}

expected_card_2_map = {
    0 : ('identifier', ('iopt', None)),
    1 : ('identifier', ('iprint', 1)),
    2 : ('identifier', ('ntype', 1)),
    3 : ('identifier', ('suff', 0.00)),
    4 : ('identifier', ('nxtra', 0)),
}


### acer card 1:

card_3_identifier_map = {
    'hk' : ['hk'],
}

expected_card_3_map = {}


### acer card 1:

card_2_identifier_map = {}

expected_card_2_map = {}


### acer card 1:

card_2_identifier_map = {}

expected_card_2_map = {}


### acer card 1:

card_2_identifier_map = {}

expected_card_2_map = {}


### acer card 1:

card_2_identifier_map = {}

expected_card_2_map = {}


### acer card 1:

card_2_identifier_map = {}

expected_card_2_map = {}


### acer card 1:

card_2_identifier_map = {}

expected_card_2_map = {}


### acer card 1:

card_2_identifier_map = {}

expected_card_2_map = {}


### acer card 1:

card_2_identifier_map = {}

expected_card_2_map = {}


### acer card 1:

card_2_identifier_map = {}

expected_card_2_map = {}
