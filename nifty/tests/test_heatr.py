import os, sys
import unittest
from subprocess import call

class HeatrTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def test_heatr01_analyzer(self):
        infile = get_test_problem('heatr01')
        outfile = infile + analyzer_suffix()
        return_code = run(infile, outfile, analyzer())
        self.assertEqual(return_code, 0)

    def test_heatr01_emitter(self):
        infile = get_test_problem('heatr01')
        outfile = infile + emitter_suffix()
        return_code = run(infile, outfile, emitter())
        self.assertEqual(return_code, 0)

    def test_heatr01_lexer(self):
        infile = get_test_problem('heatr01')
        outfile = infile + lexer_suffix()
        return_code = run(infile, outfile, lexer())
        self.assertEqual(return_code, 0)

    def test_heatr01_organizer(self):
        infile = get_test_problem('heatr01')
        outfile = infile + organizer_suffix()
        return_code = run(infile, outfile, organizer())
        self.assertEqual(return_code, 0)

    def test_heatr01_parser(self):
        infile = get_test_problem('heatr01')
        outfile = infile + parser_suffix()
        return_code = run(infile, outfile, parser())
        self.assertEqual(return_code, 0)

    def test_heatr01_translator(self):
        infile = get_test_problem('heatr01')
        outfile = infile + translator_suffix()
        return_code = run(infile, outfile, translator())
        self.assertEqual(return_code, 0)

##############################################################################
# Helpers.

def get_test_problem(tp):
    test_problems = {
        'heatr01' : 'data/test_heatr/heatr01.nif',
    }
    return test_problems[tp]

def analyzer():
    return bin_dir() + 'analyzer'

def emitter():
    return bin_dir() + 'emitter'

def lexer():
    return bin_dir() + 'lexer'

def organizer():
    return bin_dir() + 'organizer'

def parser():
    return bin_dir() + 'parser'

def translator():
    return bin_dir() + 'translator'

def bin_dir():
    return 'bin/'

def analyzer_suffix():
    return '.analyzer'

def emitter_suffix():
    return '.emitter'

def lexer_suffix():
    return '.lexer'

def organizer_suffix():
    return '.organizer'

def parser_suffix():
    return '.parser'

def translator_suffix():
    return '.translator'

def run(infile, outfile, function):
    fd = open(outfile, 'w')
    return_code = call([function, infile], stdout=fd, stderr=fd)
    fd.close()
    return return_code

def suite():
    tests = [
        'test_heatr01_analyzer',
        'test_heatr01_emitter',
        'test_heatr01_lexer',
        'test_heatr01_organizer',
        'test_heatr01_parser',
        'test_heatr01_translator',
    ]
    return unittest.TestSuite(map(HeatrTestCase, tests))

if __name__ == '__main__':
    print 'usage: run the tests by issuing bin/test from the nifty top dir'
