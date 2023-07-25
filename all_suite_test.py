import unittest

from unittest.loader import makeSuite

from test_cases.add_a_player import TestAddAPlayer

def full_suite():
   test_suite = unittest.TestSuite()
   test_suite.addTest(makeSuite(TestAddAPlayer))
   return test_suite


if __name__ == '__main__':
   runner = unittest.TextTestRunner(verbosity=2)
   runner.run(full_suite())