import unittest
from binary_search_tree import *

class TestLab5(unittest.TestCase):

    def test_simple(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())
        bst.insert(10, 'stuff')
        self.assertTrue(bst.search(10))
        self.assertEqual(bst.find_min(), (10, 'stuff'))
        bst.insert(10, 'other')
        self.assertEqual(bst.find_max(), (10, 'other'))
        self.assertEqual(bst.tree_height(), 0)
        self.assertEqual(bst.inorder_list(), [10])
        self.assertEqual(bst.preorder_list(), [10])
        self.assertEqual(bst.level_order_list(), [10])

    def test_deez_bst(self):
        bst = BinarySearchTree()
        # below are empty tests
        self.assertTrue(bst.is_empty())
        self.assertIsNone(bst.tree_height())
        self.assertListEqual(bst.preorder_list(), [])
        self.assertListEqual(bst.inorder_list(), [])
        self.assertListEqual(bst.level_order_list(), [])
        self.assertIsNone(bst.find_min())
        self.assertIsNone(bst.find_max())
        # tests insert
        bst.insert(10, 'I')
        self.assertEqual(bst.tree_height(), 0)
        bst.insert(9, 'Want')
        self.assertEqual(bst.tree_height(), 1)
        bst.insert(3, 'To')
        self.assertEqual(bst.find_min(), (3, 'To'))
        self.assertEqual(bst.tree_height(), 2)
        bst.insert(15, 'Drop')
        bst.insert(30, 'Out')
        bst.insert(13, 'Of')
        bst.insert(2, 'School')
        self.assertFalse(bst.is_empty())
        self.assertEqual(bst.find_min(), (2, 'School'))
        self.assertEqual(bst.find_max(), (30, 'Out'))
        self.assertEqual(bst.tree_height(), 3)
        # below checks for all  values in the tree
        self.assertTrue(bst.search(10))
        self.assertTrue(bst.search(9))
        self.assertTrue(bst.search(3))
        self.assertTrue(bst.search(15))
        self.assertTrue(bst.search(30))
        self.assertTrue(bst.search(13))
        self.assertTrue(bst.search(2))
        self.assertFalse(bst.search(1))  # this checks a random number that doesn't exist returns False
        # below checks the order shtuff
        self.assertListEqual(bst.preorder_list(), [10, 9, 3, 2, 15, 13, 30])
        self.assertListEqual(bst.inorder_list(), [2, 3, 9, 10, 13, 15, 30])
        self.assertListEqual(bst.level_order_list(), [10, 9, 15, 3, 13, 30, 2])

        node = TreeNode(10, 'lmao')
        self.assertIsNotNone(node)
        self.assertIsNone(node.left)
        self.assertIsNone(node.right)

if __name__ == '__main__': 
    unittest.main()
