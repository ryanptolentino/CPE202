class MaxHeap:

    def __init__(self, capacity=50):
        '''Constructor creating an empty heap with default capacity = 50 but allows heaps of other capacities to be created.'''
        self.heap = [None]*(capacity+1)
        self.size = 0

    def enqueue(self, item):
        '''inserts "item" into the heap, returns true if successful, false if there is no room in the heap
           "item" can be any primitive or ***object*** that can be compared with other 
           items using the < operator'''
        # Should call perc_up
        if self.is_full():
            return False
        self.size += 1
        self.heap[self.size] = item
        self.perc_up(self.size)
        return True

    def peek(self):
        '''returns max without changing the heap, returns None if the heap is empty'''
        if self.is_empty():
            return None
        return self.heap[1]

    def dequeue(self):
        '''returns max and removes it from the heap and restores the heap property
           returns None if the heap is empty'''
        # Should call perc_down
        if self.is_empty():
            return None
        max = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.heap[self.size] = max
        self.size -= 1
        self.perc_down(1)
        return max

    def contents(self):
        '''returns a list of contents of the heap in the order it is stored internal to the heap.
        (This may be useful for in testing your implementation.)'''
        if self.is_empty():
            return []
        return self.heap[1:self.size+1]

    def build_heap(self, alist):
        '''Discards all items in the current heap and builds a heap from 
        the items in alist using the bottom-up construction method.  
        If the capacity of the current heap is less than the number of 
        items in alist, the capacity of the heap will be increased to accommodate 
        exactly the number of items in alist'''
        # Bottom-Up construction.  Do NOT call enqueue
        i = 0
        self.size = len(alist)
        while i < len(alist):
            if i > self.get_capacity() - 1:
                self.heap.append(alist[i])
            else:
                self.heap[i + 1] = alist[i]
            i += 1
        i = self.size
        while i > 0:
            self.perc_down(i)
            i -= 1

    def is_empty(self):
        '''returns True if the heap is empty, false otherwise'''
        return self.size == 0

    def is_full(self):
        '''returns True if the heap is full, false otherwise'''
        return self.size == self.get_capacity()
        
    def get_capacity(self):
        '''this is the maximum number of a entries the heap can hold
        1 less than the number of entries that the array allocated to hold the heap can hold'''
        max = len(self.heap)
        return max - 1

    def get_size(self):
        '''the actual number of elements in the heap, not the capacity'''
        return self.size
        
    def perc_down(self, i):
        '''where the parameter i is an index in the heap and perc_down moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes.'''
        while True and 2 * i <= self.size:
            first = 2 * i
            second = first + 1
            if second <= self.size and self.heap[first] < self.heap[second]:
                if self.heap[i] < self.heap[second]:
                    self.heap[i], self.heap[second] = self.heap[second], self.heap[i]
                    i = second
                else:
                    x = 5
                    break
            else:
                if self.heap[i] < self.heap[first]:
                    self.heap[i], self.heap[first] = self.heap[first], self.heap[i]
                    i = first
                else:
                    x = 5
                    break

    def perc_up(self, i):
        '''where the parameter i is an index in the heap and perc_up moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes.'''
        while i // 2 >= 1:
            if self.heap[i] > self.heap[i // 2]:
                self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i = i // 2

    def heap_sort_ascending(self, alist):
        '''perform heap sort on input alist in ascending order
        This method will discard the current contents of the heap, build a new heap using
        the items in alist, then mutate alist to put the items in ascending order'''
        self.build_heap(alist)
        while self.size > 0:
            num = self.dequeue()
            alist[self.size] = num
