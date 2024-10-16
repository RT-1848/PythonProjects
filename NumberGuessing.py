import random

def number_guess():
  print("This is the number guessing game")

  #range of the random numbers
  Base = 0
  Highest = 100
  Guessing = random.randint(Base, Highest)
  attempts = 0
  flag = True
  while(flag == True):
    user_input = int(input('Guess the number between ' + str(Base) + ' and ' + str(Highest) + ": "))
    attempts += 1
    
    if user_input == Guessing:
        print("Nice! You got the number in " + str(attempts) + " attempts!")
        break
    elif user_input < Guessing:
        print("Too Low!, Try again!")
    else:
        print("Too High!, Try again!")
    
number_guess()
