# can export the password to a file
# can use ascii characters in the password?

import string
import random


length = 20
chars = ""
chars += string.ascii_lowercase
chars += string.ascii_uppercase
chars += string.digits
chars += "!@£$%&*"

password = ""

for i in range(length):
    password += random.choices(chars)[0]


print(f"Your passwords is: {password}")
    
