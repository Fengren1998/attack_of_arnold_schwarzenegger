# Data Structure
class Node:
    def __init__(self, state):
        self.next = None
        self.previous = None

        self.parent = None
        self.children = []
        self.depth = 0

        self.action = None
        self.path_cost = 0
        self.state = state

class Queue:
    def __init__(self):
        self.queue = []

    #Adding elements
    def insert(self, node):
        self.queue.append(node)

    def insert_all(self, nodes):
        for node in nodes:
            self.insert(node)

    #Deleting elements
    def pop(self):
        #Checking if the queue is empty
        node = self.queue[0]
        self.queue.remove(node)
        return node

    def pop_last(self):
        #Checking if the queue is empty
        node = self.queue[-1]
        self.queue.remove(node)
        return node

    def get_last(self):
        return self.queue[-1]

    #Calculate size
    def size(self):
        return self.tail - self.head

    #Reset queue
    def resetQueue(self):
        self.tail = 0
        self.head = 0
        self.queue = []

    def ranged_list(self):
        list = self.queue
        for x in range(self.size()):
            list.append(self.queue[self.head + x])
        return list
