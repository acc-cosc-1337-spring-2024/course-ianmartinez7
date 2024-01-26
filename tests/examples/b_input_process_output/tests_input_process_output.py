import unittest

from src.examples.b_input_proc_output.input_process_output import add_values, test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_and_numbers(self):
        self.assertEqual(add_values(3, 4), 7)
        self.assertEqual(add_values(10.99, 1.50) , 12.49)

