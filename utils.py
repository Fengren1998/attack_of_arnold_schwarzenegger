# Data Structure
class Node:
    def __init__(self, state):
        self.next = None
        self.previous = None

        self.parent = None
        self.depth = 0

        self.action = None
        self.path_cost = 0
        self.state = state

class Fringe:
    def __init__(self):
        self.first = None
        self.last = None

    def get_first(self):
        # Get the first node
        # Make the node the last node inserted
        result = self.last

        # While the result node still has a previous node, keep getting the previous node
        while result.previous != None:
            result = result.previous

        # Then return the node
        return result

    def insert(self, node):
        if self.first or self.last == None:
            self.first = node
            self.last = node
        else:
            # Make the next node of the last node the current node
            # Then create a copy of it
            self.last.next = node
            temp = self.last

            # Make the current node the last node
            # Then make the previous node the copy of the temp
            self.last = node
            self.last.previous = temp

    def insert_all(self, nodes):
        for node in nodes:
            print('Node Action: ' + str(node.action))
            if self.first or self.last == None:
                self.first = node
                self.last = node
            else:
                # Make the next node of the last node the current node
                # Then create a copy of it
                self.last.next = node
                temp = self.last

                # Make the current node the last node
                # Then make the previous node the copy of the temp
                self.last = node
                self.last.previous = temp

    def pop(self):
        # The first node's next node will have its previous node erased
        #popped_node = self.get_first()
        popped_node = self.first
        if self.first.next != None:
            self.first = self.first.next
        else:
            self.first = None
            self.last = None
        #popped_node.next.previous = None

        # Then return the first node
        return popped_node

class Queue:
    def __init__(self):
        self.queue = []
        self.head = 0
        self.tail = 0

    #Adding elements
    def insert(self, node):
        #Checking if the queue is full
        self.queue.append(node)
        self.tail += 1

    def insert_all(self, nodes):
        for node in nodes:
            self.insert(node)

    #Deleting elements
    def pop(self):
        #Checking if the queue is empty
        if self.size() <= 0:
            self.resetQueue()
            return ("Queue Empty")
        node = self.queue[self.head]
        self.head += 1
        return node

    #Calculate size
    def size(self):
        return self.tail - self.head

    #Reset queue
    def resetQueue(self):
        self.tail = 0
        self.head = 0
        self.queue = []
