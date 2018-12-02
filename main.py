from environment import State
from utils import Queue
from ai import bfs, ids, best_fs, a_star_search
from ui import AoasUI
import tkinter as tk
from tkinter import ttk


if __name__ == '__main__':
    # Initialize all important things
    problem = State()
    fringe = Queue()
    next_gen = Queue()
    depth = 3

    saved_input = None
    user_input = None

    # Manual algorithm switching
    manual = False

    # While the solution has not been found, do all of this
    solved = False
    while solved == False:
        # saved_input to automate the entire thing for long processes
        if saved_input == None and manual == False:
            saved_input = input('"1" for BFS, "2" for IDS, "3" for Greedy BFS, "4" for A* Search: ')
        elif manual == True:
            saved_input = input('"1" for BFS, "2" for IDS, "3" for Greedy BFS, "4" for A* Search: ')

        # Do the chosen input
        if saved_input == '1':
            solution, fringe, node = bfs(problem, fringe)
        elif saved_input == '2':
            solution, fringe, node, depth, next_gen = ids(problem, fringe, next_gen, depth)
        elif saved_input == '3':
            solution, fringe, node = best_fs(problem, fringe)
        elif saved_input == '4':
            solution, fringe, node = a_star_search(problem, fringe)

        # Print the returned node values that was popped from the algorithm
        print('Connor: ' + str(node.state.connor.hp))
        print('Arnold: ' + str(node.state.terminator.hp))
        print('Arnold Defense: ' + str(node.state.terminator.defense))
        print('Depth: ' + str(node.depth))
        print('Path Cost: ' + str(node.path_cost))
        print('Greed Cost: ' + str(node.greed_cost))
        print('Action: ' + str(node.action))
        print('...')

        # If the solution was found, present it and stop finding the solution
        if solution == True:
            solved = True
            print('Solution: ' + str(fringe))
