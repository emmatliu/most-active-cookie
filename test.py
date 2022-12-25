"""
unittest -- for unit testing library
io, sys -- for capturing console output and testing it
most_active_cookie -- for testing the methods
"""
import unittest
import io
import sys
import most_active_cookie

class TestMostActiveCookie(unittest.TestCase):
    """
    Suite of test cases.
    """

    def test_parse_csv(self):
        """
        Test the parse_csv function.
        """
        self.assertEqual(most_active_cookie.parse_csv('test.csv','2018-12-09'),['AtY0laUfhglK3lC7'])
        self.assertEqual(most_active_cookie.parse_csv('test.csv','2018-12-08'),['SAZuXPGUrfbcn5UA','4sMM2LxV07bPJzwf','fbcn5UAVanZf6UtG'])
        self.assertEqual(most_active_cookie.parse_csv('test.csv','2018-12-07'),['4sMM2LxV07bPJzwf'])
        self.assertEqual(most_active_cookie.parse_csv('test.csv','2019-12-09'),[]) # Should return none if date's not there

    def test_get_args(self):
        """
        Test the argparser itself
        """
        args = most_active_cookie.get_args(['test.csv','-d','2018-12-09'])
        self.assertTrue(args.file == 'test.csv')
        self.assertTrue(args.d == '2018-12-09')
    
    def redir_output(self,test_cookies,expected_output):
        """
        Helping function for test_output

        test_cookies -- list of cookies that need to be printed
        expected_output -- desired printed string
        """
        output = io.StringIO()
        sys.stdout = output
        most_active_cookie.get_output(test_cookies)
        sys.stdout = sys.__stdout__
        self.assertTrue(output.getvalue() == expected_output)

    def test_output(self):
        """
        Testing output with redir_output helping function
        """

        n_tests = 3
        cookie_lists = [['SAZuXPGUrfbcn5UA','4sMM2LxV07bPJzwf','fbcn5UAVanZf6UtG'],['AtY0laUfhglK3lC7'],[]]
        # We add another newline to expected output as print has another newline
        output_dictionary = {
            0: 'SAZuXPGUrfbcn5UA\n4sMM2LxV07bPJzwf\nfbcn5UAVanZf6UtG\n',
            1: 'AtY0laUfhglK3lC7\n',
            2: ''
        }

        for i in range(0,n_tests):
            self.redir_output(cookie_lists[i],output_dictionary[i])


if __name__ == '__main__':
    unittest.main()
