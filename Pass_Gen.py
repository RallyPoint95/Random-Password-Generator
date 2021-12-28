#PASSWORD Generator

import string
import sys, random

def password_gen(stringLength = 8 ):
    name = input('Enter you\'re Full name: ')
    char_name1 = ''.join(random.choice(string.ascii_letters) for i in range(2))
    char_name2 = ''.join(random.choice(string.ascii_letters) for i in range(2))
    char_name = char_name1.upper() + char_name2.lower()
    int_num = ''.join(random.choice(string.digits) for i in range(3))
    spsl_char = ''.join(random.choice(string.punctuation) for i in range(2))
    password_data = char_name + int_num + spsl_char
    return ''.join(random.choice(password_data) for i in range(stringLength))
    
print(password_gen())
