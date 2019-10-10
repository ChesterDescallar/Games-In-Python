#-------------------------------------------------------------------------------
# Name:        Game Application
# Purpose:
#
# Author:      DES16000686
#
# Created:     11/05/2018
# Copyright:   (c) DES16000686 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python


#imports the libraries needed to do certain functions
import random, time, sys

#makes the variable global to be used in different functions
global playerName, playerInput, gamesPlayed, wholeGameLoop
#defining the global variables
playerName = ""
playerInput = ""
gamesPlayed = 0
wholeGameLoop = 0
selectedGame = " "

#main menu function which will be displayed to the user and ask for user input
def mainMenu(playerName):
    menuLoop = 0
    print ("Welcome " , playerName , "to Chester's Box 5000")
    print ( '************************************ \n'
            '* Press 1 for Higher or Lower      * \n'
            '* Press 2 for Maths Challenge      * \n'
            '* Press 3 for Word Scramble        * \n'
            '* Press 4 for Rock, Paper, Scissors* \n'
            '* Press 5 for Pontoon              * \n'
            '* Press 6 for On-Screen Help       * \n'
            '* Press 7 to Exit                  * \n'
            '************************************ ')
    while menuLoop == 0:
        menuAnswer = input ('Make your choice: ')
        if menuAnswer == "1":
            HigherOrLower() #executes the higher or lower function
        elif menuAnswer == "2":
            MathsChallenge() #executes the maths challenge function
        elif menuAnswer == "3":
            WordScramble() #executes the word scramble function
        elif menuAnswer == "4":
            RockPaperScissors() #executes the rock paper scissors function
        elif menuAnswer == "5":
            Pontoon() #executes the pontoon function
        elif menuAnswer == "6":
            onScreenHelp() #executes the on screen help function
        elif menuAnswer == "7":
            exit()
        else:
            print ('Invalid Option')
            return mainMenu(playerName)

#this is the function for onscreen help, running this function displays help to the user
def onScreenHelp():
    print ("***************** ON-SCREEN HELP ****************** \n"
           "*USE THE KEYBOARD TO INPUT ONE OF THE OPTIONS FOR HELP* \n"
           "1.) Higher or Lower Help \n"
           "2.) Maths Challenge Help \n"
           "3.) Word Scramble Help \n"
           "4.) Rock, Paper, and Scissors Help \n"
           "5.) Pontoon Help \n"
           "6.) Go back")
    print ('---------------------------------------------------------------')
    helpInput = input ("Your choice: ")
    if helpInput == "1":
        print("***** HIGHER OR LOWER HELP ***** \n"
              "1.)The program will generate a random number between 1-100. \n"
              "2.)You will have to guess using the keyboard input. \n"
              "3.)Try and guess it in the least amount of times.")
        print ('---------------------------------------------------------------')
        returnBack()

    elif helpInput == "2":
         print("***** Maths Challenge ***** \n"
              "1.)The program will generate random Maths equation for you to answer. \n"
              "2.)You will have to answer them using keyboard input. \n"
              "3.)Try and answer all of them correctly.")
         print ('---------------------------------------------------------------')
         returnBack()
    elif helpInput == "3":
         print("***** Word Scramble ***** \n"
              "1.)The program will generate random scrambled word for you to guess. \n"
              "2.)You will have to guess what the correct word would be using keyboard input. \n"
              "3.)Try and guess it in the least amount of times.")
         print ('---------------------------------------------------------------')
         returnBack()
    elif helpInput == "4":
        print("***** Rock Paper Scissors ***** \n"
              "1.)The computer will generate an option between Rock, Paper and Scissors. \n"
              "2.)You will have to input your option using the keyboard input, inputting 'rock' to choose Rock, 'paper' to choose Paper, and 'scissors' to choose scissors. \n"
              "3.)The program will compare the match-up and tell you who wins between the matchup. \n"
              "4.)First to get to 5 wins the game.")
        print ('---------------------------------------------------------------')
        returnBack()
    elif helpInput == "5":
        print("***** Pontoon ***** \n"
              "1.)The application will deal you and the computer 2 cards with the aim of trying to get the total between the two cards to 21 or as close to 21 as possible without going over it.\n"
              "2.)You can either input [1] to Hit and get a new card or input [2] to Stay with your current card \n"
              "3.)Both user and computer has to hit until their total is 15 or over. \n"
              "4.)You win by getting 21 or getting a higher score than the computer but less than 21.")
        print ('---------------------------------------------------------------')
        returnBack()
    elif helpInput == "6":
        return mainMenu(playerName)
    else:
        print ("Invalid input. Try again.")
