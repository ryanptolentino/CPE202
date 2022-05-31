import unittest

# Use the imports below to test either your array-based stack
# or your link-based version
from stack_array import Stack
# from stack_linked import Stack


class TestLab2(unittest.TestCase):
    def test_simple(self):
        stack = Stack(5)
        stack.push(0)
        self.assertFalse(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.size(),1)

    def test_pop(self):
        stack = Stack(5)
        stack.push(3)
        stack.push(5)
        stack.push(4)
        x = stack.pop()
        self.assertEqual(stack.num_items, 2)
        self.assertEqual(x, 4)

    def test_peek(self):
        stack = Stack(5)
        stack.push(1)
        stack.push(3)
        stack.push(5)
        self.assertEqual(stack.peek(), 5)

    def test_size(self):
        stack = Stack(5)
        stack.push(1)
        stack.push(3)
        self.assertEqual(stack.size(), 2)

    def test_push_none(self):
        stack = Stack(5)
        stack.push(1)
        stack.push(None)
        self.assertIsNone(stack.peek())

    def test_size_empty(self):
        stack = Stack(5)
        self.assertEqual(stack.size(), 0)

    def test_push_full(self):
        stack = Stack(1)
        stack.push(2)
        self.assertRaises(IndexError, stack.push, 3)

    def test_pop_empty(self):
        stack = Stack(5)
        self.assertRaises(IndexError, stack.pop)

    def test_peek_empty(self):
        stack = Stack(5)
        self.assertRaises(IndexError, stack.peek)

    def test_peek_just_one(self):
        stack = Stack(5)
        stack.push(300)
        self.assertEqual(stack.peek(), 300)

    def test_full(self):
        stack = Stack(1)
        stack.push(2)
        self.assertTrue(stack.is_full)

    def test_empty(self):
        stack = Stack(10)
        self.assertTrue(stack.is_empty)

    def test_push_string(self):
        stack = Stack(5)
        stack.push(1)
        stack.push('hello')
        self.assertEqual(stack.peek(), 'hello')

    def test_push_list(self):
        stack = Stack(5)
        stack.push(3)
        stack.push([1, 2, 3])
        self.assertListEqual(stack.peek(), [1, 2, 3])

    def test_full_on_nothing(self):
        stack = Stack(0)
        self.assertFalse(stack.is_full())


if __name__ == '__main__': 
    unittest.main()
