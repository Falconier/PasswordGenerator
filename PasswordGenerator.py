# Importing EVERYTHING!!!
##region Imports
import random
import math
import uuid


##endregion
# get Unique identifier wthout dashes
class PasswordGenerator:
    def __init__(self):


        self.__hexGUID = uuid.uuid4().hex
        # User enters password length
        ##todo: set up as entry box in gui
        length = int(input("How many characters would you like? "))
        # Password to be stored here
        self.__password = ""
        self.__storePassword = []
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

        
    while has_lowercase != True and has_uppercase != True and has_number != True and has_symbol != True:
        for x in range(length):
            choice = int(rn.random() * 2 + 1)
            if choice == 1:
                random_char = rn.choice(hexGUID)
            else:
                choice = int(rn.random() * 3 + 1)
        if choice == 1:
            random_char = chr(rn.randrange(58, 97))
        elif choice == 2:
            random_char = chr(rn.randrange(33, 48))
        else:
            random_char = chr(rn.randrange(123, 127))
        password += random_char

        # Check the flags to validate the charecter
        for char in password:
            if ascii(char) in range(97, 123):
                has_lowercase = True
            elif ascii(char) in range(65, 91):
                has_uppercase = True
            elif ascii(char) in range(48, 58):
                has_number = True
            else:
                has_symbol = True

        if password in storePassword:

    # print password and store the password in a tupple when done
    print(password)
    if password == storePassword.length:
        password
    storePassword.appened(password)
    print("Entropy:", round(math.log(94, 2), 3) * length, "bits")


    def crossCheck(pword):
        for i in range(len(storePassword)):
            if (pword == storePassword[i]):
