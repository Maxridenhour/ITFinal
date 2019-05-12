import random
import sys
import pickle
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.games = 0
    def display(self, name):
        print("Name:",self.name,"\nWins:",self.wins,"\nLosses:",self.losses,"\nTies:",self.ties,
              "\nTotal Games:",self.games)

def main():
    print ("Welcome to Rock, Paper, Scissors")
    print ("1. New Game")
    print ("2. Load Game")
    print ("3. Quit")
    option = input("--> ").upper()
    if option == "1" or option == "S" or option == "START":
        player()
    elif option == "2" or option == "L" or option == "LOAD":
        loadPlayer()
    elif option == "3" or option == "Q" or option == "QUIT":
        print("Goodbye!")
        time.sleep(2)
        sys.exit()
    else:
        main()


def computer_result():
    computer_play = random.randint(1, 3)
    if computer_play == 'R':
        print('I Played Rock')
    elif computer_play == 'S':
        print('I Played Scissors')
    elif computer_play == 'P':
        print('I Played Paper')

        
def player():
    option = input("What is your name? ")
    global PlayerIG
    PlayerIG = Player(option)
    print("Oh nice! That's a cool name %s!" % PlayerIG.name)
    time.sleep(2)
    print ("Let's Play!")
    gamePlay()

    
def loadPlayer():
    user_name = input("What is your name?")
    rps = ('.rps')
    file = user_name + rps
    save_file = open(file, "rb")
    contents = pickle.load(save_file)
    for self in contents: 
        print(self, '=>', contents[self])
    global PlayerIG
    PlayerIG = Player(user_name)
    save_file.close()
    print("Welcome Back,", PlayerIG.name)
    time.sleep(2)
    return gamePlay()


def savePlayer():
    user = PlayerIG.name
    rps = ('.rps')
    file = user + rps
    
    db =  {}
    db["Name"] = PlayerIG.name
    db["Wins"] = PlayerIG.wins
    db["Losses"] = PlayerIG.losses
    db["Ties"] = PlayerIG.ties
    db["Game Totals"] = PlayerIG.games

    save_file = open(file, 'wb')
    pickle.dump(db, save_file)
    save_file.close()


def statPlayer():
    user_name = PlayerIG.name
    rps = ('.rps')
    file = user_name + rps
    save_file = open(file, "rb")
    contents = pickle.load(save_file)
    for self in contents: 
        print(self, '=>', contents[self]) 
    save_file.close()
    time.sleep(2)
    return endGame()


def endGame():
    print ("What would you like to do?")
    print ("1. Play Again")
    print ("2. Statistics")
    print ("3. Quit")
    option = input("--> ").upper()
    if option == "1" or option == "P" or option == "PLAY GAME":
        gamePlay()
    elif option == "2" or option == "S" or option == "STATS" or option == "STATISTICS":
        statPlayer()
    elif option == "3" or option == "Q" or option == "QUIT":
        print("Goodbye!")
        time.sleep(2)
        sys.exit()
    else:
        endGame()


def gamePlay():
    rerun = True
    while rerun:

    #Computer Plays
    
        computer_play = random.randint(1, 3)
        if computer_play == 1:
            computer_play = 'R'
        elif computer_play == 2:
            computer_play = 'S'
        elif computer_play == 3:
            computer_play = 'P'
        time.sleep(1)

    #User Plays
    
        user_play = int(input("Type '1' to Play Rock, Type '2' to Play Scissors, Type '3' to Play Paper: "))
        if user_play == 1:
            user_play = 'R'
            time.sleep(0.4)
            print('I See You Played Rock')
        elif user_play == 2:
            user_play = 'S'
            time.sleep(0.4)
            print('I See You Played Scissors')
        elif user_play == 3:
            user_play = 'P'
            time.sleep(0.4)
            print('I See You Played Paper')
        else:
            print("Please type a number")
            gamePlay()

    #Stalemate

        if (user_play == 'R' and computer_play == 'R') or (user_play == 'P' and computer_play == 'P') \
            or (user_play == 'S' and computer_play == 'S'):
            time.sleep(1.2)
            computer_result()
            PlayerIG.ties += 1
            PlayerIG.games += 1
            time.sleep(1.2)
            print('Stalemate...We Both Chose The Same Thing.')

    # User Wins
    
        if user_play == 'R' and computer_play == 'S':
            time.sleep(1.2)
            computer_result() 
            PlayerIG.wins += 1
            PlayerIG.games += 1
            time.sleep(1.2)
            print('You Win. But I Do No Accept Defeat.')
        if user_play == 'P' and computer_play == 'R':
            time.sleep(1.2)
            computer_result()
            PlayerIG.wins += 1
            PlayerIG.games += 1
            time.sleep(1.2)
            print('You Win. But I Do No Accept Defeat.')
        if user_play == 'S' and computer_play == 'P':
            time.sleep(1.2)
            computer_result()
            PlayerIG.wins += 1
            PlayerIG.games += 1
            time.sleep(1.2)
            print('You Win. But I Do No Accept Defeat.')

    # Computer Wins
    
        if computer_play == 'R' and user_play == 'S':
            time.sleep(1.2)
            computer_result()
            PlayerIG.losses += 1
            PlayerIG.games += 1
            time.sleep(1.2)
            print('I Win. And Will Be Taking Your Status as The Superior Being.')
        if computer_play == 'P' and user_play == 'R':
            time.sleep(1.2)
            computer_result()
            PlayerIG.losses += 1
            PlayerIG.games += 1
            time.sleep(1.2)
            print('I Win. And Will Be Taking Your Status as The Superior Being.')
        if computer_play == 'S' and user_play == 'P':
            time.sleep(1.2)
            computer_result()
            PlayerIG.losses += 1
            PlayerIG.games += 1
            time.sleep(1.2)
            print('I Win. And Will Be Taking Your Status as The Superior Being.')

        time.sleep(1.2)
        savePlayer()
        endGame()


main()

        
