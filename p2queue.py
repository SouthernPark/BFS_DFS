"""
Math 560
Project 2
Fall 2021

p2queue.py

Partner 1:
Partner 2:
Date:
"""

"""
Queue Class
"""


class Queue:
    """
    Class attributes:
    queue    # The array for the queue.
    front    # The index of the front of the queue.
    rear     # The index ONE PAST the rear of the queue.
    numElems # The number of elements in the queue.
    """

    """
    __init__ function to initialize the Queue.
    Note: intially the size of the queue defaults to 3.
    Note: the queue is initally filled with None values.
    """

    def __init__(self, size=3):
        self.queue = [None for x in range(0, size)]
        self.front = 0
        self.rear = 0
        self.numElems = 0
        return

    """
    __repr__ function to print the stack.
    """

    def __repr__(self):
        s = '[ ' + ', '.join(map(str, self.queue)) + ' ]\n'
        s += ('Front: %d' % self.front) + '\n'
        s += ('Rear: %d' % self.rear) + '\n'
        s += ('numElems: %d' % self.numElems) + '\n'
        return s

    """
    isFull function to check if the queue is full.
    """

    def isFull(self):
        ##### IMPLEMENT! #####
        if len(self.queue) == self.numElems:
            return True
        return False

    """
    isEmpty function to check if the queue is empty.
    """

    def isEmpty(self):
        ##### IMPLEMENT! #####
        if self.numElems == 0:
            return True
        return False

    """
    resize function to resize the queue by doubling its size.
    Note: we also reset the front to index 0.
    """

    def resize(self):
        ##### IMPLEMENT! #####
        temp_arr = [None for x in range(0, 2 * self.numElems)]
        index = 0
        for i in range(self.front, len(self.queue)):
            temp_arr[index] = self.queue[i]
            index += 1
        for i in range(0, self.rear):
            temp_arr[index] = self.queue[i]
            index += 1
        self.queue = temp_arr
        self.front = 0
        self.rear = self.numElems
        return

    """
    push function to push a value into the rear of the queue.
    """

    def push(self, val):
        ##### IMPLEMENT! #####
        if self.numElems == len(self.queue):
            self.resize()
        self.queue[self.rear] = val
        self.rear = (self.rear + 1) % self.numElems
        self.numElems += 1
        return

    """
    pop function to pop the value from the front of the queue.
    """

    def pop(self):
        ##### IMPLEMENT! #####
        if self.numElems == 0:
            return None
        res = self.queue[self.front]
        self.front = (self.front + 1) % self.numElems
        self.numElems -= 1
        return res
