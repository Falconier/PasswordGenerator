import random
import math
import uuid
hexGUID = uuid.uuid4().hex
length = int(input("How many characters would you like? "))
password = ""
has_lowercase = False
has_uppercase = False
has_number = False
has_symbol = False
rn = random.SystemRandom()
random_char = ""
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
    for char in password:
        if ascii(char) in range(97, 123):
            has_lowercase = True
        elif ascii(char) in range(65, 91):
            has_uppercase = True
        elif ascii(char) in range(48, 58):
            has_number = True
        else:
            has_symbol = True
print(password)
print("Entropy:", round(math.log(94, 2), 3) * length,"bits")
