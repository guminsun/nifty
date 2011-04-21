import os, sys
import unittest
from subprocess import call

class ProblemTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def test_tp01_analyzer(self):
        infile = get_test_problem('tp01')
        outfile = infile + analyzer_suffix()
        return_code = run(infile, outfile, analyzer())
        self.assertEqual(return_code, 0)

    def test_tp01_emitter(self):
        infile = get_test_problem('tp01')
        outfile = infile + emitter_suffix()
        return_code = run(infile, outfile, emitter())
        self.assertEqual(return_code, 0)

    def test_tp01_lexer(self):
        infile = get_test_problem('tp01')
        outfile = infile + lexer_suffix()
        return_code = run(infile, outfile, lexer())
        self.assertEqual(return_code, 0)

    def test_tp01_organizer(self):
        infile = get_test_problem('tp01')
        outfile = infile + organizer_suffix()
        return_code = run(infile, outfile, organizer())
        self.assertEqual(return_code, 0)

    def test_tp01_parser(self):
        infile = get_test_problem('tp01')
        outfile = infile + parser_suffix()
        return_code = run(infile, outfile, parser())
        self.assertEqual(return_code, 0)

    def test_tp01_translator(self):
        infile = get_test_problem('tp01')
        outfile = infile + translator_suffix()
        return_code = run(infile, outfile, translator())
        self.assertEqual(return_code, 0)

    def test_tp03_analyzer(self):
        infile = get_test_problem('tp03')
        outfile = infile + analyzer_suffix()
        return_code = run(infile, outfile, analyzer())
        self.assertEqual(return_code, 0)

    def test_tp03_emitter(self):
        infile = get_test_problem('tp03')
        outfile = infile + emitter_suffix()
        return_code = run(infile, outfile, emitter())
        self.assertEqual(return_code, 0)

    def test_tp03_lexer(self):
        infile = get_test_problem('tp03')
        outfile = infile + lexer_suffix()
        return_code = run(infile, outfile, lexer())
        self.assertEqual(return_code, 0)

    def test_tp03_organizer(self):
        infile = get_test_problem('tp03')
        outfile = infile + organizer_suffix()
        return_code = run(infile, outfile, organizer())
        self.assertEqual(return_code, 0)

    def test_tp03_parser(self):
        infile = get_test_problem('tp03')
        outfile = infile + parser_suffix()
        return_code = run(infile, outfile, parser())
        self.assertEqual(return_code, 0)

    def test_tp03_translator(self):
        infile = get_test_problem('tp03')
        outfile = infile + translator_suffix()
        return_code = run(infile, outfile, translator())
        self.assertEqual(return_code, 0)

    def test_tp05_analyzer(self):
        infile = get_test_problem('tp05')
        outfile = infile + analyzer_suffix()
        return_code = run(infile, outfile, analyzer())
        self.assertEqual(return_code, 0)

    def test_tp05_emitter(self):
        infile = get_test_problem('tp05')
        outfile = infile + emitter_suffix()
        return_code = run(infile, outfile, emitter())
        self.assertEqual(return_code, 0)

    def test_tp05_lexer(self):
        infile = get_test_problem('tp05')
        outfile = infile + lexer_suffix()
        return_code = run(infile, outfile, lexer())
        self.assertEqual(return_code, 0)

    def test_tp05_organizer(self):
        infile = get_test_problem('tp05')
        outfile = infile + organizer_suffix()
        return_code = run(infile, outfile, organizer())
        self.assertEqual(return_code, 0)

    def test_tp05_parser(self):
        infile = get_test_problem('tp05')
        outfile = infile + parser_suffix()
        return_code = run(infile, outfile, parser())
        self.assertEqual(return_code, 0)

    def test_tp05_translator(self):
        infile = get_test_problem('tp05')
        outfile = infile + translator_suffix()
        return_code = run(infile, outfile, translator())
        self.assertEqual(return_code, 0)

##############################################################################
# Helpers.

def get_test_problem(tp):
    test_problems = {
        'tp01' : 'data/test_problems/tp01.nif',
        'tp03' : 'data/test_problems/tp03.nif',
        'tp05' : 'data/test_problems/tp05.nif',
        'tp13' : 'data/test_problems/tp13.nif',
        'tp14' : 'data/test_problems/tp14.nif',
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
        'test_tp01_analyzer',
        'test_tp01_emitter',
        'test_tp01_lexer',
        'test_tp01_organizer',
        'test_tp01_parser',
        'test_tp01_translator',
        'test_tp03_analyzer',
        'test_tp03_emitter',
        'test_tp03_lexer',
        'test_tp03_organizer',
        'test_tp03_parser',
        'test_tp03_translator',
        'test_tp05_analyzer',
        'test_tp05_emitter',
        'test_tp05_lexer',
        'test_tp05_organizer',
        'test_tp05_parser',
        'test_tp05_translator',
    ]
    return unittest.TestSuite(map(ProblemTestCase, tests))

if __name__ == '__main__':
    print 'usage: run the tests by issuing bin/test from the nifty top dir'
