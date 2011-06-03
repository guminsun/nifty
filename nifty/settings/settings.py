##############################################################################
# Identifier and Order Maps
#
# The identifier maps are used for looking up e.g. valid identifier names in
# a card.
#
# The order maps are used for looking up the expected order of an identifier
# in a card and whether they should be defined as an array or a regular
# identifier declaration.
#
#### Identifier Maps
#
# Identifier maps are key-value dictionaries. The key is the identifier name
# used internally by the translator and by the NJOY documentation.
# The value associated with each key is a dictionary containing meta data for
# the identifier. Data such as valid, alternative, identifier names and meta
# data of the expected value are set here.
#
# All key-value pairs in the dictionary have the form:
#
#   internal_name : {
#       'internal_name' : internal_name,
#       'valid_name_list' : name_list
#       'is_optional' : boolean,
#       'value' : value_dict,
#   }
#
# * boolean is either True or False. True indicates that the identifier is
# optional. False indicates that the identifier must be defined in the card.
# * value_dict is a dictionary containing meta data which describes the
# expected value for the identifier. E.g. whether the expected value is an
# integer or a string value.
# * valid_name_list is a list of strings containing valid, alternative, names
# for the identifier.
#
# Each alternative identifier name in valid_name_list must be uniquely
# associated to a single key within the card. Two different keys within the
# same card are not allowed to share an identical, alternative, identifier
# name.
# It is good practice to keep the internal name, e.g. the key, as the first
# name listed in the valid names list. The keys are of course assumed to be
# unique within each card as well.
#
# Note the use of Python slices to define the allowed integer ranges in the
# value dictionary.
#
#### Order Maps
#
# Order maps are key-value dictionaries on the form:
#
#   expected_order_index : (internal_name, array_index, reference to identifier in identifier map)
#
# The key, expected_order_index, in the order maps is an integer number which
# denotes the expected order of the identifier in the card's statement list.
# A key which equals 0 indicates that the associated value is the identifier
# that is expected to appear first in the card's statement list.
# The next expected identifier in the card's statement list should be assigned
# the key 1, and so on.
#
# * internal_name denotes the internal identifier name as used by the
# translator.
#
# When array_index is an integer value it denotes that the identifier is
# expected to be an array declaration with the integer value as its expected
# array index.
# When array_index is set to None it denotes that the identifier is expected
# to be a regular identifier declaration which has no array index.
#
# The third element in the value tuple should be a "reference" (e.g.
# dictionary lookup, in this case) to the expected identifier in the
# identifier map.

##############################################################################
# Global settings for all modules.

# Material numbers are expected to be in the range [0, 9999].
material_number = [slice(0, 10000)]

# MT numbers (reaction types) are expected to be in the range [1, 999]
mt_number = [slice(1, 1000)]

# Unit numbers are expected to be in the range [-99, -1] for binary mode, or
# [0, 99] for coded mode.
unit_number = [slice(-99, 100)]

##############################################################################
# Helpers.

def is_array(order_tuple):
    return (expected_array_index(order_tuple) is not None)

def is_identifier(order_tuple):
    return (expected_array_index(order_tuple) is None)

def expected_name(order_tuple):
    return order_tuple[0]

def expected_array_index(order_tuple):
    return order_tuple[1]

def expected_identifier(order_tuple):
    return order_tuple[2]
