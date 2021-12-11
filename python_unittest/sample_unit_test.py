import unittest
import sys

class SampleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        "Hook method for setting up class fixture before running tests in the class."
        cls.driver = 'test'
        cls.members = [1, 2, 3, 4]
        print('➽', sys._getframe(0).f_code.co_name)

    @classmethod
    def tearDownClass(cls):
        "Hook method for deconstructing the class fixture after running all tests in the class."
        print('➽', sys._getframe(0).f_code.co_name)

    def helper_function(self, param1):
        "helper_function"
        print('\t➪', sys._getframe(0).f_code.co_name, param1)

    def setUp(self):
        "Hook method for setting up the test fixture before exercising it."
        print('\t', sys._getframe(0).f_code.co_name)

    def tearDown(self):
        "Hook method for deconstructing the test fixture after testing it."
        print('\t', sys._getframe(0).f_code.co_name, '\n')

    def test_runs_1(self):
        print('\t➪', sys._getframe(0).f_code.co_name, self.driver)
        self.helper_function('param1 test')
        self.assertTrue(True)

    def test_runs_2(self):
        print('\t➪', sys._getframe(0).f_code.co_name, self.members)
        self.assertTrue(True)

    def test_runs_3(self):
        print('\t➪', sys._getframe(0).f_code.co_name)
        self.assertTrue(1 == 1)

if __name__ == '__main__':
    unittest.main()
