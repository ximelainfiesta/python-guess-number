import random #Imports the random function

newgame = True #Starts the game while this variable is True (if anything is False, it will kill the game)

while newgame == True: #while the variable is true
	valeatory = random.randint(1,20) #The game gives me a random number
	print valeatory #This helps me check the game and make trials
	count = -1 #and starts the count on -1 because up next it will be adding 1
	
	validar = True #This helps me initiate the second block that starts the game by asking the user a number
	while validar == True: #While this block is true...do the next thing
		count += 1 #it adds a count every time the loops goes on so it doesnt keep going eternally
		if count < 4: #if the count is below 4 do this (only if it is below four)	
			try: #starts a probability for later to dismiss future user errors
				guess = input("Welcome, guess the number: ") #asks the user for a number
				if guess == valeatory: #this compare the guess as equal as the random number
					print "You win!" 

					respuesta = False #another condition to run this part of the game, so it can repeat later or be killed
					while respuesta == False: #while this condition is false, do the next:
						print "Do you want to play again? y/n: " 
						jugardenuevo = raw_input('> ') #Ask the user for an answer
						jugardenuevo = jugardenuevo.lower() #Makes the answer in lower caps
						if jugardenuevo == "y": #If the answer is Y
							respuesta = True #This will kill my first variable and then the game goes up
							validar = False #This will kill my second variable and then the game will start again
						elif jugardenuevo == "n": #But if his answer is no
							respuesta = True #It will still kill my first
							validar = False #Will kill my second
							newgame = False #And will kill my third variable so the game will stop
							print "Good - Bye" #Very politely it will say goodbye to the user
						else: #If my user does not press y or n, the game will tell him that he is not making the right choice
							print "Invalid Option"

					#This next statement is a continuity of my if where he wins, it helps me compare the variables with the <> symbols
				elif guess > valeatory: #this compare the guess as higher than the random number
					print "You guessed to high, please try again"
				elif guess < valeatory: #this compare the guess as lower than the random number
					print "You guessed to low, please try again"

			except NameError: #if my user enters letters, the game will show him to enter only numbers
				print "Enter only numbers"
			except SyntaxError: #if my user uses something else that is not numbers, it will ask him to do it
				print "Enter only numbers"

		else: #this continues my first if statement, if the count is not below 4, the game will be over
			print "Game Over!"
			respuesta = False #But I still need to ask him if he wants to play again, i copy the play again block
			while respuesta == False:
				print "Do you want to play again? y/n: "
				jugardenuevo = raw_input('> ')
				jugardenuevo = jugardenuevo.lower()
				if jugardenuevo == "y":
					respuesta = True
					validar = False
				elif jugardenuevo == "n":
					respuesta = True
					validar = False
					newgame = False
					print "Good - Bye"
				else:
					print "Invalid Option"



