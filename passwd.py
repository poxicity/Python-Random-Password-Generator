# Importing necessary modules

import random
import string

#Ask the user how long they want the password to be.
length = int(input('\nEnter the desired length of your password (Min: 8 - Max: 94):  '))

#Define the ASCII Codes using String Module.
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digit = string.digits
punctuation = string.punctuation

#Create The Options For The Random Password
generator = lowercase + uppercase + digit + punctuation

#Use Random Module and Length Variable To Create A List
temppassword = random.sample(generator,length)

#Create the Random Password
password = "".join(temppassword)

#Print the Results
print('\n \nYour Password Is: ' )
print(password)
