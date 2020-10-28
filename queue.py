# Queue: A queue.
# Your implementation should pass the tests in test_queue.py.
# YOUR NAME

# Hint: pip3 install llist
# from llist import sllist

from llist import sllist

class Queue:

    def __init__(self):
        self.data = sllist()

    def enqueue(self, value):
        self.data.append(value)
