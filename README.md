# ITFinal
## Rock, Paper, Scissors Tutorial
### Summary
Rock, Paper, Scissors or RPS has been a long time favorite game play by everyone around the world since the early 2nd century. The game has grown from just a great way to pass the time to a way we solve who gets to do the grunt work or who gets to go first. RPS has even grown with the rise of computers and artificial intelligence gaining the psycological skills needed to play RPS making it now even more readily available to play anyone with a computer. This program is just one of example of this. In this turtorial I will show you how the game works within the Python programming language.

### The Intro
I decided to make this very definition heavy to be able to jump around the program a lot without having to find the variables I was looking for. Especially with the way things are highlighed, indented, and generally organized it just made sense to me. Below you will find the introduction to the game. Keep in mind the whole program is text based and will be outputted to the console where the user will input their decisions.

```python
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
 ```
 I decided to use the multiple if/else statements along with different ways they can input their option. This will help with error handling. Speaking of error handling, instead of running exceptions throughout the program, I used an else statement which just takes you back to the beginning of the definition. 
 
 ### Pickle
 Pickling is the art of saving and loading data or objects to a seperate file. It is built into Python as a module and it very useful in the case of saving stats of a user to a file.
 
 ```python
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
```
As you can see, the file will save with a .rps file extension helping differentiate a file in the same directory with the same name from the .rps file. This is also the first time we see the time module being used. This is to make the user feel like the computer is thinking. The computer can output all of this information almost instantly but adds a whole new level of immersiveness with the time.sleep functionality.

### The Game
The game itself is pretty self explanatory. There is an Else/If statement for each possible outcome of user to computer inputs. 

```python
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
```
As you can see at the end of the definition it saves the player state automatically and goes to the endGame definition.
### The End
The endGame definition helps us with once again keeping everything organized.
```Python 
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
```
### Questions
The full RPS.py file is located in this repository if you would like to take a look at it. If you have any questions or suggestions to my work please feel free to contact me. If you have a RPS program in a different language, please commit it. I would love to take a look at it. 
