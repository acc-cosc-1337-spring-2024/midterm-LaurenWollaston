import unittest

#I put all my tests in this file because instead of being divided up into multiple ones like the src folder, the tests were by default this one file and it's called 
#tests, which I think is implying we're just supposed to put them here even though the instructions on the blackboard said otherwise. Also, the run_tests.py in the
#root folder says not to edit it, and it's only importing this file.

from src.question_a.question_a import test_config, is_prime
from src.question_b.question_b import get_day_of_week
from src.question_c.question_c import get_random_number
from src.question_d.question_d import getFahrenheit

class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())

class isPrimeTests(unittest.TestCase):
    def testIsPrime1(self):
        self.assertEqual(False, is_prime(4))
    def testIsPrime2(self):
        self.assertEqual(True, is_prime(5))
    def testIsPrime3(self):
        self.assertEqual(True, is_prime(11))

class getDayOfWeekTests(unittest.TestCase):
    def testGetDayOfWeek1(self):
        self.assertEqual('ERROR',get_day_of_week(0))
    def testGetDayOfWeek2(self):
        self.assertEqual('MONDAY',get_day_of_week(1))
    def testGetDayOfWeek3(self):
        self.assertEqual('TUESDAY',get_day_of_week(2))
    def testGetDayOfWeek4(self):
        self.assertEqual('WEDNESDAY',get_day_of_week(3))
    def testGetDayOfWeek5(self):
        self.assertEqual('ERROR',get_day_of_week(8))

class getRandomNumberTests(unittest.TestCase):
    def testGetRandomNumber(self):
        self.assertIn(get_random_number(),range(1,6) )

class getFahrenheitTests(unittest.TestCase):
    def testGetFahrenheit1(self):
        self.assertEqual(32, int(getFahrenheit(0)))
    def testGetFahrenheit2(self):
        self.assertEqual(41, int(getFahrenheit(5)))
    def testGetFahrenheit3(self):
        self.assertEqual(50, int(getFahrenheit(10)))