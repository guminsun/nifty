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

    def test_tp02_analyzer(self):
        infile = get_test_problem('tp02')
        outfile = infile + analyzer_suffix()
        return_code = run(infile, outfile, analyzer())
        self.assertEqual(return_code, 0)

    def test_tp02_emitter(self):
        infile = get_test_problem('tp02')
        outfile = infile + emitter_suffix()
        return_code = run(infile, outfile, emitter())
        self.assertEqual(return_code, 0)

    def test_tp02_lexer(self):
        infile = get_test_problem('tp02')
        outfile = infile + lexer_suffix()
        return_code = run(infile, outfile, lexer())
        self.assertEqual(return_code, 0)

    def test_tp02_organizer(self):
        infile = get_test_problem('tp02')
        outfile = infile + organizer_suffix()
        return_code = run(infile, outfile, organizer())
        self.assertEqual(return_code, 0)

    def test_tp02_parser(self):
        infile = get_test_problem('tp02')
        outfile = infile + parser_suffix()
        return_code = run(infile, outfile, parser())
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

    def test_tp04_analyzer(self):
        infile = get_test_problem('tp04')
        outfile = infile + analyzer_suffix()
        return_code = run(infile, outfile, analyzer())
        self.assertEqual(return_code, 0)

    def test_tp04_emitter(self):
        infile = get_test_problem('tp04')
        outfile = infile + emitter_suffix()
        return_code = run(infile, outfile, emitter())
        self.assertEqual(return_code, 0)

    def test_tp04_lexer(self):
        infile = get_test_problem('tp04')
        outfile = infile + lexer_suffix()
        return_code = run(infile, outfile, lexer())
        self.assertEqual(return_code, 0)

    def test_tp04_organizer(self):
        infile = get_test_problem('tp04')
        outfile = infile + organizer_suffix()
        return_code = run(infile, outfile, organizer())
        self.assertEqual(return_code, 0)

    def test_tp04_parser(self):
        infile = get_test_problem('tp04')
        outfile = infile + parser_suffix()
        return_code = run(infile, outfile, parser())
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

    def test_tp06_analyzer(self):
        infile = get_test_problem('tp06')
        outfile = infile + analyzer_suffix()
        return_code = run(infile, outfile, analyzer())
        self.assertEqual(return_code, 0)

    def test_tp06_emitter(self):
        infile = get_test_problem('tp06')
        outfile = infile + emitter_suffix()
        return_code = run(infile, outfile, emitter())
        self.assertEqual(return_code, 0)

    def test_tp06_lexer(self):
        infile = get_test_problem('tp06')
        outfile = infile + lexer_suffix()
        return_code = run(infile, outfile, lexer())
        self.assertEqual(return_code, 0)

    def test_tp06_organizer(self):
        infile = get_test_problem('tp06')
        outfile = infile + organizer_suffix()
        return_code = run(infile, outfile, organizer())
        self.assertEqual(return_code, 0)

    def test_tp06_parser(self):
        infile = get_test_problem('tp06')
        outfile = infile + parser_suffix()
        return_code = run(infile, outfile, parser())
        self.assertEqual(return_code, 0)

    def test_tp07_analyzer(self):
        infile = get_test_problem('tp07')
        outfile = infile + analyzer_suffix()
        return_code = run(infile, outfile, analyzer())
        self.assertEqual(return_code, 0)

    def test_tp07_emitter(self):
        infile = get_test_problem('tp07')
        outfile = infile + emitter_suffix()
        return_code = run(infile, outfile, emitter())
        self.assertEqual(return_code, 0)

    def test_tp07_lexer(self):
        infile = get_test_problem('tp07')
        outfile = infile + lexer_suffix()
        return_code = run(infile, outfile, lexer())
        self.assertEqual(return_code, 0)

    def test_tp07_organizer(self):
        infile = get_test_problem('tp07')
        outfile = infile + organizer_suffix()
        return_code = run(infile, outfile, organizer())
        self.assertEqual(return_code, 0)

    def test_tp07_parser(self):
        infile = get_test_problem('tp07')
        outfile = infile + parser_suffix()
        return_code = run(infile, outfile, parser())
        self.assertEqual(return_code, 0)

    def test_tp08_analyzer(self):
        infile = get_test_problem('tp08')
        outfile = infile + analyzer_suffix()
        return_code = run(infile, outfile, analyzer())
        self.assertEqual(return_code, 0)

    def test_tp08_emitter(self):
        infile = get_test_problem('tp08')
        outfile = infile + emitter_suffix()
        return_code = run(infile, outfile, emitter())
        self.assertEqual(return_code, 0)

    def test_tp08_lexer(self):
        infile = get_test_problem('tp08')
        outfile = infile + lexer_suffix()
        return_code = run(infile, outfile, lexer())
        self.assertEqual(return_code, 0)

    def test_tp08_organizer(self):
        infile = get_test_problem('tp08')
        outfile = infile + organizer_suffix()
        return_code = run(infile, outfile, organizer())
        self.assertEqual(return_code, 0)

    def test_tp08_parser(self):
        infile = get_test_problem('tp08')
        outfile = infile + parser_suffix()
        return_code = run(infile, outfile, parser())
        self.assertEqual(return_code, 0)

    def test_tp10_analyzer(self):
        infile = get_test_problem('tp10')
        outfile = infile + analyzer_suffix()
        return_code = run(infile, outfile, analyzer())
        self.assertEqual(return_code, 0)

    def test_tp10_emitter(self):
        infile = get_test_problem('tp10')
        outfile = infile + emitter_suffix()
        return_code = run(infile, outfile, emitter())
        self.assertEqual(return_code, 0)

    def test_tp10_lexer(self):
        infile = get_test_problem('tp10')
        outfile = infile + lexer_suffix()
        return_code = run(infile, outfile, lexer())
        self.assertEqual(return_code, 0)

    def test_tp10_organizer(self):
        infile = get_test_problem('tp10')
        outfile = infile + organizer_suffix()
        return_code = run(infile, outfile, organizer())
        self.assertEqual(return_code, 0)

    def test_tp10_parser(self):
        infile = get_test_problem('tp10')
        outfile = infile + parser_suffix()
        return_code = run(infile, outfile, parser())
        self.assertEqual(return_code, 0)

    def test_tp11_analyzer(self):
        infile = get_test_problem('tp11')
        outfile = infile + analyzer_suffix()
        return_code = run(infile, outfile, analyzer())
        self.assertEqual(return_code, 0)

    def test_tp11_emitter(self):
        infile = get_test_problem('tp11')
        outfile = infile + emitter_suffix()
        return_code = run(infile, outfile, emitter())
        self.assertEqual(return_code, 0)

    def test_tp11_lexer(self):
        infile = get_test_problem('tp11')
        outfile = infile + lexer_suffix()
        return_code = run(infile, outfile, lexer())
        self.assertEqual(return_code, 0)

    def test_tp11_organizer(self):
        infile = get_test_problem('tp11')
        outfile = infile + organizer_suffix()
        return_code = run(infile, outfile, organizer())
        self.assertEqual(return_code, 0)

    def test_tp11_parser(self):
        infile = get_test_problem('tp11')
        outfile = infile + parser_suffix()
        return_code = run(infile, outfile, parser())
        self.assertEqual(return_code, 0)

    def test_tp12_analyzer(self):
        infile = get_test_problem('tp12')
        outfile = infile + analyzer_suffix()
        return_code = run(infile, outfile, analyzer())
        self.assertEqual(return_code, 0)

    def test_tp12_emitter(self):
        infile = get_test_problem('tp12')
        outfile = infile + emitter_suffix()
        return_code = run(infile, outfile, emitter())
        self.assertEqual(return_code, 0)

    def test_tp12_lexer(self):
        infile = get_test_problem('tp12')
        outfile = infile + lexer_suffix()
        return_code = run(infile, outfile, lexer())
        self.assertEqual(return_code, 0)

    def test_tp12_organizer(self):
        infile = get_test_problem('tp12')
        outfile = infile + organizer_suffix()
        return_code = run(infile, outfile, organizer())
        self.assertEqual(return_code, 0)

    def test_tp12_parser(self):
        infile = get_test_problem('tp12')
        outfile = infile + parser_suffix()
        return_code = run(infile, outfile, parser())
        self.assertEqual(return_code, 0)

    def test_tp13_analyzer(self):
        infile = get_test_problem('tp13')
        outfile = infile + analyzer_suffix()
        return_code = run(infile, outfile, analyzer())
        self.assertEqual(return_code, 0)

    def test_tp13_emitter(self):
        infile = get_test_problem('tp13')
        outfile = infile + emitter_suffix()
        return_code = run(infile, outfile, emitter())
        self.assertEqual(return_code, 0)

    def test_tp13_lexer(self):
        infile = get_test_problem('tp13')
        outfile = infile + lexer_suffix()
        return_code = run(infile, outfile, lexer())
        self.assertEqual(return_code, 0)

    def test_tp13_organizer(self):
        infile = get_test_problem('tp13')
        outfile = infile + organizer_suffix()
        return_code = run(infile, outfile, organizer())
        self.assertEqual(return_code, 0)

    def test_tp13_parser(self):
        infile = get_test_problem('tp13')
        outfile = infile + parser_suffix()
        return_code = run(infile, outfile, parser())
        self.assertEqual(return_code, 0)

    def test_tp14_analyzer(self):
        infile = get_test_problem('tp14')
        outfile = infile + analyzer_suffix()
        return_code = run(infile, outfile, analyzer())
        self.assertEqual(return_code, 0)

    def test_tp14_emitter(self):
        infile = get_test_problem('tp14')
        outfile = infile + emitter_suffix()
        return_code = run(infile, outfile, emitter())
        self.assertEqual(return_code, 0)

    def test_tp14_lexer(self):
        infile = get_test_problem('tp14')
        outfile = infile + lexer_suffix()
        return_code = run(infile, outfile, lexer())
        self.assertEqual(return_code, 0)

    def test_tp14_organizer(self):
        infile = get_test_problem('tp14')
        outfile = infile + organizer_suffix()
        return_code = run(infile, outfile, organizer())
        self.assertEqual(return_code, 0)

    def test_tp14_parser(self):
        infile = get_test_problem('tp14')
        outfile = infile + parser_suffix()
        return_code = run(infile, outfile, parser())
        self.assertEqual(return_code, 0)

    def test_tp17_analyzer(self):
        infile = get_test_problem('tp17')
        outfile = infile + analyzer_suffix()
        return_code = run(infile, outfile, analyzer())
        self.assertEqual(return_code, 0)

    def test_tp17_emitter(self):
        infile = get_test_problem('tp17')
        outfile = infile + emitter_suffix()
        return_code = run(infile, outfile, emitter())
        self.assertEqual(return_code, 0)

    def test_tp17_lexer(self):
        infile = get_test_problem('tp17')
        outfile = infile + lexer_suffix()
        return_code = run(infile, outfile, lexer())
        self.assertEqual(return_code, 0)

    def test_tp17_organizer(self):
        infile = get_test_problem('tp17')
        outfile = infile + organizer_suffix()
        return_code = run(infile, outfile, organizer())
        self.assertEqual(return_code, 0)

    def test_tp17_parser(self):
        infile = get_test_problem('tp17')
        outfile = infile + parser_suffix()
        return_code = run(infile, outfile, parser())
        self.assertEqual(return_code, 0)