#function that allows the user to go back
def returnBack():
    returnLoop = True
    while returnLoop == True:
        goBack = input("\n Input [B] to go back.")
        goBack = goBack.lower()
        if goBack == 'b':
            return onScreenHelp()
            returnLoop = False
        else:
            print ('Invalid input.')
            returnLoop = True

#higher or lower function which will execute the game
def HigherOrLower():
  gameScore = 0
  wholeGameLoop = 0
  print ('**********************\n'
          '*  Higher or Lower   *\n'
          '**********************')

  compNumber = random.randint(1,100) #generated a random number between 1-100
  print("I'm thinking of a number between 1 and 100, try and guess what it is")


  while wholeGameLoop == 0:
    print ('-----------------------------------------------------------------------')
    playerInput = input("Take a guess: ")
    gameScore = gameScore + 1 #adds 1 to the game score for the user to keep track how many guesses they have done
    print (playerInput)
    if playerInput.isdigit():
      playerInput = int(playerInput) # converts the user input into an integer to be compared to the random integer generated
      if playerInput == compNumber: #compares the user guess to the random integer generated
       print('Well Done! You have guessed my number!')
       print ('You guessed it in', gameScore, 'tries')
      #loop that allows the player to play the game again or send them back to the main menu
       playAgainLoop = 0
       while playAgainLoop == 0:
        print ('-----------------------------------------------------------------------')
        print ('Do you want to play again? [Y/N]')
        print ('-----------------------------------------------------------------------')
        playAgainInput = input ('[Y/N]')
        playAgainInput = playAgainInput.upper()
        if playAgainInput == 'Y':
            return HigherOrLower()
            playAgainLoop = playAgainLoop + 1
        elif playAgainInput == 'N':
            playAgainLoop = playAgainLoop + 1
            return mainMenu(playerName)
        else:
            print('Invalid Option')
            playAgainLoop = 0

      elif playerInput > compNumber:
       print('Too high')
      elif playerInput < compNumber:
       print('Too low')
      else:
        break

    else:
      print ('Invalid answer. Please input a number between 1-100')

#maths challenge function which will execute the game
def MathsChallenge():
    print ('********************** \n'
            '*   Maths Challenge  * \n'
            '**********************')
    score = 0
    for x in range(10):
        compNumber1 = random.randint(1,10) #generates two random number
        compNumber2 = random.randint(1,20) #generates two random number
        compAnswer = compNumber1 * compNumber2 #multiples the two number generated
        print ('What is',compNumber1 , 'X' , compNumber2 , '?' )
        playerInput = input ('Answer :' )
        a = 0
        #loops that checks whether the user has inputted a digit or not, if not, ask them to put a digit
        while a == 0:
            if playerInput.isdigit():
                playerInput = int(playerInput)
                if playerInput == compAnswer:
                    print ('That is correct!')
                    score = score + 1
                    a = a + 1
                else:
                    print ('That is incorrect!')
                    a = a + 1
            else:
                print ('Invalid input. The program only accepts numbers')
                playerInput = input ('Have another guess: ')

    print ('Well done! You have completed the challenge.')
    print ('You scored', score, 'out of 10')
    #loop that allows the player to play the game again or send them back to the main menu
    playAgainLoop = 0
    while playAgainLoop == 0:
       print ('-----------------------------------------------------------------------')
       print ('Do you want to play again? [Y/N]')
       print ('-----------------------------------------------------------------------')
       playAgainInput = input ('[Y/N]')
       playAgainInput = playAgainInput.upper()
       if playAgainInput == 'Y':
            return MathsChallenge() #returns to the function, allowing them play again
            playAgainLoop = playAgainLoop + 1
       elif playAgainInput == 'N':
            playAgainLoop = playAgainLoop + 1
            return mainMenu(playerName)
       else:
            print('Invalid Option')
            playAgainLoop = 0

#word scramble function which will execute the game
def WordScramble():
    print ('********************** \n'
            '*    Word Scramble   * \n'
            '**********************')
    guesses = 0
    #list that stores all the words that will be scramble and used for the player to guess
    Words = ['python', 'programming', 'brackets', 'debugging', 'exception', 'string', 'boolean', 'software', 'testing', 'bugs' ]
    correctWord = random.choice(Words)
    scramble = ''
    scramble = list(correctWord) #chooses the word from the list
    random.shuffle(scramble) #scrambles the word so that it doesn't look like the actual word
    scramble="".join(random.sample(correctWord, len(correctWord))) #scrambles the word so that it doesn't look like the actual word
    print ('The scrambled word is: ' , scramble)


    playerInput = input ('What is the word? : ')
    print ('------------------------------')
    guesses = guesses + 1
    playerInput = playerInput.lower() #converts player input to a lower case
    while playerInput != correctWord: #while loop so that if the user hasn't guess the correct word, it will just keep asking them to guess it
        print (playerInput)
        print('Your guess is incorrect!')
        print ('------------------------------')
        guesses = guesses + 1
        playerInput = input ('Have another guess : ')
    if playerInput == correctWord: #correct input means that they win the game
        print ('That is the correct word')
        print ('You have guessed it in', guesses, 'tries! Well done.')
        #loop that allows the player to play the game again or send them back to the main menu
        playAgainLoop = 0
        while playAgainLoop == 0:
            print ('-----------------------------------------------------------------------')
            print ('Do you want to play again? [Y/N]')
            print ('-----------------------------------------------------------------------')
            playAgainInput = input ('[Y/N]')
            playAgainInput = playAgainInput.upper()
            if playAgainInput == 'Y':
                return WordScramble()
                playAgainLoop = playAgainLoop + 1 #ends the loop
            elif playAgainInput == 'N':
                playAgainLoop = playAgainLoop + 1
                return mainMenu(playerName)
            else:
                print('Invalid Option')
                playAgainLoop = 0
    else:
        pass


