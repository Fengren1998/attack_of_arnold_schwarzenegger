from environment import State
from utils import Queue
from ai import bfs, ids
from ui import AoasUI
import tkinter as tk
from tkinter import ttk


if __name__ == '__main__':
    problem = State()
    fringe = Queue()
    next_gen = Queue()
    depth = 3

    solved = False
    while solved == False:
        user_input = input('"1" for BFS, "2" for IDS: ')
        if user_input == '1':
            solution, fringe, node = bfs(problem, fringe)
        elif user_input == '2':
            solution, fringe, node, depth, next_gen = ids(problem, fringe, next_gen, depth)

        print('Connor: ' + str(node.state.connor.hp))
        print('Arnold: ' + str(node.state.terminator.hp))
        print('Arnold Defense: ' + str(node.state.terminator.defense))
        print('Depth: ' + str(node.depth))
        print('Path Cost: ' + str(node.path_cost))
        print('Action: ' + str(node.action))
        print('...')

        if solution == True:
            solved = True
            print('Solution: ' + str(fringe))
