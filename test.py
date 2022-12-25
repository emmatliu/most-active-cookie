"""
unittest -- for unit testing library
most_active_cookie -- for testing the methods
"""
import unittest
import most_active_cookie

class TestMostActiveCookie(unittest.TestCase):

    def test_parse_csv(self):
        self.assertEqual(most_active_cookie.parse_csv('test1.txt','2019-12-08'),[])
    
    def test_get_args(self):
        self.assertEqual(most_active_cookie.get_args(['test1.txt','2019-12-08']),['test1.txt','2019-12-08'])

if __name__ == '__main__':
    unittest.main()
