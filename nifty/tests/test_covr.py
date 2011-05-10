import os, sys
import unittest
from subprocess import call

class CovrTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def test_covr01_analyzer(self):
        infile = get_test_problem('covr01')
        outfile = infile + analyzer_suffix()
        return_code = run(infile, outfile, analyzer())
        self.assertEqual(return_code, 0)

    def test_covr01_emitter(self):
        infile = get_test_problem('covr01')
        outfile = infile + emitter_suffix()
        return_code = run(infile, outfile, emitter())
        self.assertEqual(return_code, 0)

    def test_covr01_lexer(self):
        infile = get_test_problem('covr01')
        outfile = infile + lexer_suffix()
        return_code = run(infile, outfile, lexer())
        self.assertEqual(return_code, 0)

    def test_covr01_organizer(self):
        infile = get_test_problem('covr01')
        outfile = infile + organizer_suffix()
        return_code = run(infile, outfile, organizer())
        self.assertEqual(return_code, 0)

    def test_covr01_parser(self):
        infile = get_test_problem('covr01')
        outfile = infile + parser_suffix()
        return_code = run(infile, outfile, parser())
        self.assertEqual(return_code, 0)

    def test_covr02_analyzer(self):
        infile = get_test_problem('covr02')
        outfile = infile + analyzer_suffix()
        return_code = run(infile, outfile, analyzer())
        self.assertEqual(return_code, 0)

    def test_covr02_emitter(self):
        infile = get_test_problem('covr02')
        outfile = infile + emitter_suffix()
        return_code = run(infile, outfile, emitter())
        self.assertEqual(return_code, 0)

    def test_covr02_lexer(self):
        infile = get_test_problem('covr02')
        outfile = infile + lexer_suffix()
        return_code = run(infile, outfile, lexer())
        self.assertEqual(return_code, 0)

    def test_covr02_organizer(self):
        infile = get_test_problem('covr02')
        outfile = infile + organizer_suffix()
        return_code = run(infile, outfile, organizer())
        self.assertEqual(return_code, 0)

    def test_covr02_parser(self):
        infile = get_test_problem('covr02')
        outfile = infile + parser_suffix()
        return_code = run(infile, outfile, parser())
        self.assertEqual(return_code, 0)

##############################################################################
# Helpers.

def get_test_problem(tp):
    test_problems = {
        'covr01' : 'data/test_covr/covr01.nif',
        'covr02' : 'data/test_covr/covr02.nif',
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

def run(infile, outfile, function):
    fd = open(outfile, 'w')
    return_code = call([function, infile], stdout=fd, stderr=fd)
    fd.close()
    return return_code

def suite():
    tests = [
        # 01:
        'test_covr01_analyzer',
        'test_covr01_emitter',
        'test_covr01_lexer',
        'test_covr01_organizer',
        'test_covr01_parser',
        # 02:
        'test_covr02_analyzer',
        'test_covr02_emitter',
        'test_covr02_lexer',
        'test_covr02_organizer',
        'test_covr02_parser',
    ]
    return unittest.TestSuite(map(CovrTestCase, tests))

if __name__ == '__main__':
    print 'usage: run the tests by issuing bin/test from the nifty top dir'
