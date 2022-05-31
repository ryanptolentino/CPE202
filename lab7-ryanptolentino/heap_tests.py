import unittest
from heap import *


class TestHeap(unittest.TestCase):

    def test_01_enqueue(self):
        test_heap = MaxHeap(7)
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        insert = test_heap.enqueue(10)
        self.assertTrue(insert)
        self.assertEqual(test_heap.contents(), [10, 6, 9, 2, 5, 7, 8])

    def test_02_dequeue(self):
        test_heap = MaxHeap()
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        self.assertEqual(test_heap.dequeue(), 9)
        self.assertEqual(test_heap.get_size(), 5)
        self.assertEqual(test_heap.contents(), [8, 6, 7, 2, 5])

    def test_03_heap_contents(self):
        test_heap = MaxHeap(8)
        test_heap.build_heap([1, 2, 3])
        self.assertEqual(test_heap.contents(), [3, 2, 1])

    def test_04_build_heap(self):
        test_heap = MaxHeap(10)
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        self.assertEqual(test_heap.contents(), [9, 6, 8, 2, 5, 7])

    def test_05_is_empty(self):
        test_heap = MaxHeap(5)
        self.assertTrue(test_heap.is_empty())

    def test_06_is_full(self):
        test_heap = MaxHeap(2)
        built = test_heap.build_heap([1, 2, 3, 4, 5])
        self.assertTrue(test_heap.is_full())

    def test_07_get_heap_cap(self):
        test_heap = MaxHeap(7)
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        insert = test_heap.enqueue(10)
        self.assertEqual(test_heap.get_capacity(), 7)

    def test_08_get_size(self):
        test_heap = MaxHeap()
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        self.assertEqual(test_heap.get_size(), 6)

    def test_09_perc_down(self):
        test_heap = MaxHeap()
        test_heap.build_heap([2, 9, 8, 6, 5, 7])
        test_heap.perc_down(1)
        self.assertEqual(test_heap.contents(), [9, 6, 8, 2, 5, 7])

    def test_10_perc_up(self):
        test_heap = MaxHeap()
        test_heap.build_heap([2, 9, 8, 6, 5, 7])
        test_heap.perc_up(6)
        self.assertEqual(test_heap.contents(), [9, 6, 8, 2, 5, 7])

    def test_11_heap_sort_ascending(self):
        test_heap = MaxHeap()
        list1 = [2, 9, 7, 6, 5, 8]
        test_heap.heap_sort_ascending(list1)
        self.assertEqual(list1, [2, 5, 6, 7, 8, 9])

    def test_enqueue_full(self):
        test_heap = MaxHeap(2)
        built = test_heap.build_heap([1, 2, 3, 4, 5])
        self.assertFalse(test_heap.enqueue(10))

    def test_peek_empty(self):
        test_heap = MaxHeap(2)
        built = test_heap.build_heap([1, 2, 3, 4, 5])
        self.assertFalse(test_heap.is_empty())

    def test_peek_empty(self):
        test_heap = MaxHeap(5)
        self.assertIsNone(test_heap.peek())

    def test_peek(self):
        test_heap = MaxHeap(5)
        insert = test_heap.enqueue(5)
        self.assertEqual(test_heap.peek(), 5)

    def test_dequeue_empty(self):
        test_heap = MaxHeap(5)
        self.assertIsNone(test_heap.dequeue())

    def test_contents_empty(self):
        test_heap = MaxHeap(5)
        self.assertEqual(test_heap.contents(), [])

    def test_perc_down(self):
        test_heap = MaxHeap()
        test_heap.build_heap([10, 1, 2, 3, 4, 5])
        test_heap.perc_down(1)
        self.assertEqual(test_heap.contents(), [10, 4, 5, 3, 1, 2])

    def test_is_full(self):
        test_heap = MaxHeap(2)
        test_heap.enqueue(1)
        test_heap.dequeue()
        test_heap.enqueue(2)
        self.assertFalse(test_heap.is_full())

if __name__ == "__main__":
    unittest.main()