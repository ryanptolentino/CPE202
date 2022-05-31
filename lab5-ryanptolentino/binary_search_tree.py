from queue_array import Queue

class TreeNode:
    def __init__(self, key, data, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right

class BinarySearchTree:

    def __init__(self): 
        # Returns empty BST
        self.root = None

    def is_empty(self): 
        # returns True if tree is empty, else False
        return self.root is None

    def search(self, key): 
        # returns True if key is in a node of the tree, else False
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        if not self.is_empty():
            node = self.root
            return self.search_helper(key, node)

    def insert(self, key, data=None):
        # inserts new node w/ key and data
        # If an item with the given key is already in the BST, 
        # the data in the tree will be replaced with the new data
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        if self.is_empty():  # if it is empty this is the root
            self.root = TreeNode(key, data)
        else:
            current = self.root
            return self.insert_helper(key, data, current)

    def find_min(self):
        # returns a tuple with min key and data in the BST
        # returns None if the tree is empty
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        if self.is_empty():
            return None
        node = self.root
        return self.min_helper(node)

    def find_max(self): 
        # returns a tuple with max key and data in the BST
        # returns None if the tree is empty
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        if self.is_empty():
            return None
        node = self.root
        return self.max_helper(node)

    def tree_height(self): # return the height of the tree
        # returns None if tree is empty
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        if self.is_empty():
            return None
        node = self.root
        return self.height_helper(node) - 1

    def inorder_list(self):
        # return Python list of BST keys representing in-order traversal of BST
        # DON'T use a default list parameter
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        r = []
        node = self.root
        self.in_order_helper(node, r)
        return r

    def preorder_list(self):  
        # return Python list of BST keys representing pre-order traversal of BST
        # DON'T use a default list parameter
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        node = self.root
        r = []
        self.pre_helper(node, r)
        return r
        
    def level_order_list(self):  # return Python list of BST keys representing level-order traversal of BST
        # You MUST use your queue_array data structure from lab 3 to implement this method
        # DON'T attempt to use recursion
        q = Queue(25000)  # Don't change this!
        if self.is_empty():
            return []
        q.enqueue(self.root)
        r = []
        while not q.is_empty():
            node = q.dequeue()
            r.append(node.key)
            if node.left is not None:
                q.enqueue(node.left)
            if node.right is not None:
                q.enqueue(node.right)
        return r

#  everything passed this be helper functions :P

    def search_helper(self, key, node):
        if node.key == key:  # base case where it does exist in tree
            return True
        elif key < node.key and node.left is not None:
            return self.search_helper(key, node.left)
        elif key > node.key and node.right is not None:
            return self.search_helper(key, node.right)
        return False

    def insert_helper(self, key, data, node):
        if key < node.key and node.left is None:  # adds to left side of the tree
            node.left = TreeNode(key, data)
        elif key < node.key and node.left is not None:  # moves on to next node
            self.insert_helper(key, data, node.left)
        elif key > node.key and node.right is None:  # adds to right side of tree
            node.right = TreeNode(key, data)
        elif key > node.key and node.right is not None:  # moves on to next node of right node
            self.insert_helper(key, data, node.right)
        elif key == node.key:  # updates data
            node.data = data
        return node

    def min_helper(self, node):
        if node.left is None:
            return node.key, node.data
        return self.min_helper(node.left)

    def max_helper(self, node):
        if node.right is None:
            return node.key, node.data
        return self.max_helper(node.right)

    def height_helper(self, node):
        if node is None:
            return 0
        l = self.height_helper(node.left)
        r = self.height_helper(node.right)
        if l > r:
            return l + 1
        return r + 1

    def in_order_helper(self, node, r):
        if node is not None:
            self.in_order_helper(node.left, r)
            r.append(node.key)
            self.in_order_helper(node.right, r)

    def pre_helper(self, node, r):
        if node is not None:
            r.append(node.key)
            self.pre_helper(node.left, r)
            self.pre_helper(node.right, r)
