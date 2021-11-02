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
        # checck the number of elements is equal to the size
        if(self.numElems == len(self.queue)):
            return True
        return False

    """
    isEmpty function to check if the queue is empty.
    """

    def isEmpty(self):
        ##### IMPLEMENT! #####
        if(self.numElems == 0):
            return True
        return False

    """
    resize function to resize the queue by doubling its size.
    Note: we also reset the front to index 0.
    """

    def resize(self):
        ##### IMPLEMENT! #####

        temp = [None for i in range(len(self.queue)*2)]
        # move the ele in queue to temp
        for i in range(self.numElems):
            temp[i] = self.queue[self.front]
            self.front = (self.front + 1) % len(self.queue)
        self.queue = temp
        # self.numElems does not change
        return

    """
    push function to push a value into the rear of the queue.
    """

    def push(self, val):
        ##### IMPLEMENT! #####
        # firstly check if the queue is full
        if(self.isFull()):
            # resize if full
            self.resize()
        # set the last element to val
        self.queue[self.rear] = val
        # update the rear
        self.rear = (self.rear + 1) % len(self.queue)
        # update the numElements
        self.numElems += 1

        return

    """
    pop function to pop the value from the front of the queue.
    """

    def pop(self):
        ##### IMPLEMENT! #####
        # check if the queue is empty
        if(self.isEmpty()):
            return None

        # get the first element
        res = self.queue[self.front]
        # update the front pointer
        self.front = (self.front + 1) % len(self.queue)
        # update the numElement
        self.numElems -= 1

        return res
