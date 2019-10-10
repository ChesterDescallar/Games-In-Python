import random

def MathsChallenge():
    score = 0
    for x in range(10):
        compNumber1 = random.randint(1,10)
        compNumber2 = random.randint(1,10)
        compAnswer = compNumber1 * compNumber2
        print ('What is',compNumber1 , 'X' , compNumber2 , '?' )

        playerInput = input ('Answer :' )
        if playerInput.isdigit():
            playerInput = int(playerInput)


            if playerInput == compAnswer:
                print ('That is correct!')
                score = score + 1

            else:
                print ('That is incorrect!')
        else:
            print ('Invalid answer.')

MathsChallenge()


