class Node:
    '''Node for use with doubly-linked list'''
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


class OrderedList:
    '''A doubly-linked ordered list of items, from lowest (head of list) to highest (tail of list)'''

    def __init__(self):
        '''Use ONE dummy node as described in class
           ***No other attributes***
           DO NOT have an attribute to keep track of size'''
        self.dumbass = Node(None)
        self.dumbass.next = self.dumbass
        self.dumbass.prev = self.dumbass

    def is_empty(self):
        '''Returns True if OrderedList is empty
            MUST have O(1) performance'''
        return self.dumbass.next == self.dumbass

    def add(self, item):
        '''Adds an item to OrderedList, in the proper location based on ordering of items
           from lowest (at head of list) to highest (at tail of list) and returns True.
           If the item is already in the list, do not add it again and return False.
           MUST have O(n) average-case performance.  Assume that all items added to your
           list can be compared using the < operator and can be compared for equality/inequality.
           Make no other assumptions about the items in your list'''
        try:
            head = self.dumbass.next
            while head != self.dumbass and item > head.item:
                head = head.next
            if head.item == item:
                return False
            else:
                new = Node(item)
                new.prev = head.prev
                new.next = head
                head.prev.next = new
                head.prev = new
                return True
        except TypeError:
            raise TypeError('cannot have two different types of data in the list')


    def remove(self, item):
        '''Removes the first occurrence of an item from OrderedList. If item is removed (was in the list)
           returns True.  If item was not removed (was not in the list) returns False
           MUST have O(n) average-case performance'''
        head = self.dumbass
        if self.is_empty():
            return False
        else:
            while head.next != self.dumbass:
                if head.next.item == item:
                    head.next = head.next.next
                    head.next.prev = head
                    return True
                else:
                    head = head.next
            return False

    def index(self, item):
        '''Returns index of the first occurrence of an item in OrderedList (assuming head of list is index 0).
           If item is not in list, return None
           MUST have O(n) average-case performance'''
        if self.is_empty():
            raise IndexError
        current = self.dumbass.next
        spot = 0
        while current.item != item:
            current = current.next
            spot += 1
            if current == self.dumbass:
                return None
        return spot

    def pop(self, index):
        '''Removes and returns item at index (assuming head of list is index 0).
           If index is negative or >= size of list, raises IndexError
           MUST have O(n) average-case performance'''
        if self.is_empty() or index < 0:
            raise IndexError
        head = self.dumbass.next
        spot = 0
        while head != self.dumbass and spot < index:
            head = head.next
            spot += 1
        if head == self.dumbass:
            raise IndexError
        else:
            head.next.prev = head.prev
            head.prev.next = head.next
            return head.item

    def search(self, item):
        '''Searches OrderedList for item, returns True if item is in list, False otherwise"
           To practice recursion, this method must call a RECURSIVE method that
           will search the list
           MUST have O(n) average-case performance'''
        head = self.dumbass.next
        return self.search_helper(head, item)

    def python_list(self):
        '''Return a Python list representation of OrderedList, from head to tail
           For example, list with integers 1, 2, and 3 would return [1, 2, 3]
           MUST have O(n) performance'''
        if self.is_empty():
            return []
        l = []
        head = self.dumbass.next
        while head != self.dumbass:
            l.append(head.item)
            head = head.next
        return l

    def python_list_reversed(self):
        '''Return a Python list representation of OrderedList, from tail to head, using recursion
           For example, list with integers 1, 2, and 3 would return [3, 2, 1]
           To practice recursion, this method must call a RECURSIVE method that
           will return a reversed list
           MUST have O(n) performance'''
        if self.is_empty():
            return []
        head = self.dumbass.next
        return self.rev_helper(head)

    def size(self):
        '''Returns number of items in the OrderedList
           To practice recursion, this method must call a RECURSIVE method that
           will count and return the number of items in the list
           MUST have O(n) performance'''
        head = self.dumbass.next
        return self.size_helper(head)

    def size_helper(self, node):
        if node == self.dumbass:
            return 0
        return 1 + self.size_helper(node.next)

    def search_helper(self, node, item):
        if node == self.dumbass or node.item > item:
            return False
        elif node.item == item:
            return True
        else:
            return self.search_helper(node.next, item)

    def rev_helper(self, current):
        if current.next == self.dumbass:
            return [current.item]
        return self.rev_helper(current.next) + [current.item]
