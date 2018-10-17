from environment import State
from utils import Fringe, Queue
from ai import tree_search


if __name__ == '__main__':
    problem = State()
    fringe = Queue()#Fringe()
    print('Solution: ' + str(tree_search(problem, fringe)))
