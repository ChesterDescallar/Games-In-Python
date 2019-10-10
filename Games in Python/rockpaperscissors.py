import random

def RockPaperScissors():
    #set player to False
    rpsLoop = 0
    playerName = ('TEST')
    while rpsLoop == 0:
        print("Rock, Paper, Scissors?")
        print ('--------------------------------------------')
        playerScore = 0
        compScore = 0
        while playerScore < 5 and compScore < 5:
            playerInput = input('Your choice: ')
            playerInput = playerInput.lower()

             #create a list of play options
            compChoices = ["Rock", "Paper", "Scissors"]
            #assign a random play to the computer
            compChoiceInput = compChoices[random.randint(0,2)]
            compChoiceInput = compChoiceInput.lower()

            print (playerInput, 'VS', compChoiceInput )
            if playerInput == compChoiceInput:
                print("Tie!")
                print ('Player[', playerScore, '] : Computer[', compScore , ']')
                print ('--------------------------------------------')
            elif playerInput == "rock" :
                if compChoiceInput == "paper":
                    print( playerName , 'Loses! Paper beats Rock')
                    compScore = compScore + 1
                    print ('Player[', playerScore, '] : Computer[', compScore , ']')
                    print ('--------------------------------------------')
                else:
                    print(playerName, 'Wins! Rock beats Scissors')
                    playerScore = playerScore + 1
                    print ('Player[', playerScore, '] : Computer[', compScore , ']')
                    print ('--------------------------------------------')
            elif playerInput == "paper":
                if compChoiceInput == "scissors":
                    print(playerName, 'Loses! Scissors beats Paper')
                    compScore = compScore + 1
                    print ('Player[', playerScore, '] : Computer[', compScore , ']')
                    print ('--------------------------------------------')
                else:
                    print(playerName, 'Wins! Paper beats Rock')
                    playerScore = playerScore + 1
                    print ('Player[', playerScore, '] : Computer[', compScore , ']')
                    print ('--------------------------------------------')
            elif playerInput == "scissors":
                if compChoiceInput == "rock":
                    print(playerName, 'Lose! Rock beats Scissors')
                    compScore = compScore + 1
                    print ('Player[', playerScore, '] : Computer[', compScore , ']')
                    print ('--------------------------------------------')
                else:
                    print(playerName , 'Wins! Scissors beats paper')
                    playerScore = playerScore + 1
                    print ('Player[', playerScore, '] : Computer[', compScore , ']')
                    print ('--------------------------------------------')
            else:
                print("It's an INVALID play! Try again.")
                print ('--------------------------------------------')

        rpsLoop = rpsLoop + 1
        print ('The game has ended!')
        if playerScore == 5:
            print (playerName, 'has WON the GAME!')
        elif compScore == 5:
            print ('The COMPUTER has WON the GAME!')

RockPaperScissors()

