import unittest
from queue_array import Queue
# from queue_linked import Queue

class TestLab1(unittest.TestCase):
    def test_queue(self):
        '''Trivial test to ensure method names and parameters are correct'''
        q = Queue(5)
        self.assertTrue(q.is_empty())
        self.assertFalse(q.is_full())
        q.enqueue('thing1')
        q.enqueue('thing2')
        q.enqueue('thing3')
        q.enqueue('thing4')
        q.enqueue('thing5')
        self.assertEqual(q.size(), 5)  # tests to see if size of queue is 3
        x = q.dequeue()
        self.assertEqual(x, 'thing1')  # tests to see if it goes in order
        x = q.dequeue()
        self.assertEqual(x, 'thing2')
        x = q.dequeue()
        self.assertEqual(x, 'thing3')
        x = q.dequeue()
        self.assertEqual(x, 'thing4')
        x = q.dequeue()
        self.assertEqual(x, 'thing5')

    def test_enqueue_index(self):
        q = Queue(1)
        q.enqueue(2)
        self.assertRaises(IndexError, q.enqueue, 'I will raise an IndexError lmao')

    def test_dequeue_empty(self):
        q = Queue(5)
        self.assertRaises(IndexError, q.dequeue)

    def test_size(self):
        q = Queue(5)
        q.enqueue('thing1')
        q.enqueue('thing2')
        q.enqueue('thing3')
        q.dequeue()
        self.assertEqual(q.size(), 2)

    def test_enqueue_none(self):
        q = Queue(5)
        q.enqueue(None)
        x = q.dequeue()
        self.assertIsNone(x)

    def test_queue_2(self):
        '''TEST "ROTATION" thingy '''
        q = Queue(5)
        self.assertTrue(q.is_empty())
        self.assertFalse(q.is_full())
        q.enqueue('thing1')
        q.enqueue('thing2')
        q.enqueue('thing3')
        q.enqueue('thing4')
        q.enqueue('thing5')
        self.assertTrue(q.is_full())
        self.assertFalse(q.is_empty())
        x = q.dequeue()
        self.assertEqual(x, 'thing1')
        x = q.dequeue()
        self.assertEqual(x, 'thing2')
        q.enqueue('final thing')
        x = q.dequeue()
        self.assertEqual(x, 'thing3')
        x = q.dequeue()
        self.assertEqual(x, 'thing4')
        x = q.dequeue()
        self.assertEqual(x, 'thing5')
        x = q.dequeue()
        self.assertEqual(x, 'final thing')

    def test_enqueue_error(self):
        q = Queue(1)
        q.enqueue(25)
        self.assertRaises(IndexError, q.enqueue, 2)

    def test_dequeue_error(self):
        q = Queue(1)
        self.assertRaises(IndexError, q.dequeue)


if __name__ == '__main__': 
    unittest.main()
