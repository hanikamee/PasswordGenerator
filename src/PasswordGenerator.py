# This program generates a random, strong, and shuffled password based on the user's desired length

import string
import random

def password_generation():

    password_length = int(input("Please enter the desired length for your password: "))

    # input validation
    while type(password_length) != int:
        password_length = int(input("Please enter the desired length for your password: "))

    # string.printable includes lowercase and uppercase letters, numbers, and printable symbols
    password_characters = list(string.printable.strip(" \t\n\r\x0b\x0c")) 
    
    # Shuffling increases the randomness and unpredictability 
    random.shuffle(password_characters)

    password = []
    for x in range(password_length):
        password.append(random.choice(password_characters))
    
    # Shuffling the password to enhance its security
    random.shuffle(password)
    
    # Using list comprehension to convert the password from list to string
    password = ''.join([str(s) for s in password])
    
    print(f'The generated password is as follows: {password}')
    
password_generation()
