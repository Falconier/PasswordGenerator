<<<<<<< HEAD
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
=======
# Importing EVERYTHING!!!
##region Imports
import random
import math
import uuid


##endregion


# get Unique identifier without dashes
class PasswordGenerator():

    def __init__(self, leng):
        self.__hexGUID = uuid.uuid4().hex
        # User enters password length
        ##todo: set up as entry box in gui
        self.__length = leng
        # Password to be stored here
        self.__password = ""
        self.__storePassword = ()
        # Flags to check if password is correct or not
        ##region Flags
        self.__has_lowercase = False
        self.__has_uppercase = False
        self.__has_number = False
        self.__has_symbol = False
        ##endregion
        # create instance of SystemRandom class
        self.__rn = random.SystemRandom()
        self.__random_char = ""

    # Srtarts sorry for varification check
    ##genPassword Method
    def genPassword(self):
        while self.__has_lowercase != True and self.__has_uppercase != True and self.__has_number != True and self.__has_symbol != True:
            for x in range(self.__length):
                choice = int(self.__rn.random() * 2 + 1)
                ##todo: fix this soon
                if choice == 1:
                    self.__random_char = self.__rn.choice(self.__hexGUID)
                else:
                    choice = int(self.__rn.random() * 3 + 1)
                if choice == 1:
                    self.__random_char = chr(self.__rn.randrange(58, 97))
                elif choice == 2:
                    self.__random_char = chr(self.__rn.randrange(33, 48))
                else:
                    self.__random_char = chr(self.__rn.randrange(123, 127))
                self.__password += self.__random_char
            self.passCheck()
        return self.__password


    ##validate password
    def passCheck(self):
        # Check the flags to validate the charecter
        ##todo: fix this as well
        for char in self.__password:
            if ascii(char) in range(97, 123):
                self.__has_lowercase = True
            elif ascii(char) in range(65, 91):
                self.__has_uppercase = True
            elif ascii(char) in range(48, 58):
                self.__has_number = True
            else:
                self.__has_symbol = True
            # If password is not
        # if self.__password in self.__storePassword:
        #     self.__has_lowercase = False
        #     self.__has_uppercase = False
        #     self.__has_number = False
        #     self.__has_symbol = False
        #     self.__password = ""

    def display_pass(self):
        # print password and store the password in a tupple when done
        print(self.__password)
        self.__storePassword.append(self.__password)
        print("Entropy:", round(math.log(94, 2), 3) * self.__length, "bits")


# def main():
#     p = PasswordGenerator()
#     word = p.genPassword()
#     print(word)
#
# main()
>>>>>>> c8f7f9d5232427b3d87071c160b666e7f20cd6c2
