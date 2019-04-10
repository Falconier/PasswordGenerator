# Importing EVERYTHING!!!
##region Imports
import random
import math
import uuid


##endregion


# get Unique identifier without dashes
class PasswordGenerator:

    def __init__(self):
        self.__hexGUID = uuid.uuid4().hex
        # User enters password length
        ##todo: set up as entry box in gui
        self.__length = int(input("How many characters would you like? "))
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
        self.passCheck()


    ##validate password
    def passCheck(self):
        # Check the flags to validate the charecter
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
        if self.__password in self.__storePassword:
            self.__has_lowercase = False
            self.__has_uppercase = False
            self.__has_number = False
            self.__has_symbol = False
            self.__password = ""

    def display_pass(self):
        # print password and store the password in a tupple when done
        print(self.__password)
        self.__storePassword.append(self.__password)
        print("Entropy:", round(math.log(94, 2), 3) * self.__length, "bits")
