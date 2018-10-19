from environment import State
from utils import Fringe, Queue
from ai import tree_search
from ui import AoasUI
import tkinter as tk
from tkinter import ttk


if __name__ == '__main__':
    #problem = State()
    #fringe = Queue()#Fringe()
    #print('Solution: ' + str(tree_search(problem, fringe)))
    root = tk.Tk()
    root.title('Attack of Arnold Scharzenegger')
    AoasUI(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
