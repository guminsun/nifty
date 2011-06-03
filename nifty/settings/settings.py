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
