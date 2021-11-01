"""
Math 560
Project 2
Fall 2021

p2queue.py

Partner 1: QiangQiang Liu
Partner 2: Zelin Jin
Date: 11/01/2021
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
        # The queue is full if the number of stored elements equals to the size of queue.
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
        # Declare a temp array of size 2 * numElems to store more elements.
        temp_arr = [None for x in range(0, 2 * self.numElems)]
        index = 0
        # Store elements in original array to the temp array.
        for i in range(self.front, len(self.queue)):
            temp_arr[index] = self.queue[i]
            index += 1
        for i in range(0, self.rear):
            temp_arr[index] = self.queue[i]
            index += 1
        # Use the temp array as new array and initialize front and rear parameter.
        self.queue = temp_arr
        self.front = 0
        self.rear = self.numElems
        return

    """
    push function to push a value into the rear of the queue.
    """

    def push(self, val):
        ##### IMPLEMENT! #####
        # If the queue is full, resize the queue.
        if self.numElems == len(self.queue):
            self.resize()
        # Add value to the end of the queue.
        self.queue[self.rear] = val
        # Check if the rear is at the end of the queue. If so, put it to the start of queue to enable circular queue.
        self.rear = (self.rear + 1) % len(self.queue)
        self.numElems += 1
        return

    """
    pop function to pop the value from the front of the queue.
    """

    def pop(self):
        ##### IMPLEMENT! #####
        if self.numElems == 0:
            return None
        # Store the target value into parameter res.
        res = self.queue[self.front]
        # Do modulus to front to enable circular queue.
        self.front = (self.front + 1) % len(self.queue)
        self.numElems -= 1
        return res
