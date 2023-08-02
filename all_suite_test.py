import unittest

from unittest.loader import makeSuite

#from test_cases.add_a_player import TestAddAPlayer
#from test_cases.clear_the_form import import TestClearForm
from test_cases.framework import TestMediumPage
from test_cases.login_into_the_system import TestLoginPage
#from test_cases.open_list_of_the_players import TestOpenListOfPlayers
#from test_cases.select_the_leg import TestChooseTheLeg
#from test_cases.sign_out import TestSignOut

def full_suite():
   test_suite = unittest.TestSuite()
   #test_suite.addTest(makeSuite(TestAddAPlayer))
   test_suite.addTest(makeSuite(TestMediumPage))
   test_suite.addTest(makeSuite(TestLoginPage))
   #test_suite.addTest(makeSuite(TestOpenListOfPlayers))
   #test_suite.addTest(makeSuite(TestChooseTheLeg))
   #test_suite.addTest(makeSuite(TestSignOut)
   return test_suite

if __name__ == '__main__':
   runner = unittest.TextTestRunner(verbosity=2)
   runner.run(full_suite())