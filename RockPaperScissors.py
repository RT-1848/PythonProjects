import random

def play():
    print("Welcome to the game Rock, Paper, Scissors!")
    user = input("Enter 'r' for Rock, 'p' for Paper, and 's' for Scissors: ")   #Asks user for their choice
    computer = random.choice(['r','p','s']) #Gives a random choice to the computer

    if (user == computer):      #If choices are the same, it is a tie
        print("It is a tie!")
        return
    
    if winner(user, computer):  #decide the winner
        print("You Won!, Congratulations")
        return
    else:
        print("Sorry, you lost")
        return

def winner(player, opponent):
    #If true, then the player has won
    #r > s, p > r, s > p
    if (player == 'r' and opponent == 's') or (player =='p' and opponent == 'r') or (player == 's' and opponent == 'p'):
        return True
    else:
        return False

play()
