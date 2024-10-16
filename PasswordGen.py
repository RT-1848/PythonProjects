import random
import string

def generate_pw(length):
    characters = string.ascii_letters + string.digits + string.punctuation     #Concatenates A-Z and 0-9 to characters

    PW_Gen = ''.join(random.choice(characters) for i in range(length))  #Applies a randomized character variable into the PW_Gen
    return PW_Gen

length = int(input("Enter Desired PW Length: "))            #Asks user for the length
print(generate_pw(length))                 #calls the function to create PW
