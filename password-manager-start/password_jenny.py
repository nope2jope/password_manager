import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def jenny():
    password = []
    password += [letters[random.randint(0, 51)] for letter in range(0,8)]
    password += [numbers[random.randint(0, 9)] for number in range (0, 5)]
    password += [symbols[random.randint(0, 8)] for symbol in range (0, 3)]

    random.shuffle(password)
    new_password = ''.join(password)
    return new_password

jenny()


