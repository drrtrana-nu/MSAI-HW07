import unittest
from tests import test_problem1, test_letter_count, test_counts, test_bst

loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(test_problem1))
suite.addTests(loader.loadTestsFromModule(test_letter_count))
suite.addTests(loader.loadTestsFromModule(test_counts))
suite.addTests(loader.loadTestsFromModule(test_bst))

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)