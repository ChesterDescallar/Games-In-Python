#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DES16000686
#
# Created:     10/05/2018
# Copyright:   (c) DES16000686 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import random


def HigherOrLower():
  gameScore = 0
  gameLoop = True
  print ('Higher or Lower')
  print ('-------------------------')
  compNumber = random.randint(1,100)
  print("I'm thinking of a number between 1 and 100, try and guess what it is")


  while gameLoop == True:
    print ('-----------------------------------------------------------------------')
    playerInput = input("Take a guess: ")
    gameScore = gameScore + 1
    print (playerInput)
    if playerInput.isdigit():
      playerInput = int(playerInput)
      if playerInput == compNumber:
       print('Well Done! You have guessed my number!')
       print ('You guessed it in', gameScore, 'tries')
       gameLoop = False
      elif playerInput > compNumber:
       print('Too high')
      elif playerInput < compNumber:
       print('Too low')
      else:
        break

    else:
      print ('Invalid answer.')



HigherOrLower()