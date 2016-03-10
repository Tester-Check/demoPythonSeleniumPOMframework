import pytest
import unittest
from TestSuit.Suit2 import Uiops


set1_tests = unittest.TestLoader().loadTestsFromTestCase(Uiops)
suit1_tests = unittest.TestSuite([set1_tests])

unittest.TextTestRunner(verbosity=2).run(suit1_tests)

"""
from TestSuit import HTMLTestRunner
import os
from TestSuit.Suit2 import Uiops

# get the directory path to output report file
dir = os.getcwd()
# get all tests from SearchProductTest and HomePageTest class
set1_tests = unittest.TestLoader().loadTestsFromTestCase(Uiops)

# create a test suite combining search_test and home_page_test
smoke_tests = unittest.TestSuite([set1_tests])
# open the report file
outfile = open(dir + "\SmokeTestReport.html", "w")
# configure HTMLTestRunner options
runner = HTMLTestRunner.HTMLTestRunner(
stream=outfile,
title='Test Report',
description='Smoke Tests'
)
# run the suite using HTMLTestRunner
runner.run(smoke_tests)
"""