#rock paper scissors function which will execute the game
def RockPaperScissors():
    #set loop to 0
    wholeGameLoop = 0
    while wholeGameLoop == 0:
        print ('****************************** \n'
                '*    Rock. Paper, Scissors   * \n'
                '******************************')
        playerScore = 0
        compScore = 0
        #loop that keeps the game running until someone has scored 5
        while playerScore < 5 and compScore < 5:
            playerInput = input('Your choice: ')
            playerInput = playerInput.lower()

    #create a list of play options
            compChoices = ["Rock", "Paper", "Scissors"]
            #assign a random play to the computer
            compChoiceInput = compChoices[random.randint(0,2)]#generated a random play option for the user
            compChoiceInput = compChoiceInput.lower()
            #control structures that displays different outcome on what the user and computer has generated
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
        #ends the loop
        wholeGameLoop = wholeGameLoop + 1
        print ('The game has ended!')
        if playerScore == 5:
            print (playerName, 'has WON the GAME!')
        elif compScore == 5:
            print ('The COMPUTER has WON the GAME!')
        else:
            pass
        #loop that allows the player to play the game again or send them back to the main menu
        playAgainLoop = 0
        while playAgainLoop == 0:
            print ('-----------------------------------------------------------------------')
            print ('Do you want to play again? [Y/N]')
            print ('-----------------------------------------------------------------------')
            playAgainInput = input ('[Y/N]')
            playAgainInput = playAgainInput.upper()
            if playAgainInput == 'Y':
                return RockPaperScissors()
                playAgainLoop = playAgainLoop + 1
            elif playAgainInput == 'N':
                playAgainLoop = playAgainLoop + 1
                return mainMenu(playerName)
            else:
                print('Invalid Option')
                playAgainLoop = 0

