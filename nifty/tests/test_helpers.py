import unittest

from nifty.environment import helpers as helper

class HelperTestCase(unittest.TestCase):

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

def suite():
    tests = ['test_is_assignment']
    return unittest.TestSuite(map(HelperTestCase, tests))

if __name__ == '__main__':
    suite = suite()
    unittest.TextTestRunner(verbosity=2).run(suite)
