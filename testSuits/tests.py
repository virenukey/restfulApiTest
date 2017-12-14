import unittest
from scripts import testcase2

suite = unittest.TestSuite()
suite.addTest(testcase2.Testcase1)
unittest.TextTestRunner(verbosity=2).run(suite)