# python's built in queue module hands on
from queue import Queue, LifoQueue

# make a limited sized queue
# with the argument, 'maxsize'
q = Queue(maxsize=5)

# if the 'maxsize' argument is 0,
# the queue size is set as infinite
inf_q = Queue(0)

# and if you don't pass an integer value maxsize,
# this value automatically is set as 0
default_inf_q = Queue()

# if you try to get an element to an empty queue,
# it works but there is no error be thrown
# because this get is only worked in this condition
# with self.not_empty
# * with keyword is a syntactic sugar for try:finally
# https://stackoverflow.com/questions/1369526/what-is-the-python-keyword-with-used-for
q.get()

# put (enqueue) method is also supported
# same with the get method,
# it doesn't throw any error with the same reason
q.put(1)

# you can make a stack with this module
# with from queue import LifoQueue (Last in First out)
# internally, it inherits the queue
stack = LifoQueue()
