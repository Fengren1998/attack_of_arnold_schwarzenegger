from environment import State
from utils import Fringe, Queue
from ai import bfs, ids
from ui import AoasUI
import tkinter as tk
from tkinter import ttk


if __name__ == '__main__':
    problem = State()
    fringe = Queue()#Fringe()
    next_gen = Queue()
    print('Solution: ' + str(bfs(problem, fringe)))
    #print('Solution: ' + str(ids(problem, fringe, next_gen, 3)))
    #root = tk.Tk()
    #root.title('Attack of Arnold Scharzenegger')
    #AoasUI(root).pack(side="top", fill="both", expand=True)
    #root.mainloop()
