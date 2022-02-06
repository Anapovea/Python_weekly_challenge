# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 22:32:35 2022
@author: AnaPov
"""
#Random Password Generator
# Create a random alphanumeric string of length ten that must contain
# at least four digits. For example, the output can be anything like 
# 1o32WzUS87, 1P56X9Vh87
 
import random
import string

# print(string.ascii_lowercase)   # lower
# print(string.ascii_uppercase)   # upper
# print(string.ascii_letters)     # combination of both
# print(string.digits)            # To include digits from 1 to 10
# print(string.punctuation)

#Function
def password_function (letters_count, digits_count):
        
    letters = "".join((random.choice(string.ascii_letters) for i in range(letters_count)))
    # print(letters)
    
    digits = "".join((random.choice(string.digits) for i in range(digits_count)))
    # print(digits)
    
    sample_list = list(letters + digits)
    random.shuffle(sample_list)    
    # print(sample_list)
    
    final = ''.join(sample_list)
    print("Random string with", letters_count, "letters", "and", digits_count, "digits", "is:", final)

    return

#Calling the function
generated_password = password_function(6, 4)
print(generated_password)

# Output 3kw7qzx9b7, OKc871Zg0A 