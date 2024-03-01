#
import unittest
from src.homework.h_strings.strings import get_hamming_distance, get_dna_complement
#from src.homework.h_strings.strings import get_dna_complement

class Test_Config(unittest.TestCase):

    def test_get_hamming_distance(self):
        self.assertEqual(get_hamming_distance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT"), 7)
        self.assertEqual(get_hamming_distance('CCGTGGTCCACGAAAGAT', 'ATCTGGTGAGCTGACCTA'), 12) #sanity check second test case
    
    def test_get_dna_complement(self):
        self.assertEqual(get_dna_complement('AAAACCCGGT'), 'ACCGGGTTTT')
        self.assertEqual(get_dna_complement('CTCGTCGGATGATGCATT'), 'AATGCATCATCCGACGAG') #sanity check second test case

