import os, sys
import unittest

test_dir = os.path.dirname(__file__) # ./test_helpers.py
env_top = os.path.split(test_dir)[0] # ../
sys.path.insert(0, env_top)

import helpers as helper

class TestHelperFunctions(unittest.TestCase):

    def setUp(self):
        self.l_value_node = {
            'line_number' : 5,
            'name' : 'nendf',
            'node_type' : 'identifier'
        }
        self.r_value_node = {
            'line_number' : 5,
            'node_type' : 'integer',
            'value' : 20
        }
        self.assignment_node = {
            'l_value' : self.l_value_node,
            'line_number' : 5,
            'node_type' : '=',
            'r_value' : self.r_value_node
        }

    def test_is_assignment(self):
        self.assertTrue(helper.is_assignment(self.assignment_node))

if __name__ == '__main__':
    unittest.main()