##############################################################################
# Helpers.

def get_test_problem(tp):
    test_problems = {
        'tp01' : 'data/test_problems/tp01.nif',
        'tp02' : 'data/test_problems/tp02.nif',
        'tp03' : 'data/test_problems/tp03.nif',
        'tp04' : 'data/test_problems/tp04.nif',
        'tp05' : 'data/test_problems/tp05.nif',
        'tp06' : 'data/test_problems/tp06.nif',
        'tp07' : 'data/test_problems/tp07.nif',
        'tp08' : 'data/test_problems/tp08.nif',
        'tp10' : 'data/test_problems/tp10.nif',
        'tp11' : 'data/test_problems/tp11.nif',
        'tp12' : 'data/test_problems/tp12.nif',
        'tp13' : 'data/test_problems/tp13.nif',
        'tp14' : 'data/test_problems/tp14.nif',
        'tp17' : 'data/test_problems/tp17.nif',
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
        # Test Problem 01:
        'test_tp01_analyzer',
        'test_tp01_emitter',
        'test_tp01_lexer',
        'test_tp01_organizer',
        'test_tp01_parser',
        # Test Problem 02:
        'test_tp02_analyzer',
        'test_tp02_emitter',
        'test_tp02_lexer',
        'test_tp02_organizer',
        'test_tp02_parser',
        # Test Problem 03:
        'test_tp03_analyzer',
        'test_tp03_emitter',
        'test_tp03_lexer',
        'test_tp03_organizer',
        'test_tp03_parser',
        # Test Problem 04:
        'test_tp04_analyzer',
        'test_tp04_emitter',
        'test_tp04_lexer',
        'test_tp04_organizer',
        'test_tp04_parser',
        # Test Problem 05:
        'test_tp05_analyzer',
        'test_tp05_emitter',
        'test_tp05_lexer',
        'test_tp05_organizer',
        'test_tp05_parser',
        # Test Problem 06:
        'test_tp06_analyzer',
        'test_tp06_emitter',
        'test_tp06_lexer',
        'test_tp06_organizer',
        'test_tp06_parser',
        # Test Problem 07:
        'test_tp07_analyzer',
        'test_tp07_emitter',
        'test_tp07_lexer',
        'test_tp07_organizer',
        'test_tp07_parser',
        # Test Problem 08:
        'test_tp08_analyzer',
        'test_tp08_emitter',
        'test_tp08_lexer',
        'test_tp08_organizer',
        'test_tp08_parser',
        # Test Problem 10:
        'test_tp10_analyzer',
        'test_tp10_emitter',
        'test_tp10_lexer',
        'test_tp10_organizer',
        'test_tp10_parser',
        # Test Problem 11:
        'test_tp11_analyzer',
        'test_tp11_emitter',
        'test_tp11_lexer',
        'test_tp11_organizer',
        'test_tp11_parser',
        # Test Problem 12:
        'test_tp12_analyzer',
        'test_tp12_emitter',
        'test_tp12_lexer',
        'test_tp12_organizer',
        'test_tp12_parser',
        # Test Problem 13:
        'test_tp13_analyzer',
        'test_tp13_emitter',
        'test_tp13_lexer',
        'test_tp13_organizer',
        'test_tp13_parser',
        # Test Problem 14:
        'test_tp14_analyzer',
        'test_tp14_emitter',
        'test_tp14_lexer',
        'test_tp14_organizer',
        'test_tp14_parser',
        # Test Problem 17:
        'test_tp17_analyzer',
        'test_tp17_emitter',
        'test_tp17_lexer',
        'test_tp17_organizer',
        'test_tp17_parser',
    ]
    return unittest.TestSuite(map(ProblemTestCase, tests))

if __name__ == '__main__':
    print 'usage: run the tests by issuing bin/test from the nifty top dir'
