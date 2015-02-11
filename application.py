"""This game's purpose is to find the random number"""
import random #Imports the random function
#Starts the game while this variable is True (if anything is False, it will kill the game)
NEWGAME = True
while NEWGAME == True: #while the variable is true
    VALEATORY = random.randint(1, 20) #The game gives me a random number
    print VALEATORY #This helps me check the game and make trials
    COUNT = -1 #and starts the COUNT on -1 because up next it will be adding 1
    VALIDATE = True #initiate the second block that starts the game by asking the user a number
    while VALIDATE == True: #While this block is true,do the next thing
        COUNT += 1 #it adds a COUNT every time the loops goes on so it doesnt keep going eternally
        if COUNT < 4: #if the COUNT is below 4 do this (only if it is below four)
            try: #starts a probability for later to dismiss future user errors
                GUESS = input("Welcome, GUESS the number: ") #asks the user for a number
                if GUESS == VALEATORY: #this compare the GUESS as equal as the random number
                    print "You win!"
                    #another condition to run this part, so it can repeat later or be killed
                    ANSWER = False
                    while ANSWER == False: #while this condition is false, do the next:
                        print "Do you want to play again? y/n: "
                        PLAYAGAIN = raw_input('> ') #Ask the user for an answer
                        PLAYAGAIN = PLAYAGAIN.lower() #Makes the answer in lower caps
                        if PLAYAGAIN == "y": #If the answer is Y
                            ANSWER = True #kill my 1 variable and then it goes up
                            VALIDATE = False #kill my 2 variable and then it will start again
                        elif PLAYAGAIN == "n": #But if his answer is no
                            ANSWER = True #It will still kill my first
                            VALIDATE = False #Will kill my second
                            NEWGAME = False #And will kill my third variable so the game will stop
                            print "Good - Bye" #Very politely it will say goodbye to the user
                        else: #If my user does not press y or n
                            print "Invalid Option"
                #This next statement is a continuity of my if where he wins
                elif GUESS > VALEATORY: #this compare the GUESS as higher than the random number
                    print "You GUESSed too high, please try again"
                elif GUESS < VALEATORY: #this compare the GUESS as lower than the random number
                    print "You GUESSed too low, please try again"
            #if my user enters letters, the game will show him to enter only numbers
            except NameError: #This goes with the try
                print "Enter only numbers"
            except SyntaxError:
                print "Enter only numbers"
        #this continues my first if statement, if the COUNT is not below 4, the game will be over
        else:
            print "Game Over!"
            ANSWER = False #I still need to ask him if he wants to play again
            while ANSWER == False:
                print "Do you want to play again? y/n: "
                PLAYAGAIN = raw_input('> ')
                PLAYAGAIN = PLAYAGAIN.lower()
                if PLAYAGAIN == "y":
                    ANSWER = True
                    VALIDATE = False
                elif PLAYAGAIN == "n":
                    ANSWER = True
                    VALIDATE = False
                    NEWGAME = False
                    print "Good - Bye"
                else:
                    print "Invalid Option"
