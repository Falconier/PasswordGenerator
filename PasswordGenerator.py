"""
PasswordGenerator.py: generates a pseudo-random password
By Isaac Patton, Ian Mense, Jacob Bullin
4/10/2019
"""
import random
import math
import uuid
from tkinter import *


class PasswordGenerator:
    def __init__(self, parent):
        self.__hexGUID = uuid.uuid4().hex
        self.__length = StringVar()
        self.__password_done = 0
        self.__password = ""
        self.__passwords_used = ()
        self.__final_pass = StringVar()
        self.__entropy = StringVar()
        self.__rn = random.SystemRandom()
        self.create_gui(parent)

    def create_gui(self, window):
        window.title("")
        window.iconbitmap("blue_key.ico")
        window.resizable(width=False, height=False)
        length_lbl = Label(window, text = "Length: ").grid(row=0, column=0, sticky=N + S + E + W)
        length_entry = Entry(window, text = self.__length).grid(row=0,column=1, sticky=N + S + E + W)
        gen_btn = Button(window, text = "Generate Password",
                         command = self.main).grid(row=1, columnspan=2, sticky=N + S + E + W)
        pass_entry = Entry(window, textvariable = self.__final_pass, state="readonly",
                           relief=FLAT).grid(row=2, columnspan=2, sticky=N + S + E + W)
        entropy_lbl = Label(window, textvariable = self.__entropy).grid(row=3, columnspan=2, sticky=N + S + E + W)
    def main(self):
        self.__password_done = 0
        while self.__password_done == 0:
            self.__password = ""
            has_lowercase = 0
            has_uppercase = 0
            has_number = 0
            has_symbol = 0
            for x in range(int(self.__length.get())):
                choice = int(self.__rn.random() * 2 + 1)
                if choice == 1:
                    random_char = self.__rn.choice(self.__hexGUID)
                else:
                    choice = int(self.__rn.random() * 3 + 1)
                    if choice == 1:
                        random_char = chr(self.__rn.randrange(58, 97))
                    elif choice == 2:
                        random_char = chr(self.__rn.randrange(33, 48))
                    else:
                        random_char = chr(self.__rn.randrange(123, 127))
                self.__password += random_char
            if self.__password not in self.__passwords_used:
                for char in self.__password.encode():
                    if char in range(97, 123):
                        has_lowercase = 1
                    elif char in range(65, 91):
                        has_uppercase = 1
                    elif char in range(48, 58):
                        has_number = 1
                    else:
                        has_symbol = 1
                if has_lowercase == 1 and has_uppercase == 1 and has_number == 1 and has_symbol == 1:
                    self.__password_done = 1
        self.__final_pass.set(self.__password)
        used_list = list(self.__passwords_used)
        used_list.append(self.__password)
        self.__passwords_used = tuple(used_list)
        self.__entropy.set("Entropy: " + str(round(math.log(94, 2), 3) * int(self.__length.get())) + " bits")


def main():
    root = Tk()
    pg = PasswordGenerator(root)
    root.mainloop()
main()