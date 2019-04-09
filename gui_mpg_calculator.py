'''
gui_mpg_calculator.py: create a GUI mpg calculator using tkinter
By B. Zhang
4/8/2019
'''

import tkinter as tk
from tkinter import ttk

class MPGFrame(ttk.Frame):
    def __init__(self, parent):#set up the GUI
        ttk.Frame.__init__(self, parent, padding = "10px, 10px, 10px, 10px" )
        self.pack()

        #define StringVar objects for the Entry widgets
        self.milesDriven = tk.StringVar()
        self.gallonsUsed = tk.StringVar()
        self.milePerGallon = tk.StringVar()

        #layout all widgets user will see
        ttk.Label(self, text = "Miles Driven:" ).grid(column = 0, row = 0, sticky=tk.E)
        ttk.Entry(self, width = 30, textvariable = self.milesDriven).grid(column = 1, row = 0)

        ttk.Label(self, text = "Gallons of Gas Used:" ).grid(column = 0, row = 1, sticky=tk.E)
        ttk.Entry(self, width = 30, textvariable = self.gallonsUsed).grid(column = 1, row = 1)

        ttk.Label(self, text = "Miles Per Gallon: " ).grid(column = 0, row = 2, sticky=tk.E)
        ttk.Entry(self, width = 30, textvariable = self.milePerGallon, state =  "readonly").grid(column = 1, row = 2)

        ttk.Button(self, text = "Calculate", command = self.calculateMPG).grid(column = 1, row = 3)

        #add paddings to all widgets
        for child in self.winfo_children():
            child.grid_configure(padx = 5, pady = 3)

    def calculateMPG(self):
        miles = float(self.milesDriven.get())
        gallons = float(self.gallonsUsed.get())

        mpg = miles / gallons

        mpg = round(mpg, 2)

        #display the mpg
        self.milePerGallon.set(mpg)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("MPG Calculator")
    MPGFrame(root)
    root.mainloop()








