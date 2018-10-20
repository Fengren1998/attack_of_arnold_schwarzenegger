from environment import State
from utils import Queue
from ai import tree_search
import tkinter as tk
from tkinter import ttk

class AoasUI(tk.Frame):
    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)
        self.grid(column=0, row=0)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.parent = parent

        self.test_problem = State()
        self.test_fringe = Queue()
        self.problem = State()
        self.solution = tree_search(self.test_problem, self.test_fringe)
        self.solution_stage = 0

        self.connor_hp = tk.IntVar()
        self.arnold_hp = tk.IntVar()

        self.connor_defense = tk.StringVar()
        self.arnold_defense = tk.StringVar()

        self.update()

        name_column = 1
        data_column = 2

        self.ui_label(1, name_column, 'Connor')
        self.ui_label(4, name_column, 'Arnold')
        self.ui_label(2, name_column, 'Defense')
        self.ui_label(5, name_column, 'Defense')
        self.ui_label(1, data_column, self.connor_hp, True)
        self.ui_label(4, data_column, self.arnold_hp, True)
        self.ui_label(2, data_column, self.connor_defense, True)
        self.ui_label(5, data_column, self.arnold_defense, True)

        self.ui_btn(6, data_column, 'Next', self.resolve)

    def resolve(self):
        if self.solution_stage < len(self.solution):
            print(self.solution[self.solution_stage])
            self.problem.agent_action(self.solution[self.solution_stage])
            self.update()
            self.solution_stage += 1

    def update(self):
        self.connor_hp.set(self.problem.connor.hp)
        self.arnold_hp.set(self.problem.terminator.hp)
        self.connor_defense.set(self.problem.connor.defense)
        self.arnold_defense.set(self.problem.terminator.defense)

    def ui_label(self, row, column, text, textvariable=False):
        if textvariable == False:
            tk.Label(self, text=text).grid(column=column, row=row)
        else:
            tk.Label(self, textvariable=text).grid(column=column, row=row)

    def ui_btn(self, row, column, text, command):
        tk.Button(self, text=text, command=command).grid(column=column, row=row)
