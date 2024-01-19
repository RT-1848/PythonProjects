import random
from Words import words

#Word that the player should try to guess
word = random.choice(words)
lettersGuessed = ""

#Number of turns allowed before player loses
Failure = 7

print("\n")
for letter in word:
    print("_", end="")

#loop until too many failed attempts
while (Failure > 0):
    print("\n")
    guess = input("Enter a letter: ")   #Get guessed letter from player

    if guess in word:
        #Player guessed the letter correctly
        print(f"Nice! There is one or more {guess} in the word!")
    else:
        #Player did not guess correctly
        print(f"Incorrect. There is not a {guess} in the word. You have {Failure} turns left. ")
        Failure -= 1

    #Keep a list of all letters guessed
    lettersGuessed += guess
    wrongletter = 0

    for letter in word:
        if letter in lettersGuessed:
            print(f"{letter}", end="")
        else:
            print(f"_", end="")
            wrongletter += 1
            
    if wrongletter == 0:
        print("\n")
        print(f"Congraulations! You have won! The word was {word}")
        break
else:
    print(f"\nUnfortunately, you did not win at this time. The given word was {word}. Sorry!")
