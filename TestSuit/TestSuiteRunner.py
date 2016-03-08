import unittest
from TestSuit.Suit2 import Uiops


set1_tests = unittest.TestLoader().loadTestsFromTestCase(Uiops)
suit1_tests = unittest.TestSuite([set1_tests])

unittest.TextTestRunner(verbosity=2).run(suit1_tests)

