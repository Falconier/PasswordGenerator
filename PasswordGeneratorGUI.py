import tkinter as tk
from tkinter import ttk

class PasswordGeneratorUI:
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10px, 10px, 10px, 10px")
        self.pack()

        self.passLen = tk.StringVar()

        ttk.Label(self, text="Password Length:").grid(column=0, row=0, sticky=tk.E)
        ttk.Entry(self, width=30, textvariable=self.passLen).grid(column=1, row=0)

        ttk.Label(self, text="Password: ").grid(column=0, row=2, sticky=tk.E)

        ttk.Button(self, text="Calculate", command=self.makePassword).grid(column=1, row=3)

    def makePassword(self):
        # password =
        # return
        pass