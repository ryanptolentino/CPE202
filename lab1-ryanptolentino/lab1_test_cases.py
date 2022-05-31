import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """checks for if error is raised when list is empty"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_max_list_iter_values(self):
        """tests the max list func with actual values"""
        tlist = [1, 2, 3, 4, 5]
        self.assertEqual(max_list_iter(tlist), 5)

    def test_max_list_iter_orders(self):
        """tests the max list func with values out of order"""
        tlist = [100, 3, 2 ,1, 482, 154]
        self.assertEqual(max_list_iter(tlist), 482)

    def test_max_list_iter_multiple(self):
        """tests the max list func with multiple max values"""
        tlist = [1, 3, 5, 5, 4, 5, 2]
        self.assertEqual(max_list_iter(tlist), 5)

    def test_max_list_iter_empty(self):
        """tests the func with empty list"""
        tlist = []
        self.assertEqual(max_list_iter(tlist), None)

    def test_reverse_rec(self):
        """checks to see if the func can reverse list"""
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])

    def test_reverse_rec_error(self):
        """checks to see if the func raises value error"""
        tlist = None
        self.assertRaises(ValueError, reverse_rec, tlist)

    def test_reverse_rec_types(self):
        """checks to see if func works with different variable types"""
        tlist = [1, 6, 'hello', 6.9, 4, 'world', ['this is a list']]
        self.assertEqual(reverse_rec(tlist), [['this is a list'], 'world', 4, 6.9, 'hello', 6, 1])

    def test_reverse_rec_empty(self):
        """checks to see if func works with empty list"""
        tlist = []
        self.assertEqual(reverse_rec(tlist), [])

    def test_bin_search_mid(self):
        """tests to see if value is at mid"""
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )

    def test_bin_search_low(self):
        """tests lower bound"""
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(1, low, high, list_val), 1)

    def test_bin_search_high(self):
        """tests higher bound"""
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(9, low, high, list_val), 7)

    def test_bin_search_not_found(self):
        """tests to see if value is not found"""
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        low = 0
        high = len(list_val)-1
        self.assertIsNone(bin_search(5, low, high, list_val))

    def test_bin_search_error(self):
        """checks to see if raises value error"""
        tlist = None
        self.assertRaises(ValueError, bin_search, 69, 0, 1, tlist)  # used to check for exception

    def test_bin_search_empty(self):
        tlist = []
        self.assertEqual(bin_search(1, 0, 10, tlist), None)

    def test_reverse_mutate(self):
        """reverses test list"""
        intlist = [1, 2, 3]
        reverse_list_mutate(intlist)
        self.assertEqual(intlist, [3, 2, 1])

    def test_reverse_mutate_error(self):
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_list_mutate(tlist)

    def test_reverse_mutate_long_values(self):
        """checks to see if func works with different variable types and an overall longer list"""
        tlist = [1, 6, 'hello', 6.9, 4, 'world', ['this is a list']]
        self.assertEqual(reverse_list_mutate(tlist), None)

    def test_reverse_mutate_empty(self):
        """checks to see if func works with empty list ;-;"""
        self.assertEqual(reverse_list_mutate([]), None)

if __name__ == "__main__":
        unittest.main()

    
