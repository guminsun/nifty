##############################################################################
# Global settings for all modules.

# Material numbers are expected to be in the range [0, 9999].
material_number = [slice(0, 10000)]

# Unit numbers are expected to be in the range [-99, -1] for binary mode, or
# [0, 99] for regular files.
unit_number = [slice(-99, 0), slice(0, 100)]

##############################################################################
# Helpers.

def is_array(order_map):
    return (expected_array_index(order_map) is not None)

def is_identifier(order_map):
    return (expected_array_index(order_map) is None)

def expected_name(order_map):
    return order_map[0]

def expected_array_index(order_map):
    return order_map[1]

def expected_identifier(order_map):
    return order_map[2]
