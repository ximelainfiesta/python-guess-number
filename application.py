import random #Imports the random function

aleatorio = random.randint(1,20) #generates a random number from 1 to 20
guess = input("Welcome, guess the number: ") #asks the user for a number

#This next if statement helps me compare the variables with the <> and == symbols
if guess > aleatorio: #this compare the guess as higher than the random number
	print "you guessed to high, please try again"
elif guess < aleatorio: #this compare the guess as lower than the random number
	print "you guessed to low, please try again"
elif guess == aleatorio: #this compare the guess as equal as the random number
	print "you win!"

print aleatorio #it helps me to verify that the machine is working and sending the correct answer according to the guess