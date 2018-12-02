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

        self.greed_cost = None
        self.a_star_cost = None

class Queue:
    def __init__(self):
        self.queue = []

    # Adding elements
    def insert(self, node):
        self.queue.append(node)

    def insert_all(self, nodes):
        for node in nodes:
            self.insert(node)

    # Deleting and Getting elements
    def pop(self):
        # Return the first node, by removing it then returning it
        node = self.queue[0]
        self.queue.remove(node)
        return node

    def pop_last(self):
        # Return the last inserted node, by removing it then returning it
        node = self.queue[-1]
        self.queue.remove(node)
        return node

    def pop_specific(self, node):
        # Iterate through the nodes in the queue
        for node_a in self.queue:
            # If the iterated node is equal to the node in arguments, remove the iterated node and return it (pop)
            if node_a == node:
                node_target = node_a
                self.queue.remove(node_a)
                return node_target

        # Otherwise, return None
        return None

    def get_last(self):
        # Simply get the last node, not pop it
        # Made for Iterative Deepening Search
        return self.queue[-1]

    # Calculate size
    def size(self):
        # Filler function just in case, currently has no use
        # Queue.tail and Queue.head do not exist anymore
        return self.tail - self.head

    # Reset queue
    def resetQueue(self):
        # Filler function just in case, currently has no use
        # Queue.tail and Queue.head do not exist anymore
        self.tail = 0
        self.head = 0
        self.queue = []

    def ranged_list(self):
        # Filler function, what even is the point of this method
        # Just use Queue.queue
        # Why did I make this
        list = self.queue
        return list

def bubble_sort(fringe, greed=True):
    queue = fringe.queue

    # Bubble sort, from first to last
    # Check if next node is less than, if it is then swap
    for x in range(len(queue)):
        # y_range is the amount of times that the [y] for loop will iterate
        # Thus, this simulates the bubble sort
        y_range = len(queue) - x
        for y in range(y_range):
            # If the y + 1 is not equal to the end of the array, then attempt the swap
            # Why? Because it will go overboard the range of the array
            if y + 1 < y_range:
                if greed == True:
                    # If it's Greedy BFS, do the swap stuff
                    if queue[y + 1].greed_cost < queue[y].greed_cost:
                        temp = queue[y + 1]
                        queue[y + 1] = queue[y]
                        queue[y] = temp
                else:
                    # If it's A* Search, do the swap stuff
                    if queue[y + 1].a_star_cost < queue[y].a_star_cost:
                        temp = queue[y + 1]
                        queue[y + 1] = queue[y]
                        queue[y] = temp
