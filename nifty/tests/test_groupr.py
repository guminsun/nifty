import os, sys
import unittest
from subprocess import call

class GrouprTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def test_groupr01_analyzer(self):
        infile = get_test_problem('groupr01')
        outfile = infile + analyzer_suffix()
        return_code = run(infile, outfile, analyzer())
        self.assertEqual(return_code, 0)

    def test_groupr01_emitter(self):
        infile = get_test_problem('groupr01')
        outfile = infile + emitter_suffix()
        return_code = run(infile, outfile, emitter())
        self.assertEqual(return_code, 0)

    def test_groupr01_lexer(self):
        infile = get_test_problem('groupr01')
        outfile = infile + lexer_suffix()
        return_code = run(infile, outfile, lexer())
        self.assertEqual(return_code, 0)

    def test_groupr01_organizer(self):
        infile = get_test_problem('groupr01')
        outfile = infile + organizer_suffix()
        return_code = run(infile, outfile, organizer())
        self.assertEqual(return_code, 0)

    def test_groupr01_parser(self):
        infile = get_test_problem('groupr01')
        outfile = infile + parser_suffix()
        return_code = run(infile, outfile, parser())
        self.assertEqual(return_code, 0)

    def test_groupr02_analyzer(self):
        infile = get_test_problem('groupr02')
        outfile = infile + analyzer_suffix()
        return_code = run(infile, outfile, analyzer())
        self.assertEqual(return_code, 0)

    def test_groupr02_emitter(self):
        infile = get_test_problem('groupr02')
        outfile = infile + emitter_suffix()
        return_code = run(infile, outfile, emitter())
        self.assertEqual(return_code, 0)

    def test_groupr02_lexer(self):
        infile = get_test_problem('groupr02')
        outfile = infile + lexer_suffix()
        return_code = run(infile, outfile, lexer())
        self.assertEqual(return_code, 0)

    def test_groupr02_organizer(self):
        infile = get_test_problem('groupr02')
        outfile = infile + organizer_suffix()
        return_code = run(infile, outfile, organizer())
        self.assertEqual(return_code, 0)

    def test_groupr02_parser(self):
        infile = get_test_problem('groupr02')
        outfile = infile + parser_suffix()
        return_code = run(infile, outfile, parser())
        self.assertEqual(return_code, 0)

    def test_groupr03_analyzer(self):
        infile = get_test_problem('groupr03')
        outfile = infile + analyzer_suffix()
        return_code = run(infile, outfile, analyzer())
        self.assertEqual(return_code, 0)

    def test_groupr03_emitter(self):
        infile = get_test_problem('groupr03')
        outfile = infile + emitter_suffix()
        return_code = run(infile, outfile, emitter())
        self.assertEqual(return_code, 0)

    def test_groupr03_lexer(self):
        infile = get_test_problem('groupr03')
        outfile = infile + lexer_suffix()
        return_code = run(infile, outfile, lexer())
        self.assertEqual(return_code, 0)

    def test_groupr03_organizer(self):
        infile = get_test_problem('groupr03')
        outfile = infile + organizer_suffix()
        return_code = run(infile, outfile, organizer())
        self.assertEqual(return_code, 0)

    def test_groupr03_parser(self):
        infile = get_test_problem('groupr03')
        outfile = infile + parser_suffix()
        return_code = run(infile, outfile, parser())
        self.assertEqual(return_code, 0)

    def test_groupr04_analyzer(self):
        infile = get_test_problem('groupr04')
        outfile = infile + analyzer_suffix()
        return_code = run(infile, outfile, analyzer())
        self.assertEqual(return_code, 0)

    def test_groupr04_emitter(self):
        infile = get_test_problem('groupr04')
        outfile = infile + emitter_suffix()
        return_code = run(infile, outfile, emitter())
        self.assertEqual(return_code, 0)

    def test_groupr04_lexer(self):
        infile = get_test_problem('groupr04')
        outfile = infile + lexer_suffix()
        return_code = run(infile, outfile, lexer())
        self.assertEqual(return_code, 0)

    def test_groupr04_organizer(self):
        infile = get_test_problem('groupr04')
        outfile = infile + organizer_suffix()
        return_code = run(infile, outfile, organizer())
        self.assertEqual(return_code, 0)

    def test_groupr04_parser(self):
        infile = get_test_problem('groupr04')
        outfile = infile + parser_suffix()
        return_code = run(infile, outfile, parser())
        self.assertEqual(return_code, 0)

    def test_groupr05_analyzer(self):
        infile = get_test_problem('groupr05')
        outfile = infile + analyzer_suffix()
        return_code = run(infile, outfile, analyzer())
        self.assertEqual(return_code, 0)

    def test_groupr05_emitter(self):
        infile = get_test_problem('groupr05')
        outfile = infile + emitter_suffix()
        return_code = run(infile, outfile, emitter())
        self.assertEqual(return_code, 0)

    def test_groupr05_lexer(self):
        infile = get_test_problem('groupr05')
        outfile = infile + lexer_suffix()
        return_code = run(infile, outfile, lexer())
        self.assertEqual(return_code, 0)

    def test_groupr05_organizer(self):
        infile = get_test_problem('groupr05')
        outfile = infile + organizer_suffix()
        return_code = run(infile, outfile, organizer())
        self.assertEqual(return_code, 0)

    def test_groupr05_parser(self):
        infile = get_test_problem('groupr05')
        outfile = infile + parser_suffix()
        return_code = run(infile, outfile, parser())
        self.assertEqual(return_code, 0)

##############################################################################
# Helpers.

def get_test_problem(tp):
    test_problems = {
        'groupr01' : 'data/test_groupr/groupr01.nif',
        'groupr02' : 'data/test_groupr/groupr02.nif',
        'groupr03' : 'data/test_groupr/groupr03.nif',
        'groupr04' : 'data/test_groupr/groupr04.nif',
        'groupr05' : 'data/test_groupr/groupr05.nif',
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
        # 1:
        'test_groupr01_analyzer',
        'test_groupr01_emitter',
        'test_groupr01_lexer',
        'test_groupr01_organizer',
        'test_groupr01_parser',
        # 2:
        'test_groupr02_analyzer',
        'test_groupr02_emitter',
        'test_groupr02_lexer',
        'test_groupr02_organizer',
        'test_groupr02_parser',
        # 3:
        'test_groupr03_analyzer',
        'test_groupr03_emitter',
        'test_groupr03_lexer',
        'test_groupr03_organizer',
        'test_groupr03_parser',
        # 4:
        'test_groupr04_analyzer',
        'test_groupr04_emitter',
        'test_groupr04_lexer',
        'test_groupr04_organizer',
        'test_groupr04_parser',
        # 5:
        'test_groupr05_analyzer',
        'test_groupr05_emitter',
        'test_groupr05_lexer',
        'test_groupr05_organizer',
        'test_groupr05_parser',
    ]
    return unittest.TestSuite(map(GrouprTestCase, tests))

if __name__ == '__main__':
    print 'usage: run the tests by issuing bin/test from the nifty top dir'
