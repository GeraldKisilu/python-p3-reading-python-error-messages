import unittest
import runpy

class TestNameError(unittest.TestCase):
    '''
    Tests for NameError in a_name_error.py
    '''

    def test_name_error(self):
        '''
        Run a_name_error.py and check for NameError
        '''
        with self.assertRaises(NameError):
            runpy.run_path('lib/a_name_error.py')

class TestSyntaxError(unittest.TestCase):
    '''
    Tests for SyntaxError in a_syntax_error.py
    '''

    def test_syntax_error(self):
        '''
        Run a_syntax_error.py and check for SyntaxError
        '''
        with self.assertRaises(SyntaxError):
            runpy.run_path('lib/a_syntax_error.py')

class TestTypeError(unittest.TestCase):
    '''
    Tests for TypeError in a_type_error.py
    '''

    def test_type_error(self):
        '''
        Run a_type_error.py and check for TypeError
        '''
        with self.assertRaises(TypeError):
            runpy.run_path('lib/a_type_error.py')

class TestAssertionError(unittest.TestCase):
    '''
    Tests for AssertionError in an_assertion_error.py
    '''

    def test_assertion_error(self):
        '''
        Run an_assertion_error.py and check for AssertionError
        '''
        with self.assertRaises(AssertionError):
            runpy.run_path('lib/an_assertion_error.py')

if __name__ == '__main__':
    unittest.main()
