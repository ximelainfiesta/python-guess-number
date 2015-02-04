import random

aleatorio = random.randint(1,20)
usuario = input("Welcome, guess the number: ")

if usuario > aleatorio:
	print "too high"
elif usuario < aleatorio:
	print "too low"

print aleatorio