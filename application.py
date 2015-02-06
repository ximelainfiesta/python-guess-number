import random #Imports the random function

newgame = True

while newgame == True: #it makes the loop go until 4
	valeatory = random.randint(1,20)
	print valeatory
	count = -1 #it helps the while statement to start the count in 0
	
	validar = True
	while validar == True:
		count += 1 #it adds a count every time the loops goes on so it doesnt keep going eternally
		if count < 4: 	
			try:
				guess = input("Welcome, guess the number: ") #asks the user for a number
				if guess == valeatory: #this compare the guess as equal as the random number
					print "You win!"
					respuesta = False
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

					#This next if statement helps me compare the variables with the <> and == symbols
				elif guess > valeatory: #this compare the guess as higher than the random number
					print "You guessed to high, please try again"
				elif guess < valeatory: #this compare the guess as lower than the random number
					print "You guessed to low, please try again"
		
				else: 
					pass

			except NameError:
				print "Enter only numbers"
			except SyntaxError:
				print "Enter only numbers"
		else:
			print "Game Over!"
			respuesta = False
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



