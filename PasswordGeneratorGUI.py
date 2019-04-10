import tkinter as tk
from tkinter import ttk
from PasswordGenerator import PasswordGenerator

class PasswordGeneratorUI(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10px, 10px, 10px, 10px")
        self.pack()
        self.__pword = tk.StringVar()
        self.passLen = tk.StringVar()

        ttk.Label(self, text="Password Length:").grid(column=0, row=0, sticky=tk.E)
        ttk.Entry(self, width=30, textvariable=self.passLen).grid(column=1, row=0)

        ttk.Label(self, text="Password: ").grid(column=0, row=2, sticky=tk.E)
        ttk.Label(self, textvariable = self.__pword).grid(column=1, row=2)
        ttk.Button(self, text="Calculate", command=self.makePassword).grid(column=1, row=3)

    def makePassword(self):
        p = PasswordGenerator(int(self.passLen.get()))
        self.__pword.set(p.genPassword())
        print(self.__pword.get())

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Generate Password")
    PasswordGeneratorUI(root)
    root.mainloop()
