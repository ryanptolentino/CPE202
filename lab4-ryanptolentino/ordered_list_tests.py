import unittest
from ordered_list import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        t_list = OrderedList()
        t_list.add(10)
        self.assertEqual(t_list.python_list(), [10])
        self.assertEqual(t_list.size(), 1)
        self.assertEqual(t_list.index(10), 0)
        self.assertTrue(t_list.search(10))
        self.assertFalse(t_list.is_empty())
        self.assertEqual(t_list.python_list_reversed(), [10])
        self.assertTrue(t_list.remove(10))
        t_list.add(10)
        self.assertEqual(t_list.pop(0), 10)

    def test_simple_again(self):
        t_list = OrderedList()
        self.assertRaises(IndexError, t_list.index, 1)
        self.assertRaises(IndexError, t_list.pop, 1)
        self.assertTrue(t_list.is_empty())
        self.assertTrue(t_list.add(1))
        t_list.add(2)
        t_list.add(3)
        t_list.add(4)  # [1, 2, 3, 4]
        self.assertFalse(t_list.add(4))
        self.assertEqual(t_list.size(), 4)
        self.assertFalse(t_list.remove(5))
        self.assertTrue(t_list.remove(4))  # [1, 2, 3]
        self.assertFalse(t_list.search(4))
        self.assertEqual(t_list.size(), 3)
        self.assertEqual(t_list.index(3), 2)
        self.assertEqual(t_list.index(2), 1)
        self.assertRaises(IndexError, t_list.pop, 5)
        self.assertEqual(t_list.pop(1), 2)  # [1, 3]
        t_list.add(2)  # [1, 2, 3]
        self.assertListEqual(t_list.python_list(), [1, 2, 3])
        self.assertListEqual(t_list.python_list_reversed(), [3, 2, 1])

    def test_simple_1(self):
        t_list = OrderedList()
        t_list.add(10)
        t_list.add(10)
        t_list.add(10)
        self.assertEqual(t_list.index(10), 0)
        self.assertEqual(t_list.size(), 1)

    def test_add_none(self):
        t_list = OrderedList()
        t_list.add(None)
        self.assertFalse(t_list.add(None))

    def test_add_nayfin(self):
        try:
            t_list = OrderedList()
            t_list.add()
        except TypeError as e:
            self.assertEqual(str(e), "add() missing 1 required positional argument: 'item'")

    def test_add_beginning(self):
        t_list = OrderedList()
        t_list.add(10)
        self.assertEqual(t_list.index(10), 0)

    def test_add_mid(self):
        t_list = OrderedList()
        t_list.add(3)
        t_list.add(7)
        t_list.add(8)
        t_list.add(4)
        self.assertEqual(t_list.index(4), 1)

    def test_add_end(self):
        t_list = OrderedList()
        t_list.add(3)
        t_list.add(5)
        t_list.add(6)
        self.assertEqual(t_list.index(6), 2)

    def test_add_2_data(self):
        try:
            t_list = OrderedList()
            t_list.add('balls')
            t_list.add(5)
        except TypeError as e:
            self.assertEqual(str(e), 'cannot have two different types of data in the list')

    def test_remove_empty(self):
        t_list = OrderedList()
        self.assertFalse(t_list.remove(3))

    def test_remove_nayfin(self):
        try:
            t_list = OrderedList()
            t_list.remove()
        except TypeError as e:
            self.assertEqual(str(e), "remove() missing 1 required positional argument: 'item'")

    def test_remove_begin(self):
        t_list = OrderedList()
        t_list.add(3)
        self.assertTrue(t_list.remove(3))
        self.assertTrue(t_list.is_empty())

    def test_index_none(self):
        t_list = OrderedList()
        t_list.add(3)
        self.assertEqual(t_list.index(None), None)

    def test_index_nayfin(self):
        try:
            t_list = OrderedList()
            t_list.add(3)
            t_list.index()
        except TypeError as e:
            self.assertEqual(str(e), "index() missing 1 required positional argument: 'item'")

    def test_python_list_empty(self):
        t_list = OrderedList()
        self.assertListEqual(t_list.python_list(), [])

    def test_python_list_rev_empty(self):
        t_list = OrderedList()
        self.assertListEqual(t_list.python_list_reversed(), [])


if __name__ == '__main__':
    unittest.main()