#pontoon function which will execute the game
def Pontoon():
    wholeGameLoop = 0
    print ('**********************\n'
            '*   Pontoon  or 21   *\n'
            '**********************')
    #array - lists of value that will be used for the pontoon, there are 4 10s on each deck to represent the picture card
    deckOfCards = [1,2,3,4,5,6,7,8,9,10,10,10,10,1,2,3,4,5,6,7,8,9,10,10,10,10,1,2,3,4,5,6,7,8,9,10,10,10,10,1,2,3,4,5,6,7,8,9,10,10,10,10,]
    #array this is where the user's hand and dealer's hand will be stored
    userHand = []
    dealerHand = []

    match = True
    stick = False
    cardDeal = 0
    #loop that keeps the program running until someone has won
    while match == True:
        #loop that allows the program to "deal" two cards to the user and the computer
        while cardDeal <= 1:
            userCard = random.choice(deckOfCards) #selects a random card 'value' from the array
            userHand.append(userCard) #appends the generated choice onto the user's hand
            deckOfCards.remove(userCard) #removes the card from the array deckOfCards
            dealerCard = random.choice(deckOfCards) #selects a random card 'value' from the array
            dealerHand.append(dealerCard) #appends the generated choice onto the delear's hand
            deckOfCards.remove(dealerCard) #removes the card from the array deckOfCards
            cardDeal = cardDeal + 1
        #outputs the cards to the user to see
        usersTotal = sum(userHand)
        print (playerName, '. This is your current hand: ', userHand, 'Total:(',usersTotal,')')
        print ("Opponent's hands: [",dealerHand[0],', X]')
        print ('-----------------------------------------------------------------------')
        dealersTotal = sum(dealerHand)
        #deals a new card for the computer of their total is less than 15
        dealerLoop = 0
        thirdCard = ""
        fourthCard = ""
        fifthCard = ""
        while dealerLoop == 0:
                if dealersTotal < 15:
                        dealerCard = random.choice(deckOfCards)
                        dealerHand.append(dealerCard)
                        deckOfCards.remove(dealerCard)
                        dealersTotal = sum(dealerHand)
                        thirdCard = "X"
                        if dealerLoop == 2:
                            fourthCard = "X"
                        elif dealerLoop == 3:
                            fifthCard = "X"
                        else:
                            pass
                else:
                        dealerLoop = dealerLoop + 1
        while stick == False:
            #user has to deal a card if their total is under 15
            if usersTotal < 15:
                print ('You have to:\n[1] Hit and play another card')
                playerInput = input ("User's choice: ")
                if playerInput == '1':
                    userCard = random.choice(deckOfCards)
                    userHand.append(userCard)
                    deckOfCards.remove(userCard)
                    usersTotal = sum(userHand)
                    print ('-----------------------------------------------------------------------')
                    print (playerName, "'s current hand: " ,userHand, 'Total:(',usersTotal,')')
                    print ("Opponent's hands: [",dealerHand[0], ', X ,',thirdCard,']')
                    print ('-----------------------------------------------------------------------')
                    usersTotal = sum(userHand)
                    if usersTotal == 21:
                        if usersTotal > dealersTotal:
                            print (usersTotal)
                            print (dealersTotal)
                            print ('You win the game!')
                            stick = True
                        elif usersTotal == dealersTotal:
                            print (usersTotal)
                            print (dealersTotal)
                            print ("It's a tie! But you still lose the game!")
                            stick = True
                        else:
                            pass
                    elif usersTotal > 21:
                        print (usersTotal)
                        print (dealersTotal)
                        print ("It's a bust! You lost the game.")
                        stick = True
                    else:
                        pass
                else:
                    print('Invalid input.')
            #allows the user to choose whether they want to stick or hit if the total of their cards is 15 or over
            elif usersTotal >=15:
                print ('Do you wish to:\n[1] Hit and play another card \nor \n[2] Stick with the current hand')
                playerInput = input ("User's choice: ")
                if playerInput == '1':
                    userCard = random.choice(deckOfCards)
                    userHand.append(userCard)
                    deckOfCards.remove(userCard)
                    usersTotal = sum(userHand)
                    print ('-----------------------------------------------------------------------')
                    print (playerName, "'s current hand: " ,userHand, 'Total:(',usersTotal,')')
                    print ("Opponent's hands: [",dealerHand[0], ', X ,',thirdCard, ',', fourthCard, ']')
                    print ('-----------------------------------------------------------------------')
                    usersTotal = sum(userHand)
                    if usersTotal == 21:
                        print (usersTotal)
                        print (dealersTotal)
                        print ('You win the game!')
                        stick = True
                    elif usersTotal > 21:
                        print (usersTotal)
                        print (dealersTotal)
                        print ("It's a bust! You lost the game.")
                        stick = True
                    else:
                        pass
                #allows the user to stick with their current card
                elif playerInput == '2':
                    stick = True
                    usersTotal = sum(userHand)
                    print ('-----------------------------------------------------------------------')
                    print ("User's total : ", usersTotal)
                    print ("Dealer's total : ", dealersTotal)
                    #control structures that displays different outcome on what the user and computer has generated
                    if usersTotal > dealersTotal:
                        if usersTotal <= 21:
                            print('You won! Well done,',playerName)
                        elif usersTotal > 21:
                            print ("It's a bust! You lose.")
                            stick = True
                        else:
                            pass

                    elif usersTotal < dealersTotal:
                        if dealersTotal <= 21:
                            print ('You lose! The computer got a higher total than you.')
                        elif dealersTotal > 21:
                            print ("The dealer went bust!", playerName, "You win!")
                        else:
                            pass

                    elif usersTotal == dealersTotal:
                            print ("It's a tie. But DEALER wins!")
                    else:
                        pass

                else:
                    print('Invalid input.')
        #loop that allows the player to play the game again or send them back to the main menu
        playAgainLoop = 0
        while playAgainLoop == 0:
            print ('-----------------------------------------------------------------------')
            print ('Do you want to play again? [Y/N]')
            print ('-----------------------------------------------------------------------')
            playAgainInput = input ('[Y/N]')
            playAgainInput = playAgainInput.upper()
            if playAgainInput == 'Y':
                return Pontoon()
                playAgainLoop = playAgainLoop + 1 #ends the loop
            elif playAgainInput == 'N':
                playAgainLoop = playAgainLoop + 1
                return mainMenu(playerName)
                match = False
            else:
                print('Invalid Option')
                playAgainLoop = 0





#main program
playerName = input('Enter your Username:')
if playerName == '':
        playerName = ('Player 1')
else:
    pass
print ('--------------------------------------------')
print ('Username has been set to :', playerName)
print ('--------------------------------------------')
mainMenu(playerName)
