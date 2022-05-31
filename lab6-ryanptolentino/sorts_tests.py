import unittest
from sorts import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        nums = [23, 10]
        comps = selection_sort(nums)
        self.assertEqual(comps, 1)
        self.assertEqual(nums, [10, 23])

    def test_selection_sort_from_class(self):
        nums = [10, 20, 12, 7, 18]
        comps = selection_sort(nums)
        self.assertEqual(comps, 10)
        self.assertEqual(nums, [7, 10, 12, 18, 20])

    def test_main(self):
        main()


if __name__ == '__main__': 
    unittest.main()
